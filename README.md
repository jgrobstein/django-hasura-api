# Django & Hasura GraphQL API with Authentication

Backend project with user authentication and JWT provided by allauth and graphene coupled with postgres and hasura containers.

## Running application
```
docker-compose up --build
docker exec -d app python manage.py migrate
```

[source](https://hasura.io/blog/how-to-setup-authentication-with-django-graphene-and-hasura-graphql/)