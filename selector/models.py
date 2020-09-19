# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class Artists(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        managed = False
        db_table = 'artists'
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        managed = False
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Designers(models.Model):
    designer_id = models.IntegerField(primary_key=True)
    designer = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.designer}'

    class Meta:
        managed = False
        db_table = 'designers'
        verbose_name = 'Designer'
        verbose_name_plural = 'Designers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Families(models.Model):
    family_id = models.IntegerField(primary_key=True)
    family = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.family}'

    class Meta:
        managed = False
        db_table = 'families'
        verbose_name = 'Family'
        verbose_name_plural = 'Families'


class GameArtists(models.Model):
    game_artist_id = models.IntegerField(primary_key=True)
    game = models.ForeignKey('Games', on_delete=models.SET_NULL, blank=True, null=True)
    artist = models.ForeignKey('Artists', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_artists'
        verbose_name = 'Game Artist'
        verbose_name_plural = 'Game Artists'


class GameCategories(models.Model):
    game_category_id = models.IntegerField(primary_key=True)
    game = models.ForeignKey('Games', on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey('Categories', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_categories'
        verbose_name = 'Game Category'
        verbose_name_plural = 'Game Categories'


class GameDesigners(models.Model):
    game_designer_id = models.IntegerField(primary_key=True)
    game = models.ForeignKey('Games', on_delete=models.SET_NULL, blank=True, null=True)
    designer = models.ForeignKey('Designers', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_designers'
        verbose_name = 'Game Designer'
        verbose_name_plural = 'Game Designers'


class GameFamilies(models.Model):
    game_family_id = models.IntegerField(primary_key=True)
    game = models.ForeignKey('Games', on_delete=models.SET_NULL, blank=True, null=True)
    family = models.ForeignKey('Families', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_families'
        verbose_name = 'Game Family'
        verbose_name_plural = 'Game Families'


class GameMechanics(models.Model):
    game_mechanic_id = models.IntegerField(primary_key=True)
    game = models.ForeignKey('Games', on_delete=models.SET_NULL, blank=True, null=True)
    mechanic = models.ForeignKey('Mechanics', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_mechanics'
        verbose_name = 'Game Mechanic'
        verbose_name_plural = 'Game Mechanics'


class GamePublishers(models.Model):
    game_publisher_id = models.IntegerField(primary_key=True)
    game = models.ForeignKey('Games', on_delete=models.SET_NULL, blank=True, null=True)
    publisher = models.ForeignKey('Publishers', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_publishers'
        verbose_name = 'Game Publisher'
        verbose_name_plural = 'Game Publishers'


class GameSubdomains(models.Model):
    game_subdomain_id = models.IntegerField(primary_key=True)
    game = models.ForeignKey('Games', on_delete=models.SET_NULL, blank=True, null=True)
    subdomain = models.ForeignKey('Subdomains', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_subdomains'
        verbose_name = 'Game Subdomain'
        verbose_name_plural = 'Game Subdomains'


class Games(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    average = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    minplayers = models.IntegerField(blank=True, null=True)
    maxplayers = models.IntegerField(blank=True, null=True)
    playingtime = models.IntegerField(blank=True, null=True)
    yearpublished = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    game_id = models.IntegerField(primary_key=True)

    artists = models.ManyToManyField('Artists', through='GameArtists', related_name='game_id')
    categories = models.ManyToManyField('Categories', through='GameCategories', related_name='game_id')
    designers = models.ManyToManyField('Designers', through='GameDesigners', related_name='game_id')
    families = models.ManyToManyField('Families', through='GameFamilies', related_name='game_id')
    mechanics = models.ManyToManyField('Mechanics', through='GameMechanics', related_name='game_id')
    publishers = models.ManyToManyField('Publishers', through='GamePublishers', related_name='game_id')
    subdomains = models.ManyToManyField('Subdomains', through='GameSubdomains', related_name='game_id')

    def get_absolute_url(self):
        return reverse('games-detail', args=[str(self.game_id)])

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['game_id']
        managed = False
        db_table = 'games'
        verbose_name = 'Game'
        verbose_name_plural = 'Games'


class Mechanics(models.Model):
    mechanic_id = models.IntegerField(primary_key=True)
    mechanic = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.mechanic}'

    class Meta:
        managed = False
        db_table = 'mechanics'
        verbose_name = 'Mechanic'
        verbose_name_plural = 'Mechanics'


class Publishers(models.Model):
    publisher_id = models.IntegerField(primary_key=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.publisher}'

    class Meta:
        managed = False
        db_table = 'publishers'
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'


class Subdomains(models.Model):
    subdomain_id = models.IntegerField(primary_key=True)
    subdomain = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.subdomain}'

    class Meta:
        managed = False
        db_table = 'subdomains'
        verbose_name = 'Subdomain'
        verbose_name_plural = 'Subdomains'
