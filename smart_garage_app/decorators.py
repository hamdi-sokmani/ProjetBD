from django.http import HttpResponse
from django.shortcuts import redirect

# Précise les rôles attribués à chaque utilisateur de l'application et les droits d'accès dont ils disposent
# unauthenticate_user : les pages de login et register
# responsable_role : le role de Chef des techniciens

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def responsable_role(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'technicien':
            return redirect('responsable')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
    
