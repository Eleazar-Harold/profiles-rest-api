from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """helps django work with our custom user model"""
    def create_user(self, email, name, password=None):
        """create a new user profile object"""
        if not email:
            raise ValueError("users must have an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """creates and saves a new super user with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a 'user profile' inside our system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """used to get a user's full name."""
        return self.name

    def get_short_name(self):
        """used to get a user's short name"""
        return self.name

    def __str__(self):
        """django uses this when it need to convert the object into a string"""
        return self.email 