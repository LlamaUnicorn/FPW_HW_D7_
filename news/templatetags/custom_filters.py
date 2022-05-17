from django import template

register = template.Library()


@register.filter()
def censor(value):
    profanity = ['редиска', 'новости']
    try:
        for word in profanity:
            if word.find(value):
                value = value.replace(word[1::], "*" * (len(word)-1))
        return f'{value}'
    except TypeError as e:
        print(f'Фильтр применяется только к строкам: {e}')
