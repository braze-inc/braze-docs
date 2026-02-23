---
nav_title: Atualizações ao vivo para Android
article_title: Atualizações ao Vivo para o SDK Braze do Android
page_order: 0.1
description: "Aprenda como configurar Atualizações ao Vivo para o SDK Braze do Android."
platform: 
  - Android
  - FireOS
hidden: true
---

# Atualizações ao vivo para Android

> Aprenda como usar Atualizações ao Vivo do Android no SDK Braze, também conhecido como [Notificações Centricas de Progresso](https://developer.android.com/about/versions/16/features/progress-centric-notifications). Essas notificações são semelhantes a [Atividades ao Vivo para o SDK Braze do Swift]({{site.baseurl}}/developer_guide/live_notifications/live_activities), permitindo que você exiba notificações interativas na tela de bloqueio. O Android 16 introduz notificações centradas em progresso para ajudar os usuários a acompanhar perfeitamente jornadas iniciadas pelo usuário, do início ao fim.

## Como funciona?

Você pode usar a interface [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para personalizar como as notificações push do Braze são exibidas. Ao estender `BrazeNotificationFactory`, o Braze chamará o método `createNotification()` da sua fábrica antes que a notificação seja exibida ao usuário. Em seguida, ele passará uma carga útil contendo pares de chave-valor personalizados enviados através do painel do Braze ou da API REST.

## Exibindo uma Atualização ao Vivo

Nesta seção, você fará parceria com o Superb Owl, o anfitrião de um novo programa de jogos onde equipes de resgate de vida selvagem competem para ver quem consegue salvar mais corujas. Eles estão procurando aproveitar as Atualizações ao Vivo em seu aplicativo Android, para que possam exibir o status de uma partida em andamento e fazer atualizações dinâmicas na notificação em tempo real.

![Um exemplo de Atualização ao Vivo do Android]({% image_buster /assets/img/android/android-live-update.png %}){: style="max-width:40%;"}

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### Etapa 1: Criar uma fábrica de notificações personalizada

Em seu aplicativo, crie um novo arquivo chamado `MyCustomNotificationFactory.kt` que estenda [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para lidar com a forma como as Atualizações ao Vivo do Braze são exibidas.

No exemplo a seguir, o Superb Owl criou uma fábrica de notificações personalizada para exibir uma Atualização ao Vivo para partidas em andamento. No próximo passo, você criará um novo método chamado `getTeamInfo` para mapear os dados de uma equipe para a atividade.

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

Em `MyCustomNotificationFactory.kt`, crie um novo método para lidar com dados quando as Atualizações ao Vivo forem exibidas.

Superb Owl criou o seguinte método para mapear o nome e o logotipo de cada equipe para Atualizações Ao Vivo expandidas:

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

### Etapa 3: Defina a fábrica de notificações personalizada

Na sua classe de aplicativo, use [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?) para definir sua fábrica de notificações personalizada.

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Etapa 4: Envie a atividade

Você pode usar o endpoint da API REST [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) para enviar uma notificação por push para o dispositivo Android de um usuário.

#### Exemplo de comando curl

Superb Owl enviou sua solicitação usando o seguinte comando curl:

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
Embora os comandos curl sejam úteis para testes, recomendamos lidar com essa chamada em seu backend, onde você já está lidando com suas [Atividades Ao Vivo do iOS]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift).
{% endalert %}

#### Parâmetros de solicitação

| Chave                          | Descrição |
|------------------------------|------------|
| `REST_API_KEY`               | Uma chave da API REST da Braze com permissões `messages.send`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| `BRAZE_REST_ENDPOINT`         | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
| `USER_ID`                    | O ID do usuário para quem você está enviando a notificação. |
| `messages.android_push.title` | O título da mensagem. Por padrão, isso não é usado para as notificações ao vivo da fábrica de notificações personalizada, mas pode ser usado como um fallback. |
| `messages.android_push.alert` | O corpo da mensagem. Por padrão, isso não é usado para as notificações ao vivo da fábrica de notificações personalizada, mas pode ser usado como um fallback. |
| `messages.extra`             | Pares chave-valor que a fábrica de notificações personalizada usa para notificações ao vivo. Você pode atribuir qualquer string a este valor—no entanto, no exemplo acima, `live_updates` é usado para determinar se é uma notificação por push padrão ou ao vivo. |
| `ASSIGNED_NOTIFICATION_ID`   | O ID da notificação que você deseja atribuir à notificação ao vivo do usuário escolhido. O ID deve ser exclusivo para este jogo e deve ser usado para [atualizar a notificação existente](#android_step-4-update-data-with-the-braze-rest-api) mais tarde. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Etapa 5: Atualizar a atividade

Para atualizar a Atualização Ao Vivo existente com novos dados, modifique os pares chave-valor relevantes atribuídos a `messages.extra`, em seguida, use o mesmo `notification_id` e chame o endpoint `/messages/send` novamente.
