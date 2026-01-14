{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Disposition personnalisée des notifications

Les notifications de Braze sont envoyées sous forme de [messages de données](https://firebase.google.com/docs/cloud-messaging/concept-options), ce qui signifie que votre application aura toujours une chance de répondre et d'effectuer un comportement en conséquence, même en arrière-plan (contrairement aux messages de notification, qui peuvent être traités automatiquement par le système lorsque votre application est en arrière-plan). Ainsi, votre application aura la possibilité de personnaliser l’expérience, par exemple en affichant des éléments d’IU personnalisés dans la notification envoyée à la barre de notification. Bien que l'implémentation de push de cette manière puisse être peu familière à certains, l'une de nos fonctionnalités bien connues chez Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), est un excellent exemple de l'utilisation de composants de vue personnalisés pour créer une expérience engageante !

{% alert important %}
Android impose certaines limitations sur les composants pouvant être utilisés pour implémenter des vues personnalisées. Les dispositions de la vue de la notification doivent _uniquement_ contenir des objets de vue compatibles avec le framework [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews).
{% endalert %}

Vous pouvez utiliser l'interface [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) pour personnaliser l'affichage des notifications push de Braze. En étendant `BrazeNotificationFactory`, Braze appellera la méthode `createNotification()` de votre usine avant que la notification ne soit affichée à l'utilisateur. Il transmettra ensuite une charge utile contenant des paires clé-valeur personnalisées envoyées via le tableau de bord de Braze ou l'API REST.

Dans cette section, vous serez le partenaire de Superb Owl, l'animateur d'un nouveau jeu télévisé dans lequel des équipes de sauvetage d'animaux sauvages s'affrontent pour savoir qui peut enregistrer le plus grand nombre de hiboux. Ils cherchent à exploiter les notifications de mise à jour en ligne dans leur application Android, afin d'afficher le statut d'un match en cours et d'effectuer des mises à jour dynamiques de la notification en temps réel.

![La ligne/en production/instantanée que Superb Owl veut montrer, affiche un match en cours entre 'Wild Bird Fund' et 'Owl Rescue'. Nous sommes actuellement dans le quatrième quart-temps et le score est de 2-4 avec OWL en tête.]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

### Étape 1 : Ajouter une mise en page personnalisée

Vous pouvez ajouter une ou plusieurs présentations RemoteView de notification personnalisées à votre projet. Ils permettent de gérer l'affichage des notifications lorsqu'elles sont réduites ou développées. La structure de votre répertoire devrait ressembler à ce qui suit :

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

Dans chaque fichier XML, créez une mise en page personnalisée. Superb Owl a créé les mises en page suivantes pour leurs mises en page RemoteView réduites et étendues :

{% tabs local %}
{% tab  Exemple : Mise en page réduite %}
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

{% tab Exemple : Disposition élargie %}
{% details Montrer le code d'exemple %}
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

### Étape 2 : Créer une fabrique de notifications personnalisées

Dans votre application, créez un nouveau fichier nommé `MyCustomNotificationFactory.kt` qui étend [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) pour gérer l'affichage des présentations RemoteView personnalisées.

Dans l'exemple suivant, Superb Owl a créé une usine de notification personnalisée pour afficher une mise en page RemoteView pour les matchs en cours. Dans l' [étape suivante](#android_step-3-map-custom-data), ils créeront une nouvelle méthode appelée `getTeamInfo` pour mapper les données d'une équipe à l'activité.

{% details Montrer le code d'exemple %}
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

### Étape 3 : Mappage de données personnalisées

Dans `MyCustomNotificationFactory.kt`, créez une nouvelle méthode pour traiter les données lorsque des mises à jour en direct sont affichées.

Superb Owl a créé la méthode suivante pour mapper le nom et le logo de chaque équipe aux lignes/en production/instantanées étendues :

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

### Étape 4 : Définir la fabrique de notifications personnalisée

Dans votre classe d'application, utilisez [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)pour définir votre fabrique de notifications personnalisée.

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

### Étape 5 : Envoyer l'activité

Vous pouvez utiliser le point d'arrivée de l'API [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) REST API endpoint pour envoyer une notification push à l'appareil Android d'un utilisateur.

#### Exemple de commande curl

Superb Owl a envoyé sa requête en utilisant la commande curl suivante :

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
Bien que les commandes curl soient utiles pour les tests, nous recommandons de gérer cet appel dans votre backend où vous gérez déjà vos [activités iOS Live.]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift)
{% endalert %}

#### Paramètres de demande

| Clé                           | Description                                                                                                                                                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REST_API_KEY`                | Une clé API Braze REST avec des autorisations `messages.send`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**.                                                                                                     |
| `BRAZE_REST_ENDPOINT`         | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints).                                                                                                                  |
| `USER_ID`                     | L'ID de l'utilisateur auquel vous envoyez la notification.                                                                                                                                                                                          |
| `messages.android_push.title` | Titre du message. Par défaut, elle n'est pas utilisée pour les notifications en ligne/en production/instantanée de la fabrique de notifications personnalisée, mais elle peut être utilisée comme solution de repli.                                                                                                    |
| `messages.android_push.alert` | Le corps du message. Par défaut, elle n'est pas utilisée pour les notifications en ligne/en production/instantanée de la fabrique de notifications personnalisée, mais elle peut être utilisée comme solution de repli.                                                                                                     |
| `messages.extra`              | Paires clé-valeur que la fabrique de notifications personnalisée utilise pour les notifications en ligne/en production/instantanée. Vous pouvez attribuer n'importe quelle chaîne de caractères à cette valeur. Toutefois, dans l'exemple ci-dessus, `live_updates` est utilisé pour déterminer s'il s'agit d'une notification push par défaut ou en direct.  |
| `ASSIGNED_NOTIFICATION_ID`    | L'ID de notification que vous souhaitez attribuer à la notification en ligne/instantanée de l'utilisateur choisi. L'ID doit être unique pour ce jeu et doit être utilisé pour [mettre à jour la notification existante](#android_step-4-update-data-with-the-braze-rest-api) ultérieurement. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Étape 6 : Mettre à jour l'activité

Pour mettre à jour la notification RemoteView existante avec de nouvelles données, modifiez les paires clé-valeur pertinentes attribuées à `messages.extra`, puis utilisez le même `notification_id` et appelez à nouveau le point de terminaison `/messages/send`.

## Notifications push personnalisées

Les notifications push peuvent afficher des informations spécifiques à l’utilisateur dans une hiérarchie de vue personnalisée. Dans l'exemple suivant, un déclencheur API est utilisé pour envoyer une notification push personnalisée à un utilisateur afin qu'il puisse suivre sa progression après avoir accompli une tâche spécifique dans l'application.

![Exemple de tableau de bord personnalisé]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

Pour configurer un push personnalisé dans le tableau de bord, enregistrez la catégorie spécifique que vous souhaitez voir s'afficher, puis définissez tous les attributs utilisateur pertinents que vous souhaitez afficher à l'aide de Liquid.

![Exemple de tableau de bord personnalisé]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}
