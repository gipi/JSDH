from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render_to_response

import random

def index(request):
    """Homepage"""

    private_key, A = start_dh()

    # the session_key is used as key to retrieve the secret exponent
    session_key = random.getrandbits(256)
    cache.set(session_key, private_key)

    print "session_key = %s\nprivate_key = %s\nA = %s" % (session_key, private_key, A)

    return render_to_response(
        'index.html', {
            'p': settings.P,
            'g': settings.G,
            'A': A,
            'session_key': session_key,
    })

def start_dh():
    """Generate the parameters needed to start a DH session.

    Returns the private key and the A parameter to send to other user"""
    private_key = random.getrandbits(256)
    A = pow(settings.G, private_key, settings.P)

    return private_key, A

def finish_dh(private_key, B):
    """Calculate the session key generated at the end of the DH exchange"""
    K = pow(B, private_key, settings.P)

    return K

def finish(request):
    """Get B and compute K"""
    B = long(request.POST['B'])
    ciphertext = request.POST['password']
    session_key = request.POST['session_key']
    private_key = cache.get(session_key)

    K = finish_dh(private_key, B)

    print "password = %s\nsession_key = %s\nprivate_key = %s\nB = %s\nK = %s" % (ciphertext, session_key, private_key, B, K)

    return render_to_response(
        'finished.html', {
            'K': K,
            'ciphertext': ciphertext,
    })
