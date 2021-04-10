from django.db import models



class OTP(models.Model):
    useremail=models.CharField(max_length=100)
    usertype=models.CharField(max_length=50)
    otpcode=models.CharField(max_length=10)
    @staticmethod
    def get_otp_by_useremail(useremail):
        return OTP.objects.filter(useremail=useremail)
    