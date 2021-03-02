from django.shortcuts import redirect, render
from allauth.socialaccount.models import SocialAccount
from .forms import FileForm
from .models import Through

def home(request):
    if request.user.id:
        djangouser = request.user
        socialaccuser = SocialAccount.objects.filter(user = djangouser)[0]
        if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    socialaccuser.filemodels
                except:
                    Through.objects.create(ForUser = socialaccuser)
                else:
                    pass
                finally:
                    form.instance.UserThrough = socialaccuser.filemodels
                    form.save()
                    return redirect('home')
        else:
            try:
                socialaccuser.filemodels
            except:
                Through.objects.create(ForUser = socialaccuser)
            else:
                pass
            finally:
                return render(request, 'home.html', {'f_form': FileForm, 'files':socialaccuser.filemodels.files.all()})
    else:
        return render(request, 'home.html')

