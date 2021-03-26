# from django.shortcuts import render, get_object_or_404, redirect
# from django.core.mail import send_mail
# import telebot
# from .models import Post, Education, Experience, Certificates, Skills, Photo
# from .forms import ApplicationForm
#
#
# def index(request):
#     posts = Post.objects.all()
#     education = Education.objects.all()
#     experience = Experience.objects.all()
#     certificates = Certificates.objects.all()
#     skills = Skills.objects.all()
#     photo = Photo.objects.first()
#     return render(request, 'index.html', {
#         'all_posts': posts,
#         'education': education,
#         'experience': experience,
#         'certificates': certificates,
#         'skills': skills,
#         'photo': photo,
#     })
#
#
# def detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog-post-1.html', {'post': post})
#
#
# def contact(request):
#     bot = telebot.TeleBot('1596134202:AAHgSkzwY5xdFw7zeUZVHylZGpAzrmh8fGo')
#     if request.method == 'POST':
#         form = ApplicationForm(request.POST)
#         if form.is_valid():
#             to_email = ['initmenthor@gmail.com', ]
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             msg = f'Имя: {name} \nПочта: {email} \nТема{subject} \nСообщение: {message}'
#             send_mail(subject, message, to_email, email, fail_silently=False)
#             bot.send_message(959339948, msg)
#     return redirect('index')
