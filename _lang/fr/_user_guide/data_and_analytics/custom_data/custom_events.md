---
nav_title: Événements personnalisés
article_title: Évènements personnalisés
page_order: 1
page_type: reference
description: "Cet article de référence décrit les événements et propriétés personnalisés, leur utilisation et où voir les analyses pertinentes."

---

# [![Cours d’apprentissage Braze]{% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Événements personnalisés

Les événements personnalisés sont des actions effectuées par vos utilisateurs, ou des mises à jour de vos utilisateurs. Ils sont mieux adaptés pour le suivi des interactions utilisateur à forte valeur ajoutée dans votre application. La journalisation d’un événement personnalisé peut déclencher un nombre et un type de campagnes de suivi, et permet aux filtres de segmentation répertoriés de filtrer la fréquence et dernière occurrence de cet événement.

## Gestion des événements personnalisés

Pour créer et gérer des événements personnalisés dans le tableau de bord, allez sur **Manage Settings** > **Événements personnalisés**. Sur cette page, vous pouvez afficher, gérer ou bloquer les événements personnalisés existants, ou en créer un nouveau. Si vous bloquez un événement personnalisé, aucune donnée ne sera collectée concernant cet événement, les données existantes seront indisponibles, sauf si elles sont réactivées, et les événements exclus ne s’afficheront pas dans les filtres ou les graphiques.

## Journalisation des événements personnalisés

La liste suivante énumère les méthodes utilisées pour enregistrer des événements personnalisés sur les différentes plateformes. Dans ces pages, vous pourrez également trouver des documents sur la façon d’ajouter des propriétés et des quantités à vos événements personnalisés.

{% details Expand for documentation by platform %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Windows Universal]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

{% enddetails %}

## Stockage d’événements personnalisés

Toutes les données stockées sur les **Profils utilisateur**, y compris les métadonnées d’événement personnalisées (première/dernière occurrence, nombre total, et X en Y sur 30 jours), sont conservées indéfiniment tant que chaque profil est [actif]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Filtres de segmentation des événements personnalisés

Le tableau suivant montre les filtres disponibles pour la segmentation des utilisateurs en fonction d’événements personnalisés.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si l’événement personnalisé s’est produit **plus de X fois** | **PLUS QUE** | **CHIFFRE** |
| Vérifie si l’événement personnalisé s’est produit **moins de X fois** | **MOINS QUE** | **CHIFFRE** |
| Vérifie si l’événement personnalisé s’est produit ** exactement X fois** | **EXACTEMENT** | **CHIFFRE** |
| Vérifie si l’événement personnalisé s’est produit pour la dernière fois **après la date X** | **APRÈS** | **DATE** |
| Vérifie si l’événement personnalisé s’est produit pour la dernière fois **avant la date X** | **AVANT** | **DATE** |
| Vérifie si l’événement personnalisé s’est produit pour la dernière fois il** y a plus de X jours** | **PLUS DE** | **IL Y A X JOURS** (Nombre positif) |
| Vérifie si l’événement personnalisé a eu lieu **il y a moins de X jours** | **MOINS QUE** | **IL Y A X JOURS** (Nombre positif) |
| Vérifie si l’événement personnalisé s’est produit **plus de X (Max = 50)  fois** | **PLUS QUE** | dans les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’événement personnalisé s’est produit **moins de X (Max = 50) fois** | **MOINS QUE** | dans les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’événement personnalisé s’est produit **exactement X (Max = 50)  fois** | **EXACTEMENT** | dans les **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Analyse d’événements personnalisés

Braze indique le nombre de fois où ces événements ont eu lieu ainsi que la dernière fois qu’ils ont été exécutés par chaque utilisateur pour la segmentation. Sur la page [Événements personnalisés][7] du tableau de bord, vous pouvez voir la fréquence à laquelle chaque événement personnalisé se produit, ainsi que par segment dans le temps pour une analyse plus détaillée. Ceci est particulièrement utile pour voir comment vos campagnes ont affecté les événements personnalisés,  en regardant les lignes grises placées par Braze sur la série temporelle pour indiquer la dernière fois qu’une campagne a été envoyée.

![Représentation graphique d’événements personnalisés sur le Tableau de bord montrant les tendances pour deux événements personnalisés différents][8]

