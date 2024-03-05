from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import pandas as pd

def index(request):
    return redirect(reverse('bus_stations'))


data = pd.read_csv('data-398-2018-08-30.csv')
data = data[['Name', 'District']]
data['Street'] = data['Name'].str.extract(', (.+?)\(', expand=False)

CONTENT = data.to_dict('records')

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)
