from django.db import models
from django.contrib.auth.models import User

class  TechType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='techtype'

class product(models.Model):
    productname=models.CharField(max_length=255)
    producttype=models.ForeignKey(TechType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    price=models.DecimalField(max_digits='6', decimal_places=2)
    productURL=models.URLField()
    description=models.TextField()

    def __str__(self):
        return self.productname

        class Meta:
            db_table='product'

class Review(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(product, on_delete=models.CASCADE)
    reviewdate=models.DateField()
    reviewtext=models.TextField()

    def discountAmount(self):
        disc=self.discountAmount()
        self.discountedprice=self.price-disc* .05
        return self.discount

# it is almost working
    def discountProce(self):
        self. discountedPrice=self.price-self.discount
        return self.price * .05

       #def discountProce(self):

    def __str__(self):
        return self.productname

    def __str__(self):
        return self.title

    class Meta:
        db_table='review'

