---
nav_title: Crear indicadores de características
article_title: Crear indicadores de características
page_order: 20
description: "Este artículo de referencia explica cómo crear indicadores de características para coordinar el despliegue de nuevas características."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Crear feature flags

> Las banderas de características te permiten habilitar o deshabilitar a distancia la funcionalidad para una selección de usuarios. Crea una nueva bandera de característica dentro del panel de Braze. Proporciona un nombre y un `ID`, una audiencia objetivo y un porcentaje de usuarios para los que habilitar esta característica. Luego, utilizando ese mismo `ID` en el código de tu aplicación o sitio web, puedes ejecutar condicionalmente determinadas partes de tu lógica empresarial. Para saber más sobre los indicadores de características y cómo puedes utilizarlos en Braze, consulta [Acerca de los indicadores de características]({{site.baseurl}}/developer_guide/feature_flags/).

## Requisitos previos

### Versión del SDK

Para utilizar las feature flags, asegúrate de que tus SDK están actualizados al menos con estas versiones mínimas:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Permisos Braze

Para gestionar las banderas de características en el panel, necesitarás ser administrador o tener los siguientes [permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/):

| Permiso                                                                    | Qué puedes hacer                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **Administrar conmutadores de características**                                                      | Ver, crear y editar feature flags.     |
| **Campañas de acceso, Lienzos, Tarjetas, Banderas de características, Segmentos, Mediateca** | Ver la lista de banderas de características disponibles. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Crear una bandera de característica

### Paso 1: Crear una nueva bandera de característica

Ve a **Mensajería** > **Indicadores de características** y, a continuación, selecciona **Crear indicador de características**.

![Una lista de banderas de características creadas previamente en el panel de Braze]({% image_buster /assets/img/feature_flags/feature-flags-list.png %}){: style="max-width:75%"}

### Paso 2: Rellena los datos

En **Detalles**, introduce un nombre, ID y descripción para tu bandera de características.

| Campo        | Descripción                                                                                                                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Apellidos         | Un título legible para tus especialistas en marketing y administradores.                                                                                                                                                       |
| ID           | El ID único que utilizarás en tu código para comprobar si esta característica está [habilitada para un usuario](#enabled). Este ID no se puede cambiar más tarde, así que revisa nuestras [mejores prácticas de denominación de ID](#naming-conventions) antes de continuar. |
| Descripción  | Una descripción opcional que da algo de contexto sobre tu bandera de característica.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paso 3: Crear propiedades personalizadas

En **Propiedades**, crea propiedades personalizadas a las que tu aplicación pueda acceder a través del SDK de Braze cuando tu característica esté habilitada. Puedes asignar un valor de cadena, booleano, imagen, marca de tiempo, JSON o un número a cada variable, así como establecer un valor predeterminado.

{% tabs local %}
{% tab ejemplo %}
En el siguiente ejemplo, la bandera de característica muestra un banner de agotado para una tienda de comercio electrónico utilizando las propiedades personalizadas indicadas: 

|Nombre de la propiedad|Tipo|Valor|
|--|--|--|
|`banner_height`|`number`|`75`|
|`banner_color`|`string`|`blue`|
|`banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|
|`homepage_icon`|`image`|`http://s3.amazonaws.com/[bucket_name]/`|
|`account_start`|`timestamp`|`2011-01-01T12:00:00Z`|
|`footer_settings`|`JSON`|`{ "colors": [ "red", "blue", "green" ], "placement": 123 }`|

{% alert tip %}
No hay límite en el número de propiedades que puedes añadir. Sin embargo, las propiedades de una bandera de característica están limitadas a un total de 10 KB. Tanto los valores de propiedad como las claves tienen una longitud máxima de 255 caracteres.
{% endalert %}
{% endtab %}
{% endtabs %}

### Paso 4: Elige segmentos a los que dirigirte

Antes de desplegar una bandera de características, tienes que elegir un [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) de usuarios al que dirigirte. Utiliza el menú desplegable **Añadir filtro** para filtrar a los usuarios de tu audiencia objetivo. Añade varios filtros para limitar aún más tu audiencia.

![Dos menús desplegables. El primero dice Usuarios objetivo por segmento. El segundo dice Filtros adicionales.]({% image_buster /assets/img/feature_flags/feature-flags-targeting.png %})

### Paso 5: Configura el tráfico de despliegue {#rollout}

Por defecto, las banderas de características siempre están desactivadas, lo que te permite separar la fecha de lanzamiento de tus características de la activación total de tus usuarios. Para iniciar el despliegue, utiliza el control deslizante **Tráfico de despliegue**, o introduce un porcentaje en el cuadro de texto, para elegir el porcentaje de usuarios aleatorios del segmento seleccionado que recibirán esta nueva característica.

![Un control deslizante denominado Tráfico de Despliegue, que oscila entre 0 y 100.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.png %}){: style="max-width:75%;"}

