
from django.contrib import admin
from django.urls import path
from loapp.views import locate
from app.views import home,Order,My_Order,About,Contact,Price,Update_Order,Delete_Order

urlpatterns = [
    path('admin/', admin.site.urls),
    path("locate/",locate, name="locate"),
    path("",home, name="home"),
    path("Order/",Order, name="Order"),
    path("My_Order/",My_Order, name="My_Order"),
    path("About/",About, name="About"),
    path("Contact/",Contact, name="Contact"),
    path("Price/",Price, name="Price"),
    path('Update_Order/<int:order_number>/',Update_Order, name='Update_Order'),
    path('Delete_Order/<int:order_number>/',Delete_Order, name='Delete_Order'),

]
