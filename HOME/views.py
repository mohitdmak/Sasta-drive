from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import FileForm
from .models import Through

#function-based view to direct the user to the home page
def home(request):
    # If user is logged in, we need the socialaccount object to display or post the form to upload files,
    # since the FileObject model is connected with the SocialAccount via Through model. 
    if request.user.is_authenticated:
        djangouser = request.user
        if request.method == 'POST':
            # Adding a 'request.FILES' parameter to capture the file which the user had uploaded.
            form = FileForm(request.POST, request.FILES)
            # Checking if the SocialAccount User already has a Through model created for FileObject,
            # If created, directly linking it with the form instance, else creating the Through model first, and then linking it.
            # After the File is saved to the database, redirecting the user to the home page.
            if form.is_valid():
                if Through.objects.filter(ForUser = djangouser).exists():
                    form.instance.UserThrough = djangouser.filemodels
                    form.save()
                    return redirect('home')
                else:
                    Through.objects.create(ForUser = djangouser)
                    form.instance.UserThrough = djangouser.filemodels
                    form.save()
                    return redirect('home')
        # If get request, we still need to ensure that the Through model exists for the logged in user as we need it to,
        # access the files that the user has uploaded and display them
        else:
            if Through.objects.filter(ForUser = djangouser).exists():
                return render(request, 'home.html', {'f_form': FileForm, 'files':djangouser.filemodels.files.all()})
            else:
                Through.objects.create(ForUser = djangouser)
                return render(request, 'home.html', {'f_form': FileForm, 'files':djangouser.filemodels.files.all()})
    # In this case, the user is logged out, and thus he would not see the File Uploading Form or Files uploaded
    # Here the user can only access the logging in button.
    else:
        return render(request, 'home.html')