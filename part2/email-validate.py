from email.utils import parseaddr

def match_email(email_address):
    try:
        parseaddr(email_address)
        return True
    except ValueError:
        return False

# Example usage
email_address = 'example@example.com'
if match_email(email_address):
    print("Valid email address")
else:
    print("Invalid email address")

