---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur de fil d’actualité pour le Web
platform: Web
page_order: 1
page_type: reference
description: "Cet article explique comment utiliser les paires clé-valeur dans vos cartes de fil d’actualités via le SDK Braze."
channel: news feed

---

# Paires clé-valeur

> Cet article explique comment utiliser les paires clé-valeur dans vos cartes de fil d’actualités via le SDK Braze.

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Les objets `Card` peuvent éventuellement porter des paires clé-valeur comme `extras`. Ces données peuvent être utilisées pour envoyer des données avec une carte pour une manipulation ultérieure par l’application. Appelez `card.extras` pour accéder à ces valeurs.

Consultez les JSDocs pour plus d'informations sur [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) et [CaptionedImage.](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)

