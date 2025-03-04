# Generated by Django 5.1.6 on 2025-03-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificates',
            options={'ordering': ['-issue_date']},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-end_date', '-start_date'], 'verbose_name_plural': 'Education'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['-end_date', '-start_date']},
        ),
        migrations.AlterModelOptions(
            name='personalinformation',
            options={'verbose_name_plural': 'Personal Information'},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('short_description', models.CharField(max_length=100)),
                ('detailed_description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_images')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_ongoing', models.BooleanField(default=False)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('skills', models.ManyToManyField(related_name='project', to='resume.skill')),
            ],
            options={
                'ordering': ['-end_date', '-start_date'],
            },
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
