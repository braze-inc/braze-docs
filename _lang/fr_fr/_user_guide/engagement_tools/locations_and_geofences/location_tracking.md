---
nav_title: Suivi de localisation
article_title: Suivi de localisation
page_order: 0
page_type: reference
description: "Cet article de référence explique comment utiliser le suivi de localisation et le ciblage de localisation dans vos applications ainsi que les partenaires qui prennent en charge le suivi de localisation."
tool: Location
search_rank: 2
---

# Suivi de localisation

> La collecte des données de localisation enregistre le dernier emplacement depuis lequel un utilisateur a ouvert votre application à l’aide des données de localisation GPS. Vous pouvez utiliser ces informations pour segmenter les données en fonction des utilisateurs qui se trouvaient dans un emplacement défini.

## Activer le suivi de localisation

Pour activer la collecte des données de localisation sur votre application, reportez-vous au guide du développeur de la plateforme que vous utilisez :

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

En général, les applications mobiles utilisent la puce GPS de l'appareil et d'autres systèmes (comme le balayage Wi-Fi) pour suivre l'emplacement/localisation d'un utilisateur. Les applications web utilisent le WPS (Wi-Fi Positioning System) pour suivre l'emplacement/localisation d'un utilisateur. Toutes ces plateformes demandent aux utilisateurs d'accepter l'emplacement/localisation. L’exactitude de vos données de suivi de localisation peut être affectée par le fait que vos utilisateurs aient activé ou non le Wi-Fi sur leur appareil. Les utilisateurs Android peuvent également choisir différents modes de localisation : les données des utilisateurs qui sont en mode « Économiseur de batterie » ou « Appareil uniquement » peuvent être inexactes.

### Emplacement des utilisateurs du SDK par adresse IP

Braze détecte les emplacements/localisations des utilisateurs à partir du pays géolocalisé en utilisant l'adresse IP du début de la première session SDK. 

Auparavant, Braze utilisait le code pays des paramètres régionaux de l'appareil lors de la création de l'utilisateur du SDK et pendant la durée de la première session. Ce n'est qu'après le traitement de la première session que l'adresse IP est utilisée pour définir un pays plus fiable pour l'utilisateur. Cela signifie que le pays de l'utilisateur n'a été défini avec une plus grande précision qu'à partir de la deuxième session, une fois que le début de la première session a été traité.

Désormais, Braze utilise l'adresse IP pour définir la valeur du pays sur les profils utilisateurs créés via le SDK, et ce paramètre de pays basé sur l'IP est disponible pendant et après la première session.

## Ciblage de localisation

En utilisant des segments et des données de suivi de la localisation, vous pouvez configurer des campagnes et des stratégies basées sur la localisation de vos utilisateurs. Par exemple, vous voudrez peut-être lancer une campagne promotionnelle pour les utilisateurs qui vivent dans une région donnée, ou exclure les utilisateurs situés dans une région dont les réglementations sont plus strictes.

Reportez-vous à [le ciblage par lieu]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/) pour plus d'informations sur la création d'un segment de lieu.

## Réglage de l’attribut de localisation par défaut

Vous pouvez également utiliser l’[endpoint `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) dans notre API pour mettre à jour l'attribut standard [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/). Voici un exemple :

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [ 
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## Prise en charge des partenariats pour les balises et les géorepérages

En combinant la prise en charge des balises ou des géorepérages existants avec nos fonctionnalités de ciblage et d'envoi de messages, vous obtenez davantage d'informations sur les actions physiques de vos utilisateurs, ce qui vous permet de leur envoyer des messages en conséquence. Vous pouvez tirer parti de l'emplacement/localisation avec certains de nos partenaires : 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## Foire aux questions

### Quand Braze recueille-t-il des données de localisation ?

Braze enregistre uniquement les données de localisation lorsque l’application est ouverte en avant-plan. Par conséquent, notre filtre `Most Recent Location` cible les utilisateurs en fonction du dernier endroit où ils ont ouvert l’application (également appelé début de session).

Gardez les nuances suivantes à l’esprit :

- Si l'emplacement/localisation est désactivé, le filtre `Most Recent Location` affiche le dernier emplacement/localisation enregistré.
- Si un utilisateur a déjà eu un emplacement/localisation enregistré sur son profil, il est concerné par le filtre `Location Available`, même s'il s'est désabonné de la géolocalisation depuis lors.

### Quelle est la différence entre le filtre Most Recent Device Locale (Dernière localisation de l’appareil) et Most Recent Location (Dernière localisation) ?

La `Most Recent Device Locale` provient des paramètres de l’appareil de l’utilisateur. Par exemple, pour les utilisateurs d'iPhone, cela apparaît dans leur appareil sous **Réglages** > **Général** > **Langue & Région.** Ce filtre est utilisé pour collecter des informations sur la langue et la mise en forme régionale, telles que les dates et adresses, et est indépendant du filtre `Most Recent Location`.

La `Most Recent Location` correspond aux dernières données GPS connues du dispositif. Elle est mise à jour au début de la session et est stockée dans le profil de l'utilisateur.

### Si un utilisateur s'abonne au suivi de l'emplacement/localisation, ses données d'emplacement antérieures sont-elles supprimées de Braze ?

Non. Si un emplacement/localisation a déjà été enregistré sur le profil d'un utilisateur, ces données ne sont pas automatiquement supprimées si l'utilisateur choisit par la suite de ne plus suivre l'emplacement/localisation.

## Résolution des problèmes

### Aucun utilisateur n'a d'emplacements/localisations disponibles

Braze capture par défaut l'emplacement/localisation le plus récent d'un utilisateur via le SDK. Cela signifie généralement que « l’emplacement récent » est l’endroit à partir duquel votre utilisateur a récemment utilisé votre application. Si vous envoyez des données de localisation Braze en arrière-plan, vous aurez peut-être des données plus granulaires.

Si aucun utilisateur n'a de lieux disponibles, deux vérifications rapides peuvent vous aider à confirmer la collecte des données et le transfert de la date.

#### Collecte de données

Confirmez que votre application recueille les données de localisation :

- Pour iOS, cela signifie que les utilisateurs choisissent de partager leurs données de localisation via une invite à un moment donné du parcours utilisateur. 
- Pour Android, assurez-vous que votre application demande des autorisations de localisation fine ou grossière lors de l’installation.

Pour voir si les données de localisation de l'utilisateur sont envoyées à Braze, utilisez le filtre **Location Available**. Ce filtre vous permet de voir le pourcentage d’utilisateurs avec un « emplacement le plus récent ».

![Un segment d'emplacement/localisation qui utilise le filtre "Emplacement disponible".]({% image_buster /assets/img_archive/trouble7.png %})

#### Transfert de données

Confirmez auprès de vos développeurs que les données de localisation sont bien transmises à Braze. Normalement, la transmission des données de localisation est gérée automatiquement par le SDK après que l'utilisateur a donné les autorisations, mais vos développeurs ont peut-être désactivé le suivi de localisation dans Braze. Vous trouverez plus d’informations sur le suivi des données de localisation pour :
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)