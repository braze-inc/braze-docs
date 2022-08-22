---
nav_title: Événements d’achat
article_title: Événements d’achat
page_order: 0.5
page_type: reference
description: "Cet article de référence décrit les événements et propriétés d’achat, leur utilisation et où voir les analyses qui s’y rapportent."

---

# Événements d’achat

Les événements d’achat sont des actions d’achat effectuées par vos utilisateurs. Ces événements sont utilisés pour enregistrer les achats dans l’application et établir la valeur à vie (LTV) de chaque profil utilisateur individuel. Ces événements d’achat doivent être configurés par votre équipe. La journalisation des événements d’achat vous permet d’ajouter des propriétés comme la quantité et le type, ce qui vous aide à cibler de façon encore plus précise vos utilisateurs en fonction de ces propriétés.

Après avoir configuré et commencé à journaliser des événements d’achat, vous pouvez afficher ces données d’achat sur le profil d’un utilisateur, sur [l’onglet Overview (Aperçu)]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab).

## Enregistrement des événements d’achat

Vous pouvez consigner les achats en envoyant un [Objet d’achat]({{site.baseurl}}/api/objects_filters/purchase_object/) au endpoint [Suivi Utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

La liste suivante énumère les méthodes utilisées pour enregistrer les achats sur les différentes plateformes. Sur ces pages, vous pourrez également trouver des documents sur la façon d’ajouter des propriétés et des quantités à votre événement d’achat.

- [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unité]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_purchases/)
- [Windows Universal]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/)

## Exclure des événements d’achat

Dans le tableau de bord de Braze, vous pouvez gérer les exclusions depuis **Manage Settings** > **Produits**. Consultez la section [Gestion des événements et des attributs personnalisés]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/) pour en savoir plus.

## Segmentation des événements d’achat

Lors du ciblage des utilisateurs, vous pouvez déclencher un nombre ou un type de campagnes de suivi en fonction des événements d’achat enregistrés, et activer les filtres de segmentation suivants en fonction de la fréquence et dernière occurrence de cet événement.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si le nombre total de dollars dépensé **est supérieur à** ****| **SUPÉRIEUR À** | **CHIFFRE** |
| Vérifie si le nombre total de dollars dépensé **est inférieur à** ****| **INFÉRIEUR À** | **CHIFFRE** |
| Vérifie si le nombre total de dollars dépensé **est exactement** ****| **EXACTEMENT** | **CHIFFRE** |
| Vérifie si l’achat a été effectué **après la date X** | **APRÈS** | **DATE** |
| Vérifie si l’achat a été effectué **avant la date X** | **AVANT** | **DATE** |
| Vérifie si l’achat a été effectué **il y a plus de X jours** | **PLUS DE** | **DATE** |
| Vérifiez si l’achat a été effectué **il y a moins de X jours** | **MOINS DE** | **DATE** |
| Vérifie si l’achat a eu lieu **plus de X (Max = 50) fois** | **PLUS DE** | dans les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’achat a eu lieu **moins de X (Max = 50) fois** | **MOINS DE** | dans les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’achat a eu lieu **exactement X (Max = 50) fois** | **EXACTEMENT** | dans les **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**Exemple de filtrage basé sur l’événement d’achat :**

![Filtrage pour les utilisateurs ayant effectué plus de cinq achats][1]{: style="max-width:80%;margin-left:15px;"}

{% alert tip %} 
Si vous souhaitez segmenter sur le nombre de fois où un achat spécifique s’est produit, vous devez enregistrer l’achat individuellement en tant [qu’attribut personnalisé]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage) incrémental.
{% endalert %}

## Analyse des événements d’achat

En plus de suivre les indicateurs d’achat pour la segmentation, Braze note également le nombre d’achats de chaque produit et le chiffre d’affaires généré au fil du temps. Vous pouvez afficher ces données sur la [Revenus]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) .

![Le graphique d’achat sur la page Chiffre d’affaires affiche les statistiques pour tous les achats][4]

![Tableau de répartition des achats sur la page Revenus, montrant les produits dans vos applications, le nombre de fois qu’ils ont été achetés et leurs chiffre d’affaires associé][3]

## Propriétés de l'événement d’achat {#purchase-properties}

Avec les propriétés de l'événement d’achat, vous pouvez définir des propriétés sur les achats pour qualifier plus précisément les conditions de déclenchement, améliorer la personnalisation des messages et générer des analyses plus sophistiquées via l’exportation de données brutes. Les types de valeur de propriété (chaîne de caractères, numérique, booléenne, date) varient selon la plateforme et sont souvent attribués en tant que paires clé-valeur.

Par exemple, si une application d’e-commerce souhaite envoyer un message à un utilisateur après qu’il ait fait un achat, elle pourrait en outre améliorer son audience cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété d’événement d’achat `brand_name`.

**Exemple de déclencheur basé sur les propriétés de l'événement d’achat :**

![Des paramètres de Livraison par événement pour envoyer une campagne aux utilisateurs qui achètent des écouteurs de la marque HeadphoneMart][2]{: style="max-width:80%;margin-left:15px;"}

Consulter [Objet Propriétés d’achat]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) pour plus de détails.

### Segmentation des propriétés d’événement

La segmentation des propriétés d’événement vous permet de cibler les utilisateurs en fonction de leurs événements personnalisés, mais également en fonction des propriétés associées à ces événements. Cette fonction ajoute des options de filtrage supplémentaires lors de la segmentation des achats et des événements personnalisés.

![][6]

Ces filtres de segmentation comprennent :
- A fait un événement personnalisé avec la propriété Y avec la valeur V X fois dans les Y derniers jours .
- A effectué au moins un achat avec la propriété Y avec la valeur V X fois dans les Y derniers jours.
- Ajoute la capacité de segmenter sur 1, 3, 7, 14, 21 et 30 jours.

Contrairement aux [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), les segments utilisés sont mis à jour en temps réel, prennent en charge une quantité illimitée de segments, offrent un historique de 30 jours au maximum et entraînent des points de données. Comme elles consomme des points de données supplémentaires, vous devez contacter votre CSM pour activer les propriétés de l'événement dans vos événements personnalisés. Une fois approuvés, des propriétés supplémentaires peuvent être ajoutées dans le tableau de bord sous **Manage Settings > Événements personnalisés > Gérer les Propriétés** pour être utilisées dans l’étape ciblage lors de la création de la campagne ou du Canvas.

### Référence des propriétés de l'événement d’achat avec Liquid

Lorsque vous envoyez des données d’achat qui incluent des propriétés d’achat, vous pouvez utiliser la balise `event_properties` pour référencer les propriétés d’achat dans vos communications de canal.

{% raw %}

```liquid
{{event_properties.${your_custom_event_property}}}
```

{% endraw %}

Par exemple, pour référencer le nom d’un produit, remplacez `your_custom_event_property` par le `product_id`.

[1]: {% image_buster /assets/img/purchase1.png %}
[2]: {% image_buster /assets/img/purchase2.png %}
[3]: {% image_buster /assets/img/purchase3.png %}
[4]: {% image_buster /assets/img/purchase4.jpg %}
[5]: {% image_buster /assets/img/purchase5.png %}
[6]: {% image_buster /assets/img/nested_object3.png %}
