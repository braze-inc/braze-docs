---
nav_title: Style personnalisé
article_title: Style personnalisé de fil d’actualité pour le Web
platform: Web
page_order: 0
page_type: reference
description: "Cet article couvre les options de style personnalisé pour les fils d’actualité dans votre application Web."
channel: fil d’actualité

---

# Style personnalisé

> Cet article couvre les options de style personnalisé pour les fils d’actualité dans votre application Web.

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Les éléments de l’IU de Braze sont dotés d’un aspect et une convivialité par défaut qui correspondent aux composeurs du tableau de bord de Braze et visent à assurer la cohérence avec d’autres plateformes mobiles Braze. Les styles par défaut de Braze sont définis en CSS au sein du SDK Braze. En écrasant des styles sélectionnés dans votre application, il est possible de personnaliser notre fil standard avec vos propres images de fond, des familles de polices, des styles, des tailles, des animations, et bien plus encore.

Par exemple, voici un exemple de remplacement qui entraînera l’apparition d’un fil d'actualité de 800 px de large :

``` css
body .ab-feed {
  width: 800px;
}
```