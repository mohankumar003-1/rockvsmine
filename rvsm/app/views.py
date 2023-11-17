from django.shortcuts import render
from .code import predicts
def main(request):
     if request.method == 'POST':
          a = request.POST.get('input1')
          b = request.POST.get('input2')
          c = request.POST.get('input3')
          d = request.POST.get('input4')
          e = request.POST.get('input5')
          f = request.POST.get('input6')
          ans =  predicts(a,b,c,d,e,f)
          if(ans == 1):
               print("here")

               return render(request,'index.html',{'ans': ans})
          else:
               print("here2")
               return render(request,'index.html',{'ans': ans})
          
     return render(request,'index.html')
