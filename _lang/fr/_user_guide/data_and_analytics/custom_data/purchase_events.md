---
nav_title: Événements d’achat
article_title: Événements d’achat
page_order: 8
page_type: reference
description: "Cet article de référence décrit les événements et propriétés d’achat, leur utilisation, leur segmentation, où voir les analyses qui s’y rapportent, etc."
search_rank: 3
---

# Événements d’achat

> Les événements d’achat sont des actions d’achat effectuées par vos utilisateurs. Ces événements sont utilisés pour enregistrer les achats dans l’application et établir la valeur à vie (LTV) de chaque profil utilisateur individuel. Ces événements d’achat doivent être configurés par votre équipe. La journalisation des événements d’achat vous permet d’ajouter des propriétés comme la quantité et le type, ce qui vous aide à cibler de façon encore plus précise vos utilisateurs en fonction de ces propriétés.

Après avoir configuré et commencé à journaliser des événements d’achat, vous pouvez afficher ces données d’achat sur le profil d’un utilisateur, sur [l’onglet Overview (Aperçu)]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab).

## Enregistrement des événements d’achat

Vous pouvez consigner les achats en envoyant un [Objet Achat]({{site.baseurl}}/api/objects_filters/purchase_object/) à l’endpoint [Suivi Utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

La liste suivante énumère les méthodes utilisées pour enregistrer les achats sur les différentes plateformes. Sur ces pages, vous pourrez également trouver des documents sur la façon d’ajouter des propriétés et des quantités à votre événement d’achat.

- [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_purchases/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/)

## Exclure des événements d’achat

Dans le tableau de bord de Braze, vous pouvez gérer les exclusions depuis **Manage Settings (Gérer les paramètres)** > **Products (Produits)**. Consultez la section [Gestion des événements et des attributs personnalisés]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/) pour en savoir plus.

## Segmentation des événements d’achat

Lors du ciblage des utilisateurs, vous pouvez déclencher un nombre ou un type de campagnes de suivi en fonction des événements d’achat enregistrés, et activer les filtres de segmentation suivants en fonction de la fréquence et dernière occurrence de cet événement.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si le total de dollars dépensé **est supérieur à **un **nombre**| **SUPÉRIEUR À** | **NOMBRE** |
| Vérifie si le total de dollars dépensé **est inférieur à **un **nombre**| **MOINS DE** | **NOMBRE** |
| Vérifie si le nombre total de dollars dépensé **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** |
| Vérifie si l’achat a été effectué **après la date X** | **APRÈS** | **DATE** |
| Vérifiez si l’achat a été effectué **avant la date X** | **AVANT** | **DATE** |
| Vérifiez si l’achat a été effectué **il y a plus de X jours** | **PLUS DE** | **DATE** |
| Vérifie si l’achat a été effectué **il y a moins de X jours** | **MOINS DE** | **DATE** |
| Vérifie si l’achat a eu lieu **plus de X (Max = 50) fois** | **PLUS DE** | in les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’achat a eu lieu **moins de X (Max = 50) fois** | **MOINS DE** | in les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’achat a eu lieu **exactement X (Max = 50) fois** | **EXACTEMENT** | in les **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**Exemple de filtrage basé sur l’événement d’achat :**

![Filtrage pour les utilisateurs ayant effectué plus de cinq achats][1]{: style="max-width:80%;margin-left:15px;"}

{% alert tip %} 
Si vous souhaitez segmenter sur le nombre de fois où un achat spécifique s’est produit, vous devez enregistrer l’achat individuellement en tant [qu’attribut personnalisé]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage) incrémental.
{% endalert %}

## Analyse des événements d’achat

En plus de suivre les indicateurs d’achat pour la segmentation, Braze note également le nombre d’achats de chaque produit et le chiffre d’affaires généré au fil du temps. Vous pouvez afficher ces données sur la page [Revenue (Revenus)]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) .

![Le graphique d’achat sur la page Revenus affiche les statistiques pour tous les achats][4]

![Tableau de répartition des achats sur la page Revenus, montrant les produits dans vos applications, le nombre de fois qu’ils ont été achetés et leurs chiffre d’affaires associé][3]

## Propriétés de l’événement d’achat {#purchase-properties}

Avec les propriétés de l'événement d’achat, vous pouvez définir des propriétés sur les achats pour qualifier plus précisément les conditions de déclenchement, améliorer la personnalisation des messages et générer des analyses plus sophistiquées via l’exportation de données brutes. Les types de valeur de propriété (chaîne de caractères, numérique, booléenne, date) varient selon la plateforme et sont souvent attribués en tant que paires clé-valeur.

Par exemple, si une application d’e-commerce souhaite envoyer un message à un utilisateur après qu’il ait fait un achat, elle pourrait en outre améliorer son audience cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété de l’événement d’achat `brand_name`.

**Exemple de déclencheur basé sur les propriétés de l'événement d’achat :**

![Des paramètres de Livraison par événement pour envoyer une campagne aux utilisateurs qui achètent des écouteurs de la marque HeadphoneMart][2]{: style="max-width:80%;margin-left:15px;"}

Consulter [Objet Propriétés d’achat]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) pour plus de détails.

### Segmentation des propriétés de l’événement

