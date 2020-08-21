from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course #import templates to pass the context into the template
# BASE VIEW Class = VIEW

class CourseObjectMixin(object):
    model = Course
    #lookup = 'id' #then all the id/'id' need to be changed to lookup

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj

class CourseCreateView(View):
    template_name = "courses/course_create.html"
    def get(self, request, *args, **kwargs):
        #GET METHOD
        form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        #POST METHOD
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm() #reinitialized the form
        context = {"form": form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class CourseUpdateView(CourseObjectMixin, View): #the CourseObjectMixin class must be construct before this for inherit
    template_name = "courses/course_update.html"

    def get(self, request, id=None, *args, **kwargs):
        #GET METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj) #pass the object as an instance to the form
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        #POST METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html"

    def get(self, request, id=None, *args, **kwargs):
        #GET METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        #POST METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses')
        return render(request, self.template_name, context)

class CourseView(CourseObjectMixin, View):
    template_name = "courses/course_detail.html" #DetailView
    def get(self, request, id=None, *args, **kwargs): #need the self reference; id=None means the id is not requied
        context = {'object': self.get_object()}
        # if id is not None:
        #     obj = get_object_or_404(Course,id=id)
        #     context['object'] = obj
        return render(request, self.template_name, context)

    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})
    
#HTTP METHODS, here the name for an funciton based views does not matter; not like in the class based views
def my_fbv(requst, *args, **kwargs):
    return render(requst, 'about.html', {})