from django.shortcuts import render,redirect
from .models.product import Product
from .models.user import User
from .models.otp import OTP
from .models.store import Store
from .models.driver import Driver
from .models.category import Category
from .models.coupon import Coupon
from .models.subcategory import Subcategory
from .models.advertising import Advertising
from .models.shopcategory import Shopcategory
from .models.order import Order
from .models.chat import Chat
from .models.driverorderpickup import Driverorderpickup
from .models.like import Like
from .models.notification import Notification
from .models.productfilter import Productfilter
from .models.attribute import Productattribute
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from boltons import iterutils
import datetime
from django.conf import settings
from django.core.mail import send_mail
import random
import stripe
from .models.chat import ChatSerializer
stripe.api_key = "sk_test_51H6HtIBIRW4ci3Bh2WYF9bkxfJZydcTVgosqEVhzlsrDS2fhgmMFd3bCo6Rn7bFgx6TtOZLYKgX8zI1ltidHvja600x1w3CRGz"
# Create your views here.


def sendmail(request,subject,msg,to):
    print(subject,msg,to,settings.EMAIL_HOST_USER)
    send_mail(
        subject,
        msg,
        settings.EMAIL_HOST_USER,
        [to],
        fail_silently=False
    )

# def login_google(request):
#     print(request.POST.get('username'))
    
#     return redirect('/storepage')

def index(request):
    print(request.POST.get('username'))
    #if request.POST.get('username')==None:
        
    return redirect('/UserLogin') #render(request,'index.html')
def login(request):
    print("login",request.POST)
    if request.POST.get('username'):
        request.session['user_name']=request.POST.get('username')
        return redirect('/storepage')
    else:
        return redirect('/UserLogin')
def UserSignUp(request):
    if request.session.get('user_id'):
        return redirect('/storepage')
    try:
        if request.method=="POST":

            message=[]
            postData=request.POST
            if(not postData.get('first_name')):
                message.append("Please enter first name")
            else:
                first_name=postData.get('first_name')
            if(not postData.get('last_name')):
                message.append("Please enter last name")
            else:
                last_name=postData.get('last_name')
            user_image=None#request.FILES['file']
            if(not postData.get('email')):
                message.append("Please enter email")
            else:
                email=postData.get('email')
            if(not postData.get('password')):
                message.append("Please enter password")
            else:
                password=postData.get('password')
            if(not postData.get('birthday')):
                message.append("Please enter birthday")
            else:
                birthday=postData.get('birthday')
            if(not postData.get('gender')):
                message.append("Please enter gender")
            else:
                gender=postData.get('gender')
            if(not postData.get('address1')):
                message.append("Please enter address1")
            else:
                address1=postData.get('address1')
            if(not postData.get('address2')):
                address2=""#message.append("Please enter address2")
            else:
                address2=postData.get('address2')
            if(not postData.get('city')):
                message.append("Please enter city")
            else:
                city=postData.get('city')

            if(not postData.get('state')):
                message.append("Please enter state")
            else:
                state=postData.get('state')
            if(not postData.get('zipcode')):
                message.append("Please enter zipcode")
            else:
                zipcode=postData.get('zipcode')
            if(not postData.get('phone_number')):
                message.append("Please enter phone_number")
            else:
                phone_number=postData.get('phone_number')
            if(not postData.get('mailing_address')):
                message.append("Please enter mailing address")
            else:
                mailing_address=postData.get('mailing_address')
            if(not postData.get('Digital_wallet')):
                Digital_wallet=""#message.append("Please enter Digital wallet")
            else:
                Digital_wallet=postData.get('Digital_wallet')
            if(not postData.get('Credit_Debit')):
                message.append("Please enter Credit Debit Number")
            else:
                Credit_Debit=postData.get('Credit_Debit')
            if(not postData.get('Credit_Debit')):
                message.append("Please enter card number")
            else:
                card_number=postData.get('Credit_Debit')
            if(not postData.get('security_code')):
                message.append("Please enter secuirity code")
            else:
                security_code=postData.get('security_code')
            if(not postData.get('Exp_Date')):
                message.append("Please enter Exp diary")
            else:
                Exp_Date=postData.get('Exp_Date')
            print(len(message))
            if(len(message)) > 0:
                return render(request,'User/userregister.html',{'message':message,'data':postData})
            if mailing_address=="YES":
                mailaddress1=address1
                mailaddress2=address2
                mailcity=city
                mailstate=state
                mailzipcode=zipcode
                mailphone_number=phone_number
            else:
                mailaddress1=postData.get('mailaddress1')
                mailaddress2=postData.get('mailaddress2')
                mailcity=postData.get('mailcity')
                mailstate=postData.get('mailstate')
                mailzipcode=postData.get('mailzipcode')
                mailphone_number=postData.get('mailphone_number')

            #if not first_name and not last_name and not email and not password and not birthday and not gender and not address1 and not address2 and not city and not state and not zipcode and not phone_number and not mailing_address and not Digital_wallet and not Credit_Debit and not card_number and not security_code and not Exp_Date:
            


            print(first_name,last_name,email,birthday,gender,address1,address2,city,state,zipcode,phone_number,mailing_address,Digital_wallet,Credit_Debit,card_number,security_code,Exp_Date)
            data={
                "first_name":first_name,
                "last_name":last_name,
                "email":email,
                "birthday":birthday,
                "gender":gender,
                "address1":address1,
                "address2":address2,
                "city":city,
                "state":state,
                "zipcode":zipcode,
                "phone_number":phone_number,
                "mailing_address":mailing_address

            }
            #try:
            user=User(first_name=first_name,
                    last_name=last_name,
                    user_image=user_image,
                    email=email,
                    password=make_password(password),
                    birthday=birthday,
                    gender=gender,
                    address1=address1,
                    address2=address2,
                    city=city,
                    state=state,
                    zipcode=zipcode,
                    phone_number=phone_number,
                    mailing_address=mailing_address,
                    mailaddress1=mailaddress1,
                    mailaddress2=mailaddress2,
                    mailcity=mailcity,
                    mailstate=mailstate,
                    mailzipcode=mailzipcode,
                    mailphone_number=mailphone_number,
                    payment_method=Digital_wallet,
                    card_number=card_number,
                    security_code=security_code,
                    expiration_date=Exp_Date,
                    status=1)
            if user.isExists():
                message.append('Account already exists')
                return render(request,'User/userregister.html',{'message':message,'data':postData})
            user.save()
            request.session['user_id']=user.id
            print("Saved")
            return redirect('/storepage')
            #return render(request,'index.html',{'message':'Successfully Registered'})
            # except :
            #     return render(request,'userregister.html',{'message':'Registration Error','data':data})
        return render(request,'User/userregister.html')

    except Exception as e:
        return render(request,'User/userregister.html')
    
def userLogin(request):
    # try:
    print("session id",request.session.get('user_id'))
    print("session_name",request.session.get('user_name'))
    # if request.session.get('user_id') == None:
    #     print("user", request.session.get('user_id'))
    #     return render(request,'User/userlogin.html')
    # if request.session.get('user_name') == None:

    #     print("usern",request.session.get('user_name'))
    #     return render(request,'User/userlogin.html')
    if request.session.get('user_id'):
        return redirect('/storepage')
    if request.session.get('store_id'):
        return redirect('/StoreDashBoard')
    stores=Store.get_all_stores()
    numberofstore=len(stores)
    if request.method=="POST":
        
        postData=request.POST
        email=postData.get('email')
        password=postData.get('password')
        print(email,password)
        user=User.get_user_by_email(email)
        message=[]
        print("user password",user.get().password)
        if user:

            print("user password",user.get().password)
           
            if check_password(password,user.get().password):
                request.session['user_id']=user.get().id
                print("Login Success full")
                return redirect('/storepage')
            else:
                message.append("credential error")
                username=request.session.get('user_name')
                if request.session.get('user_name')==None:
                    username="none"
                    
                return render(request,'User/userlogin.html',{'numberofstore':numberofstore,'message':message,'username':username})
        else:
            message.append("credential error")
            username=request.session.get('user_name')
            if request.session.get('user_name')==None:
                username="none"
            return render(request,'User/userlogin.html',{'numberofstore':numberofstore,'message':message,'username':username})       
    else:
        username=request.session.get('user_name')
        if request.session.get('user_name')==None:
            username="none"
        return render(request,'User/userlogin.html',{'numberofstore':numberofstore,'username':username})
    # except Exception as e:
    #     pass

