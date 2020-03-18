'''import render'''
from django.shortcuts import render

# Create your views here.
def gallery(request):
    '''return gallery'''
    return render(request, 'gallery/gallery.html')
