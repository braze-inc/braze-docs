---
nav_title: Atualizações ao vivo para Android
article_title: Atualizações em tempo real para o SDK do Android Braze
page_order: 0.1
description: "Saiba como configurar o Live Updates para o SDK do Android Braze."
platform: 
  - Android
  - FireOS
---

# Atualizações ao vivo para Android

> Saiba como usar as atualizações ao vivo do Android no Braze SDK, também conhecidas como [notificações centradas no progresso](https://developer.android.com/about/versions/16/features/progress-centric-notifications). Essas notificações são semelhantes às [Live Activities do SDK do Swift Braze]({{site.baseurl}}/developer_guide/live_notifications/live_activities), permitindo a exibição de notificações interativas na tela de bloqueio. O Android 16 apresenta notificações centradas no progresso para ajudar os usuários a rastrear perfeitamente as jornadas iniciadas pelo usuário, do início ao fim.

## Como funciona?

Você pode usar a interface [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para personalizar como as notificações por push do Braze são exibidas. Ao estender o site `BrazeNotificationFactory`, o Braze chamará o método `createNotification()` de sua fábrica antes que a notificação seja exibida ao usuário. Em seguida, ele passará uma carga útil contendo pares de chave-valor personalizados enviados pelo dashboard do Braze ou pela API REST.

## Exibição de uma atualização ao vivo

Nesta seção, você fará parceria com a Superb Owl, a apresentadora de um novo game show em que equipes de resgate de animais selvagens competem para ver quem consegue salvar mais corujas. Eles querem aproveitar o Live Updates em seu app para Android, para que possam exibir o status de uma partida em andamento e fazer atualizações dinâmicas na notificação em tempo real.

![Um exemplo de atualização ao vivo do Android]({% image_buster /assets/img/android/android-live-update.png %}){: style="max-width:40%;"}

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### Etapa 1: Criar uma fábrica de notificações personalizada

Em seu aplicativo, crie um novo arquivo chamado `MyCustomNotificationFactory.kt` que estende [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para lidar com a forma como as atualizações do Braze Live são exibidas.

No exemplo a seguir, a Superb Owl criou uma fábrica de notificações personalizada para exibir uma atualização ao vivo das partidas em andamento. Na próxima etapa, você criará um novo método chamado `getTeamInfo` para mapear os dados de uma equipe para a atividade.

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

### Etapa 2: Mapear dados personalizados

Em `MyCustomNotificationFactory.kt`, crie um novo método para tratar os dados quando as atualizações ao vivo forem exibidas.

A Superb Owl criou o seguinte método para mapear o nome e o logotipo de cada equipe para as atualizações ao vivo expandidas:

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

### Etapa 3: Definir a fábrica de notificações personalizadas

Em sua classe de aplicativo, use [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)para definir sua fábrica de notificações personalizada.

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Etapa 4: Enviar a atividade

Você pode usar o endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) REST API para enviar uma notificação por push para o dispositivo Android de um usuário.

#### Exemplo de comando curl

A Superb Owl enviou sua solicitação usando o seguinte comando curl:

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
Embora os comandos curl sejam úteis para testes, recomendamos lidar com essa chamada no backend, onde você já está lidando com as [iOS Live Activities]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift).
{% endalert %}

#### Parâmetros de solicitação

| Chave                          | Descrição |
|------------------------------|------------|
| `REST_API_KEY`               | Uma chave da API REST da Braze com permissões `messages.send`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| `BRAZE_REST_ENDPOINT`         | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
| `USER_ID`                    | O ID do usuário para o qual você está enviando a notificação. |
| `messages.android_push.title` | O título da mensagem. Por padrão, isso não é usado para as notificações ao vivo da fábrica de notificações personalizadas, mas pode ser usado como fallback. |
| `messages.android_push.alert` | O corpo da mensagem. Por padrão, isso não é usado para as notificações ao vivo da fábrica de notificações personalizadas, mas pode ser usado como fallback. |
| `messages.extra`             | Pares de valores-chave que a fábrica de notificações personalizadas usa para notificações ao vivo. Você pode atribuir qualquer string a esse valor; no entanto, no exemplo acima, `live_updates` é usado para determinar se é uma notificação por push padrão ou ao vivo. |
| `ASSIGNED_NOTIFICATION_ID`   | O ID de notificação que deseja atribuir à notificação ao vivo do usuário escolhido. O ID deve ser exclusivo para esse jogo e deve ser usado para [atualizar a notificação existente](#android_step-4-update-data-with-the-braze-rest-api) posteriormente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Etapa 5: Atualizar a atividade

Para atualizar o Live Update existente com novos dados, modifique os pares de valores-chave relevantes atribuídos a `messages.extra` e, em seguida, use o mesmo `notification_id` e chame novamente o ponto de extremidade `/messages/send`.
