---
nav_title: Bases de la toile
article_title: Bases de la toile
page_order: 1
page_type: Référence
description: "Cet article de référence couvre les bases de Canvas, couvrant diverses questions que vous devriez vous poser lors de la mise en place de votre premier Canvas."
tool: Toile
---

{% comment %}
Séparez la section « Les Bases » dans « Trouvez votre stratégie » et « Bâtir votre voyage client » et « Anatomie d'un Canevas » - déplacez Anatomie d'une toile pour créer une toile et la mettre 1er. De plus, créez un formulaire réel pour qu'ils téléchargent - besoin d'écrire dans l'endroit où cette information deviendra utile.
{% endcomment %}

# Canevas : Les bases

## Trouvez votre stratégie avec les cinq W de visualisation

Répondez aux questions ci-dessous pour commencer:

* __Qu'est-ce que__ j'essaie d'aider le client à faire ou à comprendre ? (Nom du canevas)

* __Quand__ un utilisateur commencera-t-il cette expérience ? Choisissez un.
  * Entrez les utilisateurs à une heure désignée : __Planifié__
    * Démarrer une session
    * Effectuer un événement personnalisé
    * Entrez un emplacement
    * Interagissez avec ou quittez une autre campagne ou Canvas
  * Entrez l'utilisateur quand il effectue des actions : __-Based Action__
    * Effectuer un achat
    * Démarrer une session
    * Effectuer un événement personnalisé
    * Entrez un emplacement
    * Interagissez avec ou quittez une autre campagne ou Canvas
  * Entrez les utilisateurs lorsqu'ils effectuent une action spécifique qui déclenche une requête API à Braze (avancé): __API-Triggered__
    * Les campagnes déclenchées par l'API vous donnent la flexibilité d'héberger le contenu des messages dans le tableau de bord Braze tout en dictant quand un message est envoyé et à qui, via votre API.<br><br>

* __Qui__ essayons-nous d'atteindre ? (Nom du segment avec _filtres supplémentaires_ optionnels)
  * Données personnalisées
  * Activité de l'utilisateur
  * Reciblage
  * Activité marketing
  * Attributs de l'utilisateur
  * Installer Attribution
  * Activité sociale<br><br>

* __Pourquoi__ est-ce que je crée ce Canvas ?
  * Démarrer la session : je veux qu'ils reviennent et s'engagent avec l'application.
  * Faire un achat: Je veux qu'ils achètent.
  * Effectuer un événement personnalisé : je veux qu'ils effectuent une action spécifique que je traque en tant qu'événement personnalisé.
  * Application de mise à jour : je veux qu'ils mettent à jour leur version de l'application<br><br>

* __Où__ les atteindrons-nous ?
  * Courriel
  * Pousser (Android, iOS, Windows, web)
  * Messages dans l'application
  * Cartes de contenu
  * SMS ou MMS
  * Webhook<br><br>

* __Comment__ allons-nous les atteindre ? (Excellent endroit pour tester différentes configurations de messagerie)
  * Timing : Planifier ou déclencher des messages à l'aide d'outils tels que le Timing Intelligent et les retards après les événements déclencheurs
  * Cadence & Canal: Utiliser un canal puis un autre ou envoyer des messages sur plusieurs canaux simultanément
  * Contenu: Construire une copie créative avec des appels forts, des propositions de valeur et des CGA
  * Ciblage : Ajouter des segments et/ou des filtres supplémentaires
  * Déclencheurs : Utilisez les actions client pour déclencher des messages<br><br>

## Anatomie de la toile

{% comment %}
Remplacer toutes les images ci-dessous. Penser à la section restructuration avec une image étiquetée et des onglets cliquables
{% endcomment %}

{% tabs %}
  {% tab Canvas %}
    __Canvas__ fait référence à l'espace de travail et à la visualisation globale.<br><br> ![Voyage]({% image_buster /assets/img/Canvas2.png %})
  {% endtab %}

  {% tab Journey %}
    Un voyage de __ou un voyage client__ est l'expérience d'un utilisateur individuel au sein du Canvas.<br><br> ![Voyage pour un nouvel utilisateur]({% image_buster /assets/img_archive/Journey_2.png %})
  {% endtab %}

  {% tab Entry Step %}
    __L'Étape__ et __L'Assistant d'entrée__ sont la première étape que vous prenez lors de la création de votre Canevas. Ici, vous pouvez contrôler la façon dont vos utilisateurs commencent et accomplissent leur voyage client.<br><br> ![Voyage_3]({% image_buster /assets/img/entry-wizard.gif %})
  {% endtab %}

  {% tab Variants %}
    __Variantes__ sont les flux de variantes que les marketeurs construisent qui créent des trajets personnalisés.<br><br> ![Voyage_3]({% image_buster /assets/img/variants.gif %})
  {% endtab %}

  {% tab Steps %}
    __Les étapes__ sont des points de décision individuels (comme les messages) dans une variante.<br><br> ![Voyage_4]({% image_buster /assets/img/steps.gif %})
  {% endtab %}
{% endtabs %}

## Construire le voyage du client sur Canvas

### Nommez votre Canevas : Le “quoi”

Ne sous-estimez jamais la puissance du nom. Braze est construit pour la collaboration, c'est donc le moment idéal pour se familiariser avec la façon dont vous communiquerez vos objectifs avec votre équipe. Vous pouvez ajouter des balises (y compris des balises d’équipe) et nommer à la fois les étapes et les variantes à l’intérieur du canevas. Pour en savoir plus sur les voyages des clients, consultez notre [cours LAB](http://lab.braze.com/mapping-customer-lifecycles) de cartographie de la vie des utilisateurs !

