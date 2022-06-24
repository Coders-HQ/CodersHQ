from djangosaml2idp.processors import BaseProcessor


class GroupProcessor(BaseProcessor):
    """
        Example implementation of access control for users:
        - superusers are allowed
        - staff is allowed
        - they have to belong to a certain group
    """
    group = "ExampleGroup"

#     def has_access(self, request):
#         user = request.user
#         return user.is_superuser or user.is_staff or user.groups.filter(name=self.group).exists()
