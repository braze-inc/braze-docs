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

> AppsFlyer es una plataforma de atribución y análisis de marketing móvil que te ayuda a analizar y optimizar tus aplicaciones a través de estrategias de análisis de marketing, atribución móvil y vinculación en profundidad.

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
Si tienes una aplicación Android, tendrás que pasar un ID de dispositivo Braze único a AppsFlyer. 

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
Antes de febrero de 2023, nuestra integración de atribución de AppsFlyer utilizaba el IDFV como identificador principal para cotejar los datos de atribución de iOS. No es necesario que los clientes de Braze que utilicen Objective-C obtengan el Braze `device_id` y lo envíen a AppsFlyer al instalarlo, ya que no habrá interrupción del servicio.
{% endalert%}

Para los que utilicen el SDK Swift v5.7.0+, si deseas seguir utilizando IDFV como identificador mutuo, debes confirmar que el campo `useUUIDAsDeviceId` está configurado en `false` para que no se interrumpa la integración. 

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

{% tab Unity %}
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

Aquí encontrarás el punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puede crear una nueva o invalidar una existente. La clave de importación de datos y el endpoint REST se utilizan en el siguiente paso cuando se configura un postback en el dashboard de AppsFlyer.<br><br>![El cuadro "Importación de datos para la atribución de instalaciones" disponible en la página Tecnología de AppsFlyer. En esta casilla se incluye la clave de importación de datos y el punto final REST.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### Paso 3: Configurar Braze en el panel de AppsFlyer

1. En AppsFlyer, vaya a la página de **socios integrados** en la barra de la izquierda. A continuación, busca **Braze** y selecciona el logotipo de Braze para abrir una ventana de configuración.
2. Dentro de la pestaña **Integración**, active **Activar socio**.
3. Proporciona la clave de importación de datos y el punto final REST que encontraste en el panel Braze. 
4. Desactive la **privacidad avanzada** y guarde la configuración.

Encontrarás información adicional sobre estas instrucciones en [la documentación de AppsFlyer.](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration)

### Paso 4: Confirmar la integración

Una vez que Braze reciba los datos de atribución de AppsFlyer, el indicador de estado de la conexión en la página de socios tecnológicos de AppsFlyer en Braze cambiará de "No conectado" a "Conectado". También se incluirá una marca de tiempo de la última solicitud realizada con éxito. 

Ten en cuenta que esto no ocurrirá hasta que recibamos datos sobre una instalación atribuida. Las instalaciones orgánicas, que deberían excluirse del postback de AppsFlyer, son ignoradas por nuestra API y no se tienen en cuenta a la hora de determinar si se ha establecido una conexión correcta.

### Paso 5: Visualización de los datos de atribución de los usuarios

#### Campos de datos disponibles

Suponiendo que configure su integración como se sugiere, Braze asignará todos los datos de instalación no orgánicos a filtros de segmento.

| Campo de datos de AppsFlyer | Filtro de segmento de soldadura |
| -------------------- | --------------------- |
| `media_source` | Fuente atribuida |
| `campaign` | Campaña atribuida |
| `af_adset` | Grupo de anuncios atribuidos |
| `af_ad` | Anuncio atribuido |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Su base de usuarios puede segmentarse por datos de atribución en el cuadro de mandos de Braze utilizando los filtros Instalar atribución.

![Cuatro filtros disponibles. El primero es "La fuente de atribución de instalación es network_val_0". La segunda es "Instalar fuente de atribución es campaign_val_0". La tercera es "Instalar fuente de atribución es adgroup_val_0". La cuarta es "Instalar fuente de atribución es creative_val_0". Junto a los filtros enumerados, puede ver cómo se añadirán estas fuentes de atribución al perfil del usuario. En el cuadro "Atribución de instalación" de la página de información de un usuario, la fuente de instalación aparece como network_val_0, la campaña aparece como campaign_val_0, etc.]({% image_buster /assets/img/braze_attribution.png %})

Además, los datos de atribución de un usuario concreto están disponibles en el perfil de cada usuario en el panel Braze.

{% alert note %}
Los datos de atribución de las campañas de Facebook y X (antes Twitter) no están disponibles a través de nuestros socios. Estas fuentes de medios no permiten a sus socios compartir datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.
{% endalert %}

## Integrar AppsFlyer con un proveedor de servicios de correo electrónico para crear enlaces profundos

AppsFlyer se integra con SendGrid y SparkPost como proveedores de servicios de correo electrónico (ESP) para admitir enlaces profundos y seguimiento de clics. Siga las instrucciones siguientes para integrarse con el ESP de su elección.

{% alert tip %}
Los enlaces profundos -enlaces que dirigen a los usuarios a una página o lugar específicos dentro de una aplicación o sitio web- se utilizan para crear una experiencia de usuario personalizada. Aunque su uso está muy extendido, pueden surgir problemas al utilizar enlaces profundos enviados por correo electrónico con el seguimiento de clics, otra característica importante utilizada para recopilar datos de los usuarios. Estos problemas se deben a que los ESP envuelven los enlaces profundos en un dominio de registro de clics, rompiendo el enlace original. Por lo tanto, la compatibilidad con los vínculos profundos requiere una configuración adicional. Si integra AppsFlyer con SendGrid o SparkPost, evitará estos problemas. Más información sobre este tema en [Enlaces universales y Enlaces de aplicaciones]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).
{% endalert %}

