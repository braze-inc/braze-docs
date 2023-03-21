---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
page_order: 3
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "Cet article de référence présente le partenariat entre Currents Braze et Microsoft Azure Blob Storage, une solution de stockage d’objets extrêmement évolutive pour les données non structurées."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) est une solution de stockage d’objets massivement évolutive pour les données non-structurées, proposée dans la suite de produits Azure de Microsoft.

L’intégration de Braze et de Microsoft Azure Blob Storage vous permet de réexporter des données vers Azure et de diffuser des données Currents. Vous pouvez ensuite utiliser un processus ETL (extraction, transformation et chargement) pour transférer vos données vers d’autres sites.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte de stockage Microsoft Azure et Azure | Un compte de stockage Microsoft Azure et Azure est requis pour profiter de ce partenariat. |
| Currents (facultatif) | Pour exporter des données dans Currents, vous devez avoir configuré [Currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Pour intégrer Microsoft Azure Blob Storage, vous devez disposer d’un compte de stockage et d’une chaîne de connexion pour permettre à Braze d’exporter des données vers Azure ou de diffuser des données Currents.

### Étape 1 : Créer un compte de stockage

Dans Microsoft Azure, accédez à **Storage Accounts (Comptes de stockage)** dans la barre latérale et cliquez sur **+ Add (+ Ajouter)** pour créer un nouveau compte de stockage. Ensuite, choisissez le nom de votre compte de stockage. Il n’est pas nécessaire de mettre à jour les autres paramètres par défaut. Enfin, cliquez sur **Review + create (Vérifier + Créer)**. 

Même si vous disposez déjà d’un compte de stockage, nous vous recommandons de créer un nouveau compte spécifiquement pour vos données Braze.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### Étape 2 : Obtenir une chaîne de connexion

Une fois le compte de stockage activé, accédez au menu **Access Keys (Clés d’accès)** de votre compte de stockage et notez la chaîne de connexion.

Microsoft fournit deux clés d’accès pour maintenir les connexions. Il utilise la première pendant que la deuxième est renouvelée. Vous n’avez besoin que de la chaîne de connexion de l’une des deux clés.

{% alert note %}
Braze utilise la chaîne de connexion fournie dans ce menu, et non pas la clé.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### Étape 3 : Créer un conteneur de service Blob

Accédez au menu **Blobs** sous la section **Blob Service (Service Blob)** de votre compte de stockage. Créez un conteneur de service Blob dans le compte de stockage que vous avez créé plus tôt. 

Donnez un nom à votre conteneur de service Blob. Il n’est pas nécessaire de mettre à jour les autres paramètres par défaut.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### Étape 4 : Choisir une méthode d’exportation

{% tabs %}
{% tab Currents %}
Dans Braze, accédez à **Currents > + Create Current (+ Créer un Current) > Azure Blob Data Export (Exportation de données Azure Blob)** et renseignez le nom de votre intégration et votre adresse e-mail.

Indiquez ensuite votre chaîne de connexion, le nom du conteneur et le préfixe BlobStorage (facultatif).

![Page Currents de Microsoft Azure Blob Storage dans Braze. Cette page comporte des champs pour le nom de l’intégration, l’adresse e-mail de contact, la chaîne de caractères de connexion, le nom du conteneur et le préfixe.]({% image_buster /assets/img/maz.png %})

Enfin, faites défiler jusqu’au bas de la page et sélectionnez les événements d’engagement par message ou les événements de comportement client que vous souhaitez exporter. Une fois terminé, lancez votre Current.

{% endtab %}
{% tab Azure data export %}
Dans Braze, accédez à **Technology Partners (Partenaires technologiques)** > **Microsoft Azure** et renseignez votre chaîne de connexion, le nom du conteneur de stockage Azure et le préfixe de stockage Azure.

Ensuite, assurez-vous que la case **Make this the default data export destination (Faire de cette destination la destination d’exportation de données par défaut)** est cochée, ce qui vous permettra de vérifier que vos données sont bien envoyées à Azure. Une fois terminé, enregistrez votre intégration.

![Page d’exportation des données Microsoft Azure dans Braze. Cette page comporte des champs pour la chaîne de caractères de connexion, le nom du conteneur et le préfixe.]({% image_buster /assets/img/azure_data_export.png %})

{% endtab %}
{% endtabs %}

{% alert important %}
Il est important de garder votre chaîne de connexion à jour : le connecteur cessera d’envoyer des événements si les informations d’identification de votre connecteur expirent. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}
