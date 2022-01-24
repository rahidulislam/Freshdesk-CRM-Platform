from accounts.models.account_models import Account
from accounts.models.bank_account_model import Bank
from django.contrib import admin


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_account_name', 'bank_account_number', 'account_type', 'bank_name', 'bank_short_name', 'bank_branch')
    search_fields = ('bank_account_name', 'bank_account_number', 'account_type', 'bank_name', 'bank_short_name', 'bank_branch')
    list_filter = ('account_type', 'bank_name', 'bank_short_name', 'bank_branch')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'country')
    search_fields = ('account_name', 'country', 'industry')
    list_filter = ('industry',)

    @admin.display(boolean=True, description='Is Opend?')
    def is_opend(self, obj):
        return obj.status is not None
