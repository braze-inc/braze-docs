---
nav_title: Prise en charge des balises et geofences
article_title: Prise en charge des balises et geofences
page_order: 7
page_type: reference
tool: 
  - Segments
  - Position
description: "Cet article aborde brièvement la prise en charge des balises et geofences et explique comment utiliser votre compte de partenaire de localisation pour commencer à suivre la localisation de vos utilisateurs."

---

# Prise en charge des balises et geofences

> Cet article aborde brièvement la prise en charge des balises et geofences et explique comment utiliser votre compte de partenaire de localisation pour commencer à suivre la localisation de vos utilisateurs.

Combinez votre prise en charge de balises ou de geofences avec les fonctions de ciblage et de messagerie de Braze pour en savoir plus sur les actions physiques de vos utilisateurs et leur envoyer des messages en conséquence.

## Prise en charge de Radar

Radar offre une prise en charge complète d’un nombre illimité de geofences personnalisées, des geofences POI pré-intégrées, de la détection des balises, de la détection de la région, du suivi des trajets, etc. Lorsque vous activez l’intégration entre Radar et Braze, Radar transmet des événements en temps réel et des attributs utilisateur qui peuvent être utilisés pour déclencher des campagnes en temps réel, soutenir les opérations de collecte et de livraison du dernier kilomètre, optimiser le suivi de flotte et la logistique des services d’expédition, ou créer des segments d’utilisateur en fonction des modèles de localisation. De plus, les API de Radar Geo peuvent être exploitées pour enrichir ou personnaliser vos campagnes marketing via le Contenu connecté. Consultez l’article [Intégrations Radar]({{site.baseurl}}/partners/message_personalization/location/radar/#radar) pour en savoir plus.

## Prise en charge de Gimbal

Connecter votre compte Gimbal à Braze vous permet de suivre le moment auquel vos utilisateurs entrent ou sortent de vos zones définies et de déclencher des événements suite à ces entrées et sorties. De plus, vous pouvez suivre des informations supplémentaires, comme le nom du lieu où se trouvent vos utilisateurs ou encore leur adresse résidentielle comme propriété d’événement, afin de personnaliser encore davantage votre message. Consultez la documentation de Gimbal ainsi que nos instructions concernant les intégrations [iOS][1] et [Android][2]. 

{% alert note %}
Notez que cela fonctionnera de la même manière pour les balises de Gimbal ainsi que pour leurs solutions de geofence.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#beacon-integration
