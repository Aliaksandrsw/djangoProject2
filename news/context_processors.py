def authentication_status(request):
    return {
        'user_authenticated': request.user.is_authenticated
    }