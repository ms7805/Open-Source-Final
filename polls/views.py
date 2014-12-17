
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from polls.forms import UserForm, UserProfileForm, QuestionForm, ChoiceForm, PictureForm
from polls.models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-modified_date')[:10]

class OldView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-modified_date')[11:]




class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class EditView(generic.DetailView):
    model = Question
    template_name = 'polls/edit.html'

def tagView(request):
    tags = request.POST['tag']
    question_with_tag = Question.objects.filter(tag=tags)
    context = {'question_with_tag':question_with_tag}
    return render(request, 'polls/index.html',context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@login_required()
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/polls/')
            #return IndexView(request)
        else:
            print form.errors
    else:
        form = QuestionForm(user=request.user);
    return render(request, 'polls/add_question.html',{'form': form})

def photo_upload(request):
     if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/polls/')
        else:
            print form.errors
     else:
        form = PictureForm()
     return render(request, 'polls/add_photo.html',{'form': form})

@login_required()
def add_choice(request):
     if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/polls/')
            #return IndexView(request)
        else:
            print form.errors
     else:
        form = ChoiceForm()
     return render(request, 'polls/add_choice.html',{'form': form})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.date_modified = timezone.now()
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def vote2(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes -= 1
        selected_choice.date_modified = timezone.now()
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def edit_q(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    if p.user.user.username == request.user.username:
        data = request.POST['body']
        p.question_text = data
        p.modified_date = timezone.now()
        p.save();
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    else:
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You are not the creator of the question.",
        })
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
def edit_a(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        a = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        if p.user.user.username == request.user.username:
            data = request.POST['body']
            a.choice_text = data
            a.modified_date = timezone.now()
            a.save();
            return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        else:
            return render(request, 'polls/detail.html', {
                'question': p,
                'error_message': "You are not the creator of the answer.",
            })
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/polls/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponseRedirect('/polls/')

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'polls/login.html', {})

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'polls/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/polls/')