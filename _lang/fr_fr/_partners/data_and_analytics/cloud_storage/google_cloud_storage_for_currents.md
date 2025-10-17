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

{% alert important %}
Si vous passez d'un fournisseur de stockage en nuage à un autre, contactez votre gestionnaire satisfaction client Braze pour obtenir de l'aide sur la configuration et la validation de votre nouvelle intégration.
{% endalert %}

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

![]({% image_buster /assets/img/gcs1.png %})

Donnez un nom au rôle, puis sélectionnez **+Ajouter des autorisations** et choisissez les éléments suivants :

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
L'autorisation `storage.objects.delete` est facultative. Il permet à Braze de nettoyer les fichiers incomplets.<br><br>Dans de rares circonstances, Google Cloud peut mettre fin aux connexions de manière anticipée, ce qui entraîne l'écriture par Braze de fichiers incomplets sur Google Cloud Storage. Dans la plupart des cas, Braze fera une nouvelle tentative et créera un nouveau fichier avec les données correctes, laissant l'ancien fichier dans Google Cloud Storage.
{% endalert %}

Lorsque vous avez terminé, sélectionnez **Créer**.

![]({% image_buster /assets/img/gcs2.png %})

### Étape 2 : Créer un nouveau compte de service

#### Étape 2.1 : Créer le compte de service

Créez un nouveau compte de service dans votre console Google Cloud Platform en naviguant vers **IAM & admin** > **Comptes de service** et en sélectionnant **Créer un compte de service**.

![]({% image_buster /assets/img/gcs3.png %})

Ensuite, donnez un nom au compte de service et accordez-lui l'accès à votre rôle personnalisé nouvellement créé.

![Dans Google Cloud Platform, sur la page de création de services, saisissez le nom de votre rôle dans le champ "Sélectionner un rôle".]({% image_buster /assets/img/gcs4.png %})

#### Étape 2.2 : Créer une clé

En bas de la page, utilisez le bouton **Créer une clé** pour créer une clé privée **JSON** à utiliser dans Braze. Une fois la clé créée, elle sera téléchargée sur votre machine.

![]({% image_buster /assets/img/gcs5.png %})

### Étape 3 : Configurer des flux Currents dans Braze

Dans Braze, naviguez vers **Currents** > **\+ Créer un flux Currents** > **Exportation des données de Google Cloud Storage** et indiquez votre nom d'intégration et votre e-mail de contact.

Ensuite, téléchargez votre clé privée JSON sous **Identifiants GCS JSON** et indiquez le nom de votre compartiment CGS et le préfixe GCS (facultatif). 

{% alert important %}
Il est important de maintenir votre fichier d'informations d'identification à jour ; si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

![La page Currents Google Cloud Storage dans Braze. Cette page contient des champs pour le nom de l'intégration, l'e-mail du contact, l'identifiant JSON GCS, le nom du compartiment GCS et le préfixe.]({% image_buster /assets/img/gcs6.png %})

Enfin, faites défiler la page vers le bas et sélectionnez les événements d'engagement des messages ou les événements de comportement des clients que vous souhaitez exporter. Une fois l'opération terminée, lancez votre flux Currents.

### Étape 4 : Configurer les exportations de Google cloud storage

Pour configurer les exportations Google Cloud Storage (GCS), accédez à **Partenaires technologiques** > **Google Cloud Storage**, saisissez vos identifiants GCS et sélectionnez **Faire de cette destination la destination d'exportation de données par défaut**.

Gardez à l'esprit que l'organisation et le contenu de tout fichier exporté seront identiques entre les intégrations AWS S3, Microsoft Azure et Google Cloud Storage.

{% alert important %}
Veillez à saisir la valeur JSON complète [générée par Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete).
{% endalert %}

![La page Google cloud storage dans le bord de bord de Braze.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### Étape 5 : Testez les informations d'identification de votre compte de service (facultatif)

Votre compte de service Google Cloud IAM doit disposer des autorisations suivantes :

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Pour vérifier ces autorisations dans le tableau de bord de Braze, accédez à la page **Google Cloud Storage**, puis sélectionnez **Tester les informations d'identification**.

![La section des informations d'identification de Google Cloud Storage dans le tableau de bord de Braze.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Comportement à l'exportation

Les utilisateurs qui ont intégré une solution de stockage de données en nuage et qui tentent d'exporter des API, des rapports de tableau de bord ou des rapports CSV rencontreront le problème suivant :

- Toutes les exportations API ne renvoient pas d'URL de téléchargement dans le corps de la réponse et doivent être récupérées via le stockage de données.
- Tous les rapports des tableaux de bord et les rapports CSV seront envoyés à l'e-mail de l'utilisateur pour être téléchargés (aucune autorisation de stockage n'est requise) et sauvegardés sur le stockage de données.

## Résolution des problèmes

### Les informations d'identification de Google Cloud Storage ne sont pas valides.

Si vous recevez l'erreur suivante lorsque vous tentez d'entrer vos données d'identification :

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Assurez-vous que votre compte de service Google Cloud IAM dispose des autorisations suivantes :

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Après vérification, vous pouvez [tester vos informations d'identification dans le tableau de bord de Braze](#step-5-test-your-service-account-credentials-optional).
