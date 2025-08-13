---
nav_title: Création de géorepérages
article_title: Création de géorepérages
page_order: 1
page_type: reference
toc_headers: h2
description: "Cet article de référence présente les géorepérages et explique comment créer et configurer les événements de géorepérage."
tool: 
  - Location
search_rank: 9
---

# Géorepérages

> Le « géorepérage » est un concept qui fait partie intégrante de nos solutions de localisation en temps réel. Une géorepérage est une zone géographique virtuelle, représentée par des coordonnées latitudinales et longitudinales associées à un rayon, formant un cercle autour d’une position générale spécifique. Ces géorepérages peuvent varier, allant de la taille d’un bâtiment à celle d’une ville entière.

## Fonctionnement

Les géorepérages peuvent être utilisés pour déclencher des campagnes en temps réel lorsque les utilisateurs entrent et sortent de leurs frontières, ou envoyer des campagnes de suivi quelques heures ou quelques jours plus tard. Les utilisateurs qui entrent ou sortent de vos géorepérages apportent une nouvelle couche de données qui peut être utilisée pour segmenter et recibler.

Les géorepérages sont organisées en ensembles. Un ensemble est un groupe de géorepérages qui peut être utilisé pour segmenter ou contacter des utilisateurs sur toute la plateforme. Chaque ensemble de géorepérages peut contenir un maximum de 10 000 géorepérages.

Vous pouvez créer ou télécharger un nombre illimité de géorepérages.

- Les applications Android ne peuvent stocker localement que 100 géorepérages à la fois. Braze est configuré pour stocker jusqu’à 20 géorepérages par application en local.
- Les appareils iOS peuvent surveiller jusqu’à 20 géorepérages à la fois par application. Braze surveille jusqu’à 20 emplacements s’il y a suffisamment d’espace disponible. 
- Si l'utilisateur est éligible pour recevoir plus de 20 géorepérages, Braze téléchargera la quantité maximale d'emplacements en fonction de la proximité de l'utilisateur au moment du démarrage de la session.
- Pour que les géorepérages fonctionnent correctement, vous devez vous assurer que votre application n’utilise pas tous les emplacements de géorepérage disponibles.

Reportez-vous au tableau suivant pour connaître les termes courants de géorepérage et leur description.

| Terme | Description |
|---|---|
| Latitude et longitude | Le centre géographique de la géorepérage. |
| Rayon | Le rayon de la géorepérage exprimé en mètres et mesuré par son centre géographique. Nous vous recommandons de définir un rayon minimum de 100 à 150 mètres pour tous les géorepérages. |
| Temps de récupération | Les utilisateurs reçoivent des notifications déclenchées par la géorepérage après avoir effectué des transitions d'entrée ou de sortie sur des géofences individuelles. Après une transition, il existe un délai prédéfini pendant lequel l'utilisateur ne peut plus effectuer la même transition sur ce géorepérage individuel. Ce temps, appelé "cooldown", est prédéfini par Braze et a pour principal objectif d'éviter les requêtes inutiles sur le réseau. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Créer manuellement des géorepérages

### Étape 1 : Créer un ensemble de géorepérages

Pour créer une géorepérage, vous devez d'abord créer un jeu de géorepérage.

1. Allez dans **Audience** > **Emplacements** dans le tableau de bord de Braze.
2. Sélectionnez **Créer un ensemble de géorepérages**.
3. Pour **Nom du jeu**, entrez un nom pour votre jeu de géorepérage.
4. (Facultatif) Ajoutez des tags pour filtrer votre jeu.

### Étape 2 : Ajouter les géorepérages

Ensuite, vous pouvez ajouter des géofences à votre ensemble de géorepérages.

