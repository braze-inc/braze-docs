{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Configuración de las notificaciones push

### Paso 1: Configura tu proyecto

{% tabs %}
{% tab Android %}
Primero, añade Firebase a tu proyecto de Android. Para obtener instrucciones paso a paso, consulta la [guía de configuración de Firebase](https://firebase.google.com/docs/android/setup) de Google.
{% endtab %}

{% tab iOS %}
{% multi_lang_include developer_guide/swift/apns_token.md %}
{% endtab %}
{% endtabs %}

### Paso 2: Habilitar notificaciones push

{% tabs %}
{% tab Android %}
Añade las siguientes líneas al archivo `engine.ini` de tu proyecto. Asegúrate de sustituir `YOUR_SEND_ID` por el [ID del remitente en tu proyecto Firebase](https://firebase.google.com/docs/cloud-messaging/concept-options#credentials).

```ini
bEnableFirebaseCloudMessagingSupport=true
bIsFirebaseCloudMessagingRegistrationEnabled=true
FirebaseCloudMessagingSenderIdKey=YOUR_SENDER_ID
```

Dentro del mismo directorio que [BrazeUPLAndroid.xml](./BrazeSample/Plugins/Braze/Source/Braze/BrazeUPLAndroid.xml)crea un nuevo directorio llamado `AndroidCopies` y añade allí tu archivo `google-services.json`.
{% endtab %}

{% tab iOS %}
En tu proyecto, ve a **Configuración** > **Configuración del proyecto** > **iOS** > **En línea** y, a continuación, marca **Habilitar soporte de notificaciones remotas**. Cuando hayas terminado, comprueba que tu provisión tiene habilitadas las capacidades push.

{% alert important %}
Para habilitar las capacidades push para iOS, tu proyecto debe haber sido construido desde el código fuente. Para más información, consulta [Unreal Engine: Construir a partir del código fuente](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source).
{% endalert %}
{% endtab %}
{% endtabs %}

## Configuraciones opcionales

{% tabs %}
{% tab Android %}
#### Configuración de iconos pequeños y grandes

Para configurar los [iconos pequeño y grande de notificación]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android&tab=android#configure-icons):

1. Añade iconos a la carpeta de dibujables adecuada (`drawable` por predeterminado) dentro de la carpeta `AndroidCopies/res`.
2. Añade `braze.xml` a la carpeta `AndroidCopies/res/values` para configurar los iconos. Un archivo muy básico de braze.xml:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <drawable name="com_braze_push_small_notification_icon">@drawable/notification_small_icon</drawable>
        <drawable name="com_braze_push_large_notification_icon">@drawable/notification_large_icon</drawable>
    </resources>
    ```

{% alert note %}
Los archivos de la carpeta `AndroidCopies` se copiarán en la estructura del proyecto Android generado, tal y como se define en `BrazeUPLAndroid.xml`.
{% endalert %}
{% endtab %}

{% tab iOS %}
#### Notificaciones de lanzamiento a distancia

A partir de la versión 4.25.3 de Unreal Engine, UE4 carece de soporte adecuado para recibir una notificación remota que provoque el lanzamiento inicial de la aplicación. Para poder recibir esta notificación, hemos creado dos parches git para aplicar: uno para UE4 y otro para el plugin Braze SDK.

1. En el directorio `Source` de tu motor UE4, aplica el parche git `UE4_Engine-Cache-Launch-Remote-Notification.patch`.
2. En tu directorio Braze Unreal SDK, aplica el parche git `Braze_SDK-Read-Cached-Remote-Launch-Notification.patch`.
{% endtab %}
{% endtabs %}