### Créer les conditions de départ : Le « Quand »

Quand un client rencontrera-t-il ce Canvas? Les utilisateurs peuvent entrer dans votre Canvas de deux façons : des déclencheurs planifiés ou axés sur l'action.

| Planifié                                                                                                                                                                                                        | Action-Based                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vous pouvez utiliser la livraison planifiée lorsque vous voulez envoyer un Canvas immédiatement à votre public cible, le faire envoyer régulièrement, ou le programmer pour une heure spécifique dans le futur. | Ces Canvases répondent à des comportements particuliers de la clientèle au fur et à mesure qu'ils se produisent. Ces déclencheurs basés sur l'action peuvent inclure l'ouverture de votre application, la réalisation d'un achat, l'interaction avec une autre campagne ou le déclenchement de tout événement personnalisé. |
{: .reset-td-br-1 .reset-td-br-2}

### Sélectionnez un public d'entrée pour l'entrée: Le « qui»

« Qui tentez de vous atteindre? » Ici, vous pouvez utiliser un segment prédéfini et ajouter d'autres filtres. Les filtres incluent:

| Filtre                     | Libellé                                                                                                                                                                                                                             |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Données personnalisées     | Les filtres de données personnalisés vous permettent de segmenter les utilisateurs en fonction des événements et des attributs que vous définissez. Avec eux, vous pouvez utiliser des fonctionnalités spécifiques à votre produit. |
| Activité de l'utilisateur  | Les filtres d'activité utilisateur vous permettent de segmenter les clients en fonction de leurs actions et achats.                                                                                                                 |
| Reciblage                  | Les filtres de redistribution vous permettent de segmenter les clients qui ont été envoyés, reçus ou interagissés avec des campagnes ou des toiles précédentes.                                                                     |
| Activité marketing         | Les filtres de marketing filtrent les clients en fonction de comportements universels comme le dernier engagement ou les campagnes reçues.                                                                                          |
| Attributs de l'utilisateur | Les clients du segment des filtres d'attributs utilisateur par leurs attributs et caractéristiques constants.                                                                                                                       |
| Installer Attribution      | Installez des filtres d'attribution pour les clients par leur première source, adgroup, campagne ou publicité.                                                                                                                      |
| Activité sociale           | L'activité sociale filtre les clients en fonction de leur activité sur les réseaux sociaux, notamment par la connexion à Facebook et Twitter.                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

Seuls les utilisateurs qui correspondent à ces critères d'audience cible peuvent entrer dans le voyage.

### Identifier les événements de conversion : le « pourquoi»

Pourquoi construisez-vous ce Canvas? Il est toujours important d'avoir un objectif défini en tête et Canvas vous aide à comprendre comment vous vous exécutez contre les indicateurs de performance comme l'engagement de session, achats, et événements personnalisés.

En sélectionnant au moins un événement de conversion, vous aurez la possibilité de comprendre la performance de votre campagne et aussi de vous aider à optimiser la performance de votre Canvas comme si votre Canvas possède plusieurs variantes et/ou un groupe de contrôle Braze utilisera l'événement de conversion pour déterminer la meilleure variation pour atteindre cet objectif.

### Construisez l’expérience : « comment» et « où»

1. __Configuration des variantes :__ Une variante est la piste que chaque client suit pendant son voyage. Canvas prend en charge jusqu'à huit variantes avec un groupe de contrôle. Bien que non requis, vous pouvez nommer chaque variante, ainsi que contrôler la distribution du public cible en suivant chaque variante.

2. __Étapes de construction :__ Une étape est un point de décision de marketing — quelle est l'expérience que vous créez ? Dans une étape, vous pouvez définir des déclencheurs ou planifier la livraison, affiner le ciblage en ajoutant des filtres ou en marquant [les événements d'exception][1] et ajouter des canaux à partir d'e-mails pour pousser sur les webhooks.

3. __Déterminer quand et comment utiliser les étapes & variantes :__ Chaque toile doit avoir au moins une variante et au moins un pas. La limite du ciel à partir de là, alors comment décidez-vous de la forme de votre Canvas ? C’est là que vos objectifs, vos données et vos hypothèses entrent en jeu. La tempête de cerveau « Comment » et « Où » venue d'en haut vous aidera à tracer la forme et la structure de votre Canevas. Il y a quelques approches que vous pouvez utiliser:
    - __Travail en arrière :__ Certains buts ont des sous-objectifs plus petits. Par exemple, si vous visez à convertir un utilisateur gratuit en abonnement, vous aurez peut-être besoin d’une page avec vos services d’abonnement. Un visiteur peut avoir besoin de voir les options avant d'acheter. Vous pouvez concentrer vos efforts de messagerie sur leur montrer cette page avant une page de paiement. Travailler en arrière pour comprendre le voyage que le client doit parcourir pour atteindre son objectif est essentiel pour le guider vers la conversion.
    - __Commencez par le statu quo et ajoutez-en plus :__ Avez-vous mené une campagne similaire par le passé ? Ou bien est-il actuellement en cours d'exécution ? Utilisez ce message et ajoutez-le. Essayez un nouveau filtre ou ajoutez un message de suivi. Regardez vos performances et continuez à optimiser en apportant des changements incrémentaux.
    - __Regardez vers les autres :__ L'imitation est la forme la plus élevée de flatterie. Ne pas réinventer dans la roue. Ne vous inquiétez pas, nous vous avons couvert. À la fin de ce guide, vous trouverez quelques lignes qui peuvent vous aider à commencer.


[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/