{% alert important %}
No configures el tráfico de despliegue por encima del 0 % hasta que estés listo para que tu nueva característica se active en vivo. Cuando definas inicialmente tu feature flag en el panel, deja esta configuración en 0 %.
{% endalert %}

## Utilizar el campo "habilitación" para las banderas de tus características {#enabled}

Una vez que hayas definido la bandera de tu característica, configura tu aplicación o sitio para comprobar si está habilitada o no para un usuario concreto. Cuando esté habilitada, establecerás alguna acción o harás referencia a las propiedades variables del indicador de características en función de tu caso de uso. El SDK de Braze proporciona métodos para obtener el estado de tu feature flag y sus propiedades en tu aplicación. 

Las banderas de las características se actualizan automáticamente al inicio de la sesión, para que puedas mostrar la versión más actualizada de tu característica al iniciarla. El SDK almacena en caché estos valores para poder utilizarlos mientras no estés conectado. 

{% alert note %}
Asegúrate de registrar [las impresiones de la bandera de características](#impressions).
{% endalert %}

Supongamos que vas a lanzar un nuevo tipo de perfil de usuario para tu aplicación. Puedes configurar `ID` como `expanded_user_profile`. A continuación, harías que tu aplicación comprobara si debe mostrar este nuevo perfil de usuario a un usuario concreto. Por ejemplo:

{% tabs %}
{% tab JavaScript %}

```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag?.enabled == true {
  print("expanded_user_profile is enabled")
} else {
  print("expanded_user_profile is not enabled")
}
```
{% endtab %}
{% tab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag?.enabled == true) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const featureFlag = await Braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Unity %}
```csharp
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.Enabled) {
  Console.WriteLine("expanded_user_profile is enabled");
} else {
  Console.WriteLine("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Cordova %}
```javascript
const featureFlag = await BrazePlugin.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);  
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab Flutter %}
```dart
BrazeFeatureFlag? featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
if (featureFlag?.enabled == true) {
  print("expanded_user_profile is enabled");
} else {
  print("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Roku %}
```brightscript
featureFlag = m.braze.getFeatureFlag("expanded_user_profile")
if featureFlag <> invalid and featureFlag.enabled
  print "expanded_user_profile is enabled"
else
  print "expanded_user_profile is not enabled"
end if
```
{% endtab %}
{% endtabs %}

### Registro de la impresión de una bandera de característica {#impressions}

Realiza un seguimiento de la impresión de una bandera de característica siempre que un usuario haya tenido la oportunidad de interactuar con tu nueva característica, o cuando __podría__ haber interactuado si la característica está desactivada (en el caso de un grupo de control en una prueba A/B). Las impresiones de la bandera de características sólo se registran una vez por sesión. 

Normalmente, puedes poner esta línea de código directamente debajo de donde haces referencia a tu bandera de característica en tu aplicación:

{% tabs %}
{% tab JavaScript %}

```javascript
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")
```

{% endtab %}
{% tab Java %}

```java
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.logFeatureFlagImpression("expanded_user_profile")
```

{% endtab %}
{% tab React Native %}

```javascript
Braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.LogFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Flutter %}
```dart
braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% endtabs %}

### Acceder a las propiedades {#accessing-properties}

Para acceder a las propiedades de una bandera de característica, utiliza uno de los métodos siguientes, según el tipo que hayas definido en el panel.

Si una propiedad a la que has hecho referencia no existe, estos métodos devolverán `null`.

{% tabs %}
{% tab JavaScript %}

```javascript
// Returns the Feature Flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
const stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
const booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
const numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
const imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a FeatureFlagJsonPropertyValue
const jsonProperty = featureFlag.getJsonProperty("footer_settings");
```

{% endtab %}
{% tab Swift %}

```swift
// Returns the Feature Flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")

