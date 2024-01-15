from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse
from.models import blog
from .forms import Postform
# Create your views here.
def show_data(request):
    data=blog.objects.all()
    fm=Postform()   
    return render(request,'myapp/home.html',{'form':fm,'data':data})

def Save_form(request):
    if request.method == 'POST':
        fm = Postform(request.POST)
        if fm.is_valid():
            sid = request.POST.get('stuid')
            title = request.POST['title']
            dis = request.POST['dis']
            if (sid == ''):
                usr = blog(id=sid,title=title, dis=dis)
            else:  
                usr = blog(id=sid, title=title, dis=dis)
                usr.save()
                stud = blog.objects.values()
                student_data = list(stud)
                return JsonResponse({'status': 'Save', 'student_data': student_data})
        else:
            return JsonResponse({'status': 0})
    else:
        return JsonResponse({'status': 0})





###delete
def delete_data(request):
    if request.method =="POST":
        id = request.POST.get('sid')
        print(id)
        pi = blog.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})

#Edit Data
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        student = blog.objects.get(pk=id)
        student_data = {"id":student.id,"title":student.title,"dis":student.dis}
        return JsonResponse(student_data)          


# def delete_data(request,id):
#    if request.method=='POST':
#       d=blog.objects.get(pk=id)
#       d.delete()
#       return JsonResponse({'status':1})
#    else:
#       return JsonResponse({'status':0})