---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "Cet article de référence présente le partenariat entre Braze et Amazon S3, un système de stockage hautement évolutif proposé par Amazon Web Services."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) est un système de stockage hautement évolutif proposé par Amazon Web Services.

L'intégration de Braze et Amazon S3 s'appuie sur [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) pour envoyer les données de Braze à votre instance S3, ce qui vous permet d'y stocker des données jusqu'à ce que vous souhaitiez les connecter à d'autres plateformes, outils et emplacements/localisations. Vous pouvez également procéder à l'intégration par le biais d'exportations de données de tableaux de bord. Suivez les instructions de cette page pour démarrer votre intégration AWS S3.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Amazon S3 | Un compte Amazon S3 est nécessaire pour profiter de ce partenariat. |
| Compartiment S3 dédié | Avant d'intégrer Amazon S3, vous devez créer un compartiment S3 pour votre application.<br><br>Si vous disposez déjà d'un compartiment S3, nous vous recommandons tout de même de créer un nouveau compartiment spécifiquement pour Braze afin de pouvoir limiter les autorisations. Reportez-vous aux instructions suivantes pour savoir comment créer un nouveau compartiment. |
| Currents | Pour pouvoir réexporter des données vers Amazon S3, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Créez un nouveau compartiment S3

Pour créer un compartiment pour votre application, ouvrez la [console Amazon S3](https://console.aws.amazon.com/s3/) et suivez les instructions pour **vous connecter** ou **créer un compte avec AWS.** Après vous être connecté, sélectionnez **S3** dans la catégorie **Stockage et distribution de contenu**. Sélectionnez **Créer un compartiment** dans l'écran suivant. Vous serez invité à créer votre compartiment et à sélectionner une région.

## Intégration

Braze dispose de deux stratégies d'intégration différentes avec Amazon S3 - l'une pour [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) et l'autre pour toutes les exportations de données des tableaux de bord (exportations CSV, rapports d'engagement, etc.). Les deux intégrations prennent en charge deux méthodes d'authentification/autorisation différentes :

