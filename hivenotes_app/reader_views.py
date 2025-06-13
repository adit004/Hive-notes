from django.shortcuts import redirect, render

from hivenotes_app.forms import LoginRegister, ReaderRegister


def reader_registor(request):
    login_form = LoginRegister()
    reader_form = ReaderRegister()

    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        reader_form = ReaderRegister(request.POST)
        if login_form.is_valid() and reader_form.is_valid():
            reader = login_form.save(commit=False)
            reader.is_customer = True
            reader.save()

            user1 = reader_form.save(commit=False)
            user1.user = reader
            user1.save()
            return redirect('/')
    return render(request, "reader/registor.html", {'login_form': login_form, 'reader_form': reader_form})

