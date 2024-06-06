---
nav_title: Événements personnalisés
article_title: Événements personnalisés
page_order: 9
page_type: reference
description: "Cet article de référence décrit les propriétés et les événements personnalisés, la segmentation, leur utilisation, les propriétés d’entrées Canvas, où voir les analyses pertinentes, etc."
search_rank: 2
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Événements personnalisés

> Les événements personnalisés sont des actions effectuées par vos utilisateurs, ou des mises à jour de vos utilisateurs. Ils sont mieux adaptés pour le suivi des interactions utilisateur à forte valeur ajoutée dans votre application. La journalisation d’un événement personnalisé peut déclencher un nombre et un type de campagnes de suivi, et permet aux filtres de segmentation répertoriés de filtrer la fréquence et dernière occurrence de cet événement.

## Cas d’utilisation

Parmi les cas courants d’utilisation d’événements personnalisés figurent les situations suivantes :
- Déclencher une campagne ou un Canvas sur la base d’un événement personnalisé en utilisant la [livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).
- Segmenter les utilisateurs sur la base du nombre de fois où ils ont effectué un événement personnalisé, quand il s’est produit pour la dernière fois, etc.
- Utiliser le tableau de bord des [analytiques d’événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) pour visualiser et agréger le nombre de fois où s’est produit chaque événement
- Vous pouvez obtenir des analytiques supplémentaires en utilisant les rapports d’[entonnoir]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) et de [rétention]({{site.baseurl}}/user_guide/data_and_analytics/reporting/retention_reports/).
- Tirer parti des [propriétés d’entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) pour utiliser les métadonnées de votre événement personnalisé à des fins de personnalisation de vos étapes Canvas.
- Générer des analytiques plus sophistiquées avec [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents).
- Paramétrer des [événements d’exception Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events#canvas-exception-events) pour définir les moments où vos utilisateurs ne devraient pas avancer à l’étape suivante de votre Canvas.
- Et plus encore !

## Gestion des événements personnalisés

Pour créer et gérer des événements personnalisés dans le tableau de bord, allez sur **Manage Settings (Gérer les paramètres)** > **Custom Events (Événements personnalisés)**. Sur cette page, vous pouvez afficher, gérer ou bloquer les événements personnalisés existants, ou en créer un nouveau. Si vous bloquez un événement personnalisé, aucune donnée ne sera collectée concernant cet événement, les données existantes seront indisponibles, sauf si elles sont réactivées, et les événements exclus ne s’afficheront pas dans les filtres ou les graphiques.

## Journalisation des événements personnalisés

La liste suivante énumère les méthodes utilisées pour enregistrer des événements personnalisés sur les différentes plateformes. Dans ces pages, vous pourrez également trouver des documents sur la façon d’ajouter des propriétés et des quantités à vos événements personnalisés.

{% details Développer la documentation par plateforme %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

{% enddetails %}

## Stockage d’événements personnalisés

Toutes les données stockées sur les **Profils utilisateur**, y compris les métadonnées d’événement personnalisées (première/dernière occurrence, nombre total, et X en Y sur 30 jours), sont conservées indéfiniment tant que chaque profil est [actif]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Filtres de segmentation des événements personnalisés

Le tableau suivant montre les filtres disponibles pour la segmentation des utilisateurs en fonction d’événements personnalisés.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si l’événement personnalisé s’est produit **plus de X fois** | **PLUS DE** | **NOMBRE** |
| Vérifie si l’événement personnalisé s’est produit **moins de X fois** | **MOINS DE** | **NOMBRE** |
| Vérifie si l’événement personnalisé s’est produit **exactement X fois** | **EXACTEMENT** | **NOMBRE** |
| Vérifie si l’événement personnalisé s’est produit pour la dernière fois **après la date X** | **APRÈS** | **DATE** |
| Vérifie si l’événement personnalisé s’est produit pour la dernière fois **avant la date X** | **AVANT** | **DATE** |
| Vérifie si l’événement personnalisé s’est produit pour la dernière fois **il y a plus de X jours** | **PLUS DE** | **IL Y A X JOURS** (Nombre positif) |
| Vérifie si l’événement personnalisé a eu lieu **il y a moins de X jours** | **MOINS DE** | **IL Y A X JOURS** (Nombre positif) |
| Vérifie si l’événement personnalisé s’est produit **plus de X (Max = 50) fois** | **PLUS DE** | in les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’événement personnalisé s’est produit **moins de X (Max = 50) fois** | **MOINS DE** | in les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’événement personnalisé s’est produit **exactement X (Max = 50) fois** | **EXACTEMENT** | in les **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Analyse d’événements personnalisés

Braze indique le nombre de fois où ces événements ont eu lieu ainsi que la dernière fois qu’ils ont été exécutés par chaque utilisateur pour la segmentation. Sur la page de rapports d’**événements personnalisés** du tableau de bord, vous pouvez voir la fréquence à laquelle chaque événement personnalisé se produit, ainsi que par segment dans le temps pour une analyse plus détaillée. Ceci est particulièrement utile pour voir comment vos campagnes ont affecté les événements personnalisés,  en regardant les lignes grises placées par Braze sur la série temporelle pour indiquer la dernière fois qu’une campagne a été envoyée.

![Représentation graphique d’événements personnalisés sur le Tableau de bord montrant les tendances pour deux événements personnalisés différents][8]

{% alert tip %}
Comme pour un évènement personnalisé, [des attributs personnalisés incrémentaux]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) peuvent être utilisés pour mettre un compteur sur une action de l’utilisateur. Cependant, vous ne pourrez pas afficher les données d’attribut personnalisées dans une série temporelle. Les actions de l’utilisateur qui ne doivent pas être analysées dans les séries temporelles doivent être enregistrées via cette méthode.
{% endalert %}

### L’analyse des événements personnalisés ne s’affiche pas ?

Notez que les segments créés avec des données d’événements personnalisés ne peuvent pas afficher les données historiques datant d’avant leur création.

## Propriétés de l'événement  personnalisé

Avec des propriétés de l'événement personnalisé, vous pouvez définir des propriétés sur des événements personnalisés et des achats. Ces propriétés peuvent ensuite être utilisées pour des conditions de déclenchement admissibles supplémentaires, une personnalisation accrue des messages, des conversions de suivi et la génération d’analyses plus sophistiquées via l’exportation des données brutes.

{% alert important %}
Chaque événement personnalisé ou achat peut avoir jusqu’à 256 propriétés de l'événement personnalisé distinctes. Si un événement personnalisé ou un achat est enregistré avec plus de 256 propriétés, seules les 256 premières propriétés seront capturées et utilisables.
{% endalert %}

### Format attendu

Les valeurs des propriétés doivent être un objet dont les clés sont les noms de propriétés et les valeurs sont les valeurs de propriété. Les noms de propriété doivent être des chaînes de caractères non vides de moins de 255 caractères, qui ne commencent pas par un symbole de dollar ($).

Les valeurs de propriété peuvent être l’un des types de données suivants :

| Type de données | Description |
| --- | --- |
| Chiffres | Ces attributs peuvent être des [entiers (integer)](https://en.wikipedia.org/wiki/Integer) ou des [floats ](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booléens |  |
| Datetimes | Chaînes de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Non pris en charge dans les tableaux. |
| Chaînes de caractères | 255 caractères ou moins. |
| Tableaux | Les tableaux ne peuvent pas inclure des dates/horodatages. |
| Objets | Les objets seront ingérés en tant que chaînes de caractères. |
| Objets imbriqués | Objets se trouvant à l’intérieur d’autres objets. Pour plus d’informations, consultez la section [Objets imbriqués](#nested-objects) de cet article.
{: .reset-td-br-1 .reset-td-br-2}

Les objets Propriété d’événement qui contiennent des valeurs de tableau ou d’objet peuvent avoir une charge utile de propriété d’événement de 50 Ko maximum.

Vous pouvez modifier le type de données de votre propriété d’événement personnalisé, mais vous devez être conscient de l’impact si vous modifiez [des types de données]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) après que les données aient été collectées.

### Utiliser des propriétés de l’événement personnalisé

#### Déclencher des messages

Vous pouvez utiliser les propriétés de l’événement personnalisées pour affiner votre audience pour une campagne ou un Canvas particulier. Par exemple, si vous disposez d’une application d’e-commerce et souhaitez envoyer un message à un utilisateur lorsqu’il abandonne son panier, vous pourriez améliorer son audience cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété de l’événement personnalisé `cart value`.

![Filtres de propriété de l’événement personnalisé pour une carte abandonnée. Deux filtres sont combinés avec un opérateur ET pour envoyer cette campagne aux utilisateurs ayant abandonné leur carte avec une valeur de panier comprise entre 100 et 200 dollars][16]

Les propriétés de l’événement personnalisées imbriquées sont également prises en charge dans la [livraison par événement][19] ou le traitement des conversions.

![Filtres de propriété de l’événement personnalisé pour une carte abandonnée. Un filtre est sélectionné si un quelconque produit du panier a un prix supérieur à 100 dollars.][20]

#### Personnaliser des messages

Vous pouvez également utiliser les propriétés de l’événement personnalisées pour la personnalisation du modèle d’envoi de message. Toute campagne utilisant la [Livraison par événement][19] avec un événement déclencheur peut utiliser des propriétés de l’événement personnalisées de cet événement pour personnaliser les messages.

par exemple, si vous disposez d’une application de jeu et souhaitez envoyer un message aux utilisateurs qui ont terminé un niveau, vous pourriez personnaliser votre message avec une propriété pour le temps qu’il a fallu à l’utilisateur pour terminer le niveau. Dans cet exemple, le message est personnalisé pour trois segments différents en utilisant la [logique conditionnelle][18]. La propriété de l’événement personnalisée appelée `time_spent` peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% alert warning %}
Si l’utilisateur ne dispose pas d’une connexion Internet, les messages in-app déclenchés avec des propriétés de l’événement personnalisées modélisées (par exemple, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}), échoueront et ne s’afficheront pas.
{% endalert %}

