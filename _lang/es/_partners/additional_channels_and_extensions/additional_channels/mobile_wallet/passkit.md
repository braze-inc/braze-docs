---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "Este artículo de referencia describe la asociación entre Braze y Passkit. Esta asociación te habilita para ampliar tu alcance móvil integrando los pases de Apple Wallet y Google Pay en la experiencia de tus clientes."
page_type: partner
search_tag: Partner

---

# PassKit

> PassKit te habilita para ampliar tu alcance móvil integrando pases de Apple Wallet y Google Pay en la experiencia de tus clientes. Cree, gestione, distribuya y analice fácilmente el rendimiento de cupones digitales, tarjetas de fidelización, carnés de socio, entradas y mucho más; sin que sus clientes necesiten otra aplicación.

_Esta integración está mantenida por Passkit._

## Sobre la integración

La integración de Braze y PassKit le permite aumentar y medir el compromiso de sus campañas en línea mediante la entrega instantánea de pases personalizados de Apple Wallet y Google Pay. A continuación, puede analizar el uso y realizar ajustes en tiempo real para aumentar el tráfico en la tienda activando mensajes basados en la ubicación y actualizaciones personalizadas y dinámicas en el monedero móvil del cliente. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta PassKit | Necesitarás tener una cuenta PassKit y un administrador de cuentas PassKit. |
| `userDefinedID` | Para actualizar adecuadamente los eventos personalizados y los atributos personalizados de sus usuarios entre PassKit y Braze, deberá establecer el ID externo de Braze como `userDefinedID`. Este `userDefinedID` se utilizará cuando se hagan llamadas API a los puntos finales de PassKit. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

Para enriquecer aún más la experiencia de tus clientes con el monedero móvil, desde tu panel PassKit puedes optar por pasar datos a Braze a través del [punto final]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) Braze [`/users/track`.]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) 

Ejemplos de datos para compartir de PassKit incluyen:
- **Pase creado**: cuando un cliente hace clic en un enlace de pase y se le muestra por primera vez un pase.
- **Instalación del pase**: cuando el cliente añade y guarda el pase en su aplicación monedero.
- **Actualizaciones de pases**: cuando se actualiza un pase.
- **Eliminación del pase**: cuando un cliente elimina el pase de su aplicación monedero.

Una vez introducidos los datos en Braze, puede crear audiencias, personalizar el contenido mediante Liquid y activar campañas o Canvases después de que se hayan realizado estas acciones.

## Conectar Passkit a Braze

Para pasar datos desde PassKit, asegúrese de que ha configurado su ID externo Braze como `externalId` de PassKit.

1. Dentro de **Ajustes**, en **Integraciones** en su proyecto o programa PassKit pass haga clic en **Conectar** en la pestaña **Braze**.<br>![La ficha de integración de Braze en la plataforma PassKit.]({% image_buster /assets/img/passkit/passkit5.png %}){: style="max-width:80%"}<br><br>
2. Introduce tu clave de API Braze, la URL del punto final y un nombre para tu conector.<br><br>
3. Active **Activar integración** y los eventos que desee en Braze para activar o personalizar sus mensajes.<br>![El mosaico de integración de PassKit Braze se amplió para aceptar la clave de API, la URL del punto final, el nombre de la integración, la configuración de habilitación, la configuración de la afiliación y la configuración del pase.]({% image_buster /assets/img/passkit/passkit4.png %}){: style="max-width:70%"}

## Crear pase utilizando un enlace SmartPass

Dentro de Braze, puedes configurar un enlace SmartPass para generar una URL única para que tus clientes instalen su pase en Android o iOS. Para ello, debe definir una carga útil de datos SmartPass cifrada que se pueda llamar desde un bloque de contenido Braze. Este [bloque de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) puede reutilizarse para futuros pases y cupones. Durante su integración se utilizará lo siguiente:

