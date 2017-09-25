# To call a view in django we need to map it to a URL.
# To map a view to a URL we need a URLconf
# This file is a URLconf

from django.conf.urls import url

# This is a 'relative' import
# (See PEP 328 for the history)
# `.` means the current package
from . import views

# urlpatterns is a list of `url` instances
# the `django.url` initializer takes a regex and a list of urls or a string representing a namespace
# the `django.include` function takes a path to another URLConf method that should be used in its place
#
# In the example below, we match on any string beginning with `polls/`.
# Django will take that string, remove the leading portion of the string that matched (here the `polls/`) and send the
# remainder of the string to the URLConf that the include() points to (here `polls.url`)
urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
