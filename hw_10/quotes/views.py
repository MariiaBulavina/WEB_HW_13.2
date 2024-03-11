from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import  AuthorForm, QuoteForm
from .models import Author, Quote


def main(request, page=1):

    quotes = Quote.objects.select_related('author').prefetch_related('tags').all().order_by('created_at')
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


@login_required
def author(request):

    if request.method == 'POST':

        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})

    return render(request, 'quotes/add_author.html', {'form': AuthorForm()})


@login_required
def quote(request):

    if request.method == 'POST':
        
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_quote.html', {'form': form})

    return render(request, 'quotes/add_quote.html', {'form': QuoteForm()})


def author_info(request, name):

    author = get_object_or_404(Author, fullname=name)
    return render(request, 'quotes/author_info.html', {'author': author})


def found_by_teg(request, tag):
    
    quotes = Quote.objects.filter(tags__name__in=[tag])
    return render(request, 'quotes/found_by_tag.html', {'quotes': quotes, 'tag': tag})

