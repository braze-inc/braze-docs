---
nav_title: Emplacement/localisation
article_title: Emplacements/localisation
page_order: 0
page_type: reference
description: "Cet article de référence explique comment utiliser la géolocalisation et le ciblage d'emplacements dans vos apps et quels partenaires prennent en charge la géolocalisation."
tool: Location
search_rank: 2
---

# Emplacement/localisation

> La collecte d'emplacements permet de capturer l'emplacement/localisation le plus récent d'un utilisateur lorsque l'application a été ouverte à l'aide des données de localisation GPS. Vous pouvez utiliser ces informations pour segmenter les données en fonction des utilisateurs qui se trouvaient dans un emplacement/localisation défini.

## Activation de l'emplacement/localisation

Pour activer la collecte d'emplacements/localisations sur votre app, reportez-vous au guide du développeur de la plateforme que vous utilisez :

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

En général, les applications mobiles utilisent la puce GPS de l'appareil et d'autres systèmes (comme le balayage Wi-Fi) pour suivre l'emplacement/localisation de l'utilisateur. Les applications web utiliseront le WPS (Wi-Fi Positioning System) pour suivre l'emplacement/localisation de l'utilisateur. Toutes ces plateformes exigeront des utilisateurs qu'ils acceptent l'emplacement/localisation. La précision de vos données d'emplacement/localisation peut être affectée par l'activation ou non du Wi-Fi sur les appareils de vos utilisateurs. Les utilisateurs d'Android peuvent également choisir différents modes d'emplacement/localisation : les utilisateurs qui sont en mode "Économie de batterie" ou "Appareil uniquement" peuvent avoir des données inexactes.

### Emplacement/localisation des utilisateurs du SDK par adresse IP

À partir du 26 novembre 2024, Braze détectera les emplacements/localisations des utilisateurs à partir du pays géolocalisé en utilisant l'adresse IP du début de la première session SDK. 

Auparavant, Braze utilisait le code pays des paramètres régionaux de l'appareil lors de la création de l'utilisateur du SDK et pendant la durée de la première session. Ce n'est qu'après le traitement de la première session que l'adresse IP est utilisée pour définir un pays plus fiable pour l'utilisateur. Cela signifie que le pays de l'utilisateur n'a été défini avec une plus grande précision qu'à partir de la deuxième session, une fois que le début de la première session a été traité.

Désormais, Braze utilisera l'adresse IP pour définir la valeur du pays sur les profils utilisateurs créés via le SDK, et ce paramètre de pays basé sur l'IP sera disponible pendant et après la première session.

## Emplacements/ciblage

Grâce aux données d'emplacement/localisation et aux segments, vous pouvez implémenter des campagnes et des stratégies basées sur l'emplacement. Par exemple, vous pouvez vouloir mener une campagne promotionnelle pour les utilisateurs qui vivent dans une ligne/en production/instantanée ou exclure les utilisateurs d'une région dont la réglementation est plus stricte.

Reportez-vous à la section [Ciblage des emplacements]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/) pour plus d'informations sur la création d'un segment d'emplacement/localisation.

## Définition difficile de l'attribut emplacement/localisation par défaut

Vous pouvez également utiliser l'[endpoint`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de notre API pour mettre à jour l'attribut [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/) pour mettre à jour l'attribut standard. En voici un exemple :

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

## Questions fréquemment posées

### Quand Braze recueille-t-il des données d'emplacement/localisation ?

Braze ne collecte l'emplacement/localisation que lorsque l'application est ouverte au premier plan. Par conséquent, notre filtre `Most Recent Location` cible les utilisateurs en fonction de l'endroit où ils ont ouvert l'application pour la dernière fois (également appelé début de session).

Vous devez également tenir compte des nuances suivantes :

- Si l'emplacement/localisation est désactivé, le filtre `Most Recent Location` affichera le dernier emplacement/localisation enregistré.
- Si un utilisateur a déjà eu un emplacement/localisation stocké sur son profil, il sera concerné par le filtre `Location Available`, même s'il s'est désabonné de la géolocalisation depuis lors.

### Quelle est la différence entre les filtres "Locale de l'appareil le plus récent" et "Emplacement le plus récent" ?

Le site `Most Recent Device Locale` provient des paramètres de l'appareil de l'utilisateur. Par exemple, pour les utilisateurs d'iPhone, cela apparaît dans leur appareil sous **Réglages** > **Général** > **Langue & Région.** Ce filtre est utilisé pour capturer les formats linguistiques et régionaux, tels que les dates et les adresses, et est indépendant du filtre `Most Recent Location`.

Le site `Most Recent Location` est le dernier emplacement/localisation GPS connu de l'appareil. Elle est mise à jour au début de la session et est stockée dans le profil de l'utilisateur.

### Si un utilisateur s'abonne au suivi de l'emplacement/localisation, ses anciennes données d'emplacement seront-elles supprimées de Braze ?

Non. Si un emplacement/localisation a déjà été enregistré sur le profil d'un utilisateur, ces données ne seront pas automatiquement supprimées si l'utilisateur choisit par la suite de ne plus suivre l'emplacement/localisation.

