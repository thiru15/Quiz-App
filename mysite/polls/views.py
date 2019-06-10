from django.http import HttpResponse

from django.shortcuts import render

from .models import Question
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
from django.utils import timezone
from django.urls import reverse



from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question,Correct


class IndexView(generic.ListView):
    model=Question

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[::-1]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# ...
def finish(request):

    #sc=selected_choice.votes
    sum=0
    for choice in Question.objects.all():
           sum+=int(choice.correct)

    sc=sum

    return render(request, "polls/finish.html",context={"sc":sc})

def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    selected_choice = question.choice_set.get(pk=request.POST['choice'])


    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:

        #return HttpResponse(question.correct)
        if str(selected_choice.choice_text)==str(selected_choice.answer):
            selected_choice.votes += 1
            selected_choice.save()
            question.correct+=1
            question.save()
            fl=True
            sc=selected_choice.votes
            #Correct.no_of_correct+=1
            #Correct.save()
            #return HttpResponse(sc)
            #return render(request,'polls/results.html',context={"fl":"fl" , "selected_choice":"selected_choice"})
            #finish(request,sc)
            #return render(request,'polls/results.html',context={"fl":"fl","sc":sc})
            #return HttpResponseRedirect(reverse('polls:results',context={"fl":"fl","selected_choice":"selected_choice"},args=(question.id,)))

        #return HttpResponse(str(selected_choice.choice_text)+"  "+str(selected_choice.answer))

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return render(request,'polls/index.html')
        #return HttpResponseRedirect(reverse('polls:index', args=(question.id,)))
