---
nav_title: Paires clé-valeur
article_title: Nouvelles Paires Key-Value pour Android/FireOS
page_order: 8
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre la façon d'utiliser des paires clé-valeur dans votre flux d'actualités pour votre application Android."
channel:
  - fil d'actualité
---

# Paires clé-valeur

`Les objets` de la carte peuvent éventuellement transporter des paires clé-valeur sous la forme `d'extras`. Celles-ci peuvent être utilisées pour envoyer des données avec une carte `` pour une gestion ultérieure par l'application.

Appeler ce qui suit sur un objet `Card` pour récupérer ses extras :

{% tabs %}
{% tab JAVA %}

```java
Carte<String, String> getExtras()
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
extras : Carte<String, String>
```

{% endtab %}
{% endtabs %}

Consultez le [Javadoc][36] pour plus d'informations.

[36]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#getExtras()
