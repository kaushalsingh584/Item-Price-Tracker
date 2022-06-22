from django.shortcuts import render
from .forms import UserRegistrationForm
from django.shortcuts import redirect


# Create your views here.

def register(request):
    if request.POST:
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        
    # if there is a get request or any other request the we provide the user with the new form
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request,'users/register.html',context)