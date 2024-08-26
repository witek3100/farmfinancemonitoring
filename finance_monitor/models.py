from datetime import timezone
from enum import Enum

from django.db import models


class InvoiceCategory(Enum):
    BREEDING_START = 1, "wystawienie kur"
    FORAGE = 2, "pasza"
    WATER = 3, "woda"
    ELECTRICITY = 4, "prąd"
    DRUGS = 5, "leki"
    WET = 6, "weterynaz"
    UTILIZATION = 7, "utylizacja"
    GAS = 8, "gaz"
    DISINFECTION = 9, "dezynfekcja"
    INSURANCE = 10, "ubezpieczenie budynków"

    @staticmethod
    def get_all():
        return [c.value for c in InvoiceCategory]


class InvoiceType(Enum):
    INCOME = 1, "przychod"
    EXPENSE = 2, "wydatek"

    @staticmethod
    def get_all():
        return [c.value for c in InvoiceType]


class ForageType(Enum):
    STARTER = 1, "starter"
    GROWLER = 2, "growler"
    FINISHER = 3, "finisher"

    @staticmethod
    def get_all():
        return [c.value for c in ForageType]


class Flock(models.Model):
    number = models.AutoField(primary_key=True)
    date_start = models.DateField(auto_now_add=True)
    data_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Rzut numer {self.number}'

class Invoice(models.Model):
    date = models.DateField(help_text='Data wystawienia faktury')
    cost = models.DecimalField(max_digits=10, decimal_places=2, help_text='Łączna kwota')
    type = models.IntegerField(choices=InvoiceType.get_all(), help_text='Typ (Koszt/Przychód)')
    invoice_number = models.CharField(max_length=50, help_text='Numer faktury')
    category = models.IntegerField(choices=InvoiceCategory.get_all(), help_text='Kategoria')
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE, help_text='Rzut')
    amount = models.IntegerField(default=None, null=True, help_text='Ilość')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True, help_text='Cena jednostkowa')
    water_usage = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True, help_text='Zużycie wody')
    forage_type = models.IntegerField(choices=ForageType.get_all(), help_text='Typ paszy', null=True)
    payment_deadline = models.DateField(help_text='Termin zapłaty', null=True)
    drug_name = models.CharField(null=True, help_text='Nazwa leku', max_length=50)

