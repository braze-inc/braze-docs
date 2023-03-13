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

## Demande du nombre de cartes de contenu non lues

Vous pouvez à tout moment [demander le nombre de cartes non lues][1]  en utlisant :

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

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html
