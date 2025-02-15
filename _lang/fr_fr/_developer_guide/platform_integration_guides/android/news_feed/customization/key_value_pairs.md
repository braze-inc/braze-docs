---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur de fil d’actualité pour Android et FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique comment utiliser les paires clé-valeur de fil d'actualité dans votre application Android ou FireOS."
channel:
  - news feed

---

# Paires clé-valeur

> Cet article de référence explique comment utiliser les paires clé-valeur de fil d'actualité dans votre application Android ou FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Les objets `Card` peuvent éventuellement porter des paires clé-valeur comme `extras`. Elles peuvent être utilisées pour envoyer des données avec une `Card` pour une manipulation ultérieure par l’application.

Appelez les éléments suivants sur un objet `Card` pour récupérer ses compléments :

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
