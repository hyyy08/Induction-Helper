from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers import DatabaseUserSerializer, InductionSerializer
from core.models import DatabaseUser, Induction
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import csv



class export_user_pdf(APIView):
    def get(self, request):
        data_users = DatabaseUser.objects.all()
        serializer = DatabaseUserSerializer(data_users, many=True)
        template_path = 'export_file.html'
        context = {'dataUsers': serializer.data} 
        template = get_template(template_path)
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="dataUser_report.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

class export_user_csv(APIView):
    def get(self, request):
        data_users = DatabaseUser.objects.all()
        serializer = DatabaseUserSerializer(data_users, many=True)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="dataUser_report.csv"'
        writer = csv.writer(response)
        writer.writerow(['UserId', 'Email', 'FirstName', 'Lastname'])
        for data_user in serializer.data:
            writer.writerow([data_user['userID'], data_user['email'], data_user['firstName'], data_user['lastName']])
        return response



class export_induction_to_pdf(APIView):
    def get(self, request):
        data_users = DatabaseUser.objects.all()
        serializer = DatabaseUserSerializer(data_users, many=True)

        template_path = 'export_file.html'
        context = {'dataUsers': serializer.data}

        template = get_template(template_path)
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="dataUser_report.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response

class export_induction_to_csv(APIView):
    def get(self, request):
        data_users = DatabaseUser.objects.all()
        serializer = DatabaseUserSerializer(data_users, many=True)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="dataUser_report.csv"'

        writer = csv.writer(response)
        writer.writerow(['UserId', 'Email', 'FirstName', 'Lastname'])

        for data_user in serializer.data:
            writer.writerow([data_user['userID'], data_user['email'], data_user['firstName'], data_user['lastName']])

        return response

class export_induction_to_pdf_byID(APIView):
    def get(self, request, user_id=None):
        if user_id is not None:
            user = get_object_or_404(DatabaseUser, userID=user_id)
            inductions = Induction.objects.filter(userID=user).order_by('userID__firstName')
        else:
            inductions = Induction.objects.all().order_by('userID__firstName')

        serializer = InductionSerializer(inductions, many=True)

        template_path = 'export_induction_to_pdf.html'
        context = {'inductions': serializer.data}

        template = get_template(template_path)
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        if user_id is not None:
            response['Content-Disposition'] = f'attachment; filename="{user.firstName}_{user.lastName}_induction_report.pdf"'
        else:
            response['Content-Disposition'] = 'attachment; filename="all_users_induction_report.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response


