---
nav_title: Pares Chave-Valor
article_title: Pares de chave-valor de mensagem no app para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 6.9
description: "Este artigo de referência aborda os pares de chave/valor de mensagens no app para seu app Android ou FireOS."
channel:
  - in-app messages

---

# Pares chave-valor

> Este artigo de referência aborda os pares de chave/valor de mensagens no app para seu app Android ou FireOS.

Os objetos de mensagem no app podem conter pares de chave/valor como `extras`. Eles são especificados no dashboard em **Configurações** ao criar uma campanha de mensagem no app. Esses podem ser usados para enviar dados com uma mensagem no app para processamento posterior pelo aplicativo.

Chame o seguinte quando você receber um objeto de mensagem no app para recuperar seus extras:

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

Consulte este [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721) para saber mais.

