from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render,redirect
from testapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from testapp.models import Quiz1,Profile,Choice,Quiz2,Choice2,Profile1,Profile2
l=[];sum1=0;sum2=0;sum=0;l1=[]
count=0
count1=0

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
   return render(request,'home.html')


@login_required
def user_logout(request):
    logout(request)
    return render(request,'index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            user.is_active = False
            #profile = profile_form.save(commit=False)
            #profile.user = user
            #profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your quiz account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            #return HttpResponse(to_email)
            email.send()
            return render(request,'acc_active_sent.html')
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def activate(request, uidb64, token):
         try:
             uid = force_text(urlsafe_base64_decode(uidb64))
             user = User.objects.get(pk=uid)
             #return HttpResponse(user)
         except(TypeError, ValueError, OverflowError, User.DoesNotExist):
               user = None
         user.is_active = True
         user.save()
         login(request, user)
                  # return redirect('home')
         return render(request,'login.html',{'user_login':user_login})

def user_login(request):
           if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user:
                    if user.is_active:

                          login(request,user)
                          return render(request,'home.html')
                    else:
                          return HttpResponse("Your account was inactive.")
                else:
                    print("Someone tried to login and failed.")
                    print("They used username: {} and password: {}".format(username,password))
                    return HttpResponse("Invalid login details given")
           else:
                 return render(request, 'login.html', {})
def finish1(request,user_id):

    #Profile.user=use.username
    #Profile.save()
    global sum1
    
    sc=sum1
    #return HttpResponse(Profile.objects.all())
    c = User.objects.get(pk=user_id)
    
    pr=Profile1()
    pr.user=c
    pr.scores=sum1

    global count
    if count==0:
         pr.save()
         count+=1


    pro=Profile2.objects.all()


    '''for use in User.objects.all():
        use.scores+=sum
        use.scores.save()
        break'''
    return render(request, "finish1.html",context={"sc":sc,"pro":pro})

def finish2(request,user_id):

    #Profile.user=use.username
    #Profile.save()
    
    #return HttpResponse(Profile.objects.all())
    c = User.objects.get(pk=user_id)
    pr = Profile2()
    global sum2
    pr.user=c
    pr.scores=sum2
    sc=sum2
    global count1
    if count1==0:
         pr.save()
         count1+=1


    pro=Profile2.objects.all()


    '''for use in User.objects.all():
        use.scores+=sum
        use.scores.save()
        break'''
    return render(request, "finish2.html",context={"sc":sc,"pro":pro})
def finish(request,user_id):

    #Profile.user=use.username
    #Profile.save()
    
   
    pre=Profile2.objects.all()
    b=int()
    sum=sum2+sum1
    sc=sum
    #return HttpResponse(Profile.objects.all())
    c = User.objects.get(pk=user_id)
    pr = Profile()
    pr.user=c
    pr.scores=sum
    pr.save()
    pro=Profile.objects.all()


    '''for use in User.objects.all():
        use.scores+=sum
        use.scores.save()
        break'''
    return render(request, "finish.html",context={"sc":sc,"pro":pro})

@login_required
def quiz1(request):
    latest_question_list = Quiz1.objects.all()
    return render(request,'quiz1.html',context={"latest_question_list":latest_question_list})


@login_required
def quiz2(request):
    latest_question_list = Quiz2.objects.all()
    return render(request,'quiz2.html',context={"latest_question_list":latest_question_list})


def vote1(request, question_id):
    question = get_object_or_404(Quiz1, pk=question_id)
    #return HttpResponse(question.correct)
    #choice=Choice1.objects.all()            
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #choice=request.POST.get('a')
        #a=1
    except (KeyError, Quiz1.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'index.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        s=question.correct
        #return HttpResponse(selected_choice.choice_text)
        #return HttpResponse(l)
        global sum1
        if question not in l:
                if str(selected_choice.choice_text)==str(s):
                   fl=True
                    
                   sum1+=1
                   l.append(question)

        sc=sum1
            #return HttpResponse("Thank You")
            #return render(request,'polls/results.html',context={"fl":"fl" , "selected_choice":"selected_choice"})
            #finish(request,sc)
        #return render(request,'quiz1.html',context={"choices":choices})
        return render(request,'results.html',context={"sc":sc})

def vote2(request, question_id):
    question = get_object_or_404(Quiz2, pk=question_id)
    #return HttpResponse(question.correct)
    #choice=Choice1.objects.all()            
    selected_choice = question.choice2_set.get(pk=request.POST['choice'])
    try:
        selected_choice = question.choice2_set.get(pk=request.POST['choice'])
        #choice=request.POST.get('a')
        #a=1
    except (KeyError, Quiz2.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'index.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        s=question.correct
        #return HttpResponse(selected_choice.choice_text)
        #return HttpResponse(l)
        global sum2
        if question not in l:
                if str(selected_choice.choice_text)==str(s):
                   fl=True 
                   sum2+=1
                   l.append(question)

        sc=sum2
            #return HttpResponse("Thank You")
            #return render(request,'polls/results.html',context={"fl":"fl" , "selected_choice":"selected_choice"})
            #finish(request,sc)
        #return render(request,'quiz1.html',context={"choices":choices})
        return render(request,'results.html',context={"sc":sc})


       

