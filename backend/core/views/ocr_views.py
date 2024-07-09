from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from paddleocr import PaddleOCR
import cv2
import numpy as np
import re

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def correct_orientation(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use OpenCV to detect edges in the image
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # Use HoughLines to detect lines in the image
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    
    if lines is not None:
        # Calculate the angle of the detected lines
        angles = []
        for line in lines:
            rho, theta = line[0]
            angle = np.degrees(theta)
            if angle > 45:
                angle = angle - 90
            angles.append(angle)
        
        # Calculate the median angle
        median_angle = np.median(angles)
        
        # Rotate the image to correct orientation
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, median_angle, 1.0)
        corrected_image = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return corrected_image
    
    # Return the original image if no lines were detected
    return image

@method_decorator(csrf_exempt, name='dispatch')
class OCRView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('image')
        if not file:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

        image = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        # Correct the orientation of the image
        corrected_image = correct_orientation(image)

        result = ocr.ocr(corrected_image)
        text = ''
        for line in result:
            text += ' '.join([word_info[1][0] for word_info in line]) + ' '
        
        # Parse the text to extract the first name, last name, and student number
        first_name = ''
        last_name = ''
        student_number = ''
        
        # Regular expression to match a student number (assumed to be a sequence of digits)
        student_number_match = re.search(r'\b\d{8}\b', text)
        if student_number_match:
            student_number = student_number_match.group(0)
        
        # Extract name information
        # Assuming the name is formatted as "first_name last_name" before the student number
        name_match = re.search(r'STUDENT\s+([A-Za-z- ]+)\s+(\b[A-Z]+\b)\s+' + student_number, text)
        if name_match:
            first_name = name_match.group(1).strip()
            last_name = name_match.group(2).strip()
        
        return Response({
            'firstName': first_name,
            'lastName': last_name,
            'studentNumber': student_number
        })
