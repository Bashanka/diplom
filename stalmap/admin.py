from django.contrib import admin
from .models import Image, Photo, PhotoDownload, MapObjectType, MapType, GeoMap, MapObject, ModelType, Model, \
    ArchComplex, Scene, Leader, State, UnitType, WarUnit, UnitHead, HistoryEvent, Participant, DataType, Data, \
    ActionType, Action, HistoryAction

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'user')
    list_filter = ('user', 'name')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'downloadCount', 'user')
    list_filter = ('user', 'name')

@admin.register(PhotoDownload)
class PhotoDownloadAdmin(admin.ModelAdmin):
    list_display = ('photo', 'ip')
    # list_filter = ('photo')

@admin.register(MapObjectType)
class MapObjectTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user')
    list_filter = ('user', 'name')

@admin.register(MapType)
class MapTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user')
    list_filter = ('user', 'name')

@admin.register(GeoMap)
class GeoMapAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'scale', 'longitude', 'latitude', 'mapType', 'user')
    list_filter = ('user', 'mapType', 'name')

@admin.register(MapObject)
class MapObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'coordinates', 'address', 'description', 'mapObjectType', 'geoMap', 'user')
    list_filter = ('user', 'mapObjectType', 'geoMap', 'name')

@admin.register(ModelType)
class ModelTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user')
    list_filter = ('user', 'name')

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'marker', 'description', 'file', 'modelType', 'user')
    list_filter = ('user', 'modelType', 'name')

@admin.register(ArchComplex)
class ArchComplexAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user')
    list_filter = ('user', 'name')

@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user')
    list_filter = ('user', 'name')

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography', 'file', 'user')
    list_filter = ('user', 'name')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user')
    list_filter = ('user', 'name')

@admin.register(UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent', 'user')
    list_filter = ('user', 'parent', 'name')

@admin.register(WarUnit)
class WarUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'unitType', 'state', 'user')
    list_filter = ('user', 'state', 'unitType', 'name')

@admin.register(UnitHead)
class UnitHeadAdmin(admin.ModelAdmin):
    list_display = ('begin', 'end', 'unitType', 'warUnit', 'leader', 'user')
    list_filter = ('user', 'unitType', 'warUnit', 'begin')

@admin.register(HistoryEvent)
class HistoryEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'begin', 'end', 'file', 'description', 'parent', 'user')
    list_filter = ('user', 'parent', 'begin', 'name')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter = ('user', 'name')

@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user')
    list_filter = ('user', 'name')

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'dataType', 'user')
    list_filter = ('user', 'dataType', 'name')

@admin.register(ActionType)
class ActionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user')
    list_filter = ('user', 'name')

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('name', 'begin', 'end', 'actionType', 'data', 'user')
    list_filter = ('user', 'actionType', 'begin', 'name')

@admin.register(HistoryAction)
class HistoryActionAdmin(admin.ModelAdmin):
    list_display = ('name', 'begin', 'end', 'historyEvent', 'action', 'description', 'user')
    list_filter = ('user', 'historyEvent', 'action', 'begin')
