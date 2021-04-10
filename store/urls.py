"""simntx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index,login,about,carrer,contact,customer,UserSignUp,userLogin,UserUpdate,ForgetPassword,SetPassword,Userlogout,UserProfileUpdate,StoreSignUp,StoreLogin,vendorforgetpassword,vendorSetPassword,Storelogout,StoreDashBoard,StoreAccount,AddCategory,EditCategory,deleteCategory,AddSubCategory,CategoryList,SubCategoryList,AddProduct,EditSubCategory,deleteSubCategory,Coupons,Addcoupon,EditCoupon,deleteCoupon,applycoupon,Filter,AddFilter,EditFilter,deleteFilter,Attribute,AllProduct,EditProduct,deleteProduct,AllAdvertisement,AddAdvertisement,EditAdvertisement,deleteAdvertisement,storepage,vendorpage,productview,singleproductview,addtocart,cart,charge,ordersview,DriverSignup,DriverLogin,driverupdate,driverforgetpassword,driverSetPassword,Driverorders,DriverLogout,yesdriverorderpickup,nodriverorderpickup,salesforthemonth,similartocart,likesingleproduct,userchat,vendorchat

urlpatterns = [
   
    path('',index,name='homepage'),
    path('login',login),
    path('UserSignup',UserSignUp),
    path('UserLogin',userLogin),
    path('UserUpdate',UserUpdate),
    path('UserLogout',Userlogout),
    path('forgetpassword',ForgetPassword),
    path('setpassword',SetPassword),
    path('userprofileupdate',UserProfileUpdate),
    path('StoreSignup',StoreSignUp),
    path('StoreLogin',StoreLogin),
    path('vendorforgetpassword',vendorforgetpassword),
    path('vendorsetpassword',vendorSetPassword),
    path('Storelogout',Storelogout),
    path('StoreDashBoard',StoreDashBoard),
    path('Storeaccount',StoreAccount),
    path('Storelogout',Storelogout),
    path('Category',CategoryList),
    path('Addcategory',AddCategory),
    path('EditCategory/<category_id>',EditCategory),
    path('DeleteCategory/<category_id>',deleteCategory),
    path('EditSubCategory/<subcategory_id>',EditSubCategory),
    path('DeleteSubCategory/<subcategory_id>',deleteSubCategory),
    path('SubCategory',SubCategoryList),
    path('Addsubcategory',AddSubCategory),
    path('Product',AllProduct),
    path('AddProduct',AddProduct),
    path('EditProduct/<product_id>',EditProduct),
    path('DeleteProduct/<product_id>',deleteProduct),
    path('Advertisements',AllAdvertisement),
    path('AddAdvertisement',AddAdvertisement),
    path('EditAdvertisement/<advertisement_id>',EditAdvertisement),
    path('DeleteAdvertisement/<advertisement_id>',deleteAdvertisement),
    path('Coupon',Coupons),
    path('Addcoupon',Addcoupon),
    path('EditCoupon/<coupon_id>',EditCoupon),
    path('DeleteCoupon/<coupon_id>',deleteCoupon),
    path('applycoupon',applycoupon),
    path('Filter',Filter),
    path('Addfilter',AddFilter),
    path('EditFilter/<filter_id>',EditFilter),
    path('DeleteFilter/<filter_id>',deleteFilter),
    path('Attribute',Attribute),
    path('salesforthemonth',salesforthemonth),
    path('storepage',storepage),
    path('vendorpage/<shopcategory_id>',vendorpage),
    path('products/<store_id>',productview),
    path('product/<product_id>',singleproductview),
    path('like/<product_id>',likesingleproduct),
    path('addtocart/<product_id>',addtocart),
    path('similartocart/<product_id>',similartocart),
    path('cart',cart),
    path('charge',charge),
    path('orders',ordersview),


    path('about',about),
    path('career',carrer),
    path('contact',contact),
    path('customer',customer),


    path('userchat',userchat),
    path('vendorchat',vendorchat),

    path('DriverSignup',DriverSignup),
    path('DriverLogin',DriverLogin),
    path('Driverupdate',driverupdate),
    path('driverforgetpassword',driverforgetpassword),
    path('driversetpassword',driverSetPassword),
    path('DriverLogout',DriverLogout),
    path('driverorders',Driverorders),
    path('yesdriverorderpickup/<order_id>',yesdriverorderpickup),
    path('nodriverorderpickup/<order_id>',nodriverorderpickup)
]
