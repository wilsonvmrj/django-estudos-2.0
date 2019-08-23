from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm

# Create your views here.
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons })


def persons_new(request):
    form = PersonForm(request.POST, request.FILES, None)
    print(form)
    print("1")
    if form.is_valid():
        form.save()
        return redirect('peson_list')
    else:
        return render(request, 'person_form.html', {'form': form})


    
