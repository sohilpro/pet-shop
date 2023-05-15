from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import AccessToken


# @receiver(post_save, sender=User)
# def create_jwt_token(sender, instance, created, **kwargs):
#     if created:
#         token = AccessToken.for_user(instance)
#         print(token)
#         instance.jwt_token = str(token)
#         print(str(token))
#         instance.save()



#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxODM2NDI1LCJpYXQiOjE2ODE4MzYxMjUsImp0aSI6IjBjNTU1MjUwZWI1YTRmZmY5NGU2YzA4ODE4Mjc3MDZlIiwidXNlcl9pZCI6MX0.Lcu233yQx4I2YL-c0RbGOJzytglXnTJX98mgcLRVehk
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxODM2NDI1LCJpYXQiOjE2ODE4MzYxMjUsImp0aSI6IjBjNTU1MjUwZWI1YTRmZmY5NGU2YzA4ODE4Mjc3MDZlIiwidXNlcl9pZCI6MX0.Lcu233yQx4I2YL-c0RbGOJzytglXnTJX98mgcLRVehk
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxODM2NDcxLCJpYXQiOjE2ODE4MzYxNzEsImp0aSI6IjRiMTNiNTQyNjFjZTRjZTM4MTRlMzYzZjdiNzczMWU2IiwidXNlcl9pZCI6MX0.zIqAjhFnEWQ2zBXkhr-aGqD8ayyPSW7y5UIKXmyuZ3g