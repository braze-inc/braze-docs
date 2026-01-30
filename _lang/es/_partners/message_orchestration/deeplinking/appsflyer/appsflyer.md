---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "Este artículo de referencia describe la asociación entre Braze y AppsFlyer, una plataforma de análisis y atribución de marketing móvil que le ayuda a analizar y optimizar sus aplicaciones."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> [AppsFlyer](https://www.appsflyer.com/) es una plataforma de análisis y atribución de marketing móvil que te ayuda a analizar y optimizar tus aplicaciones mediante análisis de marketing, atribución móvil y vinculación en profundidad.

La integración de Braze y AppsFlyer le permite comprender mejor cómo optimizar y crear campañas más holísticas aprovechando los datos de atribución de instalaciones móviles de AppsFlyer. 

También puede pasar sus audiencias (cohortes) de AppsFlyer directamente a Braze con la integración [AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences/), lo que le permite crear potentes campañas de captación de clientes dirigidas a los usuarios adecuados en el momento oportuno. 

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta AppsFlyer | Se necesita una cuenta AppsFlyer para beneficiarse de esta asociación. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de su plataforma, es posible que se requieran fragmentos de código en su aplicación. Encontrará más detalles sobre estos requisitos en el paso 1 del proceso de integración. |
| SDK de AppsFlyer | Además del SDK de Braze necesario, debes instalar el [SDK de AppsFlyer](https://dev.appsflyer.com/hc/docs/getting-started).
| Configuración completa del dominio de correo electrónico | Debe haber completado el [paso de configuración de IP y dominio]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) para configurar su correo electrónico durante la incorporación a Braze. |
| Certificado SSL | Su [certificado SSL]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate) debe estar configurado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Mapear ID de dispositivo

{% tabs local %}
{% tab Android %}
Si tienes una aplicación Android, debes pasar un ID de dispositivo Braze único a AppsFlyer. 

Asegúrate de que las siguientes líneas de código se insertan en el lugar correcto: después de iniciar el SDK de Braze y antes del código de inicialización del SDK de AppsFlyer. Consulta [la guía de integración de Android SDK](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) de AppsFlyer para obtener más información.

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
Antes de febrero de 2023, nuestra integración de atribución de AppsFlyer utilizaba el Identificador de Vendedor (IDFV) como identificador principal para cotejar los datos de atribución de iOS. No es necesario que los clientes de Braze que utilicen Objective-C obtengan la dirección Braze `device_id` y la envíen a AppsFlyer al instalarla, porque no se interrumpe el servicio.
{% endalert%}

Para los que utilicen el SDK Swift v5.7.0+, si quieres seguir utilizando IDFV como identificador mutuo, debes confirmar que el campo `useUUIDAsDeviceId` está configurado en `false` para evitar una interrupción de la integración. 

Si se establece en `true`, debes implementar el mapeado de ID de dispositivo iOS para Swift con el fin de pasar el `device_id` de Braze a AppsFlyer al instalar la aplicación para que Braze coincida adecuadamente con las atribuciones de iOS.

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab unity %}
Para mapear el ID del dispositivo en Unity, utiliza lo siguiente:

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### Paso 2: Obtener la clave de importación de datos Braze

En Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y seleccione **AppsFlyer**. 

