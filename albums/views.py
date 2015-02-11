from django.http.response import Http404
from django.shortcuts import render_to_response, redirect
from albums.models import Album, Photo, Comment, Avatar
from django.core.exceptions import ObjectDoesNotExist
from .forms import CommentForm, AlbumsForm, PhotoForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def albums(request, page_number=1):
    all_albums = Album.objects.all()
    current_page = Paginator(all_albums, 12)
    args = {}
    args['albums'] = current_page.page(page_number)
    username = request.user.id
    if username is not None:
        args['username'] = auth.get_user(request).username
        x = User.objects.get(id=username)
        args['avatar'] = Avatar.objects.get(avatar_user=x)
    return render_to_response('albums.html', args)


def album(request, id):
    args = {}
    photo_form = PhotoForm
    args.update(csrf(request))
    args['album'] = Album.objects.get(id=id)
    args['photos'] = Photo.objects.filter(album_id=id)
    username = request.user.id
    if username is not None:
        args['username'] = auth.get_user(request).username
        x = User.objects.get(id=username)
        args['form'] = photo_form
        args['avatar'] = Avatar.objects.get(avatar_user=x)
    return render_to_response("album.html", args)


def add_like(request, id):
    username = auth.get_user(request).username
    q = username + "_" + id + "_" + id
    try:
        if q in request.COOKIES:
            redirect('/albums/all/')
        else:
            album = Album.objects.get(id=id)
            album.album_likes += 1
            album.save()
            response = redirect('/albums/all/')
            response.set_cookie(q, "likes albums %s" % id)
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/albums/all/')


def photo(request, id):
    args = {}
    comment_form = CommentForm
    args.update(csrf(request))
    args['photo'] = Photo.objects.get(id=id)
    args['comments'] = Comment.objects.filter(comments_photo_id=id).order_by('-id')
    args['form'] = comment_form
    username = request.user.id
    if username is not None:
        args['username'] = auth.get_user(request).username
        x = User.objects.get(id=username)
        args['avatar'] = Avatar.objects.get(avatar_user=x)
    return render_to_response('photo.html', args)


def add_comment(request, id):
    photo_id = id
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_photo = Photo.objects.get(id=photo_id)
            username = request.user.id
            comment.comments_author = User.objects.get(id=username)
            form.save()
            request.session.set_expiry(30)
            request.session['pause'] = True
    return redirect('/albums/photo/get/%s/' % photo_id)


def add_photo(request, id):
    album_id = id
    if request.POST:
        form = PhotoForm(request.POST)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.album = Album.objects.get(id=album_id)
            form.save()
    return redirect('/albums/get/%s/' % album_id)


def add_like_photo(request, id):
    username = auth.get_user(request).username
    q = username + "_" + id
    try:
        photo_id = id
        x = Photo.objects.get(photo_id=photo_id)
        if q in request.COOKIES:
            redirect('/albums/get/%s/' % x.album_id)
        else:
            f = Photo.objects.get(id=photo_id)
            f.photo_likes += 1
            f.save()
            response = redirect('/albums/get/%s/' % x.album_id)
            response.set_cookie(q, "likes photo %s" % photo_id)
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/albums/get/%s/' % x.album_id)


def search(request):
    args = {}
    args['username'] = auth.get_user(request).username
    username = request.user.id
    x = User.objects.get(id=username)
    args['avatar'] = Avatar.objects.get(avatar_user=x)
    if 'search' in request.GET and request.GET['search']:
        s = request.GET['search']
        once = Album.objects.filter(title=s)
        args['albums'] = once
        return render_to_response('albums.html', args)
    else:
        args['search'] = 'Ничего не найдено'
        return render_to_response('albums.html', args)


def my_albums(request):
    args = {}
    args['username'] = auth.get_user(request).username
    username = request.user.id
    x = User.objects.get(id=username)
    args['avatar'] = Avatar.objects.get(avatar_user=x)
    args['albums'] = Album.objects.filter(album_user_id=x.id)
    return render_to_response('albums.html', args)


def add_album1(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        form = AlbumsForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            username = request.user.id
            album.album_user = User.objects.get(id=username)
            form.save()
    username = request.user.id
    x = User.objects.get(id=username)
    args['avatar'] = Avatar.objects.get(avatar_user=x)
    args['albums'] = Album.objects.filter(album_user_id=x.id)
    args['username'] = auth.get_user(request).username
    return redirect('/albums/all/')


def add_album(request):
    args = {}
    args.update(csrf(request))
    form = AlbumsForm
    args['form'] = form
    args['username'] = auth.get_user(request).username
    username = request.user.id
    x = User.objects.get(id=username)
    args['avatar'] = Avatar.objects.get(avatar_user=x)
    return render_to_response('addalbum.html', args)


def add_like_comment(request, id, photo_id):
    username = auth.get_user(request).username
    q = id + "_" + username
    try:
        comment_id = id
        if q in request.COOKIES:
            redirect('/albums/photo/get/%s/' % photo_id)
        else:
            f = Comment.objects.get(id=comment_id)
            f.comments_likes += 1
            f.save()
            response = redirect('/albums/photo/get/%s/' % photo_id)
            response.set_cookie(q, "likes photo %s" % comment_id)
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/albums/photo/get/%s/' % photo_id)