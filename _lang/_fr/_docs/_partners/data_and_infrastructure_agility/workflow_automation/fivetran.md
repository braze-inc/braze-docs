---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Cet article décrit le partenariat entre Braze et Fivetran, un outil d'automatisation de flux de travail qui peut vous aider dans la prise de décision soutenue par des données en fournissant des données prêtes à être interrogées dans votre entrepôt cloud."
page_type: partenaire
search_tag: Partenaire
tool: Courants
---

# Fivetran

> [Fivetran](https://fivetran.com/) est une marque mondialement reconnue dont les produits centrés sur les analystes et les pipelines entièrement gérés permettent de prendre des décisions basées sur des données en fournissant des données prêtes à être interrogées dans votre entrepôt cloud.

L'intégration de Braze et Fivetran permet aux utilisateurs de créer un pipeline de maintenance zéro qui vous permet de collecter et d'analyser les données de Braze en connectant toutes vos applications et bases de données à un entrepôt central. Une fois que les données ont été collectées dans l'entrepôt central, les équipes de données peuvent explorer les données de Braze efficacement en utilisant leurs outils de renseignements commerciaux préférés.

## Pré-requis

| Exigences                         | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte de cinq personnes          | Un compte [Fivetran](https://fivetran.com/login?next=%2Fdashboard) est requis pour profiter de ce partenariat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Braze clé API REST                | Une clé API Braze REST avec les permissions suivantes :<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages. chedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- achats. roduct_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription. roupies. et <br><br> Ceci peut être créé dans le tableau de bord **Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API** |
| Point de terminaison REST Braze   | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][1].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Courants de Braze                 | [Les courants de Braze](https://www.braze.com/product/data-agility-management/currents/) doivent être connectés à Amazon S3 ou Google Cloud Storage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Amazon S3 ou Google Cloud Storage | Cette intégration nécessite que vous ayez accès à un Amazon S3 ou Google Cloud Storage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

L'intégration des courants suivants est prise en charge à la fois pour [Amazon S3](#setting-up-braze-currents-for-s3) et [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage).

### Mise en place des courants de Braze pour S3

#### Étape 1 : Localisez votre ID externe {#step-one}

Dans le tableau de bord [de Fivetran](https://fivetran.com/dashboard), cliquez sur **+ Connecteur** trouvé dans le coin supérieur droit de l'écran et sélectionnez le connecteur **Braze** pour lancer le formulaire d'installation. Ensuite, sélectionnez **Amazon S3**. Notez l'ID externe fourni ici; vous en aurez besoin pour permettre à Fivetran d'accéder à votre compartiment S3.

![Formulaire de configuration du connecteur Fivetran]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### Étape 2 : Donnez à Fivetran l'accès à un seau S3 spécifié

##### Créer une politique IAM

Ouvrez la [console Amazon IAM](https://console.aws.amazon.com/iam/home#home) et accédez à **Politiques > Créer une politique**.

![Politiques d'Amazon S3]({% image_buster /assets/img/fivetran_as3_iam.png %})

Ensuite, cliquez sur l'onglet **JSON** et collez la politique ci-dessous. Assurez-vous de remplacer `{your-bucket-name}` par le nom de votre compartiment S3.

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effet": "Autoriser",
      "Action": [
"s3:Get*",
"s3:Liste*"
      ],
      "Ressource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effet": "Autorisation",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Ressource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

Enfin, cliquez sur **Revoir la politique** et donnez à la politique un nom et une description uniques. Cliquez sur **Créer une politique** pour construire votre politique.

![Bouton de revue de la politique d'Amazon S3]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### Créer un rôle IAM {#step-two}

Dans AWS, accédez à **Rôles**, puis sélectionnez **Créer un nouveau rôle**.

![Nouveau rôle Amazon S3 IAM]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Sélectionnez **Un autre compte AWS** et fournissez l'ID du compte Fivetran `834469178297`. Assurez-vous de cocher la case à cocher **Require un ID externe**. Ici, vous fournirez l'ID externe trouvé à l'étape 1.

![Amazon S3 requiert un ID externe]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Ensuite, cliquez sur **Suivant : Autorisations** pour sélectionner la politique que vous venez de créer.

![Politique de sélection d'Amazon S3]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Cliquez sur **Suivant : Examiner**, nommer votre nouveau rôle (c.-à-d. Fivetran), et cliquez sur **Créer un rôle**. Une fois créé, cliquez sur le rôle que vous venez de créer et notez le rôle ARN affiché.

![Rôle d'Amazon S3 IAM ARN]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Vous pouvez spécifier les permissions pour le rôle ARN que vous désignez pour Fivetran. Donner des permissions sélectives à ce rôle permettra à Fivetran de synchroniser uniquement ce qu'il a les permissions de voir.
{% endalert %}

#### Étape 3 : Terminez le connecteur de Fivetran

À Fivetran, cliquez sur **+ Connecteur** situé en haut à droite de l'écran et sélectionnez le connecteur **Braze** pour lancer le formulaire d'installation. Dans le formulaire, remplissez les champs avec les valeurs appropriées :
- `Schéma de destination`: Un nom de schéma unique.
- `URL de l'API`: Votre point de terminaison de l'API REST Braze.
- `Clé API`: votre clé API REST Braze.
- `ID externe`: L'ID externe mis en [étape 2](#step-two) des courants configurent des directions. Cet ID est une valeur fixe.
- `Seau`: Trouvé dans votre compte Braze en naviguant vers **Intégration > Devises > [Votre nom actuel] > Nom Bucket**.
- `Rôle ARN`: Le rôle ARN peut être trouvé dans [l'étape 1](#step-one) des directions de configuration courante.

{% alert important %}
Assurez-vous que **Amazon S3** est sélectionné comme le choix **de stockage nuagique**.
{% endalert %}

Enfin, cliquez sur **Enregistrer & Tester**, et Fivetran fera le reste en synchronisant avec les données de votre compte Braze !

### Mise en place des courants de Braze pour Google Cloud Storage

#### Étape 1 : Récupérez votre e-mail de Fivetran dans Google Cloud Storage {#step-one2}

Dans le tableau de bord [Fivetran](https://fivetran.com/dashboard), cliquez sur **+ Connecteur** trouvé dans le coin supérieur droit de l'écran et sélectionnez le connecteur **Braze** pour lancer le formulaire d'installation. Ensuite, sélectionnez **Google Cloud storage**. Prenez note de l'adresse e-mail qui apparaît.

![Formulaire de configuration du connecteur Fivetran]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### Étape 2 : Accorder un accès au seau

Naviguez vers votre [console de stockage Google](https://console.cloud.google.com/storage/browser) et sélectionnez le compartiment avec lequel vous avez configuré les courants de Braze, et cliquez sur **Editer les permissions du compartiment**.

![Seckets de stockage Google]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

Ensuite, accordez à la visionneuse d'objet de stockage `` l'accès à l'e-mail à partir de [l'étape 1](#step-one2) en ajoutant l'e-mail en tant que membre. Notez le nom du bucket ; vous en aurez besoin à l'étape suivante pour configurer Fivetran.

![Ajouter un membre à un compartiment de stockage Google]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### Étape 3 : Terminez le connecteur de Fivetran

À Fivetran, cliquez sur **+ Connecteur** situé en haut à droite de l'écran et sélectionnez le connecteur **Braze** pour lancer le formulaire d'installation. Dans le formulaire, remplissez les champs avec les valeurs appropriées :
- `Schéma de destination`: Un nom de schéma unique.
- `URL de l'API`: Votre point de terminaison de l'API REST Braze.
- `Clé API`: votre clé API REST Braze.
- `Nom du Bucket`: Trouvé dans votre compte Braze en naviguant vers **Intégration > Devises > [Votre nom actuel] > Nom du Bucket**.
- `Dossier`: Trouvé dans votre compte Braze en naviguant vers **Intégration > Devises > [Votre nom actuel] > Préfixe**.

{% alert important %}
Assurez-vous que **Google Cloud Storage** est sélectionné comme le choix **de stockage dans le Cloud**.
{% endalert %}

Enfin, cliquez sur **Enregistrer & Tester**, et Fivetran fera le reste en synchronisant avec les données de votre compte Braze !

[1]: {{site.baseurl}}/api/basics/#api-definitions