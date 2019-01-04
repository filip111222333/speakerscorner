from django import utils
from konferencija.settings import EMAIL_HOST
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

def send_mail_to(instance):
    #Security mesures creation of custom token and uid
    token = default_token_generator.make_token(instance)
    uid = utils.http.urlsafe_base64_encode(utils.encoding.force_bytes(instance.pk))
    uid = uid.decode("utf-8")
    #Sending mail
    from_email = EMAIL_HOST
    message = 'http://127.0.0.1:8000/users/validate/'+ uid + '/' + token +'/'
    send_mail('Registration',message,from_email,[instance.email],fail_silently=False,)
