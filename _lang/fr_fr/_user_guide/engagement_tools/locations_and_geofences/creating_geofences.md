---
nav_title: Créer du géorepérage
article_title: Créer du géorepérage
page_order: 1
page_type: reference
toc_headers: h2
description: "Découvrez comment configurer les autorisations de localisation, créer un message d'amorçage pour les autorisations de localisation et créer des géorepérages pour des campagnes basées sur la localisation."
tool: 
  - Location
search_rank: 9
---

# Géorepérages

> Un géorepérage est une zone géographique virtuelle, représentée par des coordonnées de latitude et de longitude associées à un rayon, formant un cercle autour d'une position géographique spécifique. Les géorepérages peuvent varier, allant de la taille d'un bâtiment à celle d'une ville entière. Vous pouvez utiliser les géorepérages pour déclencher des campagnes en temps réel lorsque les utilisateurs entrent ou sortent de leurs frontières, ou envoyer des campagnes de suivi quelques heures ou quelques jours plus tard.

{% alert tip %}
Pour un guide pas à pas, consultez le cours d'apprentissage Braze [Créer un géorepérage](https://learning.braze.com/create-a-geofence).
{% endalert %}

## Fonctionnement

Les géorepérages sont organisés en ensembles de géorepérages — un groupe de géorepérages que vous pouvez utiliser pour segmenter ou contacter des utilisateurs sur toute la plateforme. Chaque ensemble de géorepérages peut contenir un maximum de 10 000 géorepérages. Vous pouvez créer ou télécharger un nombre illimité de géorepérages.

Les utilisateurs qui entrent ou sortent de vos géorepérages apportent une nouvelle couche de données utilisateur que vous pouvez exploiter pour la segmentation et le reciblage.

Gardez à l'esprit les limites suivantes par appareil :

- Les applications Android ne peuvent stocker localement que 100 géorepérages à la fois. Braze est configuré pour n'en stocker que 20 par application en local.
- Les appareils iOS peuvent surveiller jusqu'à 20 géorepérages à la fois par application. Braze surveille jusqu'à 20 emplacements s'il y a suffisamment d'espace disponible.
- Si l'utilisateur est éligible pour plus de 20 géorepérages, Braze télécharge le nombre maximal d'emplacements en fonction de la proximité de l'utilisateur au moment du démarrage de la session.
- Pour que les géorepérages fonctionnent correctement, assurez-vous que votre application n'utilise pas tous les emplacements de géorepérage disponibles.

Le tableau suivant décrit les termes courants liés au géorepérage :

| Terme | Description |
|---|---|
| Latitude et longitude | Le centre géographique du géorepérage. |
| Rayon | Le rayon du géorepérage exprimé en mètres, mesuré à partir du centre géographique. Définissez un rayon minimum de 100 à 150 mètres pour tous les géorepérages. |
| Temps de récupération | Les utilisateurs reçoivent des notifications déclenchées par le géorepérage après avoir effectué des transitions d'entrée ou de sortie sur des géorepérages individuels. Après une transition, il existe un délai prédéfini pendant lequel l'utilisateur ne peut plus effectuer la même transition sur ce géorepérage. Ce « temps de récupération » est prédéfini par Braze et a pour principal objectif d'éviter les requêtes réseau inutiles. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conditions préalables

### Exigences SDK et plateforme

Les campagnes déclenchées par géorepérage sont disponibles sur iOS et Android. Pour prendre en charge les géorepérages, les éléments suivants sont requis :

* Votre intégration doit prendre en charge les notifications push en arrière-plan.
* Les géorepérages de Braze ou la collecte des données de localisation doivent être activés.
* L'utilisateur doit accorder l'accès « Toujours autoriser » à la localisation.

{% alert important %}
La collecte des données de localisation de Braze est désactivée par défaut. Pour vérifier qu'elle est activée sur Android, confirmez que `com_braze_enable_location_collection` est défini sur `true` dans votre `braze.xml`.
{% endalert %}

Pour les instructions de configuration spécifiques à chaque plateforme, consultez [Géorepérages]({{site.baseurl}}/developer_guide/geofences/) dans le guide du développeur.

### Autorisations de localisation

Avant que vos géorepérages puissent fonctionner, les utilisateurs doivent accorder à votre application l'autorisation d'accéder à leur localisation. Comprendre les différents niveaux d'autorisation et leur impact sur le géorepérage est essentiel pour élaborer une stratégie efficace basée sur la localisation.

