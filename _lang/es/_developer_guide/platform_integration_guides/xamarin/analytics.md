---
nav_title: Análisis
article_title: Análisis para Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 4
description: "En este artículo se cubren los análisis de iOS, Android y FireOS para la plataforma Xamarin."

---
 
# Análisis de Xamarin

> Aprende a generar y revisar análisis para la plataforma Xamarin.

## Seguimiento de la sesión

El SDK de Braze informa de los datos de sesión utilizados por el panel de Braze para calcular la participación de los usuarios y otros análisis esenciales para comprender a tus usuarios. Basándose en la siguiente semántica de sesión, nuestro SDK genera puntos de datos de "inicio de sesión" y "cierre de sesión" que tienen en cuenta la duración de la sesión y los recuentos de sesiones visibles dentro del panel Braze.

Para establecer un ID de usuario o iniciar una sesión, utiliza el método `ChangeUser`, que toma un parámetro de ID de usuario.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).ChangeUser("user_id");
```

Consulta [las instrucciones de integración de Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) para obtener información detallada sobre cuándo y cómo establecer y cambiar un ID de usuario.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.ChangeUser("user_id");
```

Consulta [las instrucciones de integración de]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) iOS para obtener información detallada sobre cuándo y cómo establecer y cambiar un ID de usuario.

{% endtab %}
{% endtabs %}

## Registro de eventos personalizados

Puedes grabar eventos personalizados en Braze utilizando `LogCustomEvent` para conocer mejor los patrones de uso de tu aplicación y segmentar a tus usuarios por sus acciones en el panel.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogCustomEvent("event_name");
```

Consulta [las instrucciones de integración en Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/) para conocer en profundidad las mejores prácticas e interfaces de seguimiento de eventos.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogCustomEvent("event_name");
```

Consulta [las instrucciones de integración en]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) iOS para conocer en profundidad las mejores prácticas e interfaces de seguimiento de eventos.

{% endtab %}
{% endtabs %}

## Registrar compras

Registra las compras dentro de la aplicación utilizando `LogPurchase` para hacer un seguimiento de tus ingresos a lo largo del tiempo y a través de las fuentes de ingresos, así como segmentar a tus usuarios por su valor de duración de vida.

Braze admite compras en varias divisas. Las compras que notifiques en una divisa distinta del USD se mostrarán en el panel en USD según la tasa de cambio en la fecha en que se notificaron.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogPurchase("product_id", "USD", new Java.Math.BigDecimal(3.50));
```

Consulta [las instrucciones de integración en Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/) para conocer en profundidad las mejores prácticas e interfaces de seguimiento de los ingresos.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogPurchase("product_id", "USD", 3.50);
```

Consulta [las instrucciones de integración en]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) iOS para conocer en profundidad las mejores prácticas e interfaces de seguimiento de los ingresos.

{% endtab %}
{% endtabs %}

### Registrar las compras a nivel de pedido

Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

### Claves reservadas

Las siguientes claves están reservadas y **no pueden** utilizarse como propiedades de la compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Registro de atributos personalizados

Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el panel.

### Atributos predeterminados del usuario

Para asignar atributos de usuario recogidos automáticamente por Braze, puedes utilizar los métodos setter que vienen con el SDK. Por ejemplo, puedes configurar el nombre de pila del usuario:

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetFirstName("first_name");
```

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetFirstName("first_name");
```

{% endtab %}
{% endtabs %}

Se admiten los siguientes atributos:

- Nombre
- Apellido
- Género
- Fecha de nacimiento
- Ciudad natal
- País
- Número de teléfono
- Correo electrónico

### Atributos personalizados del usuario

Además de nuestros métodos predefinidos de atributos de usuario, Braze también proporciona atributos personalizados utilizando `SetCustomUserAttribute` para hacer un seguimiento de los datos de tus aplicaciones.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

Consulta [las instrucciones de integración en Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) para conocer en profundidad las mejores prácticas e interfaces de seguimiento de atributos.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

Consulta [las instrucciones de integración en]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) iOS para conocer en profundidad las mejores prácticas e interfaces de seguimiento de atributos.

{% endtab %}
{% endtabs %}

## seguimiento de ubicación

Para ver un ejemplo de análisis de registro y seguimiento, consulta nuestros ejemplos de aplicaciones [MAUI para Android](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/MainActivity.cs) y [MAUI para iOS](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/MainPage.xaml.cs).

{% tabs %}
{% tab Android %}
Para más información, consulta [las instrucciones de integración en Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/).
{% endtab %}

{% tab ios %}
Para permitir el seguimiento local, consulta [iOS: Utilizando la ubicación en segundo plano](http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/) y las [instrucciones de integración en iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/locations_and_geofences/).
{% endtab %}
{% endtabs %}

