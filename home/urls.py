from django.contrib.auth import views as auth_views
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.signup_view, name="create_user"), # Keep name='create_user' for compatibility
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("detect_user/", views.detect_user, name="detect_user"),
    path("notes_detail/", views.notes_detail, name="notes_detail"),
    path("edit_note/<int:pk>/", views.edit_note, name="edit_note"),
    path("opened_note/<int:pk>/", views.open_note, name="open_note"),
    path("move_to_trash/<int:pk>/", views.move_to_trash, name="move_to_trash"),
    path("return_note/<int:pk>/", views.return_note, name="return_note"),
    path("trash_notes/", views.trash_notes, name="trash_notes"),
    path("delete_note/<int:pk>/", views.delete_note, name="delete_note"),
]