La segmentation des propriétés d’événement vous permet de cibler les utilisateurs en fonction de leurs événements personnalisés, mais également en fonction des propriétés associées à ces événements. Cette fonctionnalité ajoute des options de filtrage supplémentaires lors de la segmentation des achats et des événements personnalisés.

![][6]

Ces filtres de segmentation comprennent :
- A fait un événement personnalisé avec la propriété Y avec la valeur V X fois dans les Y derniers jours .
- A effectué au moins un achat avec la propriété Y avec la valeur V X fois dans les Y derniers jours.
- Ajoute la capacité de segmenter sur 1, 3, 7, 14, 21 et 30 jours.

Contrairement aux [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), les segments utilisés sont mis à jour en temps réel, prennent en charge une quantité illimitée de segments, offrent un historique de 30 jours au maximum et entraînent des points de données. Comme elles consomme des points de données supplémentaires, vous devez contacter votre gestionnaire du succès des clients de Braze pour activer les propriétés de l'événement dans vos événements personnalisés. Une fois approuvés, des propriétés supplémentaires peuvent être ajoutées dans le tableau de bord sous **Manage Settings > Custom Events > Manage Properties (Gérer les paramètres > Événements personnalisés > Gérer les propriétés)** pour être utilisées dans l’étape ciblage lors de la création de la campagne ou du Canvas.

### Propriétés d’entrée et propriétés de l’événement Canvas

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Cette section est disponible pour référence lors de l’utilisation des `canvas_entry_properties` et des `event_properties` pour le flux de travail Canvas d’origine.
{% endalert %}

Vous pouvez tirer parti des `canvas_entry_properties` et des `event_properties` dans les parcours utilisateur de votre Canvas. Consultez notre section [Propriété d’entrées et d’événement Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) pour obtenir plus d’informations ainsi que des exemples.

{% alert important %}
Vous ne pouvez pas utiliser les `event_properties` dans la première étape de message. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d’action avec l’événement correspondant **avant** l’étape de message qui comprend `event_properties`.
{% endalert %}

{% tabs local %}
{% tab Canvas Entry Properties %}

Les [propriétés d’entrée Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) sont les propriétés que vous mappez pour les Canvas basés sur l’événement ou déclenchés par API. Notez que l’objet `canvas_entry_properties` a une taille maximale limite de 50 KB.

{% alert note %}
Expressément pour les Canaux de communication in-app, `canvas_entry_properties` ne peut être référencé dans Canvas Flow et dans l’éditeur Canvas d’origine que si vous avez activé les propriétés d’entrées persistantes dans l’éditeur d’origine durant l’accès anticipé précédent.
{% endalert %}

Pour les envois de messages Canvas Flow, les `canvas_entry_properties` peuvent être utilisés en Liquid dans n’importe laquelle des étapes de message. Utilisez le Liquid lorsque vous référencez ces propriétés : ``{% raw %} canvas_entry_properties${property_name} {% endraw %}``. Prenez note du fait que les événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi. 

{% raw %}
Vous pouvez, par exemple, considérer la demande suivante : `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Vous pouvez ajouter le mot « chaussures » à un message avec le Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

Pour les Canvas construits à partir de l’éditeur d’origine, `canvas_entry_properties` ne peut être référencé que dans la première étape complète d’un Canvas.

{% endtab %}

{% tab Event Properties %}
Les propriétés de l’événement sont les propriétés que vous avez définies pour des événements personnalisés et des achats. Ces `event_properties` peuvent être utilisées dans les campagnes ayant une livraison par événement ainsi que dans les Canvas.

Dans Canvas Flow, les événements personnalisés et les propriétés de l’événement d’achat peuvent être utilisées en Liquid dans n’importe quelle étape de message suivant une étape de parcours d’action. Pour Canvas Flow, assurez-vous d’utiliser {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} si vous référencez ces `event_properties`. Ces événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi dans le composant de message.

Pour l’éditeur Canvas d’origine, les `event_properties` ne peuvent pas être utilisées dans les étapes complètes planifiées. Cependant, vous pouvez utiliser les `event_properties` dans la première étape complète d’un Canvas par événement, même si l’étape complète est planifiée.

Dans la première étape de message suivant un parcours d’action, vous pouvez utiliser les `event_properties` liées à l’événement référencé dans le parcours d’action. Ces `event_properties` ne peuvent être utilisées que si un utilisateur effectue effectivement l’action (n’est pas passé dans le groupe « Tous les autres »). Vous pouvez disposer d’autres étapes (n’étant pas un autre parcours d’action ou une étape de message) entre ce parcours d’action et l’étape de message.

{% endtab %}
{% endtabs %}

### Journaliser les achats au niveau de la commande
Si vous souhaitez journaliser les achats au niveau de la commande au lieu du niveau de produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Consultez notre [spécification d’objet d’achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) pour en savoir plus. 

[1]: {% image_buster /assets/img/purchase1.png %}
[2]: {% image_buster /assets/img/purchase2.png %}
[3]: {% image_buster /assets/img/purchase3.png %}
[4]: {% image_buster /assets/img/purchase4.jpg %}
[5]: {% image_buster /assets/img/purchase5.png %}
[6]: {% image_buster /assets/img/nested_object3.png %}
