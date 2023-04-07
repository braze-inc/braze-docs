---
nav_title: Catégories de fil d’actualité
page_order: 9

page_type: reference
description: "Cet article de référence décrit les différentes catégories de fil d’actualité qui vous permettent d’intégrer plusieurs instances du fil d’actualités dans votre application."
tool: Dashboard
channel: fil d’actualité
---

# Catégories de fil d’actualité

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Les catégories de fil d’actualité vous permettent d’intégrer plusieurs instances du fil d’actualités dans votre application. Il est possible d’intégrer des fils d’actualité dans différentes fenêtres qui affichent uniquement une certaine catégorie de cartes de fil d’actualité.

![Panneau du Fil d’actualité présentant un aperçu de la carte d’image avec légende pour un élément de fil d’actualité intitulé « Vous adorez les sucreries ? Venez découvrir tous nos bonbons ! » accompagné du message « Rendez-nous visite en magasin pour découvrir des bonbons irrésistibles ! Mentionnez cette publicité et obtenez 50 % de réduction sur votre premier sac de bonbons. » Les catégories de fil d’actualité incluent quatre cases à cocher : News (Actualités), Announcements (Annonces), Advertising (Publicité) et Social. Aucune des catégories n’est sélectionnée.][1]

Le fait qu’un fil d’actualités soit désigné comme faisant partie d’une catégorie spécifique n’est pas visible pour l’utilisateur final. Par défaut, le fil d’actualité de Braze affiche les cartes de toutes les catégories, à moins qu’un fil ne soit spécifiquement configuré dans le code d’application pour afficher uniquement certaines catégories. Pour plus d’informations sur la configuration du code de votre application, consultez l’article [Définir une catégorie de fil d’actualité][2].

[1]: {% image_buster /assets/img_archive/Newsfeed_category.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/defining_a_news_feed_category/
