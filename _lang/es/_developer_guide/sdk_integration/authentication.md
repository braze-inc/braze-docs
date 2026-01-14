---
page_order: 1.2
nav_title: Autenticación
article_title: Configuración de la autenticación para el SDK de Braze
description: "Este artículo de referencia cubre la autenticación del SDK y cómo habilitar esta característica en el SDK de Braze."
platform:
  - iOS
  - Android
  - Web
  
---

# Configuración de la autenticación SDK

> La Autenticación del SDK te permite proporcionar una prueba criptográfica (generada en el servidor) a las solicitudes del SDK realizadas en nombre de usuarios que han iniciado sesión.

## Cómo funciona

Después de habilitar esta característica en tu aplicación, puedes configurar el panel de Braze para que rechace cualquier solicitud con un JSON Web Token (JWT) no válido o que falte, lo que incluye:

- Envío de eventos personalizados, atributos, compras y datos de sesión
- Crear nuevos usuarios en tu espacio de trabajo Braze
- Actualización de los atributos estándar del perfil de usuario
- Recibir o desencadenar mensajes

Ahora puedes impedir que los usuarios no autentificados que hayan iniciado sesión utilicen la clave de API de SDK de tu aplicación para realizar acciones maliciosas, como suplantar la identidad de otros usuarios.

## Configuración de la autenticación

### Paso 1: Configura tu servidor {#server-side-integration}

#### Paso 1.1: Generar un par de claves pública/privada {#generate-keys}

Genera un par de claves públicas/privadas RSA256. La clave pública se añadirá finalmente al panel de Braze, mientras que la clave privada debe almacenarse de forma segura en tu servidor.

Recomendamos usar una clave RSA con 2048 bits con el algoritmo RS256 JWT.

{% alert warning %}
Recuerda mantener _la privacidad de_ tus claves privadas. Nunca expongas o codifiques tu clave privada en tu aplicación o sitio web. Cualquiera que conozca tu clave privada puede suplantar o crear usuarios en nombre de tu aplicación.
{% endalert %}

#### Paso 1.2: Crear un Token Web JSON para el usuario actual {#create-jwt}

Una vez que tengas tu clave privada, tu aplicación del lado del servidor debe utilizarla para devolver un JWT a tu aplicación o sitio web para el usuario conectado en ese momento.

Normalmente, esta lógica podría ir allí donde tu aplicación solicitaría normalmente el perfil del usuario actual; como un punto final de inicio de sesión o donde tu aplicación actualice el perfil del usuario actual.

Al generar el JWT, se esperan los siguientes campos:

**Encabezado JWT**

| Campo | Obligatoria | Descripción                         |
| ----- | -------- | ----------------------------------- |
| `alg` | Sí  | El algoritmo admitido es `RS256`. |
| `typ` | Sí  | El tipo debe ser igual a `JWT`.        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

**Carga útil JWT**

