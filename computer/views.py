from django.shortcuts import render,redirect
from django.views import View
from .models import Computer,ComputerSpecification
from django.contrib import messages
# import get_object_or_404()
from django.shortcuts import get_object_or_404

# Create your views here.
class Homepage (View):

    def get(self,request):
        computer=Computer.objects.all()
        context={
            'computer':computer,
        }

        return render(request,'computer/homepage.html',context)


class Create(View):

    def get(self,request):
        specification=ComputerSpecification.objects.all()
        context={
            'specification':specification,
        }

        return render(request,'computer/create.html',context)

    def post(self,request):
        computer_code=request.POST['computer_code']
        computer_id=request.POST['computer']
        computer = ComputerSpecification.objects.get(id=computer_id)
        # print(computer)
        quantity=int(request.POST['quantity'])
        unit_rate=int(request.POST['unitrate'])
        total_price=quantity*unit_rate
        computers=Computer(computer_code=computer_code,computer=computer,quantity=quantity,unit_rate=unit_rate,total_price=total_price)
        computers.save()
        messages.success(request,"Computer has been sucessfully added")
        return redirect('homepage')

class Update(View):

    def get(self,request,id):
         computer=get_object_or_404(Computer,id=id)
         specification = ComputerSpecification.objects.all()
         context={
            'computer':computer,
             'specification' : specification
        }
         return render(request,'computer/update.html',context)

    def post(self,request,id):
            computer_code = request.POST['computer_code']
            computer_id = request.POST['computer']
            computer = ComputerSpecification.objects.get(id=computer_id)
            # print(computer)
            quantity = int(request.POST['quantity'])
            unit_rate = int(request.POST['unitrate'])
            total_price = quantity * unit_rate

            computers=Computer(id=id,computer_code=computer_code,computer=computer,quantity=quantity,unit_rate=unit_rate,total_price=total_price)
            computers.save()
            messages.success(request, "Computer has been sucessfully Updated")
            return redirect('homepage')

class Delete(View):

    def get(self,request,id):
        computers=get_object_or_404(Computer, id=id).delete()
        context={
            'computers':computers
        }
        if computers:
            messages.success(request,"Computer has been deleted sucessfully")

            return redirect('homepage')









