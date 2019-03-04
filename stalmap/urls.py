from django.urls import path
from .views import Index, \
    ImageView


# Index page
urlpatterns = [
    path('', Index.as_view(), name='index'),
]

# image views
urlpatterns += [
    path('images/', ImageView.as_view(), name='image-list'),
    # path('image/<int:pk>/', ImageView.as_view(), name='image-detail'),
    # path('image/create/', ImageView.as_view(), name='image-create'),
    # path('image/<int:pk>/update/', ImageView.as_view(), name='image-update'),
    # path('image/<int:pk>/delete/', ImageView.as_view(), name='image-delete'),
]
