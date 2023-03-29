---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur de fil d’actualité pour Android et FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique comment utiliser les paires clé-valeur de fil d’actualité dans votre application Android ou FireOS."
channel:
  - fil d’actualité

---

# Paires clé-valeur

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

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
