---
nav_title: Configuración inicial del SDK
article_title: Configuración inicial del SDK para Windows Universal
platform: Windows Universal
page_order: 0
description: "En este artículo de referencia se cubren los pasos iniciales de integración de SDK para integrar el SDK de Braze en tu plataforma universal de Windows."
search_rank: 1
hidden: true
---

# Integración de SDK inicial
{% multi_lang_include archive/windows_deprecation.md %}

El SDK de Braze te proporcionará una API para reportar información que se utilizará en análisis, segmentación e interacción, así como la capacidad de registrar usuarios para recibir notificaciones push y recibirlas.

>  El SDK Universal de Windows también es compatible con las aplicaciones de .NET MAUI para Windows.

## Paso 1: Instala el SDK mediante el administrador de paquetes NuGet

El SDK Universal de Windows se instala a través del [administrador de paquetes NuGet][14]. Para instalar el SDK de Braze para Windows a través de NuGet:

1. Haz clic con el botón derecho del ratón en el archivo del proyecto
2. Haz clic en "Administrar paquetes NuGet".
3. Haz clic en "En línea" en el menú desplegable de la izquierda
4. Busca "Appboy" en "NuGet.org"
5. Haz clic en el paquete NuGet "AppboyPlatform.Universal.Release" y pulsa Instalar

>  La biblioteca universal de Windows debe utilizarse para todas las aplicaciones de Windows 8.1, Windows Phone 8.1 y UWP.

## Paso 2: Creación y configuración de AppboyConfiguration.xml

Crea un archivo llamado `AppboyConfiguration.xml` en el directorio raíz de tu proyecto y añade el siguiente fragmento de código en ese archivo:

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  Asegúrate de actualizar `YOUR_API_KEY_HERE` con tu clave de API, que puedes encontrar en la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/).

Una vez que hayas añadido ese fragmento de código, asegúrate de modificar las siguientes propiedades de archivo para `AppboyConfiguration.xml`

1. Configura `Build Action` en `Content`
2. Configura `Copy to Output Directory` en `Copy Always`

## Paso 3: Configuración de package.appxmanifest

Dentro de la pestaña "Capacidades", asegúrate de que `Internet (Client)` está marcada.
![][18]

## Paso 4: Editar la clase de tu aplicación

- Añade lo siguiente a la dirección `usings` de tu archivo `App.xaml.cs`:

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- Llama a lo siguiente dentro de tu método del ciclo de vida `OnLaunched`:

```csharp
Appboy.SharedInstance.OpenSession();
```

- Llama a lo siguiente dentro de tu método del ciclo de vida `OnSuspending`:

```csharp
Appboy.SharedInstance.CloseSession();
```

## Integración de SDK básica completa

Ahora Braze debería estar recopilando datos de tu aplicación. Consulta los siguientes artículos sobre cómo registrar [atributos]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/), [eventos]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events) y [compras]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases) en nuestro SDK y cómo instrumentar la mensajería push.

>  Si estás utilizando el proyecto Unity de Braze en la misma aplicación, puede que tengas que calificar completamente las llamadas a Braze como "AppboyPlatform.Universal.Appboy"

[14]: http://www.nuget.org/
[18]: {% image_buster /assets/img_archive/internet_client.png %}
