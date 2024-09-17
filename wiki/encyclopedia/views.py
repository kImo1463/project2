from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . import util
from .util import get_entry, save_entry
import random
import markdown2

from django.shortcuts import render, redirect
from . import util

from django.shortcuts import render, redirect
from . import util

def create_page(request, title=None):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        
        if util.get_entry(title) is not None:
            return render(request, 'encyclopedia/create.html', {
                'title': title,
                'error': 'A page with this title already exists.'
            })
        
        util.save_entry(title, content)
        return redirect(f'/wiki/{title}')
    else:
        return render(request, 'encyclopedia/create.html', {
            'title': title if title else ''
        })

def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        
        save_entry(title, content)
        
        return redirect("entry", title=title)
    else:
        entry_content = get_entry(title)
        
        
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": entry_content
        })
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title": None  
    })

def entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The page you are requesting is not available."
        })
    
    html_content = markdown2.markdown(entry_content)
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def search(request):
    query = request.GET.get('q', '')
    if util.get_entry(query) is not None:
        return HttpResponseRedirect(f"/wiki/{query}")
    else:
        matching_entries = [entry for entry in util.list_entries() if query.lower() in entry.lower()]
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "entries": matching_entries
        })

        
def random_page(request):
    all_entries = util.list_entries()
    
    random_title = random.choice(all_entries)
    
    return redirect("entry", title=random_title)