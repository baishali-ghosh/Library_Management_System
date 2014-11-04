from django.contrib import admin
from libsys.models import Member, Book, Publisher, Section, Borrow

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
	list_display = ('mid', 'fname', 'midname', 'lname') 

class BookAdmin(admin.ModelAdmin):
	list_display = ('bid', 'title', 'author', 'noofcopies', 'pubid', 'secid')

class SectionAdmin(admin.ModelAdmin):
	list_display = ('sid', 'sname' )

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('pid', 'name')

class BorrowAdmin(admin.ModelAdmin):
	list_display =('bookid', 'issuedate', 'duedate')

admin.site.register(Member, MemberAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Borrow, BorrowAdmin)