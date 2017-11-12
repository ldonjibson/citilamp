from django.contrib import admin

from citilamp.models import *
# Register your models here.

models_to_register = (Continent, Country, StateProvince, City, Park, Museum, TouristCenter ,Gallery, MarketTradingcenterSHOP, HistoricalAttraction, Beach)

for model in models_to_register:
    admin.site.register(model)
