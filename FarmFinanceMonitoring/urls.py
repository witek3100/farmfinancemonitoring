"""FarmFinanceMonitoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from finance_monitor.views import (yearly_settlement, invoices, flocks,
                                   home, download_raport, create_invoice,
                                   add_flock, delete_flock, end_flock, flock, invoice)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("yearly_settlement/", yearly_settlement, name="yearly_settlement"),
    path("invoices/", invoices, name="invoices"),
    path("flocks/", flocks, name="flocks"),
    path("download_raport", download_raport, name="download_raport"),
    path("add_invoice", create_invoice, name="add_invoice"),
    path("add_flock", add_flock, name="add_flock"),
    path('delete_flock/<int:flock_id>', delete_flock),
    path('end_flock/<int:flock_id>', end_flock),

    path('flock/<int:flock_id>', flock),

    path('invoice/<int:invoice_id>', invoice),
]
