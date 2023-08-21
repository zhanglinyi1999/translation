# from django.http import HttpResponse

# # def index(request):
# #     return HttpResponse("请求路径:{}" .format(request.path))

# def hello(request):
#     return HttpResponse("Hello world ! ")


from django.shortcuts import render
 
def runoob(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)

# def runoob(request):
#   views_name = "菜鸟教程"
#   return  render(request,"runoob.html", {"name":views_name})







# import requests
# from django.conf import settings
# from django.http import JsonResponse
# import deepl
# from django.http import HttpResponse

# def translate_text(request):
#     # 获取要翻译的文本
#     # text = request.GET.get('text', '')
#     text = "Bonjour, le monde !" # "Hello, world!"
#     translator = deepl.Translator(settings.DEEPL_API_KEY)
#     result2 = translator.translate_text(text, target_lang="ZH")
#     return HttpResponse(result2)



#     if not text:
#         return JsonResponse({'error': 'No text provided.'})

#     # 构建翻译请求的参数
#     params = {
#         'auth_key': settings.DEEPL_API_KEY,
#         'text': text,
#         'target_lang': 'ZH',
#         # 这里将 'TARGET_LANGUAGE_CODE' 替换为目标语言的代码，如 'EN' 表示英语
#     }

#     # 发送翻译请求到 DeepL API
#     response = requests.get(settings.DEEPL_API_BASE_URL, params=params)

#     if response.status_code == 200:
#         # 提取翻译结果
#         translation = response.json()['translations'][0]['text']
#         return JsonResponse({'translation': translation})
#     else:
#         return JsonResponse({'error': 'Translation failed.'})