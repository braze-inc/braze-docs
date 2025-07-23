---
nav_title: Actualizaciones en vivo para Android
article_title: Actividades en vivo para el SDK Braze de Android
page_order: 0.1
description: "Aprende a configurar Actividades en vivo para el SDK Braze de Android."
platform: 
  - Android
  - FireOS
---

# Actividades en vivo para Android

> Aprende a emular las actualizaciones en vivo en el SDK Braze de Android. Aunque las Actualizaciones en vivo no están soportadas oficialmente, esta guía te mostrará cómo emular su comportamiento, para que puedas mostrar notificaciones interactivas en la pantalla de bloqueo similares a las [Actividades en vivo para el SDK de Swift Braze]({{site.baseurl}}/developer_guide/live_notifications/live_activities). A diferencia de las Actualizaciones en vivo oficiales, esta funcionalidad puede implementarse para versiones anteriores de Android.

## Cómo funciona

Puedes utilizar la interfaz [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) interfaz para personalizar cómo se muestran las notificaciones push de Braze. Al ampliar `BrazeNotificationFactory`, Braze llamará al método `createNotification()` de tu fábrica antes de que la notificación se muestre al usuario. A continuación, pasará una carga útil que contiene pares clave-valor personalizados enviados a través del panel Braze o la API REST.

## Emular una actualización en vivo

{% alert important %}
Las actualizaciones en vivo no se admiten de forma nativa en el sistema operativo Android. La sección siguiente sólo te muestra cómo emular su comportamiento general.
{% endalert %}

En esta sección, te asociarás con Búho Soberbio, el presentador de un nuevo programa de juegos en el que equipos de rescate de animales salvajes compiten para ver quién salva más búhos. Quieren aprovechar las Actualizaciones en vivo en su aplicación Android, para poder mostrar el estado de un partido en curso y realizar actualizaciones dinámicas de la notificación en tiempo real.

![La actualización en vivo que el Búho Soberbio quiere hacer, mostrando un partido en curso entre "Wild Bird Fund" y "Owl Rescue". Estamos en el cuarto cuarto y el marcador es 2-4 con OWL en cabeza.]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### Paso 1: Añadir un diseño personalizado

Puedes añadir uno o varios diseños personalizados de Actualización en vivo a tu proyecto. Son útiles para manejar cómo se muestran las notificaciones cuando se contraen o expanden. Tu estructura de directorios debe ser similar a la siguiente:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

En cada archivo XML, crea un diseño personalizado. Superb Owl creó los siguientes diseños para sus actualizaciones en vivo colapsadas y ampliadas:

{% tabs local %}
{% tab  Ejemplo: Diseño colapsado %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/notification_title"
        style="@style/TextAppearance.Compat.Notification.Title"
        android:layout_width="wrap_content"
        android:layout_height="0dp"
        android:layout_weight="1" />
</LinearLayout>
```
{% endtab %}

{% tab Ejemplo: Diseño ampliado %}
{% details Mostrar el código de muestra %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"

        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team1logo"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:layout_gravity="center"
            android:src="@drawable/team_default1"/>

        <TextView
            android:id="@+id/team1name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1.6"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/score"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="2-4"
            android:textColor="#555555"
            android:textAlignment="center"
            android:textSize="32sp"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/timeInfo"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>


    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team2logo"
            android:layout_gravity="center"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:src="@drawable/team_default2"/>

        <TextView
            android:id="@+id/team2name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>
</LinearLayout>
```
{% enddetails %}
{% endtab %}
{% endtabs %}

### Paso 2: Crear una fábrica de notificaciones personalizada

En tu aplicación, crea un nuevo archivo llamado `MyCustomNotificationFactory.kt` que extienda [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para gestionar cómo se muestran las actualizaciones en vivo de Braze.

En el siguiente ejemplo, Superbúho creó una fábrica de notificaciones personalizada para mostrar una actualización en vivo de los partidos en curso. En el [siguiente paso](#android_step-3-map-custom-data), crearán un nuevo método llamado `getTeamInfo` para mapear los datos de un equipo a la actividad.

{% details Mostrar el código de muestra %}
```kotlin
import android.app.Notification
import android.widget.RemoteViews
import androidx.core.app.NotificationCompat
import com.braze.models.push.BrazeNotificationPayload
import com.braze.push.BrazeNotificationFactory
import com.braze.push.BrazeNotificationUtils.getOrCreateNotificationChannelId
import com.braze.support.BrazeLogger.brazelog

class MyCustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        if (payload.extras.containsKey("live_update")) {
            val kvp = payload.extras
            val notificationChannelId = getOrCreateNotificationChannelId(payload)
            val context = payload.context

            if (context == null) {
                brazelog { "BrazeNotificationPayload has null context. Not creating notification" }
                return null
            }

            val team1 = kvp["team1"]
            val team2 = kvp["team2"]
            val score1 = kvp["score1"]
            val score2 = kvp["score2"]
            val time = kvp["time"]
            val quarter = kvp["quarter"]

            // Superb Owl will define the 'getTeamInfo' method in the next step.
            val (team1name, team1icon) = getTeamInfo(team1)
            val (team2name, team2icon) = getTeamInfo(team2)

            // Get the layouts to use in the custom notification.
            val notificationLayoutCollapsed = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_collapsed)
            val notificationLayoutExpanded = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_expanded)

            // Very simple notification for the small layout
            notificationLayoutCollapsed.setTextViewText(
                R.id.notification_title,
                "$team1 $score1 - $score2 $team2\n$time $quarter"
            )

            notificationLayoutExpanded.setTextViewText(R.id.score, "$score1 - $score2")
            notificationLayoutExpanded.setTextViewText(R.id.team1name, team1name)
            notificationLayoutExpanded.setTextViewText(R.id.team2name, team2name)
            notificationLayoutExpanded.setTextViewText(R.id.timeInfo, "$time - $quarter")
            notificationLayoutExpanded.setImageViewResource(R.id.team1logo, team1icon)
            notificationLayoutExpanded.setImageViewResource(R.id.team2logo, team2icon)

            val customNotification = NotificationCompat.Builder(context, notificationChannelId)
                .setSmallIcon(R.drawable.notification_small_icon)
                .setStyle(NotificationCompat.DecoratedCustomViewStyle())
                .setCustomContentView(notificationLayout)
                .setCustomBigContentView(notificationLayoutExpanded)
                .build()
            return customNotification
        } else {
            // Use the BrazeNotificationFactory for all other notifications
            return super.createNotification(payload)
        }
    }
}
```
{% enddetails %}

### Paso 3: Mapear datos personalizados

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

### Paso 4: Configura la fábrica de notificaciones personalizada

En tu clase de aplicación, utiliza [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)para configurar tu fábrica de notificaciones personalizada.

```kotlin
import com.braze.Braze

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Paso 5: Envía la actividad

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

### Paso 6: Actualiza la actividad

Para actualizar la actualización en vivo existente con nuevos datos, modifica los correspondientes pares clave-valor asignados a `messages.extra`, luego utiliza el mismo `notification_id` y vuelve a llamar al punto final `/messages/send`.
