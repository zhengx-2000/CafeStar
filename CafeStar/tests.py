from django.test import TestCase
import datetime

from CafeStar.models import User, Order, ShopStatus, Drink


# Create your tests here.

# Test User Table
class UserTest(TestCase):
    """Initialise some data"""

    def setUp(self) -> None:
        User.objects.create(UserID=1111111,
                            Manager=False,
                            Fullname='testFullName1',
                            Username='testUserName1',
                            Email='Email1',
                            Password='1231231',
                            PhoneNumber=123123,
                            Point=123)
        User.objects.create(UserID=2222222,
                            Manager=False,
                            Fullname='testFullName2',
                            Username='testUserName2',
                            Email='Email2',
                            Password='1231231',
                            PhoneNumber=123123,
                            Point=123)

    """"
    class User(models.Model):
    UserID = models.IntegerField(primary_key=True, verbose_name='UserID')
    Manager = models.BooleanField(default=False, verbose_name='Manager')
    Fullname = models.CharField(max_length=30, verbose_name='Fullname')
    Username = models.CharField(max_length=30, verbose_name='Username')
    Email = models.EmailField(max_length=30, verbose_name='Email')
    Password = models.CharField(max_length=30, verbose_name='Password')
    PhoneNumber = models.IntegerField(verbose_name='PhoneNumber')
    Point = models.IntegerField(verbose_name='Point', null=True, blank=True)"""

    def test_user_create(self):
        User.objects.create(
            UserID=3333333,
            Manager=False,
            Fullname='testFullName',
            Username='testUserName',
            Email='Email',
            Password='1231231',
            PhoneNumber=123123,
            Point=123
        )
        p = User.objects.get(UserID=3333333)
        print(p.UserID)
        print(p.Manager)
        print(p.Fullname)
        print(p.Username)
        print(p.Email)
        print(p.Password)
        print(p.PhoneNumber)
        print(p.Point)
        self.assertEqual(p.Fullname, 'testFullName')
        self.assertEqual(p.Username, 'testUserName')


    def test_user_delete(self):
        p = User.objects.get(UserID=2222222)
        p.delete()
        ret = User.objects.filter(UserID=2222222)

        self.assertEqual(len(ret),0)

    def test_user_update(self):
        p = User.objects.get(UserID=2222222)
        p.UserID = 1234567
        p.save()
        ret = User.objects.filter(UserID=1234567)
        self.assertEqual(len(ret),1)





    """   
    OrderID = models.IntegerField(primary_key=True, verbose_name='OrderID')
    UserID = models.IntegerField(verbose_name='UserID')
    DrinkID = models.IntegerField(verbose_name='DrinkID', null=True, blank=True)
    Status = models.BooleanField(default=False, verbose_name='Status')
    Drink = models.CharField(max_length=30, verbose_name='Drink')
    Sweetness = models.CharField(max_length=10, verbose_name='Sweetness', null=True, blank=True)
    Milk = models.CharField(max_length=10, verbose_name='Milk', null=True, blank=True)
    PickupTime = models.TimeField(verbose_name='PickupTime')
    Price = models.IntegerField(verbose_name='Price')
    Point = models.IntegerField(verbose_name='Point')
    """

    def test_order(self):
        Order.objects.create(
            OrderID=3333333,
            UserID=3333333,
            DrinkID=3333333,
            Status=False,
            Drink='Drink',
            Sweetness='Sweetness',
            Milk='123123',
            PickupTime=datetime.datetime(2023, 3, 21, 20, 41, 30),
            Price=10,
            Point=1
        )
        order = Order.objects.get(OrderID=3333333)
        print(order.OrderID)
        print(order.UserID)
        print(order.DrinkID)
        print(order.Status)
        print(order.Drink)
        print(order.Sweetness)
        print(order.Milk)
        print(order.PickupTime)
        print(order.Price)
        print(order.Point)
        self.assertEqual(order.OrderID, 3333333)
        self.assertEqual(order.UserID, 3333333)

    """    
    DrinkID = models.IntegerField(primary_key=True, verbose_name='DrinkID')
    Name = models.CharField(max_length=30, verbose_name='Name')
    Picture = models.ImageField(upload_to='drink_images/',
                                verbose_name='Picture')  # Here is a directory to store drinks pictures
    Description = models.CharField(max_length=100, verbose_name='Description')
    Nutrition = models.CharField(max_length=100, verbose_name='Nutrition', null=True, blank=True)
    Ingredients = models.CharField(max_length=100, verbose_name='Ingredients', null=True, blank=True)
    Price = models.IntegerField(verbose_name='Price')
    Point = models.IntegerField(verbose_name='Point')
    Rating = models.FloatField(verbose_name='Rating', null=True, blank=True)
    """

    def test_drink(self):
        Drink.objects.create(
            DrinkID=3333333,
            Name='Drink',
            Picture='drink_images/',
            Description='Description',
            Nutrition='123123',
            Ingredients='Ingredients',
            Price=1,
            Point=1,
            Rating=1.1
        )
        drink = Drink.objects.get(DrinkID=3333333)
        print(drink.DrinkID)
        print(drink.Name)
        print(drink.Picture)
        print(drink.Description)
        print(drink.Nutrition)
        print(drink.Ingredients)
        print(drink.Point)
        print(drink.Rating)

        self.assertEqual(drink.DrinkID, 3333333)
        self.assertEqual(drink.Name, 'Drink')


    """   
    OpenTime = models.DateTimeField(verbose_name='OpenTime')
    CloseTime = models.DateTimeField(verbose_name='CloseTime')
    OrderCount = models.IntegerField(verbose_name='OrderCount')
    NextOrderID = models.IntegerField(verbose_name='NextOrderID')
    """
    def test_shop(self):
        ShopStatus.objects.create(
            OpenTime=datetime.datetime(2023, 3, 21, 20, 41, 30),
            CloseTime=datetime.datetime(2023, 3, 21, 20, 41, 30),
            OrderCount=10,
            NextOrderID=1
        )
        shop = ShopStatus.objects.get(OrderCount=10)
        print(shop.OpenTime)
        print(shop.CloseTime)
        print(shop.OrderCount)
        print(shop.NextOrderID)

        self.assertEqual(shop.NextOrderID, 1)