def UserUpdate(request):
    if not request.session.get('user_id'):
        return redirect('/')
    user=User.get_user_by_user_id(request.session.get('user_id'))
    userac=User.get_user_by_user_id(request.session.get('user_id'))
    try:
        
        print(user)
        if request.method=="POST":

            message=[]
            postData=request.POST
            if(not postData.get('first_name')):
                message.append("Please enter first name")
            else:
                first_name=postData.get('first_name')
            if(not postData.get('last_name')):
                message.append("Please enter last name")
            else:
                last_name=postData.get('last_name')
            user_image=None#request.FILES['file']
            if(not postData.get('email')):
                message.append("Please enter email")
            else:
                email=postData.get('email')
            if(not postData.get('password')):
                message.append("Please enter password")
            else:
                password=postData.get('password')
            if(not postData.get('birthday')):
                message.append("Please enter birthday")
            else:
                birthday=postData.get('birthday')
            if(not postData.get('gender')):
                message.append("Please enter gender")
            else:
                gender=postData.get('gender')
            if(not postData.get('address1')):
                message.append("Please enter address1")
            else:
                address1=postData.get('address1')
            if(not postData.get('address2')):
                message.append("Please enter address2")
            else:
                address2=postData.get('address2')
            if(not postData.get('city')):
                message.append("Please enter city")
            else:
                city=postData.get('city')

            if(not postData.get('state')):
                message.append("Please enter state")
            else:
                state=postData.get('state')
            if(not postData.get('zipcode')):
                message.append("Please enter zipcode")
            else:
                zipcode=postData.get('zipcode')
            if(not postData.get('phone_number')):
                message.append("Please enter phone_number")
            else:
                phone_number=postData.get('phone_number')
            if(not postData.get('mailing_address')):
                message.append("Please enter mailing address")
            else:
                mailing_address=postData.get('mailing_address')
            if(not postData.get('Digital_wallet')):
                message.append("Please enter Digital wallet")
            else:
                Digital_wallet=postData.get('Digital_wallet')
            if(not postData.get('Credit_Debit')):
                message.append("Please enter Credit Debit Number")
            else:
                Credit_Debit=postData.get('Credit_Debit')
            if(not postData.get('Credit_Debit')):
                message.append("Please enter card number")
            else:
                card_number=postData.get('Credit_Debit')
            if(not postData.get('security_code')):
                message.append("Please enter secuirity code")
            else:
                security_code=postData.get('security_code')
            if(not postData.get('Exp_Date')):
                message.append("Please enter Exp diary")
            else:
                Exp_Date=postData.get('Exp_Date')
            print(len(message))
            if(len(message)) > 0:
                return render(request,'User/profile_update.html',{'message':message})
            if mailing_address=="YES":
                mailaddress1=address1
                mailaddress2=address2
                mailcity=city
                mailstate=state
                mailzipcode=zipcode
                mailphone_number=phone_number
            else:
                mailaddress1=postData.get('mailaddress1')
                mailaddress2=postData.get('mailaddress2')
                mailcity=postData.get('mailcity')
                mailstate=postData.get('mailstate')
                mailzipcode=postData.get('mailzipcode')
                mailphone_number=postData.get('mailphone_number')

            #if not first_name and not last_name and not email and not password and not birthday and not gender and not address1 and not address2 and not city and not state and not zipcode and not phone_number and not mailing_address and not Digital_wallet and not Credit_Debit and not card_number and not security_code and not Exp_Date:
            


            print(first_name,last_name,email,birthday,gender,address1,address2,city,state,zipcode,phone_number,mailing_address,Digital_wallet,Credit_Debit,card_number,security_code,Exp_Date)
            data={
                "first_name":first_name,
                "last_name":last_name,
                "email":email,
                "birthday":birthday,
                "gender":gender,
                "address1":address1,
                "address2":address2,
                "city":city,
                "state":state,
                "zipcode":zipcode,
                "phone_number":phone_number,
                "mailing_address":mailing_address

            }
            #try:
            
            user.first_name=first_name,
            user.last_name=last_name,
            user.user_image=user_image,
            user.email=email,
            user.password=make_password(password),
            user.birthday=birthday,
            user.gender=gender,
            user.address1=address1,
            user.address2=address2,
            user.city=city,
            user.state=state,
            user.zipcode=zipcode,
            user.phone_number=phone_number,
            user.mailing_address=mailing_address,
            user.mailaddress1=mailaddress1,
            user.mailaddress2=mailaddress2,
            user.mailcity=mailcity,
            user.mailstate=mailstate,
            user.mailzipcode=mailzipcode,
            user.mailphone_number=mailphone_number,
            user.payment_method=Digital_wallet,
            user.card_number=card_number,
            user.security_code=security_code,
            user.expiration_date=Exp_Date,
            user.status=1
            user.save()
            request.session['user_id']=user.id
            print("Saved")
            return redirect('/storepage')
            #return render(request,'index.html',{'message':'Successfully Registered'})
            # except :
            #     return render(request,'userregister.html',{'message':'Registration Error','data':data})
        elif request.method=="GET":
            return render(request,'User/profile_update.html',{'data':user,'userac':userac})

    except Exception as e:
        return render(request,'User/profile_update.html',{'data':user})
def ForgetPassword(request):
    if request.method=="POST":

        email=request.POST.get('email')
        userac=User.get_user_by_email(email)
        if userac:

            #userac=User.get_user_by_user_id(request.session.get('user_id'))
            otps=OTP.get_otp_by_useremail(email)
            if otps:
                print(otps)
                if len(otps)>0:
                    print("otp list")
                    for otp in otps:
                        if(otp.useremail==email) and (otp.usertype=="User"):
                            code=''.join(random.choice('0123456789') for _ in range(6))
                            otp.otpcode=code
                            otp.save()
                            sendmail(request,"OTP Send","otp is"+code,email)
                            break
            else:
                print("new otp")
                code=''.join(random.choice('0123456789') for _ in range(6))
                otp=OTP(useremail=email,usertype="User",otpcode=code)
                sendmail(request,"OTP Send","otp is"+code,email)
                otp.save()
            return render(request,'User/otpverification.html',{'email':email})
        else:
            return render(request,'User/forgetpassword.html',{'message':"This email is not registered"})
    else:
        return render(request,'User/forgetpassword.html')
    
def SetPassword(request):
    if request.method=="POST":
        email=request.POST.get('email')
        otpcode=request.POST.get('otp')
        password=request.POST.get('password')
        otps=OTP.objects.all()
        message="failed"
        if len(otps)>0:
            for otp in otps:
                if(otp.useremail==email) and (otp.usertype=="User") and (otp.otpcode==otpcode):
                    userac=User.get_user_by_email(email)
                    for user in userac:
                        user.password=make_password(password)
                        user.save()
                    message="success change password"
                    break
        print(message)
        return redirect('/UserLogin')




def Userlogout(request):
    if request.session.get('user_id'):
        del request.session['user_id']
    if request.session.get('user_name'):
        del request.session['user_name']
    
    print("user_id",request.session.get('user_id'),"user_name",request.session.get('user_name'))
    return redirect('/')

