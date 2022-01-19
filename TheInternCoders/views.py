
from django.shortcuts import render
from .settings import BASE_DIR
import time
def Index(request):
    return render(request, "index.html")



def Admission(request):
    if request.method == "POST":
        db_file = open(str(BASE_DIR)+"\\dbms.csv", "a")
        Name = request.POST.get('name')
        Number = request.POST.get("number")
        Course1 = request.POST.get("course")
        Course2 = request.POST.get("secondCourse")
        print(Name, Number, Course1, Course2)
        db_file.write(Name+","+Number+","+Course1+","+Course2+"\n")
        db_file.close()
        return render(request,"admission.html")

    return render(request, "admission.html")
# Thread(target = update_file,args = (db_file,)).start()