# views.py
from django.http import JsonResponse
import socket
import psutil

def get_serverIP(request):
    ip_address = None

    # Get all network interfaces (excluding loopback)
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == socket.AF_INET:
                # Exclude loopback addresses
                if not snic.address.startswith('127.') and not snic.address.startswith('192.168.56.') and not snic.address.startswith('192.168.10.') and not snic.address.startswith('192.168.67.'):
                    ip_address = snic.address
                    break
        if ip_address:
            break

    if not ip_address:
        # Fallback to localhost if no suitable IP address is found
        ip_address = '127.0.0.1'

    return JsonResponse({'ip': ip_address})