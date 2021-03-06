# Generated by Django 4.0.2 on 2022-02-18 16:43

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='title')),
                ('description', models.CharField(max_length=256, verbose_name='description')),
                ('type', models.CharField(max_length=128, verbose_name='type')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='title')),
                ('description', models.CharField(max_length=256, verbose_name='description')),
                ('tag', models.CharField(choices=[('BUG', 'BUG'), ('IMP', 'AMÉLIORATION'), ('TSK', 'TÂCHE')], default='BUG', max_length=3, verbose_name='tag')),
                ('priority', models.CharField(choices=[('LOW', 'FAIBLE'), ('MED', 'MOYENNE'), ('SUP', 'ÉLEVÉE')], default='LOW', max_length=3, verbose_name='priority')),
                ('status', models.CharField(choices=[('TOD', 'À faire'), ('DOI', 'En cours'), ('DON', 'Terminé')], default='TOD', max_length=3, verbose_name='status')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issuestracking.project')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('CREA', 'Créateur'), ('CONT', 'Contributeur')], default='CONT', max_length=128)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='issuestracking.project')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256, verbose_name='description')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='issuestracking.issue')),
            ],
        ),
        migrations.AddConstraint(
            model_name='contributor',
            constraint=models.UniqueConstraint(fields=('user', 'project'), name='no_double_contributor'),
        ),
    ]
