def logout_page(request):
    logout(request)
    return redirect('/login/')