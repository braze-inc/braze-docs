---
nav_title: Notions de base des campagnes
article_title: Notions de base des campagnes
page_order: 1
page_type: reference
description: « Le présent article de référence aborde les fondamentaux des campagnes, notamment diverses questions que vous devez vous poser lorsque vous configurez votre première campagne. »
tool: Campaigns

---

# Campagnes : Fondamentaux

## Trouvez votre stratégie avec les cinq W de la visualisation

Répondez aux questions suivantes pour commencer :

1. **Que (What)** puis-je faire pour aider le client à mieux comprendre ? (Nom de campagne)<br>
<br>


2. **Quand (When)** un utilisateur commencera-t-il cette expérience ? Choisissez l’un des éléments suivants :
    * **Planification** : Entrer les utilisateurs à un moment donné
    * **En fonction de l’action** : Entrer les utilisateurs lorsqu’ils effectuent des actions 
      * Effectuer un achat
      * Lancer une session
      * Effectuer un événement personnalisé
      * Saisir un emplacement
      * Interagir ou quitter une autre campagne ou Canvas
    * **Déclenché par un API** (avancé) : Entrer des utilisateurs lorsqu’ils effectuent une action spécifique déclenchant une demande API à Braze 
      * Les campagnes déclenchées par API vous donnent la possibilité de stocker le contenu d’un message dans le tableau de bord de Braze, en indiquant le moment où un message est envoyé et son destinataire, via votre API.<br>
<br>


3. **Qui (Who)** essayons-nous de joindre ? (Nom du segment avec filtres facultatifs supplémentaires)
  * Données personnalisées
  * Activité de l’utilisateur
  * Reciblage
  * Activité de marketing
  * Attributs utilisateur
  * Attribution d’installation
  * Activité sociale<br>
<br>


4. **Pourquoi (Why)** je crée cette campagne ?
  * Lancer la session : Je souhaite qu’ils rejoignent l’application.
  * Effectuer un achat : Je souhaite qu’ils effectuent un achat.
  * Effectuer un événement personnalisé : Je souhaite qu’ils effectuent une action spécifique pour laquelle je réalise un suivi comme événement personnalisé.
  * Mises à niveau d’application : Je souhaite qu’ils mettent à niveau leur version d’application<br>
<br>


5. **Où (Where)** devrais-je les contacter ?
  * E-mail
  * Notification push (Android, iOS, Windows, Web)
  * Messages in-app
  * Cartes de contenu
  * SMS ou MMS
  * Webhook<br>
<br>


6. **Comment (How)** devrais-je les contacter ? (Endroit idéal pour tester les différentes configurations de messagerie)
  * **Timing** : Planifier ou déclencher des messages à l’aide d’outils tels que Timing Intelligent et des délais après le déclenchement d’événements
  * **Cadence et canal** : Utiliser un canal puis un autre ou envoyer plusieurs messages sur plusieurs canaux simultanément
  * **Contenu** : Concevoir une copie créatrice avec plusieurs appels, des propositions de valeur et CTA
  * **Ciblage** : Ajouter des segments supplémentaires et des filtres
  * **Déclencheurs** : Utiliser des actions client pour déclencher des messages

## Création du parcours client dans la campagne

### Nommez votre campagne : Le « what » (quoi)

