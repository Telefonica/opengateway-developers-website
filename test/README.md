# Samplecode extractor
## Introducción

El script `test_code.sh` es una herramienta automatizada para procesar archivos que contienen bloques de código fuente en diferentes lenguajes de programación (Java, Node.js, Python, ...), extraer esos bloques de código por lenguaje de programación y caso de uso especifico. Una vez extraido y formateado, se testean y/o se ejecutan herramientas linter, para chequear su corrección y funcionamiento en la medida de lo posible.

## Premisas
El script sólo analiza los archivos ubicados en el directorio `../catalog`, cuyo nombre coincide con el formato `samplecode_<nombre_api>.md`.

Para que el script funcione correctamente, los archivos `samplecode_*.md` deben seguir el template actual para los bloques de código, es decir, cumplir las siguientes reglas:
- Los archivos deben estar ubicados en el directorio `../catalog`.
- Los nombres de los archivos deben tener el formato `samplecode_<nombre_api>.md`.
- Cada bloque de código debe estar delimitado por marcas de inicio y fin de bloque:
  - La marca de inicio de bloque debe ser ` ``` <lenguaje de programación> <Descripción del caso de uso> `.
  - La marca de fin de bloque debe ser ` ``` `.
- Los bloques de código deben estar correctamente indentados siguiendo las normas correspondientes para el lenguaje de programación al que corresponde.

## Funcionamiento

El script realiza las siguientes tareas o pasos:

1. Elimina datos de ejecuciones anteriores y crea una carpeta temporal para almacenar archivos procesados.
2. Recorre archivos `samplecode_*.md` en el directorio `../catalog` y extrae bloques de código, organizándolos en carpetas temporales según el lenguaje de programación.
3. Reorganiza el código en los archivos Node.js y Python extraídos cuyo nombre empieza por Auth_code, para colocar el código de "uso de API" en la posición correcta en el código, ya que inicialmente la primera parte del script, solo agrupa el código de los bloques secuencialmente.
4. Ejecuta pruebas y linters para los archivos procesados.

## Requisitos

Para ejecutar este script, necesitas tener instalados los siguientes programas y herramientas:

- **Bash**: Un shell compatible con Bash.
- **Node.js**: Incluyendo `npx` y `jest` para ejecutar pruebas y linters.
- **Python**: Incluyendo `flake8` para ejecutar linters.

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

Para ejecutar el script `test_code.sh`, sigue estos pasos:

1. Asegúrate de que los requisitos estén instalados.
2. Navega al directorio `test` donde se encuentra el script `test_code.sh`.
3. Ejecuta el script con el siguiente comando:
   ```bash
   ./test_code.sh
   ```
El script procesará los archivos de código fuente, reorganizará los bloques de código y ejecutará las pruebas y linters correspondientes. Los resultados se mostrarán en la terminal.

Notas:
* Asegúrate de tener permisos de ejecución para el script. Si no los tienes, puedes otorgarlos con el siguiente comando:
   ```bash
   chmod +x test_code.sh
   ```
* Analiza la salida del script y ten encuenta que algunos de los warnings tiene sentido no corregirlos. Por ejemplo, algunas variables no se utilizan en el código pero se mantienen para que los usuarios tengan claro que existen y se pueden utilizar.
