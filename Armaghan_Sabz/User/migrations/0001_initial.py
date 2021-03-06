# Generated by Django 3.2.7 on 2021-10-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('identity_code', models.IntegerField()),
                ('id_number', models.IntegerField()),
                ('serial_number', models.IntegerField()),
                ('address', models.CharField(max_length=500, unique=True)),
                ('post_cod', models.IntegerField()),
                ('landline', models.IntegerField()),
                ('phone_number', models.IntegerField(unique=True)),
                ('support_phone_number', models.IntegerField()),
                ('education', models.CharField(max_length=250)),
                ('grade', models.CharField(max_length=250)),
                ('cod_zip', models.IntegerField()),
                ('profession', models.CharField(max_length=300)),
                ('workplace_address', models.CharField(max_length=250)),
                ('job_position', models.CharField(max_length=250)),
                ('workplace_number', models.CharField(max_length=250)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