#### Considérations relatives aux filtres

- **Appels API :** Lorsque vous faites des appels API et que vous utilisez le filtre « is blank » (est vide), une propriété de l’événement personnalisée est considérée comme « vide » si elle est exclue de l’appel. Par exemple, si vous deviez inclure `"event_property": ""`, alors vos utilisateurs seraient considérés comme « non vides ».
- **Entiers :** Lorsque vous filtrez selon une quantité de propriétés de l’événement personnalisées et que cette valeur est très importante, n’utilisez pas le filtre « exactement ». Si la quantité est trop importante, elle peut être arrondie à une certaine longueur et votre filtre ne fonctionnera donc pas comme vous l’attendez. 
 
#### Points de données

En ce qui concerne les inscriptions, les propriétés de l’événement personnalisé activées pour la segmentation avec les filtres suivants sont toutes comptées comme des points de données séparés qui viennent s’ajouter au point de données consommé par l’événement personnalisé lui-même :

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

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

Pour les envois de messages Canvas Flow, les `canvas_entry_properties` peuvent être utilisés en Liquid dans n’importe laquelle des étapes de message. Utilisez le Liquid lorsque vous référencez ces propriétés : ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Prenez note du fait que les événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi. 

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

### Objets imbriqués {#nested-objects}

Vous pouvez utiliser des objets imbriqués (c.-à-d. des objets qui se trouvent à l’intérieur d’un autre objet) pour envoyer des données JSON imbriquées en tant que propriétés d’événements personnalisés et d’achats. Ces données imbriquées peuvent être utilisées pour définir des informations personnalisées dans les messages, pou déclencher des envois de message et pour la segmentation.

