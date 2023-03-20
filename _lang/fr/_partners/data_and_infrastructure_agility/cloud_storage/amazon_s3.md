---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et Amazon S3, un système de stockage hautement évolutif proposé par Amazon Web Services."
page_type: partner
search_tag: Partenaire

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) est un système de stockage hautement évolutif proposé par Amazon Web Services.

L’intégration Braze et Amazon S3 utilise [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) pour envoyer les données de Braze dans votre instance S3, ce qui vous permet de les y stocker jusqu’à ce que vous vouliez les connecter à d’autres plateformes, outils ou emplacements. Vous pouvez également effectuer l’intégration en exportant des données du tableau de bord. Suivez les instructions de cette page pour commencer votre intégration AWS S3.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Amazon S3 | Un compte Amazon S3 est requis pour profiter de ce partenariat. |
| Compartiment S3 dédié | Avant d’intégrer Amazon S3, vous devez créer un compartiment S3 pour votre application.<br><br>Si vous avez déjà un compartiment S3, nous recommandons toujours de créer un nouveau compartiment spécialement pour Braze afin de pouvoir limiter les autorisations. Reportez-vous aux instructions suivantes pour savoir comment créer un nouveau compartiment. |
| Currents | Pour exporter des données dans Amazon S3, vous devez avoir configuré [currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2}

#### Créer un nouveau compartiment S3

