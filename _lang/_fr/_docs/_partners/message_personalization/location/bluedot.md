---
nav_title: Bluedot
article_title: Bluedot
alias: /fr/partners/bluedot/
description: "Cet article décrit le partenariat entre Braze et Bluedot, une plateforme de localisation, fournissant une plate-forme de géorepérage précise et simple pour vos applications."
page_type: partenaire
search_tag: Partenaire
---

# Bluedot

> [Bluedot](https://bluedot.io/) est une plateforme de localisation qui fournit une plate-forme de géorepérage précise et simple pour vos applications. Utilisez le SDK de Bluedot pour envoyer des messages plus intelligents, automatiser l'enregistrement des commandes mobiles, optimiser les flux de travail et créer des expériences sans friction.

L'intégration de Braze et Bluedot vous permet d'utiliser les services de localisation de géorepérage de Bluedot pour créer des événements utilisateur qui peuvent être utilisés pour construire des voyages, et analyser les comportements et les intérêts des clients. Les événements (entrée/sortie) générés par l'utilisateur sur son appareil sont envoyés immédiatement à Braze avec toutes les informations pertinentes.

## Pré-requis

| Exigences      | Libellé                                                                             |
| -------------- | ----------------------------------------------------------------------------------- |
| Compte Bluedot | Un compte Bluedot actif est nécessaire pour profiter de cette intégration de Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Cas d'utilisation

Les informations personnalisées de localisation de l'événement fournies par Bluedot peuvent être utilisées dans vos campagnes pour obtenir des cas d'utilisation communs tels que:
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (Quick Service Restaurant)
- [`Cliquez et Collectez`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/)

## Intégration

### Étape 1 : Créer un projet Bluedot
Configurez votre compte Bluedot et connectez-vous à votre tableau de bord [Bluedot Canvas](https://docs.bluedot.io/canvas/). Visitez la documentation [Bluedot]((https://docs.bluedot.io/canvas/creating-a-new-project/)) pour apprendre comment créer un nouveau projet.

### Étape 2 : Intégrer les SDK
Intégrez le SDK Bluedot Point et le Braze SDK dans votre application en suivant les étapes fournies dans la documentation de l'intégration [Bluedot-Braze](https://docs.bluedot.io/integrations/braze-integration/).

### Étape 3 : Autheticate the Bluedot SDK
Utilisez le `projectId` créé à l'étape 1 pour authentifier le SDK Bluedot Point.

### Étape 4 : Utilisez les événements Bluedot dans Braze

#### Messages de déclenchement

Vous pouvez mettre en place une campagne de push ou Canvas qui s'activera sur les événements de localisation générés par le SDK Bluedot. Cette route d'intégration est idéale pour les messages en temps réel lorsque les utilisateurs entrent dans un lieu ou un lieu d'intérêt ou de communication de suivi retardée après leur départ.

Configurez une campagne basée sur l'action au sein de Braze qui enverra des messages en fonction d'un emplacement défini. Pour votre déclencheur, utilisez un événement personnalisé de `bluedot_entry` ou `bluedot_exit` comme indiqué ci-dessous:

![Composition de la campagne Bluedot]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="largeur-max-80%"}

#### Cibler les utilisateurs

Assurez-vous de cibler **tous les utilisateurs** pour votre groupe d'applications. ![Bluedot Campaign Compose]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}