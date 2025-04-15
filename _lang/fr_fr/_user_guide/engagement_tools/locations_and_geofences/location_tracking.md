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

- [iOS][2]
- [Android][3]
- [Web][4]

En général, les applications mobiles utilisent la puce GPS de l’appareil ainsi que d’autres systèmes (comme les scans Wi-Fi) pour suivre la localisation des utilisateurs. tandis que les applications Web utilisent le WPS (Wi-Fi Positioning System) pour suivre leur localisation. Toutes ces plateformes nécessitent que l’utilisateur s’abonne au suivi de la localisation. L’exactitude de vos données de suivi de localisation peut être affectée par le fait que vos utilisateurs aient activé ou non le Wi-Fi sur leur appareil. Les utilisateurs Android peuvent également choisir différents modes de localisation : les données des utilisateurs qui sont en mode « Économiseur de batterie » ou « Appareil uniquement » peuvent être inexactes.

### Emplacement des utilisateurs du SDK par adresse IP

À partir du 26 novembre 2024, Braze détectera les emplacements/localisations des utilisateurs à partir du pays géolocalisé en utilisant l'adresse IP du début de la première session SDK. 

Auparavant, Braze utilisait le code pays des paramètres régionaux de l'appareil lors de la création de l'utilisateur du SDK et pendant la durée de la première session. Ce n'est qu'après le traitement de la première session que l'adresse IP est utilisée pour définir un pays plus fiable pour l'utilisateur. Cela signifie que le pays de l'utilisateur n'a été défini avec une plus grande précision qu'à partir de la deuxième session, une fois que le début de la première session a été traité.

Désormais, Braze utilisera l'adresse IP pour définir la valeur du pays sur les profils utilisateurs créés via le SDK, et ce paramètre de pays basé sur l'IP sera disponible pendant et après la première session.

## Ciblage de localisation

En utilisant des segments et des données de suivi de la localisation, vous pouvez configurer des campagnes et des stratégies basées sur la localisation de vos utilisateurs. Par exemple, vous voudrez peut-être lancer une campagne promotionnelle pour les utilisateurs qui vivent dans une région donnée, ou exclure les utilisateurs situés dans une région dont les réglementations sont plus strictes.

Reportez-vous à [le ciblage par lieu][1] pour plus d'informations sur la création d'un segment de lieu.

## Réglage de l’attribut de localisation par défaut

Vous pouvez également utiliser l’[endpoint `users/track`][8] dans notre API pour mettre à jour l'attribut standard [`current_location`][9]. Voici un exemple :

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

- [Radar][6]
- [Infillion][10]
- [Foursquare][7]

## Foire aux questions

Consultez notre [FAQ sur les emplacements][11] pour obtenir des réponses aux questions fréquemment posées sur les emplacements.

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
[6]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[10]: {{site.baseurl}}/partners/message_personalization/location/infillion/
[11]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#locations
