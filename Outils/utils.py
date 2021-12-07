
from django.db.models import Max
from Outils.models import EvalRoles


def get_max_order(user) -> int:
    existing_roles = EvalRoles.objects.filter(eval=user)
    if not existing_roles.exists():
        return 1
    else:
        current_max = existing_roles.aggregate(max_order=Max('order'))['max_order']
        return current_max + 1

def reorder(user):
    existing_roles = EvalRoles.objects.filter(eval=user)
    if not existing_roles.exists():
        return
    number_of_films = existing_roles.count()
    new_ordering = range(1, number_of_films+1)
    
    for order, user_role in zip(new_ordering, existing_roles):
        user_role.order = order
        user_role.save()