Ne sous-estimez jamais le pouvoir du nom. Braze est conçu pour la collaboration, c’est donc le moment idéal pour évaluer la façon dont vous communiquez les objectifs à votre équipe. Vous pouvez ajouter des balises (dont des balises Teams) et nommer les étapes et les variantes dans la campagne. Pour en savoir plus sur les parcours client, consultez notre Cours d’apprentissage Braze sur le [mappage des cycles de vie utilisateur](https://learning.braze.com/mapping-customer-lifecycles) !

### Créer des conditions de démarrage : Le « When » (quand)

Quand un client accédera-t-il à cette campagne ? Les utilisateurs peuvent accéder à votre campagne de 3 façons : par une planification, des déclencheurs basés sur une action ou déclenchés par API.

| Planification | En fonction de l’action | Déclenchée par API |
|---|---|---|
|Vous pouvez planifier une livraison lorsque vous souhaitez envoyer une campagne immédiatement à votre audience cible, l’envoyer régulièrement ou planifier l’envoi à un moment spécifique dans le futur. | Ces campagnes répondent à des comportements des clients spécifiques, lorsqu’ils se produisent. Ces déclencheurs basés sur une action peuvent inclure l’ouverture de votre application, un achat effectué, l’interaction avec une autre campagne ou le déclenchement d’un événement personnalisé. | Votre équipe marketing et les ingénieurs travailleront ensemble pour déterminer les actions clés des clients sur votre plateforme qui, une fois effectuées, déclencheront un appel API à Braze et enverront vos campagnes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Sélectionnez une audience d’entrée pour l’entrée : Le « who » (qui)

Qui (Who) essayez-vous de joindre ? Vous pouvez utiliser un segment prédéfini et ajouter d’autres filtres comme :

| Filtre | Description |
|---|---|
| Données personnalisées | Les filtres Données personnalisées vous permettent de segmenter des utilisateurs en fonction d’événements et d’attributs que vous définissez. Ils vous permettent d’utiliser des fonctionnalités spécifiques pour votre produit. |
| Activité de l’utilisateur | Les filtres Activité de l’utilisateur vous permettent de segmenter des clients en fonction de leurs actions et achats. |
| Reciblage | Les filtres Reciblage vous permettent de segmenter des clients ayant été transférés, reçus ou ayant interagi avec des campagnes ou Canvas précédents. |
| Activité de marketing | Les filtres Marketing segmentent les clients en fonction de comportements universels, tels que le dernier engagement ou les campagnes reçues. |
| Attributs utilisateur | Les filtres Attribut utilisateur segmentent les clients en fonction de leurs caractéristiques et attributs constants. |
| Attribution d’installation | Les filtres Attribution d’installation segmentent les clients en fonction de leur première source, groupe d’annonces, campagne ou annonce. |
| Activité sociale | Les filtres Activité sociale segmentent les clients en fonction de leur activité sur les réseaux sociaux, à savoir leur connexion à Facebook et Twitter. |
{: .reset-td-br-1 .reset-td-br-2}

Seuls les utilisateurs répondant à ces critères d’audience cible peuvent accéder au parcours.

### Identifier des événements de conversion : Le « why » (pourquoi)

Pourquoi créez-vous cette campagne ? Il est toujours important d’avoir un objectif défini en tête et les campagnes vous permettent de comprendre comment vous vous situez par rapport aux KPI tels que l’engagement de session, les achats et les événements personnalisés.

Sélectionner au moins un événement de conversion vous donnera la possibilité de comprendre les performances de votre campagne.

### Consolider l’expérience : Le « how » (comment) et « where » (où)

Envisagez de configurer des variantes et des tests A/B. Une variante désigne une piste que chaque utilisateur suit sur son parcours. Les campagnes prennent en charge jusqu’à huit variantes avec un groupe de contrôle. Bien que cela ne soit pas nécessaire, vous pouvez nommer chaque variante et contrôler la répartition de l’audience cible, suivant chaque variante. Il n’y a pas de limites, comment définissez-vous donc la forme de votre campagne ? C’est à ce niveau que vos objectifs, données et hypothèses entrent en jeu. La réflexion sur « how » (comment) et « where » (où) vous aidera à mapper le bon parcours utilisateur pour votre campagne. Vous pouvez utiliser deux approches :
- **Travailler à contresens** : Certains objectifs ont des sous-objectifs identiques. Par exemple, si votre objectif est de convaincre un utilisateur libre de souscrire, vous aurez besoin d’un document indiquant vos services d’abonnement. Un visiteur doit voir les options avant d’acheter. Vous devez mettre en avant cette page avant une page de paiement. Travailler à contresens pour comprendre le parcours d’un client va de pair avec la réalisation de votre objectif, élément clé pour la conversion.
- **Commencer par le statu quo et ajouter des éléments** : Avez-vous déjà réalisé une campagne identique dans le passé ? Ou est-ce la première que vous menez ? Utilisez un message et ajoutez-en d’autres. Essayez un nouveau filtre ou ajoutez un message de réponse. Examinez vos performances et continuez à optimiser en apportant des modifications progressives.
- **Regarder les autres** : L’imitation est la plus grande forme de flatterie. Ne réinventez pas la roue. N’ayez crainte, nous avons une solution. À la fin de ce guide, vous trouverez des caractéristiques essentielles qui vous aideront à démarrer.
