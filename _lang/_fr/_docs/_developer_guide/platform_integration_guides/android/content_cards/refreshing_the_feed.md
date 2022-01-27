---
nav_title: Rafraîchissement du flux
article_title: Rafraîchissement du flux de carte de contenu pour Android/FireOS
page_order: 4
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre comment implémenter le rafraîchissement de la carte de contenu dans votre application Android."
channel:
  - cartes de contenu
---

# Rafraîchissement des cartes de contenu

Vous pouvez mettre en file d'attente une mise à jour manuelle des Cartes de Contenu Braze à tout moment en appelant :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(contexte).requestContentCardsRefresh(false);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(contexte).requestContentCardsRefresh(false)
```

{% endtab %}
{% endtabs %}

Pour plus d'informations sur cette méthode, veuillez consulter [notre KDoc][1] correspondant.

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/request-content-cards-refresh.html
