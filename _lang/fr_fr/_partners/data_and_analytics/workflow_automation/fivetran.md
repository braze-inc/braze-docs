---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Cet article de référence présente le partenariat entre Braze et Fivetran, un outil d'automatisation des flux de travail qui peut vous aider dans la prise de décision adossée aux données en fournissant des données prêtes à être interrogées dans votre entrepôt cloud."
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/) est une marque mondialement reconnue dont les produits axés sur l'analyse et les pipelines entièrement gérés permettent de prendre des décisions fondées sur des données en fournissant des données prêtes à être interrogées dans votre entrepôt en nuage.

L'intégration de Braze et Fivetran permet aux utilisateurs de créer un pipeline sans maintenance qui vous permet de collecter et d'analyser les données de Braze en connectant toutes vos applications et bases de données à un entrepôt central. Une fois les données collectées dans l'entrepôt central, les équipes chargées des données peuvent explorer efficacement les données de Braze à l'aide de leurs outils d'aide à la décision préférés. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Fivetran | Un compte [Fivetran](https://fivetran.com/login?next=%2Fdashboard) est nécessaire pour bénéficier de ce partenariat. |
| Clé d'API REST Braze | Une clé API REST de Braze avec les autorisations suivantes :<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#api-definitions). |
| Braze Currents | [Braze Currents](https://www.braze.com/product/data-agility-management/currents/) doit être connecté à Amazon S3 ou à Google Cloud Storage. |
| Amazon S3 ou Google Cloud Storage | Cette intégration nécessite que vous ayez accès à un service Amazon S3 ou à Google Cloud Storage. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Intégration

L'intégration Currents suivante est prise en charge pour [Amazon S3](#setting-up-braze-currents-for-s3) et [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage).

### Mise en place des Braze Currents pour S3

#### Étape 1 : Rechercher votre ID externe {#step-one}

Dans le [tableau de bord Fivetran](https://fivetran.com/dashboard), sélectionnez **\+ Connecteur**, puis le connecteur **Braze** pour lancer le formulaire de configuration. Ensuite, sélectionnez **Amazon S3**. Notez l'ID externe fourni ici ; vous en aurez besoin pour permettre à Fivetran d'accéder à votre compartiment S3. 

![Le Fivetran a configuré un formulaire de connecteur Braze. Le champ de l'ID externe nécessaire à cette étape est situé au milieu de la page dans un cadre gris clair.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### Étape 2 : Donner à Fivetran l'accès à un compartiment S3 spécifié.

##### Création d'une politique IAM

Ouvrez la [console Amazon IAM](https://console.aws.amazon.com/iam/home#home) et naviguez vers **Politiques > Créer une politique.**

![Console Amazon IAM avec liste des politiques.]({% image_buster /assets/img/fivetran_as3_iam.png %})

Ensuite, ouvrez l'onglet **JSON** et collez la politique suivante. Veillez à remplacer `{your-bucket-name}` par le nom de votre compartiment S3.

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

Enfin, sélectionnez **Réviser** la politique et donnez-lui un nom et une description uniques. Sélectionnez **Créer une politique** pour créer votre politique. 

![Champs pour nommer la politique et fournir une description.]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### Créer un rôle IAM {#step-two}

Dans AWS, accédez à **Rôles**, puis sélectionnez **Créer un nouveau rôle**.

![La page "Rôles" avec le bouton pour créer un nouveau rôle.]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Sélectionnez **un autre compte AWS** et indiquez l'ID du compte Fivetran `834469178297`. Veillez à cocher la case **Require external ID.** Vous y indiquerez l'ID externe trouvé à l'étape 1.

![Le champ pour saisir votre "Account ID", une case à cocher pour exiger l'ID externe et une zone de texte vide pour saisir votre "ID externe".]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Ensuite, sélectionnez **Next : Permissions** pour sélectionner la politique que vous venez de créer.

![Liste des politiques.]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Sélectionnez **Next : Consultez le site**, donnez un nom à votre nouveau rôle (par exemple Fivetran) et sélectionnez **Créer un rôle**. Une fois le rôle créé, sélectionnez-le et notez l'ARN du rôle affiché.

![L'ARN Amazon S3 indiqué dans le rôle.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Vous pouvez spécifier des autorisations pour l'ARN de rôle que vous désignez pour Fivetran. L'attribution d'autorisations sélectives à ce rôle permet à Fivetran de synchroniser uniquement ce qu'il a le droit de voir.
{% endalert %}

#### Étape 3 : Complétez le connecteur Fivetran

Dans Fivetran, sélectionnez **\+ Connecteur**, puis le connecteur **Braze** pour lancer le formulaire de configuration. Dans le formulaire, remplissez les champs donnés avec les valeurs appropriées :
- `Destination schema`: Un nom de schéma unique.
- `API URL`: Votre endpoint de l'API REST de Braze.
- `API Key`: Votre clé API REST de Braze. 
- `External ID`: L'ID externe défini à l'[étape 2](#step-two) des instructions de configuration de Currents. Cet ID est une valeur fixe.
- `Bucket` : Vous le trouverez dans votre compte Braze en naviguant vers **Intégrations partenaires** > **Exportation de données** > votre nom actuel.
- `Role ARN` : L'ARN du rôle se trouve à l'[étape 1](#step-one) des instructions relatives à la configuration actuelle.

{% alert important %}
Assurez-vous qu'**Amazon S3** est sélectionné comme choix de **stockage en nuage**.
{% endalert %}

Enfin, sélectionnez **Enregistrer et tester**, et Fivetran fera le reste en se synchronisant avec les données de votre compte Braze !

### Configuration de Braze Currents pour Google Cloud Storage

#### Étape 1 : Récupérer vos e-mails Fivetran dans Google Cloud Storage {#step-one2}

Dans le [tableau de bord Fivetran](https://fivetran.com/dashboard), sélectionnez **\+ Connecteur**, puis le connecteur **Braze** pour lancer le formulaire de configuration. Ensuite, sélectionnez le **stockage dans le nuage de Google**. Notez l'adresse e-mail qui apparaît.

![Le Fivetran a configuré un formulaire de connecteur Braze. Le champ de l'e-mail nécessaire à cette étape est situé au milieu de la page dans une boîte gris clair.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### Étape 2 : Accorder l'accès au compartiment

Accédez à votre [Google Storage Console](https://console.cloud.google.com/storage/browser) et sélectionnez le compartiment avec lequel vous avez configuré Braze Currents, puis sélectionnez **Modifier les autorisations du compartiment**.

![Les compartiments disponibles de la console de Google Storage. Localisez un compartiment et sélectionnez l'icône verticale à trois points pour ouvrir le menu déroulant qui vous permet de modifier les emplacements du compartiment.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

Ensuite, accordez à `Storage Object Viewer` l'accès à l'e-mail de l'[étape 1](#step-one2) en ajoutant l'e-mail en tant que membre. Notez le nom du compartiment ; vous en aurez besoin à l'étape suivante pour configurer Fivetran.

![Seau avec autorisations.]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### Étape 3 : Complétez le connecteur Fivetran

Dans Fivetran, sélectionnez **\+ Connecteur**, puis le connecteur **Braze** pour lancer le formulaire de configuration. Dans le formulaire, remplissez les champs donnés avec les valeurs appropriées :
- `Destination schema`: Un nom de schéma unique.
- `API URL`: Votre endpoint de l'API REST de Braze.
- `API Key`: Votre clé API REST de Braze. 
- `Bucket Name` : Vous le trouverez dans votre compte Braze en naviguant vers **Intégrations partenaires** > **Exportation de données** > votre nom actuel.
- `Folder` : Vous le trouverez dans votre compte Braze en naviguant vers **Intégrations partenaires** > **Exportation de données** > votre nom actuel.

{% alert important %}
Assurez-vous que **Google cloud storage** est sélectionné comme choix de **stockage dans le nuage**.
{% endalert %}

Enfin, sélectionnez **Enregistrer et tester**, et Fivetran fera le reste en se synchronisant avec les données de votre compte Braze !

