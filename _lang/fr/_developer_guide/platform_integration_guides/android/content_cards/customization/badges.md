---
nav_title: Badges
article_title: Badges de carte de contenu pour Android et FireOS
page_order: 4.4
platform: 
  - Android
  - FireOS
description: "Cet article explique comment ajouter des badges à vos cartes de contenu dans votre application Android ou FireOS."
channel:
  - cartes de contenu

---

# Badges

## Demander le décompte des cartes de contenu non lues

Vous pouvez à tout moment [demander le nombre de cartes non lues][1] en appelant :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endtab %}
{% endtabs %}

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html
