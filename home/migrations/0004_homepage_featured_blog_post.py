# Generated by Django 2.2.6 on 2019-11-10 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0003_auto_20191031_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='featured_blog_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
