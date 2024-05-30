from django.urls import path
from app.views import ragister,tableview,deletetable,addtable,updatetable,filterdata


urlpatterns = [
    path('ragister/',ragister),
    path('',tableview,name='tableview'),
    path('deletetable/<int:id>',deletetable,name='deletetable'),
    path('addtable/',addtable,name='addtable'),
    path('updatetable/<int:id>',updatetable,name='updatetable'),
    path('filterdata/',filterdata,name='filterdata')
]
