from django.shortcuts import render, get_object_or_404

# from django.http import Http404
from .models import Report


# def home(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    return render(request, "webapp/home.html")


# def vision(request):
#     return render(request, 'vision.html')

# def history(request):
#     return render(request, 'history.html')

# def activities(request):
#     return render(request, 'activities.html')

# def member_gallery(request):
#     return render(request, 'member_gallery.html')


def reports(request):
    # This view will later include logic to check if a user is logged in and has member access
    latest_report_list = Report.objects.order_by("-pub_date")[:5]
    context = {
        "latest_report_list": latest_report_list,
    }
    return render(request, "webapp/reports.html", context)
    # return HttpResponse(template.render(context, request))
    # output = ", ".join([r.name for r in latest_report_list])
    # return HttpResponse(output)


# def detail(request, report_id):
#     try:
#         report = Report.objects.get(pk=report_id)
#     except Report.DoesNotExist:
#         raise Http404("Report does not exist")
#     return render(request, "webapp/detail.html", {"report": report})
# ======= A Better Coding =============
def detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, "webapp/detail.html", {"report": report})
