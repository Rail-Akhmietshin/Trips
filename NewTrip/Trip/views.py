from django.contrib.auth import logout, login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q

from django.http import HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseServerError

from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView


from .forms import *
from .models import *
from .utils import DataMixin
from other_files.get_cities.cities import cities



class FindTripMain(DataMixin, ListView):
    model = Trip
    template_name = 'Trip/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
		title='NewWay - Поиск попутчиков!',
		cities=cities,	
	)

        return dict(list(context.items()) + list(c_def.items()))


def verify(request, uuid):
    try:
        user = MyUser.objects.get(verification_uuid=uuid, is_confirmation=False)
    except MyUser.DoesNotExist:
        raise Http404("Такого аккаунта не существует")
    user.is_confirmation = True
    user.save()

    return redirect('main')



class Trips(DataMixin, ListView):
    model = Trip

    template_name = 'Trip/find.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Текущие поездки')

        return dict(list(context.items()) + list(c_def.items()))


    def get_queryset(self):
        query_where_from = self.request.GET.get('where_from')
        query_where = self.request.GET.get('where')
        if query_where_from not in cities or query_where == query_where_from:
            raise Http404()
        query_when = self.request.GET.get('when')


        posts = Trip.objects.filter(
            Q(where_from__icontains=query_where_from) & Q(where__icontains=query_where) &  Q(date_trip__icontains=query_when)
        ).order_by("time_trip")


        return posts


class ShowPost(DataMixin, DetailView):
    template_name = 'Trip/post.html'
    model = Trip
    slug_url_kwarg = "post_slug"
    context_object_name = "post"


    def get_context_data(self, *, object_list = None, **kwargs):

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Текущая поездка')
        return dict(list(context.items()) + list(c_def.items()))



class AddTrip(LoginRequiredMixin, DataMixin, CreateView):
    model = Trip
    form_class = AddTripForm
    template_name = "Trip/publish.html"
    login_url = reverse_lazy("auth")

    def form_valid(self, form):
        form.instance.trip_user_id = self.request.user.pk
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)


        c_def = self.get_user_context(
		title='Публикация поездки',
		cities=cities,
)


        return dict(list(context.items()) + list(c_def.items()))

    def get_form_kwargs(self):
        kwargs = super(AddTrip, self).get_form_kwargs()
        kwargs.update({'user': self.request.user.pk})
        return kwargs


    def get_success_url(self):
        form_where_from = self.request.POST.get('where_from')
        form_where = self.request.POST.get('where')
        form_when = self.request.POST.get('date_trip')

        url = f'?where_from={form_where_from}&where={form_where}&when={form_when}'
        slug = slugify(f'{url}&{self.request.user.pk}{self.request.user.number_phone}{self.request.user.pk}').lower()

        return str(f'/post/{slug}')







class AuthUser(DataMixin, LoginView):
    form_class = AuthUserForm
    template_name = "Trip/input.html"

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Авторизация')

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'Trip/reg.html'
    success_url = reverse_lazy('auth')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        return redirect('main')


class MyProfile(ListView):
    template_name = "Trip/myprofile.html"
    model = MyUser
    
    slug_url_kwarg = "key_profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Мой профиль'
        return context

class UpdateProfile(UpdateView):
    model = MyUser
    template_name_suffix = 'update_profile'
    form_class = UpdateUser
    context_object_name = 'form'
    template_name = 'Trip/update_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование профиля'
        return context

    def form_valid(self, form):
        form = form.save()
        return redirect('myprofile', self.request.user.key_profile)


class MyTrips(DataMixin, ListView):
    model = Trip
    template_name = 'Trip/mytrips.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Мои поездки')
        return dict(list(context.items()) + list(c_def.items()))


    def get_queryset(self):
        return Trip.objects.filter(trip_user=self.request.user)


def logout_user(request):
    logout(request)
    return redirect('main')

def delete_user(request):
    MyUser.objects.filter(pk=request.user.pk).delete()
    return redirect('main')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1> Такой страницы не существует </h1>")

def AccessIsDenied(request, exception):
    return HttpResponseForbidden(f"<h1> Доступ запрещен </h1>")

def ServerError(exception):
    return HttpResponseServerError(f"<h1> Ошибка сервера </h1>")


