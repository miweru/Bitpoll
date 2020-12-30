# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 13:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=80)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('sort_key', models.IntegerField()),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('icon', models.CharField(max_length=64)),
                ('color', models.CharField(max_length=6)),
                ('weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('spam', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('url', models.SlugField(max_length=80, unique=True)),
                ('type', models.CharField(choices=[('universal', 'Universal'), ('datetime', 'Date-Time'), ('date', 'Date')], default='universal', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('anonymous_allowed', models.BooleanField(default=True)),
                ('public_listening', models.BooleanField(default=False)),
                ('require_login', models.BooleanField(default=False)),
                ('require_invitation', models.BooleanField(default=False)),
                ('show_results', models.CharField(choices=[('summary', 'Summary'), ('complete', 'Complete'), ('never', 'Never'), ('summary after vote', 'Summary after Vote'), ('complete after vote', 'Complete after Vote')], default='complete', max_length=20)),
                ('send_mail', models.BooleanField(default=False)),
                ('one_vote_per_user', models.BooleanField(default=True)),
                ('allow_comments', models.BooleanField(default=True)),
                ('show_invitations', models.BooleanField(default=True)),
                ('timezone_name', models.CharField(default='Europe/Berlin', max_length=40)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PollWatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('anonymous', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField()),
                ('comment', models.TextField()),
                ('assigned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigning', to=settings.AUTH_USER_MODEL)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VoteChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Choice')),
                ('value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.ChoiceValue')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Vote')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='choicevalue',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll'),
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll'),
        ),
        migrations.AlterUniqueTogether(
            name='votechoice',
            unique_together=set([('vote', 'choice')]),
        ),
    ]
