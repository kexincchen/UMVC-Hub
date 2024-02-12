from django.contrib import admin
from .models import Report, Tag


# class TagInline(admin.TabularInline):
#     model = Tag
#     extra = 3

# class ReportAdmin(admin.ModelAdmin):
#     # fields = ["pub_date", "name"]
#     fieldsets = [
#         (None, {"fields": ["name"]}),
#         ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
#     ]
#     inlines = [TagInline]


class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {"fields": ["name", "tags", "description"]},
        ),  # Add "tags" to the fields list
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    filter_horizontal = ("tags",)  # This makes the tags selection easier to use
    list_display = ["name", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["name"]


admin.site.register(Report, ReportAdmin)
admin.site.register(Tag)
