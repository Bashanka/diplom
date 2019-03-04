from django.db import models
from django.contrib.auth.models import User


def user_directory_image_path(instance, filename):
    return "user_{0}/images/{1}".format(instance.user.id, filename)


class Image(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    image = models.ImageField(upload_to=user_directory_image_path, verbose_name="Изображение")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


def user_directory_photo_path(instance, filename):
    return "user_{0}/photos/{1}".format(instance.user.id, filename)


class Photo(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    image = models.ImageField(upload_to=user_directory_photo_path, verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    downloadCount = models.IntegerField(default=0, verbose_name="Количество скачиваний")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class PhotoDownload(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, verbose_name="Фото")
    ip = models.TextField(max_length=50, verbose_name="IP")

    def __unicode__(self):
        return self.photo

    class Meta:
        verbose_name = "Количество скачиваний"
        verbose_name_plural = "Количество скачиваний"


class MapObjectType(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Тип объекта карты"
        verbose_name_plural = "Типы объектов карты"


class MapType(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Тип  карты"
        verbose_name_plural = "Типы  карт"


def user_directory_geomap_path(instance, filename):
    return "user_{0}/geomaps/{1}".format(instance.user.id, filename)


class GeoMap(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    file = models.FileField(upload_to=user_directory_geomap_path, verbose_name="Файл")
    scale = models.FloatField(verbose_name="Масштаб")
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")
    mapType = models.ForeignKey(MapType, on_delete=models.CASCADE, verbose_name="Тип карты")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Географическая карта"
        verbose_name_plural = "Географические карты"


class MapObject(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    coordinates = models.TextField(verbose_name="Координаты")
    address = models.TextField(verbose_name="Адрес")
    description = models.TextField(verbose_name="Описание")
    mapObjectType = models.ForeignKey(MapObjectType, on_delete=models.CASCADE, verbose_name="Тип объекта карты")
    geoMap = models.ForeignKey(GeoMap, on_delete=models.CASCADE, verbose_name="Карта")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Объект карты"
        verbose_name_plural = "Объекты карты"


class ModelType(models.Model):
    name = models.TextField(max_length=200, verbose_name="Тип модели")
    description = models.TextField(verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Тип модели"
        verbose_name_plural = "Типы моделей"


def user_directory_model_path(instance, filename):
    return "user_{0}/models/{1}/{2}".format(instance.user.id, instance.modelType.name, filename)


class Model(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    marker = models.BooleanField(default=False, verbose_name="Маркер")
    description = models.TextField(verbose_name="Описание")
    file = models.FileField(upload_to=user_directory_model_path, verbose_name="Модель")
    mapObject = models.ManyToManyField(MapObject, blank=True, verbose_name="Объект карты")
    image = models.ManyToManyField(Image, blank=True)
    modelType = models.ForeignKey(ModelType, on_delete=models.CASCADE, verbose_name="Тип модели")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"


class ArchComplex(models.Model):
    name = models.TextField(verbose_name="Название")
    model = models.ManyToManyField(Model, verbose_name="Модели")
    description = models.TextField(verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Архитектурный комплекс"
        verbose_name_plural = "Архитектурные комплексы"


class Scene(models.Model):
    name = models.TextField(verbose_name="Название")
    archComplex = models.ManyToManyField(ArchComplex, verbose_name="Архитектурные комплексы")
    model = models.ManyToManyField(Model, verbose_name="Модели")
    description = models.TextField(verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Сцена"
        verbose_name_plural = "Сцены"


def user_directory_leader_path(instance, filename):
    return "user_{0}/leaders/{1}".format(instance.user.id, filename)


class Leader(models.Model):
    name = models.TextField(max_length=200, verbose_name="Имя")
    biography = models.TextField(verbose_name="Биография")
    file = models.FileField(verbose_name="Файл")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Лидер"
        verbose_name_plural = "Лидеры"


class State(models.Model):
    name = models.TextField(max_length=200, verbose_name="Имя")
    description = models.TextField(verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class UnitType(models.Model):
    name = models.TextField(max_length=200, verbose_name="Имя")
    description = models.TextField(verbose_name="Описание")
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name="Состоит в")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Тип военного подразделения"
        verbose_name_plural = "Типы военных подразделений"


class WarUnit(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    unitType = models.ForeignKey(UnitType, on_delete=models.CASCADE, verbose_name="Тип военного подразделения")
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Военное подразделение"
        verbose_name_plural = "Военные подразделения"


class UnitHead(models.Model):
    begin = models.DateField(verbose_name="Начало")
    end = models.DateField(verbose_name="Конец")
    unitType = models.ForeignKey(UnitType, on_delete=models.CASCADE, verbose_name="Тип военного подразделения")
    warUnit = models.ForeignKey(WarUnit, on_delete=models.CASCADE, verbose_name="Военное подразделение")
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE, verbose_name="Лидер")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.leader

    class Meta:
        verbose_name = "Глава военного подразделения"
        verbose_name_plural = "Главы военных подразделений"


def user_directory_historyevent_path(instance, filename):
    return "user_{0}/historyevents/{1}".format(instance.user.id, filename)


class HistoryEvent(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    begin = models.DateField(verbose_name="Начало")
    end = models.DateField(verbose_name="Конец")
    file = models.FileField(upload_to=user_directory_historyevent_path, verbose_name="Файл")
    description = models.TextField(verbose_name="Описание")
    geoMap = models.ManyToManyField(GeoMap, blank=True,verbose_name="Карта")
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL,
                               verbose_name="Историческое событие")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Историческое событие"
        verbose_name_plural = "Исторические события"


class Participant(models.Model):
    name = models.TextField(max_length=200, verbose_name="Имя")
    mapObject = models.ManyToManyField(MapObject, blank=True, verbose_name="Объект карты")
    warUnit = models.ManyToManyField(WarUnit, blank=True, verbose_name="Военное подразделение")
    historyEvent = models.ManyToManyField(HistoryEvent, blank=True, verbose_name="Историческое событие")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"


class DataType(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Тип данных"
        verbose_name_plural = "Типы данных"


class Data(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    dataType = models.ForeignKey(DataType, on_delete=models.CASCADE, verbose_name="Тип данных")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Данные"
        verbose_name_plural = "Данные"


class ActionType(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Тип события"
        verbose_name_plural = "Типы собитий"


class Action(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    begin = models.DateField(verbose_name="Начало")
    end = models.DateField(verbose_name="Конец")
    actionType = models.ForeignKey(ActionType, on_delete=models.CASCADE, verbose_name="Тип события")
    data = models.ForeignKey(Data, on_delete=models.CASCADE, verbose_name="Данные")
    participant = models.ManyToManyField(Participant, blank=True, verbose_name="Участники")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class HistoryAction(models.Model):
    name = models.TextField(max_length=200, verbose_name="Название")
    begin = models.DateField(verbose_name="Начало")
    end = models.DateField(verbose_name="Конец")
    historyEvent = models.ForeignKey(HistoryEvent, on_delete=models.CASCADE, verbose_name="Историческое событие")
    action = models.ForeignKey(Action, on_delete=models.CASCADE, verbose_name="Событие")
    description = models.TextField(verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Историческое событие"
        verbose_name_plural = "Исторические события"