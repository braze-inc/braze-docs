---
nav_title: Descarte de mensagens
article_title: Descarte de mensagens no app para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 5
description: "Este artigo de referência aborda o descarte de mensagens em seu app Android ou FireOS."
channel:
  - in-app messages

---

# Descarte de mensagem

> Este artigo de referência aborda o descarte de mensagens em seu app Android ou FireOS.

## Desativar o descarte com o botão Voltar

Por padrão, o botão Voltar do dispositivo descarta as mensagens no app da Braze. Esse comportamento pode ser desativado por mensagem via [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html). 

No exemplo a seguir, `disable_back_button` é um par chave-valor personalizado definido na mensagem no app que indica se a mensagem deve permitir que o botão de voltar dispense a mensagem:

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new DefaultInAppMessageManagerListener() {
  @Override
  public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
    final Map<String, String> extras = inAppMessage.getExtras();
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false);
    }
  }

  @Override
  public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage);
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
  }
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : DefaultInAppMessageManagerListener() {
  override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
    val extras = inAppMessage.extras
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
    }
  }

  override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage)
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
  }
})
```
{% endtab %}
{% endtabs %}

{% alert note %}
Nota que, se essa funcionalidade estiver desativada, será usado o comportamento padrão do botão Voltar do dispositivo da atividade do host. Isso pode fazer com que o botão de voltar feche o aplicativo em vez da mensagem no app exibida.
{% endalert %}

## Dispensa com toque fora do modal

O valor padrão e histórico é `false`, o que significa que cliques fora do modal não fecharão o modal. Definir esse valor como `true` resultará no fechamento da mensagem no app modal quando o usuário tocar fora da mensagem no app. Esse comportamento pode ser ativado chamando:

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

