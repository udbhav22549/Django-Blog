from django.shortcuts import redirect, render
from django.views import View
from .forms import UserRegisterForm

class RegisterView(View):
    def get(self,request):
        form= UserRegisterForm()
        return render(request, 'users/register.html', {'form': form} )

    #store the data in database
    def post(self,request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
