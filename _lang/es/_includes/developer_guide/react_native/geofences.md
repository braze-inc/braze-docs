{% alert important %}
Las geovallas son compatibles **tanto** con **iOS como** con **Android** en el SDK de React Native. El`requestLocationInitialization`método es exclusivo para Android y no es necesario para iOS. El`requestGeofences`método está disponible en ambas plataformas. De forma predeterminada, el SDK puede solicitar y supervisar automáticamente las geovallas cuando la ubicación está disponible; puedes confiar en esta configuración automática o llamar`requestGeofences`a  para solicitarlo manualmente.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %} En Android, tendrás que [configurar notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) para la sincronización de geovallas.

## Configuración de geovallas {#setting-up-geofences}

### Paso 1: Habilitar en Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Paso 2: Configuración completa nativa de Android

Dado que el SDK de React Native utiliza el SDK nativo de Braze para Android, completa la configuración de geovallas nativas de Android para tu proyecto. El equivalente en iOS de estos pasos se describe en la guía nativa de geovallas del SDK de SWIFT ([pasos 2.2 a 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)); el paso 2.1 (Añadir el módulo BrazeLocation) no es necesario para React Native, ya que BrazeLocation ya está incluido implícitamente en el SDK de Braze React Native.

1. **Actualización`build.gradle`:** Añade`android-sdk-location`  y la ubicación de Google Play Services. Ver [geovallas de Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
2. **Actualiza el manifiesto:** Añade permisos de ubicación y el receptor de arranque Braze. Ver [geovallas de Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
3. **Habilitar la recopilación de ubicación de Braze:** Actualiza tu`braze.xml`archivo. Ver [geovallas de Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

### Paso 3: Configuración nativa completa para iOS

Dado que el SDK de React Native utiliza el SDK nativo de Braze para iOS, completa la configuración de geovallas nativas de iOS para tu proyecto siguiendo las instrucciones del SDK nativo de SWIFT a partir del paso 2.2: actualiza tu`Info.plist`  con descripciones del uso de la ubicación (paso 2.2) y habilita las geovallas en tu configuración de Braze, incluyendo`automaticGeofenceRequests = true`  (paso 3); opcionalmente, habilita los informes en segundo plano (paso 3.1). El paso 2.1 (Añadir el módulo BrazeLocation) no es necesario, ya que BrazeLocation ya está incluido implícitamente en el SDK de Braze React Native. Consulta [las geovallas de iOS, pasos 2.2 a 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module).

### Paso 4: Solicitar geovallas desde JavaScript

**En Android:** Después de que el usuario conceda los permisos de ubicación, llama a`requestLocationInitialization()`  para inicializar las características de ubicación de Braze y solicitar geovallas a los servidores de Braze. Este método no es compatible con iOS y no es necesario para iOS.

**En iOS:** El equivalente es habilitar la`automaticGeofenceRequests`configuración en tu configuración nativa de SWIFT u Objective-C Braze (consulta el paso 3). Con esta habilitación, el SDK solicita y supervisa automáticamente las geovallas cuando la ubicación está disponible; no se requiere ninguna `requestLocationInitialization`llamada JavaScript equivalente a .

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### Paso 5: Solicitar geovallas manualmente (opcional)

Tanto en iOS como en Android, puedes solicitar manualmente una actualización de la geovalla para unas coordenadas GPS específicas utilizando `requestGeofences`. De forma predeterminada, Braze recupera automáticamente la ubicación del dispositivo y solicita geovallas. Para proporcionar manualmente una coordenada:

1. Desactiva las solicitudes automáticas de geovallas. En Android, configura`com_braze_automatic_geofence_requests_enabled`  en`false`  en tu `braze.xml`. En iOS, configura`automaticGeofenceRequests`  en`false`  en tu configuración de Braze.
2. Llama`requestGeofences`con la latitud y longitud deseadas:

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
Las geovallas solo pueden solicitarse una vez por sesión, ya sea automáticamente por el SDK o manualmente con este método.
{% endalert %}
