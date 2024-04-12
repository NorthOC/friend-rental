from django.contrib import admin
from .models import User, FriendReview, FriendSetting, UserReview, Dispute, Payment, Withdrawal, Order
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'birthday', 'profile_type', 'wallet')
    search_fields = ('first_name', 'last_name', 'email', 'pk')

admin.site.register(User, UserAdmin)
admin.site.register(FriendSetting)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Withdrawal)
admin.site.register(Dispute)
admin.site.register(UserReview)
admin.site.register(FriendReview)