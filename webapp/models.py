# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.db.models import signals
from django.dispatch import dispatcher
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.IntegerField(u'phone', max_length=15, help_text='', blank=True, null=True,)
    mobile = models.IntegerField(u'mobile', max_length=15, help_text='', blank=True, null=True,)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = u'Profil'
        verbose_name_plural = u'Profily'

@receiver(post_save, sender=User)
def handle_user_save(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        #exclude = ['user',]
        fields = '__all__' # Or a list of the fields that you want to include in your form
        widgets = {'user': forms.HiddenInput()}


        # widgets = {
        #     'jmeno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zadej jméno'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zadej email'}),
        #     'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Případně zadej telefonní číslo'}),
        #     'zprava': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Napiš zprávu', 'rows': '10', 'cols': '40'}),
        # }
