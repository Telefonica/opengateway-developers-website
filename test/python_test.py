import unittest
from unittest.mock import patch, MagicMock, ANY
import importlib
import sys
import os

# Añadir el directorio actual al path para importar mocks
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TestCibaSandbox(unittest.TestCase):
    def __init__(self, methodName='runTest', module_path=None):
        super(TestCibaSandbox, self).__init__(methodName)
        self.module_path = module_path

    @patch('mock_aggregator_sdk.Simswap')
    def test_simswap(self, MockSimswap):
        mock_simswap_client = MockSimswap.return_value
        mock_simswap_client.retrieve_date.return_value = MagicMock(strftime=lambda x: "December 23, 2024, 09:49:42 AM")

        # Importar el script después de aplicar los mocks
        module = importlib.import_module(self.module_path + 'CIBA_Sandbox_SDK_for_Python')

        # Verificar que los métodos fueron llamados correctamente
        MockSimswap.assert_called_once_with(
            'your_client_id',
            'your_client_secret',
            '+34555555555'
        )
        mock_simswap_client.retrieve_date.assert_called_once()

        # Verificar la salida del script
        with patch('builtins.print') as mocked_print:
            importlib.reload(module)
            mocked_print.assert_called_once_with("SIM was swapped: December 23, 2024, 09:49:42 AM")

    @patch('mock_aggregator_sdk.DeviceLocation')
    @patch('mock_aggregator_sdk.ClientCredentials')
    def test_devicelocation(self, MockClientCredentials, MockDeviceLocation):
        mock_credentials = MockClientCredentials.return_value
        mock_devicelocation_client = MockDeviceLocation.return_value
        mock_devicelocation_client.verify.return_value = True

        module =importlib.import_module(self.module_path + 'CIBA_Sandbox_SDK_for_Python')

        # Verificar que los métodos fueron llamados correctamente
        MockClientCredentials.assert_called_once_with(
            client_id = 'your_client_id',
            client_secret = 'your_client_secret'
        )
        MockDeviceLocation.assert_called_once_with(
            credentials=mock_credentials,
            phone_number="+34666666666"
        )
        mock_devicelocation_client.verify.assert_called_once_with(40.5150, -3.6640, 10, "+34666666666")

        # Verificar la salida del script
        with patch('builtins.print') as mocked_print:
            importlib.reload(module)
            mocked_print.assert_called_once_with("Is the device in location? True")

    @patch('mock_aggregator_sdk.AgeVerifier')
    @patch('mock_aggregator_sdk.ClientCredentials')
    def test_ageverification(self, MockClientCredentials, MockAgeVerifier):
        mock_credentials = MockClientCredentials.return_value
        mock_age_client = MockAgeVerifier.return_value
        mock_result = MagicMock()
        mock_result.ageCheck = True
        mock_result.verifiedStatus = True
        mock_result.identityMatchScore = 0.95
        mock_result.contentLock = False
        mock_result.parentalControl = False
        mock_age_client.verify_age.return_value = mock_result

        module = importlib.import_module(self.module_path + '_Sample_SDK_for_Python')

        # Verificar que los métodos fueron llamados correctamente
        MockClientCredentials.assert_called_once_with(
            client_id='my-app-id',
            client_secret='my-app-secret'
        )
        MockAgeVerifier.assert_called_once_with(
            credentials=mock_credentials,
            phone_number='+34629255833'
        )
        mock_age_client.verify_age.assert_called_once()

        # Verificar las salidas del script
        with patch('builtins.print') as mocked_print:
            importlib.reload(module)
            expected_calls = [
                ('Age check passed?', True),
                ('Verified ID?', True),
                ('Match score:', 0.95),
                ('Content lock:', False),
                ('Parental control:', False)
            ]
            actual_calls = mocked_print.call_args_list
            self.assertEqual(len(actual_calls), 5)

    @patch('mock_aggregator_sdk.TenureVerifier')
    @patch('mock_aggregator_sdk.ClientCredentials')
    def test_tenure(self, MockClientCredentials, MockTenureVerifier):
        mock_credentials = MockClientCredentials.return_value
        mock_tenure_client = MockTenureVerifier.return_value
        mock_result = MagicMock()
        mock_result.tenureDateCheck = True
        mock_result.contractType = "postpaid"
        mock_tenure_client.check_tenure.return_value = mock_result

        module = importlib.import_module(self.module_path + '_Sample_SDK_for_Python')

        # Verificar que los métodos fueron llamados correctamente
        MockClientCredentials.assert_called_once_with(
            client_id='my-app-id',
            client_secret='my-app-secret'
        )
        MockTenureVerifier.assert_called_once_with(
            credentials=mock_credentials,
            phone_number='+34629255833'
        )
        mock_tenure_client.check_tenure.assert_called_once()

        # Verificar las salidas del script
        with patch('builtins.print') as mocked_print:
            importlib.reload(module)
            calls = mocked_print.call_args_list
            self.assertGreaterEqual(len(calls), 1)  # Al menos el primer print

    @patch('mock_aggregator_sdk.DeviceStatus')
    @patch('mock_aggregator_sdk.ClientCredentials')
    def test_devicestatus(self, MockClientCredentials, MockDeviceStatus):
        mock_credentials = MockClientCredentials.return_value
        mock_devicestatus_client = MockDeviceStatus.return_value
        mock_devicestatus_client.roaming.return_value = False

        module = importlib.import_module(self.module_path + 'CIBA_Sample_SDK_for_Python')

        # Verificar que los métodos fueron llamados correctamente
        MockClientCredentials.assert_called_once_with(
            client_id='your_client_id',
            client_secret='your_client_secret'
        )
        MockDeviceStatus.assert_called_once_with(
            credentials=mock_credentials,
            phone_number="+34777777777"
        )
        mock_devicestatus_client.roaming.assert_called_once_with("+34777777777")

        # Verificar la salida del script
        with patch('builtins.print') as mocked_print:
            importlib.reload(module)
            mocked_print.assert_called_once_with("Is device in roaming status? False")

    @patch('mock_aggregator_sdk.DeviceSwap')
    @patch('mock_aggregator_sdk.ClientCredentials')
    def test_deviceswap(self, MockClientCredentials, MockDeviceSwap):
        mock_credentials = MockClientCredentials.return_value
        mock_deviceswap_client = MockDeviceSwap.return_value
        mock_deviceswap_client.retrieve_date.return_value = MagicMock(strftime=lambda x: "January 15, 2024, 10:30:00 AM")

        module = importlib.import_module(self.module_path + 'CIBA_Sample_SDK_for_Python')

        # Verificar que los métodos fueron llamados correctamente
        MockClientCredentials.assert_called_once_with(
            client_id='your_client_id',
            client_secret='your_client_secret'
        )
        MockDeviceSwap.assert_called_once_with(
            credentials=mock_credentials,
            phone_number="+34333333333"
        )
        mock_deviceswap_client.retrieve_date.assert_called_once()

        # Verificar la salida del script
        with patch('builtins.print') as mocked_print:
            importlib.reload(module)
            mocked_print.assert_called_once_with("Device was swapped: January 15, 2024, 10:30:00 AM")

    @patch('mock_aggregator_sdk.KYCMatch')
    @patch('mock_aggregator_sdk.ClientCredentials')
    def test_knowyourcustomer(self, MockClientCredentials, MockKYCMatch):
        mock_credentials = MockClientCredentials.return_value
        mock_kyc_client = MockKYCMatch.return_value
        mock_result = MagicMock()
        mock_result.match = True
        mock_result.score = 0.95
        mock_kyc_client.match.return_value = mock_result

        module = importlib.import_module(self.module_path + 'CIBA_Sample_SDK_for_Python')

        # Verificar que los métodos fueron llamados correctamente
        MockClientCredentials.assert_called_once_with(
            client_id='your_client_id',
            client_secret='your_client_secret'
        )
        MockKYCMatch.assert_called_once_with(
            credentials=mock_credentials,
            phone_number="+34666666666"
        )

    @patch('mock_aggregator_sdk.NumberVerification')
    @patch('mock_aggregator_sdk.ClientCredentials')
    def test_numberverification(self, MockClientCredentials, MockNumberVerification):
        mock_credentials = MockClientCredentials.return_value
        mock_nv_client = MockNumberVerification.return_value
        mock_result = MagicMock()
        mock_result.devicePhoneNumberVerified = True
        mock_nv_client.verify.return_value = mock_result

        module = importlib.import_module(self.module_path + 'Auth_code_Sample_SDK_for_Python_simple')

        # Verificar que los métodos fueron llamados correctamente
        MockClientCredentials.assert_called_once_with(
            clientid='my-app-id',
            clientsecret='my-app-secret'
        )
        MockNumberVerification.assert_called_once_with(mock_credentials, '+34666666666')
        mock_nv_client.verify.assert_called_once_with('+34666666666')

        # Verificar la salida del script
        with patch('builtins.print') as mocked_print:
            importlib.reload(module)
            mocked_print.assert_called_once_with("Phone number verified")

    @patch('mock_aggregator_sdk.QoDMobile')
    @patch('mock_aggregator_sdk.ClientCredentials')
    def test_qod(self, MockClientCredentials, MockQoDMobile):
        mock_credentials = MockClientCredentials.return_value
        mock_qod_client = MockQoDMobile.return_value
        
        module = importlib.import_module(self.module_path + 'CIBA_Sample_SDK_for_Python')

        # Verificar que los métodos fueron llamados correctamente
        MockClientCredentials.assert_called_once_with(
            clientid='my-app-id',
            clientsecret='my-app-secret'
        )
        MockQoDMobile.assert_called_once()