def UserProfileUpdate(request):
    #try:
    if not request.session.get('user_id'):
       return redirect('/')
    user=User.get_user_by_user_id(request.session.get('user_id'))
    userac=User.get_user_by_user_id(request.session.get('user_id'))
    #try:
        
    print(user)
    if request.method=="POST":

        message=[]
        postData=request.POST
        if(not postData.get('first_name')):
            message.append("Please enter first name")
        else:
            first_name=postData.get('first_name')
        if(not postData.get('last_name')):
            message.append("Please enter last name")
        else:
            last_name=postData.get('last_name')
        #user_image=None#request.FILES['file']
        if(not postData.get('email')):
            message.append("Please enter email")
        else:
            email=postData.get('email')
        if(not postData.get('password')):
            message.append("Please enter password")
        else:
            password=postData.get('password')
        if(not postData.get('birthday')):
            message.append("Please enter birthday")
        else:
            birthday=postData.get('birthday')
        if(not postData.get('gender')):
            message.append("Please enter gender")
        else:
            gender=postData.get('gender')
        if(not postData.get('address1')):
            message.append("Please enter address1")
        else:
            address1=postData.get('address1')
        if(not postData.get('address2')):
            message.append("Please enter address2")
        else:
            address2=postData.get('address2')
        if(not postData.get('city')):
            message.append("Please enter city")
        else:
            city=postData.get('city')

        if(not postData.get('state')):
            message.append("Please enter state")
        else:
            state=postData.get('state')
        if(not postData.get('zipcode')):
            message.append("Please enter zipcode")
        else:
            zipcode=postData.get('zipcode')
        if(not postData.get('phone_number')):
            message.append("Please enter phone_number")
        else:
            phone_number=postData.get('phone_number')
        if(not postData.get('mailing_address')):
            message.append("Please enter mailing address")
        else:
            mailing_address=postData.get('mailing_address')
        if(not postData.get('Credit_Debit')):
            message.append("Please enter Credit Debit Number")
        else:
            Credit_Debit=postData.get('Credit_Debit')
        if(not postData.get('Credit_Debit')):
            message.append("Please enter card number")
        else:
            card_number=postData.get('Credit_Debit')
        if(not postData.get('security_code')):
            message.append("Please enter secuirity code")
        else:
            security_code=postData.get('security_code')
        if(not postData.get('Exp_Date')):
            message.append("Please enter Exp diary")
        else:
            Exp_Date=postData.get('Exp_Date')
        print(len(message))
        if(len(message)) > 0:
            return render(request,'User/profile_update.html',{'message':message})
        if mailing_address=="YES":
            mailaddress1=address1
            mailaddress2=address2
            mailcity=city
            mailstate=state
            mailzipcode=zipcode
            mailphone_number=phone_number
        else:
            mailaddress1=postData.get('mailaddress1')
            mailaddress2=postData.get('mailaddress2')
            mailcity=postData.get('mailcity')
            mailstate=postData.get('mailstate')
            mailzipcode=postData.get('mailzipcode')
            mailphone_number=postData.get('mailphone_number')

        #if not first_name and not last_name and not email and not password and not birthday and not gender and not address1 and not address2 and not city and not state and not zipcode and not phone_number and not mailing_address and not Digital_wallet and not Credit_Debit and not card_number and not security_code and not Exp_Date:
        


        print(first_name,last_name,email,birthday,gender,address1,address2,city,state,zipcode,phone_number,mailing_address,Credit_Debit,card_number,security_code,Exp_Date)
        data={
            "first_name":first_name,
            "last_name":last_name,
            "email":email,
            "birthday":birthday,
            "gender":gender,
            "address1":address1,
            "address2":address2,
            "city":city,
            "state":state,
            "zipcode":zipcode,
            "phone_number":phone_number,
            "mailing_address":mailing_address

        }
        #try:
        print("first name",first_name)
        
        user1=User(id=request.session.get('user_id'),
            first_name=first_name,
            last_name=last_name,
            
            email=email,
            password=make_password(password),
            birthday=birthday,
            gender=gender,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zipcode=zipcode,
            phone_number=phone_number,
            mailing_address=mailing_address,
            mailaddress1=mailaddress1,
            mailaddress2=mailaddress2,
            mailcity=mailcity,
            mailstate=mailstate,
            mailzipcode=mailzipcode,
            mailphone_number=mailphone_number,
            payment_method=Credit_Debit,
            card_number=card_number,
            security_code=security_code,
            expiration_date=Exp_Date,
            status=1)






        # user.first_name=first_name,
        # user.last_name=last_name,
        # # user.user_image=user_image,
        # user.email=email,
        # user.password=make_password(password),
        # #user.birthday=birthday,
        # user.gender=gender,
        # user.address1=address1,
        # user.address2=address2,
        # user.city=city,
        # user.state=state,
        # user.zipcode=zipcode,
        # user.phone_number=phone_number,
        # user.mailing_address=mailing_address,
        # user.mailaddress1=mailaddress1,
        # user.mailaddress2=mailaddress2,
        # user.mailcity=mailcity,
        # user.mailstate=mailstate,
        # user.mailzipcode=mailzipcode,
        # user.mailphone_number=mailphone_number,
        # user.payment_method=Credit_Debit,
        # user.card_number=card_number,
        # user.security_code=security_code,
        # user.expiration_date=Exp_Date,
        # user.status=1
        user1.save()
        request.session['user_id']=user.id
        print("updated")
        return redirect('/storepage')
        #return render(request,'index.html',{'message':'Successfully Registered'})
        # except :
        #     return render(request,'userregister.html',{'message':'Registration Error','data':data})
    elif request.method=="GET":
        return render(request,'User/profile_update.html',{'data':user,'userac':userac})

    # except Exception as e:
    #     return render(request,'User/profile_update.html',{'data':user})
    



def StoreSignUp(request):
    shopcategories=Shopcategory.get_all_shopcategory()
    if request.session.get('store_id'):
        return redirect('/StoreDashBoard')
    try:
        if request.method=="GET":
            
            print(shopcategories)
            return render(request,'Store/shopregister.html',{'shopcategories':shopcategories})
        else:
            postData=request.POST
            message=[]
            if(not postData.get('store_name')):
                message.append("enter store name")
            else:
                store_name=postData.get('store_name')
            if(not postData.get('store_email')):
                message.append("enter store email")
            else:
                store_email=postData.get('store_email')
            store_image=None#request.FILES['file']
            if(not postData.get('store_password')):
                message.append("enter store password")
            else:
                store_password=postData.get('store_password')
            if(not postData.get('Store_open_date')):
                message.append("enter store open date")
            else:
                store_open_date=postData.get('Store_open_date')
            if(not postData.get('store_category')):
                message.append("enter store category")
            else:
                store_category=postData.get('store_category')
            if(not postData.get('store_address')):
                message.append("enter store address")
            else:
                store_address=postData.get('store_address')
            if(not postData.get('store_suit')):
                message.append("enter store suit")
            else:
                store_suit=postData.get('store_suit')
            if(not postData.get('city')):
                message.append("enter store city")
            else:
                store_city=postData.get('city')
            if(not postData.get('state')):
                message.append("enter store state")
            else:
                store_state=postData.get('state')
            if(not postData.get('store_phone_number')):
                message.append("enter store phone number")
            else:
                store_phone=postData.get('store_phone_number')
            if(not postData.get('zipcode')):
                message.append("enter store zipcode")
            else:
                store_zipcode=postData.get('zipcode')
            if(not postData.get('store_tax')):
                message.append("enter store tax")
            else:
                store_tax=postData.get('store_tax')
            if(not postData.get('store_delivery_fees')):
                message.append("enter store delivery fees")
            else:
                store_delivery_fees=postData.get('store_delivery_fees')
            store_aggrement=postData.get('read_agreement')

            print(store_name,store_email,store_image,store_password,store_open_date,store_address,store_city,store_state,store_phone,store_zipcode,store_aggrement,store_suit)
            if(len(message)) > 0:
                return render(request,'Store/shopregister.html',{'message':message,'data':postData,'shopcategories':shopcategories})
            data={
                "store_name":store_name,
                "store_email":store_email,
                "store_image":store_image,
                "store_open_date":store_open_date,
                "store_address":store_address,
                "store_suit":store_suit,
                "store_city":store_city,
                "store_state":store_state,
                "store_phone":store_phone,
                "store_zipcode":store_zipcode,
                "store_aggrement":store_aggrement
            }


            #try:
            store=Store(store_name=store_name,
                        store_email=store_email,
                        store_image=store_image,
                        store_password=make_password(store_password),
                        store_open_date=store_open_date,
                        store_category=store_category,
                        store_address=store_address,
                        store_suit=store_suit,
                        store_city=store_city,
                        store_state=store_state,
                        store_phone=store_phone,
                        store_zipcode=store_zipcode,
                        store_tax=store_tax,
                        store_delivery_fees=store_delivery_fees,
                        store_aggrement=store_aggrement,
                        store_active=1,
                        status=1)
                        
            if store.isExists():
                message.append("Account already exists")
                return render(request,'Store/shopregister.html',{'message':message,'data':postData,'shopcategories':shopcategories})
            
            store.save()
            request.session['store_id']=store.id
        
            return redirect('/StoreDashBoard')
    except Exception as e:
        pass
   
        #except:
        #return render(request,'shopregister.html',{'message':'Registration Error','data':data})
