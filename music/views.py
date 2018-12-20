from django.views import generic
from . models import Album, Song
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


def details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, "music/detail.html", {'album': album, })


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = reverse_lazy('music:index')


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

# class DetailView(generic.ListView, album_id):
#     model = Album
#     template_name = 'music/detail.html'
#     def get_queryset(self):
#         album = get_object_or_404(Album, pk=album_id)
#         return render("music/detail.html", {'album': album, })

# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song
#
#
# def index(request):
#     allalbums = Album.objects.all()
#     return render(request, "music/index.html", {'allalbums': allalbums, })
#
#
# def details(request,album_id):
#     checkalbum = get_object_or_404(Album,pk=album_id)
#     return render(request, "music/detail.html", {'checkalbum': checkalbum, })
#
#
# def favorite(request,album_id):
#     checkalbum = get_object_or_404(Album,pk=album_id)
#     try:
#         selected_song = checkalbum.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'checkalbum': checkalbum, 'error_message': "No Valid Song Selected", })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'checkalbum': checkalbum})
