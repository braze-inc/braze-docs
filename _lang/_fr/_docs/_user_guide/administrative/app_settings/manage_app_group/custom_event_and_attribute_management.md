---
nav_title: Gestion d'attributs et d'événements personnalisés
article_title: Gestion d'attributs et d'événements personnalisés
page_order: 1
page_type: Référence
description: "Cet article de référence couvre la gestion d'événements et d'attributs personnalisés, ainsi que la compréhension des comparaisons de types de données."
---

# Gestion d'événements et d'attributs personnalisés

## Ajout d'attributs personnalisés, d'événements personnalisés et de produits

Vous pouvez gérer les attributs personnalisés, les événements personnalisés (et leurs propriétés) et les produits (et leurs propriétés) depuis les onglets respectifs sur la page **Gérer les paramètres**:

- Attributs personnalisés
- Événements personnalisés
- Produits

Pour ajouter un attribut personnalisé, un événement ou un produit, allez dans l'onglet respectif et cliquez sur **+ Ajouter**. Donnez-lui un nom (et pour les attributs personnalisés, un type de données) et cliquez sur **Enregistrer**. Cela activera le suivi.

### Gestion des propriétés

Une fois que vous avez créé un **événement personnalisé** ou **produit**, vous pouvez cliquer sur **Gérer les propriétés** pour cet événement ou ce produit pour ajouter de nouvelles propriétés, liste noire des propriétés existantes, et voir quelles campagnes ou Canvases utilisent cette propriété dans un [événement déclencheur]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-1-select-a-trigger-event).

!\[manageproperties1.png\]\[73\]{: style="max-width:70%"}

Pour que ces attributs personnalisés, événements, produits ou propriétés d'événement ajoutés, puissent être voyageurs, vous devez demander à votre développeur de le créer dans le SDK en utilisant le nom exact que vous avez utilisé pour l'ajouter plus tôt. Ou, vous pouvez utiliser les [APIs]({{site.baseurl}}/api/basics/) de Braze pour importer des données sur cet attribut. Après cela, l'attribut personnalisé, l'événement ou un autre seront utilisables et s'appliqueront à vos utilisateurs !

{% alert note %}
Toutes les données du profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs. Les propriétés personnalisées des événements sont stockées et disponibles pour la Segmentation pendant trente (30) jours. Si vous souhaitez tirer parti des propriétés de l'événement pour Segmentation, veuillez contacter votre responsable de compte Braze, Responsable du succès client, ou ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).
{% endalert %}

## Liste noire des attributs personnalisés, des événements personnalisés et des produits

Si vous souhaitez arrêter de suivre un attribut personnalisé, un événement ou un produit spécifique (par ex. création accidentelle pendant les tests, non utile), recherchez le dans l'onglet **Événements personnalisés** , puis cliquez sur **Liste de blocs**.

Pour éviter la collecte de certains attributs de périphériques, consultez notre [guide SDK][88].

Une fois qu'un événement ou un attribut personnalisé est bloqué :

- Aucune donnée ne sera collectée concernant cet événement/attribut,
- Les données existantes seront indisponibles, sauf si réactivé,
- Les événements et attributs bloqués n'apparaîtront pas dans les filtres ou graphiques.

Pour cela, Braze envoie les informations de la liste noire vers chaque appareil. C'est important comme si vous envisagiez de bloquer un grand nombre d'événements et d'attributs (centaines de milliers ou de millions), il s'agira d'une opération intensive en matière de données.

Une chose à considérer est que bloquer un grand nombre d'événements et d'attributs est possible, mais pas recommandé. Ceci est dû au fait que chaque fois qu'un événement est effectué ou qu'un attribut est (potentiellement) envoyé à Braze, cet événement ou attribut doit être vérifié avec la liste noire entière. Si elle apparaît sur la liste, elle ne sera pas envoyée. Cette opération prend du temps, et si la liste grossit, votre application pourrait commencer à ralentir. Si vous n'avez pas besoin d'utiliser l'événement ou l'attribut dans le futur, il devrait être retiré de votre code d'application lors de votre prochaine version.

Les modifications apportées à la liste noire peuvent prendre quelques minutes pour se propager. Vous pouvez réactiver n'importe quel événement ou attribut de la liste noire à tout moment.

## Forcer les comparaisons de types de données

Braze reconnaît automatiquement les types de données des attributs qui nous sont envoyés. Cependant, dans le cas où plusieurs types de données sont appliqués à un seul attribut, vous pouvez forcer le type de données de n'importe quel attribut à nous faire savoir ce qu'il est vraiment. Cliquez sur le menu déroulant dans la colonne Type de données à choisir.

{% alert note %} Les types de données forcés ne s'appliquent pas aux propriétés d'événement, ni aux propriétés d'achat. {% endalert %}

!\[Liste déroulante des types de données de la vue des attributs personnalisés\]\[75\]

{% alert warning %}
Si vous choisissez de forcer le type de données pour un attribut, toutes les données qui n'entrent pas dans ce type ne seront pas ignorées.
{% endalert %}

### Coercition du type de données

| Type de données forcé | Libellé                                                                                  |
| --------------------- | ---------------------------------------------------------------------------------------- |
| Boolean               | Les entrées de `1`, `true`, `t` (non sensible à la casse) seront stockées comme `true`   |
| Boolean               | Les entrées de `0`, `false`, `f` (non sensible à la casse) seront stockées comme `false` |
| Numéros               | Les nombres entiers (c'est-à-dire `1`, `1.5`) seront stockés en tant que nombres         |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus d'informations sur les options de filtrage spécifiques exposées par différentes comparaisons de types de données, consultez [le rapport de configuration][43]. Et pour plus d'informations sur les différents types de données disponibles, reportez-vous à [Types de données d'attributs personnalisés][44].

{% alert note %}
Les données envoyées à Braze sont immuables et ne peuvent pas être supprimées ou modifiées une fois que nous les avons reçues. Cependant, vous pouvez utiliser l'une des étapes listées ci-dessus pour exercer un contrôle sur ce que vous suivez dans votre tableau de bord.
{% endalert %}
[73]: {% image_buster /assets/img_archive/manageproperties1.png %} [75]: {% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %}


[43]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[88]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection
