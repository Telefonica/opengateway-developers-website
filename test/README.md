# OpenGateway Sample Code Testing Suite
## Introducción

El directorio `test` contiene una suite completa de testing automatizado para todas las APIs de OpenGateway. Incluye:

1. **Extractor de código de muestra**: El script `test_code.sh` procesa archivos que contienen bloques de código fuente en diferentes lenguajes de programación (Java, Node.js, Python), los extrae, formatea y valida automáticamente.

2. **Suite de tests completa**: 
   - **Tests de Python** (`python_test.py`): 9 tests unitarios con mocks para todas las APIs
   - **Tests de Node.js** (`nodeSandbox.test.js`): 9 tests de integración con el SDK oficial
   - **Tests de validación HTML** (`htmlForm.test.js`): Validación de configuraciones de formularios

3. **SDK Mock personalizado** (`mock_aggregator_sdk.py`): Implementación mock completa para testing sin dependencias externas.

## APIs Soportadas

El sistema de testing tiene cobertura completa para las siguientes 9 APIs de OpenGateway:

1. **AgeVerification** - Verificación de edad de usuarios
2. **DeviceLocation** - Verificación de ubicación de dispositivos  
3. **DeviceStatus** - Estado de conectividad y roaming
4. **DeviceSwap** - Detección de cambios de dispositivo
5. **KnowYourCustomer** - Verificación de datos de cliente (KYC)
6. **NumberVerification** - Verificación de números de teléfono
7. **QualityOnDemand** - Gestión de calidad de servicio (QoD)
8. **Simswap** - Detección de intercambio de SIM
9. **Tenure** - Verificación de antigüedad de cliente

## Archivos de Testing

### Archivos principales:
- `test_code.sh` - Script principal de orquestación
- `python_test.py` - Suite de tests de Python (9 tests)
- `nodeSandbox.test.js` - Suite de tests de Node.js (9 tests)  
- `htmlForm.test.js` - Tests de validación HTML (4 tests)
- `mock_aggregator_sdk.py` - SDK mock para testing Python
- `package.json` - Configuración de dependencias Node.js

### Configuración:
- `babel.config.js` - Configuración de Babel para ES6
- `eslint.config.mjs` - Configuración de ESLint
- `.gitignore` - Exclusiones de archivos temporales

## Premisas
El extractor de código analiza archivos ubicados en el directorio `../catalog`, cuyo nombre coincide con el formato `samplecode_<nombre_api>.md`.

Para que el script funcione correctamente, los archivos `samplecode_*.md` deben seguir el template actual para los bloques de código, es decir, cumplir las siguientes reglas:
- Los archivos deben estar ubicados en el directorio `../catalog`.
- Los nombres de los archivos deben tener el formato `samplecode_<nombre_api>.md`.
- Cada bloque de código debe estar delimitado por marcas de inicio y fin de bloque:
  - La marca de inicio de bloque debe ser ` ``` <lenguaje de programación> <Descripción del caso de uso> `.
  - La marca de fin de bloque debe ser ` ``` `.
- Los bloques de código deben estar correctamente indentados siguiendo las normas correspondientes para el lenguaje de programación al que corresponde.

## Funcionamiento

### Script Principal (`test_code.sh`)
El script de orquestación realiza las siguientes tareas:

1. **Extracción de código**: Procesa archivos `samplecode_*.md` y extrae bloques de código por lenguaje
2. **Corrección automática**: Aplica fixes automáticos para imports y sintaxis de Python
3. **Generación de SDKs simplificados**: Crea versiones mock para APIs problemáticas
4. **Ejecución de tests**: Ejecuta la suite completa de Python y Node.js
5. **Linting**: Valida código con ESLint (JavaScript) y flake8 (Python)

### Tests de Python (`python_test.py`)
- **Framework**: unittest con mock
- **Cobertura**: 9 APIs con tests individuales
- **Mock SDK**: Utiliza `mock_aggregator_sdk.py` para simular respuestas
- **Validación**: Verifica llamadas correctas y respuestas esperadas

### Tests de Node.js (`nodeSandbox.test.js`)  
- **Framework**: Jest con mocks del SDK oficial
- **Cobertura**: 9 APIs con configuraciones específicas
- **SDK**: Utiliza `@telefonica/opengateway-sandbox-sdk`
- **Validación**: Tests de instanciación y métodos principales

### Tests HTML (`htmlForm.test.js`)
- **Propósito**: Valida configuraciones de formularios web
- **Cobertura**: Scope y redirect URLs para todas las APIs
- **Framework**: Jest con JSDOM para manipulación DOM

## Requisitos

### Sistema base:
- **Bash**: Shell compatible con Bash (zsh también funciona)
- **Git**: Para gestión de versiones

### Node.js:
- **Node.js** (v14+): Runtime de JavaScript
- **npm**: Gestor de paquetes (incluido con Node.js)
- **jest**: Framework de testing para JavaScript
- **eslint**: Linter para JavaScript/TypeScript

### Python:
- **Python** (v3.7+): Intérprete de Python
- **pip**: Gestor de paquetes de Python
- **flake8**: Linter para Python
- **unittest**: Framework de testing (incluido en Python)

## Instalación

1. **Instalar Node.js y npm**:
   - Puedes descargar e instalar Node.js desde nodejs.org.
   - npm se instala automáticamente con Node.js.

2. **Instalar las dependencias del proyecto**:

    - Navega al directorio del proyecto `test`,  donde se encuentra el archivo package.json.
    - Ejecuta el siguiente comando para instalar las dependencias:
      ```bash
      npm install
      ```

3. **Instalar Python**:
   - Puedes descargar e instalar Python desde python.org.

4. **Instalar flake8**:
   - Ejecuta el siguiente comando para instalar `flake8`:
     ```bash
     pip install flake8
     ```

## Ejecución

### Ejecución completa (recomendada)
```bash
cd test
chmod +x test_code.sh  # Solo la primera vez
./test_code.sh
```

### Ejecución individual de tests

**Solo tests de Python:**
```bash
cd test
python python_test.py
```

**Solo tests de Node.js:**
```bash
cd test
npm test
# O específicamente:
npx jest nodeSandbox.test.js
npx jest htmlForm.test.js
```

**Solo linting:**
```bash
cd test
# JavaScript/Node.js
npx eslint tmp/js/**/*.js

# Python  
flake8 tmp/py/
```

## Resultados Esperados

### ✅ Ejecución Exitosa
```
################### Python test ##################################
Ran 9 tests in 0.011s
OK

################### Node & html test ##################################
Test Suites: 2 passed, 2 total  
Tests: 13 passed, 13 total
```

### ⚠️ Warnings Esperados
- **ESLint warnings en `/tmp`**: Archivos generados automáticamente pueden tener warnings de estilo
- **Variables no utilizadas**: Algunas variables se mantienen para claridad educativa
- **Syntax errors en archivos generados**: Algunos archivos en `/tmp` pueden tener errores de sintaxis menores

## Estructura de Archivos Generados

```
test/
├── tmp/                          # Archivos temporales generados
│   ├── js/                       # Código JavaScript extraído
│   │   ├── devicelocation/       # Por API
│   │   ├── simswap/
│   │   └── ...
│   ├── py/                       # Código Python extraído  
│   └── html/                     # Código HTML extraído
├── python_test.py                # Tests principales Python
├── nodeSandbox.test.js          # Tests principales Node.js
├── htmlForm.test.js             # Tests de formularios HTML
├── mock_aggregator_sdk.py       # SDK mock para Python
└── test_code.sh                 # Script orquestador
```

## Notas Importantes

- El directorio `/tmp` se regenera en cada ejecución
- Los tests utilizan datos mock, no requieren conectividad real
- Algunos warnings de linting son intencionales para mantener claridad educativa
- Los archivos en `/tmp` son para validación automática, no para uso directo
