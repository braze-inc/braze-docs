---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Cet article de référence décrit le partenariat entre Braze et Foursquare, une plateforme de données de localisation qui permet de déclencher des événements en temps réel en fonction de la localisation."
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) est une plateforme de données de localisation qui fournit un ciblage des données de localisation dans vos campagnes Braze. Utilisez le SDK Pilgrim de Foursquare sur les applications iOS et Android pour déclencher des événements en temps réel en fonction de l'emplacement/localisation, ce qui vous permet d'exploiter les puissantes capacités de ciblage géographique de Foursquare pour envoyer des messages pertinents et personnalisés avec Braze.

_Cette intégration est gérée par Foursquare._

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Foursquare | Un compte Foursquare est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Espace de travail Braze et identifiants d'applications | L'espace de travail Braze et les ID d'application se trouvent dans la [console de développement]({{site.baseurl}}/api/api_key/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Intégration

Pour intégrer les deux plateformes, vous devez intégrer les deux SDK et mapper les champs utilisateur correspondants. Après avoir intégré le SDK Pilgrim, vous recevrez des événements de localisation sur l'appareil ou sur un webhook. 

### Étape 1 : Mapper les champs d'ID utilisateur

Pour mapper correctement les champs entre les deux SDK, définissez le même ID utilisateur dans les deux systèmes à l'aide de la [`changeUser`méthode]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids) du SDK Braze `setUserId` et de la méthode de [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) dans le SDK Pilgrim.

### Étape 2 : Configurer la console Pilgrim


Recherchez l'espace de travail et les ID d'application dans la console de développement Braze. Ensuite, entrez votre clé d'API Braze REST et vos identifiants d'application dans la console Foursquare Pilgrim.

Une fois que vous avez configuré la console Pilgrim, le SDK Pilgrim enregistre les événements de localisation et les transmet à Braze, ce qui vous permet de recibler et de segmenter les clients qualifiés. Consultez le [site des développeurs de Foursquare](https://developer.foursquare.com/) pour plus de détails.

{% alert important %}
Le SDK Pilgrim nécessite que vous activiez les services de localisation.
{% endalert %}

## Messages déclencheurs

Une fois l'intégration configurée, vous pouvez configurer une campagne ou un canevas qui permettra d'agir en dehors des événements d'emplacement/localisation générés par le SDK Pilgrim. Cette méthode d'intégration est idéale pour l'envoi de messages en temps réel juste après que les utilisateurs entrent dans un lieu qui les intéresse ou pour retarder les communications de suivi après leur départ, comme une note de remerciement ou un rappel.

Pour envoyer une campagne qui enverra des messages en fonction d'un emplacement/localisation défini :
- Créez une campagne Braze ou un canvas en activant l’option **Livraison par événement**
- Pour votre déclencheur, utilisez un événement personnalisé `arrival` ou avec un filtre de propriétés d'événement `locationType`, comme indiqué dans la capture d'écran suivante.

![Une campagne basée sur l'action à l'étape de réception indiquant « arrivée » sélectionnée comme option « Réaliser un événement personnalisé », où « LocationType » est égal à « domicile ». ]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Reciblage

Pour recibler vos utilisateurs, utilisez le SDK Pilgrim pour définir un `last_location` attribut personnalisé sur les profils utilisateur de vos utilisateurs de Braze. Vous pouvez ensuite utiliser la comparaison `matches regex` pour recibler les utilisateurs qui se sont rendus à un endroit précis dans le monde réel, par exemple en segmentant tous les utilisateurs qui se sont récemment rendus dans une pizzeria.

![Une campagne basée sur l'action à l'étape des utilisateurs cibles indiquant que « last_location » est égal à « Pizza Place ». ]({% image_buster /assets/img_archive/last-location-segment.png %})

Vous pouvez également segmenter les utilisateurs de Braze qui ont visité un type de site particulier en fonction de ceux de Foursquare `primaryCategoryId` au cours d'une période donnée. Pour tirer parti de ce point de données pour vos cas d'utilisation de reciblage, enregistrez-`primaryCategoryId` en tant que propriété d’événement lors de votre processus de segmentation d'audience. [Pour identifier les utilisateurs et les propriétés utilisés par l'API Foursquare et le SDK Pilgrim, consultez le site des développeurs de Foursquare.](https://developer.foursquare.com/)


