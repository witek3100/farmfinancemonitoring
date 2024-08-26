from datetime import date

from django.shortcuts import render, redirect
from django.contrib import messages
from finance_monitor.models import InvoiceType, Invoice, Flock
from .forms import InvoiceForm

def home(request):
    return render(request, 'finance_monitor/home.html')

def yearly_settlement(request):

    income_invoices = Invoice.objects.filter(type=1)
    expense_invoices = Invoice.objects.filter(type=2)

    total_income = sum(invoice.cost for invoice in income_invoices)
    total_expenses = sum(invoice.cost for invoice in expense_invoices)

    context = {
        'total_income': sum(invoice.cost for invoice in income_invoices),
        'total_expenses': sum(invoice.cost for invoice in expense_invoices),
        'balance': total_income - total_expenses,
        'total_invoices': len(income_invoices) + len(expense_invoices),
        'total_flocks': Flock.objects.count()
    }

    return render(request, 'finance_monitor/yearly_settlement.html', context)

def invoices(request):
    expenses = Invoice.objects.filter(type=2)
    incomes = Invoice.objects.filter(type=1)
    context = {
        'expenses': expenses,
        'incomes': incomes,
    }
    return render(request, 'finance_monitor/invoices.html', context)

def flocks(request):
    flocks_in_progress = Flock.objects.filter(data_end__isnull=True)
    flocks_done = Flock.objects.filter(data_end__isnull=False)
    return render(request, 'finance_monitor/flocks.html', {
        'flocks_in_progress': flocks_in_progress,
        'flocks_done': flocks_done,
    })

def download_raport(request):
    return None

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoices')
    else:
        form = InvoiceForm()

    return render(request, 'finance_monitor/invoice_form.html', {'form': form})

def add_flock(request):
    flock = Flock(date_start=date.today())
    flock.save()
    flock_id = flock.pk
    return redirect(f'flock/{flock_id}')

def delete_flock(request, flock_id):
    flock = Flock.objects.get(pk=flock_id)
    flock.delete()
    return redirect('flocks')

def end_flock(request, flock_id):
    flock = Flock.objects.get(pk=flock_id)
    flock.data_end = date.today()
    flock.save()
    return redirect('flocks')

def flock(request, flock_id):
    flock = Flock.objects.get(pk=flock_id)
    invoices = Invoice.objects.filter(flock=flock)
    return render(request, 'finance_monitor/flock.html', {'invoices': invoices, 'flock': flock.pk})

def invoice(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)
    return render(request, 'finance_monitor/invoice.html', {'invoice': invoice})
