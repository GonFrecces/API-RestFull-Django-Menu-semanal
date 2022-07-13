from django.db import models

# Create your models here.

class Menu(models.Model):
    Id_dia_semana = models.AutoField(primary_key=True,serialize=True,verbose_name='Id_dia_semana')
    dias = {
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Juves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    }
    Dia = models.CharField(max_length=60,blank=True, null=True, choices=dias)


    def __str__(self):
        return '%s' %(self.Dia)



class Plato(models.Model):
    Id_plato = models.AutoField(primary_key=True,serialize=True,verbose_name='Id_plato')
    Nombre = models.CharField(max_length=60, blank=True, null=True)
    Menu = models.ForeignKey(Menu, related_name='plato',on_delete=models.CASCADE)

    def __str__(self):
        return '%s' %(self.Nombre)


class Ingredientes(models.Model):
    Plato = models.ForeignKey(Plato, related_name='ingredientes',on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=60, blank=True, null=True)
    

    def __str__(self):
        return '%s' %(self.Nombre)





