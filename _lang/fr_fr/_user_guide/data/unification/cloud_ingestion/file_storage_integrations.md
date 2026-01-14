---
nav_title: Intégrations de stockage de fichiers
article_title: Intégrations de stockage de fichiers
description: "Cette page traite de l'ingestion de données dans le cloud Braze et de la synchronisation des données pertinentes de S3 vers Braze."
page_order: 3
page_type: reference

---

# Intégrations de stockage de fichiers

> Cette page explique comment configurer la prise en charge de l'ingestion de données dans le cloud et synchroniser les données pertinentes de S3 vers Braze.

## Comment cela fonctionne-t-il ?

Vous pouvez utiliser Cloud Data Ingestion (CDI) for S3 pour intégrer directement un ou plusieurs compartiments S3 de votre compte AWS à Braze. Lorsque de nouveaux fichiers sont publiés sur S3, un message est envoyé à SQS et Braze Cloud Data Ingestion prend en charge ces nouveaux fichiers. 

L'ingestion de données dans le nuage prend en charge les éléments suivants :

- Fichiers JSON
- fichiers CSV
- Fichiers Parquet
- Attribut, événement personnalisé, événement d'achat, suppression d'utilisateur et données de catalogue.

## Conditions préalables

L'intégration nécessite les ressources suivantes :

 - Compartiment S3 pour le stockage des données 
 - File d'attente SQS pour les notifications de nouveaux fichiers 
 - Rôle IAM pour l'accès à Braze  

### Définitions AWS

Tout d'abord, définissons certains des termes utilisés dans le cadre de cette tâche.

| Durée | Définition |
| --- | --- |
| Nom de ressource Amazon (ARN) | L'ARN est un identifiant unique pour les ressources AWS. |
| Gestion des identités et des accès (IAM) | IAM est un service web qui vous permet de contrôler en toute sécurité l'accès aux ressources AWS. Dans ce tutoriel, vous allez créer une politique IAM et l'attribuer à un rôle IAM pour intégrer votre compartiment S3 à Braze Cloud Data Ingestion. |
| Amazon Simple Queue Service (SQS) | SQS est une file d'attente hébergée qui vous permet d'intégrer des systèmes et des composants logiciels distribués. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuration de l'ingestion de données dans le nuage (Cloud Data Ingestion) dans AWS

### Étape 1 : Créer un compartiment source

Créez un compartiment S3 à usage général avec les paramètres par défaut dans votre compte AWS. Les compartiments S3 peuvent être réutilisés d'une synchronisation à l'autre, à condition que le dossier soit unique.

Les paramètres par défaut sont les suivants :

- ACL désactivés
- Bloquer tout accès public
- Désactiver le versionnement des compartiments
- Cryptage SSE-S3

Prenez note de la région dans laquelle vous avez créé le compartiment, car vous créerez une file d'attente SQS dans la même région à l'étape suivante.

### Étape 2 : Créer une file d'attente SQS

Créez une file d'attente SQS pour suivre l'ajout d'objets dans le compartiment que vous avez créé. Utilisez pour l'instant les paramètres de configuration par défaut. 

Une file d'attente SQS doit être unique au niveau mondial (par exemple, une seule peut être utilisée pour une synchronisation CDI et ne peut pas être réutilisée dans un autre espace de travail).

{% alert important %}
Veillez à créer ce SQS dans la même région que celle dans laquelle vous avez créé le compartiment.
{% endalert %}

Veillez à noter l'ARN et l'URL du SQS, car vous les utiliserez fréquemment au cours de cette configuration.

