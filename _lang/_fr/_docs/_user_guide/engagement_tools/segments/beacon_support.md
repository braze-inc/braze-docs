---
nav_title: Support Beacon et Geofence
article_title: Support Beacon et Geofence
page_order: 7
page_type: Référence
tool:
  - Segments
  - Localisation
description: "Cet article décrit brièvement le support de Beacon et de Geofence et comment utiliser votre compte partenaire de localisation pour commencer le suivi de la localisation."
---

# Prise en charge des balises et de la géorepérage

> Cet article décrit brièvement le support de Beacon et de Geofence et comment utiliser votre compte partenaire de localisation pour commencer le suivi de la localisation.

La combinaison du support de balises ou de géorepérages existants avec les fonctionnalités de ciblage et de messagerie de Braze vous permet d'en apprendre davantage sur les actions physiques de votre utilisateur et de lui envoyer un message en conséquence.

## Support du radar

Radar est entièrement compatible avec les géofences personnalisées illimitées, les géofences POI pré-construites, la détection des balises, la détection des régions, le suivi des trajets et bien plus encore. Lorsque vous activez l'intégration du Radar et de Braze, Radar transfère les événements de localisation en temps réel et les attributs de l'utilisateur qui peuvent être utilisés pour déclencher des campagnes en temps réel, optimisez les opérations de ramassage et de livraison des derniers milles, optimisez le suivi des flottes et la logistique d'expédition, ou construisez des segments des utilisateurs en fonction des modèles d'emplacement. De plus, les API de Radar Geo peuvent être utilisées pour enrichir ou personnaliser vos campagnes de marketing grâce au Contenu connecté. Visitez notre [page des intégrations de Radar](https://www.braze.com/docs/partners/message_personalization/location/radar/#radar) pour en savoir plus.

## Prise en charge des places de la nacelle

La connexion de votre compte Gimbal à Braze vous permet de suivre lorsque vos utilisateurs entrent ou quittent vos lieux définis et déclenchent des événements à partir de ces entrées et de ces sorties. De plus, vous pouvez suivre des informations supplémentaires comme le nom du lieu ou la visite de Dwell en tant que propriété événementielle afin que vous puissiez personnaliser encore plus votre messagerie. Veuillez référencer la documentation de Gimbal avec nos instructions pour l'intégration à [iOS][1] et à [Android][2].

{% alert note %}
Notez que cela fonctionnera de la même façon pour les balises de Gimbal, ainsi que pour leurs solutions de géorepérage.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#beacon-integration