| Campo | Obligatoria | Descripción                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | Sí  | El "asunto" debe ser igual al ID de usuario que proporcionas al SDK de Braze cuando llamas a `changeUser`  |
| `exp` | Sí | La "caducidad" de cuándo quieres que caduque este token.                                |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Para saber más sobre los tokens Web JSON, o para echar un vistazo a las muchas bibliotecas de código abierto que simplifican este proceso de firma, consulta [https://jwt.io.](https://jwt.io)
{% endalert %}

### Paso 2: Configura el SDK {#sdk-integration}

Esta característica está disponible a partir de las siguientes [versiones del SDK]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
Para las integraciones de iOS, en esta página se detallan los pasos para el SDK Swift de Braze. Para ver ejemplos de uso en el SDK heredado de AppboyKit para iOS, consulta [este archivo](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) y [este archivo](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m).
{% endalert %}

#### Paso 2.1: Habilita la autenticación en el SDK de Braze.

Cuando esta característica está habilitada, el SDK de Braze añadirá el último JWT conocido del usuario actual a las solicitudes de red realizadas a los servidores Braze.

{% alert note %}
No te preocupes, inicializar sólo con esta opción no afectará a la recopilación de datos en modo alguno, hasta que empieces a [aplicar la autenticación](#braze-dashboard) dentro del panel Braze.
{% endalert %}

{% tabs %}
{% tab JavaScript %}
Cuando llames a `initialize`, establece la propiedad opcional `enableSdkAuthentication` en `true`.
```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab Java %}
Cuando configures la instancia de Braze, llama a `setIsSdkAuthenticationEnabled` a `true`.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

Alternativamente, puedes añadir `<bool name="com_braze_sdk_authentication_enabled">true</bool>` a tu braze.xml.
{% endtab %}
{% tab KOTLIN %}
Cuando configures la instancia de Braze, llama a `setIsSdkAuthenticationEnabled` a `true`.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

Alternativamente, puedes añadir `<bool name="com_braze_sdk_authentication_enabled">true</bool>` a tu braze.xml.
{% endtab %}
{% tab Objective-C %}
Para habilitar la Autenticación SDK, establece la propiedad `configuration.api.sdkAuthentication` de tu objeto `BRZConfiguration` en `YES` antes de inicializar la instancia de Braze:

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Swift %}
Para habilitar la Autenticación SDK, establece la propiedad `configuration.api.sdkAuthentication` de tu objeto `Braze.Configuration` en `true` al inicializar el SDK:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
Actualmente, la autenticación del SDK debe habilitarse como parte de la inicialización del SDK en el código nativo de iOS y Android. Para habilitar la Autenticación SDK en el SDK de Flutter, sigue las integraciones para iOS y Android desde las otras pestañas. Una vez habilitada la Autenticación SDK, el resto de la característica puede integrarse en Dart.
{% endtab %}
{% endtabs %}

#### Paso 2.2: Configura la JWT del usuario actual

Siempre que tu aplicación llame al método Braze `changeUser`, proporciona también el JWT que se [generó en el servidor](#braze-dashboard).

También puedes configurar el token para que se actualice a mitad de sesión para el usuario actual.

{% alert note %}
Ten en cuenta que `changeUser` solo debe invocarse cuando el ID de usuario haya _cambiado realmente_. No debes utilizar este método para actualizar el token de autenticación (JWT) si el ID de usuario no ha cambiado.
{% endalert %}

{% tabs %}
{% tab JavaScript %}
Proporciona el JWT cuando llames a [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
):

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

O, cuando hayas refrescado el token del usuario en mitad de la sesión:

```javascript
import * as braze from"@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

Proporciona el JWT cuando llames a [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

O, cuando hayas refrescado el token del usuario en mitad de la sesión:

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

Proporciona el JWT cuando llames a [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER")
```

O, cuando hayas refrescado el token del usuario en mitad de la sesión:

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Objetivo-C %}

Proporciona el JWT cuando llames a [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"JWT-FROM-SERVER"];
```

O, cuando hayas refrescado el token del usuario en mitad de la sesión:

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"NEW-JWT-FROM-SERVER"];
```
{% endtab %}
{% tab Swift %}

Proporciona el JWT cuando llames a [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
O, cuando hayas refrescado el token del usuario en mitad de la sesión:

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Dart %}

Proporciona el JWT cuando llames a [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```dart
braze.changeUser("userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
O, cuando hayas refrescado el token del usuario en mitad de la sesión:

```dart
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```

{% endtab %}
{% endtabs %}

#### Paso 2.3: Registra una función de devolución de llamada para tokens no válidos {#sdk-callback}

Cuando esta característica se establece como [Requerido](#enforcement-options), los siguientes escenarios harán que las solicitudes SDK sean rechazadas por Braze:
- El JWT había caducado en el momento en que lo recibió la API de Braze
- El JWT estaba vacío o faltaba
- No se ha podido verificar JWT para las claves públicas que has cargado en el panel de Braze

Puedes utilizar `subscribeToSdkAuthenticationFailures` para suscribirte y recibir una notificación cuando las solicitudes del SDK fallen por uno de estos motivos. Una función de devolución de llamada contiene un objeto con la información relevante [`errorCode`](#error-codes), `reason` para el error, el `userId` de la solicitud (si el usuario no es anónimo), y el token de autenticación (JWT) que causó el error. 

Las solicitudes fallidas se reintentarán periódicamente hasta que tu aplicación proporcione un nuevo JWT válido. Si ese usuario sigue conectado, puedes utilizar esta devolución de llamada como una oportunidad para solicitar un nuevo JWT a tu servidor y suministrar al SDK de Braze este nuevo token válido.

{% alert tip %}
Estos métodos de devolución de llamada son un buen lugar para añadir tu propio servicio de seguimiento o registro de errores para controlar la frecuencia con la que se rechazan tus solicitudes Braze.
{% endalert %}

{% tabs %}
{% tab JavaScript %}
```javascript
import * as braze from"@braze/web-sdk";
braze.subscribeToSdkAuthenticationFailures((error) => {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  const updated_jwt = await getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(updated_jwt);
});
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    // TODO: Optionally log to your error-reporting service
    // TODO: Check if the error user matches the currently logged-in user
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    // TODO: Optionally log to your error-reporting service
    // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  NSLog(@"Invalid SDK Authentication Token.");
  NSString *newSignature = getNewTokenSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% endtabs %}

### Paso 3: Habilitar la autenticación en el panel de control {#braze-dashboard}

A continuación, puedes habilitar la autenticación en el panel de Braze para las aplicaciones que configuraste anteriormente.

Ten en cuenta que las solicitudes de SDK seguirán fluyendo como de costumbre sin autenticación, a menos que la configuración de Autenticación de SDK de la aplicación se establezca en **Obligatorio** en el panel de Braze.

Si algo va mal con tu integración (por ejemplo, tu aplicación está pasando tokens incorrectamente al SDK, o tu servidor está generando tokens no válidos), desactiva esta característica en el panel de Braze, y los datos volverán a fluir como de costumbre sin verificación.

#### Opciones de aplicación {#enforcement-options}

En la página **Administrar configuración** del panel, cada aplicación tiene tres estados de Autenticación SDK que controlan cómo verifica Braze las solicitudes.

| Configuración| Descripción|
| ------ | ---------- |
| **Deshabilitada** | Braze no verificará el JWT suministrado para un usuario. (Configuración predeterminada)|
| **Opcional** | Braze verificará las solicitudes de los usuarios registrados, pero no rechazará las solicitudes no válidas. |
| **Obligatoria** | Braze verificará las solicitudes de los usuarios registrados y rechazará los JWT no válidos.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/sdk-auth-settings.png %})

La configuración **Opcional** es una forma útil de controlar el impacto potencial que esta característica tendrá en el tráfico SDK de tu aplicación.

Un JWT inválido se notificará tanto en el estado **Opcional** como en el **Requerido**, sin embargo, sólo el estado **Requerido** rechazará las solicitudes SDK haciendo que las aplicaciones vuelvan a intentarlo y soliciten un nuevo JWT.

## Administrador de claves públicas {#key-management}

### Añadir una clave pública

Puedes añadir hasta tres claves públicas para cada aplicación: una principal, una secundaria y una terciaria. También puedes añadir la misma clave a más de una aplicación si es necesario. Para añadir una clave pública:

1. Ve al panel de Braze y selecciona **Configuración** > Configuración de la aplicación **.**
2. Elige una aplicación de tu lista de aplicaciones disponibles.
3. En **Autenticación SDK**, selecciona **Añadir clave pública**.
4. Introduce una descripción opcional, pega tu clave pública y selecciona **Añadir clave pública**.

### Asignar una nueva clave primaria

Para asignar una clave secundaria o terciaria como nueva clave primaria:

1. Ve al panel de Braze y selecciona **Configuración** > Configuración de la aplicación **.**
2. Elige una aplicación de tu lista de aplicaciones disponibles.
3. En **Autenticación SDK**, elige una clave y selecciona **Gestionar** > **Convertir en clave principal**.

### Borrar una clave

Para eliminar una clave primaria, [asigna primero una nueva primaria](#assign-a-new-primary-key) y luego elimina tu clave. Para borrar una clave no primaria:

1. Ve al panel de Braze y selecciona **Configuración** > Configuración de la aplicación **.**
2. Elige una aplicación de tu lista de aplicaciones disponibles.
3. En **Autenticación SDK**, elige una clave no primaria y selecciona **Gestionar** > **Eliminar clave pública**.

## Análisis {#analytics}

Cada aplicación mostrará un desglose de los errores de Autenticación SDK recopilados mientras esta característica está en estado **Opcional** y **Obligatorio**.

Los datos están disponibles en tiempo real, y puedes pasar el ratón por encima de los puntos del gráfico para ver un desglose de los errores de una fecha determinada.

![Un gráfico que muestra el número de instancias de errores de autenticación. También se muestra el número total de errores, el tipo de error y el intervalo de fechas ajustable.]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## Códigos de error {#error-codes}

| Código de error| Motivo del error | Descripción |
| --------  | ------------ | ---------  |
| 10 | `EXPIRATION_REQUIRED` | La caducidad es un campo obligatorio para el uso de Braze.|
| 20 | `DECODING_ERROR` | Clave pública no coincidente o error general no detectado.|
| 21 | `SUBJECT_MISMATCH` | Los sujetos esperados y los reales no son los mismos.|
| 22 | `EXPIRED` | El token proporcionado ha caducado.|
| 23 | `INVALID_PAYLOAD` | La carga útil del token no es válida.|
| 24 | `INCORRECT_ALGORITHM` | No se admite el algoritmo del token.|
| 25 | `PUBLIC_KEY_ERROR` | No se ha podido convertir la clave pública al formato adecuado.|
| 26 | `MISSING_TOKEN` | No se ha proporcionado ningún token en la solicitud.|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | Ninguna clave pública coincide con el token proporcionado.|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | No todos los ID de usuario de la carga útil de la solicitud coinciden como es debido.|
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 role="presentation" }

## Preguntas más frecuentes (FAQ) {#faq}

#### ¿Es necesario habilitar esta característica en todas mis aplicaciones al mismo tiempo? {#faq-app-by-app}

No, esta característica puede habilitarse para aplicaciones concretas y no es necesario utilizarla en todas tus aplicaciones a la vez.

#### ¿Qué ocurre con los usuarios que siguen utilizando versiones anteriores de mi aplicación? {#faq-sdk-backward-compatibility}

Cuando empieces a aplicar esta característica, las solicitudes realizadas por versiones anteriores de la aplicación serán rechazadas por Braze y reintentadas por el SDK. Después de que los usuarios actualicen su aplicación a una versión compatible, esas solicitudes en cola empezarán a aceptarse de nuevo.

Si es posible, debes empujar a los usuarios a actualizarse como harías con cualquier otra actualización obligatoria. Alternativamente, puedes mantener la característica [Opcional](#enforcement-options) hasta que veas que un porcentaje aceptable de usuarios se ha actualizado.

#### ¿Qué caducidad debo utilizar al generar un JWT? {#faq-expiration}

Te recomendamos que utilices el valor más alto de la duración media de la sesión, la caducidad de la cookie/token de sesión o la frecuencia con la que tu aplicación actualizaría el perfil del usuario actual.

#### ¿Qué ocurre si un JWT caduca en mitad de la sesión de un usuario? {#faq-jwt-expiration}

Si el token de un usuario caduca en mitad de la sesión, el SDK tiene una [función de devolución de llamada](#sdk-callback) que invocará para que tu aplicación sepa que se necesita un nuevo JWT para seguir enviando datos a Braze.

#### ¿Qué ocurre si mi integración en servidor se rompe y ya no puedo crear un JWT? {#faq-server-downtime}

Si tu servidor no puede proporcionar un JWT o detectas algún problema de integración, siempre puedes desactivar la característica en el panel de Braze.

Una vez desactivado, el SDK reintentará cualquier solicitud fallida pendiente, y Braze la aceptará.

#### ¿Por qué esta característica utiliza claves públicas/privadas en lugar de secretos compartidos? {#faq-shared-secrets}

Al utilizar secretos compartidos, cualquiera con acceso a ese secreto compartido, como la página del panel de Braze, podría generar tokens y suplantar la identidad de tus usuarios finales.

En su lugar, utilizamos claves públicas/privadas para que ni siquiera los Empleados de Braze (y mucho menos los usuarios de tu panel) tengan acceso a tus claves privadas.

#### ¿Cómo se reintentarán las solicitudes rechazadas? {#faq-retry-logic}

Cuando se rechaza una solicitud debido a un error de autenticación, el SDK invocará su devolución de llamada utilizada para actualizar la JWT del usuario. 

Las solicitudes se reintentarán periódicamente utilizando un método de retirada exponencial. Después de 50 intentos fallidos consecutivos, los reintentos se pausarán hasta el siguiente inicio de sesión. Cada SDK también tiene un método para solicitar manualmente una descarga de datos.

