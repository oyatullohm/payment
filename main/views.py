from django.shortcuts import render , redirect
from django.views import View
from .models import Payment , Customer
import datetime

online_month = datetime.datetime.now()
class HomeView(View):
    def get(self,request):
        month = str(online_month.month)
        summa = 0
        payment =  Payment.objects.filter(month=month).prefetch_related('customer')
        for i in payment:
            summa += i.summa
        context = {
            'customer':Customer.objects.all().order_by('paid'),
            'payment':payment,
            'summa':summa}
        return render (request ,'index.html',context)
    def post(self,request):
        id = request.POST.get('id')
        sum = request.POST.get('sum')
        month = request.POST.get('month')
        if month == '0':
            month = str(online_month.month)
        customer = Customer.objects.get(id=int(id))
        payment =  Payment.objects.create(customer=customer,month=month , summa=sum)
        if int(payment.summa )== int(customer.summa):
            customer.paid = True
            customer.save()
        return redirect('main:home')

class CreateCustomerView(View):
    def post(self ,request):
        name = request.POST.get('name')
        summa = request.POST.get('sum')
        Customer.objects.create(name=name,summa=summa)
        return redirect('main:home')


class MonthDetailView(View):
    def get(self,request,pk):
        month = str(pk)
        summa = 0
        payment =  Payment.objects.filter(month=month).prefetch_related('customer')
        for i in payment:
            summa += i.summa
        context = {
            'customer':Customer.objects.all().order_by('paid'),
            'payment':payment,
            'summa':summa}
        return render (request ,'detail_month.html',context)


class UpdatePaymentView(View):
    def post(self,request,pk):
        py = Payment.objects.get(id=int(pk))
        sum = request.POST.get('sum')
        py.summa = sum
        py.save()
        return redirect('main:home')

class UpdateCustomerSummaView(View):
    def post(self,request,pk):
        customer = Customer.objects.get(id=int(pk))
        sum = request.POST.get('sum')
        customer.summa = sum
        customer.save()
        return redirect('main:home')

def refresh(request):
    customer = Customer.objects.all()
    for i in customer:
        i.paid = False
        i.save()
    return redirect('main:home')