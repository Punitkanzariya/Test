from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('unit/', views.converter_view, name='converter_view'),
    path('currency/', views.currency_converter_view, name='currency_converter_view'),
    path('number-system/', views.number_system_converter, name='number_system_converter'),
    path('color/', views.color_converter, name='color_converter'),
    path('health/', views.health_converter, name='health_converter'),
    path('imagetopdf/', views.image_to_pdf_view, name='image_to_pdf_view'),
    path('wordtopdf/', views.word_to_pdf_converter, name='word_to_pdf_converter'),
    path('pdftoword/', views.pdf_to_word_converter, name='pdf_to_word_converter'),
]