- [Méthode de clé d'accès secrète AWS](#aws-secret-key-auth-method)
- [Méthode ARN de rôle AWS](#aws-role-arn-auth-method)

## Méthode d'authentification par clé secrète AWS

Cette méthode d'authentification génère une clé secrète et un ID de clé d'accès qui permet à Braze de s'authentifier en tant qu'utilisateur sur votre compte AWS pour écrire des données dans votre compartiment.

### Étape 1 : Créer un utilisateur {#secret-key-1}

Pour récupérer votre ID de clé d'accès et votre clé d'accès secrète, vous devez [créer un utilisateur IAM et un groupe d'administrateurs dans AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Étape 2 : Obtenir des informations d'identification {#secret-key-2}

Après avoir créé un nouvel utilisateur, cliquez sur **Afficher les informations de sécurité de l'utilisateur** pour révéler votre ID de clé d'accès et votre clé d'accès secrète. Ensuite, notez ces informations d'identification quelque part ou cliquez sur le bouton **Télécharger les informations d'identification**, car vous devrez les saisir ultérieurement dans le tableau de bord de Braze.

![][11]

### Étape 3 : Créer une politique {#secret-key-3}

Naviguez vers **Politiques > Démarrer > Créer une politique** pour ajouter des autorisations pour votre utilisateur. Ensuite, sélectionnez **Créer votre propre politique.** Cela donnera des autorisations limitées, de sorte que Braze ne pourra accéder qu'aux compartiments spécifiés. 

![][12]

{% alert note %}
Des politiques différentes sont nécessaires pour "Currents" et "Exportation des données du tableau de bord".
{% endalert %}

Spécifiez le nom de la politique de votre choix et saisissez l'extrait de code suivant dans la section **Document de politique.**  Veillez à remplacer `INSERTBUCKETNAME` par le nom de votre compartiment. Sans ces autorisations, l'intégration échouera lors de la vérification des informations d'identification et ne sera pas créée.

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
{% tab Export des données du tableau de bord %}
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

### Étape 4 : Joindre la politique {#secret-key-4}

Après avoir créé une nouvelle politique, naviguez vers **Utilisateurs** et cliquez sur votre utilisateur spécifique. Dans l'onglet **Permissions**, cliquez sur **Joindre une politique** et sélectionnez la nouvelle politique que vous avez créée. Vous êtes maintenant prêt à lier vos identifiants AWS à votre compte Braze.

![][13]

### Étape 5: Lier Braze à AWS {#secret-key-5}

{% tabs %}
{% tab Braze Currents %}

Dans Braze, accédez à **Intégrations partenaires** > **Export des données**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez **Currents** sous **Intégrations.**
{% endalert %}

Ensuite, cliquez sur **Créer un flux Currents** et sélectionnez **Exportation de données Amazon S3.**

Nommez votre flux Currents, puis dans la section **Identifiants**, assurez-vous que le bouton radio **Clé d'accès secrète AWS** est sélectionné, puis saisissez votre ID d'accès S3, votre clé d'accès secrète AWS et le nom du compartiment S3 dans les champs désignés.

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Maintenez à jour votre ID de clé d'accès AWS et votre clé d'accès secrète. Si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

Vous pouvez également ajouter les personnalisations suivantes en fonction de vos besoins :

- **Chemin d'accès au dossier :** La valeur par défaut est `currents`. Si ce dossier n'existe pas, Braze le créera automatiquement pour vous. 
- **Chiffrement AES-256 côté serveur, au repos :** La valeur par défaut est OFF et inclut l'en-tête `x-amz-server-side-encryption`.

Cliquez sur **Lancer le flux Currents** pour continuer.

Une notification vous indiquera si vos informations d'identification ont été validées avec succès. AWS S3 devrait maintenant être configuré pour Braze Currents.

{% endtab %}
{% tab Export des données du tableau de bord %}

Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques** et cliquez sur **Amazon S3**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les **partenaires technologiques** sous la rubrique **Intégrations.**
{% endalert %}

Sur la page Identifiants AWS, assurez-vous que le bouton radio **Clé d'accès secrète AWS** est sélectionné, puis saisissez votre ID d'accès AWS, votre clé d'accès secrète AWS et le nom du compartiment S3 AWS dans les champs désignés. Lorsque vous saisissez votre clé secrète, cliquez d'abord sur **Tester les informations d'identification** pour vous assurer que vos informations d'identification fonctionnent, puis cliquez sur **Enregistrer** en cas de succès.

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Vous pouvez toujours récupérer de nouvelles informations d'identification en naviguant vers votre utilisateur, et en cliquant sur **Créer une clé d'accès** dans l'onglet **Informations d'identification de sécurité** dans la console AWS.
{% endalert %}

Une notification vous indiquera si vos informations d'identification ont été validées avec succès. AWS S3 devrait maintenant être intégré à votre compte Braze.

{% endtab %}
{% endtabs %}

## Méthode d'authentification du rôle AWS ARN

Cette méthode d'authentification génère un nom de ressource Amazon (ARN) de rôle qui permet au compte Amazon de Braze de s'authentifier en tant que membre du rôle que vous avez créé pour écrire des données dans votre compartiment.

### Étape 1 : Créer une politique {#role-arn-1}

Pour commencer, connectez-vous à la console de gestion AWS en tant qu'administrateur de compte. Accédez à la section IAM de la console AWS, cliquez sur **Politiques** dans la barre de navigation, puis sur **Créer une politique.**

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Des politiques différentes sont nécessaires pour "Currents" et "Exportation des données du tableau de bord".
{% endalert %}

Ouvrez l'onglet **JSON** et saisissez l'extrait de code suivant dans la section **Policy Document.**  Veillez à remplacer `INSERTBUCKETNAME` par le nom de votre compartiment. Cliquez sur **Réviser la politique** lorsque vous avez terminé.

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
{% tab Export des données du tableau de bord %}

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
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

Ensuite, donnez un nom et une description à la politique et cliquez sur **Créer une politique**.

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Étape 2 : Créer un rôle {#role-arn-2}

Dans la même section IAM de la console, cliquez sur **Rôles > Créer un rôle**.

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Récupérez votre ID de compte Braze et votre ID externe à partir de votre compte Braze :
- **Currents** : Dans Braze, accédez à **Intégrations partenaires** > **Export des données**. Ensuite, cliquez sur **Créer un flux Currents** et sélectionnez **Exportation de données Amazon S3.** Vous trouverez ici les identifiants nécessaires à la création de votre rôle.
- **Exportation des données du tableau de bord**: Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques** et cliquez sur **Amazon S3**. Vous trouverez ici les identifiants nécessaires à la création de votre rôle.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), ces pages se trouvent à un emplacement/localisation différent :<br>- **Currents** est situé sous **Intégrations** > **Currents** <br>- **Partenaires technologiques** est accessible sous **Intégrations.**
{% endalert %}

De retour sur la console AWS, sélectionnez **Un autre compte AWS** comme type de sélecteur d'entité de confiance. Indiquez votre ID de compte Braze, cochez la case **Require external ID** et saisissez l'ID externe de Braze. Cliquez sur **Suivant** lorsque vous avez terminé.

![La page S3 "Create Role" (Créer un rôle). Cette page contient des champs pour spécifier le nom du rôle, la description du rôle, les entités de confiance, les politiques et les limites des autorisations.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Étape 3 : Joindre la politique {#role-arn-3}

Ensuite, attachez la politique que vous avez créée précédemment au rôle. Recherchez la police dans la barre de recherche et cochez-la pour la joindre. Cliquez sur **Suivant** lorsque vous avez terminé.

![ARN du rôle]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Donnez un nom et une description au rôle, puis cliquez sur **Create Role (Créer un rôle)**.

![ARN du rôle]({{site.baseurl}}/assets/img/create_role_4_name.png)

Vous devriez maintenant voir votre rôle nouvellement créé dans la liste.

### Étape 4 : Lien vers Braze AWS {#role-arn-4}

Dans la console AWS, trouvez votre rôle nouvellement créé dans la liste. Cliquez sur le nom pour ouvrir les détails de ce rôle.

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

Prenez note de l'**ARN du rôle** en haut de la page de résumé du rôle.

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Retournez sur votre compte Braze et copiez l'ARN du rôle dans le champ prévu à cet effet.

{% tabs %}
{% tab Braze Currents %}

Dans Braze, accédez à la page **Currents** sous la rubrique **Intégrations.** Ensuite, cliquez sur **Créer un flux Currents** et sélectionnez **Exportation de données Amazon S3**

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Donnez un nom à votre flux Currents. Ensuite, dans la section **Identifiants**, assurez-vous que l’option **ARN du rôle AWS** est sélectionnée, puis indiquez votre ARN de rôle et le nom du compartiment S3 d'AWS dans les champs désignés.

Vous pouvez également ajouter les personnalisations suivantes en fonction de vos besoins :

- Chemin d'accès au dossier (par défaut : `currents`)
- Cryptage AES-256 côté serveur, au repos (désactivé par défaut) - Inclut l'en-tête `x-amz-server-side-encryption`

Cliquez sur **Lancer le flux Currents** pour continuer.

Une notification vous indiquera si vos informations d'identification ont été validées avec succès. AWS S3 devrait maintenant être configuré pour Braze Currents.

{% alert important %}
Si vous recevez une erreur "Les identifiants S3 ne sont pas valides", cela peut être dû à une intégration trop rapide après la création d'un rôle dans AWS. Attendez et réessayez.
{% endalert %}

{% endtab %}
{% tab Export des données du tableau de bord %}

Dans Braze, accédez à la page **Partenaires technologiques** sous **Intégrations** et cliquez sur **Amazon S3**.

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Sur la page des **identifiants AWS**, assurez-vous que l’option **ARN du rôle AWS** est sélectionnée, puis saisissez votre ARN de rôle et le nom du compartiment S3 d'AWS dans les champs désignés. Cliquez d'abord sur **Tester les informations d'identification** pour vous assurer que vos informations d'identification fonctionnent correctement, puis cliquez sur **Enregistrer** en cas de succès.

{% alert tip %}
Vous pouvez toujours récupérer de nouvelles informations d'identification en naviguant vers votre utilisateur, et en cliquant sur **Créer une clé d'accès** dans l'onglet **Informations d'identification de sécurité** dans la console AWS.
{% endalert %}

Une notification vous indiquera si vos informations d'identification ont été validées avec succès. AWS S3 devrait maintenant être intégré à votre compte Braze.

{% endtab %}
{% endtabs %}

## Comportement à l'exportation

Les utilisateurs qui ont intégré une solution de stockage de données en nuage et qui tentent d'exporter des API, des rapports de tableau de bord ou des rapports CSV rencontreront le problème suivant :

- Toutes les exportations API ne renvoient pas d'URL de téléchargement dans le corps de la réponse et doivent être récupérées via le stockage de données.
- Tous les rapports des tableaux de bord et les rapports CSV seront envoyés à l'e-mail de l'utilisateur pour être téléchargés (aucune autorisation de stockage n'est requise) et sauvegardés sur le stockage de données. 

## Connecteurs multiples

Si vous avez l'intention de créer plusieurs connecteurs Currents à envoyer vers votre compartiment S3, vous pourrez utiliser les mêmes identifiants, mais devrez spécifier un chemin de dossier différent pour chacun. Ils peuvent être créés dans le même espace de travail, ou divisés et créés dans plusieurs espaces de travail. Vous avez également la possibilité de créer une politique unique pour chaque intégration, ou de créer une politique qui couvre les deux intégrations. 

Si vous prévoyez d'utiliser le même compartiment S3 pour les flux Currents et les exports de données, vous devrez créer deux politiques distinctes, car chaque intégration nécessite des autorisations différentes.


[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