1. Sélectionnez **Dessiner un géorepérage** pour cliquer sur le cercle et le faire glisser sur la carte. Répétez l'opération pour ajouter d'autres géorepérages à votre ensemble, si nécessaire.
2. (Facultatif) Vous pouvez sélectionner **Modifier** et remplacer la description du géorepérage par un nom.
3. Sélectionnez **Enregistrer le jeu de géorepérage** pour l'enregistrer.

{% alert tip %}
Nous recommandons de créer des géorepérages avec un rayon d’au moins 200 mètres pour qu’elles fonctionnent de manière optimale. Pour plus d'informations sur les options configurables, reportez-vous à la section [Intégrations mobiles.](#mobile-integrations)
{% endalert %}

![Un jeu de géorepérage avec deux géorepérages "EastCoastGreaterNY" et "WesternRegion" avec deux cercles sur la carte.]({% image_buster /assets/img/geofence_example.png %})

## Téléchargement en masse de géorepérages {#creating-geofence-sets-via-bulk-upload}

Les géorepérages peuvent être téléchargées en bloc en tant qu’objet GeoJSON de type `FeatureCollection`. Chaque géorepérage est un type de géométrie `Point` dans la collection de fonctionnalités. Les propriétés de chaque fonctionnalité nécessitent un `radius` et une clé `name` facultative pour chaque géorepérage. 

Pour télécharger votre GeoJSON, sélectionnez **Plus** > **Télécharger GeoJSON**.

Lorsque vous créez vos géorepérages, tenez compte des détails suivants :

- La valeur `coordinates` dans le GeoJSON est formatée comme `[Longitude, Latitude]`.
- Le rayon maximum de géorepérage pouvant être téléchargé est de 10 000 mètres (environ 100 kilomètres ou 62 miles).

### Exemple

L'exemple suivant conseille un GeoJSON correct pour spécifier deux géorepérages : l'un pour le siège de Braze à New York et l'autre pour la Statue de la Liberté au sud de Manhattan.

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.992473, 40.755669]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

## Utiliser des événements de géorepérage

Une fois les géorepérages configurés, vous pouvez les utiliser pour améliorer et enrichir la façon dont vous communiquez avec vos utilisateurs.

### Campagnes de déclenchement et canevas

Pour utiliser les données de géorepérage dans le cadre des déclencheurs de campagne et de Canvas, choisissez la **livraison par événement** pour la méthode de livraison. Ensuite, ajoutez une action de déclenchement `Trigger a Geofence`. Pour finir, choisissez l’ensemble de géorepérages et les types d’événements de transition de géorepérage pour votre message. Vous pouvez également faire progresser les utilisateurs dans un Canvas à l’aide des événements de géorepérage.

