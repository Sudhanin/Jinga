from django.shortcuts import render,redirect
from medium import Client
import os
# Create your views here.
def post(request):
    return render(request,'index.html')
def publish(request):
    if request.method=="POST":
       title=request.POST["title"]
       imgloc=request.POST["img_loc"]
       content=request.POST["message"]
       client=Client(application_id="bd2220b27e6a",application_secret="5ea5ccec18e6b7d12466900d47417fdcc52f352f")
       client.access_token="2a0432ffe8985834d0f939991291b6d589eef0684b425e8fce1c964a7e0be1263"
       user=client.get_current_user()
       imgup=client.upload_image(file_path=os.path.join('D:\\IV\\One plus\\Photos',imgloc),content_type="image/jpeg")
       url=imgup['url']
       content="<img src="+url+"><p>"+content+ "</p>"
       post=client.create_post(user_id=user["id"], title=title,content=content,content_format="html")
       return render(request,'blank.html',post)
    else:
     return render(request,'index.html')