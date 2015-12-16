


from pyramid.response import Response


def welcome_view(request):
    return Response('Hi :) This is a test pyramid application!')
