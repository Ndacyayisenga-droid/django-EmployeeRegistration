from django.db import models



from djmoney.models.fields import MoneyField

# Create your models here.

#class emp_id(models.Model):
    #def number():
     #   no = emp_id.objects.count()
      #  if no == none:
       #     return 1
        #else:
         #   return no + 1

    #employeecode = models.IntegerField(_('Code'), max_length=6, unique=True, \
    #default=number)

class Position(models.Model):
    title = models.CharField(max_length=50)    


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=5)
    salary = MoneyField(max_digits=14, decimal_places=2)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
