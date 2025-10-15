// CIBA_Sandbox_SDK_for_Node.js.test.js
import { jest } from '@jest/globals';
import sandboxSdk from '@telefonica/opengateway-sandbox-sdk';
import fs from 'fs';
import path from 'path';

const { DeviceLocation, Simswap, DeviceStatus, NumberVerification, QualityOnDemand, DeviceSwap, KnowYourCustomer, AgeVerification, Tenure } = sandboxSdk;

jest.mock('@telefonica/opengateway-sandbox-sdk', () => ({
    DeviceLocation: jest.fn(),
    Simswap: jest.fn(),
    DeviceStatus: jest.fn(),
    NumberVerification: jest.fn(),
    QualityOnDemand: jest.fn(),
    DeviceSwap: jest.fn(),
    KnowYourCustomer: jest.fn(),
    AgeVerification: jest.fn(),
    Tenure: jest.fn()
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

describe('DeviceStatus Client', () => {
    let getConnectivityMock;

    beforeEach(() => {
        jest.clearAllMocks();
        getConnectivityMock = jest.fn().mockReturnValue({ status: 'CONNECTED_DATA' });
        DeviceStatus.mockImplementation(() => ({
            getConnectivity: getConnectivityMock
        }));
    });

    test('should call DeviceStatus and getConnectivity with correct parameters', () => {
        console.log = jest.fn();

        const deviceStatus = new DeviceStatus(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        const result = deviceStatus.getConnectivity();

        expect(DeviceStatus).toHaveBeenCalledWith(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        expect(getConnectivityMock).toHaveBeenCalled();
        expect(result.status).toBe('CONNECTED_DATA');
    });
});

describe('NumberVerification Client', () => {
    let verifyNumberMock;

    beforeEach(() => {
        jest.clearAllMocks();
        verifyNumberMock = jest.fn().mockReturnValue(true);
        NumberVerification.mockImplementation(() => ({
            verifyNumber: verifyNumberMock
        }));
    });

    test('should call NumberVerification and verifyNumber with correct parameters', () => {
        console.log = jest.fn();

        const numberVerification = new NumberVerification(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        const result = numberVerification.verifyNumber();

        expect(NumberVerification).toHaveBeenCalledWith(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        expect(verifyNumberMock).toHaveBeenCalled();
        expect(result).toBe(true);
    });
});

describe('QualityOnDemand Client', () => {
    let createSessionMock;

    beforeEach(() => {
        jest.clearAllMocks();
        createSessionMock = jest.fn().mockReturnValue({ sessionId: '12345', status: 'AVAILABLE' });
        QualityOnDemand.mockImplementation(() => ({
            createSession: createSessionMock
        }));
    });

    test('should call QualityOnDemand and createSession with correct parameters', () => {
        console.log = jest.fn();

        const qod = new QualityOnDemand(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        const result = qod.createSession();

        expect(QualityOnDemand).toHaveBeenCalledWith(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        expect(createSessionMock).toHaveBeenCalled();
        expect(result.sessionId).toBe('12345');
        expect(result.status).toBe('AVAILABLE');
    });
});

describe('DeviceSwap Client', () => {
    let checkSwapMock;

    beforeEach(() => {
        jest.clearAllMocks();
        checkSwapMock = jest.fn().mockReturnValue({ swapped: true, lastSwapDate: '2023-12-25' });
        DeviceSwap.mockImplementation(() => ({
            checkSwap: checkSwapMock
        }));
    });

    test('should call DeviceSwap and checkSwap with correct parameters', () => {
        console.log = jest.fn();

        const deviceSwap = new DeviceSwap(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        const result = deviceSwap.checkSwap();

        expect(DeviceSwap).toHaveBeenCalledWith(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        expect(checkSwapMock).toHaveBeenCalled();
        expect(result.swapped).toBe(true);
        expect(result.lastSwapDate).toBe('2023-12-25');
    });
});

describe('KnowYourCustomer Client', () => {
    let matchMock;

    beforeEach(() => {
        jest.clearAllMocks();
        matchMock = jest.fn().mockReturnValue({ match: true });
        KnowYourCustomer.mockImplementation(() => ({
            match: matchMock
        }));
    });

    test('should call KnowYourCustomer and match with correct parameters', () => {
        console.log = jest.fn();

        const kyc = new KnowYourCustomer(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        const result = kyc.match();

        expect(KnowYourCustomer).toHaveBeenCalledWith(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        expect(matchMock).toHaveBeenCalled();
        expect(result.match).toBe(true);
    });
});

describe('AgeVerification Client', () => {
    let verifyAgeMock;

    beforeEach(() => {
        jest.clearAllMocks();
        verifyAgeMock = jest.fn().mockReturnValue({ verificationResult: true });
        AgeVerification.mockImplementation(() => ({
            verifyAge: verifyAgeMock
        }));
    });

    test('should call AgeVerification and verifyAge with correct parameters', () => {
        console.log = jest.fn();

        const ageVerification = new AgeVerification(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        const result = ageVerification.verifyAge();

        expect(AgeVerification).toHaveBeenCalledWith(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        expect(verifyAgeMock).toHaveBeenCalled();
        expect(result.verificationResult).toBe(true);
    });
});

describe('Tenure Client', () => {
    let getTenureMock;

    beforeEach(() => {
        jest.clearAllMocks();
        getTenureMock = jest.fn().mockReturnValue({ tenure: 24 });
        Tenure.mockImplementation(() => ({
            getTenure: getTenureMock
        }));
    });

    test('should call Tenure and getTenure with correct parameters', () => {
        console.log = jest.fn();

        const tenure = new Tenure(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        const result = tenure.getTenure();

        expect(Tenure).toHaveBeenCalledWith(credentials, undefined, CUSTOMER_PHONE_NUMBER);
        expect(getTenureMock).toHaveBeenCalled();
        expect(result.tenure).toBe(24);
    });
});
