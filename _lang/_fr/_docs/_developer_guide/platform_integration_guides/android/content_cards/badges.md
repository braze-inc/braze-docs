---
nav_title: Badges
article_title: Badges de carte de contenu pour Android/FireOS
page_order: 5
platform:
  - Android
  - Pare-feu
description: "Cet article explique comment ajouter des badges à vos Cartes de Contenu dans votre application Android."
channel:
  - cartes de contenu
---

# Ajout d'un badge

Vous pouvez [demander le nombre de cartes non lues][1] à tout moment en appelant :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(contexte).getContentCardUnviewedCount();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endtab %}
{% endtabs %}

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/get-content-card-unviewed-count.html