def StoreLogin(request):
    if (request.session.get('store_id')):
        return redirect('/StoreDashBoard')
    #try:
    if request.method=="POST":
        
        postData=request.POST
        email=postData.get('store_email')
        password=postData.get('password')
        print(email,password)
        store=Store.get_store_by_email(email)
        if store:

            print(store.get().store_password)
            if check_password(password,store.get().store_password):
                request.session['store_id']=store.get().id
                stor=Store.get_all_active_stores(email)
                stor.store_active=1
                stor.save()
                print("Login Success full")
                print(request.session.get('store_id'))
                return redirect('/StoreDashBoard')#render(request,'storedashboard.html')
            return render(request,'Store/shoplogin.html')
        else:
            return render(request,'Store/shoplogin.html',{'message':'Credential Error'})
    else:
        
        return render(request,'Store/shoplogin.html')
        
    # except Exception as e:
    #     pass
def vendorforgetpassword(request):
    if request.method=="POST":
        email=request.POST.get('email')
        storeac=Store.get_store_by_email(email)
        if storeac:
            #userac=User.get_user_by_user_id(request.session.get('user_id'))
            otps=OTP.get_otp_by_useremail(email)
            if otps:
                print(otps)
                if len(otps)>0:
                    print("otp list")
                    for otp in otps:
                        if(otp.useremail==email) and (otp.usertype=="Store"):
                            code=''.join(random.choice('0123456789') for _ in range(6))
                            otp.otpcode=code
                            otp.save()
                            sendmail(request,"OTP Send","otp is"+code,email)
                            break
            else:
                print("new otp")
                code=''.join(random.choice('0123456789') for _ in range(6))
                otp=OTP(useremail=email,usertype="Store",otpcode=code)
                sendmail(request,"OTP Send","otp is"+code,email)
                otp.save()
            return render(request,'Store/otpverification.html',{'email':email})
        else:
           return render(request,'Store/forgetpassword.html',{'message':"There was no login with email"}) 
    else:
        return render(request,'Store/forgetpassword.html')
    
def vendorSetPassword(request):
    if request.method=="POST":
        email=request.POST.get('email')
        otpcode=request.POST.get('otp')
        password=request.POST.get('password')
        otps=OTP.objects.all()
        message="failed"
        if len(otps)>0:
            for otp in otps:
                if(otp.useremail==email) and (otp.usertype=="Store") and (otp.otpcode==otpcode):
                    storeac=Store.get_store_by_email(email)#User.get_user_by_email(email)
                    storeac.store_password=make_password(password)
                    message="success change password"
                    break
        print(message)
        return redirect('/StoreLogin')

def Storelogout(request):
    store=Store.get_store_by_store_id(request.session.get('store_id'))
    store.store_active=0
    store.save()
    del request.session['store_id']
    return redirect('/')
def StoreDashBoard(request):
    try:
        print(request.session.get('store_id'))
        if(request.session.get('store_id')==None):
            return redirect('/StoreLogin')
        categories=Category.get_category_by_store_id(request.session.get('store_id'))
        subcategories=Subcategory.get_sub_categories_by_store_id(request.session.get('store_id'))
        products=Product.get_all_products_by_store_id(request.session.get('store_id'))
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        notifications=Notification.get_notification_by_store_id(storeac.id)
        #chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
        chats=Chat.objects.all()
        users=User.get_all_user()
        print(chats)
        print(notifications)
        print(storeac.store_image)
        data={
            'categories':categories,
            'subcategories':subcategories,
            'products':products,
            'storeac':storeac,
            'notifications':notifications,
            'chats':chats,
            'users':users,

        }
        return render(request,'Store/storedashboard.html',data)
    except expression as identifier:
        pass
    
def StoreAccount(request):
    if(request.session.get('store_id')==None):
        return redirect('/StoreLogin')
    storeac=Store.get_store_by_store_id(request.session.get('store_id'))
    if request.method=="GET":
        return render(request,'Store/storeaccount.html',{'storeac':storeac})

