import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Report


class ReportModelTests(TestCase):
    def test_was_published_recently_with_old_report(self):
        """
        was_published_recently() returns False for reports whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_report = Report(pub_date=time)
        self.assertIs(old_report.was_published_recently(), False)

    def test_was_published_recently_with_recent_report(self):
        """
        was_published_recently() returns True for reports whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_report = Report(pub_date=time)
        self.assertIs(recent_report.was_published_recently(), True)

def create_report(name, days):
    """
    Create a report with the given `name` and published the
    given number of `days` offset to now (negative for reports published
    in the past, positive for reports that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Report.objects.create(name=name, pub_date=time)


class ReportIndexViewTests(TestCase):
    def test_no_reports(self):
        """
        If no reports exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("web:reports"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No reports are available.")
        self.assertQuerySetEqual(response.context["latest_report_list"], [])

    def test_past_report(self):
        """
        Reports with a pub_date in the past are displayed on the
        reports page.
        """
        report = create_report(name="Past report.", days=-30)
        response = self.client.get(reverse("web:reports"))
        self.assertQuerySetEqual(
            response.context["latest_report_list"],
            [report],
        )

    def test_future_report(self):
        """
        Reports with a pub_date in the future aren't displayed on
        the reports page.
        """
        create_report(name="Future report.", days=30)
        response = self.client.get(reverse("web:reports"))
        self.assertContains(response, "No reports are available.")
        self.assertQuerySetEqual(response.context["latest_report_list"], [])

    def test_future_report_and_past_report(self):
        """
        Even if both past and future reports exist, only past reports
        are displayed.
        """
        report = create_report(name="Past report.", days=-30)
        create_report(name="Future report.", days=30)
        response = self.client.get(reverse("web:reports"))
        self.assertQuerySetEqual(
            response.context["latest_report_list"],
            [report],
        )

    def test_two_past_reports(self):
        """
        The reports reports page may display multiple reports.
        """
        report1 = create_report(name="Past report 1.", days=-30)
        report2 = create_report(name="Past report 2.", days=-5)
        response = self.client.get(reverse("web:reports"))
        self.assertQuerySetEqual(
            response.context["latest_report_list"],
            [report2, report1],
        )