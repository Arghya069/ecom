# Generated by Django 3.2.9 on 2022-04-21 12:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('productname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('productdesc', models.CharField(max_length=300)),
                ('product_cost', models.FloatField()),
                ('available_quantity', models.IntegerField(default=1)),
                ('product_image', models.ImageField(default='default.png', upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('mobile', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('Email', models.EmailField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('photo', models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