## Comprendre les autorisations de localisation

iOS et Android proposent tous deux plusieurs niveaux d'accès à la localisation. Le niveau d'autorisation accordé par un utilisateur détermine directement si le géorepérage fonctionne et la précision des données de localisation.

### Niveaux d'autorisation

{% tabs local %}
{% tab iOS %}

| Autorisation | Description | Prise en charge du géorepérage |
|---|---|---|
| **Autoriser une fois** | Accorde l'accès à la localisation pour une seule session. L'invite réapparaît la prochaine fois que l'utilisateur ouvre l'application. | Non. Le suivi en arrière-plan est désactivé, l'appareil ne reçoit donc les mises à jour de localisation que lorsque l'application est ouverte. |
| **Autoriser pendant l'utilisation de l'app** | Accorde l'accès à la localisation lorsque l'application est au premier plan. Après cette autorisation, iOS peut présenter une invite de suivi demandant à l'utilisateur de passer à « Toujours autoriser ». | Oui. iOS active la surveillance de la localisation en arrière-plan, y compris les transitions de géorepérage, pour les applications disposant de cette autorisation. |
| **Toujours autoriser** | Accorde un accès continu à la localisation, y compris en arrière-plan et lorsque l'application est fermée. | Oui. Cela offre la surveillance de géorepérage la plus fiable. |
| **Ne pas autoriser** | Refuse tout accès à la localisation. | Non. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Android %}

| Autorisation | Description | Prise en charge du géorepérage |
|---|---|---|
| **Pendant l'utilisation de l'app** | Accorde l'accès à la localisation lorsque l'application est au premier plan. | Non. Sur Android, l'accès à la localisation en arrière-plan est requis pour la surveillance du géorepérage. |
| **Toujours autoriser** | Accorde un accès continu à la localisation, y compris en arrière-plan. Sur Android 10 et versions ultérieures, cela nécessite une invite séparée après l'autorisation initiale « Pendant l'utilisation de l'app ». | Oui. Cela est requis pour le géorepérage sur Android. |
| **Ne pas autoriser** | Refuse tout accès à la localisation. Sur Android 13 et versions ultérieures, si un utilisateur refuse l'invite de localisation deux fois, le système d'exploitation bloque les invites ultérieures dans l'application. | Non. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### Localisation précise ou approximative

Sur iOS 14+ et Android 12+, les utilisateurs peuvent choisir entre la localisation précise et approximative.

| Paramètre | Précision | Impact sur le géorepérage |
|---|---|---|
| **Localisation précise (activée)** | Précision de l'ordre de 5 à 50 mètres, utilisant le GPS, le Wi-Fi et la triangulation cellulaire. | Les géorepérages fonctionnent comme prévu. Recommandé pour tous les cas d'utilisation basés sur le géorepérage. |
| **Localisation approximative (désactivée)** | Précision d'environ 3 kilomètres carrés (environ 1 mile carré). L'appareil renvoie une zone générale plutôt que des coordonnées exactes. | Les géorepérages ne se déclenchent pas de manière fiable. L'appareil ne peut pas déterminer avec précision si un utilisateur se trouve à l'intérieur ou à l'extérieur d'une frontière de géorepérage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Pour que le géorepérage fonctionne de manière fiable, les utilisateurs doivent activer la localisation précise. Incluez cette recommandation dans votre message d'amorçage des autorisations de localisation afin que les utilisateurs comprennent pourquoi la localisation précise est importante.
{% endalert %}

## Configurer un message d'amorçage pour les autorisations de localisation

Un message d'amorçage pour les autorisations de localisation est un message in-app qui explique la valeur du partage des données de localisation avant que l'utilisateur ne voie l'invite native du système d'exploitation. Comme l'invite native de localisation ne peut être affichée qu'une seule fois (sur iOS) ou un nombre limité de fois (sur Android), préparer les utilisateurs en amont augmente les taux d'abonnement.

### Étape 1 : Collaborer avec votre équipe de développement

Comme les messages in-app de Braze n'incluent pas de bouton d'action intégré pour invoquer l'invite native d'autorisation de localisation, votre équipe de développement doit gérer les autorisations de localisation côté appareil. Avant de créer le message in-app dans Braze, coordonnez-vous avec votre équipe de développement pour configurer des liens profonds que votre message in-app pourra appeler. L'implémentation spécifique dépend de l'architecture de votre application, mais les approches courantes incluent :

