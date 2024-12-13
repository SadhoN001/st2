from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UsersForm
from .models import TodoItem, Service

# Create your views here.
def homepage(request):
    serviceData=Service.objects.all()
    data={
        'title': "homepage-skd",
        'name':'Sadhon Kumar Dev',
        'list': ['a','b', 'c', 'd', 'e'],
        'stn':[
            {'name':'skd', 'phone':'015834420'},
            {'name':'jkd', 'phone':'9983434375'},
        ],
        'serviceData':serviceData 
        
    }
    return render(request, 'index.html', data)

def portfol(request):
    return render(request, 'index1.html')

def about_us(request):
    if request.method == "GET":
        output= request.GET.get("output")
    return render(request, 'about-us.html', {'output':output})

def userform(request):
    totalans=0
    fn=UsersForm()
    data={'form':fn,}
    try:
        # n1= int(request.GET['num1'])
        # n2= int(request.GET['num2'])
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            totalans = n1 + n2
            # print(totalans)
            
            data={
                'n1':n1,
                'n2':n2,
                'output':totalans,
                'form':fn,
            }
            url= "/food/about-us/?output={}".format(totalans)
            return redirect(url)
    except:
        pass 
    
    # return render(request, 'userform.html', {'output': totalans})
    return render(request, 'userform.html',data)

def submitform(request):
    try:
        # n1= int(request.GET['num1'])
        # n2= int(request.GET['num2'])
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            totalans = n1 + n2
            # print(totalans)
            
            data={
                'n1':n1,
                'n2':n2,
                'output':totalans,
            }
            # url= "/food/about-us/?output={}".format(totalans)
            # return redirect(url)
            return HttpResponse(totalans)
    except:
        pass
    
def calculator(request):
    c=''
    try:
        if request.method == 'POST':
            n1= eval(request.POST.get('num1'))
            n2= eval(request.POST.get('num2'))
            opr= request.POST.get('opr')
            if opr == '+':
                c=n1+n2
            elif opr == '-':
                c=n1-n2
            elif opr == '*':
                c=n1*n2
            elif opr == '/':
                c=n1/n2
            
    except:
        c="invalid operation...."
    
    return render(request, 'calculator.html',{'c':c})

def evanodd(request):
    c=''
    if request.method == 'POST':
        if request.POST.get('num1')== "":
            return render(request,'evanodd.html',{'error':True})
                          
        n1= eval(request.POST.get('num1'))
        if n1%2==0:
            c="Evan Number"
        else:
            c="Odd Number"
    return render(request,'evanodd.html',{'c':c})

def todos(request):
    item= TodoItem.objects.all()
    return render(request, "todos.html", {'todos':item})