import requests

domain = "https://www.linkedin.com/"

response = requests.get(domain)

headers = response.headers


if "Strict-Transport-Security" in headers:
    print(domain + " is not vulnerable to (Strict-Transport-Security)")
else:
    print(domain + " is vulnerable to (Strict-Transport-Security)")

if "X-Content-Type-Options" in headers:
    print(domain + " is not vulnerable to (X-Content-Type-Options)")
else:
    print(domain + " is vulnerable to (X-Content-Type-Options)")

if "Content-Security-Policy" in headers:
    print(domain + " is not vulnerable to (Content-Security-Policy)")
else:
    print(domain + " is vulnerable to (Content-Security-Policy)")

if "X-Frame-Options" in headers:
    print(domain + " is not vulnerable to (X-Frame-Options)")
else:
    print(domain + " is vulnerable to (X-Frame-Options)")

if "Referrer-Policy" in headers:
    print(domain + " is not vulnerable to (Referrer-Policy)")
else:
    print(domain + " is vulnerable to (Referrer-Policy)")

if "Permissions-Policy" in headers:
    print(domain + " is not vulnerable to (Permissions-Policy)")
else:
    print(domain + " is vulnerable to (Permissions-Policy)")
