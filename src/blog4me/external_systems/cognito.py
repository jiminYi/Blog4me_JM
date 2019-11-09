import logging

import boto3

logger = logging.getLogger('pycogn.Cognito')


class Cognito:
    def __init__(self, region, user_pool_id, app_client_id, identity_pool_id):
        self.idp_client = boto3.client('cognito-idp')
        self.identity_client = boto3.client('cognito-identity')
        self.region = region
        self.user_pool_id = user_pool_id
        self.app_client_id = app_client_id
        self.identity_pool_id = identity_pool_id

    def get_identity_id(self, username, password):
        try:
            token = self._get_token(username, password)
            provider = 'cognito-idp.%s.amazonaws.com/%s' % (self.region, self.user_pool_id)
            response = self.identity_client.get_id(IdentityPoolId=self.identity_pool_id,Logins={provider: token})
            logger.info(response)
            identity_id = response['IdentityId']
        except self.idp_client.exceptions.NotAuthorizedException as e:
            logger.error("error: {}".format(e))
            identity_id = None
        return identity_id

    def _get_token(self, username, password):
        response = self.idp_client.admin_initiate_auth(UserPoolId=self.user_pool_id,
                                                       ClientId=self.app_client_id,
                                                       AuthFlow='ADMIN_NO_SRP_AUTH',
                                                       AuthParameters={'USERNAME': username, 'PASSWORD': password})
        logger.info(response)
        token = response['AuthenticationResult']['IdToken']
        return token
