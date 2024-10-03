from django.urls import path
from .views import ComplaintsUserView, ComplaintsAdminView, CommentsComplaintsView

urlpatterns = [
    path('complaints-admin', ComplaintsAdminView.as_view()),
    path('complaints-admin/<str:pk>', ComplaintsAdminView.as_view()),
    path('complaints', ComplaintsUserView.as_view()),
    path('complaints/<str:folio>', ComplaintsUserView.as_view()),
    path('comments', CommentsComplaintsView.as_view()),
    path('comments/<str:pk>', CommentsComplaintsView.as_view())
]