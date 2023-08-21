from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import deepl
# 表单
def search_form(request):
    return render(request, 'search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)



# 接收请求数据
def search_translate(request):  
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        text = request.GET['q']     # "Bonjour, le monde !" # "Hello, world!"
        translator = deepl.Translator(settings.DEEPL_API_KEY)
        result1 = translator.translate_text(text, target_lang="EN-GB")
        result2 = translator.translate_text(text, target_lang="ZH")
        message = '翻译为: ' + str(result1)+ "    " + str(result2)
    
    else:
        message = '你提交了空表单'
    return HttpResponse(message)