---
nav_title: Suivi de la localisation
article_title: Suivi de la localisation
page_order: 0
page_type: Référence
description: "Cet article de référence explique comment utiliser le suivi de localisation et le ciblage de localisation dans vos applications."
tool: Localisation
---

# Suivi de localisation

La collection de localisation capture l'emplacement le plus récent de l'utilisateur lorsque l'application a été ouverte en utilisant les données de localisation GPS. Vous pouvez utiliser ces informations pour segmenter les données en fonction des utilisateurs qui se trouvaient dans un emplacement défini.

## Activation du suivi de localisation

Pour activer la collecte de localisation sur votre application, jetez un œil au guide de développement approprié pour la plateforme que vous utilisez:

- [iOS][2]
- [Android][3]
- [Web][4]

En général, les applications mobiles utiliseront la puce GPS de l'appareil et d'autres systèmes (comme l'analyse Wi-Fi) pour suivre la localisation d'un utilisateur. Les applications Web utiliseront le WPS (système de positionnement Wi-Fi) pour suivre la localisation d'un utilisateur.

Notez que la précision de vos données de localisation peut être affectée par le fait que vos utilisateurs aient ou non activé le Wi-Fi sur leur appareil. Les utilisateurs d'Android peuvent également choisir différents modes de localisation : les utilisateurs qui sont en mode "Économie de batterie" ou "Périphérique uniquement" peuvent avoir des données inexactes.

## Ciblage de l'emplacement

En utilisant les données de suivi de la localisation, vous pouvez configurer des campagnes et des stratégies basées sur la localisation. Par exemple, vous pouvez organiser une campagne promotionnelle pour les utilisateurs qui vivent dans une région particulière, ou exclure les utilisateurs dans une région où les réglementations sont plus strictes.

Consultez la section [Suivi de localisation][1] pour plus d'informations sur le ciblage de l'emplacement.

## Paramétrage difficile de l'attribut d'emplacement par défaut

Vous pouvez également utiliser le point de terminaison [`utilisateurs/piste`][8] de notre API pour mettre à jour l'attribut par défaut [`current_location`][9] </a> -- par exemple :
```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [ 
    {
      "external_id" : "XXX",
      "current_location" : {"longitude":-0. 18092, "latitude": 51.509865}
      }
   ]
}
```

## Partenaires technologiques

Vous pouvez également tirer parti du suivi de la localisation avec certains de nos partenaires, par exemple :

- [Neura][5]
- [Radar][6]
- [Foursquare][7]
- [Gimbal][10]

## Foire aux questions

Visitez notre page [FAQ sur les lieux][11] pour obtenir des réponses aux questions les plus fréquemment posées sur les lieux.

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/location_tracking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[4]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.trackLocation
[5]: {{site.baseurl}}/partners/data_augmentation/contextual_location/neura_actions/
[6]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[10]: {{site.baseurl}}/partners/data_augmentation/contextual_location/gimbal/
[11]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#locations