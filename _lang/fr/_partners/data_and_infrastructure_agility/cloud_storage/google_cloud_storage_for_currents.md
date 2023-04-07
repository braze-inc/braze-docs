---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
page_order: 2
alias: /partners/google_cloud_storage_for_currents/
description: "Cet article de référence présente le partenariat entre Braze et Google Cloud Storage, une solution de stockage d’objets extrêmement évolutive pour les données non structurées."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/) est une solution de stockage d’objets extrêmement évolutive pour les données non structurées, qui est proposée par Google dans le cadre de sa suite de produits Cloud Computing.

L’intégration de Braze et de Google Cloud Storage vous permet de diffuser des données Currents vers Google Cloud Storage. Vous pouvez ensuite utiliser un processus ETL (extraction, transformation et chargement) pour transférer vos données vers d’autres sites, comme Google BigQuery.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Google Cloud Storage | Un compte Google Cloud Storage est requis pour profiter de ce partenariat. |
| Currents | Pour réexporter des données dans Google Cloud Storage, vous devez avoir configuré [Currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Pour intégrer Google Cloud Storage, vous devez configurer les informations d’identification appropriées afin de permettre à Braze d’obtenir des informations sur les compartiments de stockage dans lesquels il écrit des données (`storage.buckets.get`) et de créer des objets dans ce compartiment (`storage.objects.create`). 

Les instructions ci-dessous vous aideront à créer un rôle et un compte de service qui généreront une clé privée à utiliser dans votre intégration Currents.

### Étape 1 : Créer un rôle

Créez un nouveau rôle dans votre Google Cloud Platform Console en accédant à **IAM & Admin > Roles (Rôles) > + Create Role (+ Créer un rôle)**.

![][2]

Ensuite, donnez un nom à votre rôle, cliquez sur **+Add Permissions (+ Ajouter des autorisations)** et ajoutez `storage.buckets.get` et `storage.objects.create`, puis cliquez sur **Create (Créer)**.

Ajoutez éventuellement des autorisations `storage.objects.delete` pour permettre à Braze de nettoyer les fichiers incomplets. Dans de rares circonstances, Google Cloud peut interrompre les connexions prématurément, ce qui oblige Braze à écrire des fichiers incomplets sur Google Cloud Storage. Dans des circonstances normales, Braze réessayera et créera un nouveau fichier avec les données correctes, laissant l'ancien fichier dans Google Cloud Storage.

![][3]

### Étape 2 : Créer un compte de service

Créez un nouveau compte de service dans votre Google Cloud Platform Console en accédant à **IAM & Admin > Service Accounts (Comptes de service)** et en sélectionnant **Create Service Account (Créer un compte de service)**.

![][4]

Ensuite, donnez un nom à votre compte de service et accordez-lui un accès à votre nouveau rôle personnalisé.

![Dans la plateforme Google Cloud, sur la page « Create Service (Créer un service) », saisissez le nom de votre rôle dans le champ « Select a Role (Sélectionner un rôle) ».][5]

#### Créer une clé

Au bas de la page, cliquez sur le bouton **Create Key (Créer une clé)** pour créer une clé privée **JSON** à utiliser dans Braze. Une fois créée, cette clé sera téléchargée sur votre ordinateur.

![][6]

### Étape 3 : Configurer Currents dans Braze

Dans Braze, accédez à **Currents > + Create Current (+ Créer un Current) > Google Cloud Storage Data Export (Exportation de données Google Cloud Storage)** et renseignez le nom de votre intégration et votre adresse e-mail.

Téléchargez ensuite votre clé privée JSON dans **GCS JSON Credentials (Informations d’identification JSON pour GCS)** et renseignez le nom de votre compartiment GCS et le préfixe GCS (facultatif). 

{% alert important %}
Il est important de garder vos informations d’identification à jour : le connecteur cessera d’envoyer des événements si les informations d’identification de votre connecteur expirent. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}

![La page Google Cloud Storage de Currents dans Braze. Cette page comporte des champs pour le nom de l’intégration, l’adresse e-mail de contact, les informations d’identification JSON pour GCS, le nom du compartiment GCS et le préfixe.][7]

Enfin, faites défiler jusqu’au bas de la page et sélectionnez les événements d’engagement par message ou les événements de comportement client que vous souhaitez exporter. Une fois terminé, lancez votre Current.

[2]: {% image_buster /assets/img/gcs1.png %}
[3]: {% image_buster /assets/img/gcs2.png %}
[4]: {% image_buster /assets/img/gcs3.png %}
[5]: {% image_buster /assets/img/gcs4.png %}
[6]: {% image_buster /assets/img/gcs5.png %}
[7]: {% image_buster /assets/img/gcs6.png %}
