import unittest
from unittest.mock import patch, MagicMock, ANY
import importlib
import sys
import os

class TestCibaSandbox(unittest.TestCase):
    def __init__(self, methodName='runTest', module_path=None):
        super(TestCibaSandbox, self).__init__(methodName)
        self.module_path = module_path
    
    @patch('opengateway_sandbox_sdk.Simswap')
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

    @patch('opengateway_sandbox_sdk.DeviceLocation')
    @patch('opengateway_sandbox_sdk.ClientCredentials')
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
            phone_number=ANY
        )
        mock_devicelocation_client.verify.assert_called_once_with(ANY, ANY, ANY, ANY)

        # Verificar la salida del script
        with patch('builtins.print') as mocked_print:
            importlib.reload(module)
            mocked_print.assert_called_once_with("Is the device in location? True")

if __name__ == '__main__':
    base_dir = sys.argv[1] if len(sys.argv) > 1 else 'tmp/py'

    if not os.path.exists(base_dir):
        print(f"Error: La ruta especificada '{base_dir}' no existe.")
        sys.exit(1)

    suite = unittest.TestSuite()

    for api in os.listdir(base_dir):
        api_dir = os.path.join(base_dir, api)
        script_path = os.path.join(api_dir, 'CIBA_Sandbox_SDK_for_Python.py')
        
        if os.path.isfile(script_path):
            module_path = base_dir.replace('/', '.') + '.' + api + '.'
            TestCibaSandbox.script_path = script_path

            suite.addTest(TestCibaSandbox('test_' + api, module_path=module_path))

    runner = unittest.TextTestRunner()
    runner.run(suite)
