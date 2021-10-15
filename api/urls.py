#URL routing settings for api objects that loads the correct veiws to send to the front end 
from django.conf.urls import url
from . import views


app_name = "api"
urlpatterns = [	
	url(r'^cart', views.CartView.as_view(), name="cart"),
	url(r'^payment', views.payment, name="payment"),
	]