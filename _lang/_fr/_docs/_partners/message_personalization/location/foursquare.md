---
nav_title: Foursquare
article_title: Foursquare
alias: /fr/partners/foursquare/
description: "Cet article décrit le partenariat entre Braze et Foursquare, une plateforme de données de localisation, fournissant le déclenchement en temps réel d'événements en fonction de l'emplacement."
page_type: partenaire
search_tag: Partenaire
---

# Foursquare

{% include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) est une plateforme de données de localisation fournissant des données de localisation ciblées dans vos campagnes Braze. Utilisez Foursquare Pilgrim SDK sur les applications iOS et Android pour fournir le déclenchement d'événements en temps réel en fonction de l'emplacement, vous permettant d'exploiter les puissantes capacités de géo-ciblage de Foursquare pour envoyer des messages pertinents et personnalisés avec Braze.

## Pré-requis

| Exigences                   | Libellé                                                                                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Braze clé API REST          | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Braze App Group and App IDs | Le groupe d'applications Braze et les ID d'applications se trouvent dans la [console développeur]({{site.baseurl}}/docs/api/api_key/).                                                                       |
| Compte Foursquare           | Vous devez avoir un compte Foursquare actif pour utiliser leurs services avec Braze                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Pour intégrer les deux plates-formes, vous devez intégrer les deux SDK et mapper les champs utilisateur correspondants. Après avoir intégré le Pilgrim SDK, vous recevrez des événements de localisation sur l'appareil ou à un webhook.

### Étape 1 : Mappez les champs ID utilisateur

Pour associer correctement les champs entre les deux SDK, définir le même ID d'utilisateur dans les deux systèmes en utilisant la méthode [`changeUser`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids) dans le Braze SDK et la méthode `setUserId` de [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) dans le Pilgrim SDK.

### Étape 2 : Configurer la console de Pilgrim
!\[Pilgrim Developer Console\]\[2\]{: style="float:right;max-width:40%;margin-left:15px;"}

Trouvez les ID du groupe d'applications et des applications dans la console de développement de Braze. Ensuite, entrez votre clé API et votre ID d'application Braze REST dans la console Foursquare de Pilgrim.

Une fois que vous avez configuré la Console de Pèlerin, le Pilgrim SDK enregistrera les événements de localisation et les transmettra au Brésil, vous permettant de rediriger et de segmenter des clients qualifiés. Voir le site de développement de [Foursquare](https://developer.foursquare.com/) pour plus de détails.

{% alert important %}
Pilgrim SDK exige que vous autorisiez les services de localisation.
{% endalert %}

## Déclenchement des messages

Une fois l'intégration mise en place, vous pouvez mettre en place une campagne ou Canvas qui se chargera des événements de localisation générés par le Pilgrim SDK. Cette route d'intégration est idéale pour la messagerie en temps réel dès que les utilisateurs entrent dans un lieu d'intérêt ou de communication de suivi retardée après leur départ, comme une note de remerciement ou un rappel.

Pour envoyer une campagne qui enverra des messages en fonction d'un emplacement défini :
- Créez une campagne Braze ou Canvas qui envoie avec **Livraison avec Action-Based**
- Pour votre déclencheur, utilisez un événement personnalisé de `arrivée` avec un filtre de propriété événement pour `locationType` comme indiqué ci-dessous.

![Console de Développeur de Pèlerin]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Reciblage

Pour recibler vos utilisateurs, utilisez le SDK de Pilgrim pour définir un attribut personnalisé `last_location` sur les profils d'utilisateurs de Braze. Vous pouvez ensuite utiliser la comparaison de `correspondances regex` pour retarget les utilisateurs qui sont allés à un emplacement particulier dans le monde réel, par exemple, segmenter tous les utilisateurs qui se trouvaient récemment dans une pizzeria.

![Ciblage du tableau de bord Braze]({% image_buster /assets/img_archive/last-location-segment.png %})

Vous pouvez également segmenter les utilisateurs de Braze qui ont visité un type particulier de lieu basé sur l' `primaryCategoryId` de Foursquare dans une fenêtre de temps particulière. Pour tirer parti de ce point de données pour vos cas d'utilisation de retardage, enregistrez `primaryCategoryId` en tant que propriété événement pendant le processus de segmentation de votre auditoire. Pour identifier les utilisateurs et les propriétés utilisées par l'API Foursquare et le SDK Pilgrim, veuillez vous référer au site de développement [Foursquare](https://developer.foursquare.com/).
[1]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %} [2]: {% image_buster /assets/img_archive/pilgrim-dev-console.png %}