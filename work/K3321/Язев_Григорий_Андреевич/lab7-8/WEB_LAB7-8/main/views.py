from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import Technique
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ContactMessage
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
def index(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Спасибо за сообщение!')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
def home(request):
    techniques = Technique.objects.all()
    return render(request, 'home.html', {'techniques': techniques})

def technique_detail(request, pk):
    technique = get_object_or_404(Technique, pk=pk)
    return render(request, 'technique_detail.html', {'technique': technique})

@login_required
def admin_messages(request):
    if not request.user.is_staff:
        return render(request, 'not_authorized.html')
    messages = ContactMessage.objects.order_by('-submitted_at')
    return render(request, 'admin_messages.html', {'messages': messages})
def is_admin(user):
    return user.is_staff
@login_required
@user_passes_test(is_admin)
def clear_messages(request):
    if request.method == "POST":
        ContactMessage.objects.all().delete()
        messages.success(request, "Все сообщения успешно удалены.")
    return redirect('admin_messages')
