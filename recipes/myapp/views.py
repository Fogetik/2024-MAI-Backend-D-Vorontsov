from django.shortcuts import render
from django.http import JsonResponse 
from django.db.models import Q
from django.utils import timezone
from .models import News
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def profile(request):
    return JsonResponse({'name':request.user.username})


def allNews(request):
    if request.method == 'GET':
        result = []
        a = News.objects.all()
        for a_w in a:
            result.append({'id': a_w.id, 
                        'title':a_w.title,
                        'description':a_w.description,
                        'author_id':a_w.author_id,
                        'date' : a_w.created_at})
        
        print(result)
        return JsonResponse(result, safe=False)
    else:
            return JsonResponse({'error': 'Only GET requests are allowed'})
        

    

def findNews(request):
    if request.method == 'GET':
        result = []
        param_title = request.GET.get('title')
        param_description = request.GET.get('description')

        filter_conditions = Q()

        if param_title:
            filter_conditions |= Q(title__icontains=param_title) 

        if param_description:
            filter_conditions |= Q(description__icontains=param_description) 


        if filter_conditions != Q():
            a = News.objects.filter(filter_conditions)
            for a_w in a:
                result.append({'id': a_w.id, 
                                'title':a_w.title,
                                'description':a_w.description,
                                'author_id':a_w.author_id,
                                'date' : a_w.created_at})
                
            print('a')
            print(filter_conditions)
            print(a)
            return JsonResponse(result, safe=False)
                
        return allNews(request)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'})
    
@csrf_exempt
def newNews(request):
    if request.method == 'POST':
        new_object = News.objects.create(title=request.POST['title'],
                                        description=request.POST['description'],
                                        author=User.objects.get(pk=int(request.POST['author'])),
                                        created_at=timezone.now())
        return JsonResponse({'status': 'success', 'id': new_object.id})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
    