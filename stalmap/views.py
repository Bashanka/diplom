from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Image, Photo, PhotoDownload, MapObjectType, MapType, GeoMap, MapObject, ModelType, Model, \
    ArchComplex, Scene, Leader, State, UnitType, WarUnit, UnitHead, HistoryEvent, Participant, DataType, Data, \
    ActionType, Action, HistoryAction

# Create your views here.


class Index(TemplateView):
    template_name = "index.html"


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk
            }
            return JsonResponse(data)
        else:
            return response


class ImageView(ListView):
    template_name = "image/list.html"
    model = Image

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)


class ImageCreateView(AjaxableResponseMixin, CreateView):
    model = Image
