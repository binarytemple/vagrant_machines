

from bitbucket.bitbucket import Bitbucket
bb = Bitbucket(username='binarytemple', password='', repo_name_or_slug='village-timetable-parser')
bb.authorize("f7XTPKEw475LnbrvJ7", "GaFcjNsedMbKnPE4Ye3X6svGR7XfcUbV","http://localhost")
import webbrowser
webbrowser.open(bb.url('AUTHENTICATE', token=bb.access_token))

oauth_verifier = raw_input('Enter verifier from url [oauth_verifier] i.e 7889090090')

r = bb.verify(oauth_verifier)
(res,keys) = bb.ssh.all()
len(keys)
#keys[0]['label']
#keys[0]['pk']
#bb.ssh.delete(84026)

(res,keys) = bb.ssh.all()
keys
