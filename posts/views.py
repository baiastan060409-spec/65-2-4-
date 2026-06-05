from django.views.generic import ListView, DetailView
from posts.models import Post, Category

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(is_active=True).select_related('category')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем список категорий отдельно от постов
        context['categories'] = Category.objects.filter(is_active=True)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.filter(is_active=True)