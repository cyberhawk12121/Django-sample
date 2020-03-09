from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsOwnerOrReadOnly(BasePermission):
    message= "You aren't the owner"
    my_safe_method= ['PUT']
    
    def has_object_permission(self, request, view, object):
        # if request.method in self.my_safe_method:
        # if request.method in SAFE_METHODS:
        #   return True
        return object.email == request.user