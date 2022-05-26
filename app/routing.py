from django.urls import path
from app.consumers import GraphConsumerCmn, GraphConsumerAi, DetailsConsumerCmn

ws_urlpatterns = [
    path('ws/graph/', GraphConsumerCmn.as_asgi()),
    path('ws/table/', GraphConsumerAi.as_asgi()),
    path('ws/details/', DetailsConsumerCmn.as_asgi()),
]