from django.shortcuts import render,redirect
from django.views import generic
import requests
import base64

base_url = 'https://api.spotify.com/v1/'

# class IndexView(generic.TemplateView):
#     template_name = "index.html"

class LoginView(generic.TemplateView):
    template_name = "login.html"

# def login_run(request):
#     client_id = request.POST["client_id"]
#     return redirect('https://accounts.spotify.com/authorize?response_type=code&client_id='+
#                     client_id+"&redirect_uri=http://127.0.0.1:8000/spotify/login_callback")

# def login_callback(request):
#     return render(request,
#                   "login_client_secret.html")

def generate_token(request):
    client_id = request.POST["client_id"]
    client_secret = request.POST["client_secret"]
    # code = request.GET.get("code",'')
    # enc_str = client_id + ":" + client_secret
    # headers = {"Authorization":"Basic " + str(base64.b64encode(enc_str.encode("ascii"))),
    #            "Content-Type":"application/json; charset=utf-8"}
    body={"grant_type":"client_credentials",
          "client_id":client_id,
          "client_secret":client_secret}
    response = requests.post("https://accounts.spotify.com/api/token",body)
    json_respose = response.json()
    access_token = json_respose.get("access_token")
    request.session["token"] = access_token
    return redirect("/spotify/home?token="+str(access_token))

class HomeView(generic.TemplateView):
    template_name = "home.html"

def results(request):
    # token=request.GET.get("token")
    token = request.session["token"]
    headers = {
        "Authorization":'Bearer {}'.format(token)
    }
    value = request.POST["value"]
    type_name = request.POST["type"]
    search_url = base_url + "search?"+'q={}'.format(value) + '&type={}'.format(type_name)
    response = requests.get(search_url,headers=headers)
    results = response.json()

    if type_name == "artist":
        result_artists = results.get("artists").get("items")
        return render(request,"search_results.html",{"artists":result_artists})
    elif type_name == "track":
        result_tracks = results.get("tracks").get("items")
        return render(request,"search_results.html",{"tracks":result_tracks})
    elif type_name == "album":
        result_albums = results.get("albums").get("items")
        return render(request,"search_results.html",{"albums":result_albums})

