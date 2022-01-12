---
nav_title: Événements personnalisés
article_title: Événements personnalisés
page_order: 1
page_type: Référence
description: "Cet article de référence décrit les événements et propriétés personnalisés, leur utilisation, et où visualiser les analyses pertinentes."
---

# Événements personnalisés

Les événements personnalisés sont des actions prises ou mises à jour à propos de vos utilisateurs. Ils sont les mieux adaptés pour suivre les interactions utilisateur de grande valeur dans votre application. Loguer un événement personnalisé peut déclencher n'importe quel nombre et n'importe quel type de campagnes de suivi, et active les filtres de segmentation listés sur la récurrence et la fréquence de cet événement.

{% alert tip %}
Pour en savoir plus sur l'utilisation d'événements personnalisés dans vos stratégies de messagerie, consultez notre cours LAB [Événements et attributs personnalisés](http://lab.braze.com/custom-events-and-attributes)!
{% endalert %}

## Journalisation des événements personnalisés

Voici la liste des méthodes utilisées par les différentes plates-formes pour enregistrer les événements personnalisés. Dans ces pages, vous pourrez également trouver de la documentation sur la façon d'ajouter des propriétés et des quantités à vos événements personnalisés.

{% details Expand for documentation by platform %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [React Natif]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unité]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Univers Windows]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

{% enddetails %}

## Stockage d'événements personnalisés

Toutes les données stockées sur le **Profil utilisateur**, y compris les métadonnées d'événement personnalisées (première/dernière occurrence, le nombre total, et X en Y sur 30 jours), sont conservés indéfiniment tant que chaque profil est actif.

## Filtres de segmentation d'événements personnalisés

Le tableau suivant montre les filtres disponibles pour segmenter les utilisateurs par des événements personnalisés.

| Options de segmentation                                                                             | Filtre de liste déroulante | Input Options                                      |
| --------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------- |
| Vérifie si l'événement personnalisé s'est produit __plus de X fois__                                | __PLUS PAR__               | __NOMBRE__                                         |
| Vérifie si l'événement personnalisé s'est produit __moins de X fois__                               | __MOINS QUE__              | __NOMBRE__                                         |
| Vérifie si l'événement personnalisé s'est produit __exactement X fois__                             | __EXACTEMENT__             | __NOMBRE__                                         |
| Vérifie si l'événement personnalisé s'est produit pour la dernière fois __après la date X__         | __APRES__                  | __HEURE__                                          |
| Vérifie si l'événement personnalisé s'est produit pour la dernière fois __avant la date X__         | __AVANT__                  | __HEURE__                                          |
| Vérifie si l'événement personnalisé s'est produit pour la dernière fois __il y a plus de X jours__  | __PLUS PAR__               | __NOMBRE DE JOURS AGO__ (Numéro Positif)           |
| Vérifie si l'événement personnalisé s'est produit pour la dernière fois __il y a moins de X jours__ | __MOINS QUE__              | __NOMBRE DE JOURS AGO__ (Numéro Positif)           |
| Vérifie si l'événement personnalisé s'est produit __plus de X (Max = 50) nombre de fois__           | __PLUS PAR__               | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
| Vérifie si l'événement personnalisé s'est produit __moins de X (max = 50) nombre de fois__          | __MOINS QUE__              | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
| Vérifie si l'événement personnalisé s'est produit __exactement X (max = 50) nombre de fois__        | __EXACTEMENT__             | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Analyses d'événements personnalisées

Braze note le nombre de fois où ces événements se sont produits ainsi que la dernière fois qu'ils ont été exécutés par chaque utilisateur pour la segmentation. Sur la page [Événements personnalisés][7] dans le tableau de bord, vous pouvez voir dans l'agrégat la fréquence à laquelle chaque événement personnalisé se produit, ainsi que par segment au fil du temps pour une analyse plus détaillée. Ceci est particulièrement utile pour voir comment vos campagnes ont affecté l'activité de l'événement personnalisé en regardant les lignes grises surcouches Braze sur la série de temps pour indiquer la dernière fois qu'une campagne a été envoyée.

!\[custom_event_analytics_example.png\]\[8\]

{% alert tip %}
[L'incrémentation d'attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) peut être utilisée pour garder un compteur sur une action utilisateur similaire à un événement personnalisé. Cependant, vous ne serez pas en mesure de voir les données d'attributs personnalisés dans une série horaire. Les actions de l'utilisateur qui n'ont pas besoin d'être analysées dans les séries temporelles doivent être enregistrées en utilisant cette méthode.
{% endalert %}

### Analyses personnalisées des événements ne s'affichent pas ?

Veuillez noter que les segments créés avec des données d'événement personnalisées ne peuvent pas afficher les données historiques précédentes avant qu'elles n'aient été créées.

## Propriétés personnalisées de l'événement

Avec des propriétés d'événement personnalisées, vous pouvez définir des propriétés sur des événements personnalisés et des achats. Ces propriétés peuvent ensuite être utilisées pour de nouvelles conditions de déclenchement qualifiantes, pour augmenter la personnalisation de la messagerie et pour générer des analyses plus sophistiquées grâce à l'exportation de données brutes.

