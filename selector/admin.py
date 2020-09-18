from django.contrib import admin
from .models import Artists, Categories, Designers, Families, GameArtists, GameCategories, GameDesigners, GameFamilies, GameMechanics, GamePublishers, GameSubdomains, Games, Mechanics, Publishers, Subdomains 
# Register your models here.

#admin.site.register(Artists)
#admin.site.register(Categories)
#admin.site.register(Designers)
#admin.site.register(Families)
#admin.site.register(GameArtists)
#admin.site.register(GameCategories)
#admin.site.register(GameDesigners)
#admin.site.register(GameFamilies)
#admin.site.register(GameMechanics)
#admin.site.register(GamePublishers)
#admin.site.register(GameSubdomains)
#admin.site.register(Games)
#admin.site.register(Mechanics)
#admin.site.register(Publishers)
#admin.site.register(Subdomains)

@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category',)

@admin.register(Designers)
class DesignersAdmin(admin.ModelAdmin):
    list_display = ('designer',)

@admin.register(Families)
class FamiliesAdmin(admin.ModelAdmin):
    list_display = ('family',)

@admin.register(GameArtists)
class GameArtistsAdmin(admin.ModelAdmin):
    pass

@admin.register(GameCategories)
class GameCategoriesAdmin(admin.ModelAdmin):
    pass

@admin.register(GameDesigners)
class GameDesignersAdmin(admin.ModelAdmin):
    pass

@admin.register(GameFamilies)
class GameFamiliesAdmin(admin.ModelAdmin):
    pass

@admin.register(GameMechanics)
class GameMechanicsAdmin(admin.ModelAdmin):
    pass

@admin.register(GamePublishers)
class GamePublishersAdmin(admin.ModelAdmin):
    pass

@admin.register(GameSubdomains)
class GameSubdomainsAdmin(admin.ModelAdmin):
    pass

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('name', 'average', 'minplayers', 'maxplayers', 'thumbnail')
    list_filter = ('minplayers', 'maxplayers')

@admin.register(Mechanics)
class MechanicsAdmin(admin.ModelAdmin):
    pass

@admin.register(Publishers)
class PublishersAdmin(admin.ModelAdmin):
    pass

@admin.register(Subdomains)
class SubdomainsAdmin(admin.ModelAdmin):
    pass
