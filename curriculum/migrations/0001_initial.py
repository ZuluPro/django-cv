# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('authority', models.CharField(max_length=200, verbose_name='authority')),
                ('url', models.URLField(max_length=300, verbose_name='url', blank=True)),
                ('description', models.TextField(max_length=2000, verbose_name='description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CertificationItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_year', models.IntegerField(verbose_name='start year')),
                ('start_month', models.IntegerField(verbose_name='start month')),
                ('expires', models.BooleanField(default=False, verbose_name='expires')),
                ('end_year', models.IntegerField(null=True, verbose_name='end year', blank=True)),
                ('end_month', models.IntegerField(null=True, verbose_name='end month', blank=True)),
                ('certification', models.ForeignKey(related_name='items', to='curriculum.Certification')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('entreprise', models.CharField(max_length=200, verbose_name='entreprise')),
                ('description', models.TextField(max_length=3000, verbose_name='description', blank=True)),
                ('type', models.CharField(max_length=5, null=True, verbose_name='type', choices=[(None, 'unknown'), (b'SALAR', 'salaried'), (b'CHIEF', 'founder/chief'), (b'FREEL', 'freelance/chief'), (b'OTHER', 'other')])),
                ('start_year', models.IntegerField(verbose_name='start year')),
                ('start_month', models.IntegerField(verbose_name='start month')),
                ('still', models.BooleanField(default=True, verbose_name='still in office')),
                ('end_year', models.IntegerField(null=True, verbose_name='end year', blank=True)),
                ('end_month', models.IntegerField(null=True, verbose_name='end month', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=50, unique=True, serialize=False, verbose_name='name', primary_key=True)),
                ('description', models.TextField(max_length=2000, verbose_name='description', blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='LanguageItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(default=b'NOT', max_length=5, verbose_name='level', choices=[(b'NOT', 'Notion'), (b'BAS', 'basic'), (b'ADV', 'advanced'), (b'PRO', 'professional'), (b'BIL', 'bilingual')])),
                ('language', models.ForeignKey(related_name='items', to='curriculum.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200, verbose_name='title')),
                ('description', models.TextField(max_length=3000, verbose_name='description', blank=True)),
                ('url', models.CharField(max_length=300, verbose_name='URL', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contribution', models.TextField(max_length=3000, verbose_name='contribution', blank=True)),
                ('start_year', models.IntegerField(verbose_name='start year')),
                ('start_month', models.IntegerField(verbose_name='start month')),
                ('still', models.BooleanField(default=True, verbose_name='still contributor')),
                ('end_year', models.IntegerField(null=True, verbose_name='end year', blank=True)),
                ('end_month', models.IntegerField(null=True, verbose_name='end month', blank=True)),
                ('project', models.ForeignKey(related_name='items', to='curriculum.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=150, verbose_name='First name')),
                ('lastname', models.CharField(max_length=150, verbose_name='Last name')),
                ('title', models.CharField(max_length=200, verbose_name='Title', blank=True)),
                ('resume', models.TextField(max_length=3000, verbose_name='resume', blank=True)),
                ('image', models.ImageField(upload_to=b'', verbose_name='image', blank=True)),
                ('phone', models.CharField(max_length=100, verbose_name='phone', blank=True)),
                ('website', models.CharField(max_length=300, verbose_name='website', blank=True)),
                ('email', models.CharField(max_length=100, verbose_name='email', blank=True)),
                ('address', models.CharField(max_length=300, verbose_name='address', blank=True)),
                ('driving_license', models.CharField(max_length=100, verbose_name='driving license', blank=True)),
                ('hobbies', models.TextField(max_length=1000, verbose_name='hobbies', blank=True)),
                ('tags', models.CharField(max_length=500, verbose_name='tags', blank=True)),
            ],
            options={
                'verbose_name': 'resume',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200, verbose_name='name')),
                ('description', models.TextField(max_length=2000, verbose_name='description', blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SkillItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E'), (b'D', b'D')])),
                ('resume', models.ForeignKey(related_name='skills', to='curriculum.Resume')),
                ('skill', models.ForeignKey(related_name='items', to='curriculum.Skill', to_field=b'name')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(max_length=150, verbose_name='school')),
                ('degree', models.CharField(max_length=150, verbose_name='degree')),
                ('topic', models.CharField(max_length=150, verbose_name='topic', blank=True)),
                ('result', models.CharField(max_length=150, verbose_name='result', blank=True)),
                ('description', models.TextField(max_length=3000, verbose_name='description', blank=True)),
                ('year', models.IntegerField(verbose_name='year')),
                ('month', models.IntegerField(verbose_name='month')),
                ('resume', models.ForeignKey(related_name='trainings', to='curriculum.Resume')),
            ],
        ),
        migrations.AddField(
            model_name='projectitem',
            name='resume',
            field=models.ForeignKey(related_name='projects', to='curriculum.Resume'),
        ),
        migrations.AddField(
            model_name='languageitem',
            name='resume',
            field=models.ForeignKey(related_name='languages', to='curriculum.Resume'),
        ),
        migrations.AddField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(related_name='experiences', to='curriculum.Resume'),
        ),
        migrations.AddField(
            model_name='certificationitem',
            name='resume',
            field=models.ForeignKey(related_name='certifications', to='curriculum.Resume'),
        ),
        migrations.AlterUniqueTogether(
            name='certification',
            unique_together=set([('title', 'authority')]),
        ),
        migrations.AlterUniqueTogether(
            name='skillitem',
            unique_together=set([('skill', 'resume')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectitem',
            unique_together=set([('resume', 'project')]),
        ),
        migrations.AlterUniqueTogether(
            name='languageitem',
            unique_together=set([('language', 'resume')]),
        ),
        migrations.AlterUniqueTogether(
            name='certificationitem',
            unique_together=set([('certification', 'resume')]),
        ),
    ]