Pour créer un nouveau compartiment pour votre application, ouvrez la [console Amazon S3](https://console.aws.amazon.com/s3/) et suivez les instructions pour **Se connecter** ou **Créer un compte AWS**. Une fois connecté, sélectionnez **S3** dans la catégorie **Stockage et livraison de contenu**. Sélectionnez **Créer un compartiment** sur l’écran suivant. Vous serez invité à créer votre compartiment et à sélectionner une région.

## Intégration

Braze a deux stratégies d’intégration différentes pour Amazon S3 : une pour [currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) et une autre pour toutes les exportations de données du tableau de bord (exportations CSV, rapports d’engagement, etc.) Les deux intégrations prennent en charge deux méthodes authentication/authorization différentes :

- [Méthode avec clé d’accès secrète AWS](#aws-secret-key-auth-method)
- [Méthode avec ARN AWS](#aws-role-arn-auth-method)

## Méthode d’authentification avec clé secrète AWS

Cette méthode d’authentification génère une clé secrète et un identifiant d’accès qui permet à Braze de s’authentifier en tant qu’utilisateur sur votre compte AWS afin d’écrire des données dans votre compartiment.

### Étape 1 : Créer un utilisateur {#secret-key-1}

Pour récupérer votre identifiant d’accès et votre clé d’accès secrète, vous devez [créer un groupe d’utilisateurs et d’administrateurs IAM dans AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Étape 2 : Obtenir des informations d’identification {#secret-key-2}

Après avoir créé un nouvel utilisateur, cliquez sur **Show User Security Credentials (Afficher les informations d’identification de sécurité de l’utilisateur)** pour révéler votre ID d’accès et votre clé d’accès secrète. Ensuite, notez ces informations d’identification quelque part ou cliquez sur le bouton **Download Credentials (Télécharger les informations d’identification)**. Vous devrez saisir ces identifiants dans le tableau de bord de Braze ultérieurement.

![][11]

### Étape 3 : Créer une politique {#secret-key-3}

Accédez à **Policies (Politiques) > Get Started (Démarrer) > Create Policy (Créer une politique)** pour ajouter des autorisations à votre utilisateur. Ensuite, sélectionnez **Create Your Own Policy (Créer votre propre politique)**. Cela vous permettra d’accorder un nombre limité d’autorisations pour que Braze ne puisse accéder qu’aux compartiments désignés. 

![][12]

{% alert note %}
Différentes politiques sont requises pour « Currents » et l’« Dashboard Data Export (Exportation des données du tableau de bord) ».
{% endalert %}

Donnez un nom à la politique et saisissez l’extrait de code suivant dans la section **Document de la politique**. Assurez-vous de remplacer `INSERTBUCKETNAME` par le nom de votre compartiment. Sans ces autorisations, l’intégration ne passera pas la vérification des informations d’identification et ne sera pas créée.

{% tabs %}
{% tab Braze Currents %}
```json
{
  "Version": "2012-10-17",
  "Statement": [
    { "Effect": "Allow",
      "Action": ["s3:GetBucketLocation"],
      "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
    }
    ,
    { "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:ListBucket"],
      "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
    }
  ]
}
```
{% endtab %}
{% tab Dashboard Data Export %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### Étape 4 : Joindre une politique {#secret-key-4}

Après avoir créé une nouvelle politique, accédez à **Users (Utilisateurs)** et cliquez sur votre utilisateur. Dans l’onglet **Permissions (Autorisations)**, cliquez sur **Attach Policy (Joindre une politique)** et sélectionnez la nouvelle politique que vous avez créée. Vous êtes maintenant prêt à associer vos identifiants AWS à votre compte Braze.

![][13]

### Étape 5 : Lier Braze à AWS {#secret-key-5}

{% tabs %}
{% tab Braze Currents %}

Dans Braze, accédez à la page **Currents** sous **Integrations (Intégrations)**. Ensuite, cliquez sur **Create Current (Créer un Current)** et sélectionnez **Amazon S3 Data Export (Exportation des données Amazon S3)**.

Nommez votre Current, puis dans la section **Credentials (Informations d’identification)**, assurez-vous que la case d’option **AWS Secret Access Key (Clé d’accès secrète AWS)** est sélectionnée, puis saisissez votre ID d’accès S3, la clé d’accès secrète AWS et le nom du compartiment AWS S3 dans les champs indiqués.

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Assurez-vous de garder votre clé d’accès AWS et votre clé d’accès secrète à jour. Le connecteur arrêtera d’envoyer des événements si les informations d’identification de votre connecteur expirent. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}

Vous pouvez également ajouter les personnalisations suivantes en fonction de vos besoins :

- Chemin du dossier (par défaut, `currents`) 
- Cryptage AES-256 au repos côté serveur (désactivé par défaut) - Inclut l’en-tête `x-amz-server-side-encryption`

Cliquez sur **Launch Current (Lancer Current)** pour continuer.

Une notification vous informera si vos identifiants ont bien été validés. AWS S3 devrait maintenant être configuré pour les Currents Braze.

{% endtab %}
{% tab Dashboard Data Export %}

Dans Braze, accédez à la page **Technology Partners (Partenaires de technologie) ** sous **Integrations (Intégrations)** et cliquez sur **Amazon S3**.

Sur la page des identifiants AWS, assurez-vous que la case d’option **AWS Secret Access Key (Clé d’accès secrète AWS)** est sélectionnée, puis saisissez votre ID d’accès AWS, la clé d’accès secrète AWS et le nom du compartiment AWS S3 dans les champs indiqués. Au moment de renseigner votre clé secrète, cliquez d’abord sur **Test Credentials (Tester les informations d’identification)** pour vous assurer que vos identifiants fonctionnent, puis cliquez sur **Save (Enregistrer)** après vous être connecté avec succès.

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Vous pouvez toujours récupérer de nouvelles informations d’identification en accédant à votre profil utilisateur, puis en cliquant sur **Create Access Key (Créer une clé d’accès)** dans l’onglet **Security Credentials (Informations d’identification de sécurité)** de la console AWS.
{% endalert %}

Une notification vous informera si vos identifiants ont bien été validés. AWS S3 devrait maintenant être intégré à votre compte Braze.

{% endtab %}
{% endtabs %}

## Méthode d’authentification de l’ARN du rôle AWS

Cette méthode d’authentification génère un ARN (Amazon Resource Name) de rôle qui permet au compte Amazon de Braze de s’authentifier en tant que membre du rôle que vous avez créé pour écrire des données dans votre compartiment.

### Étape 1 : Créer une politique {#role-arn-1}

Pour commencer, connectez-vous à la console de gestion AWS en tant qu’administrateur de compte. Accédez à la section IAM de la console AWS, cliquez sur **Policies (Politiques)** dans la barre de navigation, puis cliquez sur **Create Policy (Créer une politique)**.

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Différentes politiques sont requises pour « Currents » et l’« Dashboard Data Export (Exportation des données du tableau de bord) ».
{% endalert %}

Ouvrez l’onglet **JSON** et saisissez l’extrait de code suivant dans la section **Policy Document (Document de la politique)**. Assurez-vous de remplacer `INSERTBUCKETNAME` par le nom de votre compartiment. Cliquez sur **Review Policy (Vérifier la politique)** après avoir terminé.

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Dashboard Data Export %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

Ensuite, ajoutez un nom et une description pour la politique, puis cliquez sur **Create Policy (Créer une politique)**.

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Étape 2 : Créer un rôle {#role-arn-2}

Dans la même section IAM de la console AWS, cliquez sur **Roles (Rôles) > Create Role (Créer un rôle)**.

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Récupérez votre ID de compte Braze et votre ID externe sur votre compte Braze :
- **Currents** : Dans Braze, accédez à la page **Currents** sous **Integrations (Intégrations)**. Ensuite, cliquez sur **Create Current (Créer un Current)** et sélectionnez **Amazon S3 Data Export (Exportation des données Amazon S3)**. Vous trouverez ici les identifiants nécessaires pour créer votre rôle.
- **Exportation des données du tableau de bord** : Dans Braze, accédez à la page **Technology Partners (Partenaires de technologie) ** sous **Integrations (Intégrations)** et cliquez sur **Amazon S3**. Vous trouverez ici les identifiants nécessaires pour créer votre rôle.

De retour sur la console AWS, sélectionnez **Another AWS Account (Autre compte AWS)** comme type de sélecteur de l’entité approuvée. Renseignez votre ID de compte Braze, cochez la case **Require external ID (Exiger un ID externe)** et saisissez l’ID externe de Braze. Cliquez sur **Next (Suivant)** une fois terminé.

![Page S3 « Create Role (Créer un rôle) ». Cette page comporte des champs pour le nom du rôle, la description du rôle, les entités de confiance, les politiques et les restrictions d’autorisations.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Étape 3 : Joindre une politique {#role-arn-3}

Ensuite, joignez la politique que vous avez créée plus tôt au rôle. Recherchez la politique dans la barre de recherche et cochez la case pour la joindre. Cliquez sur **Next (Suivant)** une fois terminé.

![ARN du rôle]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Donnez un nom et une description au rôle, puis cliquez sur **Create Role (Créer un rôle)**.

![ARN du rôle]({{site.baseurl}}/assets/img/create_role_4_name.png)

Le rôle que vous venez de créer devrait maintenant apparaître dans la liste.

### Étape 4 : Lier Braze à AWS {#role-arn-4}

Dans la console AWS, recherchez le rôle que vous venez de créer dans la liste. Cliquez sur le nom du rôle pour ouvrir les détails.

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

Notez l’**ARN du rôle** qui se trouve en haut de la page Role summary (Synthèse du rôle).

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Revenez sur votre compte Braze et copiez l’ARN du rôle dans le champ indiqué.

{% tabs %}
{% tab Braze Currents %}

Dans Braze, accédez à la page **Currents** sous **Integrations (Intégrations)**. Ensuite, cliquez sur **Create Current (Créer un Current)** et sélectionnez **Amazon S3 Data Export (Exportation des données Amazon S3)**

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Donnez un nom à votre Current. Ensuite, dans la section **Credentials (Informations d’identification)**, assurez-vous que la case d’option **AWS Role ARN (ARN de rôle AWS)**est sélectionnée, puis saisissez l’ARN de votre rôle et le nom de votre compartiment AWS S3 dans les champs indiqués.

Vous pouvez également ajouter les personnalisations suivantes en fonction de vos besoins :

- Chemin du dossier (par défaut, `currents`)
- Cryptage AES-256 au repos côté serveur (désactivé par défaut) - Inclut l’en-tête `x-amz-server-side-encryption`

Cliquez sur **Launch Current (Lancer Current)** pour continuer.

Une notification vous informera si vos identifiants ont bien été validés. AWS S3 devrait maintenant être configuré pour les Currents Braze.

{% alert important %}
Si vous recevez une erreur intitulée « S3 credentials are invalid (Informations d’identification S3 invalides) », cela peut être dû à une intégration effectuée trop rapidement après avoir créé un rôle dans AWS. Attendez un moment, puis essayez à nouveau. 
{% endalert %}

{% endtab %}
{% tab Dashboard Data Export %}

Dans Braze, accédez à la page **Technology Partners (Partenaires de technologie) ** sous **Integrations (Intégrations)** et cliquez sur **Amazon S3**.

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

À la page **AWS Credentials (Informations d’identification AWS)**, assurez-vous que la case d’option **AWS Role ARN (ARN de rôle AWS)**est sélectionnée, puis saisissez l’ARN de votre rôle et le nom de votre compartiment AWS S3 dans les champs indiqués. Cliquez d’abord sur **Test Credentials (Tester les informations d’identification)** pour vous assurer que vos identifiants fonctionnent, puis cliquez sur **Save (Enregistrer)** après vous être connecté avec succès.

{% alert tip %}
Vous pouvez toujours récupérer de nouvelles informations d’identification en accédant à votre profil utilisateur, puis en cliquant sur **Create Access Key (Créer une clé d’accès)** dans l’onglet **Security Credentials (Informations d’identification de sécurité)** de la console AWS.
{% endalert %}

Une notification vous informera si vos identifiants ont bien été validés. AWS S3 devrait maintenant être intégré à votre compte Braze.

{% endtab %}
{% endtabs %}

## Connecteurs multiples

Si vous avez l’intention de créer plusieurs connecteurs Currents à envoyer à votre compartiment S3, vous pouvez utiliser les mêmes informations d’identification, mais vous devrez indiquer un chemin de dossier différent pour chacun d’entre eux. Ces connecteurs peuvent être créés dans le même groupe d’apps, ou être divisés et créés dans plusieurs groupes d’apps. Vous avez également la possibilité de créer une seule politique pour chaque intégration, ou encore de créer une politique qui couvre les deux intégrations. 

Si vous prévoyez d’utiliser le même compartiment S3 pour Currents et les exportations de données, vous devrez créer deux politiques séparées, étant donné que chaque intégration nécessite des autorisations différentes.


[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
