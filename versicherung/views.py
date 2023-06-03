from django.shortcuts import render


# Create your views here.
def schadensfall_list(request: HttpRequest):
    schadensfall_list = Schadensfall.objects.all()
    context = {"schadensfall_list": schadensfall_list}
    return render(request, "schadensfall/schadensfall_list.html", context)
