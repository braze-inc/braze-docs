---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "Cet article de référence présente le partenariat entre Braze et Bluedot, une plateforme de localisation qui fournit des données de géorepérage précises et simples à vos applications."
page_type: partner
search_tag: Partner

---

# Bluedot

> [Bluedot](https://bluedot.io/) est une plateforme de localisation qui fournit à vos applications des données de géorepérage précises et simples. Utilisez le SDK de Bluedot pour envoyer des messages plus intelligents, automatiser les enregistrements de commandes mobiles, optimiser les flux de travail et créer des expériences fluides. 



## À propos de l'intégration

L'intégration de Braze et de Bluedot vous permet d'utiliser les services delocalisation de Bluedot pour créer des événements utilisateur qui peuvent être utilisés pour créer des parcours, des campagnes et analyser les comportements et les intérêts des clients. Les événements (entrée/sortie) générés par l'utilisateur sur son appareil sont envoyés immédiatement à Braze avec toutes les informations pertinentes. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Bluedot | Un compte Bluedot est nécessaire pour profiter de cette intégration. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Les informations personnalisées sur l'emplacement des événements fournies par Bluedot peuvent être utilisées dans vos campagnes pour réaliser des cas d'utilisation courants tels que :
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (Restaurant à service rapide)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/) 

## Intégration

### Étape 1 : Créer un projet Bluedot
Créez votre compte Bluedot et connectez-vous à votre [tableau de bord Bluedot Canvas](https://docs.bluedot.io/canvas/). Consultez la [documentation de Bluedot](https://docs.bluedot.io/canvas/creating-a-new-project/) pour savoir comment créer un nouveau projet.

### Étape 2 : Intégrer les SDK
Intégrez le SDK Bluedot Point et le SDK Braze dans votre application en suivant les étapes fournies dans la documentation sur l'[intégration Bluedot-Braze](https://docs.bluedot.io/integrations/braze-integration/).

### Étape 3 : Authentifier le SDK de Bluedot
Utilisez le paramètre `projectId` créé à l'étape 1 pour authentifier le SDK Bluedot Point.

### Étape 4 : Utiliser les événements de Bluedot dans Braze

#### Déclenchement des messages

Vous pouvez déployer une campagne de notifications push ou un canvas qui agira à partir d'événements de localisation générés par le SDK Bluedot. Cette voie d'intégration est idéale pour l'envoi de messages en temps réel au moment où les utilisateurs entrent dans un emplacement qui les intéresse, ou pour une communication de suivi différée après leur départ.

Dans Braze, mettez en place une campagne basée sur des actions qui enverra des messages en fonction d'un emplacement défini. Pour votre déclencheur, utilisez un événement personnalisé de `bluedot_entry` ou `bluedot_exit` comme indiqué dans la capture d'écran suivante :

![Une campagne basée sur les actions dans l'étape de distribution. Ici, vous disposez de deux options de planification qui enverront la campagne si un utilisateur effectue un événement personnalisé `bluedot_entry` ou `bluedot_exit`.]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### Ciblage des utilisateurs

Veillez à cibler **Tous les utilisateurs** pour votre espace de travail.
![Une campagne basée sur l'action avec l'étape des utilisateurs cibles vous encourageant à sélectionner "Tous les utilisateurs" comme segmentation souhaitée.]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}