Aquí encontrarás el punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puede crear una nueva o invalidar una existente. La clave de importación de datos y el endpoint REST se utilizan en el siguiente paso cuando se configura un postback en el dashboard de AppsFlyer.<br><br>![El cuadro "Importación de datos para la atribución de instalaciones" disponible en la página Tecnología de AppsFlyer. En este cuadro se incluye la clave de importación de datos y el punto final REST.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### Paso 3: Configurar Braze en el panel de AppsFlyer

1. En AppsFlyer, vaya a la página de **socios integrados** en la barra de la izquierda. A continuación, busca **Braze** y selecciona el logotipo de Braze para abrir una ventana de configuración.
2. Dentro de la pestaña **Integración**, active **Activar socio**.
3. Proporciona la clave de importación de datos y el punto final REST que encontraste en el panel Braze. 
4. Desactive la **privacidad avanzada** y guarde la configuración.

Encontrarás información adicional sobre estas instrucciones en [la documentación de AppsFlyer.](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration)

### Paso 4: Confirmar la integración

Después de que Braze reciba los datos de atribución de AppsFlyer, el indicador de estado de la conexión en la página de socios tecnológicos de AppsFlyer en Braze cambia de "No conectado" a "Conectado" e incluye una marca de tiempo de la última solicitud realizada con éxito.

Este estado sólo cambia cuando Braze recibe datos sobre una instalación atribuida. Braze ignora las instalaciones orgánicas (las excluye del postback de AppsFlyer) y no las cuenta a la hora de determinar si la conexión se ha realizado correctamente.

### Paso 5: Visualización de los datos de atribución de los usuarios

#### Campos de datos disponibles

Si la integración se ha realizado correctamente, Braze mapea todos los datos de instalación no orgánicos en filtros de segmento.

| Campo de datos de AppsFlyer | Filtro de segmento de soldadura |
| -------------------- | --------------------- |
| `media_source` | Fuente atribuida |
| `campaign` | Campaña atribuida |
| `af_adset` | Grupo de anuncios atribuidos |
| `af_ad` | Anuncio atribuido |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Puedes segmentar tu base de usuarios por datos de atribución en el panel de Braze utilizando los filtros de atribución de instalación.

![Cuatro filtros disponibles. La primera es "Fuente de atribución de instalación es network_val_0". La segunda es "Fuente de atribución de instalación es campaign_val_0". La tercera es "Fuente de atribución de instalación es adgroup_val_0". La cuarta es "Fuente de atribución de instalación es creative_val_0". Junto a los filtros enumerados, puedes ver cómo se añadirán estas fuentes de atribución al perfil de usuario. En el cuadro "Atribución de instalación" de la página de información de un usuario, la fuente de instalación aparece como network_val_0, y la campaña como campaign_val_0,, etc.]({% image_buster /assets/img/braze_attribution.png %})

Además, los datos de atribución de un usuario concreto están disponibles en el perfil de cada usuario en el panel Braze.

{% alert note %}
Los datos de atribución de las campañas de Facebook y X (antes Twitter) no están disponibles a través de nuestros socios. Estas fuentes de medios no permiten a sus socios compartir datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.
{% endalert %}

## Integra AppsFlyer con Braze para una vinculación en profundidad

Los enlaces profundos -enlaces que dirigen a los usuarios a una página o lugar específicos dentro de una aplicación o sitio web- se utilizan para crear una experiencia de usuario personalizada. 

Aunque su uso está muy extendido, pueden surgir problemas al utilizar enlaces profundos por correo electrónico con seguimiento de clics#8212otra característica importante utilizada en la recopilación de datos de usuario. Estos problemas se deben a que los proveedores de servicios de correo electrónico (ESP) envuelven los vínculos profundos en un dominio de registro de clics, rompiendo el vínculo original. Por lo tanto, la compatibilidad con los vínculos profundos requiere una configuración adicional.

AppsFlyer proporciona un [servicio](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer) que evita estos problemas, habilitando a AppsFlyer para que actúe como intermediario entre el servidor ESP y tu dominio.  Su función como proxy habilita el suministro de archivos de asociación (AASA/vínculos activos), lo que facilita la vinculación en profundidad. 

## Paso 1 - Crear un dominio de seguimiento de clics 

Siguiendo los elementos iniciales de [la guía de configuración de correo electrónico de Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate), crea un dominio de envío de correo electrónico y un dominio de seguimiento de clics. Para obtener asistencia, puedes crear un ticket a través del panel de Braze para iniciar la configuración del nuevo CTD con el equipo de correo electrónico de Braze.

![La interfaz de usuario de Braze muestra el botón "Obtener ayuda", que se encuentra debajo del botón "Soporte" en la esquina superior derecha]({% image_buster /assets/img/attribution/appsflyer/1.png %})

Es obligatorio crear un nuevo CTD, aunque ya utilices uno existente. Esto garantiza que no haya ningún impacto en el tráfico de las campañas de correo electrónico en vivo actuales. 

{% alert important%}
AppsFlyers crea el certificado SSL. En esta fase, es probable que los enlaces de correo electrónico no sean seguros, es decir, que el prefijo de la URL sea HTTP en lugar de HTTPS. Esto se resuelve en pasos posteriores.	
{%endalert%}

## Paso 2 - Crear una plantilla OneLink en AppsFlyer
Crea una [plantilla OneLink](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures) y configura Enlaces universales/Enlaces de aplicación en "Cuando se instale la aplicación". Esta plantilla se utiliza posteriormente para crear enlaces OneLink para tus campañas de correo electrónico.

{% alert note%} Si ya tienes configurada una plantilla OneLink que habilita los Enlaces Universales/Enlaces de Aplicaciones, puedes utilizarla.
{%endalert%}

## Paso 3 - Configura tu integración Braze en Appsflyer
Ahora es el momento de configurar tu integración Braze en AppsFlyer. Este paso y el siguiente ("Configura tu aplicación") pueden configurarse al mismo tiempo.
Para configurar tu integración Braze en AppsFlyer:

### 1\. En AppsFlyer, en el menú lateral, selecciona Interacción > Integración ESP.
![La interfaz de usuario de Appsflyer muestra el botón "Integración ESP", que se encuentra en el menú de la izquierda]({% image_buster /assets/img/attribution/appsflyer/2.png %})

 
### 2\. Selecciona Braze.
![La interfaz de usuario de Appsflyer muestra la lista de integraciones ESP, incluida Braze.]({% image_buster /assets/img/attribution/appsflyer/3.png %})

 
### 3\. Selecciona la plantilla de OneLink que deseas utilizar para las campañas de correo electrónico y, a continuación, haz clic en Siguiente.
![La interfaz de usuario de Appsflyer muestra el menú desplegable que permite a los usuarios seleccionar su plantilla.]({% image_buster /assets/img/attribution/appsflyer/4.png %})

 
### 4\. Introduce tu dominio de seguimiento de clics y el valor "Braze endpoint", que se proporcionó con el nuevo CTD creado en el paso 1, y luego haz clic en Validar conexión.

Esto valida que el dominio de seguimiento de clics apunta al punto final que has introducido.

![La interfaz de usuario de Appsflyer resalta dónde los clientes deben añadir su dominio de seguimiento de clics y los detalles asociados.]({% image_buster /assets/img/attribution/appsflyer/5.png %})

Con "Braze Endpoint", AppsFlyer está pidiendo los detalles proporcionados por Braze en el Paso 1 de esta guía, concretamente el nuevo CTD. 

A continuación, haz clic en **Validar conexión**, que valida que el dominio de seguimiento de clics apunta al punto final que has introducido.
Cuando hayas terminado, haz clic en **Siguiente**.

### 5\. Dirige el tráfico de enlace a Appsflyer:

#### a. Copia y envía las instrucciones personalizadas prefabricadas en AppsFlyer a tu administrador de TI o de dominio. 

Tu administrador debe redirigir el tráfico de tu campaña de correo electrónico desde los servidores ESP a los servidores de AppsFlyer actualizando tus registros de DNS CNAME con el nuevo dominio que AppsFlyer te ha proporcionado.

Como resultado, cada vez que se hace clic en un enlace, el clic se redirige a AppsFlyer, que a su vez lo redirige al punto final ESP.

![Diagrama que ilustra cómo los datos de los clics pasan de tu dominio, a AppsFlyer, a tu esp endpoint]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. Después de copiar y enviar las instrucciones, haz clic en Listo.
Se ha creado tu integración Braze.

{%alert important%}
El estado de tu integración Braze es pendiente y sólo empezará a funcionar una vez mapeado el registro CNAME. Una nueva integración puede tardar hasta 24 horas después de ser mapeada en empezar a funcionar y activarse.
{%endalert%}

## Paso 4: Configura tu aplicación (Tarea del desarrollador)
Appsflyer [ofrece orientación](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task) sobre la correcta configuración de la aplicación, que deben seguir tus equipos web o de aplicaciones para soportar el enlace universal. 

## Paso 5: Confirma que el seguimiento de clics SSL está habilitado con Braze

En esta fase, después de compartir y validar los detalles del CTD en Appsflyer, te recomendamos que realices un envío de prueba para confirmar si tu dominio de envío Onelink tiene un certificado SSL. Esto se ajusta a nuestra guía de [configuración del correo electrónico](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate).

Puedes realizar la garantía de calidad y la solución de problemas enviando un vínculo profundo mediante OneLink. Consulte la [documentación de AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) para más detalles sobre el uso de OneLink.

Si los enlaces CTD se identifican como HTTP, ponte en contacto con el equipo de operaciones de correo electrónico de Braze para habilitar el seguimiento de clics SSL. Esto garantiza que todos los enlaces HTTP se conviertan automáticamente a HTTPS.
Puedes utilizar el siguiente ejemplo de texto de mensaje cuando te pongas en contacto con tu administrador del éxito del cliente, o volviendo a crear un ticket en el panel de Braze, como en el paso 1: 

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS. 
```

### URL de seguimiento de clics de AppsFlyer en Braze (opcional)

Puede utilizar los [enlaces de atribución OneLink](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) de AppsFlyer en campañas Braze a través de push, correo electrónico y más. Esto te permite enviar datos de atribución de instalación o reactivación de la interacción de tus campañas Braze a AppsFlyer. Como resultado, podrás medir tus esfuerzos de marketing con mayor eficacia y tomar decisiones basadas en datos.

Puede simplemente crear su URL de seguimiento OneLink en AppsFlyer e insertarla directamente en sus campañas Braze. AppsFlyer utiliza entonces sus [metodologías de atribución probabilística](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) para atribuir al usuario que ha hecho clic en el enlace. Le recomendamos que añada a sus enlaces de seguimiento de AppsFlyer un identificador de dispositivo para mejorar la precisión de las atribuciones de sus campañas Braze. Esto atribuye de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs local %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). La integración de SDK de AppsFlyer también recoge el GAID. Puedes incluir el GAID en tus enlaces de seguimiento de clics de AppsFlyer utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como AppsFlyer recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones SDK. Puedes utilizar el IDFC como identificador del dispositivo. Puedes incluir el IDFV en tus enlaces de seguimiento de clics de AppsFlyer utilizando la siguiente lógica de Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}
