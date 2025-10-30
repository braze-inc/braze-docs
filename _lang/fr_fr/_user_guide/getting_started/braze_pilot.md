---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilot est une application mobile conçue pour se connecter de façon fluide/sans heurts à votre tableau de bord Braze. Vous pouvez ainsi lancer des campagnes et des toiles dans l'application, donnant vie aux messages de Braze sur votre propre téléphone. Braze Pilot comprend une bibliothèque de simulations d'applications pour des marques fictives représentant différents secteurs d'activité, ce qui vous permet d'expérimenter ce que pourrait être votre envoi de messages du point de vue de vos clients."
description: "Découvrez les différentes façons d'utiliser Braze pour envoyer des messages depuis le tableau de bord de Braze vers votre téléphone."

guide_featured_title: "Articles de section"
guide_featured_list:
  - name: Démarrer avec Braze Pilot
    link: /docs/user_guide/getting_started/braze_pilot/getting_started/
    image: /assets/img/braze_icons/brush-02.svg
  - name: Dictionnaire de données
    link: /docs/user_guide/getting_started/braze_pilot/data_dictionary/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Liens profonds
    link: /docs/user_guide/getting_started/braze_pilot/deep_links/
    image: /assets/img/braze_icons/link-03.svg

---

## Simulations d'applications pilotes

Le cœur de Braze Pilot est sa bibliothèque de simulations d'applications. Chaque application est une simulation réaliste d'une marque fictive spécifique à l'industrie, instrumentée pour enregistrer un riche assortiment d'événements et d'attributs qui créent des opportunités infinies pour alimenter les cas d'utilisation courants de Braze.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington est une appli de fitness avec des séances d'entraînement, des objectifs d'exercice et un service premium Steppington+. Il offre plusieurs endroits pour démontrer les [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), une section qui peut être révélée avec des [drapeaux de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags), et une bibliothèque robuste d'enregistrement d'événements personnalisés qui permettent d'illustrer de nombreux parcours clients pour ce secteur.

La page d'accueil de Steppington avec des icônes pour l'entraînement au marathon, le yoga, le cyclisme et les poids.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantalonLabyrinthe

PantsLabyrinth est une application de commerce électronique qui vend (vous l'avez deviné) des pantalons ! L'application PantsLabyrinth comprend une expérience sur l'application d'un panier d'achat complet, une fonctionnalité optionnelle de liste de souhaits qui peut être activée avec un drapeau de fonctionnalité, et de nombreuses occasions de plaisanteries sournoises avec des amis du Royaume-Uni.

Une page produit pour PantsLabyrinth avec des options pour ajouter des jeans au panier.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon 

MovieCanon est un service de streaming parfaitement conçu pour illustrer les cas d'utilisation courants de Braze autour de l'engagement de contenu. 

L'application MovieCanon propose différents films à suspense.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Comment Pilot se connecte à votre tableau de bord de Braze

Le SDK de Braze est un ensemble de codes qui recueille les données de vos utilisateurs une fois intégré à votre app ou site web. Lorsque vous connectez Pilot à votre tableau de bord, vous initialisez cette connexion entre l'application Pilot sur votre téléphone et le SDK de Braze, et vous établissez une connexion unique avec votre instance Braze en donnant à Pilot votre identifiant de clé API pour votre tableau de bord.

La première étape de la mise en place de Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Une fois que Pilot se connecte à votre tableau de bord de Braze, le SDK de Braze fonctionne dans l'application comme il le fera une fois que vous aurez intégré le SDK à votre propre application ou site web. Cela signifie que Braze va :

- Stocker des données sur l'activité de vos utilisateurs dans Pilot, y compris des données personnalisées propres aux marques fictives de l'appli.
- Collectez automatiquement les données de session, les infos sur l'appareil et les jetons de poussée.
- Alimentez les notifications push, les messages in-app et les canaux d'envoi de messages des cartes de contenu qui nécessitent une intégration SDK pour fonctionner.

Pour en savoir plus sur le SDK de Braze, consultez la rubrique [Intégration]({{site.baseurl}}/user_guide/getting_started/integration).

La pile d'engagement client de Braze, qui comprend des intégrations, des API, des SDK pour l'ingestion de données, la classification, l'orchestration, la personnalisation et l'action avec des canaux de messagerie pour une boucle de rétroaction interactive avec vos clients.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Profils utilisateurs à Braze

Chaque donnée envoyée à Braze est stockée dans un profil utilisateur dédié à un utilisateur particulier de votre app ou site web. Une fois que vous avez connecté Pilote à votre tableau de bord de Braze, Braze commencera à enregistrer des données sur vous en tant qu'utilisateur de Pilote. Deux types d'utilisateurs peuvent être créés pour vous grâce à cette connexion : les utilisateurs anonymes et les utilisateurs identifiés.

### Anonyme 

Cet état de connexion conseille l'expérience sur l'application d'un invité de votre application ou site web qui ne s'est pas encore connecté. Si vous initialisez Pilot en tant qu'utilisateur anonyme, Braze crée un [profil utilisateur anonyme]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users) pour vous et y enregistre des données sur votre activité. Les utilisateurs anonymes peuvent toujours être ciblés par des campagnes, mais vous ne pourrez pas consulter leur profil utilisateur directement dans votre tableau de bord Braze.

### Identifié

Cet état de connexion signifie que Braze reconnaît votre profil utilisateur grâce à un identifiant unique qui vous est attribué, appelé identifiant externe. Vous pouvez rechercher cet identifiant externe dans la page **Recherche d'utilisateur** de votre tableau de bord pour localiser votre profil utilisateur, qui stockera tous les attributs utilisateur et les événements enregistrés à partir de Pilot en fonction de votre activité dans l'appli.

Exemple de profil utilisateur Braze pour l'utilisateur "torchie-208117".]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### Type de connexion

Pour vérifier le type de connexion dont vous disposez, vous pouvez consulter l'état de la connexion en haut à droite de votre écran.

{% tabs local %}
{% tab Anonymous user  %}

**Anonyme** indique que vous enregistrez des données en tant qu'utilisateur anonyme.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_anonymous.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Identified user %}

Si vous enregistrez des données en tant qu'utilisateur identifié, une icône d'utilisateur s'affiche à côté de votre ID externe.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**Non connecté** indique que vous n'avez pas encore initialisé la connexion du SDK de Braze avec Pilot.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Campagnes et toiles

Les campagnes et les canevas vous permettent d'envoyer des messages à vos utilisateurs. 

- Les campagnes sont idéales pour les messages uniques envoyés à un segment d'audience spécifique sur différents canaux. 
- Les canevas sont des flux de campagne avancés qui vous permettent d'automatiser et d'orchestrer des parcours clients personnalisés sur plusieurs canaux. Dans un Canvas, vous pouvez mettre en place une logique de branchement, des délais, des points de décision et des événements de conversion pour guider les clients à travers une série d'interactions. Les toiles permettent d'assurer une communication cohérente et fluide sur différents points de contact, augmentant ainsi les chances d'engagement client et de conversion.

## Canaux d'envoi de messages pris en charge

Braze Currents prend actuellement en charge les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), qui apparaissent dans votre application, délivrant des messages opportuns pendant que l'utilisateur est activement engagé.

Un message in-app dans l'application MovieCanon "Vous appréciez MovieCanon ? Parrainez vos amis" avec une option permettant d'entrer votre e-mail pour envoyer une recommandation.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}