def AddCategory(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        return render(request,'Store/category_add.html',{'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        name=postData.get('category_name')
        shop_id=request.session.get('store_id')
        print(name,shop_id)
        category=Category(name=name,
                          Shop_id=shop_id,
                          status=1)
        if category.isExists():
            print("Exists")
            return render(request,'Store/category_add.html',{'chats':chats,'users':users})
        category.save()
        print("Category Saved Successfully")
        return redirect('/Category')
def EditCategory(request,category_id):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    category=Category.get_category_by_category_id(category_id)
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    print(category.name)
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        return render(request,'Store/category_edit.html',{'category':category,'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        category.name=postData.get('category_name')
        category.save()
        print("category updated")
        return redirect('/Category')
def deleteCategory(request,category_id):
    category=Category.get_category_by_category_id(category_id)
    subcategories=Subcategory.get_sub_categories_by_store_id(request.session.get('store_id'))
    for subcat in subcategories:
        if subcat.Cat_id==category_id:
            subcat.delete()
    category.delete()
    return redirect('/Category')
def CategoryList(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        store_id=request.session.get('store_id')
        if(request.session.get('store_id')==None):
            return redirect('/StoreLogin')
        print(store_id)
        categories=Category.get_category_by_store_id(store_id)
        print(categories)
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        notifications=Notification.get_notification_by_store_id(storeac.id)
        print(notifications)
        return render(request,'Store/categorylist.html',{'categories':categories,'storeac':storeac,'notifications':notifications,'chats':chats,'users':users})

def AddSubCategory(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        categories=Category.get_category_by_store_id(request.session.get('store_id'))
        return render(request,'Store/subcategory_add.html',{'categories':categories,'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        name=postData.get('sub_category_name')
        category_id=postData.get('category_id')
        store_id=request.session.get('store_id')
        print(name,category_id,store_id)
        subcat=Subcategory(name=name,
                          Cat_id=category_id,
                          store_id=store_id,
                          status=1)
        if subcat.isExists():
            print("Exists")
            return render(request,'Store/subcategory_add.html',{'chats':chats,'users':users})
        subcat.save()
        print("Sub Category Add Successfully")
        return redirect('/SubCategory')
def SubCategoryList(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        store_id=request.session.get('store_id')
        if(request.session.get('store_id')==None):
            return redirect('/StoreLogin')
        categories=Category.get_category_by_store_id(store_id)
        subcategories=Subcategory.get_sub_categories_by_store_id(store_id)#Subcategory.get_subcategory_by_category_id(category_id)
        print(subcategories)
        print(categories)
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        notifications=Notification.get_notification_by_store_id(storeac.id)
        print(notifications)
        return render(request,'Store/subcategorylist.html',{'subcategories':subcategories,'categories':categories,'storeac':storeac,'notifications':notifications,'chats':chats,'users':users})
def EditSubCategory(request,subcategory_id):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    subcategory=Subcategory.get_subcategory_by_subcategory_id(subcategory_id)
    print(subcategory.name)
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        return render(request,'Store/subcategory_edit.html',{'subcategory':subcategory,'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        subcategory.name=postData.get('subcategory_name')
        subcategory.save()
        print("category updated")
        return redirect('/SubCategory')
def deleteSubCategory(request,subcategory_id):
    subcategory=Subcategory.get_subcategory_by_subcategory_id(subcategory_id)
    subcategory.delete()
    return redirect('/SubCategory')


def AllProduct(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        store_id=request.session.get('store_id')
        if(request.session.get('store_id')==None):
            return redirect('/StoreLogin')
        products=Product.get_all_products_by_store_id(store_id)
        subcategories=Subcategory.get_sub_categories_by_store_id(store_id)
        print(subcategories)
        print(products)
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        notifications=Notification.get_notification_by_store_id(storeac.id)
        print(notifications)
        return render(request,'Store/productlist.html',{'subcategories':subcategories,'products':products,'storeac':storeac,'notifications':notifications,'chats':chats,'users':users})
def AddProduct(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        categories=Category.get_category_by_store_id(request.session.get('store_id'))
        subcategories=Subcategory.get_sub_categories_by_store_id(request.session.get('store_id'))
        return render(request,'Store/product_add.html',{'categories':categories,'subcategories':subcategories,'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        product_name=postData.get('product_name')
        product_color=postData.get('product_color')
        product_size=postData.get('product_size')
        product_price=postData.get('product_price')
        product_descriptions=postData.get('product_descriptions')
        product_image=request.FILES['product_image']
        product_category=postData.get('category_id')

        print(product_name,product_color,product_size,product_price,product_descriptions,product_image,product_category)
        product=Product(product_name=product_name,
                        product_color=product_color,
                        product_size=product_size,
                        product_price=product_price,
                        product_descriptions=product_descriptions,
                        product_image=product_image,
                        product_category=product_category,
                        store_id=request.session.get('store_id'),
                        status=1)
        product.add()
        return redirect('/Product')
def EditProduct(request,product_id):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    product=Product.get_product_by_product_id(product_id)
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        categories=Category.get_category_by_store_id(request.session.get('store_id'))
        subcategories=Subcategory.get_sub_categories_by_store_id(request.session.get('store_id'))
        return render(request,'Store/product_edit.html',{'product':product,'categories':categories,'subcategories':subcategories,'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        product.product_name=postData.get('product_name')
        product.product_color=postData.get('product_color')
        product.product_size=postData.get('product_size')
        product.product_price=postData.get('product_price')
        product.product_descriptions=postData.get('product_descriptions')
        product.product_image=request.FILES['product_image']
        product.product_category=postData.get('category_id')
        product.save()
        print("product updated")
        return redirect('/Product')

def deleteProduct(request,product_id):
    product=Product.get_product_by_product_id(product_id)
    product.delete()
    return redirect('/Product')

def AllAdvertisement(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    advertisement=Advertising.get_all_advertising_by(request.session.get('store_id'))
    if(request.session.get('store_id')==None):
        return redirect('/StoreLogin')
    print(advertisement)
    storeac=Store.get_store_by_store_id(request.session.get('store_id'))
    notifications=Notification.get_notification_by_store_id(storeac.id)
    print(notifications)
    return  render(request,'Store/advertisementlist.html',{'advertisements':advertisement,'storeac':storeac,'notifications':notifications,'chats':chats,'users':users})

def AddAdvertisement(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        advertisement=Advertising.get_all_advertising_by(request.session.get('store_id'))

        return render(request,'Store/advertisement_add.html',{'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        advertising_image=request.FILES['advertising_image']
        advertising_start_date=postData.get('advertising_start_date')
        advertising_end_date=postData.get('advertising_end_date')
        advertising_message=postData.get('advertising_message')
        store_id=request.session.get('store_id')
        print(advertising_image,advertising_start_date,advertising_end_date,advertising_message,store_id)
        advertise=Advertising(advertising_image=advertising_image,
                              advertising_start_date=advertising_start_date,
                              advertising_end_date=advertising_end_date,
                              advertising_message=advertising_message,
                              store_id=store_id,
                              status=1)
        advertise.save()
        return redirect('/Advertisements')
def EditAdvertisement(request,advertisement_id):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    print(advertisement_id)
    advertise=Advertising.get_by_advertisement_id(advertisement_id)
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        return render(request,'Store/advertisement_edit.html',{'advertise':advertise,'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        advertise.advertising_image=request.FILES['advertising_image']
        advertise.advertising_start_date=postData.get('advertising_start_date')
        advertise.advertising_end_date=postData.get('advertising_end_date')
        advertise.advertising_message=postData.get('advertising_message')
        advertise.save()
        print("Advertisement updated")
        return redirect('/Advertisements')
def deleteAdvertisement(request,advertisement_id):
    advertise=Advertising.get_by_advertisement_id(advertisement_id)
    advertise.delete()
    return redirect('/Advertisements')
def Coupons(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        store_id=request.session.get('store_id')
        if(request.session.get('store_id')==None):
            return redirect('/StoreLogin')
        coupons=Coupon.get_coupon_by_store_id(request.session.get('store_id'))
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        notifications=Notification.get_notification_by_store_id(storeac.id)
        print(notifications)
        return render(request,'Store/coupons.html',{'coupons':coupons,'storeac':storeac,'notifications':notifications,'chats':chats,'users':users})
def Addcoupon(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        return render(request,'Store/coupon_add.html',{'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        coupon_code=postData.get('coupon_code')
        coupon_discount=postData.get('coupon_discount')
        shop_id=request.session.get('store_id')
        
        coupon=Coupon(coupon_code=coupon_code,
                          coupon_discount=coupon_discount,
                          coupon_store_id=shop_id,
                          coupon_status=1)
        if coupon.isExists():
            print("Exists")
            return render(request,'Store/coupon_add.html',{'chats':chats,'users':users})
        coupon.save()
        print("Coupon Saved Successfully")
        return redirect('/Coupon')   
def EditCoupon(request,coupon_id):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    coupons=Coupon.getCouponbyCoupon_id(coupon_id)
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    print(coupons.coupon_code)
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        return render(request,'Store/coupon_edit.html',{'coupons':coupons,'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        coupons.coupon_code=postData.get('coupon_code')
        coupons.coupon_discount=postData.get('coupon_discount')
        coupons.save()
        print("coupon updated")
        return redirect('/Coupon') 
def deleteCoupon(request,coupon_id):
    coupons=Coupon.getCouponbyCoupon_id(coupon_id)
    coupons.delete()
    return redirect('/Coupon')
def Filter(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        store_id=request.session.get('store_id')
        if(request.session.get('store_id')==None):
            return redirect('/StoreLogin')
        filters=Productfilter.get_filter_by_store_id(request.session.get('store_id'))
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        notifications=Notification.get_notification_by_store_id(storeac.id)
        categories=Category.get_all_categories()
        print(notifications)
        return render(request,'Store/filters.html',{'categories':categories,'filters':filters,'storeac':storeac,'notifications':notifications,'chats':chats,'users':users})
def AddFilter(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        categories=Category.get_category_by_store_id(request.session.get('store_id'))
        return render(request,'Store/filter_add.html',{'categories':categories,'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        filter_name=postData.get('filter_name')
        category_id=postData.get('category_id')
        store_id=request.session.get('store_id')
        print(filter_name,category_id,store_id)
        filter=Productfilter(filter_name=filter_name,
                            filter_category=category_id,
                            filter_store_id=store_id,
                            status=1)
        if filter.isExists():
            print("Exists")
            return render(request,'Store/filter_add.html',{'chats':chats,'users':users})
        filter.save()
        print("Filter Add Successfully")
        return redirect('/Filter')
def EditFilter(request,filter_id):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    filters=Productfilter.get_filter_by_filter_id(filter_id)
    print(filters)
    print(filters.filter_name)
    if request.method=="GET":
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        return render(request,'Store/filter_edit.html',{'filter':filters,'storeac':storeac,'chats':chats,'users':users})
    else:
        postData=request.POST
        filters.filter_name=postData.get('filter_name')
        filters.save()
        print("filter updated")
        return redirect('/Filter')
def deleteFilter(request,filter_id):
    filters=Productfilter.get_filter_by_filter_id(filter_id)
    filters.delete()
    return redirect('/Filter')

def Attribute(request,product_id):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    if request.method=="GET":
        store_id=request.session.get('store_id')
        if(request.session.get('store_id')==None):
            return redirect('/StoreLogin')
        attributes=Productattribute.get_filter_by_product_id(product_id)
        storeac=Store.get_store_by_store_id(request.session.get('store_id'))
        notifications=Notification.get_notification_by_store_id(storeac.id)
        categories=Category.get_all_categories()
        print(notifications)
        return render(request,'Store/Attributes.html',{'categories':categories,'attributes':attributes,'storeac':storeac,'notifications':notifications,'chats':chats,'users':users})

def salesforthemonth(request):
    chats=Chat.get_all_chat_by_vendor_id(request.session.get('store_id'))
    users=User.get_all_user()
    storeac=Store.get_store_by_store_id(request.session.get('store_id'))
    orders=Order.get_order_pickup()
    finalorder=[]
    for order in orders:
        print(order.product.store_id)
        if order.product.store_id==request.session.get('store_id'):
            finalorder.append(order)
    print(orders)
    print(finalorder)
    notifications=Notification.get_notification_by_store_id(storeac.id)
    print(notifications)
    return render(request,'Store/salesforthemonth.html',{'storeac':storeac,'orders':orders,'notifications':notifications,'chats':chats,'users':users})

def storepage(request):
    
    shopcategories=Shopcategory.get_all_shopcategory()
    print(shopcategories)
    # if (request.session.get('user_id') request.session.get('user_name')):
    #     return redirect('/UserLogin')
    if (request.session.get('user_id')==None) and (request.session.get('user_name')==None):
        return redirect('/UserLogin')
    if((request.session.get('user_id') != None)):
        username=None
        userac=User.get_user_by_user_id(request.session.get('user_id'))

    if((request.session.get('user_name') != None)):
        userac=None
        username=request.session.get('user_name')
    
    shopcategories=iterutils.chunked(shopcategories, 3)
    print(shopcategories)
    advertisements=Advertising.get_all_advertisement()

    newadvertisements=[]
    for advertise in advertisements:
        if advertise.advertising_end_date > datetime.date.today():
            newadvertisements.append(advertise)
    advertisements=newadvertisements

    print(advertisements)
    stores=Store.get_all_stores()
    print(len(stores))
    numberofstore=len(stores)
    cartproducts=cart(request)
    orders=ordersview(request)

    chats=Chat.get_all_chat()
    print(chats)
    allstores=Store.get_all_stores()
    activestores=Store.get_active_stores()
    print("active",len(activestores))
    return render(request,'User/storepage.html',{'shopcategories':shopcategories,'userac':userac,'username':username,'advertisements':advertisements,'numberofstore':numberofstore,'activestores':len(activestores),'stores':stores,'cartproducts':cartproducts,'orders':orders,'chats':chats,'allstores':allstores})

def vendorpage(request,shopcategory_id):
    print(shopcategory_id)
    if(request.session.get('user_id')==None):
        return redirect('/UserLogin')
   
    userac=User.get_user_by_user_id(request.session.get('user_id'))
    stores=Store.get_all_stores()
    print(len(stores))
    numberofstore=len(stores)
    stores=Store.get_store_by_shopcategory(shopcategory_id)
    stores=iterutils.chunked(stores, 3)
    print(stores)
    advertisements=Advertising.get_all_advertisement()
    cartproducts=cart(request)
    orders=ordersview(request)
    allstores=Store.get_all_stores()
    activestores=Store.get_active_stores()
    chats=Chat.get_all_chat()
    print(chats)
    return render(request,'User/vendorpage.html',{'stores':stores,'chats':chats,'userac':userac,'advertisements':advertisements,'numberofstore':numberofstore,'activestores':len(activestores),'cartproducts':cartproducts,'orders':orders,'allstores':allstores})

def productview(request,store_id):
    if(request.session.get('user_id')==None):
        return redirect('/UserLogin')
    userac=User.get_user_by_user_id(request.session.get('user_id'))
    products=Product.get_all_products_by_store_id(store_id)
    store_name=Store.get_store_by_store_id(store_id)
    products=iterutils.chunked(products, 3)
    print(products)
    advertisements=Advertising.get_all_advertisement()
    stores=Store.get_all_stores()
    print(len(stores))
    numberofstore=len(stores)
    cartproducts=cart(request)
    orders=ordersview(request)
    allstores=Store.get_all_stores()
    activestores=Store.get_active_stores()
    chats=Chat.get_all_chat()
    print(chats)
    return render(request,'User/productview.html',{'products':products,'chats':chats,'userac':userac,'advertisements':advertisements,'numberofstore':numberofstore,'activestores':len(activestores),'cartproducts':cartproducts,'orders':orders,'allstores':allstores,'store_name':store_name})
def singleproductview(request,product_id):
    if(request.session.get('user_id')==None):
        return redirect('/UserLogin')
    carts=request.session.get('cart')
    if not carts:
        request.session.cart={}
    
    userac=User.get_user_by_user_id(request.session.get('user_id'))
    product=Product.get_product_by_product_id(product_id)
    #print(product.product_category)
    category=Category.get_category_by_category_id(product.product_category)
    stores=Store.get_all_stores()
    advertisements=Advertising.get_all_advertisement()
    #stores=Store.get_all_stores()
    #print(len(stores))
    numberofstore=len(stores)
    like=Like.get_like_by_user_id_product_id(userac.id,product.id)
    #print(like)
    cartproducts=cart(request)
    orders=ordersview(request)
    allstores=Store.get_all_stores()
    store_id=Product.get_product_by_product_id(product_id).store_id
    store_name=Store.get_store_by_store_id(store_id)
    print(stores)
    activestores=Store.get_active_stores()
    chats=Chat.get_all_chat()
    print(chats)
    return render(request,'User/singleproductview.html',{'product':product,'chats':chats,'category':category,'userac':userac,'stores':stores,'advertisements':advertisements,'numberofstore':numberofstore,'activestores':len(activestores),'like':like,'cartproducts':cartproducts,'orders':orders,'allstores':allstores,'store_name':store_name})
def likesingleproduct(request,product_id):

    like=Like.get_like_by_user_id_product_id(request.session.get('user_id'),product_id)
    print(like)
    if not like:
        like=Like(product=product_id,user=request.session.get('user_id'),like=True,status=True)
        like.save()
    else:
        if like.like==False:
            like.like=True
        else:
            like.like=False
        like.save()
        user=User.get_user_by_user_id(request.session.get('user_id'))
        product=Product.get_product_by_product_id(product_id)
        print(user.first_name+"Liked "+product.product_name)
        notification=Notification(notification=user.first_name+" Liked "+product.product_name,
                                  notification_to=product.store_id,
                                  notification_from_type='user',
                                  notification_time=datetime.datetime.now(),
                                  status=1
                                  )
        notification.save()
    return redirect('/product/'+product_id)
    
def addtocart(request,product_id):
    cart=request.session.get('cart')
    if cart:
        quantity=cart.get(product_id)
        if quantity:
            cart[product_id]=quantity+1
        else:
            cart[product_id]=1
    else:
        cart={}
        cart[product_id]=1
    request.session['cart']=cart
    print(request.session['cart'])
    
    return redirect('/similartocart/'+product_id)
def similartocart(request,product_id):
    products=Product.get_product_by_product_id(product_id)
    productss=Product.get_product_by_category(products.product_category)
    userac=User.get_user_by_user_id(request.session.get('user_id'))
    
    store_id=Product.get_product_by_product_id(product_id).store_id
    store_name=Store.get_store_by_store_id(store_id)
    
    print(productss)
    productssimilar=Product.get_all_product()
    arr=[]
    i=0
    for prod in productssimilar:
        arr.append(prod)
        i+=1
        if i==4:
            break
    productssimilar=arr
    print(productssimilar)
    stores=Store.get_all_stores()
    numberofstore=len(stores)
    cartproducts=cart(request)
    orders=ordersview(request)
    allstores=Store.get_all_stores()
    activestores=Store.get_active_stores()
    
    return render(request,"User/similartocart.html",{'products':products,'productssimilar':productssimilar,'userac':userac,'stores':stores,'numberofstore':numberofstore,'activestores':len(activestores),'cartproducts':cartproducts,'orders':orders,'allstores':allstores,'store_name':store_name})

def cart(request):
    if(request.session.get('user_id')==None):
        return redirect('/UserLogin')
    userac=User.get_user_by_user_id(request.session.get('user_id'))

    cart=request.session.get('cart')
    if not cart:
        request.session.cart={}
        return redirect('/storepage')
    else:
        stores=Store.get_all_stores()
        numberofstore=len(stores)
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        print(products)
        return products
        #return render(request,'cart.html',{'products':products,'userac':userac,'numberofstore':numberofstore})

stripe.api_key = "sk_test_51H6HtIBIRW4ci3Bh2WYF9bkxfJZydcTVgosqEVhzlsrDS2fhgmMFd3bCo6Rn7bFgx6TtOZLYKgX8zI1ltidHvja600x1w3CRGz"
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["key"] =settings.STRIPE_PUBLISHABLE_KEY 
    return context

def charge(request):
    if request.method=='POST':
        userac=User.get_user_by_user_id(request.session.get('user_id'))
        customer=stripe.Customer.create(
            email=userac.email,
            description=userac.first_name+" "+userac.last_name,
            source=request.POST.get('stripeToken')
        )
        total=request.POST.get("total_price")
        print(total)
        charge=stripe.Charge.create(
            amount=int(float(total*78)),
            currency="usd",
            customer=customer,
            description="Simntx user Payment",
        )
        print(request.POST)

        address=request.POST.get('address')
        phone=request.POST.get('phone')
        user=request.session.get('user_id')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        for product in products:
            order=Order(user=User(id=user),
                        product=product,
                        price=product.product_price,
                        address=address,
                        phone=phone,
                        stripe_charge_id=charge.id,
                        #quantity=cart.get(product.id)
                        date=datetime.datetime.now().strftime("%Y-%m-%d"),
                        quantity=cart.get(str(product.id)))
            order.placeOrder()
        print(address,phone,user,cart,products)
        request.session['cart']={}
        return redirect('/storepage')
        # charge=stripe.Charge.create(
        #     amount=500,
        #     currency='usd',
        #     description='A Django Charged',
        #     source=request.POST['stripeToken']
        #     )
        #return render(request,'User/charge.html')

    

def ordersview(request):
    user =request.session.get('user_id')
    orders=Order.get_orders_by_user(user)
    userac=User.get_user_by_user_id(request.session.get('user_id'))
    print(orders)
    stores=Store.get_all_stores()
    numberofstore=len(stores)
    return orders
    #return render(request,'order.html',{'orders':orders,'userac':userac,'numberofstore':numberofstore})

def DriverSignup(request):
    if(request.session.get('driver_id')):
        return redirect('/driverorders')
    if request.method=="POST":
        message=[]
        postData=request.POST
        if(not postData.get('first_name')):
            message.append("Please enter First Name")
        else:
            first_name=postData.get('first_name')
        if(not postData.get('last_name')):
            message.append("Please enter Last Name")
        else:
            last_name=postData.get('last_name')
        if(not postData.get('email')):
            message.append("Please enter Email Address")
        else:
            email=postData.get('email')
        if(not postData.get('password')):
            message.append("Please enter Password")
        else:
            password=postData.get('password')
        if(not postData.get('birthday')):
            message.append("Please enter birthday")
        else:
            birthday=postData.get('birthday')
        if(not postData.get('gender')):
            message.append("Please enter gender")
        else:
            gender=postData.get('gender')
        if(not postData.get('driver_image')):
            message.append("Please enter driver image")
        else:
            driver_image=request.FILES['driver_image']
        if(not postData.get('address1')):
            message.append("Please enter driver address1")
        else:
            address1=postData.get('address1')
        if(not postData.get('address2')):
            message.append("Please enter driver address2")
        else:
            address2=postData.get('address2')
        if(not postData.get('city')):
            message.append("Please enter driver city")
        else:
            city=postData.get('city')
        if(not postData.get('state')):
            message.append("Please enter driver state")
        else:
            state=postData.get('state')
        if(not postData.get('zipcode')):
            message.append("Please enter driver zipcode")
        else:
            zipcode=postData.get('zipcode')
        if(not postData.get('phone_number')):
            message.append("Please enter driver phone_number")
        else:
            phone_number=postData.get('phone_number')
        if(not postData.get('vehical_type')):
            message.append("Please enter driver vehical_type")
        else:
            vehical_type=postData.get('vehical_type')
        if(not postData.get('social_security')):
            message.append("Please enter driver social_security")
        else:
            social_security=postData.get('social_security')
        if(not postData.get('license_number')):
            message.append("Please enter driver license_number")
        else:
            license_number=postData.get('license_number')
        if(not postData.get('islicense')):
            message.append("Please enter driver islicense")
        else:
            islicense=postData.get('islicense')
        if(not postData.get('account_number')):
            message.append("Please enter driver account_number")
        else:
            account_number=postData.get('account_number')
        if(not postData.get('routing_number')):
            message.append("Please enter driver routing_number")
        else:
            routing_number=postData.get('routing_number')
        if(not postData.get('convicted_of_any_felonies')):
            message.append("Please enter driver convicted_of_any_felonies")
        else:
            convicted_of_any_felonies=postData.get('convicted_of_any_felonies')
        if(not postData.get('concede_to_a_background_check')):
            message.append("Please enter driver concede_to_a_background_check")
        else:
            concede_to_a_background_check=postData.get('concede_to_a_background_check')
        if(len(message)) > 0:
            return render(request,'Driver/driversignup.html',{'message':message,'data':postData})
        print(first_name,last_name,email,password,birthday,gender,driver_image,address1,address2,city,state,zipcode,phone_number,vehical_type,social_security,license_number,islicense,account_number,routing_number,convicted_of_any_felonies,concede_to_a_background_check)
        driver=Driver(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=make_password(password),
                        birthday=birthday,
                        gender=gender,
                        driver_image=driver_image,
                        address1=address1,
                        apt=address2,
                        city=city,
                        state=state,
                        zipcode=zipcode,
                        phone_number=phone_number,
                        vehical_type=vehical_type,
                        social_security=social_security,
                        license_number=license_number,
                        islicense=islicense,
                        account_number=account_number,
                        routing_number=routing_number,
                        convicted_of_any_felonies=convicted_of_any_felonies,
                        concede_to_a_background_check=concede_to_a_background_check,
                        status=1
                        )
        if driver.isExists():
            message.append("Account Already Exists!")
            return render(request,'Driver/driversignup.html',{'message':message,'data':postData})
        driver.save()
        request.session['driver_id']=driver.id
        return redirect('/driverorders')

    return render(request,'Driver/driversignup.html')

def DriverLogin(request):
    if(request.session.get('driver_id')):
        return redirect('/driverorders')
    if request.method=="POST":
            
        postData=request.POST
        email=postData.get('driver_email')
        password=postData.get('password')
        print(email,password)
        driver=Driver.get_driver_by_email(email)
        if driver :
            print("driver",driver)
            print(driver.get().password)
            if check_password(password,driver.get().password):
                request.session['driver_id']=driver.get().id
                print("Login Success full")
                print(request.session.get('driver_id'))
                return redirect('/driverorders')#render(request,'storedashboard.html')
            return render(request,'Driver/driverlogin.html')
        else:
            return render(request,'Driver/driverlogin.html',{'message':"credential wrong"})

    else:
        
        return render(request,'Driver/driverlogin.html')
    return render(request,'Driver/driverlogin.html')

def driverupdate(request):
    
    if request.method=="POST":
        message=[]
        postData=request.POST
        if(not postData.get('first_name')):
            message.append("Please enter First Name")
        else:
            first_name=postData.get('first_name')
        if(not postData.get('last_name')):
            message.append("Please enter Last Name")
        else:
            last_name=postData.get('last_name')
        if(not postData.get('email')):
            message.append("Please enter Email Address")
        else:
            email=postData.get('email')
        if(not postData.get('password')):
            message.append("Please enter Password")
        else:
            password=postData.get('password')
        if(not postData.get('birthday')):
            message.append("Please enter birthday")
        else:
            birthday=postData.get('birthday')
        if(not postData.get('gender')):
            message.append("Please enter gender")
        else:
            gender=postData.get('gender')
        if(not postData.get('driver_image')):
            message.append("Please enter driver image")
        else:
            driver_image=request.FILES['driver_image']
        if(not postData.get('address1')):
            message.append("Please enter driver address1")
        else:
            address1=postData.get('address1')
        if(not postData.get('address2')):
            message.append("Please enter driver address2")
        else:
            address2=postData.get('address2')
        if(not postData.get('city')):
            message.append("Please enter driver city")
        else:
            city=postData.get('city')
        if(not postData.get('state')):
            message.append("Please enter driver state")
        else:
            state=postData.get('state')
        if(not postData.get('zipcode')):
            message.append("Please enter driver zipcode")
        else:
            zipcode=postData.get('zipcode')
        if(not postData.get('phone_number')):
            message.append("Please enter driver phone_number")
        else:
            phone_number=postData.get('phone_number')
        if(not postData.get('vehical_type')):
            message.append("Please enter driver vehical_type")
        else:
            vehical_type=postData.get('vehical_type')
        if(not postData.get('social_security')):
            message.append("Please enter driver social_security")
        else:
            social_security=postData.get('social_security')
        if(not postData.get('license_number')):
            message.append("Please enter driver license_number")
        else:
            license_number=postData.get('license_number')
        if(not postData.get('islicense')):
            message.append("Please enter driver islicense")
        else:
            islicense=postData.get('islicense')
        if(not postData.get('account_number')):
            message.append("Please enter driver account_number")
        else:
            account_number=postData.get('account_number')
        if(not postData.get('routing_number')):
            message.append("Please enter driver routing_number")
        else:
            routing_number=postData.get('routing_number')
        if(not postData.get('convicted_of_any_felonies')):
            message.append("Please enter driver convicted_of_any_felonies")
        else:
            convicted_of_any_felonies=postData.get('convicted_of_any_felonies')
        if(not postData.get('concede_to_a_background_check')):
            message.append("Please enter driver concede_to_a_background_check")
        else:
            concede_to_a_background_check=postData.get('concede_to_a_background_check')
        if(len(message)) > 0:
            return render(request,'Driver/driversignup.html',{'message':message,'data':postData})
        print(first_name,last_name,email,password,birthday,gender,driver_image,address1,address2,city,state,zipcode,phone_number,vehical_type,social_security,license_number,islicense,account_number,routing_number,convicted_of_any_felonies,concede_to_a_background_check)
        driver=Driver(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=make_password(password),
                        birthday=birthday,
                        gender=gender,
                        driver_image=driver_image,
                        address1=address1,
                        apt=address2,
                        city=city,
                        state=state,
                        zipcode=zipcode,
                        phone_number=phone_number,
                        vehical_type=vehical_type,
                        social_security=social_security,
                        license_number=license_number,
                        islicense=islicense,
                        account_number=account_number,
                        routing_number=routing_number,
                        convicted_of_any_felonies=convicted_of_any_felonies,
                        concede_to_a_background_check=concede_to_a_background_check,
                        status=1
                        )
        if driver.isExists():
            message.append("Account Already Exists!")
            return render(request,'Driver/driverupdate.html',{'message':message,'data':postData})
        driver.save()
        request.session['driver_id']=driver.id
        return redirect('/driverorders')

    return render(request,'Driver/driverupdate.html')
def driverforgetpassword(request):
    if request.method=="POST":
        email=request.POST.get('email')
        userac=Driver.get_driver_by_email(email)
        if userac:

            otps=OTP.get_otp_by_useremail(email)
            if otps:
                print(otps)
                if len(otps)>0:
                    print("otp list")
                    for otp in otps:
                        if(otp.useremail==email) and (otp.usertype=="Driver"):
                            code=''.join(random.choice('0123456789') for _ in range(6))
                            otp.otpcode=code
                            otp.save()
                            sendmail(request,"OTP Send","otp is"+code,email)
                            break
            else:
                print("new otp")
                code=''.join(random.choice('0123456789') for _ in range(6))
                otp=OTP(useremail=email,usertype="Driver",otpcode=code)
                sendmail(request,"OTP Send","otp is"+code,email)
                otp.save()
            return render(request,'Driver/otpverification.html',{'email':email})
        else:
            return render(request,'Driver/forgetpassword.html',{'message':"this email is not registered"})
        #userac=User.get_user_by_user_id(request.session.get('user_id'))
        
    else:
        return render(request,'Driver/forgetpassword.html')
def driverSetPassword(request):
    if request.method=="POST":
        email=request.POST.get('email')
        otpcode=request.POST.get('otp')
        password=request.POST.get('password')
        otps=OTP.objects.all()
        message="failed"
        if len(otps)>0:
            for otp in otps:
                if(otp.useremail==email) and (otp.usertype=="Driver") and (otp.otpcode==otpcode):
                    userac=Driver.get_driver_by_email(email)
                    userac.password=make_password(password)
                    message="success change password"
                    break
        print(message)
        return redirect('/DriverLogin')

def Driverorders(request):
    if(request.session.get('driver_id')==None):
        return redirect('/DriverLogin')
    orders=Order.get_all_order()
    driverac=Driver.get_driver_by_driver_id(request.session.get('driver_id'))
    return render(request,'Driver/driver_orders.html',{'driverac':driverac,'orders':orders})
def DriverLogout(request):
    del request.session['driver_id']
    return redirect('/')
def yesdriverorderpickup(request,order_id):
    print(order_id)
    driverac=Driver.get_driver_by_driver_id(request.session.get('driver_id'))
    order=Order.get_order_by_order_id(order_id)
    order.orderpickup=True
    order.save()
    driverorderpic=Driverorderpickup(driver=driverac,order=order,pickup=True,status=1)
    driverorderpic.save()
    return redirect('/driverorders')


def nodriverorderpickup(request,order_id):
    driverac=Driver.get_driver_by_driver_id(request.session.get('driver_id'))
    order=Order.get_order_by_order_id(order_id)
    
    driverorderpic=Driverorderpickup(driver=driverac,order=order,pickup=False,status=1)
    driverorderpic.save()
    return redirect('/driverorders')

def about(request):
    stores=Store.get_all_stores()
    numberofstore=len(stores)
    return render(request,"about.html",{'numberofstore':numberofstore})
def contact(request):
    stores=Store.get_all_stores()
    numberofstore=len(stores)
    return render(request,"contact.html",{'numberofstore':numberofstore})
def carrer(request):
    stores=Store.get_all_stores()
    numberofstore=len(stores)
    return render(request,"carrer.html",{'numberofstore':numberofstore})
def customer(request):
    return render(request,"carrer.html")


from django.http import JsonResponse

def userchat(request):
    print(request.POST)
    chat=Chat(msgfrom=request.session.get('user_id'),
             msgto=request.GET.get('vendor_id'),
             msgfromusertype="User",
             msgtusertype="Vendor",
             msgtime=datetime.datetime.now(),
             msg=request.GET.get('msg'))
    chat.save()
    data = {
        'is_taken':"okay"
    }
    l=list()
    chats=Chat.objects.all()
    # for ch in chats:
    #     ser=ChatSerializer(ch)
    #     print(ser)
    #     l.append(ser.data)
    #     print(ser.data)
    # print(l)

    return JsonResponse({"chats":list(chats.values())})#redirect(request.META['HTTP_REFERER'])

def applycoupon(request):
    print(request.GET)
    coupon=Coupon.get_coupon_by_coupon_code(request.GET.get('coupon_code'))
    print(coupon)
    if coupon==False:
        return JsonResponse({"coupon_discount":"Invalid Coupon Code"})
    else:
        product=Product.get_product_by_product_id(request.GET.get('product_id'))
        print(product.store_id,coupon.coupon_store_id)
        if product.store_id == coupon.coupon_store_id:
            return JsonResponse({"coupon_discount":str(coupon.coupon_discount)+"%"})
        else:
            return JsonResponse({"coupon_discount":"Invalid Coupon Code"})
       
    
def vendorchat(request):
    print(request.GET)
    chat=Chat(msgfrom=request.session.get('store_id'),
             msgto=request.GET.get('vendor_id'),
             msgfromusertype="Vendor",
             msgtusertype="User",
             msgtime=datetime.datetime.now(),
             msg=request.GET.get('msg'))
    chat.save()
    data = {
        'is_taken':"okay"
    }
    l=list()
    chats=Chat.objects.all()
    # for ch in chats:
    #     ser=ChatSerializer(ch)
    #     print(ser)
    #     l.append(ser.data)
    #     print(ser.data)
    # print(l)


    return JsonResponse({"chats":list(chats.values())})#redirect(request.META['HTTP_REFERER'])
