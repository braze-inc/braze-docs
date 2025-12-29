---
nav_title: Création de géorepérages
article_title: Création de géorepérages
page_order: 1
page_type: reference
toc_headers: h2
description: "Cet article de référence explique ce que sont les géorepérages et comment créer et configurer des événements de géorepérage."
tool: 
  - Location
search_rank: 9
---

# Géorepérages

> Le concept de géorepérage est au cœur de notre offre d'emplacement/localisation en temps réel. Un géorepérage est une zone géographique virtuelle, conseillée par la latitude et la longitude combinées à un rayon, formant un cercle autour d'une position globale spécifique. Les géorepérages peuvent varier de la taille d'un bâtiment à celle d'une ville entière.

## Comment cela fonctionne-t-il ?

Les géorepérages peuvent être utilisés pour déclencher des campagnes en temps réel lorsque les utilisateurs entrent et sortent de leurs frontières, ou envoyer des campagnes de suivi quelques heures ou quelques jours plus tard. Les utilisateurs qui entrent ou sortent de vos géorepérages ajoutent une nouvelle couche de données utilisateur que vous pouvez utiliser pour la segmentation et le reciblage.

Les géofences sont organisées en ensembles de géofences, c'est-à-dire un groupe de géofences qui peuvent être utilisées pour segmenter ou engager les utilisateurs sur l'ensemble de la plateforme. Chaque ensemble de géoréférences peut contenir un maximum de 10 000 géoréférences.

Vous pouvez créer ou télécharger un nombre illimité de géorepérages.

- Les applications Android ne peuvent stocker localement que 100 géorepérages à la fois. Braze est configuré pour ne stocker localement qu'un maximum de 20 géorepérages par application.
- Les appareils iOS peuvent surveiller jusqu'à 20 géorepérages à la fois par application. Braze surveillera jusqu'à 20 emplacements/localisations dans la limite des places disponibles. 
- Si l'utilisateur est éligible pour recevoir plus de 20 géorepérages, Braze téléchargera la quantité maximale d'emplacements en fonction de la proximité de l'utilisateur au moment du démarrage de la session.
- Pour que les géorepérages fonctionnent correctement, vous devez vous assurer que votre application n'utilise pas tous les emplacements de géorepérage disponibles.

Reportez-vous au tableau suivant pour connaître les termes courants de géorepérage et leur description.

| Durée | Description |
|---|---|
| Latitude et longitude | Le centre géographique du géorepérage. |
| Rayon | Le rayon du géorepérage en mètres, mesuré à partir du centre géographique. Nous vous recommandons de définir un rayon minimum de 100 à 150 mètres pour tous les géorepérages. |
| Refroidissement | Les utilisateurs reçoivent des notifications déclenchées par la géorepérage après avoir effectué des transitions d'entrée ou de sortie sur des géofences individuelles. Après une transition, il existe un délai prédéfini pendant lequel l'utilisateur ne peut plus effectuer la même transition sur ce géorepérage individuel. Ce temps, appelé "cooldown", est prédéfini par Braze et a pour principal objectif d'éviter les requêtes inutiles sur le réseau. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Créer manuellement des géorepérages

### Étape 1 : Créer un ensemble de géorepérages

Pour créer une géorepérage, vous devez d'abord créer un jeu de géorepérage.

1. Allez dans **Audience** > **Emplacements** dans le tableau de bord de Braze.
2. Sélectionnez **Créer un ensemble de géorepérages**.
3. Pour **Nom du jeu**, entrez un nom pour votre jeu de géorepérage.
4. (Facultatif) Ajoutez des tags pour filtrer votre jeu.

### Étape 2 : Ajouter les géorepérages

Ensuite, vous pouvez ajouter des géofences à votre ensemble de géorepérages.

1. Sélectionnez **Dessiner un géorepérage** pour cliquer sur le cercle et le faire glisser sur la carte. Répétez l'opération pour ajouter d'autres géorepérages à votre ensemble, si nécessaire.
2. (Facultatif) Vous pouvez sélectionner **Modifier** et remplacer la description du géorepérage par un nom.
3. Sélectionnez **Enregistrer le jeu de géorepérage** pour l'enregistrer.

{% alert tip %}
Nous vous recommandons de créer des géorepérages d'un rayon d'au moins 200 mètres pour une fonctionnalité optimale. Pour plus d'informations sur les options configurables, reportez-vous à la section [Intégrations mobiles.](#mobile-integrations)
{% endalert %}

Un ensemble de géoréseaux avec deux géoréseaux "EastCoastGreaterNY" et "WesternRegion" avec deux cercles sur la carte.]({% image_buster /assets/img/geofence_example.png %})

## Téléchargement en masse de géorepérages {#creating-geofence-sets-via-bulk-upload}

Les géorepérages peuvent être téléchargés en vrac sous la forme d'un objet GeoJSON de type `FeatureCollection`. Chaque géorepérage est un type de géométrie `Point` dans la collection de fonctionnalités. Les propriétés de chaque fonctionnalité requièrent une clé `radius` et une clé `name` facultative pour chaque géorepérage. 

Pour télécharger votre GeoJSON, sélectionnez **Plus** > **Télécharger GeoJSON**.

Lorsque vous créez vos géorepérages, tenez compte des détails suivants :

- La valeur `coordinates` dans le GeoJSON est formatée comme `[Longitude, Latitude]`.
- Le rayon maximum de géorepérage pouvant être téléchargé est de 10 000 mètres (environ 10 kilomètres ou 6,2 miles).

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

## Utilisation des événements de géorepérage

Une fois les géorepérages configurés, vous pouvez les utiliser pour améliorer et enrichir la façon dont vous communiquez avec vos utilisateurs.

### Campagnes de déclenchement et canevas

