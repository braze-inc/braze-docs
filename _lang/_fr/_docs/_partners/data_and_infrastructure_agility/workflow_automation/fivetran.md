---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Cet article décrit le partenariat entre Braze et Fivetran, un outil d'automatisation de flux de travail qui peut vous aider dans la prise de décision soutenue par des données en fournissant des données prêtes à être interrogées dans votre entrepôt cloud."
page_type: partenaire
search_tag: Partenaire
---

# Fivetran

[Fivetran](https://fivetran.com/) est une marque mondialement reconnue dont les produits centrés sur les analystes et les pipelines entièrement gérés permettent de prendre des décisions basées sur des données en fournissant des données prêtes à être interrogées dans votre entrepôt cloud. Aujourd'hui, en tant que nouveau partenaire technologique de Braze, la prise de décision soutenue par les données a été rendue plus facile et plus efficace que jamais. vous permettant de passer plus de temps sur les tâches difficiles.

## Pré-requis

| Exigences                | Source                                                                               | Notes                                                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte Braze             | [Brasero](https://dashboard.braze.com/sign_in)                                       | Ce compte devrait avoir au moins un abonnement actif et des privilèges d'administrateur.                                                   |
| Compte de cinq personnes | [Fivetran](https://fivetran.com/login?next=%2Fdashboard)                             | Ce compte Fivetran devrait avoir les privilèges du propriétaire/administrateur.                                                            |
| Courants de Braze        | [Courants de Braze](https://www.braze.com/product/data-agility-management/currents/) | Les courants doivent être connectés à l'un des services de stockage cloud suivants : <br> **Amazon S3** ou **Google Cloud Storage**. |
| Braze API URL            | [Brasero](https://dashboard.braze.com/sign_in)                                       | Trouvé dans votre compte Braze.                                                                                                            |
| Clé API Braze            | [Brasero](https://dashboard.braze.com/sign_in)                                       | Trouvé dans votre compte Braze.                                                                                                            |

## Intégration

### Mise en place du courant de Braze

{% tabs %}
{% tab Amazon S3 %}

### Étape 1 : Localisez votre ID externe

Localisez votre ID externe dans le formulaire de configuration de Fivetran pour Braze. ![Formulaire de configuration du connecteur Fivetran]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

{% alert note %}
Remarquez l' **ID externe** tel que décrit ci-dessus. Les détails restants requis pour terminer la configuration seront récupérés dans les étapes suivantes.
{% endalert %}

### Étape 2 : Créer une clé API Braze pour le stockage Amazon S3

Ensuite, connectez-vous à votre tableau de bord [ici](https://dashboard.braze.com) ou avec votre [URL de tableau de bord désignée]({{site.baseurl}}/api/basics?redirected=true#endpoints) et cliquez sur **Console développeur** dans le coin inférieur gauche du tableau de bord de Braze.

À partir d'ici, [créez une clé API]({{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys) pour Fivetran et activez les autorisations suivantes pour ladite clé :

* Exporter les identifiants
* Exporter les utilisateurs
* Se désabonner
* Vous avez bouncé votre adresse e-mail
* Programmer les diffusions
* campagnes.liste
* Détails des campagnes
* Liste de toiles
* Détails de la page d'accueil
* segments.list
* détails
* Liste des produits achetés
* liste des événements
* Liste
* Détails du flux
* Informations sur les modèles
* Liste des modèles
* Obtenir le statut
* Obtenir

Enfin, prenez note de la clé API créée avant de continuer, car elle sera requise à l'étape 4.

### Étape 3 : Donnez à Fivetran l'accès à un seau S3 spécifié

#### Créer une politique IAM

Ouvrez la [console Amazon IAM](https://console.aws.amazon.com/iam/home#home) et accédez à **Politiques ->Créer une politique** comme indiqué ci-dessous.

![Politiques d'Amazon S3]({% image_buster /assets/img/fivetran_as3_iam.png %})

Ensuite, accédez à l'onglet **JSON**.

![Politique d'Amazon S3 Json]({% image_buster /assets/img/fivetran_iam_policy_json.png %})

Copiez la politique ci-dessous, remplaçant **{your-bucket-name}** par le nom de votre compartiment s3 :

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

Maintenant, cliquez sur le bouton **Revoir la politique** pour apporter des modifications finales avant l'installation.

Ici, donnez à la politique un nom unique (quelque chose comme "Fivetran-S3-Access") et une description facultative avant de cliquer sur le bouton **Créer une politique**.

![Bouton d'examen de la politique d'Amazon S3]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

#### Créer un rôle IAM

Naviguez vers **Rôles**, puis sélectionnez **Créer un nouveau rôle**.

![Nouveau rôle Amazon S3 IAM]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Sélectionnez **Un autre compte AWS**, puis cliquez sur la case à cocher pour **Require un ID externe**.

![Amazon S3 requiert un ID externe]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Ici, entrez l'ID du compte Fivetran, `834469178297`, et le `ID externe` qui a été trouvé dans le formulaire d'installation de la connexion Fivetran Braze S3 pendant l'étape 1.

![ID externe d'entrée Amazon S3]({% image_buster /assets/img/fivetran_as3_external_id.png %})

Cliquez sur **Suivant : Autorisations**et sélectionnez maintenant la politique que vous avez créée précédemment (c.-à-d. "Fivetran-S3-Access").

![Politique de sélection d'Amazon S3]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Enfin, cliquez sur **Suivant : Révisez**, nommez votre nouveau rôle (c.-à-d. Fivetran), et cliquez sur **Créer un rôle**.

#### Localisation du rôle IAM ARN

Cliquez sur le rôle que vous venez de créer, ou naviguez vers **Rôles** depuis votre [console Amazon IAM](https://console.aws.amazon.com/iam/home#home). ![Rôle d'Amazon S3 IAM ARN]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Vous pouvez spécifier les permissions pour le rôle ARN que vous désignez pour Fivetran. Donner des permissions sélectives à ce rôle permettra à Fivetran de synchroniser uniquement ce qu'il a les permissions de voir.
{% endalert %}

{% endtab %}
{% tab Google Cloud Storage %}

### Étape 1 : Récupérez votre e-mail de Fivetran dans Google Cloud Storage

Localisez votre e-mail Fivetran dans le formulaire de configuration de Fivetran pour Braze en vous connectant à votre [tableau de bord Fivetran](https://fivetran.com/dashboard), en cliquant sur **+ Connecteur** en sélectionnant **Braze** et en sélectionnant **Stockage Azure Blob** comme option `Stockage Cloud`.

![Formulaire de configuration du connecteur Fivetran]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

### Étape 2 : Créer une clé API Braze pour Google Cloud Storage

Ensuite, connectez-vous à votre compte Braze [ici](https://dashboard.braze.com) ou avec votre [URL de tableau de bord désigné]({{site.baseurl}}/api/basics?redirected=true#endpoints) et cliquez sur **Console de développement** en bas à gauche du tableau de bord de Braze.

À partir d'ici, [créez une clé API]({{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys) pour Fivetran et activez les autorisations suivantes pour ladite clé :

* Exporter les identifiants
* Exporter les utilisateurs
* Se désabonner
* Vous avez bouncé votre adresse e-mail
* Programmer les diffusions
* campagnes.liste
* Détails des campagnes
* Liste de toiles
* Détails de la page d'accueil
* segments.list
* détails
* Liste des produits achetés
* liste des événements
* Liste
* Détails du flux
* Informations sur les modèles
* Liste des modèles
* Obtenir le statut
* Obtenir

Enfin, prenez note de la clé API créée avant de continuer, car elle sera requise à l'étape 4.

### Étape 3: Autorisation

Naviguez vers votre [console de stockage Google](https://console.cloud.google.com/storage/browser) et sélectionnez un segment avec lequel vous avez configuré Braze Devises et cliquez sur **Modifier les permissions du segment**.

After clicking **Edit bucket permissions**, grant `Storage Object Viewer` access to the email from Step 1 by adding the email as a member.

![Ajouter un membre à un seau de stockage Google]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

Enfin, accédez à votre console de stockage Google Cloud [](https://console.cloud.google.com/storage?pli=1) et prenez note du nom du segment car il sera nécessaire dans les étapes finales de l'installation.

![Seaux de stockage Google]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})
{% endtab %} {% endtabs %}

## Étapes finales

Après vous être connecté à votre [tableau de bord Fivetran](https://fivetran.com/dashboard), cliquez sur **+ Connecteur** trouvé dans le coin supérieur droit de l'écran et sélectionnez le connecteur **Braze** pour lancer le formulaire d'installation. Dans le formulaire, remplissez les champs avec les valeurs appropriées :

{% tabs %}
{% tab Amazon S3 %}

`Schéma de destination`: Choisir un nom de schéma unique.

`URL de l'API`: Votre URL d'API assignée a été trouvée lors du processus de configuration des courants de Braze.

`Clé d'API`: La clé d'API notée lors du processus de configuration des courants de Braze.

`ID externe`: Valeur fixe. Utilisez cet ID pour configurer le rôle IAM à l'étape 3 du processus de configuration des courants de Braze.

`Seau`: Trouvé dans votre tableau de bord Braze en naviguant vers **Intégration > Devises > `votre-nom actuel`**.

`Rôle ARN`: Voir Étape 3 du processus de configuration des courants de Braze.

{% alert important %}
Assurez-vous que **Amazon S3** est sélectionné comme le choix `de stockage nuagique`.
{% endalert %}

{% endtab %}
{% tab Google Cloud Storage %}

`Schéma de destination`: Un nom de schéma unique.

`URL de l'API`: votre URL d'API assignée se trouve à l'étape 2 du processus de configuration des courants de Braze.

`Clé d'API`: La clé que vous avez notée à l'étape 2 du processus de configuration de Braze Currents.

`Nom de seau`: Trouvé dans votre compte Braze en naviguant vers **Intégration > Devises > `votre-nom actuel` > `Nom Seau`**.

`Dossier`: Trouvé dans votre compte Braze en naviguant vers **Intégration > Devises > `votre-nom actuel` > `Préfixe`**

{% alert important %}
Assurez-vous que **Google Cloud Storage** est sélectionné comme le choix `de stockage dans le Cloud`.
{% endalert %}

{% endtab %}
{% endtabs %}

Enfin, cliquez sur **Enregistrer & Tester** et Fivetran fera le reste en synchronisant avec les données de votre compte Braze !
