---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur de carte de contenu pour Android et FireOS
page_order: 4.2
platform: 
  - Android
  - FireOS
description: "Cet article explique comment ajouter des paires clé-valeur à vos cartes de contenu dans votre application Android ou FireOS."
channel:
  - cartes de contenu

---

# Paires clé-valeur

Les objets `Card` peuvent éventuellement porter des paires clé-valeur comme `extras`. Elles peuvent être utilisées pour envoyer des données avec une `Card` pour une manipulation ultérieure par l’application.

Consultez notre [KDoc][36] pour plus d’informations.

{% alert note %}
Les cartes de contenu ont une limite de taille maximale de 2 kb pour le contenu que vous saisissez dans le tableau de bord de Braze. Cela inclut le texte des messages, les URL d’images, les liens et les paires clé-valeur. Dépasser ce montant empêchera la carte d’être envoyée.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches
[36]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/#-2118252107%2FProperties%2F-1725759721
