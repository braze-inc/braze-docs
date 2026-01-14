---
nav_title: "Exportation d'événements de sécurité avec S3"
article_title: Paramètres de sécurité Exportation avec S3
page_order: 1
page_type: reference
description: "Cet article de référence explique comment exporter automatiquement les événements de sécurité tous les jours à minuit UTC vers Amazon S3."
---

# Exportation d'événements de sécurité avec Amazon S3

> Vous pouvez exporter automatiquement les événements de sécurité vers Amazon S3, un fournisseur de stockage en nuage, à l'aide d'une tâche quotidienne qui s'exécute à minuit UTC. Après la configuration, vous n'aurez plus besoin d'exporter manuellement les événements de sécurité à partir du tableau de bord. Cette tâche exportera les événements de sécurité des dernières 24 heures au format CSV vers votre espace de stockage S3 configuré. Le fichier CSV aura la même structure qu'un rapport exporté manuellement.

Braze prend en charge deux méthodes d'authentification et d'autorisation S3 différentes pour configurer l'exportation Amazon S3 :

- Méthode de clé d'accès au secret AWS
- Rôle AWS Méthode ARN

## Méthode de clé d'accès au secret AWS

Cette méthode génère une clé secrète et un ID de clé d'accès qui permet à Braze de s'authentifier en tant qu'utilisateur sur votre compte AWS pour écrire des données dans votre compartiment.

### Étape 1 : Créer un message in-app utilisateur

Pour récupérer votre clé d'accès secrète et votre ID de clé d'accès, vous devrez créer un utilisateur de message in-app, en suivant les instructions de la section [Configuration de votre compte AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Étape 2 : Obtenir des informations d'identification

1. Après avoir créé un nouvel utilisateur, générez la clé d'accès et téléchargez votre ID de clé d'accès et votre clé d'accès secrète.

\![Une page de résumé pour un rôle appelé "liyu-chen-test".]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2\. Notez ces informations d'identification quelque part ou téléchargez les fichiers d'informations d'identification, car vous devrez les saisir dans Braze par la suite.

\![Champs contenant la clé d'accès et la clé d'accès secrète.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Étape 3 : Créer une politique

1. Allez dans **IAM** > **Politiques** > **Créer une politique** pour ajouter des autorisations à votre utilisateur. 
2. Sélectionnez **Créer votre propre politique**, qui donne des autorisations limitées afin que Braze ne puisse accéder qu'aux compartiments spécifiés.
3. Indiquez le nom de la police de votre choix.
4. Saisissez l'extrait de code suivant dans la section **Document de politique générale**. Veillez à remplacer "INSERTBUCKETNAME" par le nom de votre compartiment. Sans ces autorisations, l'intégration échouera lors de la vérification des informations d'identification et ne sera pas créée.

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

### Étape 4 : Joindre la politique

1. Après avoir créé une nouvelle politique, allez dans **Utilisateurs** et sélectionnez votre utilisateur spécifique. 
2. Dans l'onglet **Autorisations**, sélectionnez **Ajouter des autorisations**, attachez directement la politique, puis sélectionnez cette politique. 

Vous êtes maintenant prêt à lier vos identifiants AWS à votre compte Braze !

### Étape 5 : Lier Braze à AWS

1. Dans Braze, allez dans **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et faites défiler jusqu'à la section **Téléchargement des événements de sécurité.** 
2. Basculez sur **Export to AWS S3** sous **Export to cloud storage** et sélectionnez la **clé d'accès secrète AWS**, ce qui active l'exportation S3. 
3. Saisissez les informations suivantes :
- ID de la clé d'accès AWS
- Clé d'accès secrète AWS
    - Lorsque vous saisissez cette clé, sélectionnez d'abord **Test Credentials** pour confirmer que vos informations d'identification fonctionnent.
- Nom du compartiment AWS 

La page "Security Event Download" avec les ID externes et de compte Braze renseignés.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4\. Sélectionnez **Enregistrer les modifications**. 

\![ Bouton "Enregistrer les modifications".]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

Vous avez intégré AWS S3 à votre compte Braze !

## Rôle AWS Méthode ARN

La méthode AWS role ARN génère un nom de ressource Amazon (ARN) de rôle qui permet au compte Braze Amazon de s'authentifier en tant que membre de ce rôle.

### Étape 1 : Créer une politique

1. Connectez-vous à la console de gestion AWS en tant qu'administrateur de compte. 
2. Dans la console AWS, accédez à la section **IAM** > **Politiques**, puis sélectionnez **Créer une politique.**

Une page avec une liste de politiques et un bouton pour "Créer une politique".]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3\. Ouvrez l'onglet **JSON** et saisissez l'extrait de code suivant dans la section **Policy Document.**  Veillez à remplacer `INSERTBUCKETNAME` par le nom de votre compartiment. 

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

{: start="4"}
4\. Sélectionnez " **Suivant"** après avoir examiné la politique.

Une page qui vous permet de revoir votre politique et éventuellement d'ajouter des autorisations.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5\. Donnez un nom et une description à la politique, puis sélectionnez **Créer une politique.**

Une page pour réviser et créer votre politique.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Étape 2 : Créer un rôle

1. Dans Braze, allez dans **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et faites défiler jusqu'à la section **Téléchargement des événements de sécurité.**  
2. Sélectionnez **AWS Role ARN**. 
3. Prenez note des identifiants, de l'ID de compte Braze et de l'ID externe Braze nécessaires à la création de votre rôle.

La page "Security Event Download" avec les ID externes et de compte Braze renseignés.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. Dans la console AWS, allez dans la section **IAM** > **Roles** > **Create Role.** 
5. Sélectionnez **Un autre compte AWS** comme type de sélecteur d'entité de confiance. 
6. Indiquez votre ID de compte Braze, cochez la case **Require external ID**, puis saisissez votre ID externe Braze. 
7. Sélectionnez **Suivant** lorsque vous avez terminé.

Une page avec des options permettant de sélectionner un type d'entité de confiance et de fournir des informations sur votre compte AWS.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Étape 3 : Joindre la politique

1. Recherchez la politique que vous avez créée précédemment dans la barre de recherche, puis cochez-la pour la joindre. 
2. Sélectionnez **Suivant.**

\![Une liste de politiques avec des colonnes pour leur type et leur description.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3\. Donnez un nom et une description au rôle, puis sélectionnez **Créer un rôle**.

\![Champs permettant de fournir des détails sur le rôle, tels que le nom, la description, la politique de confiance, les autorisations et les tags.]({% image_buster /assets/img/security_export/name_review_create.png %})

Votre rôle nouvellement créé apparaîtra dans la liste !

### Étape 4 : Lien vers Braze AWS

1. Dans la console AWS, trouvez votre rôle nouvellement créé dans la liste. Sélectionnez le nom pour ouvrir les détails de ce rôle et notez l'**ARN**.

\![La page de résumé d'un rôle appelé "security-event-export-olaf".]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2\. Dans Braze, allez dans **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et faites défiler jusqu'à la section **Téléchargement des événements de sécurité.** 

\!["Téléchargement des événements de sécurité" avec une bascule activée pour "Exporter vers AWS S3".]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3\. Assurez-vous que l'ARN **du rôle AWS** est sélectionné, puis saisissez l'ARN de votre rôle et le nom du compartiment AWS S3 dans les champs désignés.
4\. Sélectionnez **Tester les informations d'identification** pour confirmer que vos informations d'identification fonctionnent correctement.
5\. Sélectionnez **Enregistrer les modifications**. 

\![ Bouton "Enregistrer les modifications".]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

Vous avez intégré AWS S3 à votre compte Braze !