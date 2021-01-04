from django.contrib import admin

# Register your models here.
from .models import Cameras

admin.site.index_title = "实景观测管理后台"
admin.site.site_header = "实景观测管理系统"
admin.site.site_title = "实景观测管理系统"
@admin.register(Cameras)
class CamerasAdmin(admin.ModelAdmin):
    list_display = [
        'camera_id', 'camera_name','user', 'access_key_id',
        'access_key_secret', 'link',
        'region', 
    ]

    search_fields = [
        'user__username', 'region', "camera_id"
    ]

    list_filter = [
        "camera_id", 'user__username'
    ]

    ordering = [ 'user' ]
    def camera_id(self, obj):
        return obj.camera_id
    

    def key_id(self, obj):
        return obj.access_key_id
    key_id.short_description = 'aaa'
