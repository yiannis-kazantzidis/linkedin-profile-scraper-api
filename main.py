from linkedin_api import Linkedin

import re

def extract_linkedin_username(url):
    pattern = r'^https://www\.linkedin\.com/in/([^/]+)/?$'
    
    match = re.match(pattern, url)
    
    if match:
        return match.group(1)
    else:
        return None


# Authenticate using any Linkedin account credentials
api = Linkedin('foyaba9524@inpsur.com', 'Geforze1')

# GET a profile
profile = api.get_profile(extract_linkedin_username("https://www.linkedin.com/in/alexander-munden-296323280/?originalSubdomain=uk"))

print(profile.get('experience', []))