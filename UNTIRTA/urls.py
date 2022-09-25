from FAPERTA.views import faperta
from FEB.views import feb
from FH.views import fh
from FISIP.views import fisip
from FK.views import fk
from FKIP.views import fkip
from FT.views import ft
from PASCASARJANA.views import pascasarjana
from Profil.views import profil
from . import views

urlpatterns = [
    ('FAPERTA/', faperta), 
    ('feb/', feb),
    ('FH/', fh),
    ('FISIP/', fisip),
    ('FK/', fk),
    ('FKIP/', fkip),
    ('FT/', ft),
    ('PASCASARJANA/', pascasarjana),
    ('profil/', profil),
    ('', views.index),
]