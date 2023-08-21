# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf

import deepl
import openai
from django.conf import settings

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
import requests
import os

# 设置OpenAI API凭据
openai.api_key = 'key'
 
# 接收POST请求数据
# def search_post(request):
#     ctx ={}
#     if request.POST:
#         ctx['rlt'] = request.POST['q']
#         ctx['rlt1'] = request.POST['q']
#     return render(request, "trans.html", ctx)

from django.contrib.auth.models import User

# # 创建用户
# user = User.objects.create_user(username='zhanglinyi', password='123')
# # 或者使用 User.objects.create() 方法
# # user = User.objects.create(username='runboo')
# # user.set_password('123')

# # 保存用户密码的哈希值
# user.set_password('123')
# user.save()


def search_post(request):
    ctx ={}
    if request.POST:
        text = request.POST['q']     # "Bonjour, le monde !" # "Hello, world!"
        translator = deepl.Translator(settings.DEEPL_API_KEY)

        target_language1 = request.POST.get('target-language1', 'EN-GB')
        target_language2 = request.POST.get('target-language2', 'EN-GB')
    
        # print(target_language1, target_language2)

        if target_language1 == 'en':
            target_language1 = 'EN-GB'
        elif target_language1 == 'zh':
            target_language1 = 'ZH'
        elif target_language1 == 'de':
            target_language1 = 'DE'


        if target_language2 == 'en':
            target_language2 = 'EN-GB'
        elif target_language2 == 'zh':
            target_language2 = 'ZH'
        elif target_language2 == 'de':
            target_language2 = 'DE'


        
        target_method = request.POST.get('target_method', 'parallel')

        if target_method == 'parallel':
            target_tool1 = request.POST.get('target_tool1', 'deepl')
            print("target_tool1", target_tool1)
            if target_tool1 == 'deepl':




                result1 = translator.translate_text(text, target_lang=target_language1)
                result2 = translator.translate_text(text, target_lang=target_language2)
                # print(result1)
                # print(result2)


                # result1 = translator.translate_text(text, target_lang="EN-GB")
                # result2 = translator.translate_text(text, target_lang="ZH")

                # ctx['rlt'] = request.POST['q']
                # ctx['rlt1'] = request.POST['q']


                # ctx['rlt'] = result1
                # ctx['rlt1'] = result2
            elif target_tool1 == 'chatgpt':
                result1 = openai.Completion.create(
                    model="gpt-3.5-turbo",
                    prompt="Translate " + text +"to" + target_language1 ,
                   
                )
                result2 = openai.Completion.create(
                    model="gpt-3.5-turbo",
                    prompt="Translate " + text +"to" + target_language2 ,
                 
                )
               
                ctx['rlt'] = result1
                ctx['rlt1'] = result2
            









        elif target_method == 'streaming':
            result1 = translator.translate_text(text, target_lang=target_language1)
            result2 = translator.translate_text(result1.text, target_lang=target_language2)
        print("target_method", target_method)
        
        ctx['rlt1'] = result1
        ctx['rlt2'] = result2

    return render(request, "trans.html", ctx)




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("username", username)
        print("password", password)
        # user = authenticate(request, username=username, password=password)
        user = authenticate(username=username, password=password)
        print("user", user)
        if user is not None:
            login(request, user)
            return redirect('/home/')  # 重定向到登录后的页面
        else:
            error_message = 'Invalid login credentials'
    else:
        error_message = ''

    return render(request, 'login.html', {'error_message': error_message})


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 其他可能需要的字段

        # 创建用户
        user = User.objects.create_user(username=username, password=password)
        # 可以在这里设置其他字段的值

        # 登录用户
        login(request, user)
        return redirect('/home/')  # 重定向到注册后的页面

    return render(request, 'register.html')


def deepL_embed(request):
    # if request.method == 'POST':

    # return redirect('/https://www.deepl.com/translator/home/')
    
    return render(request, 'deepL_embed.html')
    

def deepL_test(request):
    # if request.method == 'POST':
    return render(request, 'deepL_test.html')


def redirect_to_external_website(request):
    target_url = "https://www.deepl.com/translator"  # 替换为您希望链接到的目标网站URL
    return redirect(target_url)


def show_partial_content(request):
    target_url = "https://www.deepl.com/translator/"  # 替换为您希望链接到的目标网站URL
    return render(request, 'partial_content.html', {'target_url': target_url})


def get_unique_filename(file_path):
    # 检查文件是否已存在，若存在，加上 "(1)"，"(2)" 等后缀，直至找到可用的文件名
    base_name, ext = os.path.splitext(file_path)
    counter = 1
    while os.path.exists(file_path):
        file_path = f"{base_name}({counter}){ext}"
        counter += 1
    return file_path


def translate_document(request):
    if request.method == 'POST' and request.FILES.get('file'):
        # 获取上传的文件
        uploaded_file = request.FILES['file']
        # # 读取文件内容
        # file_contents = uploaded_file.read().decode('utf-8')


        translator = deepl.Translator(settings.DEEPL_API_KEY)

        context={}

        target_language_doc = request.POST.get('target-language-doc', 'EN-GB')
        if target_language_doc == 'en':
            target_language_doc = 'EN-GB'
        elif target_language_doc == 'zh':
            target_language_doc = 'ZH'
        elif target_language_doc == 'de':
            target_language_doc = 'DE'

        # print("target_language_doc", target_language_doc)

        # original_filename = uploaded_file.name
        # print("original_filename", original_filename)

        # translated_file_path = 'C:/Users/Linyi Zhang/Downloads/Bedienungsanleitung.docx'
        # translated_file_path = original_filename
        # print("translated_file_path", translated_file_path)

        # download_path = request.POST.get('download_path', 'default_download_path')

        download_path = 'C:/Users/Linyi Zhang/Downloads'
        print("download_path", download_path)
        original_filename = uploaded_file.name
        print("original_filename", original_filename)
        translated_file_path = download_path+ '/'+ original_filename 
        print("translated_file_path", translated_file_path)

        translated_file_path = get_unique_filename(translated_file_path)
        print("translated_file_path", translated_file_path)



        try:

            with open(translated_file_path, "wb") as out_file:
                translator.translate_document(
                    uploaded_file,
                    out_file,
                    target_lang=target_language_doc
                    )
                

            context['show_translation_status'] = True
            return render(request, 'translate_document.html', context)



            
            
            # # 调用 DeepL API 进行翻译
            # deepL_api_url = 'https://api-free.deepl.com/v2/translate'
            # headers = {'Authorization': f'DeepL-Auth-Key {settings.DEEPL_API_KEY}'}
            # data = {'text': file_contents, 'target_lang': 'YOUR_TARGET_LANGUAGE'}
            # response = requests.post(deepL_api_url, headers=headers, data=data)
            # translated_text = response.json()['translations'][0]['text']
            
            # # 在页面上显示翻译结果
            # context = {'translated_text': translated_text}
            # return render(request, 'translation_app/translation_result.html', context)
        except deepl.DocumentTranslationException as error:
        # If an error occurs during document translation after the document was
        # already uploaded, a DocumentTranslationException is raised. The
        # document_handle property contains the document handle that may be used to
        # later retrieve the document from the server, or contact DeepL support.
            doc_id = error.document_handle.id
            doc_key = error.document_handle.key
            print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")
        except deepl.DeepLException as error:
        # Errors during upload raise a DeepLException
            print(error)

        context['show_translation_status'] = True
        return render(request, 'translate_document.html', context)

    return render(request, 'translate_document.html')







