from .mitarbeiter_urls import urlpatterns as mitarbeiter_patterns
from .kunde_urls import urlpatterns as kunden_patterns
from .schadensfall_urls import urlpatterns as schadensfall_patterns
from .versicherungsvertrag_urls import urlpatterns as versicherungsvertrag_patterns
from .api_urls import urlpatterns as api_patterns

patterns = (
    mitarbeiter_patterns
    + kunden_patterns
    + schadensfall_patterns
    + versicherungsvertrag_patterns
    + api_patterns
)