{% alert tip %}
Comme pour un évènement personnalisé, [des attributs personnalisés incrémentaux]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) peuvent être utilisés pour mettre un compteur sur une action de l’utilisateur. Cependant, vous ne pourrez pas afficher les données d’attribut personnalisées dans une série temporelle. Les actions de l’utilisateur qui ne doivent pas être analysées dans les séries temporelles doivent être enregistrées via cette méthode.
{% endalert %}

### L’analyse des événements personnalisés ne s’affiche pas ?

Notez que les segments créés avec des données d’événements personnalisés ne peuvent pas afficher les données historiques datant d’avant leur création.

## Propriétés de l'événement  personnalisé

Avec des propriétés de l'événement personnalisé, vous pouvez définir des propriétés sur des événements personnalisés et des achats. Ces propriétés peuvent ensuite être utilisées pour des conditions de déclenchement admissibles supplémentaires, une personnalisation accrue des messages, des conversions de suivi et la génération d’analyses plus sophistiquées via l’exportation des données brutes.

Les valeurs des propriétés doivent être un objet dont les clés sont les noms de propriétés et les valeurs sont les valeurs de propriété. Les noms de propriété doivent être des chaînes de caractères non vides de moins de 255 caractères, qui ne commencent pas un symbole de dollar ($).

Les valeurs de propriété peuvent être l’un des types de données suivants :

| Type de données | Description |
| --- | --- |
| Chiffres | Ces attributs peuvent être des [entiers (integer)](https://en.wikipedia.org/wiki/Integer) ou des [floats ](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booléens |  |
| Datetimes | Chaînes de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Non pris en charge dans les tableaux. |
| Strings | 255 caractères ou moins. |
| Tableaux | Les tableaux ne peuvent pas inclure des dates/horodatages. |
| Objets | Les objets seront ingérés en tant que chaînes de caractères. |
| Objets imbriqués | Objets se trouvant à l’intérieur d’autres objets. Pour plus d’informations, consultez la section [Objets imbriqués](#nested-objects) de cet article.
{: .reset-td-br-1 .reset-td-br-2}

Les objets de propriété d’événement qui contiennent des valeurs de tableau ou d’objet peuvent avoir une charge utile de propriété d’événement de 50 Ko maximum.

Par exemple, si une application d’e-commerce souhaite envoyer un message à un utilisateur lorsqu’il abandonne son panier, elle pourrait en outre améliorer son public cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété d’événement personnalisé « Valeur du panier » sur les paniers des utilisateurs.

{% alert important %}
Chaque événement personnalisé ou achat peut avoir jusqu’à 256 propriétés de l'événement personnalisé distinctes. Si un événement personnalisé ou un achat est enregistré avec plus de 256 propriétés, seuls les 256 premières propriétés seront capturées et utilisables.
{% endalert %}

![Filtres de propriété d’événement personnalisé pour une carte abandonnée. Deux filtres sont combinés avec un opérateur ET pour envoyer cette campagne aux utilisateurs ayant abandonné leur carte avec une valeur de panier comprise entre 100 et 200 dollars][16]

Les propriétés de l'événement personnalisées peuvent également être utilisées pour la personnalisation du modèle de messagerie. Toute campagne utilisant la [Livraison par événement][19] avec un événement déclencheur peut utiliser des propriétés de l'événement personnalisées de cet événement pour la personnaliser les messages. Si un jeu souhaite envoyer un message aux utilisateurs qui ont terminé un niveau, il pourrait personnaliser le message avec une propriété pour le temps qu’il a fallu à l’utilisateur pour terminer le niveau. Dans cet exemple, le message est personnalisé pour trois segments différents en utilisant la [logique conditionnelle][18].  La propriété d’événement personnalisée appelée ``time_spent``, peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

Notez que pour les messages du Canvas , les propriétés de l'événement de campagne d’administration basées sur les actions sont éphémères et ne peuvent être utilisées que lorsque elles se produisent. Cela signifie que les propriétés de l'événement personnalisées peuvent être référencées uniquement dans la première étape d’un Canvas. Assurez-vous d’utiliser {% raw %}`{{canvas_entry_properties.${property_name}}}`{% endraw %} si vous référencez des propriétés de l'événement dans la première étape.

{% alert warning %}
Messages in-app déclenchés avec des modèles de propriétés de l'événement personnalisé (par exemple, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) échouera et ne s’affichera pas s’il n’y a pas de connectivité Internet.
{% endalert %}

Vous pouvez modifier le type de données de votre propriété d’événement personnalisé, mais vous devez être conscient de l’impact si vous modifiez [des types de données]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) après que les données aient été collectées.

{% alert important %}
Lorsque vous faites des appels API et que vous utilisez le filtre « is blank », une propriété d’événement personnalisée est considéré comme « vide » si exclu de l’appel. Par exemple, si vous deviez inclure `"event_property": "`, alors vos utilisateurs seraient considérés comme « non vides ».
{% endalert %}

En ce qui concerne les inscriptions, les propriétés de l'événement personnalisé activées pour la segmentation avec les filtres `X Custom Event Property in Y Days` ou `X Purchase Property in Y Days` sont toutes comptées comme des points de données séparés qui viennent s’ajouter au point de données consommé par l’événement personnalisé lui-même.

### Objets imbriqués {#nested-objects}

Vous pouvez utiliser des objets imbriqués (c.-à-d. des objets qui se trouvent à l’intérieur d’un autre objet) pour envoyer des données JSON imbriquées en tant que propriétés d’événements personnalisés et d’achats. Ces données imbriquées peuvent être utilisées pour définir des informations personnalisées dans les messages, pou déclencher des envois de message et pour la segmentation.

{% alert important %}
Cette fonctionnalité est disponible généralement. Cependant, le déclenchement des messages et la segmentation des utilisateurs basés sur ces données sont en accès anticipé. Contactez votre gestionnaire de compte Braze pour plus d’informations.
{% endalert %}

#### Limitations

- Les données imbriquées ne peuvent être envoyées qu’avec des [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) et [des événements d’achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/).
- L’envoi d’attributs personnalisés imbriqués (objets comme type de données d’attribut personnalisé) est limité aux clients participant à l’accès anticipé. Pour plus d’informations, consultez la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/).
- Les objets de propriété d’événement qui contiennent des valeurs de tableau ou d’objet peuvent avoir une charge utile de propriété d’événement de 50 Ko maximum.
- Les versions SDK suivantes prennent en charge les objets imbriqués :