- Un lien profond qui déclenche l'invite native d'autorisation de localisation depuis votre application.
- Un lien profond qui ouvre la page des paramètres de localisation de l'application dans les paramètres du système d'exploitation de l'appareil, ce qui est utile pour relancer les utilisateurs qui ont précédemment refusé ou limité leurs autorisations.

Pour plus d'informations sur les liens profonds, consultez [Création de liens profonds vers du contenu in-app]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/). Pour des conseils spécifiques à chaque plateforme sur l'intégration de la localisation et du géorepérage, consultez [Géorepérages]({{site.baseurl}}/developer_guide/geofences/) dans le guide du développeur.

### Étape 2 : Créer le message in-app d'amorçage de localisation

Créez une campagne de message in-app qui explique la valeur de l'accès à la localisation. Tous les types de messages in-app prennent en charge cet abonnement, y compris le glisser-déposer.

1. Allez dans **Messagerie** > **Campagnes**, puis sélectionnez **Créer une campagne** > **Message in-app**.
2. Choisissez un type de message et une disposition. Une disposition **Modale** ou **Plein écran** vous donne plus d'espace pour expliquer les avantages.
3. Rédigez un message qui explique clairement pourquoi l'accès à la localisation profite à l'utilisateur. Par exemple :
    - « Activez la localisation pour être informé des offres à proximité. »
    - « Activez la localisation pour que nous puissions vous prévenir lorsque votre commande est prête à être retirée dans votre magasin le plus proche. »
4. Ajoutez un bouton d'appel à l'action principal (comme **Activer la localisation**) et définissez son comportement au clic sur **Lien profond vers l'app**, en utilisant le lien profond créé par votre équipe de développement pour déclencher l'invite native de localisation.
5. Ajoutez un bouton secondaire (comme **Pas maintenant**) qui ferme le message.

### Étape 3 : Cibler la bonne audience

Pour de meilleurs résultats, affichez le message d'amorçage de localisation lorsque les utilisateurs sont engagés et susceptibles de voir la valeur du partage de leur localisation.

- **Ciblez les utilisateurs qui n'ont pas encore accordé l'accès à la localisation.** Collaborez avec votre équipe de développement pour déterminer la meilleure façon de suivre et segmenter les utilisateurs en fonction de leur statut d'autorisation de localisation.
- **Programmez le message d'amorçage après une action à forte valeur,** comme la finalisation d'un achat, l'enregistrement d'un magasin en favori ou la consultation d'événements à proximité. Les utilisateurs sont plus susceptibles d'accepter lorsqu'ils comprennent l'avantage.
- **Évitez d'afficher le message d'amorçage au premier lancement.** Attendez que les utilisateurs aient suffisamment apprécié la valeur de l'application pour souhaiter une expérience plus personnalisée.

### Étape 4 : Encourager le niveau d'autorisation recommandé

Votre message d'amorçage doit encourager les utilisateurs à accorder le niveau d'autorisation qui active le géorepérage :

- **Sur iOS,** encouragez les utilisateurs à sélectionner **Autoriser pendant l'utilisation de l'app** au minimum. iOS pourra ensuite inviter l'utilisateur à passer à **Toujours autoriser** de lui-même. Vous pouvez également envoyer une campagne de suivi pour expliquer pourquoi « Toujours autoriser » offre la meilleure expérience.
- **Sur Android,** encouragez les utilisateurs à accorder **Toujours autoriser**. Sur Android 10 et versions ultérieures, l'utilisateur doit d'abord accorder « Pendant l'utilisation de l'app », puis accorder « Toujours autoriser » dans une invite de suivi séparée. Guidez-les à travers les deux étapes.

Dans les deux cas, rappelez aux utilisateurs de garder la **Localisation précise** activée pour la meilleure expérience.

## Rediriger les utilisateurs vers les paramètres du système d'exploitation

Si un utilisateur a précédemment refusé l'accès à la localisation ou sélectionné une autorisation limitée, vous ne pouvez pas déclencher à nouveau l'invite native depuis l'application sur la plupart des versions du système d'exploitation. Dirigez-les plutôt vers la mise à jour de leurs autorisations dans les paramètres de l'appareil.

