from django.shortcuts import render, redirect

def index(request):
    """/admin以下のログイン画面以外への全てのリクエストを受け取り
        /admin/loginにリダイレクトする
    """
    return redirect('/admin/login/')
