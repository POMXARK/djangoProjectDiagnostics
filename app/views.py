import requests
from django.contrib.auth.views import LoginView

# Create your views here.
from django.forms import formset_factory
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from app.forms import LoginUserForm

from django.views.generic.base import TemplateResponseMixin, ContextMixin, View

from app.models import Obj1Cmn, Obj2Cmn, Obj1Ai, Obj2Ai
from app.serializers import Ai1Serializer, Ai2Serializer


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    """
    Render a template. Pass keyword arguments from the URLconf to the context.
    """
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        global data, tables
        username = self.request.user.username
        print('lolol')
        print(request.META['HTTP_HOST'])
        print(f'http://{request.META["HTTP_HOST"]}/api/tables-1')
        if username == 'admin':
            data = Obj1Cmn.objects.values()
            tables = requests.get(f'http://{request.META["HTTP_HOST"]}/api/tables-1').json()

        if username == 'Cm002':
            data = Obj2Cmn.objects.values()
            tables = requests.get(f'http://{request.META["HTTP_HOST"]}/api/tables-2').json()

        if len(data) == 0:
            return self.render_to_response(context=[])
        data = {
            "title_page": "Api",
            "title": f"Welcome, {username}! Thanks for logging in.",
            "table_title": ["id", "current", "sts"],
            "qs": data,
            "tables": tables,
            "username": username,
        }
        return self.render_to_response(context=data)


class LoginUser(LoginView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    form_class = LoginUserForm
    template_name = 'app/login.html'

    def get_success_url(self):
        username = self.request.user.username
        if len(username) > 0:
            return reverse_lazy('home')


class BaseTableViewSetAi(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = Ai2Serializer
    #permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['idai', ]


class TableViewSetAi1(BaseTableViewSetAi):
    queryset = Obj1Ai.objects.all()


class TableViewSetAi2(BaseTableViewSetAi):
    queryset = Obj2Ai.objects.all()
