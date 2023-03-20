---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Cet article de référence présente le partenariat entre Braze et Fivetran, un outil d’automatisation de workflow qui vous aide à baser votre prise de décision sur les données en envoyant des données interrogeables dans votre entrepôt cloud."
page_type: partner
search_tag: Partenaire
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/) est une marque reconnue dans le monde entier dont les produits axés sur les analystes et les pipelines entièrement gérés permettent d’utiliser les données pour prendre des décisions éclairées en envoyant des données interrogeables dans votre entrepôt cloud.

L’intégration de Braze et Fivetran vous permet de créer un pipeline sans maintenance pour collecter et analyser les données de Braze en connectant toutes vos applications et bases de données à un entrepôt central. Une fois ces données collectées dans l’entrepôt, les équipes de données peuvent explorer efficacement les données de Braze en utilisant leurs outils d’aide à la décision préférés. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Fivetran | Un compte [Fivetran](https://fivetran.com/login?next=%2Fdashboard) est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé API REST Braze avec les autorisations suivantes :<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][1]. |
| Currents Braze | [Currents Braze](https://www.braze.com/product/data-agility-management/currents/) doit être connecté à Amazon S3 ou Google Cloud Storage. |
| Amazon S3 ou Google Cloud Storage | Cette intégration nécessite un compte Amazon S3 ou Google Cloud Storage. |
{: .reset-td-br-1 .reset-td-br-2} 

## Intégration

L’intégration Currents suivante est prise en charge pour [Amazon S3](#setting-up-braze-currents-for-s3) et [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage).

### Configuration de Currents Braze pour S3

#### Étape 1 : Localiser votre ID externe {#step-one}

Dans le [Tableau de bord de Fivetran](https://fivetran.com/dashboard), cliquez sur **+ Connector (+ Connecteur)** et sélectionnez le connecteur **Braze** pour lancer le formulaire de configuration. Ensuite, sélectionnez **Amazon S3**. Notez l’ID externe qui vous est fourni ici ; vous en aurez besoin pour permettre à Fivetran d’accéder à votre compartiment S3. 

![Le formulaire du connecteur Braze de la configuration Fivetran. Le champ ID externe requis pour cette étape se trouve au milieu de la page dans une zone gris clair.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### Étape 2 : Permettre à Fivetran d’accéder à un compartiment S3 désigné

##### Création d’une politique IAM

Ouvrez la [Console Amazon IAM](https://console.aws.amazon.com/iam/home#home) et accédez à **Policies (Politiques) > Create Policy (Créer une politique)**.

![]({% image_buster /assets/img/fivetran_as3_iam.png %})

Ensuite, cliquez sur l’onglet **JSON** et copiez-collez la politique suivante. Assurez-vous de remplacer `{your-bucket-name}` par le nom de votre compartiment S3.

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

Ensuite, cliquez sur **Review Policy (Vérifier la politique)** et ajoutez un nom et une description unique pour la politique. Cliquez sur **Create Policy (Créer une politique)** pour créer votre politique. 

![]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### Créer un rôle IAM {#step-two}

Dans AWS, accédez à **Roles (Rôles)**, puis sélectionnez **Create New Role (Créer un nouveau rôle)**.

![]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Sélectionnez **Another AWS Account (Autre compte AWS)** et renseignez l’ID de compte Fivetran `834469178297`. Assurez-vous de cocher la case **Require external ID (Exiger un ID externe)**. Ici, vous renseignerez l’ID externe fourni à l’étape 1.

![]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Ensuite, cliquez sur **Next: Permissions (Suivant : Autorisations)** pour sélectionner la politique que vous venez de créer.

![]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Cliquez sur **Next: Review (Suivant : Vérification)**, nommez votre nouveau rôle (c.-à-d. Fivetran), puis cliquez sur **Create Role (Créer un rôle)**. Enfin, cliquez sur le rôle que vous venez de créer et notez l’ARN du rôle qui s’affiche.

![L’ARN Amazon S3 répertorié dans le rôle.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Vous pouvez ajouter des autorisations à l’ARN du rôle que vous désignez pour Fivetran. Le fait d’accorder des autorisations limitées à ce rôle permettra à Fivetran de synchroniser uniquement ce que vous l’avez autorisé à voir.
{% endalert %}

#### Étape 3 : Terminer le connecteur Fivetran

Dans Fivetran, cliquez sur **+ Connector (+ Connecteur)** et sélectionnez le connecteur **Braze** pour lancer le formulaire de configuration. Remplissez les champs indiqués dans le formulaire avec les valeurs appropriées :
- `Destination schema` : un nom de schéma unique.
- `API URL` : votre endpoint d’API REST Braze.
- `API Key` : votre clé API REST Braze. 
- `External ID` : L’ID externe défini à l’[étape 2](#step-two) des instructions de configuration de Currents. Cet ID est une valeur fixe.
- `Bucket` : disponible dans votre compte Braze en accédant à **Integration (Intégration) > Currents > [Your Current name (Nom de votre Current)] > Bucket Name (Nom du compartiment)**.
- `Role ARN` : L’ARN du rôle peut être trouvé à l’[étape 1](#step-one) des instructions de configuration de Current.

{% alert important %}
Assurez-vous qu’**Amazon S3** est sélectionné en tant que **Cloud Storage (Stockage cloud)**.
{% endalert %}

Enfin, cliquez sur **Save & Test (Enregistrer et tester)**, et Fivetran se chargera du reste en synchronisant les données de votre compte Braze !

### Configuration de Currents Braze pour Google Cloud Storage

#### Étape 1 : Récupérez votre adresse e-mail Fivetran à partir de Google Cloud Storage {#step-one2}

Dans le [Tableau de bord de Fivetran](https://fivetran.com/dashboard), cliquez sur **+ Connector (+ Connecteur)** et sélectionnez le connecteur **Braze** pour lancer le formulaire de configuration. Ensuite, sélectionnez **Google Cloud storage**. Notez l’adresse e-mail qui apparaît.

![Le formulaire du connecteur Braze de la configuration Fivetran. Le champ e-mail nécessaire à cette étape est situé au milieu de la page dans une zone gris clair.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### Étape 2 : Accorder l’accès au compartiment

Accédez à votre [Console Google Storage](https://console.cloud.google.com/storage/browser) et sélectionnez le compartiment avec lequel vous avez configuré Currents Braze, puis cliquez sur **Edit bucket permissions (Modifier les autorisations du compartiment)**.

![Les compartiments disponibles de la console Google Storage. Recherchez un compartiment et cliquez sur les trois points verticaux pour ouvrir le menu déroulant qui vous permet de modifier les autorisations de compartiment.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

Ensuite, accordez un accès `Storage Object Viewer` à l’adresse e-mail de l’[étape 1](#step-one2) en ajoutant l’adresse en tant que membre. Notez le nom du compartiment ; vous en aurez besoin pour configurer Fivetran lors de l’étape suivante.

![]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### Étape 3 : Terminer le connecteur Fivetran

Dans Fivetran, cliquez sur **+ Connector (+ Connecteur)** et sélectionnez le connecteur **Braze** pour lancer le formulaire de configuration. Remplissez les champs indiqués dans le formulaire avec les valeurs appropriées :
- `Destination schema` : un nom de schéma unique.
- `API URL` : votre endpoint d’API REST Braze.
- `API Key` : votre clé API REST Braze. 
- `Bucket Name` : disponible dans votre compte Braze en accédant à **Integration (Intégration) > Currents > [Your Current name (Nom de votre Current)] > Bucket Name (Nom du compartiment)**.
- `Folder` : disponible dans votre compte Braze en accédant à **Integration (Intégration) > Currents > [Your Current name (Nom de votre Current)] > Prefix (Préfixe)**.

{% alert important %}
Assurez-vous que **Google Cloud Storage** est sélectionné en tant que **Cloud Storage (Stockage cloud)**.
{% endalert %}

Enfin, cliquez sur **Save & Test (Enregistrer et tester)**, et Fivetran se chargera du reste en synchronisant les données de votre compte Braze !

[1]: {{site.baseurl}}/api/basics/#api-definitions