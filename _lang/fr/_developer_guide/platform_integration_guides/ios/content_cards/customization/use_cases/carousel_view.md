---
nav_title: Vue carrousel
article_title: Vue Carrousel de carte de contenu pour iOS
platform: iOS
page_order: 5
description: "Cet article traite de l’implémentation d’un cas d’usage de vue carrousel de cartes de contenu pour les applications iOS."
channel:
  - cartes de contenu
---

# Cas d’utilisation : Vue carrousel

![Exemple d’application d’actualités montrant le carrousel des cartes de contenu dans un article.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Cette section couvre l’implémentation d’un flux de carrousel multi-cartes dans lequel un utilisateur peut faire glisser horizontalement pour afficher des cartes en vedette supplémentaires. Pour intégrer une vue carrousel, vous devez utiliser une implémentation entièrement personnalisée de cartes de contenu : la phase « courir » de l’[approche ramper, marcher, courir][1].

Avec cette approche, vous n’utiliserez pas les vues de Braze ni la logique par défaut, mais afficherez plutôt les cartes de contenu de manière entièrement personnalisée en utilisant vos propres vues avec les données des modèles Braze.

En termes de niveau d’effort de développement, les différences clés entre l’implémentation de base et celle du carrousel comprennent :

- Construire vos propres vues
- Enregistrer les métriques des performances de contenu
- Introduire une logique additionnelle côté client pour dicter combien et quelles cartes afficher dans le carrousel

## Mise en œuvre

### Étape 1 : Créer un contrôleur de visualisation personnalisé

Pour créer le carrousel de cartes de contenu, créez votre propre contrôleur de visualisation personnalisée (comme `UICollectionViewController`) et [souscrivez aux mises à jour des données]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/integration/#getting-the-data). Notez que vous ne pourrez pas étendre ou sous-classer la valeur par défaut `ABKContentCardTableViewController` de Braze, car il est uniquement capable de gérer nos types de cartes de contenu par défaut.

### Étape 2 : Implémenter l’analytique

Lors de la création d’un contrôleur de vue entièrement personnalisé, les impressions, les clics et les rejets de cartes de contenu ne sont pas automatiquement enregistrés. Vous devez implémenter les méthodes d’analytique respectives pour vous assurer que les impressions, les événements de rejet et les clics sont correctement enregistrés dans l’analytique de tableau de bord de Braze.

Pour plus d’informations sur les méthodes d’analytique, consultez les [Méthodes de cartes]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/integration/#card-methods). 

{% alert note %}
La même page détaille également les différentes propriétés héritées de notre classe de modèle de carte de contenu générique, que vous pouvez trouver utile pendant l’implémentation de votre vue.
{% endalert %}

### Étape 3 : Créer un observateur de carte de contenu

Créez un [Observateur de carte de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/#step-2-set-up-a-content-card-listener) chargé de la gestion de l’arrivée des cartes de contenu et de l’implémentation de la logique conditionnelle permettant d’afficher un nombre spécifique de cartes dans le carrousel à tout moment. Par défaut, les cartes de contenu sont triées par date de création (la plus récente en premier) et un utilisateur voit toutes les cartes auxquelles il est éligible.

Cela dit, vous pouvez commander et appliquer une logique d’affichage supplémentaire de différentes manières. Par exemple, vous pouvez sélectionner les cinq premiers objets de carte de contenu du tableau ou introduire des paires clé-valeur (la propriété `extras` dans le modèle de données) pour concevoir une logique conditionnelle.

Si vous implémentez un carrousel en tant que flux de cartes de contenu secondaire, reportez-vous à [Utilisation de plusieurs flux de cartes de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/) pour vous assurer que vous triez les cartes dans le flux approprié en fonction des paires clé-valeur.

{% alert important %}
Il est important de s’assurer que vos équipes marketing et développeurs coordonnent les paires clé-valeur (par ex., `feed_type = brand_homepage`), car toute entrée par les marketeurs de paires clé-valeur dans le tableau de bord de Braze doit correspondre exactement aux paires clé-valeur que les développeurs construisent dans la logique de l’application.
{% endalert %}

Pour la documentation du développeur spécifique à iOS sur la classe Cartes de Contenu, les méthodes et les attributs, reportez-vous au document iOS [référence de classe `ABKContentCard`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Considérations

- En utilisant des vues entièrement personnalisées, vous ne pourrez pas étendre ou sous-classer les méthodes utilisées dans `ABKContentCardsController`. Vous devrez à la place intégrer les méthodes et les propriétés du modèle de données vous-même.
- La logique et l’implémentation de la vue carrousel ne sont pas un type par défaut de carte de contenu dans Braze. Par conséquent la logique d’obtention du cas d’usage doit être fournie et prise en charge par votre équipe de développement.
- Vous devrez implémenter la logique côté client pour afficher un nombre spécifique de cartes dans le carrousel à tout moment.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches
