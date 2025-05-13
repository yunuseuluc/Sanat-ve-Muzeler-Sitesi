from django.contrib import admin
from .models import Sehir, Muze, Sanatci, SanatciResim, Eser, EserResim, Yorum

# Inline tanımları
class SanatciResimInline(admin.TabularInline):
    model = SanatciResim
    extra = 1

class EserResimInline(admin.TabularInline):
    model = EserResim
    extra = 1

# Admin sınıfları
@admin.register(Sanatci)
class SanatciAdmin(admin.ModelAdmin):
    inlines = [SanatciResimInline]

@admin.register(Eser)
class EserAdmin(admin.ModelAdmin):
    inlines = [EserResimInline]

# Diğer modellerin kaydı
admin.site.register(Sehir)
admin.site.register(Muze)
admin.site.register(Yorum)
