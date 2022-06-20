from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from todo.models import Todo, Category, Tag


def mainpage(request):
    return render(request, 'todo/mainpage.html')


class TodoList(ListView):
    model = Todo


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TodoList,self).get_context_data()
        context['todos'] = Todo.objects.all()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Todo.objects.filter(category=None).count()

        return context


class TodoDetail(DetailView):
    model = Todo


def cagegories_page(request, slug):
    if slug=='no-category':
        category='미분류'
        todo_list = Todo.objects.filter(category=None)
    else :
        category = Category.objects.get(slug = slug)
        todo_list = Todo.objects.filter(category = category)

    context = {
        'categories' : Category.objects.all(),
        'no_category_count' : Todo.objects.filter(category=None).count(),
        'category' : category,
        'todo_list' : todo_list
    }
    return render(request, 'todo/todo_list.html', context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug = slug)
    todo_list = tag.todo_set.all()

    context = {
        'categories' : Category.objects.all(),
        'category_less_post_count' : Todo.objects.filter(category=None).count(),
        'tag' : tag,
        'todo_list' : todo_list
    }
    return render(request, 'todo/todo_list.html', context)


class TodoCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Todo
    fields = ['todo', 'description', 'created_at', 'deadline', 'category', 'tags']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        if self.request.user.is_authenticated and (self.request.user.is_superuser or self.request.user.is_staff) :
            form.instance.author = self.request.user
            return super(TodoCreate, self).form_valid(form)
        else:
            return redirect('/list')


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['todo', 'description', 'deadline', 'category', 'tags']
    template_name = "todo/todo_form_update.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(TodoUpdate, self).dispatch(request,*args, **kwargs)
        else:
            raise PermissionDenied