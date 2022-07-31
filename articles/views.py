from multiprocessing import context
from typing import List
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.core.exceptions import BadRequest, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article, Section, Status
# Create your views here.
# create full CRUD procedures, list, create, delete, update view, cnosider draft/pending views

class ArticleNavBarHelper:
    def __init__(self, context):
        self.set_sections(context)
        self.set_statuses(context)

    def set_sections(self, context):
        context["sections"] = Section.objects.all()

    def set_statuses(self, context):
        context["statuses"] = Status.objects.all()


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles/list.html"

    def get_article_list_context(self, context, section, status):
        context["article_list"] = Article.objects.filter(
            section=section
        ).filter(
            status=status
        ).order_by("created_on").reverse()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status_id = self.kwargs.get("status")
        section_id = self.kwargs.get("section")
        user_department = self.request.user.department
        # raise BadRequest("Status ID: %s; Section ID: %s" % (status_id, section_id))
        status = Status.objects.get(id=status_id)
        section = Section.objects.get(id=section_id)
        ArticleNavBarHelper(context, user_department)
        if status.id == 2:
            return self.get_article_list_context(context, section, status)
        if self.request.user.role.id > 1:
            return self.get_article_list_context(context, section, status)
        raise PermissionDenied("You are not authorized to view this page")

class ArticleTotalListView(ListView):
    template_name = "articles/list.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_list"] = Articles.objects.filter(
            active=True
        ).order_by("created_on").reverse()
        context["current_datetime"] = datetime.now().strftime("%F %H:%M:%S")
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["article"].active == True:
            return context
        else:
            self.template_name = "errors/404.html"
            return context

class ArticleCreateView(CreateView):
    model = Article
    template_name = "articles/new.html"
    fields = [
        "title", "subtitle",
        "body", "status", "section"
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.instance.status == "published":
            raise BadRequest(
                "You are not authorized to publish; Request a review first."
            )
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "articles/edit.html"
    fields = [
        "title", "subtitle",
        "body", "status",
    ]

    def form_valid(self, form):
        if form.instance.status == "published":
            raise BadRequest(
                "You are not authorized to publish; Request a review first."
            )
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = reverse_lazy("home")