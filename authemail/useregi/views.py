from .models import CustomUser
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.core import validators
from .forms import SignUpForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from .gmail_utils import gmail_send_message
import uuid
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Generate verification token
            user.verification_token = uuid.uuid4().hex
            user.save()

            verification_link = request.build_absolute_uri(
                reverse('verify_email', args=[user.verification_token])
            )
            send_verification_email(user.email, verification_link)
            messages.success(request, 'Registration successful! Please check your email to verify your account.')
            return redirect('email_check')
        else:
            post_email = request.POST.get('email')
            if CustomUser.objects.filter(email=post_email).exists():
                form.add_error('email', ValidationError("Email already exists"))
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})        

def email_check(request):
    return render(request, 'email_check.html')



def send_verification_email(recipient_email, verification_link):
    print("i am sumedha")
    email_sent = gmail_send_message(
        recipient_email=recipient_email,
        subject="Verify Your Email Address",
        message_body=f"Please verify your email by clicking on this link: {verification_link}"
    )
    if email_sent:
        print("Verification email sent successfully.")
    else:
        print("Failed to send verification email.")


# verify user email

def verify_email(request, token):
    try:
        user = CustomUser.objects.get(verification_token=token)
        user.is_verified = True
        user.email_verified = True
        user.verification_token = None
        user.save()
        return render(request, 'login.html')
    except CustomUser.DoesNotExist:
        return HttpResponse('Invalid verification link', status=400)
