import requests
import json
from robot.api.deco import keyword


class APIKeywords:
    p = requests.session()

    @keyword('Call to Account Management')
    def call_uam_login(self):
        response = self.p.get("https://clarity.dexcom.com/users/auth/dexcom_sts")

        Clarity_call_to_UAM = response.history[1].url  # This gives us the authorize call endpoint
        redirect_response = self.p.get(Clarity_call_to_UAM)
        signURL_2 = redirect_response.url
        idsrv_xsrf_2 = redirect_response.content[4019:4126].decode()

        return signURL_2, idsrv_xsrf_2

    @keyword('Callback Post')
    def callback_post(self, signURL_2, idsrv_xsrf_2):
        data = {
            'username': 'codechallenge',
            'password': 'Password123',
            'idsrv.xsrf': idsrv_xsrf_2
        }

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        z = self.p.post(signURL_2, data=data, headers=headers)

        callBack = str(z.history[2].url)
        start = callBack.find("code=") + 5
        end = callBack.find("&")
        authCode = callBack[
                   start:end]  # I got Auth code but there is no Client Secret, so not using this code to exchange Access Token.
        return callBack

    @keyword('CAll to get Access Token')
    def get_access_token(self, callBack):
        # I saw access token inside the html response when i make GET call to calback url, so I am using this to make fetch AT
        q = self.p.get(str(callBack))
        token_start = q.text.find("window.ACCESS_TOKEN = ") + 23
        token_end = q.text.find("window.PRODUCT_STORE_HOST") - 9
        access_token = q.text[token_start:token_end]

        return access_token

    @keyword('Analysis Session Post')
    def analysis_session_post(self, access_token):
        headers = {'Content-Type': 'application/json; charset=utf-8',
                   'Access-Token': access_token}
        subjectID = 1681277794575765504
        analysisSessionId = self.p.post(f"https://clarity.dexcom.com/api/subject/{subjectID}/analysis_session",
                                        headers=headers)
        c = analysisSessionId.text
        d = json.loads(c)
        return d['analysisSessionId']

    @keyword('Assert Session Id')
    def assert_session_id(self, session_id):
        assert session_id is not None
