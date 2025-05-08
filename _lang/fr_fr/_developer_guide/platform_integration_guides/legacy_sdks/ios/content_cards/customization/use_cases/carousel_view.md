---
nav_title: Vue carrousel
article_title: Vue Carrousel de carte de contenu pour iOS
platform: iOS
page_order: 5
description: "Cet article traite de l’implémentation d’un cas d’usage de vue carrousel de cartes de contenu pour les applications iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Cas d’utilisation : Vue carrousel

![Exemple d'application d'actualités montrant un carrousel de cartes de contenu dans un article.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Cette section couvre l’implémentation d’un flux de carrousel multi-cartes dans lequel un utilisateur peut faire glisser horizontalement pour afficher des cartes en vedette supplémentaires. Pour intégrer une vue carrousel, vous devrez utiliser une carte de contenu entièrement personnalisée - la phase d'exécution de l ['approche "crawl, walk, run" (ramper, marcher, courir).]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches)

Avec cette approche, vous n'utiliserez pas les vues et la logique par défaut de Braze, mais afficherez les cartes de contenu de manière totalement personnalisée en utilisant vos propres vues alimentées par les données des modèles Braze.

En termes de niveau d’effort de développement, les différences clés entre l’implémentation de base et celle du carrousel comprennent :

- Créer vos propres vues
- Enregistrer les indicateurs des performances de contenu
- Introduire une logique additionnelle côté client pour dicter combien et quelles cartes afficher dans le carrousel

## Mise en œuvre

### Étape 1 : Créer un contrôleur de visualisation personnalisé

Pour créer le carrousel de cartes de contenu, créez votre propre contrôleur de vue personnalisé (tel que `UICollectionViewController`) et [abonnez-vous aux mises à jour des données]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#getting-the-data). Notez que vous ne pourrez ni étendre ni sous-classer notre `ABKContentCardTableViewController` par défaut, car il est uniquement capable de gérer nos types de cartes de contenu par défaut.

### Étape 2 : Mettre en œuvre les analyses

Lors de la création d’un contrôleur de vue entièrement personnalisé, les impressions, les clics et les rejets de cartes de contenu ne sont pas automatiquement enregistrés. Vous devez mettre en œuvre les méthodes d'analyse correspondantes pour vous assurer que les impressions, les événements de renvoi et les clics sont correctement enregistrés dans les analyses du tableau de bord de Braze.

Pour plus d'informations sur les méthodes d'analyse, reportez-vous aux [méthodes de carte]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#card-methods). 

{% alert note %}
La même page détaille également les différentes propriétés héritées de notre classe de modèle de carte de contenu générique, que vous pouvez trouver utile pendant l’implémentation de votre vue.
{% endalert %}

### Étape 3 : Créer un observateur de carte de contenu

Créez un [observateur de cartes]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/#step-2-set-up-a-content-card-listener) de contenu chargé de gérer l'arrivée des cartes de contenu et mettez en œuvre une logique conditionnelle pour afficher un nombre spécifique de cartes dans le carrousel à tout moment. Par défaut, les cartes de contenu sont triées par date de création (la plus récente en premier) et un utilisateur voit toutes les cartes auxquelles il est éligible.

Cela dit, vous pouvez commander et appliquer une logique d’affichage supplémentaire de différentes manières. Par exemple, vous pouvez sélectionner les cinq premiers objets de carte de contenu du tableau ou introduire des paires clé-valeur (la propriété `extras` dans le modèle de données) pour concevoir une logique conditionnelle.

Si vous implémentez un carrousel comme flux secondaire de cartes de contenu, reportez-vous à la section [Utilisation de plusieurs flux de cartes de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/) pour vous assurer que vous triez les cartes dans le flux approprié en fonction des paires clé-valeur.

{% alert important %}
Il est important de veiller à ce que vos équipes de marketing et de développement se coordonnent sur les paires clé-valeur qui seront utilisées (par exemple, `feed_type = brand_homepage`), car toutes les paires clé-valeur saisies par les marketeurs dans le tableau de bord de Braze doivent correspondre exactement aux paires clé-valeur que les développeurs créent dans la logique de l'application.
{% endalert %}

Pour obtenir la documentation pour développeurs spécifique à iOS sur la classe, les méthodes et les attributs des cartes de contenu, reportez-vous à la [référence de la classe `ABKContentCard`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html) pour iOS.

## Considérations

- En utilisant des vues entièrement personnalisées, vous ne pourrez pas étendre ou sous-classer les méthodes utilisées dans `ABKContentCardsController`. Vous devrez à la place intégrer les méthodes et les propriétés du modèle de données vous-même.
- La logique et l’implémentation de la vue carrousel ne sont pas un type par défaut de carte de contenu dans Braze. Par conséquent la logique d’obtention du cas d’usage doit être fournie et prise en charge par votre équipe de développement.
- Vous devrez implémenter la logique côté client pour afficher un nombre spécifique de cartes dans le carrousel à tout moment.

