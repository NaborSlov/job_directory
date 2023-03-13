from django.conf.urls import url

from core.views import PositionListCreateView, EmployerListCreateView, PositionRetrieveUpdateDeleteView, \
    EmployerRetrieveUpdateDeleteView

urlpatterns = [
    url(r"^positions", PositionListCreateView.as_view()),
    url(r"^employers", EmployerListCreateView.as_view()),
    url(r"^employer/(?P<id>[0-9]+)", EmployerRetrieveUpdateDeleteView.as_view(), name="get_one_employer"),
    url(r"^position/(?P<id>[0-9]+)", PositionRetrieveUpdateDeleteView.as_view(), name="get_one_position"),
]