// Returns the String property
let stringProperty: String? = featureFlag.stringProperty(key: "color")

// Returns the boolean property
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")

// Returns the number property as a double
let numberProperty: Double? = featureFlag.numberProperty(key: "height")

// Returns the Unix UTC millisecond timestamp property as an integer
let timestampProperty : Int? = featureFlag.timestampProperty(key: "account_start")

// Returns the image property as a String of the image URL
let imageProperty : String? = featureFlag.imageProperty(key: "homepage_icon")

// Returns the JSON object property as a [String: Any] dictionary
let jsonObjectProperty : [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")
```

{% endtab %}
{% tab Java %}

```java
// Returns the Feature Flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
String stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
Number numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
Long timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
String imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
JSONObject jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Returns the Feature Flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")

// Returns the String property
val stringProperty: String? = featureFlag.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = featureFlag.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = featureFlag.getNumberProperty("height")

// Returns the Unix UTC millisecond timestamp property as a long
val timestampProperty: Long? = featureFlag.getTimestampProperty("account_start")

// Returns the image property as a String of the image URL
val imageProperty: String?  = featureFlag.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% tab React Native %}

```javascript
// Returns the String property
const stringProperty = await Braze.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await Braze.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await Braze.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await Braze.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await Braze.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await Braze.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Unity %}

```csharp
// Returns the Feature Flag instance
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.GetStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.GetBooleanProperty("expanded");

// Returns the number property as an integer
var integerProperty = featureFlag.GetIntegerProperty("height");

// Returns the number property as a double
var doubleProperty = featureFlag.GetDoubleProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
var timestampProperty = featureFlag.GetTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.GetImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
var jsonObjectProperty = featureFlag.GetJSONProperty("footer_settings");
```

{% endtab %}
{% tab Cordova %}

```javascript
// Returns the String property
const stringProperty = await BrazePlugin.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await BrazePlugin.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await BrazePlugin.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await BrazePlugin.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await BrazePlugin.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Flutter %}

```dart
// Returns the Feature Flag instance
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
var numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as an integer
var timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a Map<String, dynamic> collection
var jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Roku %}

```brightscript
' Returns the String property
color = featureFlag.getStringProperty("color")

' Returns the boolean property
expanded = featureFlag.getBooleanProperty("expanded")

' Returns the number property
height = featureFlag.getNumberProperty("height")

' Returns the Unix UTC millisecond timestamp property
account_start = featureFlag.getTimestampProperty("account_start")

' Returns the image property as a String of the image URL
homepage_icon = featureFlag.getImageProperty("homepage_icon")

' Returns the JSON object property
footer_settings = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% endtabs %}

### Obtener una lista de todas las feature flags {#get-list-of-flags}

{% tabs %}
{% tab JavaScript %}

```javascript
const features = getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Swift %}

```swift
let features = braze.featureFlags.featureFlags
for let feature in features {
  print("Feature: \(feature.id)", feature.enabled)
}
```

{% endtab %}
{% tab Java %}

```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const features = await Braze.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Unity %}

```csharp
List<FeatureFlag> features = Appboy.AppboyBinding.GetAllFeatureFlags();
foreach (FeatureFlag feature in features) {
  Console.WriteLine("Feature: {0} - enabled: {1}", feature.ID, feature.Enabled);
}
```

{% endtab %}
{% tab Cordova %}
```javascript
const features = await BrazePlugin.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```
{% endtab %}
{% tab Flutter %}
```dart
List<BrazeFeatureFlag> featureFlags = await braze.getAllFeatureFlags();
featureFlags.forEach((feature) {
  print("Feature: ${feature.id} ${feature.enabled}");
});
```
{% endtab %}
{% tab Roku %}
```brightscript
features = m.braze.getAllFeatureFlags()
for each feature in features
      print "Feature: " + feature.id + " enabled: " + feature.enabled.toStr()
end for
```
{% endtab %}
{% endtabs %}

