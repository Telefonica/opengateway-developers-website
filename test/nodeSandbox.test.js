// CIBA_Sandbox_SDK_for_Node.js.test.js
import { jest } from '@jest/globals';
import sandboxSdk from '@telefonica/opengateway-sandbox-sdk';
import fs from 'fs';
import path from 'path';

const { DeviceLocation, Simswap } = sandboxSdk;

jest.mock('@telefonica/opengateway-sandbox-sdk', () => ({
    DeviceLocation: jest.fn(),
    Simswap: jest.fn()
}));

const credentials = {
    clientId: 'your_client_id',
    clientSecret: 'your_client_secret'
};
const CUSTOMER_PHONE_NUMBER = '+34666666666';

describe('DeviceLocation Client', () => {
    let verifyMock;

    beforeEach(() => {
        jest.clearAllMocks();
        verifyMock = jest.fn().mockReturnValue(true);
        DeviceLocation.mockImplementation(() => ({
            verify: verifyMock
        }));
    });

    test('should call DeviceLocation and verify with correct parameters, and log correct output', () => {
        console.log = jest.fn();

        require('./tmp/js/devicelocation/CIBA_Sandbox_SDK_for_Node.js');

        expect(DeviceLocation).toHaveBeenCalledWith(credentials, undefined, CUSTOMER_PHONE_NUMBER);

        const latitude = 40.5150;
        const longitude = -3.6640;
        const radius = 10;
        expect(verifyMock).toHaveBeenCalledWith(latitude, longitude, radius);

        expect(console.log).toHaveBeenCalledWith('Is the device in location? true');

        // Imprime el valor de console.log para verlo en la salida de la consola
        console.log.mock.calls.forEach(call => console.log(...call));
    });
});

describe('Simswap Client', () => {
    let retrieveDateMock;

    beforeEach(() => {
        jest.clearAllMocks();
        retrieveDateMock = jest.fn().mockReturnValue(new Date('2023-12-25T00:00:00Z'));
        Simswap.mockImplementation(() => ({
            retrieveDate: retrieveDateMock
        }));
    });

    test('should call Simswap and retrieveDate with correct parameters, and log correct output', () => {
        console.log = jest.fn();

        const filePath = path.resolve(__dirname, './tmp/js/simswap/CIBA_Sandbox_SDK_for_Node.js.js');
        let fileContent = fs.readFileSync(filePath, 'utf8');
        fileContent = fileContent.replace(/await\s+/g, '');
        fs.writeFileSync(filePath, fileContent, 'utf8');

        require('./tmp/js/simswap/CIBA_Sandbox_SDK_for_Node.js');

        // Verifica que Simswap se llamó con los parámetros correctos
        expect(Simswap).toHaveBeenCalledWith(credentials.clientId, credentials.clientSecret, CUSTOMER_PHONE_NUMBER);

        // Verifica que retrieveDate se llamó correctamente
        expect(retrieveDateMock).toHaveBeenCalled();

        // Verifica que la salida por consola es correcta
        const expectedDate = new Date('2023-12-25T00:00:00Z').toLocaleString('en-GB', { timeZone: 'UTC' });
        expect(console.log).toHaveBeenCalledWith(`SIM was swapped: ${expectedDate}`);

        // Imprime el valor de console.log para verlo en la salida de la consola
        console.log.mock.calls.forEach(call => console.log(...call));
    });
});
