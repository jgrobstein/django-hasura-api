# Django & Hasura GraphQL API with Authentication

Backend project with user authentication and JWT provided by allauth and graphene coupled with postgres and hasura containers.

## Running application
```
docker-compose up --build -d
docker exec -d app python manage.py migrate
```

Once containers are running open a browser to `localhost:8080` to access the hasura console.

Optionally, import the `hasura_metadata*.json` file provided to apply permissions and remote schemas in hasura or build your own from the console.

### Endpoints
---
| APP | API | Endpoint | Access |
| --- | --- | --- | --- |
| GRAPHENE | GraphQL | loaclhost:8000/graphql | Public |
| HASURA | GraphQL | loaclhost:8080/v1/graphql | Permission rules |
| HASURA | Relay | loaclhost:8080/v1beta1/relay | Permission rules |
| HASURA | Legacy GraphQL | loaclhost:8080/v1alpha1/graphql | Permission rules |
| HASURA | Schema (> v2.0) | loaclhost:8080/v2/query | Admin only |
| HASURA | Metadata (> v2.0) | loaclhost:8080/v1/metadata | Admin only |
| HASURA | Schema/Metadata (< v1.3) | loaclhost:8080/v1/query | Admin only |
| HASURA | Restified GQL | loaclhost:8080/api/rest | GQL REST Routes |
| HASURA | Version | loaclhost:8080/v1/version | Public |
| HASURA | Health | loaclhost:8080/healthz | Public |
| HASURA | PG Dump | loaclhost:8080/v1alpha1/pg_dump | Admin only |
| HASURA | Config | loaclhost:8080/v1alpha1/config | Admin only |
| HASURA | Explain | loaclhost:8080/v1/graphql/explain | Admin only |

[source](https://hasura.io/blog/how-to-setup-authentication-with-django-graphene-and-hasura-graphql/)