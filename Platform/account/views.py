from django.shortcuts import render, redirect,render_to_response,Http404
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm,RegistrationForm
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
import re
from .models import Product,CoverImage,Misc,MiscCoverImage
from django.template import RequestContext



"""def Login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        btn="Login"
        if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                login(request, user)
               #user.emailconfirmed.active_user_email()
                return render_to_response("login.html", {'form':form,"submit_btn": btn})

        else:
            return HttpResponse("Invalid details...")
    else:
    	form=LoginForm()
    	return render_to_response("login.html",{'form':form})"""


def Login(request):
    templatename="login.html"
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)                #return HttpResponse("This User is valid, active and authenticated")
            return HttpResponseRedirect("/")

        else:
            return HttpResponse("not a valid user")

    return render(request,templatename,{})



def Logout(request):
    logout(request)
    messages.success(request, "Successfully Logged out. Feel free to login again.")
    #return HttpResponseRedirect('%s'%(reverse("Login")))
    return HttpResponseRedirect('/login/')




def registration_view(request):
    form = RegistrationForm(request.POST or None)
    btn = "Join"
    if form.is_valid():
        new_user = form.save(commit=False)
        # new_user.first_name = "Justin" this is where you can do stuff with the model form
        new_user.save()
        messages.success(request, "Successfully Registered. Please confirm your email now.")
        return HttpResponseRedirect("/")
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username=username, password=password)
        # login(request, user)

    context = {
             "form": form,
             "submit_btn": btn,
    }
    return render(request, "register.html", context)



"""def registration_view(request):
    if request.method == 'POST':

        captcha_error = ""
        captcha_response = captcha.submit(
	    request.POST.get("recaptcha_challenge_field", None),
	    request.POST.get("recaptcha_response_field", None),
	    settings.RECAPTCHA_PRIVATE_KEY,
	    request.META.get("REMOTE_ADDR", None))
        if not captcha_response.is_valid:
            captcha_error = "&error=%s" % captcha_response.error_code
            c = {}
            c.update(csrf(request))
            c['repetir'] = True
            c['header'] = "register"
            return render_to_response('register.html', c, context_instance=RequestContext(request))
        else:
            if error_register(request):
                c = {}
                c.update(csrf(request))
                c['repetir'] = True
                c['header'] = "register"
                return render_to_response('register.html', c, context_instance=RequestContext(request))
            else:
                username = clean_username(request.POST['user'])
                password = request.POST['password']
                email = request.POST['email']
                user = User.objects.create_user(username, email, password)
                user.is_active = False
                user.save()
                confirmation_code = ''.join(tehrandom.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33))
                p = Profile(user=user, confirmation_code=confirmation_code)
                p.save()
                send_registration_confirmation(user)
                return HttpResponseRedirect('../../../../../')
    else:
        c = create_c(request)
        c['header'] = "register"
        return render_to_response('register.html', c, context_instance=RequestContext(request))


def send_registration_confirmation(user):
    p = user.get_profile()
    title = "Gsick account confirmation"
    content = "http://www.gsick.com/confirm/" + str(p.confirmation_code) + "/" + user.username
    send_mail(title, content, 'no-reply@gsick.com', [user.email], fail_silently=False)


def confirm(request, confirmation_code, username):
    try:
        user = User.objects.get(username=username)
        profile = user.get_profile()
        if profile.confirmation_code == confirmation_code and user.date_joined > (datetime.datetime.now()-datetime.timedelta(days=1)):
            user.is_active = True
            user.save()
            user.backend='django.contrib.auth.backends.ModelBackend'
            auth_login(request,user)
        return HttpResponseRedirect('../../../../../')
    except:
        return HttpResponseRedirect('../../../../../')


def error_register(request):
    username = request.POST['user']
    password = request.POST['password']
    email = request.POST['email']
    if not clean_username(username):
        return True
    if username.replace(" ", "") == "" or password.replace(" ", "") == "":
        return True
    if len(username) > 15 or len(password) > 50:
        return True
    if not "@" in email:
        return True
    try:
        if User.objects.get(username=username):
            return True
    except:
        pass
"""





















































SHA1_RE = re.compile('^[a-f0-9]{40}$')

def activation_view(request, activation_key):
    if SHA1_RE.search(activation_key):
        print "activation key is real"
        try:
            instance = EmailConfirmed.objects.get(activation_key=activation_key)
        except EmailConfirmed.DoesNotExist:
            instance = None
            messages.success(request, "There was an error with your request.")
            return HttpResponseRedirect("/")
        if instance is not None and not instance.confirmed:
            page_message = "Confirmation Successful! Welcome."
            instance.confirmed = True
            instance.activation_key = "Confirmed"
            instance.save()
            messages.success(request, "Successfully Confirmed! Please login.")

        elif instance is not None and instance.confirmed:
            page_message = "Already Confirmed"
            messages.success(request, "Already Confirmed.")
        else:
            page_message = ""

        context = {"page_message": page_message}
        return render_to_response("activation_complete.html", context)

    else:
		raise Http404









def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/logout/')
        else:
            return
            return HttpResponse("please check the credentials again")
            #messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
   # return render(request, 'accounts/change_password.html', {
       # 'form': form
        return render(request, 'change_password.html', {
       'form': form
    })



def rent(request):
    images=CoverImage.objects.all()
    product=Product.objects.all()
    count=len(product)

    return render_to_response("rent.html", {'product':product,'images':images,'count':count},context_instance=RequestContext(request))


def misc(request):
    images1=MiscCoverImage.objects.all()
    product1=Misc.objects.all()
    count1=len(product1)

    return render_to_response("misc.html", {'product1':product1,'images1':images1,'count1':count1},context_instance=RequestContext(request))


def contact(request):
	context = {}
	template = "contact.html"
	return render(request, template, context)

def rent_search(request):
    try:
        q=request.GET.get('q')
    except:
        None
    if q:
        products=Product.objects.filter(Q(name__icontains=q) )
        count=len(products)
        context={'query':q,'products':products,'count':count}
        template_name="search.html"
        return render_to_response(template_name,context)
    else:
        return HttpResponseRedirect('/')
