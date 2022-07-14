from django.shortcuts import redirect, render
from . forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
# get the value of username and store it in this username variable
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulations ! Account has been created succesfully and you can Login with {username}')
            return redirect('login')
    else:          
# form is similar to centext variable we have used before
        form = UserRegisterForm()
       
    return render(request, 'users/register.html',{'form': form})
        
