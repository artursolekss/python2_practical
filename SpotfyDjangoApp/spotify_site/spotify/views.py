from django.shortcuts import render,redirect
from django.views import generic
import requests
import base64

# class IndexView(generic.TemplateView):
#     template_name = "index.html"

class LoginView(generic.TemplateView):
    template_name = "login.html"

def login_run(request):
    client_id = request.POST["client_id"]
    return redirect('https://accounts.spotify.com/authorize?response_type=code&client_id='+
                    client_id+"&redirect_uri=http://127.0.0.1:8000/spotify/login_callback")

def login_callback(request):
    return render(request,
                  "login_client_secret.html")

def generate_token(request):
    client_id = request.POST["client_id"]
    client_secret = request.POST["client_secret"]
    code = request.GET.get("code",'')
    enc_str = client_id + ":" + client_secret
    headers = {"Authorization":"Basic " + str(base64.b64encode(enc_str.encode("ascii"))),
               "Content-Type":"application/json; charset=utf-8"}
    body={"code":code,"redirect_uri":'http://127.0.0.1:8000/spotify/login_callback',
          "grant_type":"authorization_code"}
    response = requests.post("https://accounts.spotify.com/api/token",headers=headers,
                            json=body)
    json_respose = response.json()
    return render(request,"token_response.html",{
      "response":str(json_respose) 
    })