if __name__ == '__main__':
    base_dir = sys.argv[1] if len(sys.argv) > 1 else 'tmp/py'

    if not os.path.exists(base_dir):
        print(f"Error: La ruta especificada '{base_dir}' no existe.")
        sys.exit(1)

    suite = unittest.TestSuite()

    # Lista de APIs con tests implementados
    implemented_tests = {
        'devicelocation': 'CIBA_Sandbox_SDK_for_Python',
        'simswap': 'CIBA_Sandbox_SDK_for_Python', 
        'ageverification': '_Sample_SDK_for_Python',
        'tenure': '_Sample_SDK_for_Python',
        'devicestatus': 'CIBA_Sample_SDK_for_Python',
        'deviceswap': 'CIBA_Sample_SDK_for_Python',
        'knowyourcustomer': 'CIBA_Sample_SDK_for_Python',

        'qod': 'CIBA_Sample_SDK_for_Python',
        'numberverification': 'Auth_code_Sample_SDK_for_Python_simple'
    }
    
    for api in os.listdir(base_dir):
        if api in implemented_tests:
            api_dir = os.path.join(base_dir, api)
            script_name = implemented_tests[api] + '.py'
            script_path = os.path.join(api_dir, script_name)
            
            if os.path.isfile(script_path):
                module_path = base_dir.replace('/', '.') + '.' + api + '.'
                TestCibaSandbox.script_path = script_path
                suite.addTest(TestCibaSandbox('test_' + api, module_path=module_path))

    runner = unittest.TextTestRunner()
    runner.run(suite)
