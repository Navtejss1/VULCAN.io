#!/usr/bin/env python3
import cgi
import requests

# Print required headers for CGI
print("Content-Type: text/html")
print()

# Retrieve the URL from the form input
form = cgi.FieldStorage()
domain = form.getvalue("url")

# Function to check headers and return results
def check_security_headers(domain):
    response = requests.get(domain)
    headers = response.headers
    
    result = f"<h2>Results for {domain}</h2><ul>"
    
    header_checks = {
        "Strict-Transport-Security": "Strict-Transport-Security",
        "X-Content-Type-Options": "X-Content-Type-Options",
        "Content-Security-Policy": "Content-Security-Policy",
        "X-Frame-Options": "X-Frame-Options",
        "Referrer-Policy": "Referrer-Policy",
        "Permissions-Policy": "Permissions-Policy"
    }
    
    for header, description in header_checks.items():
        if header in headers:
            result += f"<li>{description}: <strong>Not Vulnerable</strong></li>"
        else:
            result += f"<li>{description}: <strong>Vulnerable</strong></li>"
    
    result += "</ul>"
    return result

# Output the results
print(check_security_headers(domain))
