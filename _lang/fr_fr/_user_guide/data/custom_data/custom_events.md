---
nav_title: Événements personnalisés
article_title: Événements personnalisés
page_order: 9
page_type: reference
description: "Cet article décrit les événements/ propriétés personnalisés, la segmentation, l'utilisation, les propriétés d'entrée dans Canvas, l'endroit où afficher les analyses pertinentes, et plus encore."
search_rank: 2
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Événements personnalisés

> Cet article décrit les événements/ propriétés personnalisés, les filtres de segmentation associés, les propriétés d'entrée dans Canvas, les analyses pertinentes, etc. Pour en savoir plus sur les événements de Braze en général, consultez la rubrique [Événements.]({{site.baseurl}}/user_guide/data/custom_data/events/)

Les événements personnalisés sont des actions effectuées par vos utilisateurs, ou des mises à jour de vos utilisateurs. Lorsque des événements personnalisés sont enregistrés, ils peuvent déclencher un nombre et un type quelconque de campagnes de suivi. Vous pouvez ensuite utiliser des [filtres de segmentation](#segmentation-filters) pour segmenter les utilisateurs en fonction de la fréquence et du caractère récent de ces événements personnalisés. Les événements personnalisés sont donc les mieux adaptés au suivi des interactions utilisateur de grande valeur au sein de votre application.

## Cas d’utilisation

Parmi les cas courants d’utilisation d’événements personnalisés figurent les situations suivantes :

- Déclenchement d'une campagne ou d'un Canvas sur la base d'un événement personnalisé à l'aide de la [réception/distribution basée sur l'action.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)
- Segmentation des utilisateurs en fonction du nombre de fois qu'ils ont effectué un événement personnalisé, de la date du dernier événement, etc.
- L'utilisation du tableau de bord d'[analyse/analytique personnalisé des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) permet d'afficher un agrégat de la fréquence de chaque événement.
- Trouver des analyses/analytiques supplémentaires à l'aide des rapports d'[entonnoir]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) et de [rétention]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) (si utilisés).
- Exploitation des [propriétés d'entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) pour utiliser les métadonnées de votre événement client à des fins de personnalisation dans vos étapes du canvas.
- Générer des analyses/analytiques plus sophistiquées avec [Currents (si]({{site.baseurl}}/user_guide/data/braze_currents/) utilisé comme adjectif)
- Mise en place de [critères de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) pour définir quand les utilisateurs doivent quitter votre Canvas

## Gestion des événements personnalisés

Vous pouvez gérer, créer ou mettre en liste de blocage des événements personnalisés dans le tableau de bord en sélectionnant **Paramètres des données** > **Événements personnalisés**.

Sélectionnez le menu situé à côté d'un événement personnalisé pour effectuer les actions suivantes :

### Mise en liste de blocage

Vous pouvez mettre en liste de blocage des événements personnalisés individuels via le menu d'actions, ou sélectionner et mettre en liste de blocage jusqu'à 100 événements en bloc. 

Lorsque vous bloquez un événement personnalisé :

- Les données futures ne seront pas collectées pour cet événement.
- Les données existantes ne seront pas disponibles tant que l'événement n'aura pas été débloqué.
- Cet événement n'apparaîtra pas dans les filtres ou les graphiques.

En outre, si un événement personnalisé bloqué est actuellement référencé par des filtres ou des déclencheurs dans d'autres zones de Braze, une fenêtre modale/boîte de dialogue d'avertissement s'affiche, expliquant que toutes les instances des filtres ou des déclencheurs qui y font référence seront supprimées et archivées.

### Ajout de descriptions

Vous pouvez ajouter une description à un événement personnalisé après sa création si vous disposez de l' [autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Sélectionnez **Modifier la description** pour l'événement personnalisé et fournissez les informations que vous souhaitez, par exemple une note à l'intention de votre équipe.

## Ajout d'étiquettes

Vous pouvez ajouter des tags à un événement personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "Gérer les événements et les attributs, les achats". Les tags peuvent ensuite être utilisés pour filtrer la liste des événements.

### Consultation des rapports d'utilisation

Le rapport d'utilisation répertorie toutes les toiles, campagnes et segments utilisant un événement personnalisé spécifique. La liste ne comprend pas les utilisations de Liquid. 

Vous pouvez afficher jusqu'à 100 rapports d'utilisation à la fois en cochant les cases correspondant à plusieurs événements personnalisés, puis en sélectionnant **Afficher le rapport d'utilisation.**

## Exportation des données

Pour exporter la liste des événements personnalisés sous forme de fichier CSV, sélectionnez le bouton **Exporter tout en** haut de la page. Le fichier CSV sera généré et un lien de téléchargement vous sera envoyé par e-mail.

## Journalisation des événements personnalisés

Les événements personnalisés nécessitent une configuration supplémentaire. Vous y trouverez des informations sur les méthodes utilisées pour enregistrer les événements personnalisés et sur la manière d'ajouter des propriétés et des quantités à vos événements personnalisés.

{% details Développer la documentation par plateforme %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Stockage d’événements personnalisés

Toutes les données stockées dans le **profil utilisateur**, y compris les métadonnées des événements personnalisés (première ou dernière occurrence, nombre total et X dans Y sur 30 jours), sont conservées indéfiniment tant que chaque profil est [actif]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Filtres de segmentation

Le tableau suivant montre les filtres disponibles pour la segmentation des utilisateurs en fonction d’événements personnalisés.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'événement personnalisé s'est produit **plus de X fois.** | **PLUS DE** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois.** | **MOINS DE** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois.** | **EXACTEMENT** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **après la date X** | **APRÈS** | **DATE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **avant la date X** | **AVANT** | **DATE** |
| Vérifier si l’événement personnalisé s’est produit pour la dernière fois **il y a plus de X jours** | **PLUS DE** | **NOMBRE DE JOURS DERNIERS** (Nombre positif) |
| Vérifier si l’événement personnalisé s’est produit pour la dernière fois **il y a moins de X jours** | **MOINS DE** | **NOMBRE DE JOURS DERNIERS** (Nombre positif) |
| Vérifier si l’événement personnalisé s’est produit **plus de X (max = 50) fois** | **PLUS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l’événement personnalisé s’est produit **moins de X (max = 50) fois** | **MOINS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'événement personnalisé s'est produit **exactement X (Max = 50) fois.** | **EXACTEMENT** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Analyse

Braze note le nombre de fois où des événements personnalisés se sont produits et la dernière fois qu'ils ont été effectués par chaque utilisateur à des fins de segmentation. Consultez ces analyses en vous rendant dans la rubrique **Analytics** > **Custom Events Report (si vous utilisez un événement personnalisé**).

Sur la page **Rapport sur les événements personnalisés** du tableau de bord, vous pouvez visualiser globalement la fréquence de chaque événement personnalisé. Les lignes grises superposées à la série chronologique indiquent la dernière fois qu'une campagne a été envoyée, ce qui est utile pour voir comment vos campagnes ont affecté l'activité des événements personnalisés.

![Graphique du nombre d'événements personnalisés sur la page Événements personnalisés du tableau de bord montrant les tendances d'un événement personnalisé]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

Vous pouvez également utiliser des **filtres** pour décomposer vos événements personnalisés par heure, par moyenne mensuelle d'utilisateurs (MAU), par segment ou par formule d'indicateur clé de performance. 

![Filtres de graphe d'événements personnalisés]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Incrémentez les attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) pour conserver un compteur sur une action de l'utilisateur similaire à un événement personnalisé. Cependant, vous ne pouvez pas visualiser les données d'attributs personnalisés dans une série chronologique. Les actions des utilisateurs qui n'ont pas besoin d'être analysées dans une série temporelle doivent être enregistrées selon cette méthode.
{% endalert %}

### Pourquoi l'analyse/analytique des événements personnalisés ne s'affiche-t-elle pas ?

Les segments créés avec des données d'événements personnalisés ne peuvent pas afficher les données historiques antérieures à leur création.

## Propriétés de l'événement  personnalisé

Les propriétés d'événement personnalisées sont des métadonnées ou des attributs d'événement personnalisés qui décrivent une occurrence spécifique d'un événement. Ces propriétés peuvent être utilisées pour qualifier davantage les conditions de déclenchement, accroître la personnalisation des messages, suivre les conversions et générer des analyses/analytiques plus sophistiquées grâce à l'exportation de données brutes.

Les propriétés d'événement personnalisé ne sont pas stockées dans le profil Braze et ne consomment donc pas de points données (voir [Points données](#data-points) pour les exceptions).

{% alert important %}
Chaque événement personnalisé ou achat peut avoir jusqu’à 256 propriétés de l'événement personnalisé distinctes. Si un événement personnalisé ou un achat est enregistré avec plus de 256 propriétés, seules les 256 premières propriétés seront capturées et utilisables.
{% endalert %}

### Format attendu

Les valeurs des propriétés doivent être un objet dont les clés sont les noms des propriétés et les valeurs les valeurs des propriétés. Les noms de propriétés doivent être des chaînes de caractères non vides de moins de 255 caractères, qui ne commencent pas par un symbole de dollar (`$`).

Les valeurs de propriété peuvent être l’un des types de données suivants :

| Type de données | Description |
| --- | --- |
| Chiffres | Peuvent être des [nombres entiers](https://en.wikipedia.org/wiki/Integer) ou des [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booléens | Valeur de `true` ou `false`. |
| Datetimes | Formatés sous forme de chaînes de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Non pris en charge dans les tableaux. |
| Chaînes de caractères | 255 caractères ou moins. |
| Tableaux | Les tableaux ne peuvent pas inclure des dates/horodatages. |
| Objets imbriqués | Objets se trouvant à l’intérieur d’autres objets. Pour en savoir plus, consultez la section de cet article consacrée aux [objets imbriqués](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les objets de propriété d'événement qui contiennent des valeurs de tableau ou d'objet peuvent avoir une charge utile de propriété d'événement allant jusqu'à 100 Ko.

Vous pouvez modifier le type de données de votre propriété d'événement personnalisé, mais soyez conscient des conséquences d'un [changement de type de données]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) après la collecte des données.

### Utiliser des propriétés d’événement personnalisé

Les propriétés d'événement personnalisé peuvent être utilisées pour qualifier les déclencheurs de campagne, suivre les conversions et personnaliser les messages.

#### Déclencher des messages

Utilisez les propriétés d'événement personnalisées pour restreindre davantage votre audience dans le cadre d'une campagne ou d'un canvas particulier. Par exemple, si vous avez une application de commerce électronique et que vous souhaitez envoyer un message à un utilisateur lorsqu'il abandonne son panier, vous pouvez ajouter une propriété d'événement personnalisé de `item price` pour améliorer votre public cible et permettre une personnalisation accrue de la campagne.

![Filtres de propriété de l’événement personnalisé pour une carte abandonnée. Deux filtres sont combinés avec un opérateur AND pour envoyer cette campagne aux utilisateurs qui ont abandonné leur carte avec un prix d'article entre 100 et 200 dollars]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Les propriétés d'événement personnalisé imbriquées sont également prises en charge dans la [réception/distribution par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

![Filtres de propriété de l’événement personnalisé pour une carte abandonnée. Un filtre est sélectionné si l'un des articles du panier a un prix supérieur à 100 dollars.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png")

#### Personnaliser des messages

Vous pouvez également utiliser des propriétés d’événement personnalisé pour personnaliser les messages. Toute campagne utilisant la [livraison par]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) événement avec un événement déclencheur peut utiliser les propriétés d'événement personnalisées de cet événement pour la personnalisation des messages.

Par exemple, si vous avez une application de jeu et que vous souhaitez envoyer un message aux utilisateurs qui ont terminé un niveau, vous pourriez personnaliser davantage votre message avec une propriété pour le temps qu'il a fallu aux utilisateurs pour terminer ce niveau. Dans cet exemple, le message est personnalisé pour trois segments différents à l'aide de la [logique conditionnelle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/). La propriété d'événement personnalisé appelée `time_spent` peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Si l'utilisateur ne dispose pas d'une connexion internet, les messages in-app déclenchés avec des propriétés d'événements personnalisés (par exemple, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) échoueront et ne s'afficheront pas.
{% endalert %}

Pour une liste complète des étiquettes Liquid qui entraîneront l'envoi de messages in-app sous forme de messages in-app modélisés, reportez-vous à la rubrique [Foire aux questions.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/)

##### Considérations relatives aux filtres

- **Appels API :** Lorsque vous faites des appels API et que vous utilisez le filtre « is blank » (est vide), une propriété de l’événement personnalisée est considérée comme « vide » si elle est exclue de l’appel. Par exemple, si vous deviez inclure `"event_property": ""`, alors vos utilisateurs seraient considérés comme « non vides ».
- **Entiers :** Lorsque vous filtrez selon une quantité de propriétés d’événement personnalisé et que cette valeur est très importante, n’utilisez pas le filtre « exactement ». Si la quantité est trop importante, elle peut être arrondie à une certaine longueur et votre filtre ne fonctionnera donc pas comme vous l’attendez.

#### Segmentation

Utilisez la segmentation des propriétés d'événements pour cibler les utilisateurs en fonction des événements personnalisés pris et des propriétés associées à ces événements. Cela augmente vos options de filtrage lors de la segmentation par achat et événements personnalisés.

Les propriétés des événements personnalisés sont mises à jour en temps réel pour tout segment qui les utilise. Vous pouvez gérer les propriétés en allant dans **Paramètres des données** > **Événements personnalisés** et en sélectionnant **Gérer les propriétés de** l'événement personnalisé associé. Les propriétés d'événement personnalisé utilisées dans certains filtres de segment ont un historique de 30 jours maximum.

##### Ajout de propriétés d'événement pour la segmentation

Vous devez [disposer des autorisations utilisateur]({{site.baseurl}}/user_guide/data/data_points/#viewing-data-point-usage) "Gérer la segmentation personnalisée des événements" pour créer des segments basés sur la récurrence et la fréquence des événements.

Par défaut, vous pouvez avoir 20 propriétés d'événement segmentation par espace de travail. Contactez votre gestionnaire de compte Braze pour augmenter cette limite.

Pour ajouter des propriétés d'événement pour la segmentation, procédez comme suit :

1. Accédez à votre événement personnalisé et sélectionnez **Gérer les propriétés**.
2. Cochez la case **Activer la segmentation** pour ajouter la propriété d'événement pour la segmentation. Vous pouvez accéder à des options de filtrage supplémentaires lors de la segmentation.

Les filtres de segmentation des propriétés d'événement sont les suivants :

- A réalisé un événement personnalisé avec la propriété A et la valeur B, X fois au cours des Y derniers jours.
- A effectué des achats avec le bien A d'une valeur B, X fois au cours des Y derniers jours.
- Ajoute la possibilité de segmentation dans un délai de 1 à 30 jours.

![Un groupe de filtre qui a 'Abandon de panier' avec la propriété 'number of itmes' et la valeur 2 plus d'une fois dans les 30 derniers jours du calendrier.]({% image_buster /assets/img/nested_object3.png %})

Les données ne sont enregistrées pour une propriété d'événement donnée qu'après avoir été activées par votre gestionnaire de la satisfaction client, et les propriétés d'événement ne sont disponibles qu'à partir de cette date.

##### Points de données

En ce qui concerne les inscriptions, les propriétés d’événement personnalisé activées pour la segmentation avec les filtres suivants sont toutes comptées comme des points de données séparés qui viennent s’ajouter au point de données consommé par l’événement personnalisé lui-même :

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propriétés d’entrée et propriétés de l’événement Canvas

{% multi_lang_include canvas_entry_event_properties.md %}

### Objets imbriqués {#nested-objects}

Vous pouvez utiliser des objets imbriqués (objets à l'intérieur d'un autre objet) pour envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats. Ces données imbriquées peuvent être utilisées pour créer des modèles d'informations personnalisées dans les messages, déclencher l'envoi de messages et segmenter les utilisateurs.

Pour en savoir plus, consultez notre page dédiée aux [objets imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

## Stockage de propriété d’événement personnalisé

Les propriétés de l'événement personnalisé sont conçues pour vous aider améliorer le ciblage et à personnaliser davantage vos messages. Les propriétés de l'événement personnalisé peuvent être stockées dans Braze à court et à long terme.

Vous pouvez effectuer une segmentation basée sur les valeurs des propriétés d'événement de deux manières :

1. **Sur 30 jours :** Le personnel d'assistance de Braze peut activer la segmentation des propriétés d'événement en fonction de la fréquence et de la récurrence des valeurs de propriétés d'événement spécifiques au sein des segments de Braze. Si vous souhaitez exploiter les propriétés d'événement au sein des segments, contactez votre gestionnaire de compte Braze ou votre gestionnaire satisfaction client. Cette option aura un impact sur l'utilisation des données.<br><br>
2. **Sur 30 jours et au-delà :** Pour couvrir la segmentation des propriétés d'événement à court et à long terme, vous pouvez utiliser les [extensions de segments.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) Cette fonctionnalité segmente les utilisateurs en fonction des événements personnalisés et des propriétés d'événement suivis au cours des deux dernières années. Cette option n'aura pas d'incidence sur l'utilisation des données.

Contactez votre gestionnaire du succès des clients Braze pour obtenir des recommandations sur la meilleure approche en fonction de vos besoins spécifiques.

