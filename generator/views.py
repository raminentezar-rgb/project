from django.shortcuts import render
from .forms import SignatureForm
from django.core.files.storage import FileSystemStorage


def generate_signature(request):
    if request.method == 'POST':
        form = SignatureForm(request.POST, request.FILES)
        if form.is_valid():
            image_url = ''
            if request.FILES.get('image'):
                image = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                image_url = fs.url(filename)

            context = {
                'name': form.cleaned_data['name'],
                'title': form.cleaned_data['title'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data.get('phone', ''),
                'website': form.cleaned_data.get('website', ''),
                'image_url': image_url,
            }
            return render(request, 'generator/signature_result.html', context)
    else:
        form = SignatureForm()

    return render(request, 'generator/signature_form.html', {'form': form})
