# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [

    # URL pattern for the CityAutocomplete
    url(
        r'^city-autocomplete/$',
        views.CityAutocomplete.as_view(),
        name='city-autocomplete',
    ),


]
