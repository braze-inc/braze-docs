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
- Mise en place d' [événements d'exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events#canvas-exception-events) Canvas pour définir quand les utilisateurs ne doivent pas passer à l'étape suivante de votre Canvas.

## Gestion des événements personnalisés

Vous pouvez gérer, créer ou mettre en liste de blocage des événements personnalisés dans le tableau de bord en sélectionnant **Paramètres des données** > **Événements personnalisés**.

{% alert note %}
Si vous utilisez l' [ancienne version de la navigation]({{site.baseurl}}/navigation), vous trouverez les **événements personnalisés** sous **Gérer les paramètres.**
{% endalert %}

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

- [Android et FireOS]({{site.baseurl}}/developer_guide/platforms/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platforms/swift/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platforms/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platforms/roku/analytics/logging_custom_events/)

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

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), vous trouverez le rapport sur les **événements personnalisés** sous **Données.**
{% endalert %}

Sur la page **Rapport sur les événements personnalisés** du tableau de bord, vous pouvez visualiser globalement la fréquence de chaque événement personnalisé. Les lignes grises superposées à la série chronologique indiquent la dernière fois qu'une campagne a été envoyée, ce qui est utile pour voir comment vos campagnes ont affecté l'activité des événements personnalisés.

![Graphique du nombre d'événements personnalisés sur la page des événements personnalisés dans le tableau de bord montrant les tendances pour un événement personnalisé.][8]

Vous pouvez également utiliser des **filtres** pour décomposer vos événements personnalisés par heure, par moyenne mensuelle d'utilisateurs (MAU), par segment ou par formule d'indicateur clé de performance. 

![Filtres personnalisés pour le graphique des événements][9]{: style="max-width:40%;"}

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
| Objets | Les objets seront ingérés en tant que chaînes de caractères. |
| Objets imbriqués | Objets se trouvant à l’intérieur d’autres objets. Pour en savoir plus, consultez la section de cet article consacrée aux [objets imbriqués](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les objets de propriété d'événement qui contiennent des valeurs de tableau ou d'objet peuvent avoir une charge utile de propriété d'événement allant jusqu'à 100 Ko.

Vous pouvez modifier le type de données de votre propriété d'événement personnalisé, mais soyez conscient des conséquences d'un [changement de type de données]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) après la collecte des données.

### Utiliser des propriétés d’événement personnalisé

Les propriétés d'événement personnalisé peuvent être utilisées pour qualifier les déclencheurs de campagne, suivre les conversions et personnaliser les messages.

#### Déclencher des messages

Utilisez les propriétés d'événement personnalisées pour restreindre davantage votre audience dans le cadre d'une campagne ou d'un canvas particulier. Par exemple, si vous avez une application de commerce électronique et que vous souhaitez envoyer un message à un utilisateur lorsqu'il abandonne son panier, vous pouvez ajouter une propriété d'événement personnalisé de `cart value` pour améliorer votre public cible et permettre une personnalisation accrue de la campagne.

![Filtres de propriété de l’événement personnalisé pour une carte abandonnée. Deux filtres sont combinés avec un opérateur ET pour envoyer cette campagne aux utilisateurs ayant abandonné leur carte avec une valeur de panier comprise entre 100 et 200 dollars][16]

Les propriétés d'événement personnalisé imbriquées sont également prises en charge dans la [livraison par événement]][19].

![Filtres de propriété de l’événement personnalisé pour une carte abandonnée. Un filtre est sélectionné si un quelconque produit du panier a un prix supérieur à 100 dollars.][20]

#### Personnaliser des messages

Vous pouvez également utiliser des propriétés d’événement personnalisé pour personnaliser les messages. Toute campagne utilisant [livraison par événement][19] avec un événement déclencheur peut utiliser les propriétés d'événement personnalisées de cet événement pour la personnalisation des messages.

Par exemple, si vous avez une application de jeu et que vous souhaitez envoyer un message aux utilisateurs qui ont terminé un niveau, vous pourriez personnaliser davantage votre message avec une propriété pour le temps qu'il a fallu aux utilisateurs pour terminer ce niveau. Dans cet exemple, le message est personnalisé pour trois segments différents à l'aide de la [logique conditionnelle][18]. La propriété d'événement personnalisé appelée `time_spent` peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

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

Pour ajouter des propriétés d'événement pour la segmentation, procédez comme suit :

1. Accédez à votre événement personnalisé et sélectionnez **Gérer les propriétés**.
2. Cochez la case **Activer la segmentation** pour ajouter la propriété d'événement pour la segmentation. Vous pouvez accéder à des options de filtrage supplémentaires lors de la segmentation.

Les filtres de segmentation des propriétés d'événement sont les suivants :

- A réalisé un événement personnalisé avec la propriété A et la valeur B, X fois au cours des Y derniers jours.
- A effectué des achats avec le bien A d'une valeur B, X fois au cours des Y derniers jours.
- Ajoute la possibilité de segmentation dans un délai de 1 à 30 jours.

![Un groupe de filtres qui "a 'Abandon de panier' avec la propriété 'number of itmes' et la valeur '2' 'more than' 1'1 time in the last '30' calendar days.][3]

Les données ne sont enregistrées pour une propriété d'événement donnée qu'après avoir été activées par votre gestionnaire de la satisfaction client, et les propriétés d'événement ne sont disponibles qu'à partir de cette date.

##### Points de données

En ce qui concerne les inscriptions, les propriétés d’événement personnalisé activées pour la segmentation avec les filtres suivants sont toutes comptées comme des points de données séparés qui viennent s’ajouter au point de données consommé par l’événement personnalisé lui-même :

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propriétés d’entrée et propriétés de l’événement Canvas

Vous pouvez utiliser `canvas_entry_properties` et `event_properties` dans vos parcours utilisateurs Canvas. Reportez-vous aux [propriétés d'entrée dans le canvas et aux propriétés d'événement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) pour plus d'informations et d'exemples.

{% tabs local %}
{% tab Propriétés d'entrée de Canvas %}

Les [propriétés d'entrée de Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) correspondent aux propriétés que vous mappez pour les canvas basés sur des actions ou déclenchés par API. Notez que l’objet `canvas_entry_properties` a une taille maximale limite de 50 KB.

{% alert note %}
Expressément pour les canaux de communication in-app, `canvas_entry_properties` peut uniquement être référencé dans Canvas Flow et dans l’éditeur Canvas d’origine si vous avez activé les propriétés d’entrées persistantes dans l’éditeur d’origine durant l’accès anticipé précédent.
{% endalert %}

Pour l'envoi de messages par Canvas Flow, `canvas_entry_properties` peut être utilisé dans n'importe quelle étape du canvas avec le format Liquid suivant : ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière. 

#### Cas d’utilisation

{% raw %}
Supposons qu'un magasin de détail, RetailApp, ait la demande suivante : `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. RetailApp peut intégrer le nom du produit (chaussures) dans un message avec le code Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

RetailApp peut également déclencher l'envoi de messages spécifiques pour différentes propriétés d' `product_name` dans un canvas qui cible les utilisateurs après qu'ils aient déclenché un événement d'achat. Par exemple, ils peuvent envoyer des messages différents aux utilisateurs qui ont acheté des chaussures et à ceux qui ont acheté autre chose en ajoutant le liquide suivant dans une étape Message.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Élargir pour l'éditeur original de Canvas %}

Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Cette section n'est disponible qu'à titre de référence.

Pour les Canvas créés à partir de l’éditeur d’origine, `canvas_entry_properties` ne peut être référencé que dans la première étape complète d’un Canvas.

{% enddetails %}
{% endtab %}

{% tab Propriétés d'événement %}

{% alert important %}
Vous ne pouvez pas utiliser les `event_properties` dans la première étape de message. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d'action avec l'événement correspondant **avant** l’étape Message qui inclut `event_properties`.
{% endalert %}

Les propriétés d'événement font référence aux propriétés que vous définissez pour les événements personnalisés et les achats. Ces `event_properties` peuvent être utilisés dans des campagnes avec livraison/distribution par événement et Canvases.

Dans Canvas Flow, les événements personnalisés et les propriétés de l’événement d’achat peuvent être utilisées en Liquid dans n’importe quelle étape de message suivant une étape de parcours d’action. Veillez à utiliser {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} si vous faites référence à ces `event_properties`. Ces événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi dans le composant de message.

Dans la première étape de message suivant un parcours d’action, vous pouvez utiliser les `event_properties` liées à l’événement référencé dans le parcours d’action. Ces `event_properties` ne peuvent être utilisés que si l'utilisateur a réellement effectué l'action (et n'est pas allé dans le groupe Everyone Else). Vous pouvez disposer d’autres étapes (n’étant pas un autre parcours d’action ou une étape de message) entre ce parcours d’action et l’étape de message.

{% details Élargir pour l'éditeur original de Canvas %}

Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Cette section n'est disponible qu'à titre de référence.

Pour l’éditeur Canvas d’origine, les `event_properties` ne peuvent pas être utilisées dans les étapes complètes planifiées. Cependant, vous pouvez utiliser les `event_properties` dans la première étape complète d’un Canvas par événement, même si l’étape complète est planifiée.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Objets imbriqués {#nested-objects}

Vous pouvez utiliser des objets imbriqués (objets à l'intérieur d'un autre objet) pour envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats. Ces données imbriquées peuvent être utilisées pour créer des modèles d'informations personnalisées dans les messages, déclencher l'envoi de messages et segmenter les utilisateurs.

Pour en savoir plus, consultez notre page dédiée aux [objets imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

## Stockage de propriété d’événement personnalisé

Les propriétés de l'événement personnalisé sont conçues pour vous aider améliorer le ciblage et à personnaliser davantage vos messages. Les propriétés de l'événement personnalisé peuvent être stockées dans Braze à court et à long terme.

Vous pouvez effectuer une segmentation basée sur les valeurs des propriétés d'événement de deux manières :

1. **Sur 30 jours :** Le personnel d'assistance de Braze peut activer la segmentation des propriétés d'événement en fonction de la fréquence et de la récurrence des valeurs de propriétés d'événement spécifiques au sein des segments de Braze. Si vous souhaitez exploiter les propriétés d'événement au sein des segments, contactez votre gestionnaire de compte Braze ou votre gestionnaire satisfaction client. Cette option aura un impact sur l'utilisation des données.<br><br>
2. **Sur 30 jours et au-delà :** Pour couvrir la segmentation des propriétés d'événement à court et à long terme, vous pouvez utiliser les [extensions de segments.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) Cette fonctionnalité segmente les utilisateurs en fonction des événements personnalisés et des propriétés d'événement suivis au cours des deux dernières années. Cette option n'aura pas d'incidence sur l'utilisation des données.

Contactez votre gestionnaire du succès des clients Braze pour obtenir des recommandations sur la meilleure approche en fonction de vos besoins spécifiques.

[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[3]: {% image_buster /assets/img/nested_object3.png %}
[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[9]: {% image_buster /assets/img/custom_events_report_filters.png %}
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"