Utilisez un lien profond dans un [message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) personnalisé pour diriger l'utilisateur vers la page des paramètres de localisation de l'application dans le système d'exploitation. Votre équipe de développement peut configurer un lien profond à cet effet dans le cadre de la gestion des autorisations de localisation de votre application (voir [Étape 1](#step-1-work-with-your-development-team)).

Lors de la création de ce message in-app, tenez compte des éléments suivants :

- **Quand l'afficher :** Ciblez les utilisateurs qui ont l'autorisation « Pendant l'utilisation de l'app » lorsque vous avez besoin de « Toujours autoriser », ou les utilisateurs qui ont précédemment refusé l'accès à la localisation.
- **Exemple de message :** « Pour profiter pleinement des fonctionnalités basées sur la localisation, mettez à jour vos paramètres de localisation sur "Toujours autoriser". Appuyez ci-dessous pour accéder aux Paramètres. »

{% alert tip %}
Vous pouvez déclencher ce message in-app à n'importe quel moment du parcours utilisateur — après un achat, lors de la consultation de contenu à proximité ou dans le cadre d'un flux Canvas. Soyez sélectif lorsque vous relancez : limitez ces campagnes aux utilisateurs fidèles ou très engagés pour éviter la lassitude face aux demandes d'abonnement.
{% endalert %}

## Exemples de stratégies d'amorçage de localisation

### Amorçage « Pendant l'utilisation de l'app »

Une application de vente au détail affiche un message in-app modal après qu'un utilisateur a enregistré un magasin en favori :

- **Titre :** « Recevez des notifications sur les offres en magasin »
- **Corps :** « Activez la localisation pour que nous puissions vous envoyer des offres exclusives lorsque vous êtes à proximité de vos magasins favoris. Votre localisation n'est utilisée que pendant l'utilisation de l'application. »
- **CTA :** **Activer la localisation** redirige via un lien profond vers l'invite native d'autorisation de localisation
- **Fermeture :** **Peut-être plus tard** ferme le message

Cette approche est efficace car l'utilisateur a déjà exprimé son intérêt pour un magasin spécifique, créant un contexte naturel pour la demande d'autorisation de localisation.

### Suivi « Toujours autoriser »

Après qu'un utilisateur a accordé l'autorisation « Pendant l'utilisation de l'app », affichez un message in-app de suivi lors de la session suivante :

- **Titre :** « Ne manquez jamais une offre à proximité »
- **Corps :** « Mettez à jour vos paramètres de localisation sur "Toujours" pour que nous puissions vous informer des offres même lorsque vous ne naviguez pas dans l'application. Nous n'enverrons que des alertes pertinentes lorsque vous serez à proximité des emplacements participants. »
- **CTA :** **Mettre à jour les paramètres** redirige via un lien profond vers la page des paramètres de localisation de l'application dans le système d'exploitation
- **Fermeture :** **Conserver les paramètres actuels** ferme le message

Ce suivi donne à l'utilisateur le contexte expliquant pourquoi le passage à « Toujours autoriser » apporte une valeur supplémentaire par rapport au niveau d'autorisation initial.

## Créer manuellement des géorepérages

### Étape 1 : Créer un ensemble de géorepérages

Pour créer un géorepérage, vous devez d'abord créer un ensemble de géorepérages.

1. Allez dans **Audience** > **Emplacements** dans le tableau de bord de Braze.
2. Sélectionnez **Créer un ensemble de géorepérages**.
3. Pour **Nom de l'ensemble**, entrez un nom pour votre ensemble de géorepérages.
4. (Facultatif) Ajoutez des étiquettes pour filtrer votre ensemble.

### Étape 2 : Ajouter les géorepérages

Ensuite, ajoutez des géorepérages à votre ensemble de géorepérages.

1. Sélectionnez **Dessiner un géorepérage** pour cliquer et faire glisser le cercle sur la carte. Répétez l'opération pour ajouter d'autres géorepérages à votre ensemble si nécessaire.
2. (Facultatif) Sélectionnez **Modifier** et remplacez la description du géorepérage par un nom.
3. Sélectionnez **Enregistrer l'ensemble de géorepérages** pour enregistrer.