Pour utiliser les données de géorepérage dans le cadre des déclencheurs de campagne et de Canvas, choisissez la **livraison par événement** pour la méthode de **réception/distribution**. Ensuite, ajoutez une action de déclenchement de `Trigger a Geofence`. Enfin, choisissez les types d'événements de définition de géorepérage et de transition de géorepérage pour votre message. Vous pouvez également faire avancer les utilisateurs dans un canvas à l'aide d'événements de géorepérage.

Une campagne basée sur l'action avec un géorepérage qui se déclenchera lorsqu'un utilisateur entrera dans les aéroports allemands.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personnalisation des messages

Pour utiliser les données de géorepérage afin de personnaliser un message, vous pouvez utiliser la syntaxe de personnalisation liquide suivante :

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Mise à jour des jeux de géorepérage

Pour les utilisateurs actifs, le SDK de Braze ne demandera des géorepérages qu'une fois par jour au démarrage de la session. Cela signifie que si des modifications sont apportées aux ensembles de géorepérages après le début de la session, vous devrez attendre 24 heures à partir du moment où les ensembles sont retirés pour la première fois pour recevoir l'ensemble mis à jour.

{% alert note %}
Si les géorepérages ne sont pas chargés localement sur l'appareil, l'utilisateur ne peut pas déclencher le géorepérage même s'il entre dans la zone.
{% endalert %}

## Intégrations mobiles {#mobile-integrations}

### Exigences multiplateformes

Les campagnes déclenchées par géorepérage sont disponibles sur iOS et Android. Pour prendre en charge les géorepérages, les éléments suivants doivent être en place :

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.
2. Les géorepérages de Braze ou la collecte d'emplacements doivent être activés.
3. Pour les appareils sous iOS version 11 et supérieure, l'utilisateur doit toujours autoriser l'accès à l'emplacement/localisation pour que le géorepérage fonctionne.

{% alert important %}
À partir de la version 3.6.0 du SDK de Braze, la collecte des emplacements/localisations est désactivée par défaut. Pour vérifier qu'elle est activée sur Android, confirmez que `com_braze_enable_location_collection` est défini sur `true` dans votre `braze.xml`.
{% endalert %}

Reportez-vous à la documentation [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence) ou [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5) pour plus d'informations en fonction de votre plateforme.

{% alert tip %}
Vous pouvez également exploiter les géorepérages avec nos partenaires technologiques, tels que [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) et [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)
{% endalert %}

## Questions fréquemment posées

### Quelle est la différence entre les géorepérages et l'emplacement/localisation ?

Dans Braze, un géorepérage est un concept différent de l'emplacement/localisation. Les géorepérages sont utilisés comme déclencheurs de certains actionnements. Un géorepérage est une frontière virtuelle établie autour d'un emplacement/localisation. Lorsqu'un utilisateur entre ou sort de cette frontière, il peut déclencher une action spécifique, comme l'envoi d'un message.

La géolocalisation est utilisée pour collecter et stocker les données d'emplacement/localisation les plus récentes d'un utilisateur. Ces données peuvent être utilisées pour segmenter les utilisateurs en fonction du filtre `Most Recent Location`. Par exemple, vous pouvez utiliser le filtre `Most Recent Location` pour cibler une région spécifique de votre audience, par exemple en envoyant un message aux utilisateurs situés à New York.

### Quelle est la précision des géorepérages de Braze ?

Les géorepérages de Braze utilisent une combinaison de tous les fournisseurs d'emplacement/localisation disponibles pour un appareil afin de trianguler l'emplacement de l'utilisateur. Il s'agit notamment des tours Wi-Fi, GPS et cellulaires.

La précision typique se situe entre 20 et 50 mètres, et la précision optimale se situe entre 5 et 10 mètres. Dans les zones rurales, la précision peut se dégrader de manière significative, jusqu'à plusieurs kilomètres. Braze recommande de créer des géorepérages de plus grand rayon dans les emplacements/localisations ruraux.

Pour plus d'informations sur la précision des géorepérages, reportez-vous à la documentation [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) et [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1).

### Comment les géorepérages affectent-ils l'autonomie de la batterie ?

Notre solution de géorepérage utilise le service natif du système de géorepérage sur iOS et Android et est réglée pour arbitrer intelligemment entre précision et puissance, en enregistrant des économies de batterie et en améliorant les performances au fur et à mesure que le service sous-jacent s'améliore.

### Quand les géorepérages sont-ils actifs ?

Les géorepérages de Braze fonctionnent à toute heure de la journée, même lorsque votre appli est fermée. Ils deviennent actifs dès qu'ils sont définis et téléchargés dans le tableau de bord de Braze. Cependant, les géorepérages ne peuvent pas fonctionner si l'utilisateur a désactivé l'emplacement/localisation.

Pour que les géorepérages fonctionnent, les utilisateurs doivent avoir activé les services d'emplacement/localisation sur leur appareil et avoir autorisé votre appli à accéder à leur emplacement. Si un utilisateur a désactivé l'emplacement/localisation, votre appli ne pourra pas détecter quand il entre ou sort d'un géorepérage.

### Les données de géorepérage sont-elles stockées dans les profils utilisateurs ?

Non, Braze ne stocke pas de données de géorepérage sur les profils utilisateurs. Les géorepérages sont surveillés par les services d'emplacement/localisation d'Apple et de Google, et Braze n'est averti que lorsqu'un utilisateur déclenche un géorepérage. À ce stade, nous traitons toutes les campagnes de déclenchement associées.

### Puis-je mettre en place un géorepérage à l'intérieur d'un géorepérage ?

À titre de bonne pratique, évitez de configurer des géorepérages qui se chevauchent les uns les autres, car cela peut poser des problèmes de déclenchement des notifications.