- **URL PassKit**: Tu URL PassKit es una URL única para tu programa PassKit.<br>Cada programa tiene una URL única, y puede encontrarla en la pestaña **Distribución** de su programa o proyecto PassKit. (por ejemplo, https://pub1.pskt.io/c/ww0jir)<br><br>
- **Secreto PassKit**: Junto con la URL, necesitarás tener a mano la Clave PassKit de este programa.<br>Se encuentra en la misma página que la URL de tu PassKit.<br><br>
- **ID del programa (o proyecto)**: Tu ID del Programa PassKit será necesario para crear la URL del SmartPass. <br>Puede encontrarlo en la pestaña **Configuración** de su proyecto o programa.

Para más información sobre la creación de enlaces SmartPass encriptados, consulta este [artículo de PassKit](https://help.passkit.com/en/articles/3742778-hashed-smartpass-links).

### Paso 1: Define la carga útil de los datos de tu pase {#passkit-integrations}

En primer lugar, debe definir la carga útil del cupón o del miembro. 

Hay muchos componentes diferentes que puede incluir en su carga útil, pero aquí como dos importantes a tener en cuenta:

| Componente | Obligatoria | Tipo | Descripción |
| --------- | -------- | ---- | ----------- |
|`person.externalId` | Obligatoria | Cadena | Establecido como el ID externo de Braze, es crucial para que funcionen las devoluciones de llamada de PassKit a Braze, permitiendo a los usuarios de Braze tener cupones para múltiples ofertas en una campaña. No se aplica como único. |
| `members.member.externalId` | Opcional | Cadena | Establecido como ID externo de Braze, puedes utilizar tu ID externo para actualizar el pase de socio. La configuración de este campo hace que el usuario sea único dentro del programa de afiliación.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Para obtener una lista completa de los campos disponibles, sus tipos y descripciones útiles, echa un vistazo a la [documentación de PassKit en GitHub](https://github.com/PassKit/smart-pass-link-from-csv-generator).

#### Ejemplo de carga útil
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### Paso 2: Crear y codificar una variable de carga útil indefinida

Para crear y nombrar un nuevo bloque de contenido, vaya a **Plantillas** > **Bloques de contenido** en el panel de control de Braze.

Seleccione **Crear bloque de contenido** para empezar.

A continuación, debe definir su **Etiqueta líquida de bloque de contenido**. Después de guardar este bloque de contenido, se puede hacer referencia a esta etiqueta Liquid al redactar mensajes. En este ejemplo, hemos asignado la etiqueta de Liquid como {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}. 

Dentro de este bloque de contenido, no incluiremos directamente la carga útil, sino que la referenciaremos en una variable {% raw %}`{{passData}}`{% endraw %}. El primer fragmento de código que debe añadir a su bloque de contenido captura una codificación Base64 de la variable {% raw %}`{{passData}}`{% endraw %}.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### Paso 3: Crea tu firma de encriptación utilizando un hash SHA1 HMAC

A continuación, crearás tu firma de encriptación utilizando un hash [SHA1 HMAC](https://en.wikipedia.org/wiki/HMAC) de la URL del proyecto y de la carga útil. 

El segundo fragmento de código que debe añadir a su bloque de contenido captura la URL que se utilizará para el hash.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

A continuación, debes generar una firma utilizando este hash y tu `Project Secret`. Esto puede hacerse incluyendo un tercer fragmento de código:
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

Por último, añada la firma a la URL completa utilizando el quinto fragmento de código:
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### Paso 4: Imprime tu URL

Por último, asegúrate de llamar a tu URL final para que imprima la URL de tu SmartPass dentro de tu mensaje.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

Llegados a este punto, habrá creado un Bloque de Contenido con el siguiente aspecto:

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

En este ejemplo, se han añadido parámetros UTM para rastrear el origen de estas instalaciones hasta Braze y esta campaña.

{% alert tip %}
Recuerde guardar su Bloque de Contenido antes de salir de la página.
{% endalert %}

### Paso 5: Ponerlo todo junto

Una vez realizado este Bloque de contenido, se puede reutilizar de nuevo en el futuro. 

Puede observar que hay dos variables sin definir en el bloque de contenido de ejemplo.<br> 
{% raw %}`{{passData}}`{% endraw %} - Su carga útil de datos de paso JSON definida en [el paso 1](#passkit-integrations) <br>
{% raw %}`{{projectUrl}}`{% endraw %} - La URL de tu proyecto o programa que encontrarás en la pestaña de distribución de tu proyecto Passkit.

Esta decisión es intencionada y favorece la reutilización del Bloque de Contenidos. Dado que estas variables sólo se referencian, no se crean dentro del bloque de contenido, estas variables pueden cambiar sin tener que rehacer el bloque de contenido. 

Por ejemplo, quizá quieras cambiar la oferta introductoria para incluir más puntos iniciales en tu programa de fidelización, o quizá quieras crear una tarjeta de socio secundaria o un cupón. Estos escenarios requerirían diferentes Passkit `projectURLs` o diferentes cargas útiles de paso, que definirías por campaña en Braze.  

#### Componer el cuerpo del mensaje

Querrá capturar ambas variables en el cuerpo del mensaje y luego llamar a su Bloque de Contenido.
Captura la carga útil JSON minificada del [paso 1](#passkit-integrations):

**Asignar la URL del proyecto**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**Captura el JSON**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**Haga referencia al bloque de contenido que acaba de crear**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

El cuerpo del mensaje debe ser similar al siguiente
![Una imagen del creador de mensajes del bloque de contenido con el JSON capturado y la referencia del bloque de contenido mostrada.]({% image_buster /assets/img/passkit/passkit1.png %}){: style="max-width:70%"}

La URL de salida de la muestra es:
![La URL de salida que incluye una cadena larga de letras y números generada aleatoriamente.]({% image_buster /assets/img/passkit/passkit2.png %}){: style="max-width:70%"}

La URL de salida será larga. La razón es que contiene todos los datos de paso e incorpora la mejor seguridad de su clase para garantizar la integridad de los datos y que no se alteren mediante la modificación de la URL. Si utilizas SMS para distribuir esta URL, tal vez quieras pasarla por un proceso de acortamiento de enlaces como [bit.ly](https://dev.bitly.com/v4/#operation/createFullBitlink). Esto puede hacerse mediante una llamada de Contenido conectado a un punto final de bit.ly.

## Actualiza el pase utilizando el webhook PassKit

Dentro de Braze, puede configurar una campaña de webhook o un webhook dentro de un Canvas para actualizar un pase existente basado en el comportamiento de su usuario. Consulta los siguientes enlaces para obtener información sobre puntos finales PassKit útiles. 
- [Proyectos miembros](https://docs.passkit.io/protocols/member/)
- [Proyectos de cupones](https://docs.passkit.io/protocols/coupon/)
- [Proyectos de vuelos](https://docs.passkit.io/protocols/boarding/)

### Parámetros de la carga útil

Antes de empezar, aquí están los parámetros de carga útil JSON comunes que puede incluir dentro de sus webhooks de creación y actualización a PassKit.

| Datos | Tipo | Descripción |
| ---- | ---- | ----------- |
| `externalId` | Cadena | Permite añadir un Id único al registro de pases para proporcionar compatibilidad con un sistema existente que utilice identificadores de cliente únicos (por ejemplo, números de socio). Puedes recuperar los datos del pase utilizando este punto final a través de `userDefinedId` y `campaignName` en lugar del ID del pase. Este valor debe ser único dentro de una campaña y, una vez establecido, no puede modificarse.<br><br>Para la integración con Braze, te recomendamos que utilices el ID externo de Braze: {% raw %}`{{${user_id}}}`{% endraw %} |
| `campaignId` (cupón) <br><br> `programId` (afiliación) | Cadena | El ID de la plantilla de campaña o programa que creó en PassKit. Para ello, dirígete a la pestaña **Configuración** de tu proyecto PassKit pass. |
| `expiryDate` | IO8601 fecha y hora | La fecha de caducidad del pase. Después de la fecha de caducidad, el pase se anula automáticamente (consulta `isVoided`). Este valor anulará el valor de la plantilla y de la fecha de finalización de la campaña. |
| `status` | Cadena | El estado actual de un cupón, como `REDEEMED` o `UNREDEEMED`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paso 1: Cree su plantilla de webhook Braze

Para crear una plantilla de webhook PassKit y utilizarla en futuras campañas o lienzos, vaya a la sección **Plantillas y medios** del panel de control de Braze. Si desea crear una campaña única de webhook PassKit o utilizar una plantilla existente, seleccione **Webhook** en Braze al crear una nueva campaña.

Una vez que haya seleccionado la plantilla de webhook PassKit, debería ver lo siguiente:
- **URL del webhook**: `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **Cuerpo de la solicitud**: Texto sin procesar

#### Encabezados de solicitud y método

PassKit requiere un `HTTP Header` para la autorización que incluya tu clave de API de PassKit codificada en base 64. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Configuración**, debe sustituir el `<PASSKIT_LONG_LIVED_TOKEN>` por su token PassKit. Para recuperar tu token, navega a tu proyecto/programa PassKit, ve a **Configuración > Integraciones > Token de larga duración**.

{% raw %}
- **Método HTTP**: PUT
- **Encabezado de solicitud**:
  - **Autorización**: Portador `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud

Para configurar el webhook, rellene los detalles del nuevo evento en el cuerpo de la solicitud, incluidos los parámetros de carga útil necesarios para su caso de uso:

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### Paso 2: Vista previa de su solicitud

El texto en bruto se resaltará automáticamente si se trata de una etiqueta Braze aplicable. 

Previsualiza tu solicitud en el panel de **Previsualización** o navega a la pestaña de **Prueba**, donde puedes seleccionar un usuario al azar, un usuario existente, o personalizar el tuyo propio para probar tu webhook.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas webhook actualizadas pueden encontrarse en la lista **Plantillas webhook guardadas** al crear una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

## Recuperar detalles del pase a través de Contenido conectado

Además de crear y actualizar pases, también puedes recuperar los metadatos de los pases de tus usuarios mediante [el contenido conectado de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) Braze para incorporar detalles personalizados de los pases en tus campañas de mensajería.

**Llamada al contenido conectado de PassKit**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

**Ejemplo de respuestas de Liquid**

{% tabs local %}
{% tab pasa redemptionDetails %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab pasa el estado %}
```
UNREDEEMED 
```
{% endtab %}
{% endtabs %}


