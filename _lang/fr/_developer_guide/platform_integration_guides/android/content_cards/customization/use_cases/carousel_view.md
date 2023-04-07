---
nav_title: Vue carrousel
article_title: Cartes de contenu en vue carrousel pour Android et FireOS
page_order: 10
platform: 
  - Android
  - FireOS
description: "Cet article traite de l’implémentation d’un cas d’usage de vue carrousel de cartes de contenu pour les applications Android et FireOS."
channel:
  - cartes de contenu

---

# Vue carrousel

![Exemple d’application d’actualités montrant le carrousel des cartes de contenu dans un article]({% image_buster/assets/img_archive/cc_politer_carousel_android.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;"}

Cette section couvre l’implémentation d’un flux de carrousel multi-cartes dans lequel un utilisateur peut faire glisser horizontalement pour afficher des cartes en vedette supplémentaires. Pour intégrer une vue carrousel, vous devez utiliser une implémentation entièrement personnalisée de cartes de contenu : la phase « courir » de l’[approche ramper, marcher, courir][1].

Avec cette approche, vous n’utiliserez pas les vues de Braze ni la logique par défaut, mais afficherez plutôt les cartes de contenu de manière entièrement personnalisée en utilisant vos propres vues avec les données des modèles Braze.

En termes de niveau d’effort de développement, les différences clés entre l’implémentation de base et celle du carrousel comprennent :

- Construire vos propres vues
- Enregistrer les métriques des performances de contenu
- Introduire une logique additionnelle côté client pour dicter combien et quelles cartes afficher dans le carrousel

## Mise en œuvre

### Étape 1 : Créer un contrôleur de visualisation personnalisé

Pour créer le carrousel de cartes de contenu, créez vos propres vues personnalisées et [abonnez-vous aux mises à jour des données]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/#fully-custom-content-card-display-for-android). Notez que vous ne pourrez pas utiliser la valeur par défaut de `ContentCardFragment` de Braze, car il est uniquement capable de gérer nos types de carte de contenu par défaut.

### Étape 2 : Implémenter l’analytique

Lors de la création d’un contrôleur de vue entièrement personnalisé, les impressions, les clics et les rejets de cartes de contenu ne sont pas automatiquement enregistrés. Vous devez implémenter les méthodes d’analytique respectives pour vous assurer que les impressions, les événements de rejet et les clics sont correctement enregistrés dans l’analytique de tableau de bord de Braze.

Pour plus d’informations sur les méthodes d’analytique, consultez les [métriques des performances des cartes]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/#card-methods).

{% alert note %}
La même page détaille également les différentes propriétés héritées de notre classe de modèle de carte de contenu générique, que vous pouvez trouver utile pendant l’implémentation de votre vue.
{% endalert %}

### Étape 3 : Créer un gestionnaire de mise à jour de carte de contenu

Suivez les étapes pour l’[utilisation de plusieurs flux de cartes de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/multiple_feeds/) pour définir des paires clé-valeur sur les cartes et créer un gestionnaire de mise à jour de carte de contenu.

{% alert important %}
Il est important de veiller à ce que vos équipes marketing et de développeurs coordonnent les paires clé-valeur (par ex., `feed_type = brand_homepage`), car toute paire clé-valeur utilisée doit correspondre aux paires clé-valeur que les développeurs construisent dans la logique de l’application.
{% endalert %}

Pour obtenir la documentation développeur spécifique à Android sur la classe des cartes de contenu, les méthodes et les attributs en Kotlin, consultez la documentation [com.braze.ui.contentcards.view](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/index.html) Android.

## Considérations

- En utilisant des vues entièrement personnalisées, vous ne pourrez pas étendre ou sous-classer les méthodes utilisées dans `ABKContentCardsController`. Vous devrez à la place intégrer les méthodes et les propriétés du modèle de données vous-même.
- La logique et l’implémentation de la vue carrousel ne sont pas un type par défaut de carte de contenu dans Braze. Par conséquent la logique d’obtention du cas d’usage doit être fournie et prise en charge par votre équipe de développement.
- Vous devrez implémenter la logique côté client pour afficher un nombre spécifique de cartes dans le carrousel à tout moment.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches
