from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)
from django.core.exceptions import PermissionDenied
from .forms import ReportForm, SignUpForm
from django.contrib.auth import login
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


class ReportsView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url = "web:login"
    redirect_field_name = "web:reports"

    model = Report
    template_name = "webapp/reports.html"
    context_object_name = "latest_report_list"
    permission_required = ["webapp.can_view_reports"]

    # def test_func(self):
    #     """
    #     This method is required by UserPassesTestMixin to determine if the user passes a certain condition.
    #     """
    #     return self.request.user.has_perm("webapp.can_view_reports")

    # def handle_no_permission(self):
    #     """
    #     Override the method to provide custom behavior when the user fails the test.
    #     """
    #     if not self.request.user.is_authenticated:
    #         # Redirects to login page if the user isn't authenticated
    #         return super().handle_no_permission()
    #     else:
    #         # Raises a permission denied error if the user doesn't have the permission
    #         raise PermissionDenied(
    #             "Sorry, you do not have permission to view reports. Please contact admin."
    #         )

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


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect(
                "web:home"
            )  # Redirect to a home page or another appropriate page
    else:
        form = SignUpForm()
    return render(request, "webapp/signup.html", {"form": form})
