import os
class Config():
    "To protect from malware and hackers"
    SECRET_KEY = os.environ.get('WP_PASS')
