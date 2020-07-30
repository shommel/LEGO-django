from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry

class HomeView(LoginRequiredMixin, ListView):
	model = Entry
	template_name = 'entries/index.html'
	context_object_name = "blog_entries" 
	
	#reverse chronological order (most recent posts first) 
	ordering = ['-date']
	
	#3 entries per page
	paginate_by = 3

class EntryView(LoginRequiredMixin, DetailView):
	model = Entry
	template_name='entries/entry_detail.html'

class CreateEntryView(LoginRequiredMixin, CreateView):
	model = Entry
	template_name = 'entries/create_entry.html'

	#necessary fields for creating an entry
	fields = ['title', 'text', 'num_pieces']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