### Paso 1: Configurar OneLink en AppsFlyer

1. En AppsFlyer, seleccione una plantilla OneLink para sus campañas de correo electrónico. Asegúrese de que la plantilla admite enlaces universales (iOS) o App Links (Android). 
2. Configura tu aplicación para que admita la vinculación en profundidad con OneLink. Consulte la [documentación de AppsFlyer](https://dev.appsflyer.com/hc/docs/dl_work_flow#initial-setup) para obtener más información sobre cómo configurar su aplicación para que sea compatible con OneLink.

### Paso 2: Configura tu aplicación para que admita enlaces universales y App Links

El sistema operativo del dispositivo permite que los enlaces universales (iOS) o los enlaces a aplicaciones (Android) abran una aplicación específica al pulsarlos.

Realice los siguientes pasos para admitir enlaces universales y App Links.

{% tabs local %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
Configure el alojamiento de archivos de la Apple App Site Association (AASA) para habilitar enlaces universales en sus correos electrónicos.

1. Obtenga un expediente AASA por uno de los métodos siguientes:
    * Si ha configurado OneLink con enlaces universales, es posible que ya tenga un archivo AASA asociado a OneLink. Para obtener el archivo AASA, realice lo siguiente:
        * Copie el subdominio OneLink de su plantilla OneLink. Asegúrese de que la plantilla admite enlaces universales.
        * Péguelo en lugar del marcador de posición en la siguiente URL: `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * Para descargar el archivo AASA, pegue la URL de OneLink en la barra de direcciones de su navegador y pulse **Intro**. El archivo se descargará en su ordenador y podrá abrirlo y ver su contenido con cualquier editor de texto.
    * [La guía de Apple sobre enlaces universales](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) explica cómo crear el archivo AASA.
2. Aloje el archivo AASA en su servidor de dominio de grabación de clics. El archivo debe alojarse en la ruta: `click.example.com/.well-known/apple-app-site-association`. 

Consulte la [documentación de SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links) para saber cómo configurar el archivo AASA para SendGrid y configurar los servicios CDN para alojar el archivo AASA.

{% alert important %}
Una vez alojado el archivo AASA, cualquier cambio en la configuración de OneLink (modificación o sustitución) requiere la generación de un nuevo archivo AASA.
{% endalert %}
{% endsubtab %}
{% subtab Android %}
Configura el alojamiento de archivos de Enlaces a Activos Digitales para habilitar los Enlaces a Aplicaciones en tus correos electrónicos.

1. Obtenga un archivo de enlaces de activos digitales mediante uno de los siguientes métodos:
    * Si has configurado OneLink con App Links, es posible que ya tengas un archivo Digital Asset Links asociado a OneLink. Para obtener el archivo, realice lo siguiente:
        * Copie el subdominio OneLink de su plantilla OneLink. Asegúrese de que la plantilla es compatible con App Links.
        * Añada `/.well-known/assetlinks.json` al final de la URL de OneLink.
        * Para descargar el archivo Digital Asset Links, pegue la URL de OneLink en la barra de direcciones de su navegador y pulse **Intro**. Por ejemplo, `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. El archivo se descargará en su ordenador y podrá abrirlo y ver su contenido con cualquier editor de texto.
    * [La guía de Android sobre Enlaces de Aplicaciones](https://developer.android.com/studio/write/app-link-indexing) explica cómo crear el archivo de Enlaces de Activos Digitales.
2. Aloja el archivo de enlaces de activos digitales en tu servidor de dominio de grabación de clics. El archivo debe alojarse en la ruta: `click.example.com/.well-known/apple-app-site-association`.

Consulta la [documentación de SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links) para saber cómo configurar el archivo de enlaces de activos digitales para SendGrid y configurar los servicios de CDN para alojar el archivo de enlaces de activos digitales.

{% alert important %}
Una vez alojado el archivo Digital Asset Links, cualquier cambio en la configuración de OneLink (modificación o sustitución) requiere la generación de un nuevo archivo.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### Paso 2a: Configurar el alojamiento de archivos de AASA
Configure el alojamiento de archivos de la Apple App Site Association (AASA) para habilitar enlaces universales en sus correos electrónicos.

1. Obtenga un expediente AASA por uno de los métodos siguientes:
    * Si ha configurado OneLink con enlaces universales, es posible que ya tenga un archivo AASA asociado a OneLink. Para obtener el archivo AASA, realice lo siguiente:
        * Copie el subdominio OneLink de su plantilla OneLink. Asegúrese de que la plantilla admite enlaces universales.
        * Péguelo en lugar del marcador de posición en la siguiente URL: `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * Para descargar el archivo AASA, pegue la URL de OneLink en la barra de direcciones de su navegador y pulse **Intro**. El archivo se descargará en su ordenador y podrá abrirlo y ver su contenido con cualquier editor de texto.
    * [La guía de Apple sobre enlaces universales](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) explica cómo crear el archivo AASA.
2. Aloje el archivo AASA en su servidor de dominio de grabación de clics. El archivo debe alojarse en la ruta: `click.example.com/.well-known/apple-app-site-association`. 

Consulte la [documentación de SparkPost](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) para saber cómo configurar el archivo AASA para SparkPost y establecer sub-rutas de enlace personalizadas.

{% alert important %}
Una vez alojado el archivo AASA, cualquier cambio en la configuración de OneLink (modificación o sustitución) requiere la generación de un nuevo archivo AASA.
{% endalert %}

#### Paso 2b: Redirige tu dominio de seguimiento de clics a tu host de archivos de AASA
Durante la [configuración de su correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/), creó un registro CNAME en su servidor DNS. Realice los siguientes pasos después de verificar su dominio de seguimiento de clics en Braze. 

1. Elimine el registro CNAME que redirige su subdominio al dominio SparkPost.
2. Cree un registro CNAME que redirija su dominio de seguimiento de clics a la CDN que aloja el archivo AASA de su aplicación, en lugar del registro que eliminó anteriormente.
{% endsubtab %}
{% subtab Android %}
#### Paso 2a: Configurar el alojamiento de archivos de Digital Asset Links
Configura el alojamiento de archivos de Enlaces a Activos Digitales para habilitar los Enlaces a Aplicaciones en tus correos electrónicos.

1. Obtenga un archivo de enlaces de activos digitales mediante uno de los siguientes métodos:
    * Si has configurado OneLink con App Links, es posible que ya tengas un archivo Digital Asset Links asociado a OneLink. Para obtener el archivo, realice lo siguiente:
        * Copie el subdominio OneLink de su plantilla OneLink. Asegúrese de que la plantilla es compatible con App Links.
        * Añada `/.well-known/assetlinks.json` al final de la URL de OneLink.
        * Para descargar el archivo Digital Asset Links, pegue la URL de OneLink en la barra de direcciones de su navegador y pulse **Intro**. Por ejemplo, `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. El archivo se descargará en su ordenador y podrá abrirlo y ver su contenido con cualquier editor de texto.
    * [La guía de Android sobre Enlaces de Aplicaciones](https://developer.android.com/studio/write/app-link-indexing) explica cómo crear el archivo de Enlaces de Activos Digitales.
2. Aloja el archivo de enlaces de activos digitales en tu servidor de dominio de grabación de clics. El archivo debe alojarse en la ruta: `click.example.com/.well-known/apple-app-site-association`.

Consulte la [documentación de SparkPost](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) para saber cómo configurar el archivo de enlaces de activos digitales para SparkPost y establecer sub-rutas de enlaces personalizadas.

{% alert important %}
Una vez alojado el archivo Digital Asset Links, cualquier cambio en la configuración de OneLink (modificación o sustitución) requiere la generación de un nuevo archivo.
{% endalert %}

#### Paso 2b: Redirija su dominio de seguimiento de clics a su alojamiento de archivos de enlaces de activos digitales
Durante la [configuración de su correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/), creó un registro CNAME en su servidor DNS. Realice los siguientes pasos después de verificar su dominio de seguimiento de clics en Braze. 

1. Elimine el registro CNAME que redirige su subdominio al dominio SparkPost.
2. Cree un registro CNAME que redirija su dominio de seguimiento de clics a la CDN que aloja el archivo Digital Asset Links de su aplicación, en lugar del registro que eliminó anteriormente.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Paso 3: Configura tu SDK de AppsFlyer para que admita la vinculación en profundidad

{% tabs local %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
#### Paso 3a: Configura tu SDK para que admita el archivo AASA
Después de alojar el archivo AASA en tu dominio de grabación de clics, configura tu SDK de AppsFlyer para que admita el archivo AASA.

1. En Xcode, selecciona tu proyecto.
2. Selecciona **Capacidades.**
3. Activar **Dominios Asociados.**
4. Haz clic en **+** e introduce tu dominio de clic. Por ejemplo, `applinks:click.example.com`.
Cuando se hace clic en el enlace universal, se abre tu aplicación y se inicia el SDK. Para permitir que la aplicación extraiga el OneLink detrás del dominio de clic y resuelva el enlace profundo, realice lo siguiente:

#### Paso 3b: Manejar los datos del vínculo profundo
1. Proporciona el dominio de grabación de clics a la API del SDK [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). Es necesario llamar a esta API antes de inicializar el SDK. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
2. Utiliza la [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API para obtener los parámetros del vínculo profundo y manejar los datos del vínculo profundo.

{% endsubtab %}
{% subtab Android %}
#### Paso 3a: Configura tu SDK para que admita el archivo Enlaces de Activos Digitales

Después de alojar el archivo Digital Asset Links en su dominio de grabación de clics en el paso anterior, configure su SDK para que admita el archivo.

En el manifiesto de Android, añada el host de dominio de clic y cualquier prefijo en la etiqueta de actividad de la actividad en la que desea establecer el enlace profundo.

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### Paso 3b: Manejar los datos del vínculo profundo
Cuando se hace clic en un enlace de aplicación, se abre tu aplicación y se inicia el SDK.  Para habilitar la aplicación para extraer el OneLink detrás del dominio de clic y resolver el vínculo profundo, enumera los dominios de clic en el método SDK [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls). Esta propiedad debe establecerse antes de la inicialización del SDK. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "anotherclickdomain.com");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### Paso 3a: Configura tu SDK para que admita el archivo AASA
Después de alojar el archivo AASA en tu dominio de grabación de clics, configura tu SDK para que admita el archivo AASA.

1. En Xcode, selecciona tu proyecto.
2. Selecciona **Capacidades.**
3. Activar **Dominios Asociados.**
4. Haz clic en **+** e introduce tu dominio de clic. Por ejemplo, `applinks:click.example.com`.

#### Paso 3b: Manejar los datos del vínculo profundo
Cuando se hace clic en el enlace universal, se abre tu aplicación y se inicia el SDK. Para habilitar el SDK para extraer el OneLink detrás del dominio de clic, realiza lo siguiente:
1. Enumerar los dominios de clic en la propiedad SDK  [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). Asegúrese de establecer esta propiedad antes de la inicialización del SDK.
2. Asegúrese de que Lista <em>spgo.io</em> es uno de los dominios de la lista. SparkPost es propietario de este dominio y forma parte del flujo de redireccionamiento. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
3. Utiliza la [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API para obtener los parámetros del vínculo profundo y manejar los datos del vínculo profundo.
{% endsubtab %}
{% subtab Android %}
#### Paso 3a: Configura tu SDK para que admita el archivo Enlaces de Activos Digitales

Después de alojar el archivo Digital Asset Links en su dominio de grabación de clics en el paso anterior, configure su SDK para que admita el archivo.

En el manifiesto de Android, añada el host de dominio de clic y cualquier prefijo en la etiqueta de actividad de la actividad en la que desea establecer el enlace profundo.

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### Paso 3b: Manejar los datos de App Link
Cuando se hace clic en un enlace de aplicación, se abre tu aplicación y se inicia el SDK. Para permitir que la aplicación extraiga el OneLink detrás del dominio de clic y resuelva el enlace profundo, realice lo siguiente:

1. Enumerar los dominios de clic en el método SDK [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls). Esta propiedad debe establecerse antes de la inicialización del SDK.
2. Asegúrese de que Lista *spgo.io* es uno de los dominios de la lista. SparkPost es propietario de este dominio y forma parte del flujo de redireccionamiento. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "spgo.io");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

Una vez que hayas completado los pasos de la integración, puedes realizar el control de calidad y la solución de problemas enviando un vínculo profundo mediante OneLink. Consulte la [documentación de AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) para más detalles sobre el uso de OneLink.

### URL de seguimiento de clics de AppsFlyer en Braze (opcional)

Puede utilizar los [enlaces de atribución OneLink](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) de AppsFlyer en campañas Braze a través de push, correo electrónico y más. Esto le permite enviar los datos de atribución de instalación o reenganche de sus campañas Braze a AppsFlyer. Como resultado, podrá medir sus esfuerzos de marketing con mayor eficacia y tomar decisiones basadas en datos.

Puede simplemente crear su URL de seguimiento OneLink en AppsFlyer e insertarla directamente en sus campañas Braze. AppsFlyer utilizará entonces sus [metodologías de atribución probabilística](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) para atribuir al usuario que ha hecho clic en el enlace. Le recomendamos que añada a sus enlaces de seguimiento de AppsFlyer un identificador de dispositivo para mejorar la precisión de las atribuciones de sus campañas Braze. Esto atribuirá de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs local %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). El GAID también se recoge de forma nativa a través de la integración del SDK de AppsFlyer. Puede incluir el GAID en sus enlaces de seguimiento de clics de AppsFlyer utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como AppsFlyer recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones SDK. Puede utilizarse como identificador del dispositivo. Puede incluir el IDFV en sus enlaces de seguimiento de clics de AppsFlyer utilizando la siguiente lógica de Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}



