---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Cet article de référence présente le partenariat entre Braze et Foursquare, une plateforme de données de localisation, permettant de déclencher des événements en temps réel en fonction de l’emplacement."
page_type: partner
search_tag: Partenaire

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) est une plateforme de données de localisation qui permet de cibler les données de localisation dans vos campagnes Braze. Utilisez le SDK Pilgrim de Foursquare sur les applications iOS et Android pour fournir un déclenchement d’événement en temps réel basé sur la localisation, ce qui vous permet d’exploiter les puissantes capacités de géolocalisation de Foursquare pour envoyer des messages pertinents et personnalisés avec Braze.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Foursquare | Un compte Foursquare est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| ID de groupe d’applications et ID d’application Braze | Les ID de groupe d’apps et d’application Braze se trouvent dans la [Developer Console (Console du développeur)]({{site.baseurl}}/api/api_key/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Pour intégrer les deux plateformes, vous devez intégrer les deux SDK et mapper les champs utilisateur correspondants. Après avoir intégré le SDK Pilgrim, vous recevrez des événements de localisation sur l’appareil ou vers un webhook. 

### Étape 1 : Mapper les champs ID utilisateur

Pour mapper correctement les champs entre les deux SDK, définissez le même ID utilisateur dans les deux systèmes en utilisant la [méthode `changeUser`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids) dans le SDK Braze et la méthode `setUserId` de [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) dans le SDK Pilgrim.

### Étape 2 : Configurer la console Pilgrim
![Image de la console Pilgrim demandant l’ID du groupe, l’ID de l’application Android et l’ID de l’application iOS.][2]{: style="float:right;max-width:40%;margin-left:15px;"}

L’ID de groupe d’apps et l’ID d’application se trouvent dans la Developer Console de Braze. Ensuite, entrez votre clé d’API REST de Braze et vos identifiants d’applications dans la console Pilgrim de Foursquare.

Une fois que vous avez configuré la console Pilgrim, le SDK Pilgrim enregistre les événements de localisation et les transmet à Braze, ce qui vous permet de recibler et de segmenter les clients qualifiés. Consultez le [site du développeur Foursquare](https://developer.foursquare.com/) pour plus de détails.

{% alert important %}
Le SDK Pilgrim nécessite que vous activiez les services de localisation.
{% endalert %}

## Déclenchement des messages

Une fois l’intégration configurée, vous pouvez mettre en place une campagne de notification push ou Canvas qui activera les événements de localisation générés par le SDK Pilgrim. Cette méthode d’intégration est idéale pour les envois de messages en temps réel, lorsque les utilisateurs entrent dans un site ou un lieu d’intérêt ou pour les messages retardés de suivi après qu’ils l’aient quitté, comme une note de remerciement ou un rappel.

Pour envoyer une campagne qui enverra des messages en fonction d’un emplacement défini :
- Créez une campagne Braze ou un Canvas qui envoie via une **Livraison par événement**
- Pour votre déclencheur, utilisez un événement personnalisé de `arrival` avec un filtre de propriété d’événement pour `locationType` comme indiqué dans la capture d’écran suivante.

![Une campagne basée sur l’action dans l’étape de livraison montrant « arrival » sélectionné comme option « perform custom event », où « locationType » est égal à « home ».]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Reciblage

Pour recibler vos utilisateurs, utilisez le SDK Pilgrim pour définir un attribut personnalisé `last_location` sur les profils d’utilisateur de vos utilisateurs Braze. Vous pouvez ensuite utiliser la `matches regex` comparaison pour recibler les utilisateurs qui se sont rendus à un endroit particulier dans le monde réel, par exemple en segmentant tous les utilisateurs qui se sont rendus récemment dans une pizzeria.

![Campagne basée sur l’action dans l’étape des utilisateurs cibles montrant « last_location » égal à « Pizza Place ».]({% image_buster /assets/img_archive/last-location-segment.png %})

Vous pouvez également segmenter dans Braze les utilisateurs qui ont visité un type de lieu particulier en fonction du `primaryCategoryId` de Foursquare dans une plage de temps donnée. Pour exploiter ce point de données pour vos cas d’utilisation de reciblage, enregistrez `primaryCategoryId` comme une propriété d’événement pendant votre processus de segmentation d’audience. Pour identifier les utilisateurs et les propriétés utilisés par l’API Foursquare et le SDK Pilgrim, reportez-vous au [site du développeur Foursquare](https://developer.foursquare.com/).

[1]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[2]: {% image_buster /assets/img_archive/pilgrim-dev-console.png %}