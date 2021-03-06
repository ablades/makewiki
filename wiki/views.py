from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PageList(ListView):
    """
      Provides an overview of all page content
      pages_list: List of all wiki pages on the website
    """
    model = Page

    def get(self, request):
        """ Returns a list of wiki pages. """
        pages_list = list(Page.objects.all())
        model = Page
        return render(request, 'wiki/list.html', {'pages_list': pages_list})


class PageDetailView(DetailView):
    """
      Returns a single object page based on the objects slug

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """
    model = Page

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """

        #find page associated with the slug i_exact() better - case insensitve
        single_page = Page.objects.get(slug=slug)

        return render(request, 'wiki/page.html', {'page' : single_page} )

    def post(self, request, slug):
        pass
