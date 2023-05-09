---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "Cet article de référence présente le partenariat entre Braze et Bluedot, une plateforme d’emplacement, offrant une plateforme de géorepérage précise et simple pour vos applications."
page_type: partner
search_tag: Partenaire

---

# Bluedot

> [Bluedot](https://bluedot.io/) est une plateforme d’emplacement qui propose une plateforme de géorepérage précise et simple pour vos applications. Utilisez le SDK de Bluedot pour envoyer des messages plus intelligents, automatiser les enregistrements de commandes mobiles, optimiser les flux de travail et créer des expériences sans problème. 

L’intégration Braze et Bluedot vous permet d’utiliser les services de positionnement de geofence Bluedot pour créer des événements utilisateur qui peuvent être utilisés pour créer des voyages, des campagnes et analyser les comportements et les intérêts des clients. Les événements (entrée/exit) générés par l’utilisateur sur leur appareil sont envoyés immédiatement à Braze avec toutes les informations pertinentes. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Bluedot | Un compte Bluedot est requis pour profiter de cette intégration. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

Les informations sur les lieux d’événements personnalisés fournis par Bluedot peuvent être utilisées dans vos campagnes pour obtenir des exemples d’utilisation courants comme :
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (Restaurant de service rapide)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/) 

## Intégration

### Étape 1 : Créer un projet Bluedot
Configurez votre compte Bluedot et connectez-vous à votre [tableau de bord Bluedot Canvas](https://docs.bluedot.io/canvas/). Consultez la [documentation Bluedot]((https://docs.bluedot.io/canvas/creating-a-new-project/)) pour savoir comment créer un nouveau projet.

### Étape 2 : Intégrer les SDK
Intégrez le SDK Bluedot Point et le SDK Braze dans votre application en suivant les étapes indiquées dans la documentation [Intégration Bluedot-Braze](https://docs.bluedot.io/integrations/braze-integration/).

### Étape 3 : Authentifier le SDK Bluedot
Utilisez la valeur `projectId` créée à l’étape 1 pour authentifier le SDK Bluedot Point.

### Étape 4 : Utiliser les événements Bluedot dans Braze

#### Messages déclencheurs

Vous pouvez mettre en place une campagne de notification push ou Canvas qui activera les événements de localisation générés par le SDK Bluedot. Cette méthode d’intégration est idéale pour les envois de messages en temps réel, lorsque les utilisateurs entrent dans un site ou un lieu d’intérêt ou pour les messages retardés de suivi après qu’ils l’aient quitté.

Configurez une campagne basée sur les actions au sein du Braze qui enverra des messages basés sur un emplacement défini. Pour votre déclencheur, utilisez un événement personnalisé comme `bluedot_entry` ou `bluedot_exit` comme illustré dans la capture d’écran suivante :

![Une campagne basée sur les actions dans l’étape de livraison. Ici, vous disposez de deux options de planification qui vont envoyer la campagne si un utilisateur effectue un événement personnalisé `bluedot_entry` ou `bluedot_exit`.]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### Ciblage des utilisateurs

Assurez-vous de cibler **Tous les utilisateurs** pour votre groupe d’apps.
![Une campagne basée sur des actions avec l’étape utilisateurs cibles vous encourageant à sélectionner « Tous les utilisateurs » comme segment souhaité.]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}