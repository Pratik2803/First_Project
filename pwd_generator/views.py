from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'pwd_generator/home.html')


def password(request):
    list_a = list('abcdefghijklmnopqrstuvwxyz')
    thepassword=''
    length = int(request.GET.get('length'))

    Upper = request.GET.get('upper_case')
    if Upper == 'upper_case':
        list_a= list_a + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    special_chars = request.GET.get('special')
    if special_chars == 'special':
        list_a += list('!@#$%^&*()_+')

    No = request.GET.get('number')

    if No == 'number':
        list_a+=list('1234567890')

    for x in range(length):
        thepassword += random.choice(list_a)

    return render(request,'pwd_generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'pwd_generator/about.html')

