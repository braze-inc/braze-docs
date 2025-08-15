---
nav_title: Actualizaciones en vivo para Android
article_title: Actualizaciones en vivo del SDK de Android Braze
page_order: 0.1
description: "Aprende a configurar las Actualizaciones en vivo para el SDK Braze de Android."
platform: 
  - Android
  - FireOS
---

# Actualizaciones en vivo para Android

> Aprende a utilizar las Actualizaciones en vivo de Android en el SDK de Braze, también conocidas como [Notificaciones centradas en el progreso](https://developer.android.com/about/versions/16/features/progress-centric-notifications). Estas notificaciones son similares a [las Actividades en vivo del SDK de Swift Braze]({{site.baseurl}}/developer_guide/live_notifications/live_activities), que te permiten mostrar notificaciones interactivas en la pantalla de bloqueo. Android 16 introduce notificaciones centradas en el progreso para ayudar a los usuarios a realizar fácilmente un seguimiento de extremo a extremo de los viajes iniciados por el usuario.

## Cómo funciona

Puedes utilizar la interfaz [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) interfaz para personalizar cómo se muestran las notificaciones push de Braze. Al ampliar `BrazeNotificationFactory`, Braze llamará al método `createNotification()` de tu fábrica antes de que la notificación se muestre al usuario. A continuación, pasará una carga útil que contiene pares clave-valor personalizados enviados a través del panel Braze o la API REST.

## Mostrar una actualización en vivo

En esta sección, te asociarás con Búho Soberbio, el presentador de un nuevo programa de juegos en el que equipos de rescate de animales salvajes compiten para ver quién salva más búhos. Quieren aprovechar las Actualizaciones en vivo en su aplicación Android, para poder mostrar el estado de un partido en curso y realizar actualizaciones dinámicas de la notificación en tiempo real.

![Un ejemplo de actualización en vivo desde Android]({% image_buster /assets/img/android/android-live-update.png %}){: style="max-width:40%;"}

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### Paso 1: Crear una fábrica de notificaciones personalizada

En tu aplicación, crea un nuevo archivo llamado `MyCustomNotificationFactory.kt` que extienda [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para gestionar cómo se muestran las actualizaciones en vivo de Braze.

En el siguiente ejemplo, Superbúho creó una fábrica de notificaciones personalizada para mostrar una actualización en vivo de los partidos en curso. En el siguiente paso, crearás un nuevo método llamado `getTeamInfo` para mapear los datos de un equipo a la actividad.

```kotlin
class MyCustomNotificationFactory : IBrazeNotificationFactory {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        val notificationBuilder = populateNotificationBuilder(payload)
        val context = payload.context ?: return null

        if (notificationBuilder == null) {
            brazelog { "Notification could not be built. Returning null as created notification." }
            return null
        }
        notificationBuilder.setContentTitle("Android Live Updates").setContentText("Ongoing updates below")
        setProgressStyle(notificationBuilder, context)
        return notificationBuilder.build()
    }

    private fun setProgressStyle(notificationBuilder: NotificationCompat.Builder, context: Context) {
        val style = NotificationCompat.ProgressStyle()
            .setStyledByProgress(false)
            .setProgress(200)
            .setProgressTrackerIcon(IconCompat.createWithResource(context, R.drawable.notification_small_icon))
            .setProgressSegments(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Segment(1000).setColor(Color.GRAY),
                    NotificationCompat.ProgressStyle.Segment(200).setColor(Color.BLUE),
                )
            )
            .setProgressPoints(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Point(60).setColor(Color.RED),
                    NotificationCompat.ProgressStyle.Point(560).setColor(Color.GREEN)
                )
            )

        notificationBuilder.setStyle(style)
    }
}
```

### Paso 2: Mapear datos personalizados

En `MyCustomNotificationFactory.kt`, crea un nuevo método para manejar los datos cuando se muestren las Actualizaciones en vivo.

Superb Owl ha creado el siguiente método para mapear el nombre y el logotipo de cada equipo con Actualizaciones en vivo ampliadas:

```kotlin
class CustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        // Your existing code
        return super.createNotification(payload)
    }

    // Your new method
    private fun getTeamInfo(team: String?): Pair<String, Int> {
        return when (team) {
            "WBF" -> Pair("Wild Bird Fund", R.drawable.team_wbf)
            "OWL" -> Pair("Owl Rehab", R.drawable.team_owl)
            else  -> Pair("Unknown", R.drawable.notification_small_icon)
        }
    }
}
```

### Paso 3: Configura la fábrica de notificaciones personalizada

En tu clase de aplicación, utiliza [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)para configurar tu fábrica de notificaciones personalizada.

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Paso 4: Envía la actividad

Puedes utilizar el punto final [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) API REST para enviar una notificación push al dispositivo Android de un usuario.

#### Ejemplo de comando curl

El Búho Soberbio envió su petición utilizando el siguiente comando curl:

```
curl -X POST "https://BRAZE_REST_ENDPOINT/messages/send" \
  -H "Authorization: Bearer {REST_API_KEY}" \
  -H "Content-Type: application/json" \
  --data '{
    "external_user_ids": ["USER_ID"],
    "messages": {
      "android_push": {
        "title": "WBF vs OWL",
        "alert": "2 to 4 1:33 Q4",
        "extra": {
          "live_update": "true",
          "team1": "WBF",
          "team2": "OWL",
          "score1": "2",
          "score2": "4",
          "time": "1:33",
          "quarter": "Q4"
        },
        "notification_id": "ASSIGNED_NOTIFICATION_ID"
      }
    }
  }'
```

{% alert tip %}
Aunque los comandos curl son útiles para las pruebas, te recomendamos que gestiones esta llamada en tu backend, donde ya estás gestionando tus [Actividades en vivo de iOS]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift).
{% endalert %}

#### Parámetros de la solicitud

| Clave                          | Descripción |
|------------------------------|------------|
| `REST_API_KEY`               | Una clave de API REST de Braze con permisos `messages.send`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| `BRAZE_REST_ENDPOINT`         | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
| `USER_ID`                    | ID del usuario al que envías la notificación. |
| `messages.android_push.title` | El título del mensaje. Por predeterminado, no se utiliza para las notificaciones en vivo de la fábrica de notificaciones personalizadas, pero puede utilizarse como alternativa. |
| `messages.android_push.alert` | El cuerpo del mensaje. Por predeterminado, no se utiliza para las notificaciones en vivo de la fábrica de notificaciones personalizadas, pero puede utilizarse como alternativa. |
| `messages.extra`             | Pares clave-valor que la fábrica de notificaciones personalizada utiliza para las notificaciones en vivo. Puedes asignar cualquier cadena a este valor; sin embargo, en el ejemplo anterior, se utiliza `live_updates` para determinar si se trata de una notificación push predeterminada o en vivo. |
| `ASSIGNED_NOTIFICATION_ID`   | El ID de notificación que quieres asignar a la notificación en vivo del usuario elegido. El ID debe ser único para este juego, y debe utilizarse para [actualizar](#android_step-4-update-data-with-the-braze-rest-api) posteriormente [su notificación existente](#android_step-4-update-data-with-the-braze-rest-api). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Paso 5: Actualiza la actividad

Para actualizar la actualización en vivo existente con nuevos datos, modifica los correspondientes pares clave-valor asignados a `messages.extra`, luego utiliza el mismo `notification_id` y vuelve a llamar al punto final `/messages/send`.
