---
nav_title: ID de publicidade do Google (opcional)
article_title: ID opcional de publicidade do Google para Android
page_order: 9
platform: 
  - Android
description: "Este artigo de referência aborda os IDs de publicidade do Google e como passar essas informações de publicidade para o Braze em seu aplicativo para Android ou FireOS."

---

# ID de publicidade do Google (somente Android)

> O [ID de publicidade do Google](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) é um ID opcional específico do usuário, anônimo, exclusivo e redefinível para publicidade, fornecido pelos serviços do Google Play. Este artigo de referência aborda os IDs de publicidade do Google e como passar essas informações de publicidade para o Braze em seu aplicativo para Android ou FireOS.

O GAID permite que os usuários redefinam seu identificador, aceitem anúncios baseados em interesses nos aplicativos do Google Play e fornece aos desenvolvedores um sistema simples e padrão para continuar a monetizar seus apps.

## Como passar o ID de publicidade do Google para o Braze

O ID de publicidade do Google não é coletado automaticamente pelo SDK da Braze e deve ser definido manualmente por meio do método [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).

{% alert important %}
O Google exige que o ID de publicidade seja coletado em um thread que não seja da UI.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Thread(Runnable {
  try {
    val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext())
    Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.id, idInfo.isLimitAdTrackingEnabled)
  } catch (e: Exception) {
    e.printStackTrace()
  }
}).start()
```

{% endtab %}
{% endtabs %}


