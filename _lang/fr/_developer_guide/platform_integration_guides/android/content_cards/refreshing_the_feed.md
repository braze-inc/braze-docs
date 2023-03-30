---
nav_title: Rafraîchir le flux
article_title: Rafraîchir le flux de cartes de contenu pour Android et FireOS
page_order: 4
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique comment implémenter le rafraîchissement de la carte de contenu dans votre application Android ou FireOS."
channel:
  - cartes de contenu

---

# Rafraîchir les cartes de contenu

Vous pouvez mettre en fil d’attente un rafraîchissement manuel des cartes de contenu Braze à tout moment en appelant :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).requestContentCardsRefresh(false);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh(false)
```

{% endtab %}
{% endtabs %}

Consultez notre [KDoc correspondant][1] pour plus d’informations sur cette méthode.

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html
