from django.shortcuts import render, get_object_or_404
from .models import Property
from django.contrib import messages
from .forms import ContactForm,VisitRequestForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.shortcuts import redirect


def property_list(request):
    properties = Property.objects.all()

    # فیلتر با پارامترهای GET
    location = request.GET.get('location')
    prop_type = request.GET.get('type')
    max_price = request.GET.get('max_price')

    if location:
        properties = properties.filter(location__icontains=location)
    if prop_type:
        properties = properties.filter(type=prop_type)
    if max_price:
        properties = properties.filter(price__lte=max_price)

    return render(request, 'listings/property_list.html', {'properties': properties})


def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    return render(request, 'listings/property_detail.html', {'property': property_obj})

def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # در اینجا می‌تونی پیام رو ایمیل کنی یا ذخیره کنی
            messages.success(request, "Your message has been sent successfully!")
            form = ContactForm()  # فرم رو خالی کن بعد ارسال موفق

    return render(request, 'listings/contact.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ورود خودکار بعد ثبت‌نام
            return redirect('property_list')
    else:
        form = UserCreationForm()
    return render(request, 'listings/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    form = VisitRequestForm()

    if request.method == 'POST':
        form = VisitRequestForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.property = property_obj
            visit.save()
            messages.success(request, "Your visit request has been submitted.")
            form = VisitRequestForm()

    return render(request, 'listings/property_detail.html', {
        'property': property_obj,
        'form': form
    })




def test(request):
    return render(request,'listings/test.html')