### Actualizar las feature flags {#refreshing}

Puedes actualizar las banderas de características del usuario actual en mitad de la sesión para obtener los últimos valores de Braze.

{% alert tip %}
La actualización se produce automáticamente al iniciar la sesión. Actualizar sólo es necesario antes de acciones importantes del usuario, como antes de cargar una página de pago, o si sabes que se hará referencia a una bandera de característica.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
braze.refreshFeatureFlags(() => {
  console.log(`Feature flags have been refreshed.`);
}, () => {
  console.log(`Failed to refresh feature flags.`);
});
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.requestRefresh { result in
  switch result {
  case .success(let features):
    print("Feature flags have been refreshed:", features)
  case .failure(let error):
    print("Failed to refresh feature flags:", error)
  }
}
```

{% endtab %}
{% tab Java %}

```java
braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.refreshFeatureFlags()
```

{% endtab %}
{% tab React Native %}

```javascript
Braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.RefreshFeatureFlags();
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.refreshFeatureFlags();
```
{% endtab %}
{% tab Flutter %}
```dart
braze.refreshFeatureFlags();
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.refreshFeatureFlags()
```
{% endtab %}
{% endtabs %}

### Escuchar los cambios {#updates}

Puedes configurar el SDK de Braze para que escuche y actualice tu aplicación cuando el SDK actualice cualquier indicador de característica.

Esto es útil si quieres actualizar tu aplicación si un usuario ya no es elegible para una característica. Por ejemplo, establecer algún estado en tu aplicación en función de si una característica está habilitada o no, o de uno de sus valores de propiedad.

{% tabs %}
{% tab JavaScript %}

```javascript
// Register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
  console.log(`Features were updated`, features);
});
// Unregister this event listener
braze.removeSubscription(subscriptionId);
```

{% endtab %}
{% tab Swift %}

```swift
// Create the feature flags subscription
// - You must keep a strong reference to the subscription to keep it active
let subscription = braze.featureFlags.subscribeToUpdates { features in
  print("Feature flags were updated:", features)
}
// Cancel the subscription
subscription.cancel()
```

{% endtab %}
{% tab Java %}

```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```

{% endtab %}
{% tab React Native %}

```javascript
// Register an event listener
Braze.addListener(braze.Events.FEATURE_FLAGS_UPDATED, (featureFlags) => {
  console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```

{% endtab %}
{% tab Unity %}

Para escuchar los cambios, ajusta los valores de **Nombre del objeto del juego** y **Nombre del método de devolución de llamada** en **Configuración de Braze** > **Banderas de características** a los valores correspondientes de tu aplicación.

{% endtab %}
{% tab Cordova %}
```javascript
// Register an event listener
BrazePlugin.subscribeToFeatureFlagUpdates((featureFlags) => {
    console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```
{% endtab %}
{% tab Flutter %}

En el código Dart de tu aplicación, utiliza el siguiente código de ejemplo:

```dart
// Create stream subscription
StreamSubscription featureFlagsStreamSubscription;

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
  print("Feature flags were updated");
});

// Cancel stream subscription
featureFlagsStreamSubscription.cancel();
```

A continuación, realiza estos cambios también en la capa nativa de iOS. Ten en cuenta que no son necesarios pasos adicionales en la capa de Android.

1. Implementa `featureFlags.subscribeToUpdates` para suscribirte a las actualizaciones de las banderas de características como se describe en la documentación [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/subscribetoupdates(_:)).

2. Tu implementación de devolución de llamada a `featureFlags.subscribeToUpdates` debe llamar a `BrazePlugin.processFeatureFlags(featureFlags)`.

Para ver un ejemplo, consulta [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) en nuestra aplicación de ejemplo.

{% endtab %}
{% tab Roku %}
```brightscript
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")
```
{% endtab %}

{% tab React Hook %}
```typescript
import { useEffect, useState } from "react";
import {
  FeatureFlag,
  getFeatureFlag,
  removeSubscription,
  subscribeToFeatureFlagsUpdates,
} from "@braze/web-sdk";

export const useFeatureFlag = (id: string): FeatureFlag => {
  const [featureFlag, setFeatureFlag] = useState<FeatureFlag>(
    getFeatureFlag(id)
  );

  useEffect(() => {
    const listener = subscribeToFeatureFlagsUpdates(() => {
      setFeatureFlag(getFeatureFlag(id));
    });
    return () => {
      removeSubscription(listener);
    };
  }, [id]);

  return featureFlag;
};
```
{% endtab %}
{% endtabs %}

## Ver el registro de cambios

Para ver el registro de cambios de una feature flag, abre esta última y selecciona **Registro de cambios**.

![Página "Editar" de la bandera de una característica, con el botón "Registro de cambios" resaltado.]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

Aquí puedes revisar cuándo se produjo un cambio, quién lo hizo, a qué categoría pertenece y mucho más.

![El registro de cambios de la bandera de la característica seleccionada.]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}){: style="max-width:90%;"}

## Segmentación con indicadores de características {#segmentation}

Braze hace un seguimiento automático de los usuarios que tienen habilitada una característica. Puedes crear un segmento o un objetivo de mensajería utilizando el [filtro **Feature flags**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#feature-flags). Para más información sobre cómo filtrar por segmentos, consulta [Crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

![La sección "Filtros" con la "Bandera de características" escrita en la barra de búsqueda de filtros.]({% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}){: style="max-width:75%;"}

{% alert note %}
Para evitar segmentos recursivos, no es posible crear un segmento que haga referencia a otras banderas de características.
{% endalert %}

## Buenas prácticas

### No combines rollouts con Lienzos o experimentos

Para evitar que los usuarios sean habilitados y deshabilitados por diferentes puntos de entrada, debes establecer el control deslizante de despliegue en un valor superior a cero O habilitar la bandera de característica en un Canvas o experimento. Como práctica recomendada, si piensas utilizar una bandera de característica en un Canvas o experimento, mantén el porcentaje de despliegue a cero.

### Convenciones de denominación

Para que tu código sea claro y coherente, considera la posibilidad de utilizar el siguiente formato al nombrar el ID de la bandera de tu característica:

```plaintext
BEHAVIOR_PRODUCT_FEATURE
```

Sustituye lo siguiente:

| Marcador de posición | Descripción                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `BEHAVIOR`  | El comportamiento de la característica. En tu código, asegúrate de que el comportamiento está desactivado por defecto y evita utilizar frases como `disabled` en el nombre del indicador de característica. |
| `PRODUCT`   | El producto al que pertenece la característica.                                                                                       |
| `FEATURE`    | El nombre de la característica.                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

He aquí un ejemplo de indicador de característica en el que `show` es el comportamiento, `animation_profile` es el producto y `driver` es la característica:

```plaintext
show_animation_profile_driver
```

### Planificar con antelación

Ve siempre a lo seguro. A la hora de considerar nuevas características que puedan requerir un interruptor de apagado, es mejor liberar código nuevo con una bandera de característica y no necesitarla que darse cuenta de que es necesaria una nueva actualización de la aplicación.

### Sé descriptivo

Añade una descripción a la bandera de tu característica. Aunque se trata de un campo opcional en Braze, puede ayudar a responder preguntas que otros puedan tener al examinar las banderas de características disponibles.

- Datos de contacto del responsable de la habilitación y comportamiento de esta bandera
- Cuándo se debe desactivar esta flag
- Enlaces a documentación o notas sobre la nueva característica que controla esta bandera
- Cualquier dependencia o nota sobre cómo utilizar la característica

### Limpiar antiguas banderas de características

Todos somos culpables de dejar características activadas al 100 % durante más tiempo del necesario.

Para ayudar a mantener limpio tu código (y el panel de Braze), elimina las feature flags permanentes de tu base de código una vez que todos los usuarios se hayan actualizado y ya no necesites la opción de desactivar la característica. Esto ayuda a reducir la complejidad de tu entorno de desarrollo, pero también a mantener ordenada tu lista de banderas de características.

