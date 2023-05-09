---
nav_title: Gestion des événements et attributs personnalisés
article_title: Gestion des événements et attributs personnalisés
page_order: 1
page_type: reference
description: "Cet article de référence couvre la gestion des propriétés, des événements et des attributs personnalisés, ainsi qu’une présentation des comparaisons de type de données."

---

# Gestion des événements et attributs personnalisés

> Cet article de référence couvre la gestion des propriétés, des événements et des attributs personnalisés, ainsi qu’une présentation des comparaisons de type de données.

## Ajouter des attributs personnalisés, des événements personnalisés et des produits

Vous pouvez gérer les attributs personnalisés, les événements personnalisés (et leurs propriétés) et les produits (et leurs propriétés) des onglets respectifs sur la page **Manage Settings (Gérer les paramètres)** :

- Attributs personnalisés
- Événements personnalisés
- Produits

Pour ajouter un attribut personnalisé, un événement ou un produit personnalisé, accédez à l’onglet correspondant et cliquez sur **+ Add (+ Ajouter)**. Donnez-lui un nom (et pour des attributs personnalisés, un type de données) et cliquez sur **Save (Enregistrer)**. Cela permettra de le suivre.

### Gestion des propriétés

Une fois que vous avez créé un **Événement personnalisé** ou un **Produit**, vous pouvez cliquer sur **Manage Properties (Gérer les propriétés)** pour cet événement ou ce produit pour ajouter de nouvelles propriétés, bloquer les propriétés existantes et voir quelles campagnes ou Canvas utilisent cette propriété dans un [événement déclencheur]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-1-select-a-trigger-event).

![Propriétés personnalisées pour un événement personnalisé][73]{: style="max-width:70%"}

Pour que ces attributs personnalisés ajoutés, événements, produits ou propriétés de l’événement puissent être suivis, vous devez demander à votre développeur de le créer dans le SDK en utilisant le nom exact que vous avez utilisé pour l’ajouter plus tôt. Ou vous pouvez également utiliser l’[API]({{site.baseurl}}/api/basics/) Braze pour importer des données sur cet attribut. Ensuite, l’attribut personnalisé, l’événement ou autre sera utilisable et s’appliquera à vos utilisateurs !

{% alert note %}
Toutes les données de profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs.
{% endalert %}

## Bloquer des attributs personnalisés, des événements personnalisés et des produits

Si vous souhaitez arrêter d’effectuer un suivi d’un attribut, d’un événement ou d’un produit personnalisé spécifique (p. ex., création accidentelle pendant le test, devenue utile), recherchez-le dans l’onglet **Custom Events (Événements personnalisés)** puis cliquez sur **Blocklist (Liste de blocage)**.

Pour éviter de recueillir certains attributs d’appareil, consultez notre [Guide SDK][88].

Une fois qu’un événement ou un attribut personnalisé est exclu :

- Aucune donnée ne sera recueillie concernant cet événement/attribut,
- Les données existantes ne seront pas disponibles, sauf si elles sont réactivées,
- Les événements et attributs exclus ne s’afficheront pas dans les filtres ou les graphiques.

Pour ce faire, Braze envoie les informations de blocage à chaque appareil. Ceci est important, car si vous envisagez de bloquer un nombre important d’événements et d’attributs (des centaines de milliers ou des millions), l’opération exigera un volume de données significatif.

Il faut tenir compte du fait que le blocage d’un nombre élevé d’événements et d’attributs est possible, mais pas recommandé. En effet, chaque fois qu’un événement est exécuté ou qu’un attribut est (potentiellement) envoyé à Braze, cet événement ou cet attribut doit être vérifié par rapport à l’ensemble de la liste de blocage. S’il apparaît sur la liste, il ne sera pas envoyé. Cette opération prend du temps, et si la liste est vraiment trop longue, votre application peut commencer à ralentir. Si vous n’avez pas besoin d’utiliser l’événement ou l’attribut à l’avenir, il doit être supprimé de votre code d’application lors de votre prochaine version.

Les modifications apportées à la liste de blocage peuvent prendre quelques minutes pour se propager. Vous pouvez réactiver tout événement ou attribut exclu à tout moment.

## Forcer les comparaisons de type de données

Braze reconnaît automatiquement les types de données pour les données d’attribut qui nous sont envoyées. Cependant, dans l’éventualité où plusieurs types de données sont appliqués à un seul attribut, vous pouvez forcer le type de données de n’importe quel attribut pour nous faire savoir ce qu’il est réellement. Cliquez sur la liste déroulante dans la colonne Type de données pour choisir.

{% alert note %} Forcer les types de données ne s’applique pas aux propriétés de l’événement ou aux propriétés d’achat. {% endalert %}

![Liste déroulante des attributs personnalisés][75]

{% alert warning %}
Si vous choisissez de forcer le type de données d’un attribut, toute donnée entrante qui n’est pas du type spécifié sera ignorée.
{% endalert %}

### Contrainte de type de données

| Type de données forcées | Description |
|------------------|-------------|
| Booléen | Les entrées de `1`, `true`, `t` (non sensibles à la casse) seront conservées comme `true` |
| Booléen | Les entrées de `0`, `false`, `f` (non sensibles à la casse) seront conservées comme `false` |
| Nombre | Les nombres entiers ou floats (c.-à-d. `1`, `1.5`) seront stockés sous forme de nombres |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus d’informations sur les options de filtrage spécifiques exposées par différentes comparaisons de type de données, consultez la [Configuration des rapports][43]. Pour plus d’informations sur les différents types de données disponibles, reportez-vous à [Types de données d’attributs personnalisés][44].

{% alert note %}
Les données envoyées à Braze sont immuables et ne peuvent être supprimées ou modifiées une fois que nous les avons reçues. Cependant, vous pouvez recourir à l’une des méthodes énumérées dans les sections précédentes pour exercer un contrôle sur ce que vous suivez dans votre tableau de bord.
{% endalert %}


[43]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[73]: {% image_buster /assets/img_archive/manageproperties1.png %}
[75]: {% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %}
[88]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection
