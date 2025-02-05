from django.contrib import admin
from app2.models import Logintable
from app2.models import Usertable
from app2.models import Producttable
from app2.models import Carttable
from app2.models import Billtable

# Register your models here.
admin.site.register(Logintable)
admin.site.register(Usertable)
admin.site.register(Producttable)
admin.site.register(Carttable)
admin.site.register(Billtable)