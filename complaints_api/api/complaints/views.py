from api.models import Comment, Complaints
from .serializer import CommentSerializer, ComplaintsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password

class ComplaintsUserView(APIView):

    def get(self, request, folio=None):
        password = request.query_params.get('password', None)
        if folio and password:
            try:
                complaint = Complaints.objects.prefetch_related('comments').get(folio = folio)
                if check_password(password, complaint.password):
                    serializer = ComplaintsSerializer(complaint)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({'error':'Contraseña incorrecta'},)
            except Complaints.DoesNotExist:
                return Response({'error': 'Queja no encontrada'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'El folio y la contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        serializer = ComplaintsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ComplaintsAdminView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                complaint = Complaints.objects.prefetch_related('comments').get(pk = pk)
                serializer = ComplaintsSerializer(complaint)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Complaints.DoesNotExist:
                return Response({'error': 'Queja no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        else:
            complaints = Complaints.objects.prefetch_related('comments').all()
            serializer = ComplaintsSerializer(complaints, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        try:
            place = Complaints.objects.get(pk=pk)
            place.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Complaints.DoesNotExist:
            return Response({"error": "Queja no encontrada"}, status=status.HTTP_404_NOT_FOUND)


class CommentsComplaintsView(APIView):

    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({"error": "Comentario no encontrado"}, status=status.HTTP_404_NOT_FOUND)