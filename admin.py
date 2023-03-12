from django.contrib import admin
from .models import Admin
from .models import Customers
from .models import Agent
from .models import Address
from .models import Places
from .models import Packages
from .models import Itinerary
from .models import Day
from .models import Hotel
from .models import Booking
from .models import Payment
from .models import Cancellation
from .models import Enquiry
from .models import Feedback

admin.site.register(Admin)
admin.site.register(Customers)
admin.site.register(Agent)
admin.site.register(Address)
admin.site.register(Places)
admin.site.register(Packages)
admin.site.register(Itinerary)
admin.site.register(Day)
admin.site.register(Hotel)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Cancellation)
admin.site.register(Enquiry)
admin.site.register(Feedback)

# from .models import User

# Register your models here.
# admin.site.register(User)
