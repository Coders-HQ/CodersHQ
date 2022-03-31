from django import template

register = template.Library()

@register.filter
def remove_sym(value):
	response = value.replace("_"," ")
	response = response.replace("{","")
	response = response.replace("}","")
	return response