{% alert tip %}
Créez des géorepérages avec un rayon d'au moins 200 mètres pour un fonctionnement optimal. Pour plus d'informations, consultez les [Bonnes pratiques de géorepérage](#geofence-best-practices).
{% endalert %}

![Un ensemble de géorepérages avec deux géorepérages « EastCoastGreaterNY » et « WesternRegion » avec deux cercles sur la carte.]({% image_buster /assets/img/geofence_example.png %})

## Téléchargement en masse de géorepérages {#creating-geofence-sets-via-bulk-upload}

Vous pouvez télécharger des géorepérages en masse sous forme d'objet GeoJSON de type `FeatureCollection`. Chaque géorepérage est un type de géométrie `Point` dans la collection de fonctionnalités. Les propriétés de chaque fonctionnalité nécessitent une clé `radius` et une clé `name` facultative pour chaque géorepérage.

Pour télécharger votre fichier JSON, sélectionnez **Plus** > **Télécharger JSON**.

Lorsque vous créez vos géorepérages, tenez compte des détails suivants :

- La valeur `coordinates` dans le GeoJSON est formatée comme `[Longitude, Latitude]`.
- Le rayon maximal du géorepérage pouvant être téléchargé est de 10 000 mètres (environ 10 kilomètres ou 6,2 miles).

### Exemple

L'exemple suivant illustre le format GeoJSON approprié pour définir deux géorepérages : l'un pour le siège social de Braze à New York, et l'autre pour la Statue de la Liberté au sud de Manhattan.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.9853689, 40.7434683]
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

Une fois vos géorepérages configurés, vous pouvez les utiliser pour améliorer et enrichir la façon dont vous communiquez avec vos utilisateurs.

### Déclencher des campagnes et des Canvas

Pour utiliser les données de géorepérage dans le cadre des déclencheurs de campagne et de Canvas, choisissez la **livraison par événement** pour la méthode de réception/distribution. Ensuite, ajoutez une action de déclenchement `Trigger a Geofence`. Pour finir, choisissez l'ensemble de géorepérages et les types d'événements de transition de géorepérage pour votre message. Vous pouvez également faire progresser les utilisateurs dans un Canvas à l'aide des événements de géorepérage.

![Une campagne basée sur l'action avec un géorepérage qui se déclenche lorsqu'un utilisateur entre dans un aéroport allemand.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personnaliser les messages

Pour personnaliser un message à l'aide des données de géorepérage, vous pouvez utiliser la syntaxe de personnalisation Liquid suivante :

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Mettre à jour des ensembles de géorepérages

Le SDK de Braze ne demande les géorepérages qu'une fois par jour au démarrage de la session. Si vous apportez des modifications aux ensembles de géorepérages après le démarrage de la session, vous devrez attendre 24 heures à compter de la première récupération des ensembles pour recevoir l'ensemble mis à jour.

Si l'utilisateur a activé les notifications push en arrière-plan, Braze envoie une notification push silencieuse toutes les 24 heures lorsque les ensembles de géorepérages sont mis à jour afin de télécharger les derniers emplacements sur l'appareil.

{% alert note %}
Si les géorepérages ne sont pas chargés localement sur l'appareil, l'utilisateur ne pourra pas déclencher le géorepérage même s'il pénètre dans la zone.
{% endalert %}

## Bonnes pratiques de géorepérage

### Configuration du géorepérage

- Utilisez un rayon de 200 mètres ou plus pour un déclenchement fiable.
- Évitez de configurer des géorepérages qui se chevauchent ou sont imbriqués les uns dans les autres, car cela peut entraîner des problèmes de déclenchement.
- Un géorepérage ne peut déclencher un événement d'entrée qu'une fois toutes les six heures. Ce temps de récupération est appliqué localement. Si un utilisateur désinstalle l'application ou efface les données de l'application, tous les temps de récupération sont réinitialisés.
- Un maximum de 20 géorepérages peut être stocké sur un appareil. Si l'utilisateur est éligible pour plus de 20, Braze télécharge les emplacements les plus proches en fonction de la proximité au démarrage de la session ou lors de l'actualisation par notification push silencieuse.
- Braze n'envoie à l'appareil que les géorepérages situés dans un rayon de 2 000 kilomètres autour de l'utilisateur.

### Exigences de l'appareil

- Les autorisations de notification push et de localisation doivent toutes deux être activées pour l'application.
- Un jeton de notification push de premier plan valide est requis.

{% alert note %}
L'intégration SDK de base active uniquement le suivi de la localisation. Le géorepérage nécessite des étapes de configuration supplémentaires pour iOS et Android. Pour plus de détails, consultez [Géorepérages]({{site.baseurl}}/developer_guide/geofences/) dans le guide du développeur.
{% endalert %}

Vous pouvez également utiliser les géorepérages avec les partenaires technologiques de Braze, tels que [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) et [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/).

## Foire aux questions

### Quelle est la différence entre les géorepérages et le suivi de la localisation ?

Dans Braze, un géorepérage est un concept différent du suivi de la localisation. Les géorepérages servent de déclencheurs pour certaines actions — lorsqu'un utilisateur entre ou sort d'une frontière virtuelle établie autour d'un emplacement géographique, cela peut déclencher une action spécifique, comme l'envoi d'un message.

Le suivi de la localisation collecte et stocke les données d'emplacement les plus récentes d'un utilisateur. Ces données peuvent être utilisées pour segmenter les utilisateurs en fonction du filtre `Most Recent Location`. Par exemple, vous pouvez utiliser le filtre `Most Recent Location` pour cibler les utilisateurs situés à New York.

Pour plus d'informations, consultez [Suivi de la localisation]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/).

### Quel est le niveau de précision des géorepérages de Braze ?

Les géorepérages de Braze utilisent une combinaison de tous les fournisseurs de localisation disponibles sur un appareil pour trianguler la position de l'utilisateur, y compris le Wi-Fi, le GPS et les antennes-relais.

La précision habituelle se situe entre 20 et 50 mètres, et la précision optimale entre 5 et 10 mètres. Dans les zones rurales, la précision peut se dégrader considérablement, potentiellement sur plusieurs kilomètres. Créez des géorepérages avec des rayons plus importants pour les zones rurales.

La précision dépend également de l'activation de la localisation précise par l'utilisateur. Avec la localisation approximative uniquement, la précision chute à environ 3 kilomètres carrés, rendant les géorepérages peu fiables. Pour plus d'informations, consultez [Localisation précise ou approximative](#precise-versus-approximate-location).

### Comment les géorepérages affectent-ils la durée de vie de la batterie ?

Le géorepérage de Braze utilise le service natif de géorepérage du système sur iOS et Android. Il est conçu pour arbitrer intelligemment entre précision et consommation d'énergie, économisant la batterie et améliorant les performances au fur et à mesure que le service sous-jacent s'améliore.

### Quand les géorepérages sont-ils actifs ?

Les géorepérages de Braze fonctionnent à toute heure de la journée, même lorsque votre application est fermée. Ils deviennent actifs dès qu'ils sont définis et téléchargés dans le tableau de bord de Braze. Cependant, les géorepérages ne peuvent pas fonctionner si l'utilisateur a désactivé le suivi de la localisation.

Pour que les géorepérages fonctionnent, les utilisateurs doivent avoir activé les services de localisation sur leur appareil et avoir accordé à votre application le niveau d'autorisation de localisation requis. Pour plus d'informations, consultez [Comprendre les autorisations de localisation](#understanding-location-permissions).

### Les données de géorepérage sont-elles stockées dans les profils utilisateurs ?

Non, Braze ne stocke pas de données de géorepérage dans les profils utilisateurs. Les géorepérages sont surveillés par les services de localisation d'Apple et de Google, et Braze n'est notifié que lorsqu'un utilisateur déclenche un géorepérage. À ce stade, Braze traite toutes les campagnes de déclenchement associées.

### Puis-je définir un géorepérage au sein d'un géorepérage ?

Il est recommandé d'éviter de configurer des géorepérages qui se chevauchent, car cela pourrait entraîner des problèmes lors du déclenchement des notifications.

### Que se passe-t-il si un utilisateur refuse l'accès à la localisation ?

Votre équipe de développement peut configurer un lien profond qui ouvre la page des paramètres de localisation de l'application dans le système d'exploitation, où les utilisateurs peuvent mettre à jour leurs autorisations. Vous pouvez utiliser ce lien profond dans un message in-app personnalisé à n'importe quel moment du parcours utilisateur. Soyez sélectif quant au moment où vous affichez ce message — ciblez les utilisateurs engagés ou ceux qui ont effectué une action à forte valeur pour augmenter les chances d'abonnement. Pour plus d'informations, consultez [Rediriger les utilisateurs vers les paramètres du système d'exploitation](#redirecting-users-to-os-settings).