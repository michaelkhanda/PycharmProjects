from django.http import HttpResponse
from django.shortcuts import render

from main_app.models import Artist, Song


# Create your views here.
def show(request):
    # artist = Artist.objects.first()
    # artist = Artist.objects.order_by('?').first()
    # print(artist)
    #
    # albums = artist.album_set.all()
    # print(albums)
    #
    # for alb in albums:
    #     print(alb.name, alb.release_year)
    #     songs = alb.songs.all()
    #     print(len(songs))
    #     for s in songs:
    #         print('Song -', s.title, s.duration)

    song = Song.objects.order_by('?').first()
    print(song)

    album = song.album
    print(album)

    artists = album.artists.all()
    print(artists)
    return HttpResponse(artists)


def save_or_fetch_artists(request):
    return None


def fetch_one_artist(request):
    return None


def update_artist(request):
    return None


def albums_for_artist(request):
    return None