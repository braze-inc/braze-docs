---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "Cet article de référence présente le partenariat entre Braze et Google Cloud Storage, une solution de stockage d’objets très évolutive pour les données non structurées."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/) est un système de stockage d’objets très évolutif pour les données non structurées proposé par Google dans la suite de produits Cloud Computing.

L'intégration de Braze et Google Cloud Storage vous permet de transmettre  en continu  les données Currents vers Google Cloud Storage. Vous pouvez par la suite utiliser un processus ETL (extraction, transformation et chargement) pour transférer vos données vers d'autres emplacements, comme Google BigQuery.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Google Cloud Storage | Un compte Google Cloud Storage est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour pouvoir réexporter des données dans Google Cloud Storage, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Pour intégrer Google Cloud Storage, vous devez configurer les informations d'identification appropriées qui permettent à Braze d'obtenir des informations sur les compartiments de stockage en cours d'écriture (`storage.buckets.get`) et de créer des objets dans ce compartiment (`storage.objects.create`). 

Pour ce faire, suivez les instructions suivantes, qui vous guideront dans la création d'un rôle et d'un compte de service qui généreront une clé privée à utiliser dans votre intégration currents.

### Étape 1 : Créer un rôle

Créez un nouveau rôle dans votre console Google Cloud Platform en naviguant vers **IAM & admin** > **Rôles** > **\+ Créer un rôle.**

![][2]

Ensuite, donnez un nom au rôle, sélectionnez **+Add Permissions** et ajoutez les éléments suivants : `storage.buckets.get`, `storage.objects.create`, et `storage.objects.get`. Sélectionnez ensuite **Créer**.

Si vous le souhaitez, ajoutez des autorisations `storage.objects.delete` pour permettre à Braze de nettoyer les fichiers incomplets. Dans de rares circonstances, Google Cloud peut mettre fin aux connexions de manière anticipée, ce qui entraîne l'écriture par Braze de fichiers incomplets sur Google Cloud Storage. Dans des circonstances normales, Braze fera une nouvelle tentative et créera un nouveau fichier avec les données correctes, laissant l'ancien fichier dans Google Cloud Storage.

![][3]

### Étape 2 : Créer un compte de service

Créez un nouveau compte de service dans votre console Google Cloud Platform en naviguant vers **IAM & admin** > **Comptes de service** et en sélectionnant **Créer un compte de service**.

![][4]

Ensuite, donnez un nom au compte de service et accordez-lui l'accès à votre rôle personnalisé nouvellement créé.

![Dans la plateforme Google Cloud, la page de création de services, saisissez le nom de votre rôle dans le champ "Sélectionner un rôle".][5]

#### Créer une clé

En bas de la page, utilisez le bouton **Créer une clé** pour créer une clé privée **JSON** à utiliser dans Braze. Une fois la clé créée, elle sera téléchargée sur votre machine.

![][6]

### Étape 3 : Configurer des flux Currents dans Braze

Dans Braze, naviguez vers **Currents** > **\+ Créer un flux Currents** > **Exportation des données de Google Cloud Storage** et indiquez votre nom d'intégration et votre e-mail de contact.

Ensuite, téléchargez votre clé privée JSON sous **Identifiants GCS JSON** et indiquez le nom de votre compartiment CGS et le préfixe GCS (facultatif). 

{% alert important %}
Il est important de maintenir votre fichier d'informations d'identification à jour ; si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

![La page Currents Google Cloud Storage dans Braze. Cette page comporte des champs permettant de spécifier le nom de l'intégration, l'e-mail du contact, l'identifiant JSON GCS, le nom du compartiment GCS et le préfixe.][7]

Enfin, faites défiler la page vers le bas et sélectionnez les événements d'engagement des messages ou les événements de comportement des clients que vous souhaitez exporter. Une fois l'opération terminée, lancez votre flux Currents.

### Étape 4 : Configurer des exportations de Google Cloud Storage (GCS)

Pour configurer les exportations Google Cloud Storage (GCS), accédez à **Partenaires technologiques** > **Google Cloud Storage**, saisissez vos identifiants GCS et sélectionnez **Faire de cette destination la destination d'exportation de données par défaut**.

{% alert tip %}
Vos **informations d'identification GCS JSON** sont générées en suivant les étapes de la [documentation de Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete). Veillez à saisir l'intégralité de la valeur JSON générée.
{% endalert %}

![La page Google Cloud Storage dans le tableau de bord de Braze.][8]{: style="max-width:70%;"}

Votre compte de service Google Cloud IAM correspondant doit disposer des autorisations suivantes (vous pouvez le confirmer en sélectionnant le bouton **Tester les informations d'identification sur** la page **Google Cloud Storage** dans Braze) :
- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.get`
- `storage.objects.list`

L'organisation et le contenu de tout fichier exporté seront identiques dans les intégrations AWS S3, Microsoft Azure et Google Cloud Storage.

## Comportement à l'exportation

Les utilisateurs qui ont intégré une solution de stockage de données en nuage et qui tentent d'exporter des API, des rapports de tableau de bord ou des rapports CSV rencontreront le problème suivant :

- Toutes les exportations API ne renvoient pas d'URL de téléchargement dans le corps de la réponse et doivent être récupérées via le stockage de données.
- Tous les rapports des tableaux de bord et les rapports CSV seront envoyés à l'e-mail de l'utilisateur pour être téléchargés (aucune autorisation de stockage n'est requise) et sauvegardés sur le stockage de données. 

[2]: {% image_buster /assets/img/gcs1.png %}
[3]: {% image_buster /assets/img/gcs2.png %}
[4]: {% image_buster /assets/img/gcs3.png %}
[5]: {% image_buster /assets/img/gcs4.png %}
[6]: {% image_buster /assets/img/gcs5.png %}
[7]: {% image_buster /assets/img/gcs6.png %}
[8]: {% image_buster /assets/img/gcs7.png %}
