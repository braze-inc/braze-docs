---
nav_title: Receptor de transmissão de retorno de chamada push
article_title: Retorno de chamada do receptor de transmissão personalizado para Android
description: "Este artigo de referência aborda a criação de um receptor de transmissão personalizado para notificações por push do Android"
---

# Tratamento personalizado para recebimento de push, aberturas, dispensas e pares de valores-chave via Broadcast Receiver {#android-push-listener-broadcast-receiver}

{% alert important %}
O uso de um `BroadcastReceiver` personalizado para notificações por push foi descontinuado. Use [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) em vez disso.
{% endalert %}

O Braze também transmite intenções personalizadas quando as notificações por push são recebidas, abertas ou descartadas. Se você tiver um caso de uso específico para esses cenários (como a necessidade de ouvir pares de valores-chave personalizados ou o tratamento proprietário de deep links), precisará ouvir essas intenções criando um `BroadcastReceiver` personalizado.

## Etapa 1: Registre seu BroadcastReceiver

Registre seu `BroadcastReceiver` personalizado para ouvir as intenções de abertura e recebimento de push do Braze em seu [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml):

```xml
<receiver android:name="YOUR-BROADCASTRECEIVER-NAME" android:exported="false" >
  <intent-filter>
    <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
  </intent-filter>
</receiver>
```

## Etapa 2: Criar seu BroadcastReceiver

Seu receptor deve lidar com as intenções transmitidas pelo Braze e iniciar sua atividade com elas:

- Ele deve ser uma subclasse [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver.html) e sobrescrever `onReceive()`.
- O método `onReceive()` deve ouvir as intenções transmitidas pelo Braze.
  - Uma intenção de `NOTIFICATION_RECEIVED` será recebida quando uma notificação por push chegar.
  - Uma intenção `NOTIFICATION_OPENED` será recebida quando o usuário clicar em uma notificação por push.
  - Uma intenção de `NOTIFICATION_DELETED` será recebida quando uma notificação por push for descartada (deslizada para longe) pelo usuário.
- Ele deve executar sua lógica personalizada para cada um desses casos. Se seu receptor abrir deep links, desative a abertura automática de deep linking configurando `com_braze_handle_push_deep_links_automatically` para `false` em seu `braze.xml`.

Para obter um exemplo detalhado de receptor personalizado, consulte os seguintes trechos de código:

{% tabs %}
{% tab JAVA %}

```java
public class CustomBroadcastReceiver extends BroadcastReceiver {
  private static final String TAG = CustomBroadcastReceiver.class.getName();

  @Override
  public void onReceive(Context context, Intent intent) {
    String pushReceivedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED;
    String notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED;
    String notificationDeletedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_DELETED;

    String action = intent.getAction();
    Log.d(TAG, String.format("Received intent with action %s", action));

    if (pushReceivedAction.equals(action)) {
      Log.d(TAG, "Received push notification.");
    } else if (notificationOpenedAction.equals(action)) {
      BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent);
    } else if (notificationDeletedAction.equals(action)) {
      Log.d(TAG, "Received push notification deleted intent.");
    } else {
      Log.d(TAG, String.format("Ignoring intent with unsupported action %s", action));
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomBroadcastReceiver : BroadcastReceiver() {
  override fun onReceive(context: Context, intent: Intent) {
    val pushReceivedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED
    val notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED
    val notificationDeletedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_DELETED

    val action = intent.action
    Log.d(TAG, String.format("Received intent with action %s", action))

    when (action) {
      pushReceivedAction -> {
        Log.d(TAG, "Received push notification.")
      }
      notificationOpenedAction -> {
        BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent)
      }
      notificationDeletedAction -> {
        Log.d(TAG, "Received push notification deleted intent.")
      }
      else -> {
        Log.d(TAG, String.format("Ignoring intent with unsupported action %s", action))
      }
    }
  }

  companion object {
    private val TAG = CustomBroadcastReceiver::class.java.name
  }
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Com os botões de ação de notificação, as intenções `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` são acionadas quando os botões com ações `opens app` ou `deep link` são clicados. A administração de deep linking e extras permanece a mesma. Os botões com ações do `close` não disparam as intenções do `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` e dispensam a notificação automaticamente.
{% endalert %}

## Etapa 3: Acessar pares de valores-chave personalizados

Os pares de chave-valor personalizados enviados por meio do dashboard ou das APIs de envio de mensagens estarão acessíveis em seu receptor de transmissão personalizado para qualquer finalidade que você escolher:

{% tabs %}
{% tab JAVA %}

```java
// intent is the Braze push intent received by your custom broadcast receiver.
String deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY);

// The extras bundle extracted from the intent contains all custom key-value pairs.
Bundle extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY);

// example of getting specific key-value pair from the extras bundle.
String myExtra = extras.getString("my_key");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// intent is the Braze push intent received by your custom broadcast receiver.
val deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY)

// The extras bundle extracted from the intent contains all custom key-value pairs.
val extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY)

// example of getting specific key-value pair from the extras bundle.
val myExtra = extras.getString("my_key")
```

{% endtab %}
{% endtabs %}

{% alert note %}
Para obter a documentação sobre as chaves de dados push da Braze, consulte o [SDK do Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html?query=object%20Constants).
{% endalert %}

