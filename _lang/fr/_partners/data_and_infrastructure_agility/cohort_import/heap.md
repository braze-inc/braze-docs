---
nav_title: Heap
article_title: Heap
page_order: 1
description: "Cet article de référence présente l’intégration entre Braze et Heap, une plateforme d’informations numériques qui vous permet d’importer des données de Heap vers Braze, de créer des cohortes d’utilisateurs et d’exporter des données de Braze vers Heap pour créer des segments."
alias: /partners/heap/
page_type: partner
search_tag: Partenaire

---

# Heap

> [Heap](https://heap.io/) est une plateforme d’informations numériques qui vous permet de vous concentrer sur les opportunités de votre expérience numérique qui ont le plus d’impact sur votre entreprise, d’éliminer les difficultés, de satisfaire vos clients et de générer plus rapidement des revenus.

L’intégration de Braze et de Heap vous permet d’[importer des données de Heap vers Braze](#data-import-integration), de créer des cohortes d’utilisateurs et d’[exporter des données de Braze vers Heap](#data-export-integration) pour créer des segments.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Heap | Un compte [Heap](https://heap.io/about) est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
| Currents Braze | Pour exporter des données de Braze vers Heap, vous devez avoir configuré [Currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation
1. Réengager les utilisateurs ayant abandonné un entonnoir : Déclenchez des envois de messages de réengagement lorsque des utilisateurs abandonnent l’entonnoir d’achat ou d’abonnement.
2. Personnaliser l’essai : Identifiez les points de friction de votre essai et envoyez des rappels correctement programmés pour réengager les utilisateurs pendant une période d’essai et les aider à en tirer de la valeur.
3. Stimuler l’engagement sur les annonces et les offres : Envoyez des messages ciblés contenant des promotions, des mises à jour et des annonces de nouveaux services aux audiences concernées.

## Intégration de l’importation de données

Utilisez l’intégration de Heap à Braze pour synchroniser automatiquement les cohortes créées dans Heap avec Braze.

### Étape 1 : Obtenir la clé d’importation des données Braze

Dans Braze, cliquez sur **Technology Partners (Partenaires technologiques)**, puis sélectionnez **Heap**. Sur cette page, vous trouverez votre clé d’importation des données et un endpoint REST. Notez ces deux valeurs et transmettez-les à votre gestionnaire de compte Heap pour terminer de configurer l’intégration. 

![][3]{: style="max-width:90%;"}

### Étape 2 : Segmenter des utilisateurs importés dans Braze

Dans Braze, accédez à **Segments**, nommez votre segment de cohorte Heap et sélectionnez **Heap Cohorts (Cohortes Heap)** comme filtre. Choisissez maintenant la cohorte Heap que vous souhaitez inclure. Une fois créé, vous pouvez sélectionner votre segment de cohorte Heap comme filtre d’audience au moment de créer une campagne ou un Canvas.

![Dans le générateur de segments de Braze, le filtre des attributs utilisateur « Heap Cohort (Cohorte Heap) » est défini sur « includes (inclut) » et « Heap Test Cohort (Cohort Heap de test) ».][2]{: style="max-width:90%;"}

### Comment utiliser cette intégration

Pour utiliser votre segment Heap, créez une campagne ou un Canvas Braze et sélectionnez le segment comme audience cible. 

![Dans le générateur de campagne Braze, à l’étape du ciblage, le filtre « Target users by segment (Cibler les utilisateurs par segment) » est défini sur « Heap Cohort (Cohorte Heap) ».][4]{: style="max-width:90%;"}

## Intégration de l’exportation de données

Utilisez Currents Braze pour envoyer automatiquement des événements d’engagement (par ex. E-mail envoyé, Notification push envoyée) de Braze vers Heap afin de les analyser.

### Étape 1 : Obtenir des informations d’identification Heap

Vous aurez besoin d’une URL d’endpoint de Webhook pour configurer cette intégration. Contactez votre gestionnaire de compte Heap pour obtenir cette URL.

### Étape 2 : Configurer Currents Braze

Dans Braze, accédez à **Currents** sous **Integrations (Intégrations)** et cliquez sur **Create New Current (Créer un nouveau Current)**, puis sélectionnez **Custom Currents Export (Exportation de Current personnalisée)**. Donnez un nom à votre exportation, puis passez à la page **Current Details (Détails du Current)**. Sur cette page, vous devez saisir l’endpoint et le jeton du porteur facultatif (si fourni).

Après avoir configuré les informations d’identification de votre intégration, vérifiez tous les événements d’engagement par message, de comportement des clients et utilisateurs que vous souhaitez exporter vers Heap, puis cliquez sur **Launch Current (Lancer le Current)**.

![][5]{: style="max-width:90%;"}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/heap/heap1.png %} 
[3]: {% image_buster /assets/img/heap/heap2.png %} 
[4]: {% image_buster /assets/img/heap/heap3.png %} 
[5]: {% image_buster /assets/img/heap/heap4.png %} 
