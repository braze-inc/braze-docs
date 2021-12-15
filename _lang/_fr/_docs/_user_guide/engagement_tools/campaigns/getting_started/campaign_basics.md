---
nav_title: Les Bases de la Campagne
article_title: Les Bases de la Campagne
page_order: 1
page_type: Référence
description: '« Cet article de référence couvre les bases des campagnes, couvrant diverses questions que vous devriez vous poser lors de la mise en place de vos premières campagnes ».'
tool: Campagnes
---

# Campagnes : Les bases

## Trouvez votre stratégie avec les cinq W de visualisation

Répondez aux questions ci-dessous pour commencer:

* __Qu'est-ce que__ j'essaie d'aider le client à faire ou à comprendre ? (Camp<unk> Nom)

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

* __Pourquoi__ est-ce que je crée cette campagne ?
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

## Construire la campagne de voyage client

### Nommez votre campagne: Le “quoi”

Ne sous-estimez jamais la puissance du nom. Braze est construit pour la collaboration, donc le moment est idéal pour se familiariser avec la façon dont vous communiquerez vos objectifs avec votre équipe. Vous pouvez ajouter des Tags (y compris des Tags Teams) et nommer à la fois les étapes et les variantes dans la campagne. Pour en savoir plus sur les voyages des clients, consultez notre cours LAB [Mapping User Lifecycles](http://lab.braze.com/mapping-customer-lifecycles)!

### Créer les conditions de départ : Le « Quand »

Quand un client va-t-il se lancer dans cette campagne ? Les utilisateurs peuvent entrer dans votre campagne de trois manières: planifiée, basée sur l'action ou déclenchée par l'API.

| Planifié                                                                                                                                                                                                           | Action-Based                                                                                                                                                                                                                                                                                                            | Déclenché par l'API                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vous pouvez utiliser la livraison prévue lorsque vous souhaitez envoyer une campagne immédiatement à votre public cible, le faire envoyer régulièrement, ou le programmer pour une heure spécifique dans le futur. | Ces campagnes répondent à des comportements spécifiques des clients au fur et à mesure qu'ils se produisent. Ces déclencheurs basés sur l'action peuvent inclure l'ouverture de votre application, la réalisation d'un achat, l'interaction avec une autre campagne ou le déclenchement de tout événement personnalisé. | Votre équipe de marketing et vos ingénieurs travailleront ensemble pour déterminer les actions clés du client sur votre plateforme que, une fois réalisé, déclenchera un appel API à Braze et enverra vos campagnes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Sélectionnez un public d'entrée pour l'entrée: Le « qui»

« Qui tentez de vous atteindre? » Ici, vous pouvez utiliser un segment prédéfini et ajouter d'autres filtres. Les filtres incluent:

| Filtre                     | Libellé                                                                                                                                                                                                                             |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Données personnalisées     | Les filtres de données personnalisés vous permettent de segmenter les utilisateurs en fonction des événements et des attributs que vous définissez. Avec eux, vous pouvez utiliser des fonctionnalités spécifiques à votre produit. |
| Activité de l'utilisateur  | Les filtres d'activité utilisateur vous permettent de segmenter les clients en fonction de leurs actions et achats.                                                                                                                 |
| Reciblage                  | Les filtres de redistribution vous permettent de segmenter les clients qui ont été envoyés, reçus ou interagissés avec les campagnes précédentes ou les Canvases.                                                                   |
| Activité marketing         | Les filtres de marketing filtrent les clients en fonction de comportements universels comme le dernier engagement ou les campagnes reçues.                                                                                          |
| Attributs de l'utilisateur | Les clients du segment des filtres d'attributs utilisateur par leurs attributs et caractéristiques constants.                                                                                                                       |
| Installer Attribution      | Installez des filtres d'attribution pour les clients par leur première source, adgroup, campagne ou publicité.                                                                                                                      |
| Activité sociale           | L'activité sociale filtre les clients en fonction de leur activité sur les réseaux sociaux, notamment par la connexion à Facebook et Twitter.                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

Seuls les utilisateurs qui correspondent à ces critères d'audience cible peuvent entrer dans le voyage.

### Identifier les événements de conversion : le « pourquoi»

Pourquoi construisez-vous cette campagne? Il est toujours important d'avoir un objectif défini en tête, et campagnes vous aident à comprendre comment vous vous exécutez contre des KPIs tels que l'engagement de session, les achats et les événements personnalisés.

La sélection d'au moins un événement de conversion vous permettra de comprendre la performance de votre campagne.

### Construisez l’expérience : « comment» et « où»

Considérez la mise en place de variantes et de tests A/B. Une variante est un parcours que chaque client suit tout au long de son voyage. Les campagnes prennent en charge jusqu'à huit variantes avec un groupe de contrôle. Bien qu'il ne soit pas obligatoire, vous pouvez nommer chaque variante et contrôler la distribution du public cible en suivant chaque variante. Le ciel est la limite à partir de là, donc comment décidez-vous de la forme de votre campagne? C’est là que vos objectifs, vos données et vos hypothèses entrent en jeu. Le remue-méninges « comment » et « où» de la partie supérieure de votre cerveau vous aidera à tracer le bon voyage des utilisateurs pour votre campagne. Il y a quelques approches que vous pouvez utiliser:
- __Travail en arrière :__ Certains buts ont des sous-objectifs plus petits. Par exemple, si vous visez à convertir un utilisateur gratuit en abonnement, vous aurez peut-être besoin d’une page avec vos services d’abonnement. Un visiteur peut avoir besoin de voir les options avant d'acheter. Vous pouvez concentrer vos efforts de messagerie sur leur montrer cette page avant une page de paiement. Travailler en arrière pour comprendre le voyage que le client doit parcourir pour atteindre son objectif est essentiel pour le guider vers la conversion.
- __Commencez par le statu quo et ajoutez-en plus :__ Avez-vous mené une campagne similaire par le passé ? Ou bien est-il actuellement en cours d'exécution ? Utilisez ce message et ajoutez-le. Essayez un nouveau filtre ou ajoutez un message de suivi. Regardez vos performances et continuez à optimiser en apportant des changements incrémentaux.
- __Regardez vers les autres :__ L'imitation est la forme la plus élevée de flatterie. Ne réinventez pas la roue. Ne vous inquiétez pas, nous vous avons couverts. À la fin de ce guide, vous trouverez quelques lignes qui peuvent vous aider à commencer.