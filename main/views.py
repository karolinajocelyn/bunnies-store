from django.shortcuts import render

def show_main(request):
    context= {
        'name': 'Karolina Jocelyn',
        'class': 'PBP D'
    }
    
    return render(request, 'main.html', context)