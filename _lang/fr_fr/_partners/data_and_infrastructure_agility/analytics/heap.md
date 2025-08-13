---
nav_title: Heap
article_title: "Analyse Heap"
description: "Cet article de référence explique comment utiliser Braze Currents pour analyser automatiquement les événements d'engagement avec Heap, une plateforme d'informations numériques, qui vous permet d'importer des données Heap dans Braze, de créer des cohortes d'utilisateurs et d'exporter des données Braze vers Heap pour créer des segments."
page_type: partner
search_tag: Partner


---

# Analyse Heap

> Cet article explique comment envoyer automatiquement des événements d'engagement de Braze à Heap pour analyse. Pour plus d'informations sur l'intégration de Heap et de ses autres fonctionnalités, telles que la [synchronisation des cohortes Heap]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/#data-import-integration) avec Braze, consultez [l'article principal de Heap]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/).

## Intégration de l'exportation de données

Utilisez Braze Currents pour envoyer automatiquement les événements d'engagement (par exemple, e-mail envoyé, envoi push) de Braze à Heap pour analyse.

### Étape 1 : Obtenir des informations d'identification Heap

Vous aurez besoin d'une URL d’endpoint de webhook pour configurer cette intégration, que vous pouvez obtenir auprès de votre gestionnaire de compte Heap.

### Étape 2 : Configurer Braze Currents

Dans Braze, accédez à **Intégrations partenaires** > **Exporter les données**, cliquez sur **Créer un nouveau flux Current**, puis sélectionnez **Export Heap**. 

Donnez un nom à votre export, puis passez à la page **Détails du flux Current**. Sur cette page, entrez l'endpoint et le jeton porteur facultatif (s'il est fourni).

Après avoir configuré les informations d'identification de votre intégration, vérifiez l'engagement des messages, le comportement des clients et les événements utilisateur que vous souhaitez exporter vers Heap, puis cliquez sur **Launch Current**.

![][5]{: style="max-width:90%;"}

[5]: {% image_buster /assets/img/heap/heap4.png %} 
