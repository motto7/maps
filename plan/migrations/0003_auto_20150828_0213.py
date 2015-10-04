# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plan', '0002_post_lnglat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='transits',
            field=models.ManyToManyField(blank=True, to='plan.Transit'),
        ),
    ]
