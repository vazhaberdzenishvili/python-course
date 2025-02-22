from django.http import HttpResponseForbidden


def has_book_add_permission(function):
    def wrapper(request, *args, **kwargs):
        if request.user.has_perm('core.add_book'):
            return function(request, *args, **kwargs)

        return HttpResponseForbidden('You do not have permission to perform this action.')

    return wrapper


def has_book_delete_permission(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.has_perm('core.delete_book'):
            return function(request, *args, **kwargs)

        return HttpResponseForbidden('You do not have permission to delete this book.')

    return wrapper
