from django.contrib import admin
from .models import User, FriendReview, FriendSetting, UserReview, Dispute, Payment, Withdrawal, Order, Log
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'birthday', 'profile_type', 'wallet')
    search_fields = ('first_name', 'last_name', 'email', 'pk')

class FriendSettingAdmin(admin.ModelAdmin):
    list_display = ('pk','friend', 'price_per_hour', 'is_public')
    search_fields = ('friend',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'friend', 'order_status', 'total_price', 'fee', 'profit', 'created')
    search_fields =('user', 'friend')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('created', 'pk', 'order', 'amount', 'was_disputed', 'date_of_payout')

class WithdrawalAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Withdrawal._meta.fields]

class DisputeAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Dispute._meta.fields]

class UserReviewAdmin(admin.ModelAdmin):
    list_display  = ('pk', 'user', 'friend', 'order', 'post_as_anon', 'created', 'modified')

class FriendReviewAdmin(admin.ModelAdmin):
    list_display  = ('pk', 'friend', 'user', 'order', 'post_as_anon', 'created', 'modified')

class LogAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Log._meta.fields]


admin.site.register(User, UserAdmin)
admin.site.register(FriendSetting, FriendSettingAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Withdrawal, WithdrawalAdmin)
admin.site.register(Dispute, DisputeAdmin)
admin.site.register(UserReview, UserReviewAdmin)
admin.site.register(FriendReview, FriendReviewAdmin)
admin.site.register(Log, LogAdmin)