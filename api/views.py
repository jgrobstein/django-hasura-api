from django.http import JsonResponse

# Create your views here.


def index(request):
    response = JsonResponse({
        'title': 'Django & Hasura GraphQL API',
        'content': {
            'description': 'Backend project with user authentication and JWT provided by allauth and graphene coupled with postgres and hasura containers.',
            'endpoint': 'http://localhost:8080/v1/graphql',
        }
    }, status=418)
    return response