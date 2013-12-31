# Taken from this original code .. 

# https://bitbucket-api.readthedocs.org/en/latest/usage.html#private

>>> import webbrowser
>>> from bitbucket.bitbucket import Bitbucket
>>> bb = Bitbucket(USERNAME)
>>> # First time we need to open up a browser to enter the verifier
>>> if not OAUTH_ACCESS_TOKEN and not OAUTH_ACCESS_TOKEN_SECRET:
>>>     bb.authorize(CONSUMER_KEY, CONSUMER_SECRET, 'http://localhost/')
>>>     # open a webbrowser and get the token
>>>     webbrowser.open(bb.url('AUTHENTICATE', token=bb.access_token))
>>>     # Copy the verifier field from the URL in the browser into the console
>>>     oauth_verifier = raw_input('Enter verifier from url [oauth_verifier]')
>>>     OAUTH_ACCESS_TOKEN = bb.access_token
>>>     OAUTH_ACCESS_TOKEN_SECRET = bb.access_token_secret
>>> else:
>>>     bb.authorize(CONSUMER_KEY, CONSUMER_SECRET, 'http://localhost/', OAUTH_ACCESS_TOKEN, OAUTH_ACCESS_TOKEN_SECRET)


from bitbucket.bitbucket import Bitbucket
bb = Bitbucket(username='binarytemple', password='', repo_name_or_slug='village-timetable-parser')
bb.authorize("f7XTPKEw475LnbrvJ7", "GaFcjNsedMbKnPE4Ye3X6svGR7XfcUbV","http://localhost")
import webbrowser
webbrowser.open(bb.url('AUTHENTICATE', token=bb.access_token))

oauth_verifier = raw_input('Enter verifier from url [oauth_verifier] i.e 7889090090')

r = bb.verify(oauth_verifier)


if r[0]:
  print "For future request use these credentials\n"
  print """bb.access_token="%s" \n""" % bb.access_token
  print """bb.access_token_secret="%s" \n""" % bb.access_token_secret
else:
  print """auth failed %s\n""" % r 