#### Limitations

- Les données imbriquées sont prises en charge pour les [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) et les [événements d’achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) mais pas pour d’autres types d’événements.
- Les objets de propriété d’événement qui contiennent des valeurs de tableau ou d’objet peuvent avoir une charge utile de propriété d’événement de 50 Ko maximum.
- Les versions SDK suivantes prennent en charge les objets imbriqués :

{% sdk_min_versions web:3.3.0 ios:4.3.1 android:1.0.0 %}

#### Génération de schémas

La génération d’un schéma pour des événements comportant des propriétés de l'événement imbriqué vous permet d’accéder aux données imbriquées. Pour générer un schéma, procédez comme suit :
1. Aller à **Manage Settings (Gérer les paramètres)** > **Custom Events (Événements personnalisés)**.
2. Sélectionner **Manage Properties (Gérer les propriétés)** pour les événements avec des propriétés imbriquées.
3. Cliquez sur l’icône pour générer le schéma. Pour afficher le schéma, cliquez sur le bouton Plus.

![][6]{: style="max-width:80%;"}

Après avoir généré un schéma, vous pourrez référencer les données imbriquées pendant la [segmentation](#segmentation) et la [personnalisation](#personalization).

#### Exemples d’utilisation

##### Corps de la requête API

{% tabs %}
{% tab Music Example %}

Voici un exemple d’événement personnalisé `/users/track` « Liste de lecture créée ». Une fois qu’une liste de lecture a été créée, pour capturer ses propriétés, nous enverrons une demande API qui répertorie les « chansons» en tant que propriété, et un tableau des propriétés imbriquées des chansons.

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

Voici un exemple d’événement personnalisé `/users/track` « Commandé ». Une fois qu’une commande a été complétée, pour capturer les propriétés de cette commande, nous enverrons une demande API qui répertorie « r_details » en tant que propriété, ainsi que les propriétés imbriquées de cette commande.

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

Pour utiliser ces propriétés pour déclencher une campagne, sélectionnez votre événement personnalisé ou votre achat, puis ajoutez un filtre **Nested Property (Propriété imbriquée)**. Notez que le déclenchement de messages n’est pas encore pris en charge pour les messages in-app. Cependant, vous pouvez également ajouter des objets imbriqués après avoir généré un schéma.

{% tabs %}
{% tab Music Example %}

Déclenchement d’une campagne avec des propriétés imbriquées à partir de l’événement « Liste de lecture créée » :

![Un utilisateur choisissant une propriété imbriquée pour les filtres de propriété sur un événement personnalisé]({% image_buster /assets/img/nested_object2.png %})

L’état de déclenchement `songs[].album.yearReleased` « is » (est) « 1968 » correspond à un événement où l’une des chansons est dans un album publié en 1968. Nous utilisons les crochets `[]` pour traverser les tableaux et faisons correspondre si **n’importe quel** élément dans le tableau correspond à la propriété de l'événement.<br>
{% endtab %}
{% tab Restaurant Example %}

Déclenchement d’une campagne avec des propriétés imbriquées à partir de l’événement « Commandé » :

![Un utilisateur qui ajoute le filtre de propriété _details.name est McDonalds pour un événement personnalisé]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "McDonalds"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %} Si votre propriété d’événement contient les caractères `[]` or `.`, faites un échappement HTML en les entourant de guillemets doubles. Par exemple, `"songs[].album".yearReleased` correspondra à un événement avec la propriété littérale `"songs[].album"`.  {% endalert %}

