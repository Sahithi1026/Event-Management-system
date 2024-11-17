from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from .forms import EventForm, RegistrationForm,RegistrationForms
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            try:
                # Check if user exists in the database
                User.objects.get(username=username)
                # If user exists but password is wrong, show an error
                return render(request, 'login.html', {'error': 'Invalid credentials'})
            except User.DoesNotExist:
                # Redirect to registration if user doesn't exist
                return redirect('register')
    return render(request, 'login.html')
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            # Create the user
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('login')
    else:
        form = RegistrationForms()
    return render(request, 'register.html', {'form': form})

@login_required
def home_view(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

@login_required
def create_event_view(request):
    if not request.user.is_superuser:
        return render(request, 'error.html', {"message": "Sorry this page is only for the admins"})
    
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.created_by = request.user
        event.save()
        return redirect('home')
    
    return render(request, 'create_event.html', {'form': form})

@login_required
def register_event_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'register_event.html', {'form': form, 'event': event})

@login_required
def profile_view(request):
    registrations = Registration.objects.filter(student_email=request.user.email)
    return render(request, 'profile.html', {'registrations': registrations})
@login_required
def unregister_event_view(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id, student_email=request.user.email)
    
    if request.method == 'POST':
        registration.delete()  # Remove the registration
        return redirect('profile')  # Redirect to the profile page after unregistration

    return render(request, 'unregister_event.html', {'registration': registration})