{% sdk_min_versions web:3.3.0 ios:4.3.1 android:1.0.0 %}

#### Exemples d’utilisation

##### Corps de la requête API

{% tabs %}
{% tab Music Example %}

Voici un `/users/track` exemple d’événement personnalisé « Liste de lecture créée ». Une fois qu’une liste de lecture a été créée, pour capturer ses propriétés, nous enverrons une demande API qui répertorie les « chansons» en tant que propriété, et un tableau des propriétés imbriquées des chansons.

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

Voici un `/users/track` exemple d’événement personnalisé « Commandé ». Une fois qu’une commande a été complétée, pour capturer les propriétés de cette commande, nous enverrons une demande API qui répertorie "r_details" en tant que propriété, ainsi que les propriétés imbriquées de cette commande.

```
...
"properties": {
  "r_details": {
    "name": "McDonalds",
    "identifier": "12345678",
    "location" ; {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

##### Modèles Liquid

Les exemples de templating Liquid suivants montrent comment référencer les propriétés imbriquées de la requête API précédente pour les utiliser dans vos communications Liquid. À l’aide de Liquid et de la notation par points, parcourez les données imbriquées pour trouver le nœud spécifique que vous souhaitez inclure dans vos messages.

{% tabs local %}
{% tab Music Example %}
Modèle Liquid dans un message déclenché par l’événement « Liste de lecture créée » :

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind"<br> 
`{{event_properties.${songs}[1].title}}`: "While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Modèle Liquid dans un message déclenché par l’événement  « Commandé » :

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

##### Déclenchement du message

Pour utiliser ces propriétés pour déclencher une campagne, sélectionnez votre événement personnalisé ou votre achat, puis ajoutez un filtre **Propriété imbriquée**. Notez que le déclenchement de messages n’est pas encore pris en charge pour les messages in-app.

{% alert important %}
Les objets imbriqués sont disponibles généralement. Cependant, le déclenchement des messages et la segmentation des utilisateurs basés sur ces données sont en accès anticipé. Contactez votre gestionnaire de compte Braze pour plus d’informations.
{% endalert %}

{% tabs %}
{% tab Music Example %}

Déclenchement d’une campagne avec des propriétés imbriquées à partir de l’événement « Liste de lecture créée » :

![Un utilisateur choisissant une propriété imbriquée pour les filtres de propriété sur un événement personnalisé]({% image_buster /assets/img/nested_object2.png %})

L’état de déclenchement `songs[].album.yearReleased` « is » (1968) correspond à un événement où l’une des chansons est dans un album publié en 1968. Nous utilisons les crochets `[]` pour traverser les tableaux et faisons correspondre si **n’importe quel** élément dans le tableau correspond à la propriété de l'événement. <br> 
{% endtab %}
{% tab Restaurant Example %}

Déclenchement d’une campagne avec des propriétés imbriquées  à partir de l’événement « Commandé » :

![Un utilisateur qui ajoute le filtre de propriété r_détails.name est McDonalds pour un événement personnalisé]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "Mcdonalds »<br> 
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %} Si votre propriété d’événement contient les caractères `[]` or `.`, faites un échappement HTML en les entourant de guillemets doubles. Par exemple, `"songs[].album".yearReleased` correspondra à un événement avec la propriété littérale `"songs[].album"`.  {% endalert %}

##### Segmentation

Utilisez les [Segment extensions ]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) pour segmenter les utilisateurs en fonction des propriétés de l'événement imbriqué. La segmentation utilise la même notation que le déclenchement (voir [Déclenchement de messages](#message-triggering)).

{% alert important %}
Les objets imbriqués sont disponibles généralement . Cependant, le déclenchement des messages et la segmentation des utilisateurs basés sur ces données sont en accès anticipé. Contactez votre gestionnaire de compte Braze pour plus d’informations.
{% endalert %}

##### Segmentation des propriété d’événement

La segmentation des propriétés d’événement vous permet de cibler les utilisateurs non seulement en fonction de leurs événements personnalisés, mais aussi en fonction des propriétés associées à ces événements. Cette fonction ajoute des options de filtrage supplémentaires lors de la segmentation des achats et des événements personnalisés.

![][3]

Ces filtres de segmentation incluent :
- A eu un événement personnalisé avec la propriété Y avec la valeur V X fois dans les Y derniers jours .
- A effectué des achats avec la propriété Y avec la valeur V X fois dans les Y derniers jours.
- Ajoute la capacité de segmenter sur les 1, 3, 7, 14, 21 et 30 jours.

Contrairement aux [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), les segments utilisés sont mis à jour en temps réel, prennent en charge une quantité illimitée de segments, offrent un historique de 30 jours au maximum et entraînent des points de données. Comme elles consomment des points de données supplémentaires, vous devez contacter votre CSM pour activer les propriétés de l'événement dans vos événements personnalisés. Une fois approuvées, des propriétés supplémentaires peuvent être ajoutées dans le tableau de bord sous **Manage Settings > Événements personnalisés > Gérer les propriétés**, puis utilisées dans l’étape Ciblage de la campagne ou du Canvas.

#### Questions fréquemment posées

##### Cela consomme-t-il des points de données supplémentaires ?

Il n’y a pas de changement dans la façon dont nous facturons les points de données suite à l’ajout de cette capacité.

##### Combien de données imbriquées peuvent être envoyées ?

Si une ou plusieurs des propriétés d’ un événement contiennent des données imbriquées, la charge utile maximale pour toutes les propriétés combinées de l’événement est de 50 Ko. Toute requête dépassant cette limite de taille sera rejetée.

## Stockage de propriété d’événement personnalisé

Les propriétés de l'événement personnalisé sont conçues pour vous aider améliorer le ciblage et à personnaliser davantage vos messages. Les propriétés de l'événement personnalisé peuvent être stockées dans Braze à court et à long terme.

Si vous souhaitez segmenter les valeurs des propriétés de l'événement, vous avez deux options :

1. **sur 30 jours :** L‘équipe Support de Braze peut activer la segmentation des propriétés d’événements en fonction de la fréquence et de la dernière occurence de valeurs spécifiques  pour les propriétés d’événements dans les segments de Braze. Si vous souhaitez tirer parti des propriétés de l'événement dans Segments, contactez votre responsable de compte Braze ou votre gestionnaire du succès des clients. Notez que cette option aura un impact sur l’utilisation des données.<br> <br> 
2. **Sur et au-delà de 30 jours :** Pour couvrir la segmentation des propriétés d’événements à court et long terme, vous pouvez utiliser [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Cette fonction vous permet de segmenter en fonction des événements personnalisés et des propriétés de l'événement personnalisé qui ont fait l’objet d’un suivi au cours de l’année écoulée. Notez que cette option n’affectera pas l’utilisation des données.

Les équipes Réussite Client ou Support de Braze peuvent vous recommander la meilleure approche en fonction de vos besoins spécifiques. 


[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[3]: {% image_buster /assets/img/nested_object3.png %}
[7]: https://dashboard-01.braze.com/dashboard/custom_events/
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