![Une campagne basée sur l'action avec un géorepérage qui se déclenche lorsqu'un utilisateur entre dans un aéroport allemand.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personnalisation des messages

Pour personnaliser votre message à l’aide des données de géorepérage, vous pouvez utiliser la syntaxe de personnalisation Liquid suivante :

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Mettre à jour des ensembles de géorepérages

Pour les utilisateurs actifs, le SDK de Braze ne demandera de géorepérages qu’une fois par jour au démarrage de la session. Cela signifie que si des modifications sont apportées aux ensembles de géorepérages après le début de la session, vous devrez attendre 24 heures à compter de la première collecte des ensembles pour recevoir l’ensemble mis à jour.

{% alert note %}
Si les géorepérages ne sont pas chargées localement sur l’appareil, l’utilisateur ne pourra pas déclencher la géorepérage même s’il pénètre dans la zone délimitée.
{% endalert %}

## Intégrations mobiles {#mobile-integrations}

### Exigences interplateformes

Des campagnes déclenchées par géorepérage sont disponibles sur iOS et Android. Pour prendre en charge les géorepérages, assurez-vous de respecter les points ci-dessous :

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.
2. Les géorepérages de Braze ou la collecte des données de localisation doivent être activés.
3. Pour les appareils iOS version 11 et ultérieure, les utilisateurs doivent toujours permettre l’accès aux données de localisation pour que les géorepérages fonctionnent.

{% alert important %}
À partir de la version 3.6.0 du SDK de Braze, la collecte des emplacements/localisations est désactivée par défaut. Pour vérifier qu'il est activé sur Android, confirmez que `com_braze_enable_location_collection` est défini sur `true` dans votre `braze.xml`.
{% endalert %}

Reportez-vous à la documentation [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence) ou [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5) pour plus d'informations en fonction de votre plateforme.

{% alert tip %}
Vous pouvez également exploiter les géorepérages avec nos partenaires technologiques, tels que [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) et [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)
{% endalert %}

## Foire aux questions

### Quelle est la différence entre les géorepérages et le suivi de la localisation ?

Dans Braze, un géorepérage est un concept différent du suivi de la localisation. Les géorepérages sont utilisés comme déclencheurs de certaines actions. Un géorepérage est une frontière virtuelle établie autour d'un emplacement géographique. Lorsqu'un utilisateur entre ou sort de cette frontière, il peut déclencher une action spécifique, comme l'envoi d'un message.

La géolocalisation est utilisée pour collecter et stocker les données d'emplacement/localisation les plus récentes d'un utilisateur. Ces données peuvent être utilisées pour segmenter les utilisateurs en fonction du filtre `Most Recent Location`. Par exemple, vous pouvez utiliser le filtre `Most Recent Location` pour cibler une région spécifique de votre audience, par exemple en envoyant un message aux utilisateurs situés à New York.

### Quel est le niveau de précision des géorepérages de Braze ?

Les géorepérages de Braze utilisent une combinaison de tous les outils de géolocalisation disponibles sur un appareil pour trianguler l’emplacement de l’utilisateur. Ces outils incluent, entre autres, le WI-FI, le GPS et les antennes-relais.

La précision type est de 20 à 50 m et le plus haut degré de précision est compris entre 5 et 10 m. Dans les zones rurales, la précision peut se dégrader considérablement, potentiellement sur plusieurs kilomètres. Braze recommande de créer des géorepérages avec des rayons plus importants pour les zones rurales.

Pour plus d'informations sur la précision des géorepérages, reportez-vous à la documentation [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) et [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1).

### Comment les géorepérages affectent-elles la durée de vie de la batterie ?

Notre solution de géorepérage utilise le service natif du système de géorepérage sur iOS et Android et est réglée pour arbitrer intelligemment entre précision et puissance, en enregistrant des économies de batterie et en améliorant les performances au fur et à mesure que le service sous-jacent s'améliore.

### Quand les géorepérages sont-elles actives ?

Les géorepérages de Braze fonctionnent à toute heure de la journée, même lorsque votre application est fermée. Ils deviennent actifs dès qu'ils sont définis et téléchargés dans le tableau de bord de Braze. Cependant, les géorepérages ne peuvent pas fonctionner si l'utilisateur a désactivé le suivi de la localisation.

Pour que les géorepérages fonctionnent, les utilisateurs doivent avoir activé les services d'emplacement/localisation sur leur appareil et avoir autorisé votre appli à accéder à leur emplacement. Si un utilisateur a désactivé le suivi de la localisation, votre appli ne pourra pas détecter quand il entre ou sort d'un géorepérage.

### Les données de géorepérage sont-elles stockées dans les profils utilisateurs ?

Non, Braze ne stocke pas de données de géorepérage dans les profils utilisateurs. Les géorepérages font l’objet d’une surveillance par les services de localisation d'Apple et de Google, et Braze n'est averti que lorsqu'un utilisateur déclenche un géorepérage. À ce stade, nous traitons toutes les campagnes de déclenchement associées.

### Puis-je définir un géorepérage au sein d’un géorepérage ?

En tant que bonne pratique, évitez d’utiliser des géorepérages imbriquées, car cela pourrait entraîner des problèmes de déclenchement des notifications.

