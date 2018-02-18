from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from rest_framework import permissions

from db.map.models import Action, Submission
from db.users.models import OrganizationUser, OrganizationUserToken
from api.backends import OrganizationUserAuthentication
from api.serializers import PasswordSerializer, PasswordTokenSerializer
from api.serializers import SendSetPasswordEmailSerializer, OrganizationUserTokenSerializer
from api.serializers import ActionDetailSerializer, SubmissionSerializer, OrganizationUpdateSerializer, OrganizationReadSerializer, AccountActionListCreateSerializer


class AccountSendSetPasswordEmail(APIView):
    """View for obtaining an auth token by posting a valid email/password tuple.
    """
    throttle_scope = 'authentication'

    def post(self, request, *args, **kwargs):
        serializer = SendSetPasswordEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = OrganizationUser.objects.filter(email=email).first()
        if user is not None:
            user.send_set_password_email()
        return Response({'email': email})


class AccountSetPasswordWithToken(APIView):
    """Set org user's password, authenticating with token.
    """
    throttle_scope = 'authentication'

    def post(self, request, *args, **kwargs):
        serializer = PasswordTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(OrganizationUser, set_password_token=serializer.validated_data['token'])
        user.set_password(serializer.validated_data['password'])
        user.set_password_token = ''
        user.save()
        return Response({'id': user.pk})


class AccountToken(APIView):
    """View for obtaining an auth token by posting a valid email/password tuple.
    """
    throttle_scope = 'authentication'

    def post(self, request, *args, **kwargs):
        serializer = OrganizationUserTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = OrganizationUserToken.objects.get_or_create(user=user)
        return Response({'token': token.key, 'id': user.pk})


class AccountDeleteToken(APIView):
    """View for obtaining an auth token by posting a valid email/password tuple.
    """
    authentication_classes = (OrganizationUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    throttle_scope = 'authentication'

    def post(self, request, *args, **kwargs):
        try:
            token = self.request.user.auth_token
        except ObjectDoesNotExist:
            return Response({}, status=400)
        else:
            token.delete()
            return Response({})


class AccountSetPassword(APIView):
    """Set org user's password.
    """
    authentication_classes = (OrganizationUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    throttle_scope = 'authentication'

    def post(self, request, *args, **kwargs):
        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['password'])
        request.user.save()
        return Response({'id': request.user.pk})


class AccountOrganizationResetKey(APIView):
    """View for obtaining an auth token by posting a valid email/password tuple.
    """
    authentication_classes = (OrganizationUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        self.request.user.organization.reset_secret_key()
        return Response({'secret_key': self.request.user.organization.secret_key})


class AccountOrganization(generics.GenericAPIView, UpdateModelMixin):
    authentication_classes = (OrganizationUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrganizationUpdateSerializer

    def get_object(self):
        return self.request.user.organization

    def get(self, request, *args, **kwargs):
        return Response(OrganizationReadSerializer(self.get_object()).data)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AccountActionListCreate(generics.ListCreateAPIView):
    authentication_classes = (OrganizationUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountActionListCreateSerializer

    def get_queryset(self):
        return self.get_serializer_class().setup_eager_loading(
            Action.objects.filter(organization=self.request.user.organization)
        )

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)


class AccountActionRetrieveUpdate(generics.RetrieveUpdateAPIView):
    authentication_classes = (OrganizationUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ActionDetailSerializer

    def get_queryset(self):
        queryset = self.get_serializer_class().setup_eager_loading(
            Action.objects.filter(published=True)
        )
        return queryset


class AccountSubmissionUpdate(generics.UpdateAPIView):
    authentication_classes = (OrganizationUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SubmissionSerializer