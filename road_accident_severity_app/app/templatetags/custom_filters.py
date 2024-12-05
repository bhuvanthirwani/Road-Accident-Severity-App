from django import template

register = template.Library()

# Create a custom filter to get the dictionary value by key
@register.filter(name='get_item')
def get_item(dictionary, key):
    """Retrieve the value from a dictionary using the given key."""
    return dictionary.get(key)