from django.shortcuts import render, redirect

# Create your views here.
from .forms import ImageUploadForm

from .models import Image

from django.http import FileResponse

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_images=Image.objects.all().count()
    
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    data = Image.objects.all()
    return render(
        request,
        'index.html',
        context={'data': data},
    )


from django.views import generic

#class ImageListView(generic.ListView):
    #model = Image

class ImageDetailView(generic.DetailView):
    model = Image


def uploadView(request):                                      
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

    
    
class TagIndexView(generic.ListView):
    model = Image
    template_name = 'image_list.html'
    context_object_name = 'image'

    def get_queryset(self):
         return Image.objects.filter(tags__slug=self.kwargs.get('tag_slug'))