##### Segmentation

Utilisez les [Segment extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) pour segmenter les utilisateurs en fonction des propriétés de l'événement imbriqué. Une fois que vous avez généré un schéma, l’explorateur d’objets imbriqué s’affiche dans la section Segmentation. La segmentation utilise la même notation que le déclenchement (voir [Déclenchement de messages](#message-triggering)). 

![][4]

##### Personnalisation

Utiliser le modal **Add Personalization (Ajouter une personnalisation)**, sélectionner **Advanced Event Properties (Propriétés de l'événement avancées)** comme type de personnalisation. Cela permet d’ajouter des propriétés de l'événement imbriqué une fois qu’un schéma a été généré.

![][5]{: style="max-width:70%;"}

##### Segmentation des propriétés de l’événement

La segmentation des propriétés d’événement vous permet de cibler les utilisateurs en fonction de leurs événements personnalisés, mais également en fonction des propriétés associées à ces événements. Cette fonctionnalité ajoute des options de filtrage supplémentaires lors de la segmentation des achats et des événements personnalisés.

![][3]

Ces filtres de segmentation comprennent :
- A fait un événement personnalisé avec la propriété Y avec la valeur V X fois dans les Y derniers jours .
- A effectué au moins un achat avec la propriété Y avec la valeur V X fois dans les Y derniers jours.
- Ajoute la capacité de segmenter sur 1, 3, 7, 14, 21 et 30 jours.

Les propriétés de l'événement avec des événements personnalisés sont mises à jour en temps réel pour tous les segments qui les utilisent. Vous pouvez gérer les propriétés sous **Manage Settings > Custom Events > Manage Properties (Gérer les paramètres > Événements personnalisés > Gérer les propriétés)**. Les propriétés de l'événement personnalisé utilisées dans certains filtres de segment ont un historique de 30 jours maximum. Contactez votre gestionnaire du succès des clients de Braze pour discuter de la segmentation des propriétés des événements pour vos événements personnalisés.

#### Foire aux questions

##### Cela consomme-t-il des points de données supplémentaires ?

Il n’y a pas de changement dans la façon dont nous facturons les points de données suite à l’ajout de cette capacité.

##### Combien de données imbriquées peuvent être envoyées ?

Si une ou plusieurs des propriétés d’ un événement contiennent des données imbriquées, la charge utile maximale pour toutes les propriétés combinées de l’événement est de 50 Ko. Toute requête dépassant cette limite de taille sera rejetée.

## Stockage de propriété d’événement personnalisé

Les propriétés de l'événement personnalisé sont conçues pour vous aider améliorer le ciblage et à personnaliser davantage vos messages. Les propriétés de l'événement personnalisé peuvent être stockées dans Braze à court et à long terme.

Si vous souhaitez segmenter les valeurs des propriétés de l'événement, vous avez deux options :

1. **sur 30 jours :** L‘équipe Support de Braze peut activer la segmentation des propriétés d’événements en fonction de la fréquence et de la dernière occurrence de valeurs spécifiques pour les propriétés d’événements dans les segments de Braze. Si vous souhaitez tirer parti des propriétés de l’événement dans Segments, contactez votre responsable de compte Braze ou votre gestionnaire du succès des clients. Notez que cette option aura un impact sur l’utilisation des données.<br><br>
2. **Sur et au-delà de 30 jours :** Pour couvrir la segmentation des propriétés d’événements à court et long terme, vous pouvez utiliser [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Cette fonctionnalité vous permet de segmenter en fonction des événements personnalisés et des propriétés de l’événement personnalisé qui ont fait l’objet d’un suivi au cours des deux dernières années. Notez que cette option n’affectera pas l’utilisation des données.

Contactez votre gestionnaire du succès des clients Braze pour obtenir des recommandations sur la meilleure approche en fonction de vos besoins spécifiques.


[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[3]: {% image_buster /assets/img/nested_object3.png %}
[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"
