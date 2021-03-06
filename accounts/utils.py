import random


def get_rg_number(instance):
    _first_name = instance.first_name[:3].upper()
    return "RG-{first_name}-{random_number}".format(first_name=_first_name, random_number=random.randint(100, 999))


def unique_rg_number(instance, new_rg_number=None):
    if new_rg_number is not None:
        rg_number = new_rg_number
    else:
        rg_number = get_rg_number(instance)

    klass = instance.__class__
    qs_exists = klass.objects.filter(username=rg_number).exists()
    if qs_exists:
        new_rg_number = get_rg_number(instance)
        return unique_rg_number(instance, new_rg_number=new_rg_number)
    return rg_number
