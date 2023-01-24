import logging
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from NewTrip.celery import app
from NewTrip.settings import EMAIL_HOST_USER

@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            subject=f'Подтверждение аккаунта "{user.username}"',
            message=f"Для подтверждения аккаунта, перейдите по ссылке:\nhttp://localhost:1337{reverse('verify', kwargs={'uuid': str(user.verification_uuid)})}",
            from_email=EMAIL_HOST_USER,
	    recipient_list=[user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:

        logging.warning(f"Tried to send verification email to non-existing user '{user_id}'")
