---
nav_title: Création de geofences
article_title: Création de geofences
page_order: 1
page_type: reference
description: "Cet article de référence présente les geofences et explique comment créer et configurer les événements de geofence."
tool: 
  - Position
search_rank: 1
---
# Geofences

> Le « geofence » est un concept qui fait partie intégrante des solutions de localisation en temps réel de Braze. Une geofence est une zone géographique virtuelle, représentée par des coordonnées latitudinales et longitudinales associées à un rayon, formant un cercle autour d’une position générale spécifique. Ces geofences peuvent varier, allant de la taille d’un bâtiment à celle d’une ville entière.

Vous pouvez définir des geofences sur le tableau de bord de Braze et les utiliser pour déclencher des campagnes en temps réel quand l’utilisateur rentre ou sort de leurs limites, ou envoyer des campagnes de suivi des heures ou des jours plus tard. Les utilisateurs qui entrent ou sortent de vos geofences apportent une nouvelle couche de données qui peut être utilisée pour segmenter et recibler.

## Aperçu

Gérez les geofences à partir de la page de **Positions**. Les geofences sont organisées en ensembles. Un ensemble est un groupe de geofences qui peut être utilisé pour segmenter ou contacter des utilisateurs sur toute la plateforme. Chaque ensemble de geofences peut contenir un maximum de 10 000 geofences.

Vous pouvez créer ou télécharger une quantité illimitée de geofences dans le tableau de bord, ce qui permet à votre équipe marketing de configurer des campagnes et des ensembles de geofences sans avoir à calculer le nombre de geofences. Braze synchronisera de façon dynamique les geofences qu’il suit pour chaque utilisateur, en veillant à ce que les geofences les plus pertinentes soient toujours disponibles.

- Les applications Android ne peuvent stocker localement que 100 geofences à la fois. Braze est configuré pour stocker jusqu’à 20 geofences par application en local.
- Les appareils iOS peuvent surveiller jusqu’à 20 geofences à la fois par application. Braze surveille jusqu’à 20 emplacements s’il y a suffisamment d’espace disponible. 
- Si l’utilisateur est éligible à la réception de plus de 20 geofences, Braze téléchargera le nombre maximal de positions selon leur proximité par rapport à l’utilisateur au moment du rafraîchissement du démarrage de session ou de notification push silencieuse
- Pour que les geofences fonctionnent correctement, vous devez vous assurer que votre application n’utilise pas tous les emplacements de geofence disponibles.

## Créer des ensembles de geofences

### Créer des ensembles manuellement

À partir de la page **Emplacements**, cliquez sur **+ Create Geofence Set (+ Créer un ensemble de geofences)**.

![Ensemble de geofences d’aéroports allemands avec un utilisateur qui dessine un rayon de deux mille mètres sur la carte de l’aéroport de Hambourg.][1]

Après avoir créé un ensemble de geofences, vous pouvez ajouter manuellement des geofences en les dessinant sur la carte. Nous recommandons de créer des geofences avec un rayon d’au moins 200 mètres pour qu’elles fonctionnent de manière optimale. Pour plus d’informations sur les options configurables, consultez l’article [Configuration des geofences]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/geofence_configuration/).

### Création d’ensembles via le téléchargement en masse {#creating-geofence-sets-via-bulk-upload}

Les geofences peuvent être téléchargées en bloc en tant qu’objet GeoJSON de type `FeatureCollection`. Chaque geofence est un `Point` géométrique dans le groupe de fonctionnalités. Les propriétés de chaque fonctionnalité nécessitent un `"radius"` et une clé `"name"` facultative pour chaque geofence. Pour télécharger votre objet GeoJSON, cliquez sur **+ Create Geofence Set (+ Créer un ensemble de geofences)**, puis sur **Upload GeoJSON (Télécharger l’objet GeoJSON)**.

L’échantillon suivant représente l’objet GeoJSON approprié pour désigner deux geofences : une pour le siège de Braze à New York, et l’autre pour la statue de la Liberté au sud de Manhattan. Nous recommandons de télécharger des geofences avec un rayon d’au moins 100 mètres pour qu’elles fonctionnent de manière optimale.

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
    }, ...
  ]
```

Gardez les points suivants à l’esprit au moment de créer vos geofences :

- La valeur des `coordinates` de l’objet GeoJSON est au format [longitude/latitude].
- Le rayon maximal d’une geofence pouvant être téléchargé est de 100 000 mètres (100 kilomètres ou environ 62 miles).

## Mettre à jour des ensembles de geofences

Pour les utilisateurs actifs, le SDK de Braze ne demandera de geofences qu’une fois par jour au démarrage de la session. Cela signifie que si des modifications sont apportées aux ensembles de geofences après le début de la session, vous devrez attendre 24 heures à compter de la première collecte des ensembles pour recevoir l’ensemble mis à jour.

Pour les utilisateurs inactifs, si les notifications push sont activées en arrière-plan, Braze enverra également une notification push silencieuse toutes les 24 heures pour extraire les derniers emplacements de l’appareil.

{% alert note %}
Si les geofences ne sont pas chargées localement sur l’appareil, l’utilisateur ne pourra pas déclencher la geofence même s’il pénètre dans la zone délimitée.
{% endalert %}

### Mettre à jour pour des utilisateurs individuels

Mettre à jour les geofences pour des utilisateurs individuels peut être utile à des fins de tests. Pour mettre à jour des ensembles de geofences, déplacez-vous vers le pas de la page **Positions** et cliquez sur **Resynchroniser les geofences**. Vous serez invité à saisir le `external_id` ou le `email` des utilisateurs que vous désirez mettre à jour

## Utiliser des événements de geofence

Une fois les geofences configurées, vous pouvez les utiliser pour améliorer et enrichir la façon dont vous communiquez avec vos utilisateurs.

### Déclencheurs

Pour utiliser les données de geofence avec des déclencheurs de campagne ou de Canvas, choisissez **Livraison par événement** comme méthode de livraison. Ensuite, ajoutez une action de déclenchement de type `Déclencher une geofence`. Pour finir, choisissez l’ensemble de geofences et les types d’événements de transition de geofence pour votre message. Vous pouvez également faire progresser les utilisateurs dans un Canvas à l’aide des événements de geofence.

![][2]

### Personnalisation

Pour personnaliser votre message à l’aide des données de geofence, vous pouvez utiliser la syntaxe de personnalisation Liquid suivante :

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Foire aux questions

Consultez nos [FAQ sur les geofences][3] pour obtenir des réponses aux questions fréquemment posées sur les geofences.


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
