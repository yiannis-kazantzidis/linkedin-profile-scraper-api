from linkedin_api import Linkedin
# Authenticate using any Linkedin account credentials
api = Linkedin('foyaba9524@inpsur.com', 'Geforze1')

# GET a profile
profile = api.get_profile('alexander-munden-296323280')

# GET a profiles contact info
contact_info = api.get_profile_contact_info('alexander-munden-296323280')

# GET 1st degree connections of a given profile
connections = api.get_profile_connections('1234asc12304')

print(profile)