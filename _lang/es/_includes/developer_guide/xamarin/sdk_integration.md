## Integración del SDK de .NET MAUI

La integración del SDK Braze .NET MAUI (antes Xamarin) te proporcionará funciones básicas de análisis, así como mensajes dentro de la aplicación con los que podrás interactuar con tus usuarios. 

### Requisitos previos

Antes de integrar el SDK .NET MAUI Braze, asegúrate de que cumples los siguientes requisitos:

- A partir de la `version 3.0.0`, este SDK requiere el uso de .NET 6+ y elimina la compatibilidad con proyectos que utilicen el framework Xamarin.
- A partir de `version 4.0.0`, este SDK dejó de ser compatible con Xamarin  &Xamarin.Forms y añadió compatibilidad con .NET MAUI. Consulta [la política de Microsoft](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin) sobre el fin del soporte para Xamarin.

### Paso 1: Obtén el enlace .NET MAUI

{% tabs %}
{% tab android %}
Un enlace .NET MAUI es una forma de utilizar bibliotecas nativas en aplicaciones .NET MAUI. La implementación de una vinculación consiste en crear una interfaz C# para la biblioteca, y luego utilizar esa interfaz en tu aplicación.  Consulta la [documentación de .NET MAUI](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/). Hay dos formas de incluir la vinculación del SDK de Braze: utilizando NuGet o compilando desde el código fuente.

{% subtabs local %}
{% subtab NuGet %}
El método de integración más sencillo consiste en obtener el SDK de Braze del repositorio central [NuGet.org](https://www.nuget.org/). En la barra lateral de Visual Studio, haz clic con el botón derecho en la carpeta `Packages` y haz clic en `Add Packages...`.  Busca "Braze" e instala el paquete [`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/) en tu proyecto.

Para utilizar los servicios de ubicación y geovallas de Braze, instala también el[`BrazePlatform.BrazeAndroidLocationBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidLocationBinding/)paquete.
{% endsubtab %}

{% subtab Source %}
El segundo método de integración consiste en incluir la [fuente vinculante](https://github.com/braze-inc/braze-xamarin-sdk). En[`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding)  encontrarás nuestro código fuente vinculante; al añadir una referencia de proyecto al```BrazeAndroidBinding.csproj```  en tu aplicación .NET MAUI, se creará el vínculo con tu proyecto y podrás acceder al SDK de Braze para Android.

Para utilizar los servicios de ubicación y geovallas de Braze, añade también una referencia de proyecto a la```BrazeAndroidLocationBinding.csproj```  que se encuentra en [`appboy-component/src/androidnet6/BrazeAndroidLocationBinding`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidLocationBinding).
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert important %}
Los enlaces iOS para .NET MAUI SDK versión 4.0.0 y posteriores utilizan [Braze SWIFT SDK](https://github.com/braze-inc/braze-swift-sdk/), mientras que las versiones anteriores utilizan el [SDK AppboyKit heredado](https://github.com/Appboy/Appboy-ios-sdk).
{% endalert %}

Un enlace .NET MAUI es una forma de utilizar bibliotecas nativas en aplicaciones .NET MAUI. La implementación de una vinculación consiste en crear una interfaz C# para la biblioteca y luego utilizar esa interfaz en tu aplicación. Hay dos formas de incluir la vinculación del SDK de Braze: utilizando NuGet o compilando desde el código fuente.

{% subtabs local %}
{% subtab NuGet %}
El método de integración más sencillo consiste en obtener el SDK de Braze del repositorio central [NuGet.org](https://www.nuget.org/). En la barra lateral de Visual Studio, haz clic con el botón derecho en la carpeta `Packages` y pulsa `Add Packages...`.  Busca «Braze» e instala los últimos paquetes NuGet de .NET MAUI iOS:[Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)[Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit) ,  y[Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation)  en tu proyecto.

También proporcionamos los paquetes de bibliotecas de compatibilidad: [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat) y [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat) para facilitar tu migración a .NET MAUI.
{% endsubtab %}

{% subtab Source %}
El segundo método de integración consiste en incluir la [fuente vinculante](https://github.com/braze-inc/braze-xamarin-sdk). En[`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding)  encontrarás nuestro código fuente de enlace; al añadir una referencia de proyecto al```BrazeiOSBinding.csproj```  en tu aplicación .NET MAUI, el enlace se creará con tu proyecto y te dará acceso al SDK de Braze para iOS. Asegúrate de que `BrazeiOSBinding.csproj` aparece en la carpeta "Referencia" de tu proyecto.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Paso 2: Configura tu instancia de Braze

{% tabs %}
{% tab android %}
#### Paso 2.1: Configura el SDK de Braze en Braze.xml

Ahora que las bibliotecas están integradas, tienes que crear un archivo `Braze.xml` en la carpeta `Resources/values` de tu proyecto. El contenido de ese archivo debe parecerse al siguiente fragmento de código:

{% alert note %}
Asegúrate de sustituir `YOUR_API_KEY` por la clave de API que se encuentra en **Configuración** > **Claves de API** en el panel de Braze.
<br><br>
Si utilizas la [navegación anterior]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), puedes encontrar las claves de API en **Consola para desarrolladores** > **Configuración de API**..
{% endalert %}

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
    <string translatable="false" name="com_braze_api_key">YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
  </resources>
```
Si incluyes manualmente el código fuente de la vinculación, elimina `<item>NUGET</item>` de tu código.

{% alert tip %}
Para ver un ejemplo `Braze.xml`, consulta nuestro [ejemplo de aplicación MAUI para Android](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml).
{% endalert %}

#### Paso 2.2: Añade los permisos necesarios al manifiesto de Android

Ahora que has añadido tu clave de API, tienes que añadir los siguientes permisos a tu archivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
Para ver un ejemplo de tu `AndroidManifest.xml`, consulta el ejemplo de aplicación [MAUI de Android](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml).

#### Paso 2.3: Seguimiento de las sesiones de usuario y registro de mensajes dentro de la aplicación

Para habilitar el seguimiento de la sesión del usuario y registrar tu aplicación para mensajes dentro de la aplicación, añade la siguiente llamada al método del ciclo de vida `OnCreate()` de la clase `Application` de tu aplicación:

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab ios %}
Cuando configures tu instancia de Braze, añade el siguiente fragmento de código para configurar tu instancia:

{% alert note %}
Asegúrate de sustituir `YOUR_API_KEY` por la clave de API que se encuentra en **Configuración** > **Claves de API** en el panel de Braze.

Si utilizas la [navegación anterior]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), puedes encontrar las claves de API en **Consola para desarrolladores** > **Configuración de API**..
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

Consulta el archivo `App.xaml.cs` en la aplicación de ejemplo [MAUI de iOS](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs).
{% endtab %}
{% endtabs %}

### Paso 3: Prueba la integración

{% tabs %}
{% tab android %}
Ahora puedes iniciar tu aplicación y ver las sesiones que se registran en el panel de Braze (junto con la información del dispositivo y otros análisis). Para profundizar en las mejores prácticas para la integración del SDK básica, consulta las [instrucciones de integración de Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).
{% endtab %}

{% tab ios %}
Ahora puedes lanzar tu aplicación y ver las sesiones que se registran en el panel Braze. Para profundizar en las mejores prácticas para la integración del SDK básica, consulta las [instrucciones de integración de iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift).

{% alert important %}
Nuestro enlace público actual .NET MAUI para el SDK de iOS no se conecta al SDK de Facebook para iOS (vinculación de datos de redes sociales) y no incluye el envío del IDFA a Braze.
{% endalert %}
{% endtab %}
{% endtabs %}
