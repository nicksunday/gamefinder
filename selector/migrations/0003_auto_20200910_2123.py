# Generated by Django 3.1.1 on 2020-09-11 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selector', '0002_auto_20200910_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('artist_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'artists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Designers',
            fields=[
                ('designer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('designer', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'designers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Families',
            fields=[
                ('family_id', models.IntegerField(primary_key=True, serialize=False)),
                ('family', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'families',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GameArtists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'game_artists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GameCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'game_categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GameDesigners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'game_designers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GameFamilies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'game_families',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GameMechanics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'game_mechanics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GamePublishers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'game_publishers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('average', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('minplayers', models.IntegerField(blank=True, null=True)),
                ('maxplayers', models.IntegerField(blank=True, null=True)),
                ('playingtime', models.IntegerField(blank=True, null=True)),
                ('yearpublished', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=100, null=True)),
                ('game_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'games',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GameSubdomains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'game_subdomains',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mechanics',
            fields=[
                ('mechanic_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mechanic', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'mechanics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('publisher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'publishers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subdomains',
            fields=[
                ('subdomain_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subdomain', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'subdomains',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Designer',
        ),
        migrations.DeleteModel(
            name='Family',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='GameArtist',
        ),
        migrations.DeleteModel(
            name='GameCategory',
        ),
        migrations.DeleteModel(
            name='GameDesigner',
        ),
        migrations.DeleteModel(
            name='GameFamily',
        ),
        migrations.DeleteModel(
            name='GameMechanic',
        ),
        migrations.DeleteModel(
            name='GamePublisher',
        ),
        migrations.DeleteModel(
            name='GameSubdomain',
        ),
        migrations.DeleteModel(
            name='Mechanic',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='Subdomain',
        ),
    ]
