from django.forms import ModelForm
import time
from .models import Deal

class CreateDeal(ModelForm):
    class Meta:
        model = Deal
        fields = ['first_name', 'last_name', 'price', 'date', 'time_str', 'time_end']
        labels = {
            'first_name':'Имя',
            'last_name':'Фамилия',
            'price':'Цена',
            'date':'Дата проведения мероприятия',
            'time_str':'Время начала',
            'time_end':'Время окончания'
        }
