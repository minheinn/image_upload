from django.shortcuts import render, redirect
from . models import Category, Photo

# Create your views here.
def ShowPhoto(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
        
    categories = Category.objects.all()
    context = {'categories':categories, 'photos':photos}
    return render(request, 'pages/show_photo.html', context)

def AddPhoto(request):
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        
        photo = Photo.objects.create(
            category=category,
            name=data['name'],
            description=data['description'],
            image=image,
        )
        return redirect('show_photo')
    
    context = {'categories':categories}
    return render(request, 'pages/add_photo.html', context)

def ViewPhoto(request, slug):
    photo = Photo.objects.get(slug=slug)    
    context = {'photo':photo}
    return render(request, 'pages/view_photo.html', context)