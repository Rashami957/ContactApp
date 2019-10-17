from .forms import PersonForm


def contact_list(request):
    persons = Person.objects.all().order_by('first_name')
    if request.GET.get('search') :
        search = request.GET.get('search')
        persons = Person.objects.filter(first_name__contains=search)
    return render(request, 'contact/contact_list.html', {'persons': persons, 'count': persons.count()})





def contact_detail(request, pk) :
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'contact/contact_detail.html', {'person' : person})


def contact_new(request) :
    if request.method == 'POST' :
        form = PersonForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('/')
    else:
        form = PersonForm()
    return render(request, 'contact/contact_edit.html', {'form': form})


def contact_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/person/' + str(person.pk))
    else:
        form = PersonForm(instance=person)
    return render(request, 'contact/contact_edit.html', {'form': form})


def contact_delete(request, pk) :
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('/')


# def contact_search(request, searchname) :
#    persons = Person.objects.all().order_by('last_name')
# searchname = request.GET.get('search')
# persons = Person.objects.filter(first_name__icontains=searchname)
# p = persons.object.get(first_name__icontains=searchname)
# return render(request, 'contact/search.html', {'persons' : persons, 'count' : persons.count()})


def contact_search(request):
    questions = None
    query = None
    if request.GET.get('search'):
        search = request.GET.get('search')
        questions = Person.objects.filter(first_name__contains=search)

        name = request.GET.get('name')
        query = Person.object.filter(first_name__contains=search)

    return render(request, 'contact/contact_list.html', {
        'questions': questions
    })


from django.shortcuts import render
from .models import Person