Les valeurs des propriétés doivent être un objet où les clés sont les noms de propriété et les valeurs sont les valeurs de la propriété. Les noms de propriété doivent être des chaînes de caractères non vides inférieures ou égales à 255 caractères, sans signe de dollars ($).

Les valeurs de la propriété peuvent être l'un des types de données suivants :

| Type de données       | Libellé                                                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Numéros               | En tant que [entiers](https://en.wikipedia.org/wiki/Integer) ou [flottent](https://en.wikipedia.org/wiki/Floating-point_arithmetic)                            |
| Booléens              |                                                                                                                                                                |
| Datetimes             | Formaté en tant que chaînes au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'H:mm:ss:SSSZ`. Non pris en charge dans les tableaux. |
| Chaînes de caractères | 255 caractères ou moins.                                                                                                                                       |
| Tableaux              | Les tableaux ne peuvent pas inclure les dates.                                                                                                                 |
| Objets                | Les objets seront ingérés en tant que chaînes.                                                                                                                 |
{: .reset-td-br-1 .reset-td-br-2}

Les objets de propriété événement qui contiennent des valeurs de tableau ou d'objet peuvent avoir une charge utile de propriété événement allant jusqu'à 50 Ko.

Par exemple, si une application eCommerce voulait envoyer un message à un utilisateur lorsqu'il abandonne son panier, il pourrait également améliorer son public cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété événement personnalisée de la 'valeur du panier' des paniers.

{% alert important %}
Chaque événement ou achat personnalisé peut avoir jusqu'à 256 propriétés personnalisées distinctes. Si un événement ou un achat personnalisé est enregistré avec plus de 256 propriétés, seuls les 256 premiers seront capturés et disponibles à utiliser.
{% endalert %}

!\[customEventProperties.png\]\[16\]

Les propriétés d'événements personnalisés peuvent également être utilisées pour la personnalisation dans le modèle de messagerie. Toute campagne utilisant [Action-Based Delivery][19] avec un événement de déclenchement peut utiliser des propriétés d'événement personnalisées de cet événement pour la personnalisation de la messagerie. Si une application de jeu voulait envoyer un message aux utilisateurs qui avaient terminé un niveau, il pourrait mieux personnaliser le message avec une propriété pour le temps qu'il a fallu aux utilisateurs pour compléter ce niveau. Dans cet exemple, le message est personnalisé pour trois segments différents en utilisant la [logique conditionnelle][18].  La propriété événement personnalisée appelée `time_spent`, peut être incluse dans le message en appelant `{% raw %} {{event_properties.${time_spent}}} {% endraw %}`.

{% alert warning %}
Déclenchement de messages dans l'application avec des propriétés d'événements personnalisés gabarits (par exemple, {% raw %}`{{event_properties.${time_spent}}}`{% endraw %}) échouera et ne s'affichera pas s'il n'y a pas de connexion Internet.
{% endalert %}

Vous pouvez modifier le type de données de votre propriété événement personnalisée, mais soyez conscient des impacts [des changements de types de données]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) après que les données aient été collectées.

{% alert important %}
Lorsque vous faites des appels à l'API et que vous utilisez le filtre "est vide", une propriété d'événement spécifique est considérée comme "vide" si elle est exclue de l'appel. Par exemple, si vous incluez `"event_property": "`, alors vos utilisateurs seront considérés comme "pas vide".
{% endalert %}

En ce qui concerne l'utilisation de l'abonnement, les propriétés d'événement personnalisées activées pour la segmentation avec les filtres `X Custom Event Property en Y Days` ou `X Purchase Property en Y Days` sont toutes comptées comme des points de données distincts en plus du point de données compté par l'événement personnalisé lui-même.

## Stockage personnalisé des propriétés d'événement

Les propriétés d'événements personnalisés sont conçues pour vous aider à augmenter la précision de ciblage et à rendre les messages encore plus personnalisés. Les propriétés personnalisées des événements peuvent être stockées dans Braze à court et à long terme.

Si vous souhaitez segmenter les valeurs des propriétés de l'événement, vous avez deux options :

1. **Dans les 30 jours :** Le personnel de support de Braze peut activer la segmentation des propriétés d'événement en fonction de la fréquence et de la récurrence des valeurs de propriété d'événements spécifiques dans les segments de Braze. Si vous souhaitez tirer parti des propriétés de l’événement au sein de Segments, veuillez contacter votre responsable de compte Braze ou le responsable du service à la clientèle. Notez que cette option aura un impact sur l'utilisation des données.<br><br>
2. **En 30 jours et au-delà de 30 jours :** Pour couvrir à la fois la segmentation à court et à long terme de la propriété d'événement, vous pouvez utiliser [Extensions de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Cette fonctionnalité vous permet de segmenter vos activités en fonction des événements personnalisés et des propriétés d'événements suivis au cours de l'année écoulée. Notez que cette option n'affectera pas l'utilisation des données.

Les équipes de soutien et de succès de Braze peuvent vous aider à recommander la meilleure approche en fonction de vos besoins spécifiques.
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png" [16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"

[7]: https://dashboard-01.braze.com/dashboard/custom_events/
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
