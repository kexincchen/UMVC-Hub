from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ReportForm
from .models import Report


# def home(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# def home(request):
#     return render(request, "webapp/home.html")


# def vision(request):
#     return render(request, 'vision.html')

# def history(request):
#     return render(request, 'history.html')

# def activities(request):
#     return render(request, 'activities.html')

# def member_gallery(request):
#     return render(request, 'member_gallery.html')


# def reports(request):
#     # This view will later include logic to check if a user is logged in and has member access
#     latest_report_list = Report.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_report_list": latest_report_list,
#     }
#     return render(request, "webapp/reports.html", context)
#     # return HttpResponse(template.render(context, request))
#     # output = ", ".join([r.name for r in latest_report_list])
#     # return HttpResponse(output)


# def detail(request, report_id):
#     try:
#         report = Report.objects.get(pk=report_id)
#     except Report.DoesNotExist:
#         raise Http404("Report does not exist")
#     return render(request, "webapp/detail.html", {"report": report})
# ======= A Better Coding =============
# def detail(request, report_id):
#     report = get_object_or_404(Report, pk=report_id)
#     return render(request, "webapp/detail.html", {"report": report})
# ======= A BETTER Better Coding (Generic View)=============


class HomeView(generic.TemplateView):
    template_name = "webapp/home.html"


class DetailView(generic.DetailView):
    model = Report
    template_name = "webapp/detail.html"


class ReportsView(LoginRequiredMixin, generic.ListView):
    login_url = "web:login"
    redirect_field_name = "web:reports"

    model = Report
    template_name = "webapp/reports.html"
    context_object_name = "latest_report_list"

    def get_queryset(self):
        """
        Return the last five published reports (not including those set to be
        published in the future).
        """
        return Report.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]

    # def get_queryset(self):
    #     """Return the last five published reports."""
    #     return Report.objects.order_by("-pub_date")[:5]


def upload_report(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("web:reports")
    else:
        form = ReportForm()
    return render(request, "webapp/upload_report.html", {"form": form})


def update_report(request, report_id):
    """Update an existing report"""
    return render(request, "webapp/home.html")
