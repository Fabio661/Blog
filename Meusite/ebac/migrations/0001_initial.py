# Generated by Django 4.1.7 on 2023-03-26 03:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('editado_em', models.DateTimeField(auto_now=True)),
                ('conteudo', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Rascunho'), (1, 'Publicado')], default=0)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('conteudo', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='ebac.post')),
            ],
            options={
                'ordering': ['criado_em'],
            },
        ),
    ]
