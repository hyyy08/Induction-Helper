#view file for upload and import CSV file contain users details to the system
import io, csv
from django.db import transaction
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from core.serializers import DatabaseUserSerializer

class CSVUploadViews(APIView):
    def post(self, request, *args, **kwargs):
        csv_file = request.FILES.get('file')
        if not csv_file:
            return Response({"ERROR": "Please upload a CSV file."}, status=status.HTTP_400_BAD_REQUEST)
        
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        try:
            next(io_string)  #skip header row
        except StopIteration:
            # handle empty file
            return Response({"ERROR": "CSV file is empty."}, status=status.HTTP_400_BAD_REQUEST)
        
        reader = csv.reader(io_string, delimiter=',', quotechar='"')
        errors = []
        successful_count = 0
        skipped_count = 0

        # records are processed as one transaction
        with transaction.atomic():
            for row in reader:
                if any(not row[i].strip() for i in [0, 1, 2, 3]):
                    skipped_count += 1
                    continue  
                data = {
                    'userID': row[0],
                    'email': row[1],
                    'firstName': row[2],
                    'lastName': row[3]
                }
                print("DATA to be serialized:", data)

                serializer = DatabaseUserSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    successful_count += 1
                else:
                    errors.append(serializer.errors)
                    skipped_count += 1

            if successful_count > 0 and (errors or skipped_count > 0):
                # Partial success, some records processed successfully but there were some errors or skips
                return Response({
                    "PARTIAL SUCCESS": f"Processed {successful_count} records successfully.",
                    "ERRORS": errors,
                    "SKIPPED": f"{skipped_count} rows fail to import."
                }, status=status.HTTP_207_MULTI_STATUS)

            if successful_count == 0 and errors:
                # All failed no records processed, all had errors
                return Response({
                    "ERRORS": errors,
                    "SKIPPED": f"{skipped_count} rows fail to import"
                }, status=status.HTTP_400_BAD_REQUEST)

            if successful_count > 0 and not errors and skipped_count == 0:
                # All success
                return Response({"SUCCESS": f"All {successful_count} records processed successfully."}, status=status.HTTP_201_CREATED)

            if successful_count == 0 and skipped_count > 0 and not errors:
                # All skipped due to missing data
                return Response({
                    "SKIPPED": f"All {skipped_count} rows fail to import."
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Response for unknown errors
            return Response({"MESSAGE": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)