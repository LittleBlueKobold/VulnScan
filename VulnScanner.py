import requests    #module import

def check_vulnerabilities(url):    #define function
    common_vulnerabilities = ["/admin", "/login", "/wp-admin"]  #define vulnerabilites to look for in url path
    for path in common_vulnerabilities:
        full_url = url + path
        response = requests.get(full_url)
        if response.status_code == 200:     #http response for success
            print(f"Possible vulnerability found: {full_url}")
    else : print("no vulnerabilties found")

check_vulnerabilities("http://example.com")  #website to test