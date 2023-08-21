"""
URL configuration for HelloWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.hello),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.translate_text, name='translate_text'),
# ]


# from django.urls import path
# from . import views
 
# urlpatterns = [
#     path('runoob/', views.runoob),
# ]




from django.urls import path
from . import views,search,search2,trans
 
urlpatterns = [
    # url(r'^hello/$', views.runoob),
    # url(r'^testdb/$', testdb.testdb),
    # url(r'^search-form/$', search.search_form),
    # path('search-form/', search.search_form),
    # path('search/', search.search_translate),
    # url(r'^search/$', search.search),




    # path('search-form/', search.search_form),
    # path('search/', search.search),

    path('register/', search2.register_view, name='register'),
    path('home/', search2.deepL_test),  
    # path('about/', search.search_form), 
    path('about/', search2.deepL_embed),  
    path('search-post/', search2.search_post),
    path('login/', search2.login_view),  
    # path('deepl/', search2.deepL_embed),
    # path('redirect/', search2.redirect_to_external_website),
    # path('show-partial-content/', search2.show_partial_content, name='show_partial_content'),
    path('translate/', search2.translate_document, name='translate_document'),
]



# from django.urls import path
 
# from . import views,testdb
 
# urlpatterns = [
#     path('runoob/', views.runoob),
#     path('testdb/', testdb.testdb),
# ]


