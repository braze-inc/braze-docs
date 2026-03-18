---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilot est une application mobile conçue pour se connecter de façon fluide à votre tableau de bord de Braze. Cela vous permet de lancer des campagnes et des Canvases sur l'application, donnant ainsi vie aux messages Braze sur votre propre téléphone. Braze Pilot comprend une bibliothèque de simulations d'applications pour des marques fictives représentant différents secteurs, vous permettant ainsi de découvrir comment vos messages pourraient être perçus par vos clients."
description: "Découvrez les différentes façons d'utiliser Braze pour envoyer des messages depuis le tableau de bord de Braze vers votre téléphone."

guide_featured_title: "Section Articles"
guide_featured_list:
  - name: Premiers pas avec Braze Pilot
    link: /docs/user_guide/getting_started/braze_pilot/getting_started/
    image: /assets/img/braze_icons/brush-02.svg
  - name: Dictionnaire de données
    link: /docs/user_guide/getting_started/braze_pilot/data_dictionary/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Liens profonds
    link: /docs/user_guide/getting_started/braze_pilot/deep_links/
    image: /assets/img/braze_icons/link-03.svg

---

## Simulations de l'application pilote

Le cœur de Braze Pilot réside dans sa bibliothèque de simulations d'applications. Chaque application est une simulation réaliste d'une marque fictive spécifique à un secteur d'activité, conçue pour enregistrer un large éventail d'événements et d'attributs qui offrent des possibilités infinies pour alimenter les cas d'utilisation courants de Braze.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington est une application de fitness proposant des entraînements, des objectifs d'exercice et un service premium Steppington+. Il propose plusieurs emplacements pour présenter [les cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), une section pouvant être dévoilée à l'aide d'[indicateurs de fonctionnalités]({{site.baseurl}}/developer_guide/feature_flags), ainsi qu'une bibliothèque complète de journaux d'événements personnalisés qui permettent d'illustrer de nombreux parcours clients pour ce secteur.

![La page d'accueil de Steppington avec des icônes pour l'entraînement au marathon, le yoga, le cyclisme et la musculation.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantsLabyrinth

PantsLabyrinth est une application de commerce électronique qui commercialise, comme son nom l'indique, des pantalons. L'application PantsLabyrinth offre une expérience complète de paiement du panier d'achat, une fonctionnalité optionnelle de liste de souhaits qui peut être activée à l'aide d'un indicateur de fonctionnalité, ainsi que de nombreuses occasions de partager des plaisanteries avec des amis du Royaume-Uni.

![Une page produit pour PantsLabyrinth avec des options permettant d'ajouter des jeans au panier.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon 

MovieCanon est un service de streaming spécialement conçu pour illustrer les cas d'utilisation courants de Braze en matière d'engagement vis-à-vis du contenu. 

![L'application MovieCanon propose divers thrillers à visionner.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Comment Pilot se connecte à votre tableau de bord de Braze

Le SDK Braze est un ensemble de codes qui collecte les données de vos utilisateurs une fois intégré à votre application ou à votre site web. Lorsque vous connectez Pilot à votre tableau de bord, vous initialisez cette connexion entre l'application Pilot sur votre téléphone et le SDK Braze, et vous établissez une connexion unique avec votre instance Braze en fournissant à Pilot l'identifiant de votre clé API pour votre tableau de bord.

![La première étape de la configuration de Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Une fois Pilot connecté à votre tableau de bord de Braze, le SDK Braze fonctionne dans l'application exactement comme il le ferait si vous l'intégriez à votre propre application ou site web. Cela signifie que Braze s'engage à :

- Veuillez enregistrer les données relatives à votre activité utilisateur dans Pilot, y compris les données personnalisées spécifiques aux marques fictives de l'application.
- Collectez automatiquement les données de session, les informations sur les appareils et les jetons push.
- Les notifications push, les messages in-app et les canaux de communication de la carte de contenu nécessitent l'intégration SDK pour fonctionner.

Pour en savoir plus sur le SDK Braze, veuillez consulter la section [Intégration]({{site.baseurl}}/user_guide/getting_started/integration).

![La suite d'engagement client Braze, qui comprend des intégrations, des API, des SDK pour l'ingestion de données, la classification, l'orchestration et la personnalisation des données, ainsi que des actions avec des canaux de communication pour une boucle de rétroaction interactive avec vos clients.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Profils utilisateur dans Braze

Chaque donnée transmise à Braze est stockée dans un profil utilisateur dédié à un utilisateur particulier de votre application ou site web. Une fois que vous aurez connecté Pilot à votre tableau de bord de Braze, Braze commencera à enregistrer des données vous concernant en tant qu'utilisateur de Pilot. Deux types d'utilisateurs peuvent être créés pour vous via cette connexion : les utilisateurs anonymes et les utilisateurs identifiés.

### Anonyme 

Cet état de connexion représente l'expérience d'un invité de votre application ou site Web qui ne s'est pas encore connecté. Si vous initiaisez Pilot en tant qu'utilisateur anonyme, Braze créera un [profil utilisateur anonyme]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users) pour vous et enregistrera les données relatives à votre activité dans ce profil. Les utilisateurs anonymes peuvent toujours être ciblés par des campagnes, mais vous ne pourrez pas consulter leur profil utilisateur directement dans votre tableau de bord de Braze.

### Identifié

Ce statut de connexion signifie que Braze reconnaît votre profil utilisateur grâce à un identifiant unique qui vous a été attribué, appelé identifiant externe. Vous pouvez rechercher cet identifiant externe dans la page **Recherche d'utilisateurs** de votre tableau de bord afin de localiser votre profil utilisateur, qui stockera tous les attributs utilisateur et événements enregistrés par Pilot en fonction de votre activité dans l'application.

![Exemple de profil utilisateur Braze pour l'utilisateur « torchie-208117 ».]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### Type de connexion

Pour vérifier le type de connexion dont vous disposez, veuillez consulter l'état de la connexion en haut à droite de votre écran.

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

Si vous enregistrez des données en tant qu'utilisateur identifié, une icône utilisateur s'affichera à côté de votre ID externe.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**« Non connecté** » indique que vous n'avez pas encore initialisé la connexion du SDK Braze avec Pilot.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Campagnes et canvas

Les campagnes et les canevas vous permettent d'envoyer des messages à vos utilisateurs. 

- Les campagnes sont idéales pour les messages uniques envoyés à un segment d'audience spécifique sur différents canaux. 
- Les canevas sont des flux de campagne avancés qui vous permettent d'automatiser et d'orchestrer des parcours clients personnalisés sur plusieurs canaux. Dans un Canvas, vous pouvez mettre en place une logique de branchement, des délais, des points de décision et des événements de conversion pour guider les clients à travers une série d'interactions. Les canevas contribuent à garantir une communication cohérente et fluide entre les différents points de contact, augmentant ainsi les chances d'engagement client et de conversion.

## Canaux de communication pris en charge

Braze Pilot prend actuellement en charge [les messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), qui apparaissent dans votre application et permettent d'envoyer des messages opportuns lorsque l'utilisateur est activement engagé.

![Un message in-app dans l'application MovieCanon : « Appréciez-vous MovieCanon ? Veuillez recommander vos amis ! » avec la possibilité de saisir votre adresse de e-mail pour envoyer une recommandation.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}