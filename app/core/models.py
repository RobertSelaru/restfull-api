from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

'''Section 7: Configure Django custom user model'''
class BaseUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        '''Create and save a new user'''
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''Custom user model that supports using email instead of username'''
    pass