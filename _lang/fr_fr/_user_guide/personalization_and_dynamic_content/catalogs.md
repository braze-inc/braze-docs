---
nav_title: Catalogues
article_title: Catalogues
page_order: 6
layout: dev_guide

guide_top_header: "Catalogues"
guide_top_text: "Les catalogues accèdent aux données des fichiers CSV importés et des points d'extrémité des API pour enrichir vos messages, de la même manière que vous accédez aux attributs personnalisés ou aux propriétés d'événements personnalisés via Liquid."

description: "Cette page d’accueil présente tout ce qui concerne les catalogues. Utilisez les catalogues et les ensembles filtrés pour exploiter les données des non-utilisateurs dans vos campagnes Braze afin d'envoyer des messages personnalisés."

guide_featured_title: "Section Articles"
guide_featured_list:
- name: Création d’un catalogue
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/
  image: /assets/img/braze_icons/users-01.svg
- name: Utilisation des catalogues
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/
  image: /assets/img/braze_icons/users-01.svg
- name: Notifications de rupture de stock
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Notifications de baisse de prix
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Sélections
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/selections/
  image: /assets/img/braze_icons/list.svg
- name: Endpoints des API de catalogues
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg

guide_menu_title: "Other articles"
guide_menu_list:
- name: Blocs de produits à glisser-déposer
  link: /docs/dnd_product_blocks/
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Cas d'utilisation du catalogue

Vous pouvez ajouter n’importe quel type de données à un catalogue. Généralement, les données sont des métadonnées sur les offres, telles que les produits, les remises, les promotions, les événements, etc. Consultez les cas d'utilisation ci-dessous pour obtenir quelques exemples de la façon dont vous pouvez utiliser ces données pour cibler les utilisateurs avec des messages très pertinents.

### Retail et e-commerce

- **Promotions saisonnières :** Importez des collections de produits saisonniers et personnalisez les messages en fonction des tendances actuelles.
- **Messages localisés :** Importez les adresses, heures et services de vos emplacements, puis personnalisez les notifications en fonction des emplacements des utilisateurs.
- **Notifications de rupture de stock :** Importez des informations sur les produits qui incluent la quantité de stock, puis utilisez les [notifications de retour en stock]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/) et les événements personnalisés de Braze pour déclencher une campagne ou un Canvas qui envoie aux utilisateurs une notification indiquant qu'un produit est désormais en stock.
- **Notifications de baisse de prix :** Importez des informations sur les produits qui incluent leurs prix, puis utilisez les [notifications de baisse de prix]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications/) et les événements personnalisés de Braze pour déclencher un Canvas qui envoie aux utilisateurs une notification indiquant que le prix d'un produit a baissé.

### Divertissement

- **Plans d'abonnement :** Importez des plans d'abonnement et faites la promotion de modules complémentaires auprès de vos utilisateurs en fonction de leurs habitudes d'utilisation et des types de contenu qu'ils consomment le plus souvent.
- **Événements à venir :** Importez les listes d'événements à venir, leurs emplacements et l'âge de l'audience, puis envoyez des notifications personnalisées aux utilisateurs qui se trouvent dans la zone concernée et qui appartiennent au groupe d'âge ciblé.
- **Préférences en matière de médias :** Importez des informations sur les films et les émissions, puis recommandez du contenu à vos utilisateurs en fonction de leurs titres favoris et des genres les plus regardés.

### Voyages et hôtellerie

- **Destinations :** Importez des destinations de voyage et leurs attractions, restaurants et activités les plus populaires, puis personnalisez des recommandations à vos utilisateurs en fonction de leurs voyages précédents.
- **Hébergement :** Importez des établissements hôteliers et leurs équipements, types de chambres et tarifs, puis envoyez des promotions à vos utilisateurs en fonction des préférences qu'ils ont sélectionnées.
- **Modes de voyage** : Importez des offres et des promotions pour les modes de voyage (vols, trains, voitures de location et autres), puis envoyez-les à vos utilisateurs en fonction de l'historique de leurs recherches récentes.
- **Préférences en matière de repas :** Importer des informations sur les offres de repas et utiliser les [sélections]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) pour envoyer des messages personnalisés aux utilisateurs qui ont des préférences spécifiques en matière de repas, en fonction de la catégorie d'aliments qu'ils ont consultée le plus récemment.

## Comment les catalogues et Liquid fonctionnent-ils ensemble ?

Les catalogues sont une fonctionnalité de stockage de données. Ils contiennent de vastes ensembles de données qui peuvent être référencés dans vos messages à des fins de personnalisation. Pour faire référence aux données, vous utiliserez [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) comme langage de modélisation. En d'autres termes, les catalogues sont le lieu de stockage des données, et Liquid est le langage qui extrait les données pertinentes du lieu de stockage.

Pour des exemples de la façon dont vous pouvez utiliser Liquid pour extraire des informations de catalogue, voir les cas d'utilisation supplémentaires dans [Création d'un catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases/).

#### Limites du stockage des données

Le stockage des données pour les catalogues est limité en fonction de la taille des articles et des sélections du catalogue, qui peut être différente de la taille des fichiers CSV téléchargés.

Pour la version gratuite des catalogues, la quantité de stockage autorisée est de 100 Mo. Vous pouvez avoir un nombre illimité d'éléments tant que l'espace de stockage ne dépasse pas 100 Mo. Les sélections contribueront à votre stockage. Plus une sélection est complexe, plus elle occupera de place.

Pour Catalogues Pro, les options de taille de stockage sont les suivantes : 5 GB, 10 GB, 15 GB ou 50 GB. Notez que l'espace de stockage de la version gratuite (100 Mo) est inclus dans chacun de ces plans.
