---
nav_title: Solución de problemas relacionados con la vinculación en profundidad
article_title: Solución de problemas relacionados con la vinculación en profundidad
description: "Problemas comunes relacionados con la vinculación en profundidad en iOS y cómo diagnosticarlos, incluidos los vínculos de esquema personalizados, los vínculos universales, los vínculos de correo electrónico y los proveedores externos como Branch."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Solución de problemas relacionados con la vinculación en profundidad

> Esta página trata sobre problemas comunes relacionados con la vinculación en profundidad en iOS y cómo diagnosticarlos. Para obtener ayuda sobre cómo elegir el tipo de enlace adecuado, consulta [la guía de vinculación en profundidad de iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Para obtener más información sobre la implementación, consulta [Vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift).

## El vínculo profundo del esquema personalizado no abre la vista correcta.

Si un vínculo profundo personalizado (por ejemplo, `myapp://products/123`) abre tu aplicación pero no te lleva a la pantalla deseada:

1. **Verifica que el programa tenga registro.** En Xcode, comprueba que tu esquema aparece en la lista bajo`CFBundleURLTypes`  en `Info.plist`.
2. **Comprueba tu controlador.** Establece un punto de interrupción en`application(_:open:options:)`  para confirmar que se está llamando e inspecciona el`url`parámetro .
3. **Prueba el enlace de forma independiente.** Ejecuta el siguiente comando desde Terminal para probar el vínculo profundo fuera de Braze:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   Si el enlace no funciona aquí, el problema está en el manejo de la URL de tu aplicación, no en Braze.
4. **Comprueba el formato de la URL.** Verifica que la URL de tu campaña coincida con lo que espera tu controlador. Entre los errores más comunes se incluyen la falta de componentes de ruta o el uso incorrecto de mayúsculas y minúsculas.

## El enlace universal se abre en Safari en lugar de en la aplicación.

Si un enlace universal (por ejemplo, `https://myapp.com/products/123`) se abre en Safari en lugar de en tu aplicación:

### Verifica el derecho a los dominios asociados.

En Xcode, ve al objetivo de tu aplicación > **Capacidades& de firma** y comprueba que`applinks:yourdomain.com`aparece en el listado de **Dominios asociados**.

### Validar el archivo AASA

Tu archivo de asociación de sitios de aplicaciones de Apple (AASA) debe estar alojado en una de estas ubicaciones:

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

Verifica lo siguiente:

- El archivo se sirve a través de HTTPS con un certificado válido.
- El`Content-Type`  es `application/json`.
- El tamaño del archivo es inferior a 128 KB.
- Coincide`appID`con tu ID de equipo y tu ID de paquete (por ejemplo, `ABCDE12345.com.example.myapp`).
- La matriz`paths``components`  o  incluye los patrones de URL que esperas.

Puedes validar tu AASA utilizando [la herramienta de validación de búsqueda de Apple](https://search.developer.apple.com/appsearch-validation-tool/) o ejecutando:

```bash
swcutil dl -d yourdomain.com
```

### Comprueba el `AppDelegate`

Verifica que`application(_:continue:restorationHandler:)`  esté implementado en tu`AppDelegate`  y que gestione correctamente `NSUserActivity`el :

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Verifica la configuración del SDK de Braze.

Si utilizas enlaces universales desde notificaciones push, mensajes dentro de la aplicación o tarjetas de contenido entregadas por Braze, confirma que`forwardUniversalLinks`  está habilitado:

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
El reenvío universal de enlaces requiere acceso a los derechos de la aplicación. Cuando se ejecuta en un simulador, estos derechos no están disponibles directamente. Para realizar pruebas en un simulador, añade el`.entitlements`archivo a la fase de compilación **«Copiar recursos del paquete**».
{% endalert %}

### Comprueba si hay algún problema con la pulsación prolongada.

Si mantienes pulsado un enlace universal y seleccionas **Abrir**, iOS puede «romper» la asociación del enlace universal para ese dominio. Este es un comportamiento conocido de iOS. Para restablecerlo, mantén pulsado el enlace de nuevo y selecciona **Abrir en [nombre de la aplicación]**.

## El vínculo profundo del correo electrónico no abre la aplicación.

Los enlaces de correo electrónico pasan por el sistema de seguimiento de clics de tu ESP, que envuelve los enlaces en un dominio de seguimiento (por ejemplo, `https://click.yourdomain.com/...`). Para que los enlaces universales funcionen desde el correo electrónico, debes configurar el archivo AASA en tu dominio de seguimiento de clics, no solo en tu dominio principal.

### Verificar el dominio de seguimiento de clics AASA

1. Identifica tu dominio de seguimiento de clics en la configuración de tu ESP (SendGrid, SparkPost o Amazon SES).
2. Aloja el archivo AASA en `https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. Asegúrate de que el archivo AASA del dominio de seguimiento de clics incluya los mismos patrones `appID`de ruta válidos.

Para obtener instrucciones de configuración específicas para ESP, consulta [Enlaces universales y Enlaces a aplicaciones.]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)

### Comprueba la cadena de redireccionamiento.

Algunos ESP realizan un redireccionamiento desde la URL de seguimiento de clics a tu URL final. Los enlaces universales solo funcionan si iOS reconoce el dominio *inicial* (el dominio de seguimiento de clics) como asociado a tu aplicación. Si el redireccionamiento omite la comprobación AASA, el enlace se abre en Safari.

Para probar:

1. Envíate un correo electrónico de prueba.
2. Mantén pulsado el enlace y comprueba la URL: esta es la URL de seguimiento de clics.
3. Verifica que este dominio tenga un archivo AASA válido.

## Los vínculos profundos funcionan desde notificaciones push, pero no desde mensajes dentro de la aplicación (o viceversa).

### Comprueba BrazeDelegate.

Si implementas `BrazeDelegate.braze(_:shouldOpenURL:)`, comprueba que gestiona los enlaces de forma coherente en todos los canales. El`context`parámetro incluye el canal de origen. Busca la lógica condicional que pueda filtrar accidentalmente enlaces de canales específicos.

### Habilitar el registro detallado

[Habilita el registro detallado]({{site.baseurl}}/developer_guide/verbose_logging) y reproduce el problema. Busca la entrada`Opening` del registro:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Compara la salida del registro del canal que funciona con la del canal que no funciona. Las diferencias en`useWebView`  o`isUniversalLink`  indican cómo el SDK interpreta el enlace de manera diferente.

### Comprueba si hay delegados de visualización personalizados.

Si utilizas un delegado de visualización de mensajes dentro de la aplicación personalizado o un controlador de clics de tarjetas de contenido, comprueba que transmite correctamente los eventos de enlace al SDK de Braze para su gestión.

## «Abrir URL Web dentro de la aplicación» muestra una página en blanco o dañada.

Si al seleccionar **«Abrir URL web dentro de la aplicación»** aparece una vista web en blanco o dañada:

1. **Comprueba que la URL utiliza HTTPS.** La WebView del SDK requiere URL compatibles con ATS. Los enlaces HTTP fallan silenciosamente.
2. **Comprueba los encabezados de la política de seguridad de contenidos.** Si la página web de destino establece`X-Frame-Options: DENY`  o una restricción `Content-Security-Policy`, bloquea la representación en una WebView.
3. **Comprueba si hay redireccionamientos a esquemas personalizados.** Si la página web redirige a un esquema personalizado (por ejemplo, `myapp://`), WebView no puede gestionarlo.
4. **Prueba la URL en Safari.** Si la página no se carga en Safari en el dispositivo, tampoco se cargará en WebView.

## Solución de problemas con Braze {#branch}

Si utilizas [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) como proveedor de enlaces:

### Verifica las rutas de BrazeDelegate a Branch.

Debes`BrazeDelegate` interceptar los enlaces de Branch y pasarlos al SDK de Branch. Verifica lo siguiente:

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

Si`shouldOpenURL`se devuelven enlaces`true` de Branch, Braze los gestiona directamente en lugar de redirigirlos a Branch.

### Comprueba el dominio del enlace de la sucursal.

Verifica que el dominio de Branch en tu`BrazeDelegate`  coincida con tu dominio de enlace de Branch real. Branch utiliza varios formatos de dominio:

- `yourapp.app.link` (predeterminado)
- `yourapp-alternate.app.link` (alternativo)
- Dominios personalizados (si están configurados en el panel de control de Branch)

### Habilitar el registro de ambos SDK

Para diagnosticar dónde se rompe el eslabón de la cadena:

1. Habilita [el registro detallado de Braze]({{site.baseurl}}/developer_guide/verbose_logging): busca`Opening '<URL>':`entradas para verificar que el SDK haya recibido el enlace.
2. Habilita [el modo de prueba de Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking): comprueba el panel de control de Branch para ver los eventos de clics en los enlaces.
1. Habilita [el registro detallado de Braze]({{site.baseurl}}/developer_guide/verbose_logging). Busca`Opening '<URL>':`entradas para verificar que el SDK recibió el enlace.
2. Habilita [el modo de prueba de Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking). Comprueba el panel de Branch para ver los eventos de clics en los enlaces.
3. Si Braze registra el enlace, pero Branch no detecta ningún clic, es probable que el problema esté en la lógica`BrazeDelegate` de enrutamiento.

### Comprueba la configuración del panel de la sucursal.

En el panel de control de la sucursal, verifica lo siguiente:

- **El ID del paquete** y **el ID del equipo** de tu aplicación coinciden con tu proyecto Xcode.
- Tus **dominios asociados** incluyen el dominio del enlace de la sucursal.
- Tu archivo AASA de Branch es válido (Branch lo aloja automáticamente en`app.link`los dominios).

### Prueba los enlaces de la rama de forma independiente.

Prueba el enlace Branch fuera de Braze para aislar el problema:

1. Abre el enlace Branch en Safari en tu dispositivo. Si no se abre la aplicación, el problema está en tu configuración de Branch o AASA, no en Braze.
2. Pega el enlace de Branch en la aplicación Notas y pulsa sobre él. Los enlaces universales funcionan de forma más fiable desde Notes que desde la barra de direcciones de Safari.

## Consejos generales para la depuración

### Utilizar registro detallado

[Habilita el registro detallado]({{site.baseurl}}/developer_guide/verbose_logging) para ver exactamente cómo procesa los enlaces el SDK. Entradas clave que debes buscar:

| Entrada de registro | Qué significa |
|---|---|
| `Opening '<URL>': - channel: notification` | El SDK está procesando un enlace desde una notificación push. |
| `Opening '<URL>': - channel: inAppMessage` | El SDK está procesando un enlace desde un mensaje dentro de la aplicación. |
| `Opening '<URL>': - channel: contentCard` | El SDK está procesando un enlace desde una tarjeta de contenido. |
| `useWebView: true` | El SDK abre la URL en la vista web integrada en la aplicación. |
| `isUniversalLink: true` | El SDK identificó la URL como un enlace universal. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener más información sobre cómo leer estos registros, consulta [Lectura de registros detallados]({{site.baseurl}}/developer_guide/verbose_logging).

### Prueba los enlaces de forma aislada.

Antes de realizar pruebas a través de Braze, comprueba que tu vínculo profundo o enlace universal funciona por sí solo:

- **Esquema personalizado**: Ejecuta`xcrun simctl openurl booted "myapp://path"`  en Terminal.
- **Enlace universal**: Pega la URL en la aplicación Notas de un dispositivo físico y pulsa sobre ella. No realices pruebas desde la barra de direcciones de Safari, ya que iOS trata las URL escritas de forma diferente a los enlaces pulsados.
- **Enlace de la sucursal**: Abre el enlace Branch desde la aplicación Notas en un dispositivo.

### Prueba en un dispositivo físico

Los enlaces universales tienen una compatibilidad limitada en el simulador de iOS. Prueba siempre en un dispositivo físico para obtener resultados precisos. Si tienes que realizar pruebas en un simulador, añade el`.entitlements`archivo a la fase de compilación **«Copiar recursos del paquete**».