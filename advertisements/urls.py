#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:42:48 2023

@author: nikita
"""
from rest_framework.routers import DefaultRouter

from advertisements.views import AdvertisementViewSet

router = DefaultRouter()
router.register('advertisements', AdvertisementViewSet)

urlpatterns = router.urls