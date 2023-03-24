from django.shortcuts import render
from datetime import datetime

# Create your views here.
# if ((ay == 12) || (ay == 1) || (ay == 2)) Console.WriteLine("Winter");
# if ((ay == 3) || (ay == 4) || (ay == 5)) Console.WriteLine("Spring");
# if ((ay == 6) || (ay == 7) || (ay == 8)) Console.WriteLine("Summer");
# if ((ay == 9) || (ay == 10) || (ay == 11)) Console.WriteLine("Autumn");

def season(request):
    now = datetime.now()

    if now.month == 12 or  now.month == 1 or now.month == 2:
        return render(request, "winter.html")
    
    if now.month == 3 or  now.month == 4 or now.month == 5:
        return render(request, "spring.html")
    
    if now.month == 6 or  now.month == 7 or now.month == 8:
        return render(request, "summer.html")
    
    if now.month == 9 or  now.month == 10 or now.month == 11:
        return render(request, "autumn.html")

