import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from dataclasses import asdict

from core.models import Position, Employer


def index(request):
    return render(request, template_name="core/index.html")


def new_employer(request):
    return render(request, template_name="core/new_employer.html")


def new_position(request):
    return render(request, template_name="core/new_position.html")


def update_employer(request):
    return render(request, template_name="core/employer_update.html")


def update_position(request):
    return render(request, template_name="core/position_update.html")


class PositionListCreateView(View):
    def get(self, request, *args, **kwargs):
        positions = Position.objects_pos.all()
        json_data = {"data": []}
        for position in positions:
            json_data["data"].append(asdict(position))

        return JsonResponse(json_data)

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        new_position = Position.objects_pos.create(**data)
        json_data = {"data": asdict(new_position)}

        return JsonResponse(json_data)


class PositionRetrieveUpdateDeleteView(View):
    def get(self, request, *args, **kwargs):
        id_position = kwargs['id']
        position = Position.objects_pos.get_by_pk(id_position)
        json_data = {"data": asdict(position)}

        return JsonResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id_position = kwargs['id']
        data = json.loads(self.request.body)
        position = Position.objects_pos.update(pk=id_position, **data)
        json_data = {"data": asdict(position)}

        return JsonResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id_position = kwargs['id']
        Position.objects_pos.delete(id_position)

        return JsonResponse({"status": "ok"})


class EmployerListCreateView(View):
    def get(self, request, *args, **kwargs):
        employers = Employer.objects_emp.all()
        json_data = {"data": []}
        for employer in employers:
            json_data["data"].append(asdict(employer))

        return JsonResponse(json_data)

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        new_position = Employer.objects_emp.create(**data)
        json_data = {"data": asdict(new_position)}

        return JsonResponse(json_data)


class EmployerRetrieveUpdateDeleteView(View):
    def get(self, request, *args, **kwargs):
        id_employer = kwargs['id']
        employer = Employer.objects_emp.get_by_pk(id_employer)
        json_data = {"data": asdict(employer)}

        return JsonResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id_employer = kwargs['id']
        data = json.loads(self.request.body)
        employer = Employer.objects_emp.update(pk=id_employer, **data)
        json_data = {"data": asdict(employer)}

        return JsonResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id_position = kwargs['id']
        Employer.objects_emp.delete(id_position)

        return JsonResponse({"status": "ok"})
