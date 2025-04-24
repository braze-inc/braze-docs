---
nav_title: Intégrations de stockage de fichiers
article_title: Intégrations de stockage de fichiers
description: "Cette page traite de l'ingestion de données dans le cloud de Braze et explique comment synchroniser les données pertinentes de S3 vers Braze"
page_order: 3
page_type: reference

---

# Intégrations de stockage de fichiers

> Cette page explique comment configurer la prise en charge de l'ingestion de données dans le cloud et synchroniser les données pertinentes de S3 vers Braze.

Vous pouvez utiliser Cloud Data Ingestion (CDI) for S3 pour intégrer directement un ou plusieurs compartiments S3 de votre compte AWS à Braze. Lorsque de nouveaux fichiers sont publiés dans S3, un message est envoyé à SQS et Cloud Data Ingestion de Braze prend en charge ces nouveaux fichiers. 

Cloud Data Ingestion prend en charge les fichiers JSON, CSV et Parquet, ainsi que les données relatives aux attributs, aux événements, aux achats et à la suppression d'utilisateurs.

L'intégration nécessite les ressources suivantes :
 - Compartiment S3 pour le stockage des données 
 - File d'attente SQS pour les notifications de nouveaux fichiers 
 - Rôle IAM pour l'accès à Braze  


## Définitions AWS

Tout d'abord, définissons certains des termes utilisés dans le cadre de cette tâche.

| Terme | Définition |
| --- | --- |
| Nom de ressource Amazon (ARN) | L'ARN est un identifiant unique pour les ressources AWS. |
| Gestion des identités et des accès (IAM) | IAM est un service Web qui vous permet de contrôler, en toute sécurité, l'accès aux ressources AWS. Dans ce tutoriel, vous allez créer une politique IAM et l'attribuer à un rôle IAM pour intégrer votre compartiment S3 à Cloud Data Ingestion de Braze. |
| Amazon Simple Queue Service (SQS) | SQS est une file d'attente hébergée qui vous permet d'intégrer des systèmes et des composants logiciels distribués. |
{: .reset-td-br-1 .reset-td-br-2 }
 

## Configuration de l'ingestion de données Cloud dans AWS

### Étape 1 : Créer un compartiment source

Créez un compartiment S3 à usage général avec les paramètres par défaut dans votre compte AWS. 

Les paramètres par défaut sont les suivants :
  - ACL désactivés
  - Bloquer tout accès public
  - Désactiver la gestion des versions des compartiments
  - Chiffrement SSE-S3

Prenez note de la région dans laquelle vous avez créé le compartiment, car vous allez créer une file d'attente SQS dans la même région à l'étape suivante.

### Étape 2 : Créer une file d'attente SQS

Créez une file d'attente SQS pour suivre l'ajout d'objets dans le compartiment que vous avez créé. Utilisez pour l'instant les paramètres de configuration par défaut.

{% alert important %}
Veillez à créer ce SQS dans la même région que celle où vous avez créé le compartiment.
{% endalert %}

Veillez à noter l'ARN et l'URL du SQS, car vous les utiliserez fréquemment au cours de cette configuration.
<br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})
<br><br>

### Étape 3 : Configurer une politique d'accès

Pour configurer la politique d'accès, sélectionnez **Options avancées**. 

Ajoutez la déclaration suivante à la politique d'accès de la file d'attente, en prenant soin de remplacer `YOUR-BUCKET-NAME-HERE` par le nom de votre compartiment, et `YOUR-SQS-ARN` par l'ARN de votre file d'attente SQS, et `YOUR-AWS-ACCOUNT-ID` par l'ID de votre compte AWS : 

``` json 
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
} 
```

### Étape 4 : Ajouter une notification d'événement au compartiment S3

1. Dans le compartiment créé à l'étape 1, allez dans **Propriétés** > **Notifications d'événements.**

2. Donnez un nom à la configuration. Vous pouvez également spécifier un préfixe ou un suffixe à cibler si vous souhaitez que seul un sous-ensemble de fichiers soit ingéré par Braze.

3. Sous **Destination**, sélectionnez **File d'attente SQS** et indiquez l'ARN de la file d'attente SQS que vous avez créée à l'étape 2.

### Étape 5 : Créer une politique IAM

Créez une politique IAM pour permettre à Braze d'interagir avec votre compartiment source. Pour commencer, connectez-vous à la console de gestion AWS en tant qu’administrateur de compte. 

1. Allez dans la section IAM de la console AWS, sélectionnez **Politiques** dans la barre de navigation, puis cliquez sur **Créer une politique**.<br><br>![]({{site.baseurl}}/assets/img/create_policy_1_list.png)<br><br>

2. Ouvrez l'onglet **JSON** et saisissez l'extrait de code suivant dans la section **Policy Document**, en prenant soin de remplacer `YOUR-BUCKET-NAME-HERE` par le nom de votre compartiment et `YOUR-SQS-ARN-HERE` par le nom de votre file d'attente SQS : 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```  

{: start="3"}
3\. Sélectionnez **Réviser la politique** lorsque vous avez terminé.

