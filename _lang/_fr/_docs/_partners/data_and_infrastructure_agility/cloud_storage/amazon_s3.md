---
nav_title: Amazon S3
article_title: Amazon S3
alias: /fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr_FR/fr/
page_order: 1
description: "Cet article décrit le partenariat entre Braze et Amazon S3, un système de stockage hautement évolutif offert par Amazon Web Services."
page_type: partenaire
search_tag: Partenaire
---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) est un système de stockage hautement évolutif offert par Amazon Web Services.

Braze a deux stratégies d'intégration différentes avec Amazon S3 - une pour [les courants de Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) et une pour toutes les exportations de données du tableau de bord (CSV exportations, Rapports d'engagement, etc.) Les deux intégrations supportent deux méthodes d'authentification/autorisation différentes:

-   [Méthode de clé d'accès secrète AWS](#aws-secret-key-auth-method)
-   [Méthode ARN Rôle AWS](#aws-role-arn-auth-method)

Suivez les instructions sur cette page pour commencer votre intégration AWS S3. Si vous avez déjà un compartiment S3, nous vous recommandons de créer un nouveau compartiment **spécifiquement pour Braze** afin de limiter les permissions.

1.  Pour créer un compartiment pour votre application, ouvrez la console [Amazon S3](https://console.aws.amazon.com/s3/) et suivez les instructions pour **vous connecter** ou **créer un compte avec AWS**.
2.  Une fois connecté, sélectionnez **S3** dans la catégorie **Stockage & Contenu Delivery**.
3.  Sélectionnez **Créer un seau** sur l'écran suivant. Vous serez invité à créer votre compartiment et à sélectionner une région.

## Méthode d'authentification par clé secrète AWS

Cette méthode d'authentification génère une **clé secrète** et un **ID de clé d'accès** qui permet à Braze de s'authentifier en tant qu'utilisateur sur votre compte AWS pour écrire des données dans votre compartiment.

### Étape 1 : Créer un utilisateur {#secret-key-1}

Pour récupérer votre **ID de clé d'accès** et **clé d'accès secrète**, vous devrez [créer un **IAM User** et **Administrators Group** dans AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Étape 2 : Obtenir les identifiants {#secret-key-2}

Une fois qu'un utilisateur a été créé, cliquez sur **Afficher les identifiants de sécurité de l'utilisateur** afin que votre identifiant de clé d'accès et votre clé d'accès secrète soient révélés. Ensuite, notez ces identifiants quelque part ou cliquez sur le bouton **Télécharger les identifiants** car vous devrez les saisir plus tard dans le tableau de bord de Braze.

!\[Clé Secrète\]\[11\]

### Étape 3 : Créer une politique {#secret-key-3}

Maintenant, accédez à l'onglet **Politiques** dans la barre de navigation et sélectionnez **Démarrer** puis **Créer une politique**. Cela vous permettra d'ajouter des permissions pour votre utilisateur. Sélectionnez **Créer votre propre politique**. Cela donnera des permissions limitées donc nous avons seulement la possibilité d'accéder au bucket que vous spécifiez.

!\[Policy\]\[12\]

Entrez le code ci-dessous lors de la création de votre propre politique. Notez qu'il y a différentes règles requises pour "Actuels" vs. "Exportation des données du tableau de bord". Spécifiez un nom de politique de votre choix, et saisissez le code ci-dessous dans la section **Policy Document**. Assurez-vous de remplacer `INSERTBUCKETNAME` par votre propre nom de segment.

{% tabs %}
{% tab Braze Currents %}

```json
{
  "Version": "2012-10-17",
  "Statement": [
    { "Effet": "Autoriser",
      "Action": ["s3:GetBucketLocation"],
      "Ressource": ["arn:aws:s3:::INSERTBUCKETNA"]
    }
    ,
    { "Effet": "Autoriser",
      "Action": ["s3:PutObject", "s3:Bucket"],
      "Ressource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
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
            "Effet": "Autorisation",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Ressource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effet": "Autoriser",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Ressource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

### Étape 4 : Joindre une politique {#secret-key-4}

Une fois que votre politique a été créée, accédez à « Utilisateurs » puis cliquez sur votre utilisateur spécifique afin que vous puissiez joindre cette nouvelle politique. Dans l'onglet "Autorisations", cliquez sur "Attacher la politique".

!\[Joindre un utilisateur\]\[13\]

Recherchez la nouvelle politique que vous avez créée et cliquez pour la joindre.

Vous êtes maintenant prêt à lier vos identifiants AWS à votre compte Braze.

### Étape 5 : Lier Braze à AWS {#secret-key-5}

{% tabs %}
{% tab Braze Currents %}

Naviguez vers la page **courants** sur le tableau de bord de Braze sous la section **Intégrations** cliquez sur le menu déroulant **Create Current** et sélectionnez **Amazon S3 Data Export**.

![AWS Creds]({{site.baseurl}}/assets/img/currents-s3-example.png)

Donne un nom à l'actuel. Ensuite, dans la section **Identifiants** , assurez-vous que le bouton radio **AWS Secret Access Key** est sélectionné, puis entrez votre **ID d'accès AWS**, **Clé d'accès secrète AWS**, et **AWS S3 Bucket Name** dans les champs désignés.

{% alert warning %}
Gardez à jour votre ID de clé d'accès AWS et votre clé d'accès secret AWS. Si les identifiants de votre connecteur expirent, le connecteur arrêtera d'envoyer des événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

Vous pouvez également ajouter les personnalisations suivantes, en fonction de vos besoins :

-   Chemin du dossier (par défaut, `courants`)
-   Server-Side, At-Rest AES-256 Encryption (par défaut OFF) - Inclut l'en-tête "x-amz-server-side-encryption"

Cliquez sur **Lancer le** pour continuer.

Une notification vous informera si vos identifiants ont été validés avec succès. AWS S3 devrait maintenant être mis en place pour les courants de Braze.

{% endtab %}
{% tab Dashboard Data Export %}

Naviguez vers la page **Partenaires Technologiques** sur le tableau de bord de Braze sous la section **Intégrations** et cliquez sur **Amazon S3**.

![AWS Creds]({{site.baseurl}}/assets/img/s3_tech_partners.png)

Sur la page des identifiants AWS, assurez-vous que le bouton radio **AWS Secret Access Key** est sélectionné, saisissez ensuite votre ID d'accès AWS, votre clé d'accès secret AWS et votre nom de segment AWS S3 dans les champs désignés. Lorsque vous saisissez votre clé secrète, cliquez sur **Tester les identifiants** d'abord pour vous assurer que vos identifiants fonctionnent, puis cliquez sur **Enregistrer** une fois que cela a réussi.

{% alert tip %}
Vous pouvez toujours récupérer de nouveaux identifiants en naviguant vers votre utilisateur et en cliquant sur **Créer une clé d'accès** dans l'onglet **Identifiants de sécurité** dans la console AWS.
{% endalert %}

Une notification vous informera si vos identifiants ont été validés avec succès. AWS S3 devrait maintenant être intégré à votre compte Braze.

{% endtab %}
{% endtabs %}

## Méthode d'authentification ARN du rôle AWS

Cette méthode d'authentification génère un rôle ARN (Amazon Resource Name) qui permet au compte Amazon de Braze de s'authentifier en tant que membre du rôle que vous avez créé pour écrire des données dans votre compartiment.

### Étape 1 : Créer une politique {#role-arn-1}

Pour commencer, connectez-vous à la console de gestion AWS en tant qu'administrateur du compte. Naviguez vers la section IAM de la console AWS, cliquez sur **Politiques** dans la barre de navigation, et cliquez sur **Créer une politique**.

![Rôle ARN]({{site.baseurl}}/assets/img/create_policy_1_list.png)

Ouvrez l'onglet **JSON** et entrez le code ci-dessous dans la section **Policy Document**. Assurez-vous de remplacer `INSERTBUCKETNAME` par votre propre nom de segment. Cliquez sur **Politique de revue** lorsque vous avez terminé.

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effet": "Autorisation",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Ressource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effet": "Autoriser",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Ressource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
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
            "Effet": "Autorisation",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Ressource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effet": "Autoriser",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Ressource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

Ensuite, donnez à la politique un nom et une description et cliquez sur **Créer une politique**.

![Rôle ARN]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![Rôle ARN]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Étape 2 : Créer un rôle {#role-arn-2}

Maintenant, toujours dans la section IAM de la Console AWS, cliquez sur **Rôles** dans la barre de navigation et cliquez sur **Créer un rôle**.

![Rôle ARN]({{site.baseurl}}/assets/img/create_role_1_list.png)

Récupérez votre **ID de compte Braze** et **ID externe** de votre compte Braze.

{% tabs %}
{% tab Braze Currents %}

Accédez à la page **courants** de votre compte Braze dans la section **Intégrations** cliquez sur le menu déroulant **Create Current** et sélectionnez **Amazon S3 Data Export**.

![AWS Creds]({{site.baseurl}}/assets/img/currents-role-arn.png)

{% endtab %}
{% tab Dashboard Data Export %}

Accédez à la page **Partenaires Technologiques** de votre compte Braze dans la section **Intégrations** et cliquez sur **Amazon S3**.

![AWS Creds]({{site.baseurl}}/assets/img/data-export-role-arn.png)

{% endtab %}
{% endtabs %}

De retour sur la console AWS, sélectionnez **Un autre compte AWS** à partir du type de sélecteur d'entité de confiance. Entrez le **ID de compte Braze**, vérifiez **Nécessite un ID externe**et entrez le **ID externe Braze**. Cliquez sur "**Suivant** une fois terminé.

![Rôle ARN]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Étape 3 : Joindre une politique {#role-arn-3}

Ensuite, joignez la politique que vous avez créée plus tôt au rôle. Recherchez la politique dans la barre de recherche et placez une coche à côté de la politique pour la joindre. Cliquez sur **Suivant** une fois terminé.

![Rôle ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Donnez au Rôle un nom et une description, et cliquez sur **Créer un Rôle**.

![Rôle ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

Vous devriez maintenant voir votre nouveau rôle dans la liste.

### Étape 4 : Lier pour briser AWS {#role-arn-4}

Toujours sur la console AWS, trouvez votre nouveau rôle dans la liste. Cliquez sur le nom pour ouvrir les détails de ce rôle.

![Rôle ARN]({{site.baseurl}}/assets/img/create_role_5_created.png)

Prenez note du "Rôle ARN" en haut du résumé (cliquez sur l'icône à copier dans le presse-papier.)

![Rôle ARN]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Retournez à votre compte Braze et copiez le Rôle ARN dans le champ fourni.

{% tabs %}
{% tab Braze Currents %}

Accédez à la page **courants** de votre compte Braze dans la section **Intégrations** cliquez sur le menu déroulant **Create Current** et sélectionnez **Amazon S3 Data Export**.

![AWS Creds]({{site.baseurl}}/assets/img/currents-role-arn.png)

Donne un nom à l'actuel. Ensuite, dans la section **Identifiants** , assurez-vous que le bouton radio **AWS Rôle ARN** est sélectionné, puis entrez votre rôle ARN et AWS S3 Bucket Name dans les champs désignés.

Vous pouvez également ajouter les personnalisations suivantes, en fonction de vos besoins :

-   Chemin du dossier (par défaut, `courants`)
-   Server-Side, At-Rest AES-256 Encryption (par défaut OFF) - Inclut l'en-tête "x-amz-server-side-encryption"

Cliquez sur **Lancer le** pour continuer.

Une notification vous informera si vos identifiants ont été validés avec succès. AWS S3 devrait maintenant être mis en place pour les courants de Braze.

{% alert important %}
Si vous recevez une erreur “Les identifiants S3 sont invalides”, cela peut être dû à une intégration trop rapide après avoir créé un rôle dans AWS. Veuillez patienter et réessayer.
{% endalert %}

{% endtab %}
{% tab Dashboard Data Export %}

Accédez à la page **Partenaires Technologiques** de votre compte Braze dans la section **Intégrations** et cliquez sur **Amazon S3**.

![AWS Creds]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Sur la page des identifiants **AWS** , assurez-vous que le bouton radio **AWS Rôle ARN** est sélectionné, puis entrez votre rôle ARN et AWS S3 Bucket Name dans les champs désignés. Cliquez sur **Tester les identifiants** d'abord pour vous assurer que vos identifiants fonctionnent correctement, puis cliquez sur **Enregistrer** une fois que cela est réussi.

{% alert tip %}
Vous pouvez toujours récupérer de nouveaux identifiants en naviguant vers votre utilisateur et en cliquant sur **Créer une clé d'accès** dans l'onglet **Identifiants de sécurité** dans la console AWS.
{% endalert %}

Une notification vous informera si vos identifiants ont été validés avec succès. AWS S3 devrait maintenant être intégré à votre compte Braze.

{% endtab %}
{% endtabs %}
[11]: {% image_buster /assets/img_archive/S3_Credentials.png %} [12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %} [13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
