---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "Cet article de référence décrit le partenariat entre Braze Currents et Microsoft Azure Blob Storage, un stockage d'objets massivement évolutif pour les données non structurées."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) est un stockage d'objets massivement évolutif pour les données non structurées offert par Microsoft dans le cadre de la suite de produits Azure.

L'intégration de Braze et Microsoft azure Blob Storage vous permet de réexporter des données vers Azure et de diffuser des données Currents. Plus tard, vous pouvez utiliser un processus ETL (extraire, transformer, charger) pour transférer vos données vers d'autres emplacements.

## Prérequis

| Condition | Descriptif |
| ----------- | ----------- |
| Microsoft Azure et compte de stockage Azure | Un compte Microsoft Azure et de stockage Azure est nécessaire pour tirer parti de ce partenariat. |
| Currents | Pour exporter des données vers Currents, vous devez avoir [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configuré pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Pour intégrer Microsoft Azure Blob Storage, vous devez avoir un compte de stockage et une chaîne de caractères de connexion pour permettre à Braze soit d'exporter des données vers Azure, soit de diffuser des données Currents.

### Étape 1 : Créer un compte de stockage

Dans Microsoft azure, accédez à **Comptes de stockage** dans la barre latérale et cliquez sur **\+ Ajouter** pour créer un nouveau compte de stockage. Ensuite, fournissez un nom de compte de stockage. Les autres paramètres par défaut n'auront pas besoin d'être mis à jour. Enfin, sélectionnez **Revoir + créer**. 

Même si vous avez déjà un compte de stockage, nous vous recommandons d'en créer un nouveau spécifiquement pour vos données Braze.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### Étape 2 : Obtenez la chaîne de connexion

Une fois le compte de stockage déployé, accédez au menu **Clés d'accès** depuis le compte de stockage et notez la chaîne de caractères de connexion.

Microsoft fournit deux clés d'accès pour maintenir les connexions en utilisant une clé tout en régénérant l'autre. Vous n'avez besoin que de la chaîne de connexion de l'un d'eux.

{% alert note %}
Braze utilise la chaîne de caractères de connexion de ce menu, pas la clé.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### Étape 3 : Créer un conteneur de service blob

Accédez au menu **Blobs** dans la section **Blob Service** de votre compte de stockage. Créez un conteneur de service Blob dans le compte de stockage précédemment créé. 

Fournissez un nom pour votre conteneur de service Blob. Les autres paramètres par défaut n'auront pas besoin d'être mis à jour.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### Étape 4 : Configurer Currents

Dans Braze, accédez à **Currents > + Créer un flux Current > Exporter des données Azure Blob** et fournissez le nom de votre intégration et l'e-mail de contact.

Ensuite, fournissez votre chaîne de connexion, le nom du conteneur et le préfixe BlobStorage (facultatif).

![La page Currents du stockage Blob Microsoft Azure dans Braze. Cette page contient des champs permettant de spécifier le nom de l'intégration, l'e-mail de contact, la chaîne de connexion, le nom du conteneur et le préfixe.]({% image_buster /assets/img/maz.png %})

Enfin, faites défiler l’écran jusqu'en bas de la page et sélectionnez les événements d'engagement de message ou les événements de comportement des clients que vous souhaitez exporter. Une fois terminé, lancez votre Current.

### Étape 5 : Configurer l'exportation de données Azure

La configuration suivante configure les informations d'identification utilisées pour :
1. Les exports de segment via l'API
2. Exportations CSV (campagne, segment, exportation de données utilisateur Canvas via le tableau de bord)
3. rapports d'engagement

Dans Braze, accédez à **Intégrations de partenaires** > **Partenaires technologiques** > **Microsoft Azure** et spécifiez votre chaîne de caractères de connexion, le nom du conteneur de stockage Azure et le préfixe de stockage Azure.

Ensuite, assurez-vous que la case **Définir comme destination d'exportation des données par défaut** est cochée afin que vos données exportées soit envoyées à Azure. Lorsque vous avez terminé, enregistrez votre intégration.

![La page d'exportation des données Microsoft Azure dans Braze. Cette page contient des champs permettant de spécifier la chaîne de connexion, le nom du conteneur et le préfixe.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
Il est important de maintenir votre chaîne de connexion à jour ; si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cela persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

## Comportement à l'exportation

Les utilisateurs qui ont intégré une solution de stockage de données en nuage et qui tentent d'exporter des API, des rapports de tableau de bord ou des rapports CSV rencontreront le problème suivant :

- Toutes les exportations d'API ne renverront pas d'URL de téléchargement dans le corps de la réponse et doivent être récupérées via le stockage des données.
- Tous les rapports de tableau de bord et les rapports CSV seront envoyés à l'e-mail de l'utilisateur pour téléchargement (aucune autorisation de stockage requise) et sauvegardés sur le stockage de données. 
