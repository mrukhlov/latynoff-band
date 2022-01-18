from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'pages/index.html'


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class MediaPageView(TemplateView):
    template_name = 'pages/media.html'


class RepertoirePageView(TemplateView):
    template_name = 'pages/repertoire.html'


class OrganizersPageView(TemplateView):
    template_name = 'pages/org.html'


class ContactsPageView(TemplateView):
    template_name = 'pages/contacts.html'


class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'


class BlogArticlePageView(TemplateView):
    template_name = 'pages/blog_page.html'