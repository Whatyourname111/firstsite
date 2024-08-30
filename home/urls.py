from django.urls import path

from .forms import CreateBlogForm
from .views import home2
from .views import *

urlpatterns = [

    path('in2/', home2, name='home2'),
    path('blog/', blogList, name='blog'),
    path('craete/',craeteBlog),
    path('update/<int:id>/',update_blog_view),
    path('delete/<int:id>',deleteBlogview),
    path('area/', area_show),
    path('region/', region_show)
]


