from config import COGNITO
from external_systems.cognito import Cognito
from interfaces.account_manager import Base


class AccountManager(Base):
    def __init__(self):
        self.driver = Cognito(region=COGNITO['REGION'], user_pool_id=COGNITO['USER_POOL_ID'],
                              app_client_id=COGNITO['APP_CLIENT_ID'], identity_pool_id=COGNITO['IDENTITY_POOL_ID'])

    def signin(self, username, password):
        identity_id = self.driver.get_identity_id(username, password)
        return identity_id

    def create_account(self, username):
        pass

    def delete_account(self, username):
        pass
