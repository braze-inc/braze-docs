---
nav_title: Acheter des Événements
article_title: Acheter des Événements
page_order: 0.5
page_type: Référence
description: "Cet article de référence décrit les événements et les propriétés d'achat, leur utilisation, et où consulter les analyses pertinentes."
---

# Événements d'achat

Les événements d'achat sont des actions d'achat effectuées par vos utilisateurs. Ces événements sont utilisés pour enregistrer les achats dans l'application et établir la valeur à vie (LTV) pour chaque profil utilisateur individuel. Ces événements d'achat doivent être mis en place par votre équipe. Les événements d'achat de journaux vous donnent la possibilité d'ajouter des propriétés comme la quantité et le type, vous permettant de cibler davantage vos utilisateurs en fonction de ces propriétés.

Une fois que vous avez mis en place et commencé à enregistrer les événements d'achat, vous pouvez voir ces données d'achat sur le profil d'utilisateur.

!\[Profil utilisateur\]\[5\]{: style="max-width:80%;margin-left:15px;"}

## Évènements d'achat de journalisation

Vous pouvez enregistrer vos achats en passant un [Achat Objet]({{site.baseurl}}/api/objects_filters/purchase_object/) via le point de terminaison [de suivi utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

Voici la liste des méthodes utilisées pour enregistrer les achats. À l'intérieur de ces pages, vous pourrez également trouver de la documentation sur la façon d'ajouter des propriétés et des quantités à votre événement d'achat.

- [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)
- [React Natif]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unité]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_purchases/)
- [Univers Windows]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/)

## Évènements d'achat de la liste noire

Dans le tableau de bord de Braze, vous pouvez gérer la liste noire à partir de **Gérer les paramètres** > **Produits**. Consultez [Événements personnalisés et gestion d'attributs]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/) pour en savoir plus.

## Acheter la segmentation d'événements

Vous pouvez déclencher n'importe quel nombre ou type de campagnes de suivi en fonction des événements d'achat enregistrés, et activer les filtres de segmentation suivants en fonction de la récurrence et de la fréquence de cet événement lors du ciblage des utilisateurs.

| Options de segmentation                                                           | Filtre de liste déroulante | Input Options                                      |
| --------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------- |
| Vérifie si le nombre total de dollars dépensés __est supérieur à__ un __nombre__  | __PLUS GRAND QUE__         | __NOMBRE__                                         |
| Vérifie si le nombre total de dollars dépensés __est inférieur à__ un __nombre__  | __MOINS QUE__              | __NOMBRE__                                         |
| Vérifier si le nombre total de dollars dépensés __est exactement__ un numéro ____ | __EXACTEMENT__             | __NOMBRE__                                         |
| Vérifier si l'achat a eu lieu la dernière fois __après la date X__                | __APRES__                  | __HEURE__                                          |
| Vérifier si l'achat a eu lieu la dernière fois __avant la date X__                | __AVANT__                  | __HEURE__                                          |
| Vérifier si l'achat a eu lieu pour la dernière fois __il y a plus de X jours__    | __PLUS PAR__               | __HEURE__                                          |
| Vérifier si l'achat a eu lieu la dernière fois __il y a moins de X jours__        | __MOINS QUE__              | __HEURE__                                          |
| Vérifier si l'achat a eu lieu __plus de X (Max = 50) nombre de fois__             | __PLUS PAR__               | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
| Vérifier si l'achat a eu lieu __moins de X (Max = 50) nombre de fois__            | __MOINS QUE__              | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
| Vérifier si l'achat a eu lieu __exactement X (Max = 50) nombre de fois__          | __EXACTEMENT__             | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**Exemple de Filtrage basé sur l'Evénement d'Achat:**

!\[Purchase targeting\]\[1\]{: style="max-width:80%;margin-left:15px;"}

{% alert tip %}
Si vous souhaitez segmenter le nombre de fois qu'un achat spécifique a eu lieu, vous devriez enregistrer cet achat individuellement en tant qu'attribut [incrémentant personnalisé]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

## Acheter des analyses d'événements

En plus de suivre les paramètres d'achat pour la segmentation, Braze note également les achats de numéro pour chaque produit et les revenus générés au fil du temps. Vous pouvez voir ces données sur la page [Revenu]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

!\[Achat graphique\]\[4\]

!\[Répartition des achats\]\[3\]

## Propriétés de l'événement d'achat {#purchase-properties}

Avec l'achat de propriétés d'événement, vous pouvez définir des propriétés sur les achats qui peuvent être utilisés pour qualifier davantage les conditions de déclenchement augmenter la personnalisation de la messagerie et générer des analyses plus sophistiquées grâce à l'exportation de données brutes. Les types de valeur de la propriété (chaîne, numérique, booléen, date) varient par plate-forme, et sont souvent assignés comme paires clé-valeur.

Par exemple, si une application eCommerce voulait envoyer un message à un utilisateur après avoir fait un achat, ils pourraient également améliorer leur public cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété d’achat d’événement de `brand_name`.

**Exemple de déclenchement basé sur les propriétés de l'Evènement d'Achat :**

!\[Acheter la livraison\]\[2\]{: style="max-width:80%;margin-left:15px;"}

Reportez-vous à [Purchase Properties Object]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) pour en savoir plus.

### Référencement des propriétés d'événements d'achat avec Liquid

Lorsque vous envoyez par le biais des données d'achat qui incluent les propriétés d'achat, vous pouvez utiliser la balise `event_properties` pour référencer les propriétés d'achat dans votre message de canal.

{% raw %}

```liquid
{{event_properties.${your_custom_event_property}}}
```

{% endraw %}

Par exemple, pour référencer le nom d'un produit, remplacez `votre_custom_event_property` par le `product_id`.
[1]: {% image_buster /assets/img/purchase1.png %} [2]: {% image_buster /assets/img/purchase2.png %} [3]: {% image_buster /assets/img/purchase3. ng %} [4]: {% image_buster /assets/img/purchase4.jpg %} [5]: {% image_buster /assets/img/purchase5.png %}