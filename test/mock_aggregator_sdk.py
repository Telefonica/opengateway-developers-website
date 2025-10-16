"""
Mock implementation of aggregator_opengateway_sdk for testing purposes
"""
from unittest.mock import MagicMock

class ClientCredentials:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

class AgeVerifier:
    def __init__(self, credentials, phone_number=None, **kwargs):
        self.credentials = credentials
        self.phone_number = phone_number
    
    def verify_age(self, data):
        # Mock result
        class MockResult:
            def __init__(self):
                self.ageCheck = True
                self.verifiedStatus = True
                self.identityMatchScore = 0.95
                self.contentLock = False
                self.parentalControl = False
        return MockResult()

class TenureVerifier:
    def __init__(self, credentials, phone_number=None, **kwargs):
        self.credentials = credentials
        self.phone_number = phone_number
    
    def check_tenure(self, data):
        # Mock result
        class MockResult:
            def __init__(self):
                self.tenureDateCheck = True
                self.contractType = "postpaid"
        return MockResult()

class DeviceStatus:
    def __init__(self, credentials, phone_number=None, **kwargs):
        self.credentials = credentials
        self.phone_number = phone_number
    
    def roaming(self, phone_number):
        # Mock result - return boolean indicating roaming status
        return False

class KYCMatch:
    def __init__(self, credentials, phone_number=None, **kwargs):
        self.credentials = credentials
        self.phone_number = phone_number
    
    def match(self, data):
        # Mock result
        class MockResult:
            def __init__(self):
                self.match = True
                self.score = 0.95
        return MockResult()

class DeviceSwap:
    def __init__(self, credentials, phone_number=None, **kwargs):
        self.credentials = credentials
        self.phone_number = phone_number
    
    def retrieve_date(self):
        # Mock result - return date object with strftime method
        return MagicMock(strftime=lambda x: "January 15, 2024, 10:30:00 AM")

class NumberVerification:
    def __init__(self, clientid=None, clientsecret=None, phone_number=None, **kwargs):
        self.clientid = clientid
        self.clientsecret = clientsecret
        self.phone_number = phone_number
    
    def verify(self, phone_number):
        # Mock result
        class MockResult:
            def __init__(self):
                self.devicePhoneNumberVerified = True
        return MockResult()

class QoDMobile:
    def __init__(self, client=None, credentials=None, ip_address=None, **kwargs):
        self.client = client or credentials
        self.ip_address = ip_address
    
    def set_quality(self, duration, qos_profile):
        # Mock result - return session info
        class MockResult:
            def __init__(self):
                self.sessionId = "qod-session-123"
                self.duration = duration
        return MockResult()

class QoSProfiles:
    QOS_E = "QOS_E"
    QOS_S = "QOS_S"
    QOS_M = "QOS_M"
    QOS_L = "QOS_L"

class DeviceLocation:
    def __init__(self, credentials=None, phone_number=None, **kwargs):
        self.credentials = credentials
        self.phone_number = phone_number
    
    def verify(self, latitude, longitude, accuracy, phone_number):
        return True

class Simswap:
    def __init__(self, client_id=None, client_secret=None, phone_number=None, **kwargs):
        self.client_id = client_id
        self.client_secret = client_secret
        self.phone_number = phone_number
    
    def retrieve_date(self):
        return MagicMock(strftime=lambda x: "December 23, 2024, 09:49:42 AM")

# Alias para compatibilidad
SimSwap = DeviceSwap