===========
SingeRecord
===========

This modules provide a simple abstraction that allows you to declare a Django model as a single record model (just like a singleton).

It's not compliant with the active record pattern but i've found myself using this approach over and over again ( for example for a settings model... ) so i've turned it into a package.

************
Dependencies
************

* Django >= 1.3.1

************
Installation
************

1. ``pip instal``
2. Add ``'singlerecord'`` o the `INSTALLED_APPS` in your project's ``settings.py`` 


*****
Usage
*****

in models.py make your model extend SingleRecordModel

``
from singlerecord.models import SingleRecordModel

class SiteSettings(SingleRecordModel):
  ...
``

in admin.py register your model as a SingleRecordModelAdmin

``
from singlerecord.admin import SingleRecordModelAdmin
from myapp.models import SiteSettings
        
admin.site.register(SiteSettings, SingleRecordModelAdmin)
``

***************
Acknowledgments
***************

https://github.com/tttallis/django-singletons which as a similar implementation
