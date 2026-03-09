---
page_order: 1.4
nav_title: Registro detallado
article_title: Registro detallado
description: "Aprende a habilitar el registro detallado para el SDK de Braze, recopilar registros para la solución de problemas y compartirlos con el soporte de Braze."
---

# Registro detallado

> El registro detallado muestra información detallada y de bajo nivel del SDK de Braze, lo que te permite ver cómo se inicializa el SDK, cómo se comunica con los servidores y cómo procesa los canales de mensajería, como las notificaciones push, los mensajes dentro de la aplicación y las tarjetas de contenido.

Cuando algo no funciona como se espera, como por ejemplo, una notificación push que no llega, un mensaje dentro de la aplicación que no se muestra o datos de usuario que no se sincronizan, los registros detallados te ayudan a identificar la causa raíz. En lugar de hacer conjeturas, puedes ver exactamente lo que hace el SDK en cada paso.

{% alert tip %}
Si deseas depurar sin habilitar manualmente el registro detallado, puedes utilizar el [depurador del SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para crear sesiones de depuración directamente en el panel de Braze.
{% endalert %}

## Cuándo utilizar el registro detallado

Activa el registro detallado cuando sea necesario:

- **Verifica la inicialización del SDK**: Confirma que el SDK se inicia correctamente con la clave de API y el punto final SDK correctos.
- **Solución de problemas con la entrega de mensajes**: Comprueba si los tokens de notificaciones push están registrados, si se desencadenan los mensajes dentro de la aplicación o si las tarjetas de contenido están sincronizadas.
- **Depurar vínculos profundos**: Comprueba que el SDK recibe y abre vínculos profundos desde notificaciones push, mensajes dentro de la aplicación o tarjetas de contenido.
- **Validar el seguimiento de la sesión**: Confirma que las sesiones comienzan y terminan según lo previsto.
- **Diagnosticar problemas de conectividad**: Inspecciona las solicitudes y respuestas de red entre el SDK y los servidores de Braze.

## Habilitar el registro detallado

{% alert important %}
Los registros detallados están destinados únicamente a entornos de desarrollo y pruebas. Desactiva el registro detallado antes de lanzar tu aplicación a producción para evitar que se exponga información confidencial.
{% endalert %}

{% tabs %}
{% tab Android %}

Habilita el registro detallado antes de cualquier otra llamada al SDK en tu`Application.onCreate()`método para capturar la salida más completa.

**En código:**

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}

**En`braze.xml`:**

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```

Para verificar que la habilitación del registro detallado está activa, busca`V/Braze`  en la salida de Logcat. Por ejemplo:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

Para obtener más información, consulta [Registro de Android SDK]({{site.baseurl}}/developer_guide/sdk_integration#android_enabling-logs).

{% endtab %}
{% tab Swift %}

Establece el nivel de registro en`.debug`  en tu`Braze.Configuration`  objeto durante la inicialización.

{% subtabs %}
{% subtab SWIFT %}
```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.logger.level = .debug
let braze = Braze(configuration: configuration)
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
[configuration.logger setLevel:BRZLoggerLevelDebug];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endsubtab %}
{% endsubtabs %}

El`.debug`nivel es el más detallado y se recomienda para la solución de problemas. Para obtener más información, consulta [Registro de SWIFT SDK]({{site.baseurl}}/developer_guide/sdk_integration#swift_log-levels).

{% endtab %}
{% tab Web %}

Añade`?brazeLogging=true`  como parámetro URL o habilita la habilitación del registro durante la inicialización del SDK:

```javascript
braze.initialize('YOUR-API-KEY', {
    baseUrl: 'YOUR-SDK-ENDPOINT',
    enableLogging: true
});
```

También puedes alternar el registro después de la inicialización:

```javascript
braze.toggleLogging();
```

Los registros aparecen en la pestaña **Consola** de las herramientas de desarrollo de tu navegador. Para obtener más información, consulta [Registro de SDK Web]({{site.baseurl}}/developer_guide/sdk_integration#web_logging).

{% endtab %}
{% tab Unity %}

1. Abre los ajustes de configuración de Braze navegando hasta **Braze** > **Configuración de Braze**.
2. Selecciona el menú desplegable **Mostrar configuración de Braze para Android**.
3. En el campo **Nivel de registro del SDK**, introduce `0`.

{% endtab %}
{% tab React Native %}

Establece el nivel de registro durante la configuración del SDK:

```javascript
const configuration = new Braze.BrazeConfiguration('YOUR-API-KEY', 'YOUR-SDK-ENDPOINT');
configuration.logLevel = Braze.LogLevel.Verbose;
```

{% endtab %}
{% endtabs %}

## Recopilación de registros

Después de habilitar el registro detallado, reproduce el problema que estás resolviendo en la solución de problemas y, a continuación, recopila los registros de la consola o la herramienta de depuración de tu plataforma.

{% tabs %}
{% tab Android %}

Utiliza **Logcat** en Android Studio para capturar registros:

1. Conecta tu dispositivo o inicia un emulador.
2. En Android Studio, abre **Logcat** desde el panel inferior.
3. Filtra por`V/Braze`  o`D/Braze`  para aislar la salida del SDK de Braze.
4. Reproduce el problema.
5. Copia los registros pertinentes y guárdalos en un archivo de texto.

{% endtab %}
{% tab iOS %}

Utiliza la aplicación **Consola** en MacOS para capturar registros:

1. Instala la aplicación en tu dispositivo con el registro detallado habilitado.
2. Conecta tu dispositivo al Mac.
3. Abre la aplicación **Consola** y selecciona tu dispositivo en la barra lateral **Dispositivos**.
4. Filtra los registros por`Braze`  o`BrazeKit`  en la barra de búsqueda.
5. Reproduce el problema.
6. Copia los registros pertinentes y guárdalos en un archivo de texto.

{% endtab %}
{% tab Web %}

Utiliza las herramientas de desarrollo de tu navegador:

1. Abre las herramientas de desarrollador de tu navegador (normalmente **F12** o **Cmd+Option+I**).
2. Ve a la pestaña **Consola**.
3. Reproduce el problema.
4. Copia la salida de la consola y guárdala en un archivo de texto.

{% endtab %}
{% endtabs %}

{% alert tip %}
Cuando recopiles registros para el soporte de Braze, comienza a registrarlos antes de iniciar la aplicación y continúa hasta mucho después de que se produzca el problema. Esto ayuda a capturar la secuencia completa de eventos.
{% endalert %}

## Lectura de registros detallados

Los registros detallados siguen una estructura coherente que te ayuda a rastrear lo que está haciendo el SDK. Para aprender a interpretar la salida del registro para canales específicos, incluyendo qué entradas clave buscar y patrones comunes de solución de problemas, consulta [Lectura de registros detallados]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

## Compartir registros con el soporte de Braze

Cuando te pongas en contacto con el soporte de Braze por un problema con el SDK, incluye lo siguiente:

1. **Archivo de registro detallado**: Un registro completo desde antes del inicio de la aplicación hasta la aparición del problema.
2. **Pasos para reproducir** el problema: Una descripción clara de las acciones que desencadenan el problema.
3. **Comportamiento esperado frente a comportamiento real**: Lo que esperabas que sucediera y lo que sucedió en realidad.
4. **Versión del SDK**: La versión del SDK de Braze que estás utilizando.
5. **Plataforma y versión del sistema operativo**: Por ejemplo, iOS 18.0, Android 14 o Chrome 120.