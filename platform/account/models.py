from django.db import models

from django.contrib.auth.models import User
import os.path
import urllib,hashlib
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.urlresolvers import reverse


class Profile(models.Model):
    user=models.OneToOneField(User)


    def __unicode__(self):
            return self.user.username

    def get_picture(self):
        try:
            filename = settings.MEDIA_ROOT + '/profile_pictures/' + self.user.username + '.jpg'
            picture_url = settings.MEDIA_URL + 'profile_pictures/' + self.user.username + '.jpg'
            if os.path.isfile(filename):
                return picture_url
            else:
                gravatar_url = u'http://www.gravatar.com/avatar/{0}?{1}'.format(
                    hashlib.md5(self.user.email.lower()).hexdigest(),
                    urllib.urlencode({'d':no_picture, 's':'256'})
                    )
                return gravatar_url
        except Exception, e:
            return no_picture

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username












class UserStripe(models.Model):
	user = models.OneToOneField(User)
	stripe_id = models.CharField(max_length=120)

	def __unicode__(self):
		return str(self.stripe_id)    



class EmailConfirmed(models.Model):
	user = models.OneToOneField(User)
	activation_key = models.CharField(max_length=200)
	confirmed = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.confirmed)

	def activate_user_email(self):
		#send email here & render a string
		activation_url = "%s%s" %(settings.SITE_URL, reverse("activation_view", args=[self.activation_key]))
		context = {
			"activation_key": self.activation_key,
			"activation_url": activation_url,
			"user": self.user.username,
		}
		message = render_to_string("accounts/activation_message.txt", context)
		subject = "Activate your Email"
		self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

	def email_user(self, subject, message, from_email=None, *kwargs):
		send_mail(subject, message, from_email, [self.user.email], kwargs)




class Product(models.Model):
    title = models.CharField(max_length=120,default='')
    name = models.CharField(max_length=255)
    #slug = models.SlugField(max_length=255)
    author = models.CharField(max_length=120,default='')
    #price = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/products1")



class CoverImage(models.Model):
	image=models.ImageField(upload_to="images/ritu1")





class Misc(models.Model):
    title1 = models.CharField(max_length=120,default='')
    name1 = models.CharField(max_length=255)
    #slug = models.SlugField(max_length=255)
    price1 = models.CharField(max_length=120,default='')
    #price = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to="images/misc")


class MiscCoverImage(models.Model):
	image1=models.ImageField(upload_to="images/miscCover")

