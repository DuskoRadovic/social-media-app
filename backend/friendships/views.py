from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from friendships.models import Friendships
from friendships.serializers.default import FriendshipSerializer

User = get_user_model()


class SendFriendRequestView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = FriendshipSerializer

    def post(self, request, *args, **kwargs):
        sender = request.user
        receiver = self.get_object()
        if sender == receiver:
            return JsonResponse({'detail': 'You can not send requests to yourself'})
        friendship = Friendships(request_from=sender, request_for=receiver)
        friendship.save()
        return Response(self.get_serializer(friendship).data)