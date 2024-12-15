from django.urls import path
from . import views

urlpatterns = [
    path('http/', views.http_response_example, name='http_response'),
    path('redirect/', views.http_response_redirect, name='http_response_redirect'),
    path('bad_request/', views.http_response_bad_request, name='http_response_bad_request'),
    path('not_found/', views.http_response_not_found, name='http_response_not_found'),
    path('forbidden/', views.http_response_forbidden, name='http_response_forbidden'),
    path('server_error/', views.http_response_server_error, name='http_response_server_error'),
    path('json/', views.json_response_example, name='json_response'),
    path('streaming/', views.streaming_http_response_example, name='streaming_http_response'),
    path('file/', views.file_response_example, name='file_response'),
    path('graph/', views.http_response_custom_graph, name='http_response_graph'),
]
