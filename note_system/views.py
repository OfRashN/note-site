

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import urlencode
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, View, DeleteView, ListView
from django.db.models import Q

from accounts.models import User
from note_system.models import Note
from notes_website import settings

user = User


# разделы
def index_view(request):
    username = request.user.id
    context = {
        'notes': Note.objects.filter(Q(username=username) | Q(is_public=True)).order_by('-created_at'),
    }
    return render(request, "note_system/index.html", context=context)


def public_view(request):
    context = {
        'notes': Note.objects.order_by('-created_at').filter(is_public=True),
    }
    return render(request, "note_system/public_notes.html", context=context)


def my_notes_view(request):
    username = request.user.id
    context = {
        'notes': Note.objects.filter(username=username)
    }
    return render(request, "note_system/my_notes.html", context=context)


# заметка
def note_view(request, note_id):
    notes = Note.objects.filter(id=note_id)
    context = {
        'note_id': note_id,
        'notes': notes,
    }


    return render(request, 'note_system/note.html', context=context)



# поисковик

class SearchNoteView(ListView):
    model = Note
    template_name = 'note_system/note_list.html'
    queryset = ListView.queryset
    def get_queryset(self):
        username = self.request.user
        qs = super(SearchNoteView, self).get_queryset()
        search = self.request.GET.get('q', '')
        if search != '':
            qs = qs.filter(Q(username=username) | Q(theme__icontains=search) | Q(text__icontains=search)).order_by('-created_at')

        else:
            qs = qs
        return qs.filter(Q(is_public=True) | Q(username=username)).order_by('-created_at')

    def get_context_data(self, **kwargs):
        username = self.request.user
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('q', '')
        page = self.request.GET.get('page', '1')

        notes = Note.objects.filter(Q(username=username) | Q(is_public=True)).order_by('-created_at')
        if search != '':
            notes = Note.objects.filter(Q(is_public=True) |Q(username=username),(Q(theme__contains=search)| Q(text__contains=search))).order_by('-created_at')

        elif search == '':
            notes = notes

        else:
            pass

        # paginator = Paginator(notes, settings.POSTS_PER_PAGE)
        # notes = paginator.get_page(page)

        context.update({
            'notes' : notes,
            'search': search,
            'page': page,
            # 'paginator': paginator,
        })
        return context

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('login')
        return super().get(request, *args, **kwargs)

class CreateNoteView(CreateView):
    model = Note
    fields = ('theme', 'text', 'is_public')
    template_name = 'note_system/create_note.html'

    def form_valid(self, form):
        note = form.save(commit=False)
        note.username = self.request.user
        note.save()
        self.object = note

        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('login')
        return super().get(request, *args, **kwargs)


class EditNoteView(UpdateView):
    model = Note
    fields_public = 'theme', 'text',
    fields_private = 'theme', 'text', 'is_public',

    def dispatch(self, request, *args, **kwargs):
        note = self.get_object()  # получаем заметку(объект)
        note_status = note.is_public
        if note_status:
            self.fields = self.fields_public
        else:
            self.fields = self.fields_private
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('login')
        return super().get(request, *args, **kwargs)


class DeleteNoteView(DeleteView):
    model = Note
    success_url = reverse_lazy('index')
