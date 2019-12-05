from django.shortcuts import render, redirect
from .models import Dish, Staff, BlogPost, Mensaje, Reserva, Postulante
from .forms import ReservaForm, PostulanteForm, MensajeForm


def home(request):
    dishes = Dish.objects
    staffmembers = Staff.objects
    posts = BlogPost.objects
    lastposts = BlogPost.objects.order_by('id')[0:3]
    formReserva = ReservaForm()
    formPostulante = PostulanteForm()
    formMensaje = MensajeForm()
    return render(request, 'home/home.html', {'dishes': dishes, 'staffmembers': staffmembers, 'posts': posts, 'lastposts': lastposts,
                                              'formReserva': formReserva, 'formPostulante': formPostulante, 'formMensaje': formMensaje})


def system(request):
    return render(request, 'system/system.html')


def reserva(request):
    if request.method == 'POST':
        res = ReservaForm(request.POST)
        if res.is_valid():

            res.save()
            message = 'Reserva registrada con éxito.'
            dishes = Dish.objects
            staffmembers = Staff.objects
            posts = BlogPost.objects
            lastposts = BlogPost.objects.order_by('id')[0:3]
            formReserva = ReservaForm()
            formPostulante = PostulanteForm()
            formMensaje = MensajeForm()
            return render(request, 'home/home.html', {'message':message, 'dishes':dishes, 'staffmembers':staffmembers, 'posts':posts,
                                                  'lastposts':lastposts, 'formReserva':formReserva, 'formPostulante': formPostulante,
                                                      'formMensaje': formMensaje})
        else:
            error = 'Error al registrar tu reserva. Inténtalo nuevamente'
            return render(request, 'error.html', {'error': error})
    else:
        res = Reserva.objects
        return render(request, 'system/reservas.html', {'reservas': res})


def postulante(request):
    if request.method == 'POST':
        pos = PostulanteForm(request.POST, request.FILES)
        if pos.is_valid():
            pos.save()
            message = 'Postulación exitosa'
            dishes = Dish.objects
            staffmembers = Staff.objects
            posts = BlogPost.objects
            lastposts = BlogPost.objects.order_by('id')[0:3]
            formReserva = ReservaForm()
            formPostulante = PostulanteForm()
            formMensaje = MensajeForm()
            return render(request, 'home/home.html',
                          {'message': message, 'dishes': dishes, 'staffmembers': staffmembers, 'posts': posts,
                           'lastposts': lastposts, 'formReserva': formReserva, 'formPostulante': formPostulante, 'formMensaje': formMensaje})
        else:
            error = 'Error al registrar tu postulación. Inténtalo nuevamente'
            return render(request, 'error.html', {'error': error})
    else:
        pos = Postulante.objects
        return render(request, 'system/postulantes.html', {'postulantes': pos})


def mensaje(request):
    if request.method == 'POST':
        mes = MensajeForm(request.POST)
        if mes.is_valid():
            mes.save()
            message = 'Mensaje enviado exitosamente'
            dishes = Dish.objects
            staffmembers = Staff.objects
            posts = BlogPost.objects
            lastposts = BlogPost.objects.order_by('id')[0:3]
            formReserva = ReservaForm()
            formPostulante = PostulanteForm()
            formMensaje = MensajeForm()
            return render(request, 'home/home.html',
                          {'message': message, 'dishes': dishes, 'staffmembers': staffmembers, 'posts': posts,
                           'lastposts': lastposts, 'formReserva': formReserva, 'formPostulante': formPostulante,
                           'formMensaje': formMensaje})
        else:
            error = 'Error al intentar el mensaje. Inténtelo nuevamente'
            return render(request, 'error.html', {'error': error})
    else:
        mes = Mensaje.objects
        return render(request, 'system/mensajes.html', {'mensajes': mes})


def error(request):
    error = 'Usuario o contraseña incorrectos'
    return render(request, 'registration/login.html', {'error': error})
