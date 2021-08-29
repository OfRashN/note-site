from django.urls import path
from note_system.views import *

urlpatterns = [

    path('', index_view, name='index'),
    path('public/', public_view, name='public'),
    path('my_notes/', my_notes_view, name='my_notes'),
    path('note/<note_id>/', note_view, name='note'),
    path('create/', CreateNoteView.as_view(), name='create_note'),
    path('note/<int:pk>/edit/', EditNoteView.as_view(), name='edit_note'),
    path('note/<int:pk>/delete/', DeleteNoteView.as_view(), name='delete_note'),
    path('search/', SearchNoteView.as_view(), name='search_note'),

]
