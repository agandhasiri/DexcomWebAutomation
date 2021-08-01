
import requests

p = requests.session()
response = p.get("https://clarity.dexcom.com/users/auth/dexcom_sts")

idsrv_xsrf_1 = response.cookies.get('idsrv.xsrf')
signURL_1= response.url
print('idsrv from dexcom_sts call:', idsrv_xsrf_1)
print('UAM sign in call:', signURL_1)
print('-----------------')
# I tried above Sign In and idsrv token for login, but failed and observed that there is another sign in and idsrv from next call

Clarity_call_to_UAM = response.history[1].url
redirect_response = p.get(Clarity_call_to_UAM)
signURL_2 = redirect_response.url
print('Clarity call to UAM is:', Clarity_call_to_UAM)
print('-----------------')
print('UAM Sign In URL is:', signURL_2)
print('-----------------')
idsrv_xsrf_2 = redirect_response.content[4019:4126]
print('UAM idsrv token is:', idsrv_xsrf_2.decode())


#Preparing data for login
data = {
    'username': 'codechallenge',
    'password': 'Password123',
    'idsrv.xsrf': idsrv_xsrf_2.decode()
}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
z = p.post(signURL_2, data=data, headers=headers)

callBack = str(z.history[2].url)
start = callBack.find("code=") + 5
end = callBack.find("&")
authCode = callBack[start:end]
print('-----------------')
print('Auth Code is:', authCode)



