from pymisp import PyMISP

# The URL of the MISP instance to connect to
misp_url = 'http://127.0.0.1:80'
# Can be found in the MISP web interface under ||
# http://+MISP_URL+/users/view/me -> Authkey
misp_key = '<misp_key>'
# Should PyMISP verify the MISP certificate
misp_verifycert = False

misp = PyMISP(misp_url, misp_key, misp_verifycert, debug=False)
r = misp.search(published=False, metadata=True)
print(r)
