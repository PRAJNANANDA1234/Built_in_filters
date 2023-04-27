from django.shortcuts import render

# Create your views here.
def built_in_filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'HIi fRindSs...','dt':dt,'c':2}
    return render(request,'built_in_filter.html',d)