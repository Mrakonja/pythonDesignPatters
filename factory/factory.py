# Example of a factory pattern. Implementation using factory method.

class Button(object):
   html = ""
   def get_html(self):
      return self.html

class Image(Button):
   html = "<img></img>"

class Input(Button):
   html = "<input></input>"

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():  #this is actuall factory method pattern
   def create_button(self, typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]()

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
   print(button_obj.create_button(b).get_html())

#The button class helps to create the html tags and the associated html page. The client will not have access to the logic of code and the output represents the creation of html page.


#example of practical usecase in real world, is django forms

from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100)
    birth_date = forms.DateField(required=False)

print(PersonForm)