\![Sélection de "Avancé" avec un exemple d'objet JSON pour définir qui peut accéder à une file d'attente.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Étape 3 : Mise en place d'une politique d'accès

Pour configurer la politique d'accès, sélectionnez **Options avancées.** 

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

### Étape 4 : Ajouter une notification d'événement au compartiment S3

1. Dans le compartiment créé à l'étape 1, allez dans **Propriétés** > **Notifications d'événements.**
2. Donnez un nom à la configuration. Vous pouvez également spécifier un préfixe ou un suffixe à cibler si vous souhaitez que seul un sous-ensemble de fichiers soit ingéré par Braze.
3. Sous **Destination**, sélectionnez **File d'attente SQS** et indiquez l'ARN du SQS que vous avez créé à l'étape 2.

{% alert note %}
Si vous téléchargez vos fichiers dans le dossier racine d'un compartiment S3, puis que vous déplacez certains de ces fichiers vers un dossier spécifique du compartiment, vous risquez de rencontrer une erreur inattendue. Au lieu de cela, vous pouvez modifier les notifications d'événements pour qu'elles soient envoyées uniquement pour les fichiers du préfixe, éviter de placer des fichiers dans le compartiment S3 en dehors de ce préfixe, ou mettre à jour l'intégration sans préfixe, qui ingérera alors tous les fichiers.
{% endalert %}

### Étape 5 : Créer une politique IAM

Créez une politique IAM pour permettre à Braze d'interagir avec votre compartiment source. Pour commencer, connectez-vous à la console de gestion AWS en tant qu'administrateur de compte. 

1. Allez dans la section IAM de la console AWS, sélectionnez **Politiques** dans la barre de navigation, puis sélectionnez **Créer une politique.**<br><br>\![Le bouton "Créer une politique" dans la console AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

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

4. Donnez un nom et une description à la politique, puis sélectionnez **Créer une politique**.  

\![Un exemple de politique nommée "nouveau-nom-de-politique".]({% image_buster /assets/img/create_policy_3_name.png %})

\![Champ de description de la politique.]({% image_buster /assets/img/create_policy_4_created.png %})

### Étape 6 : Créer un rôle IAM

Pour terminer la configuration sur AWS, vous allez créer un rôle IAM et y attacher la politique IAM de l'étape 4. 

1. Dans la même section IAM de la console où vous avez créé la politique IAM, allez dans **Rôles** > **Créer un rôle**. 

<br><br>\![Le bouton "Créer un rôle".]({% image_buster /assets/img/create_role_1_list.png %})<br><br>

{: start="2"}
2\. Copiez l'ID du compte AWS de Braze à partir de votre tableau de bord de Braze. Accédez à **Cloud Data Ingestion**, sélectionnez **Create New Data Sync (Créer une nouvelle synchronisation de données)**, puis sélectionnez **S3 Import (Importer S3)**.

3. Dans AWS, sélectionnez **Un autre compte AWS** comme type de sélecteur d'entité de confiance. Indiquez votre ID de compte Braze. Cochez la case **Require external ID** et saisissez un ID externe à utiliser par Braze. Il s'agit de l'ID externe généré lors de la création d'une connexion S3 Currents dans la section **Credentials** de votre connexion Currents dans le tableau de bord de Braze. Sélectionnez **Suivant** lorsque vous avez terminé. 

<br><br> \![La page S3 "Create Role" (Créer un rôle). Cette page comporte des champs pour le nom du rôle, la description du rôle, les entités de confiance, les politiques et les limites des autorisations.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="4"}
4\. Attachez la politique créée à l'étape 4 au rôle. Recherchez la police dans la barre de recherche et cochez la case à côté de la police pour la joindre. Sélectionnez **Suivant** lorsque vous avez terminé.

<br><br>\![Rôle ARN avec le nouveau nom de politique sélectionné.]({% image_buster /assets/img/create_role_3_attach.png %})<br><br>

Donnez un nom et une description au rôle, puis sélectionnez **Créer un rôle**.

<br><br>\![Un exemple de rôle nommé "nouveau-nom-de-rôle".]({% image_buster /assets/img/create_role_4_name.png %})<br><br>

{: start="5"}
5\. Prenez note de l'ARN du rôle que vous venez de créer et de l'ID externe que vous avez généré, car vous les utiliserez pour créer l'intégration Cloud Data Ingestion.

## Configurer l'ingestion de données dans Braze

1. Pour créer une nouvelle intégration, accédez à **Paramètres des données** > **Ingestion de données dans le cloud**, sélectionnez **Créer une nouvelle synchronisation de données**, puis sélectionnez **Importation S3** dans la section des sources de fichiers. 
2. Saisissez les informations issues du processus de configuration d'AWS pour créer une nouvelle synchronisation. Précisez les éléments suivants :

  - Rôle ARN
  - ID externe
  - URL SQS (doit être unique pour chaque nouvelle intégration)
  - Nom du compartiment
  - Chemin d'accès au dossier (facultatif, doit être unique pour toutes les synchronisations d'un espace de travail)
  - Région

\![Exemple d'identifiants de sécurité tels qu'affichés dans S3 pour créer une nouvelle synchronisation d'importation.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. Donnez un nom à votre intégration et sélectionnez le type de données pour cette intégration. 

<br><br>\![Configuration des détails de synchronisation pour "cdi-s3-as-source-integration" avec les attributs de l'utilisateur comme type de données.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

{: start="4"}
4\. Ajoutez un e-mail de contact pour recevoir des notifications si la synchronisation est interrompue en raison de problèmes d'accès ou de permissions. Si vous le souhaitez, vous pouvez activer les notifications pour les erreurs au niveau de l'utilisateur et les réussites de synchronisation. 

<br><br> \![Configuration des préférences de notification des erreurs de synchronisation.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\. Enfin, testez la connexion et enregistrez la synchronisation. 

<br><br>Une option pour tester la connexion avec un aperçu des données.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

## Formats de fichiers requis

Cloud Data Ingestion prend en charge les fichiers JSON, CSV et Parquet. Chaque fichier doit contenir une ou plusieurs des colonnes d'identifiants prises en charge et une colonne de charge utile sous forme de chaîne de caractères JSON.

Braze n'impose pas d'exigences supplémentaires en matière de noms de fichiers en plus de celles imposées par AWS. Les noms de fichiers doivent être uniques. Nous vous recommandons d'ajouter un horodatage pour garantir l'unicité.

### Identifiants des utilisateurs

Votre fichier source peut contenir une ou plusieurs colonnes ou clés d'identification de l'utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant, mais un fichier source peut avoir plusieurs types d'identifiants.

| Identifiant | Description |
| --- | --- |
| `EXTERNAL_ID` | Il identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur devrait correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`. |
| `BRAZE_ID` | L'identifiant de l'utilisateur de Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID de Braze par le biais de l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, indiquez un ID externe ou un alias d'utilisateur. |
| `EMAIL` | L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour sera prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, nous utiliserons l'e-mail comme identifiant principal. |
| `PHONE` | Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour sera mis à jour en priorité. |
|`PAYLOAD` | Il s'agit d'une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Contrairement aux sources de l'entrepôt de données, la colonne `UPDATED_AT` n'est ni obligatoire ni prise en charge.
{% endalert %}

{% tabs %}
{% tab JSON Attributes %}
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
{% tab JSON Custom Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext  
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}" 
1,"{""product_name"": ""Product 1"", ""price"": 1.01}" 
```
{% endtab %}

{% endtabs %}  

Pour obtenir des exemples de tous les types de fichiers pris en charge, consultez les fichiers d'exemple dans [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).  

## Ce qu'il faut savoir

- Les fichiers ajoutés au compartiment S3 ne doivent pas dépasser 512 Mo. Les fichiers de plus de 512 Mo entraîneront une erreur et ne seront pas synchronisés sur Braze.
- Bien qu'il n'y ait pas de limite supplémentaire au nombre de lignes par fichier, nous vous recommandons d'utiliser des fichiers plus petits pour améliorer la rapidité de vos synchronisations. Par exemple, l'ingestion d'un fichier de 500 Mo prendrait beaucoup plus de temps que celle de cinq fichiers distincts de 100 Mo.
- Il n'y a pas de limite supplémentaire au nombre de fichiers téléchargés dans un temps donné.
- Il n'est pas possible de passer des commandes dans ou entre les fichiers. Nous vous recommandons de mettre périodiquement les mises à jour en lots si vous surveillez les conditions de concurrence attendues.

## Résolution des problèmes

### Téléchargement de fichiers et traitement

CDI ne traitera que les fichiers ajoutés après la création de la synchronisation. Au cours de ce processus, Braze recherche de nouveaux fichiers à ajouter, ce qui déclenche un nouvel envoi déclenché à SQS. Cela déclenchera une nouvelle synchronisation pour traiter le nouveau fichier.

Les fichiers existants peuvent être utilisés pour valider la structure des données dans la connexion de test, mais ils ne seront pas synchronisés avec Braze. Tous les fichiers existants qui doivent être synchronisés doivent être retéléchargés sur S3 pour être traités par le CDI.

### Gestion des erreurs de fichiers inattendues

Si vous observez un nombre élevé d'erreurs ou de fichiers échoués, il se peut qu'un autre processus ajoute des fichiers au compartiment S3 dans un dossier autre que le dossier cible pour CDI.

Lorsque des fichiers sont téléchargés dans le compartiment source mais pas dans le dossier source, CDI traite la notification SQS, mais n'entreprend aucune action sur le fichier, ce qui peut apparaître comme une erreur.
