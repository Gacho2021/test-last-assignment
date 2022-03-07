from django.test import TestCase
from django.config.models import user
from .models import TechType, product, Review
import datetime
from  .forms import ProdiuctForm
from django.urls import reverse_lazy, reverse
# Create your tests here.
class TechTypeTest(TestCase):
 def setup(self):
    self.type=TechType(typename='Lenovo Laptop')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Lenovo Laptop')

        def test_tablename(self):
            self.assertEqual(str(TechType._meta.db_table), 'techtype')

class productTest(TestCase):
 def setup(self):
    self.type=TechType(typename='Laptop')
    self.user=user(username='user1')
    self.product= product(productname='Lenovo',producttype=self.type, user=self.user, dateentered=date('2/10/2021'),price=1200.99,producturl='http://www.lenovo.com',description="lenovo Laptop")

def test_string(self):
        self.assertEqual(str(product), 'Lenovo')

def test_discount(self):
    disc = self.product.price * .05
    self.assertEqual(self.product.discountAmount(), disc)

def test_discountAmount(self):
    disc=self.product.price * (1 -.05)
    self.assertEqual(self.product.discountPrice(),disc)
class newProductForm(TestCase):
        #valid form data
    def test_productForm(self):
            data={
            'productname':':surface',
                'producttype' :'labtop', 
                'user':'Tegen''dateentered''February 28, 2022',
                'price': '1200'
                'producturl' 'https://www.microsoft.com'
                'discription''half laptob half tablet'
    }
        
form=ProductForm (data)
self.assertTrue(form.is_valid)
def test_productForm_Invalid(self):
 data={
            'productname':':surface',
                'producttype' :'labtop', 
                'user':'Tegen''dateentered''2022-28-2',
                'producturl': 'https://www.microsoft.com',
                'discription':'half laptob half tablet'
    }
form=ProductForm (data)
self.assertFalse(form.is_valid)
class New_Product_Authentication_Test(TestCase):
    def setup(self):
        self.test_user=User .objects.create_user(username='testuser1', password='P@ssw0rd1')
    self.type=Type.objects.create(typename='laptop')
    self.product=Product.objects.create(productname='Lenovo',producttype=self.type, user=self.test_user, dateentered=date('2/10/2021'),price=1200.99,producturl='http://www.lenovo.com',description="lenovo Laptop")

    def test_redirect_if_not_logged_in(self):
        response.self.client.get(reverse('newproduct'))
        self.assertRedirects(response,'accounts/login/?next=club/newproduct')