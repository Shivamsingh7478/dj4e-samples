from django import template
import hashlib

register = template.Library()

@register.filter(name='gravatar')
def gravatar(user, size=40):
    email = user.email.lower().encode('utf-8')
    gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email).hexdigest() + "?"
    gravatar_url += f"s={size}&d=identicon"
    return gravatar_url 