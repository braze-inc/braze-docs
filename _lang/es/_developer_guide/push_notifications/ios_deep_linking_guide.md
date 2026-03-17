---
page_order: 1.1
nav_title: Guía de vinculación en profundidad para iOS
article_title: Guía de vinculación en profundidad para iOS
description: "Descubre qué tipo de vínculo profundo debes utilizar para tu aplicación iOS, cuándo necesitas un archivo AASA y qué métodos de delegado de aplicación debes implementar."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Guía de vinculación en profundidad para iOS

> Esta guía te ayuda a elegir la estrategia de vinculación en profundidad adecuada para tu aplicación iOS, en función del canal de mensajería que utilices y de si utilizas un proveedor de vínculos externos como Branch.

Para obtener más información sobre la implementación, consulta [Vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift). Para solucionar problemas, consulta [Solución de problemas de vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

## Elegir un tipo de enlace

Hay tres formas de gestionar los enlaces de los mensajes de Braze en tu aplicación para iOS. Cada uno funciona de manera diferente y es adecuado para distintos canales y casos de uso.

| Tipo de enlace | Ejemplo | Ideal para | ¿Se abre sin tener la aplicación instalada? |
|---|---|---|---|
| **Esquema personalizado** | `myapp://products/123` | Notificaciones push, mensajes dentro de la aplicación, tarjetas de contenido | No, el enlace no funciona. |
| **Enlace universal** | `https://myapp.com/products/123` | Correo electrónico, SMS, canales con seguimiento de clics | Sí, vuelve a la Web. |
| **Abrir URL de la web dentro de la aplicación** | Cualquier`https://`URL | Mostrar contenido web en una WebView modal | N/A — se muestra en WebView |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Vínculos profundos personalizados

Los vínculos profundos personalizados (por ejemplo, `myapp://products/123`) abren la aplicación directamente en una pantalla específica. Son la opción más sencilla para canales en los que los enlaces no son modificados por terceros.

**Utiliza vínculos profundos personalizados cuando:**
- Envío de notificaciones push, mensajes dentro de la aplicación o tarjetas de contenido.
- No necesitas que el enlace funcione si la aplicación no está instalada.
- No necesitas seguimiento de clics (envoltura de enlaces de correo electrónico).

**No utilices vínculos profundos personalizados cuando:**
- Envío por correo electrónico: los ESP envuelven los enlaces para el seguimiento de clics, lo que rompe los esquemas personalizados.
- Necesitas el enlace para volver a una página Web si la aplicación no está instalada.

### Enlaces universales

Los enlaces universales (por ejemplo, `https://myapp.com/products/123`) son direcciones URL HTTPS estándar que iOS puede redirigir a tu aplicación en lugar de abrirse en un navegador. Requieren una configuración del lado del servidor (un archivo AASA) y una configuración del lado de la aplicación (derecho de dominios asociados).

**Utiliza enlaces universales cuando:**
- Envío por correo electrónico. Tu ESP envuelve los enlaces para el seguimiento de clics, por lo que los enlaces deben ser HTTPS.
- Envío de SMS u otros canales en los que los enlaces se envuelven o acortan.
- Necesitas el enlace para volver a una página de Web cuando la aplicación no está instalada.
- Estás utilizando un proveedor de enlaces externo como Branch o Appsflyer.

**No utilices enlaces universales cuando:**
- Solo necesitas vínculos profundos de mensajes push, mensajes dentro de la aplicación o tarjetas de contenido. Los esquemas personalizados son más sencillos.

### «Abrir URL Web dentro de la aplicación»

Esta opción abre una página web dentro de una WebView modal dentro de tu aplicación. El SDK de Braze se encarga de todo mediante`Braze.WebViewController`  , por lo que no es necesario escribir ningún código para gestionar las URL.

**Utiliza «Abrir URL Web dentro de la aplicación» cuando:**
- Quieres mostrar una página Web (como una promoción o un artículo) sin salir de tu aplicación.
- La URL es una página web HTTPS estándar, no un vínculo profundo a una pantalla específica de la aplicación.

**No utilices «Abrir URL Web dentro de la aplicación» cuando:**
- Debes navegar hasta una vista específica en tu aplicación. En su lugar, utiliza un esquema personalizado o un enlace universal.
- La página web requiere autenticación o tiene encabezados de política de seguridad de contenido que bloquean la incrustación.

## Lo que necesitas para cada tipo de enlace

### Vínculos profundos personalizados

| Requisito | Detalles |
|---|---|
| Archivo AASA | No es necesario |
| `Info.plist` | Realiza el registro de tu plan en`CFBundleURLTypes`  y añádelo a `LSApplicationQueriesSchemes` |
| Método delegado de la aplicación | Implementar`application(_:open:options:)`  para analizar la URL y navegar. |
| Configuración del SDK de Braze | Ninguno: el SDK abre direcciones URL de esquemas personalizados de forma predeterminada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Enlaces universales

| Requisito | Detalles |
|---|---|
| Archivo AASA | Requerido: anfitrión en `https://yourdomain.com/.well-known/apple-app-site-association` |
| Dominios asociados | Añádele`applinks:yourdomain.com`en Xcode, en **«Signing&Capabilities» (Capacidades de firma).** |
| Método delegado de la aplicación | Implementar`application(_:continue:restorationHandler:)`  para gestionar `NSUserActivity` |
| Configuración del SDK de Braze | Establecer `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (opcional) | Implementar`braze(_:shouldOpenURL:)`  para enrutamiento personalizado (por ejemplo, sucursal) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Si envías correos electrónicos a través de Braze, tu ESP (SendGrid, SparkPost o Amazon SES) envuelve los enlaces en un dominio de seguimiento de clics. Debes alojar el archivo AASA también en tu dominio de seguimiento de clics, no solo en tu dominio principal. Para obtener información sobre la configuración completa, consulta [Enlaces universales y Enlaces a aplicaciones]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).
{% endalert %}

### «Abrir URL Web dentro de la aplicación»

| Requisito | Detalles |
|---|---|
| Archivo AASA | No es necesario |
| Método delegado de la aplicación | No es necesario: el SDK se encarga de esto automáticamente. |
| Configuración del SDK de Braze | Ninguno: selecciona **Abrir URL Web dentro de la aplicación** en el compositor de campañas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cuando necesitas un archivo AASA {#when-aasa}

Solo se requiere un archivo de la Asociación de Sitios de Aplicaciones de Apple (AASA) cuando utilizas **enlaces universales**. Le indica a iOS qué URL puede manejar tu aplicación.

Necesitas un archivo AASA cuando:

- Envías vínculos profundos en campañas de correo electrónico (porque los ESP envuelven los vínculos en URL de seguimiento de clics HTTPS).
- Envías vínculos profundos en campañas SMS (porque los vínculos pueden acortarse a direcciones URL HTTPS).
- Utilizas Branch, Appsflyer u otro proveedor de enlaces (porque utilizan sus propios dominios HTTPS).
- Utilizas enlaces universales desde notificaciones push, mensajes dentro de la aplicación o tarjetas de contenido (menos habitual, pero posible con `forwardUniversalLinks = true`).

No necesitas un archivo AASA cuando:

- Solo utilizas vínculos profundos con esquema personalizado (por ejemplo, `myapp://`) desde notificaciones push, mensajes dentro de la aplicación o tarjetas de contenido.
- Utilizas la opción **Abrir URL Web dentro de la aplicación.**

Para obtener instrucciones sobre la configuración de AASA, consulta [Enlaces universales y Enlaces de aplicaciones]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#setting-up-universal-links-and-app-links).

## Cuando necesitas código de aplicación para gestionar enlaces {#when-app-code}

El método delegado que implementes dependerá del tipo de enlace que estés utilizando:

| Método delegado | Asas | Cuándo implementar |
|---|---|---|
| `application(_:open:options:)` | Vínculos profundos personalizados (`myapp://`) | Utilizas vínculos profundos personalizados desde cualquier canal. |
| `application(_:continue:restorationHandler:)` | Enlaces universales (`https://`) | Utilizas enlaces universales desde el correo electrónico, SMS o con `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | Todas las URL abiertas por el SDK | Necesitas una lógica de enrutamiento personalizada (por ejemplo, ramificación, gestión condicional, análisis). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Si utilizas un proveedor de enlaces externo como Branch, implementa`BrazeDelegate.braze(_:shouldOpenURL:)`  para interceptar las URL y reenviarlas al SDK del proveedor. Consulta [Branch para la vinculación en profundidad]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) para ver un ejemplo completo.
{% endalert %}

## Usar Branch con Braze {#branch}

Si utilizas [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) como proveedor de enlaces, tu configuración requiere algunos pasos adicionales más allá de la configuración estándar de enlaces universales:

1. **SDK de sucursal**: Integra el SDK de Branch siguiendo [la documentación de Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Dominios asociados**: Añade tu dominio Branch (por ejemplo, `applinks:yourapp.app.link`) en Xcode, en **Signing&  Capabilities** (Capacidades de firma).
3. **BrazeDelegate**: Implementa`braze(_:shouldOpenURL:)`  para redirigir los enlaces de Branch al SDK de Branch en lugar de dejar que Braze los gestione directamente.
4. **Reenviar enlaces universales**: Configúralo`configuration.forwardUniversalLinks = true`en tu configuración del SDK de Braze.

Para obtener detalles sobre la implementación y orientación sobre la depuración, consulta [Branch para la vinculación en profundidad]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/).