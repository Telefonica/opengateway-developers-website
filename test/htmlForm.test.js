const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');
const glob = require('glob');

describe('API Request Form', () => {
    let documents = [];
    let api = [];

    const apiValues = {
        devicelocation: {
            scope: 'dpv:FraudPreventionAndDetection#device-location-read',
            redirectUri: 'https://my_app_server/device-location-callback',
            phoneNumberInput: 'phone_number',
            phoneNumberValue: '+34666666666'
        },
        devicestatus: {
            scope: 'dpv:FraudPreventionAndDetection#device-status-roaming-read',
            redirectUri: 'https://my_app_server/device-status-callback',
            phoneNumberInput: 'phone_number',
            phoneNumberValue: '+34777777777'
        },
        deviceswap: {
            scope: 'dpv:FraudPreventionAndDetection#device-swap',
            redirectUri: 'https://my_app_server/deviceswap-callback',
            phoneNumberInput: 'phone_number',
            phoneNumberValue: '+34333333333'
        },
        knowyourcustomer: {
            scope: 'dpv:FraudPreventionAndDetection#kyc-match:match',
            redirectUri: 'https://my_app_server/kyc-match-callback',
            phoneNumberInput: 'phone_number',
            phoneNumberValue: '+34666666666'
        },
        numberverification: {
            scope: 'dpv:FraudPreventionAndDetection#number-verification-verify-read',
            redirectUri: '/numberverification-callback',
            phoneNumberInput: 'state',
            phoneNumberValue: '+34555555555'
        },
        qod: {
            scope: 'dpv:RequestedServiceProvision#qod',
            redirectUri: '/qod-auth-callback'
        },
        simswap: {
            scope: 'dpv:FraudPreventionAndDetection#sim-swap',
            redirectUri: '/simswap-callback',
            phoneNumberInput: 'state',
            phoneNumberValue: '+34555555555'
        }
    };

    beforeAll((done) => {
        try {
            const files = glob.sync('./tmp/html/**/Auth_code_HTML_*.html');
            files.forEach(file => {
                const filePath = path.resolve(__dirname, file);
                const html = fs.readFileSync(filePath, 'utf8');
                const dom = new JSDOM(html);
                documents.push(dom.window.document);

                const dirPath = path.dirname(filePath);
                const lastSubdirectory = path.basename(dirPath);
                api.push(lastSubdirectory);
            });
            done();
        } catch (err) {
            console.error('Error:', err);
        }
    });

    test('form should have correct action URL', () => {
        documents.forEach((document, index) => {
            try {
                const form = document.getElementById('apiRequestForm');
                expect(form.action).toBe('https://opengateway.aggregator.com/authorize', `Error in file of API:: ${api[index]}`);
            } catch (error) {
                console.error(`Error in file of API:: ${api[index]}`);
                throw error;
           }
        });
    });

    test('form should use GET method', () => {
        documents.forEach((document, index) => {
            try {
                const form = document.getElementById('apiRequestForm');
                expect(form.method.toLowerCase()).toBe('get');
            } catch (error) {
                console.error(`Error in file of API:: ${api[index]}`);
                throw error;
            }    
        });
    });

    test('hidden inputs should have correct values', () => {
        documents.forEach((document, index) => {
            const clientIdInput = document.querySelector('input[name="client_id"]');
            const responseTypeInput = document.querySelector('input[name="response_type"]');
            const scopeInput = document.querySelector('input[name="scope"]');
            const redirectUriInput = document.querySelector('input[name="redirect_uri"]');
            try {
                const apiValue = apiValues[api[index]];

                expect(clientIdInput.value).toBe('my-app-id');
                expect(responseTypeInput.value).toBe('code');
                expect(scopeInput.value).toBe(apiValue.scope);
                expect(redirectUriInput.value).toBe(apiValue.redirectUri);
            } catch (error) {
                console.error(`Error in file of API:: ${api[index]}`);
                throw error;
            }
        });
    });

    test('phone number input should have correct value and be required', () => {
        documents.forEach((document, index) => {
            const apiValue = apiValues[api[index]];
            if (api[index] === 'qod') {
                console.log('Skipping test for API::', api[index]);
                return;
            }
            const phoneNumberInput = document.getElementById(apiValue.phoneNumberInput);
            try {
                if (!phoneNumberInput) {
                    console.error(`Phone number input not found in API: ${api[index]}`);
                    return;
                }
                expect(phoneNumberInput.value).toBe(apiValue.phoneNumberValue);
                expect(phoneNumberInput.required).toBe(true);
            } catch (error) {
                console.error(`Error in file of API:: ${api[index]}`);
                throw error;
            }
        });
    });
});