4. Donnez un nom et une description à la politique et sélectionnez **Créer une politique**.  

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Étape 6 : Créer un rôle IAM

Pour terminer la configuration sur AWS, vous allez créer un rôle IAM et y associer la politique IAM de l'étape 4. 

1. Dans la même section IAM de la console où vous avez créé la politique IAM, allez dans **Rôles** > **Créer un rôle**. <br><br>![]({{site.baseurl}}/assets/img/create_role_1_list.png)<br><br>

2. Copiez l'ID du compte AWS de Braze à partir de votre tableau de bord de Braze. Accédez à l'**ingestion de données dans le cloud**, cliquez sur **Créer une nouvelle synchronisation de données** et sélectionnez **Importation S3**. <br><br>![]({{site.baseurl}}/assets/img/cloud_ingestion/s3_copy_braze_account_id.png)<br><br>

3. Dans AWS, sélectionnez **Another AWS Account (Autre compte AWS)** comme type de sélecteur d'entité de confiance. Indiquez votre ID de compte Braze, cochez la case **Require external ID (Exiger un ID externe)** et saisissez un ID externe que Braze pourra utiliser. Sélectionnez **Suivant** lorsque vous avez terminé. <br><br> ![Page S3 « Create Role (Créer un rôle) ». Cette page comporte des champs pour le nom du rôle, la description du rôle, les entités de confiance, les politiques et les restrictions d’autorisations.]({{site.baseurl}}/assets/img/create_role_2_another.png)

4. Attachez la politique créée à l'étape 4 au rôle. Recherchez la police dans la barre de recherche et cochez la case à côté de la police pour la joindre. Sélectionnez **Suivant** lorsque vous avez terminé.<br><br>![ARN du rôle]({{site.baseurl}}/assets/img/create_role_3_attach.png)<br><br>Donnez un nom et une description au rôle, puis cliquez sur **Create Role (Créer un rôle)**.<br><br>![ARN du rôle]({{site.baseurl}}/assets/img/create_role_4_name.png)<br><br>

{: start="5"}
5\. Prenez note de l'ARN du rôle que vous venez de créer et de l'ID externe que vous avez généré, car vous les utiliserez pour créer l'intégration de l’ingestion de données Cloud.  

## Configuration de Cloud Data Ingestion dans Braze

1. Pour créer une nouvelle intégration, accédez à **Paramètres des données** > **Ingestion de données dans le cloud**, sélectionnez **Créer une nouvelle synchronisation de données**, puis sélectionnez **Importation S3** dans la section des sources de fichiers. 

2. Saisissez les informations issues du processus de configuration d'AWS pour créer une nouvelle synchronisation. Précisez les éléments suivants :
- ARN du rôle
- ID externe
- URL SQS (doit être unique pour chaque nouvelle intégration)
- Nom du compartiment
- Chemin d'accès au dossier (facultatif)
- Région  

![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. Donnez un nom à votre intégration et sélectionnez le type de données pour cette intégration. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

4. Ajoutez un e-mail de contact pour recevoir des notifications si la synchronisation est interrompue en raison de problèmes d'accès ou de permissions. Si vous le souhaitez, vous pouvez activer les notifications pour les erreurs au niveau de l'utilisateur et les réussites de synchronisation. <br><br> ![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\. Enfin, testez la connexion et enregistrez la synchronisation. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})


## Formats de fichiers requis

Cloud Data Ingestion prend en charge les fichiers JSON, CSV et Parquet. Chaque fichier doit contenir une ou plusieurs colonnes d'identifiants prises en charge, ainsi qu'une colonne de données utiles sous la forme d'une chaîne de caractères JSON. 

- Identifiants des utilisateurs. Votre fichier source peut contenir une ou plusieurs colonnes ou clés d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant, mais un fichier source peut avoir plusieurs types d'identifiants. 
    - `EXTERNAL_ID` : Ceci identifie l’utilisateur que vous désirez mettre à jour. Cela doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`.
    - `BRAZE_ID` : L’identifiant d’utilisateur Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité. 
- `PAYLOAD` : Il s’agit d’une chaîne de caractères JSON des champs que vous désirez synchroniser à l’utilisateur dans Braze.

{% alert note %}
Contrairement aux sources de l'entrepôt de données, la colonne `UPDATED_AT` n'est ni nécessaire ni prise en charge.
{% endalert %}

{% alert note %}
Les fichiers ajoutés au compartiment source S3 ne doivent pas dépasser 512 Mo. Les fichiers de plus de 512 Mo entraîneront une erreur et ne seront pas synchronisés sur Braze.
{% endalert %}

{% tabs %}
{% tab Attributs JSON %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```  
{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}
{% endtab %}
{% tab Événements personnalisés JSON %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}
{% endtab %}
{% tab Événements d'achat JSON %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}

{% endtab %}
{% tab Attributs CSV %}
``` csv  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% endtabs %}  

Pour obtenir des exemples de tous les types de fichiers pris en charge, veuillez consulter les fichiers d'exemple dans [braze-examples.](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage)  
