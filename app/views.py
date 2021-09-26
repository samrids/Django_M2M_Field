from django.shortcuts import render
from app.models import Book
from app.forms import CreateBookForm

def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)

        if form.is_valid():
            title   =  form.cleaned_data['title'] 
            authors =  form.cleaned_data['authors']
            book    = Book(title  = title)
            try:
                book.save()
                book.authors.set(authors)
                msg = 'save ok'
            except Exception as e:
                msg  =  'Found somthing when wrong'
                      
            return render(request, 'msg.html', {'msg':msg})
        else:
            return render(request, 'msg.html', {'msg':' form error'})

    else:
        form = CreateBookForm()

    return render(request, 'book.html', {'form': form})

