from django.shortcuts import render
from django.contrib.auth.decorators import login_required

products = [
    {
        'image' : 'https://image1.jdomni.in/product/30082021/70/F6/A0/C39895844D39574A6FEDFAA5D9_1630321410745.jpg',
        'name' : 'Soundcore Life Q35',
        'price' : '9,999'
    },
    {
        'image' : 'https://image1.jdomni.in/product/30082021/3D/63/E4/F0F89651CB0229322BCE8787FA_1630321274077.jpg',
        'name' : 'Soundcore R500',
        'price' : '1,699'
    },
    {
        'image' : 'https://image1.jdomni.in/product/30082021/06/E1/16/4C1BC0F70B2313C2AC7B8EFD5A_1630321534604.jpg',
        'name' : 'Soundcore R100',
        'price' : '1,999'
    },
    {
        'image' : 'https://image1.jdomni.in/product/17012021/37/0C/B3/61E6DADA3FE0E61B1E6297E4A1_1610839950061.jpeg',
        'name' : 'Soundcore Life Q10',
        'price' : '2,999'
    },
]



@login_required(login_url='login')
def index(request):
    return render(request, 'home/index.html',{
        'products': products
    })
