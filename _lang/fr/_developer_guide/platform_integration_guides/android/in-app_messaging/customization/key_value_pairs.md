---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur de message in-app pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 6.9
description: "Cet article de référence couvre les paires clé-valeur de messagerie in-app pour votre application Android ou FireOS."
channel:
  - messages In-App

---

# Compléments de paires clé-valeur

Les objets de message in-app peuvent porter des paires clé-valeur comme `extras`. Elles sont spécifiés sur le tableau de bord sous **Paramètres** lors de la création d’une campagne de messages in-app. Elles peuvent être utilisées pour envoyer des données avec un message in-app pour un traitement ultérieur par l’application.

Appelez ce qui suit lorsque vous obtenez un objet de message in-app pour récupérer ses compléments :

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

Consultez ce [KDoc][44] pour plus d’informations.

[44]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721
