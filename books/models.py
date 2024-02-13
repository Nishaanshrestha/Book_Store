from django.db import models
from django.utils.text import slugify
class Country(models.Model):
     name=models.CharField(max_length=100)
     code=models.CharField(max_length=100)
     def __str__(self) :
          return f"{self.name}"

class Address(models.Model):
     city=models.CharField(max_length=100)
     state=models.IntegerField( )
     def __str__(self) :

        return f"{self.city}-{self.state}"
    

class Author (models.Model):
        name=models.CharField(max_length=100)
        age=models.IntegerField()
        address=models.OneToOneField(Address,on_delete=models.CASCADE)
        genre=models.CharField(max_length=100)
        country=models.ManyToManyField(Country)

        def __str__(self) :

            return f"{self.name}"

# class create and give name  django give built in model.Model extends cause for creat table to know django forthat we do

class Book(models.Model):
    # id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    is_bestselling=models.BooleanField(default=False)
    rating=models.FloatField("Rating")
    slug=models.SlugField(unique=True)
    published_date=models.DateField(auto_now=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title+str(self.published_date))
        super().save(*args,**kwargs)
    
    def __str__(self) :

        return f"id:{self.id} title:{self.title},rating:{self.rating}"
    

    
     
    

    
