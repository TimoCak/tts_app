from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import Context, loader
from django.views.decorators.csrf import csrf_protect
from . import tts_coqui

# Create your views here.
@csrf_protect
def tts(request: HttpRequest):
    print("WELCOME TO TTS")
    template = loader.get_template("tts.html")
    return HttpResponse(template.render(request=request, context={'singlespeaker': tts_coqui.context}))

@csrf_protect
def tts_post(request: HttpRequest):
    if request.method == 'POST':
        singlespeaker = dict(
            model=request.POST.get('model', None),
            emotion=request.POST.get('emotion', None),
            speed=request.POST.get('speed', None),
            text=request.POST.get('text', None)
        )
        tts_coqui.do_voicing(singlespeaker['model'],singlespeaker['emotion'],singlespeaker['speed'], singlespeaker['text'])
        return HttpResponseRedirect('/tts')   
    else: 
        return HttpResponse("HELLO MY GUYS")