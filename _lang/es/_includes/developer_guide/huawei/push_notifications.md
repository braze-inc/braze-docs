{% multi_lang_include developer_guide/prerequisites/android.md %}

## Configuración de las notificaciones push

Los teléfonos más nuevos fabricados por [Huawei](https://huaweimobileservices.com/) vienen equipados con Huawei Mobile Services (HMS), un servicio utilizado para entregar mensajes push en lugar de Firebase Cloud Messaging (FCM) de Google.

### Paso 1: Registro para una cuenta de desarrollador de Huawei

Antes de empezar, tendrás que registrarte y configurar una [cuenta de desarrollador de Huawei](https://developer.huawei.com/consumer/en/console). En tu cuenta de Huawei, ve a **My Projects > Project Settings > App Information (Mis proyectos > Configuración del proyecto > Información de la aplicación)**, y toma nota de `App ID` y `App secret`.

![]({% image_buster /assets/img/huawei/huawei-credentials.png %})

### Paso 2: Crea una nueva aplicación Huawei en el panel de Braze

En el panel de Braze, ve a **Configuración de la aplicación**, que aparece en la navegación **Configuración**.

Haz clic en **\+ Añadir aplicación**, ponle un nombre (como Mi aplicación Huawei) y selecciona `Android` como plataforma.

![]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

Una vez creada tu nueva aplicación Braze, localiza la configuración de notificaciones push y selecciona `Huawei` como proveedor de notificaciones push. A continuación, proporciona tu `Huawei Client Secret` y `Huawei App ID`.

![]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

### Paso 3: Integra el SDK de mensajería de Huawei en tu aplicación

Huawei proporcionó un [codelab de integración en Android](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) en el que se detalla la integración del servicio de mensajería de Huawei en tu aplicación. Sigue estos pasos para empezar.

Después de completar el codelab, tendrás que crear un [servicio de mensajes personalizado de Huawei](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) para obtener tokens de notificaciones push y reenviar mensajes al SDK de Braze.

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).setRegisteredPushToken(token);
  }

  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage.getDataOfMap())) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomPushService: HmsMessageService() {
  override fun onNewToken(token: String?) {
    super.onNewToken(token)
    Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
  }

  override fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% endtabs %}

Después de añadir tu servicio push personalizado, añade lo siguiente a tu `AndroidManifest.xml`:

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

### Paso 4: Prueba tus notificaciones push (opcional)

En este punto, habrás creado una nueva aplicación Android de Huawei en el panel de Braze, la habrás configurado con tus credenciales de desarrollador de Huawei y habrás integrado los SDK de Braze y Huawei en tu aplicación.

A continuación, podemos poner a prueba la integración probando una nueva campaña push en Braze.

#### Paso 4.1: Crear una nueva campaña de notificación push

En la página **Campañas**, crea una nueva campaña y elige **Notificación push** como tipo de mensaje.

Después de nombrar tu campaña, elige **Android Push** como plataforma push.

![El compositor de creación de campañas que muestra las plataformas push disponibles.]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

A continuación, crea tu campaña push con un título y un mensaje.

#### Paso 4.2: Envía un push de prueba

En la pestaña **Prueba**, introduce tu ID de usuario, que habrás configurado en tu aplicación utilizando el [método`changeUser(USER_ID_STRING)` ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id), y haz clic en **Enviar prueba** para enviar un push de prueba.

![La pestaña de prueba del compositor de creación de campañas muestra que puedes enviarte un mensaje de prueba a ti mismo proporcionando tu ID de usuario e introduciéndolo en el campo "Añadir usuarios individuales".]({% image_buster /assets/img/huawei/huawei-test-send.png %})

En este punto, deberías recibir una notificación push de prueba de Braze en tu dispositivo Huawei (HMS).

#### Paso 4.3: Configura la segmentación de Huawei (opcional)

Como tu aplicación de Huawei en el panel de Braze se basa en la plataforma push de Android, tienes la flexibilidad de enviar push a todos los usuarios de Android (Firebase Cloud Messaging y Huawei Mobile Services), o puedes elegir segmentar la audiencia de tu campaña en aplicaciones específicas.

Para enviar push solo a las aplicaciones de Huawei, [crea un nuevo segmento]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) y selecciona tu aplicación de Huawei en la sección **Aplicaciones**.

![]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

Por supuesto, si quieres enviar el mismo push a todos los proveedores de push de Android, puedes elegir no especificar la aplicación que enviará a todas las aplicaciones de Android configuradas dentro del espacio de trabajo actual.
