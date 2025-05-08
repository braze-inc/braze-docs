---
nav_title: Integración
article_title: Integración del SDK Braze de Cordova
page_order: 0
---

# Integración del SDK Braze de Cordova

> Aprende a integrar el SDK Cordova de Braze en tu aplicación para iOS o Android. Cuando hayas terminado, puedes [personalizar aún más el SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/).

## Integración del SDK

### Paso 1: Añade el SDK a tu proyecto

Si utilizas Cordova 6 o posterior, puedes añadir el SDK directamente desde GitHub. También puedes descargar un ZIP del [repositorio de GitHub](https://github.com/braze-inc/braze-cordova-sdk) y añadir el SDK manualmente.

{% tabs local %}
{% tab geovalla desactivada %}
Si no piensas utilizar la recopilación de ubicaciones ni las geovallas, utiliza la rama `master` de GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab geovalla habilitada %}
Si piensas utilizar la recopilación de ubicaciones y geovallas, utiliza la página `geofence-branch` de GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Puedes cambiar entre `master` y `geofence-branch` en cualquier momento repitiendo el Paso 1.
{% endalert %}

### Paso 2: Configura tu proyecto

A continuación, añade las siguientes preferencias al elemento `platform` del archivo `config.xml` de tu proyecto.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab Android %}
```xml
<preference name="com.braze.api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Sustituye lo siguiente:

| Valor                 | Descripción                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_KEY`       | Tu [clave de API REST de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | Un punto final de API personalizado. Este punto final se utiliza para dirigir los datos de tu instancia de Braze al grupo de aplicaciones correcto en tu panel de Braze. |

El elemento `platform` de tu archivo `config.xml` debe ser similar al siguiente:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab Android %}
```xml
<platform name="android">
    <preference name="com.braze.api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Desactivar el seguimiento automático de la sesión (sólo Android)

De manera predeterminada, el plugin de Android Cordova hace un seguimiento automático de las sesiones. Para desactivar el seguimiento automático de la sesión, añade la siguiente preferencia al elemento `platform` del archivo `config.xml` de tu proyecto:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Para volver a iniciar el seguimiento de las sesiones, llama a `BrazePlugin.startSessionTracking()`. Ten en cuenta que sólo se hará un seguimiento de las sesiones iniciadas después de la siguiente `Activity.onStart()`.
