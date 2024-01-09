from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Submit
from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()

		self.helper.form_method = 'post'
		self.helper.form_action = '/contact/'
		self.helper.form_class = "form-group"
		self.helper.form_id = 'contact-form'

		self.helper.add_input(Submit('submit', 'Submit'))

	name = forms.CharField(max_length=100, label="Your name", widget=forms.TextInput(attrs={'class': 'col', 'placeholder':'Charlie Kelly'}))
	email = forms.CharField(label="Your email", widget=forms.EmailInput(attrs={'class': 'col', 'placeholder':'rat_king@kittenmittons.com'}))
	message = forms.CharField(max_length=500, label="Your inquiry", widget=forms.Textarea(attrs={'placeholder':"Now let's talk about the mail. Can we talk about the mail, please, Mac? I've been dying to talk about the mail with you all day, OK? \"Pepe Silvia,\" this name keeps coming up over and over again. Every day Pepe's mail is getting sent back to me. Pepe Silvia! Pepe Silvia! I look in the mail, and this whole box is Pepe Silvia! So I say to myself, \"I gotta find this guy! I gotta go up to his office and put his mail in the guy's godd*mn hands! Otherwise, he's never going to get it and he's going to keep coming back down here.\" So I go up to Pepe's office and what do I find out, Mac? What do I find out?! There is no Pepe Silvia. The man does not exist, okay? So I decide, \"Oh sh*t, buddy, I gotta dig a little deeper.\" There's no Pepe Silvia? You gotta be kidding me! I got boxes full of Pepe! All right. So I start marchin' my way down to Carol in HR and I knock on her door and I say, \"Carol! Carol! I gotta talk to you about Pepe.\" And when I open the door what do I find? There's not a single godd*mn desk in that office! There...is...no...Carol in HR. Mac, half the employees in this building have been made up. This office is a godd*mn ghost town."}))
