from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    user_image=models.ImageField(upload_to='uploads/store/',default="uploads/store/71doo5dci8L._SL1200__flBZ8kI.jpg")
    password=models.CharField(max_length=500)
    birthday=models.DateField()#default=datetime.datetime.today)
    gender=models.CharField(max_length=50)
    address1=models.CharField(max_length=200,default="")
    address2=models.CharField(max_length=200,default="")
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    zipcode=models.CharField(max_length=100,default="")
    mailaddress1=models.CharField(max_length=200,default="")
    mailaddress2=models.CharField(max_length=200,default="")
    mailcity=models.CharField(max_length=100,default="")
    mailstate=models.CharField(max_length=100,default="")
    mailzipcode=models.CharField(max_length=100,default="")
    mailphone_number=models.CharField(max_length=100,default="")
    phone_number=models.CharField(max_length=100,default="")
    mailing_address=models.CharField(max_length=100)
    payment_method=models.CharField(max_length=200,default="")
    card_number=models.CharField(max_length=200,default="")
    security_code=models.CharField(max_length=100,default="")
    expiration_date=models.CharField(max_length=100,default="")
    status=models.IntegerField(default=1)
    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.filter(email=email,status=1)
        except:
            return False
    @staticmethod
    def get_all_user():
        return User.objects.all()
    @staticmethod
    def get_user_by_user_id(id):
        try:
            return User.objects.get(id=id)
        except:
            return False
    def isExists(self):
        if User.objects.filter(email=self.email):
            return True
        else:
            return False
    def savedata(self):
        self.save()


    