from django.db import models

# Create your models here.
class Edu_Level(models.Model):
    Level=models.CharField(max_length=100)

    def __str__(self):
        return self.Level

class Experince_Type(models.Model):
    Exp_Type=models.CharField(max_length=100)

    def __str__(self):
        return self.Exp_Type

class Introduction(models.Model):
    Name=models.CharField('Name' , max_length=100)
    phone_number=models.CharField(' Phone Number' , max_length=11)
    email=models.EmailField(null=True, blank=True)
    About=models.TextField(null=True, blank=True)
    
    Institution_Name=models.CharField(max_length=100)
    Education_1=models.ForeignKey(Edu_Level,on_delete=models.CASCADE)
    Time=models.CharField(max_length=100)

 
    skill_1= models.CharField('Skill...' , max_length=100)
    skill_2= models.CharField('Skill...' , max_length=100, null=True, blank=True)
    skill_3= models.CharField('Skill...' , max_length=100, null=True, blank=True)
    skill_4= models.CharField('Skill...' , max_length=100, null=True, blank=True)
    skill_5= models.CharField('Skill...' , max_length=100, null=True, blank=True)

    Experience_1=models.CharField('Experinece' , max_length=100 , null=True , blank=True)
    Experince_Name1=models.ForeignKey(Experince_Type,on_delete=models.CASCADE)
    Organization_1=models.CharField('Organization /Company' ,max_length=100,null= True, blank=True)

    Experience_2=models.CharField('Experinece' , max_length=100 , null=True , blank=True)
    Experince_Name2=models.ForeignKey(Experince_Type,on_delete=models.CASCADE, related_name='+')
    Organization_2=models.CharField('Organization /Company' ,max_length=100,null= True, blank=True)

    Language_Proficiency=models.CharField(max_length=100)

    