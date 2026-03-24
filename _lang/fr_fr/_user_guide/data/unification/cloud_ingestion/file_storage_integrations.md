---
nav_title: Intégrations de stockage de fichiers
article_title: Intégrations de stockage de fichiers
description: "Cette page traite de l'ingestion de données dans le cloud Braze et de la synchronisation des données pertinentes de S3 vers Braze."
page_order: 3
page_type: reference

---

# Intégrations de stockage de fichiers

> Cette page explique comment configurer la prise en charge de l'ingestion de données dans le cloud et synchroniser les données pertinentes de S3 vers Braze.

Cette page présente les étapes de synchronisation et de source qui sont actuellement en accès anticipé (EA). Pour les étapes de l'expérience en disponibilité générale, consultez [Expérience en disponibilité générale](#general-availability-experience).

## Fonctionnement

Vous pouvez utiliser Cloud Data Ingestion (CDI) for S3 pour intégrer directement un ou plusieurs compartiments S3 de votre compte AWS à Braze. Lorsque de nouveaux fichiers sont publiés sur S3, un message est envoyé à SQS et Cloud Data Ingestion de Braze prend en charge ces nouveaux fichiers. 

L'ingestion de données dans le cloud prend en charge les éléments suivants :

- Fichiers JSON
- Fichiers CSV
- Fichiers Parquet
- Données d'attributs, d'événements personnalisés, d'événements d'achat, de suppression d'utilisateurs et de catalogues

## Conditions préalables

L'intégration nécessite les ressources suivantes :

 - Compartiment S3 pour le stockage des données 
 - File d'attente SQS pour les notifications de nouveaux fichiers 
 - Rôle IAM pour l'accès à Braze  

### Définitions AWS

Commençons par définir les termes utilisés dans le cadre de cette tâche.

| Terme | Définition |
| --- | --- |
| Nom de ressource Amazon (ARN) | L'ARN est un identifiant unique pour les ressources AWS. |
| Gestion des identités et des accès (IAM) | IAM est un service Web qui vous permet de contrôler, en toute sécurité, l'accès aux ressources AWS. Dans ce tutoriel, vous allez créer une politique IAM et l'attribuer à un rôle IAM pour intégrer votre compartiment S3 à Cloud Data Ingestion de Braze. |
| Amazon Simple Queue Service (SQS) | SQS est une file d'attente hébergée qui vous permet d'intégrer des systèmes et des composants logiciels distribués. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuration de l'ingestion de données Cloud dans AWS

### Étape 1 : Créer un compartiment source

Créez un compartiment S3 à usage général avec les paramètres par défaut dans votre compte AWS. Les compartiments S3 peuvent être réutilisés d'une synchronisation à l'autre, à condition que le dossier soit unique.

Les paramètres par défaut sont les suivants :

- ACL désactivés
- Bloquer tout accès public
- Désactiver la gestion des versions des compartiments
- Chiffrement SSE-S3
  - SSE-S3 est le seul type de chiffrement côté serveur pris en charge. Le chiffrement Amazon KMS n'est pas pris en charge.

Notez bien la région dans laquelle vous avez créé le compartiment, car vous devrez créer une file d'attente SQS dans la même région à l'étape suivante.

### Étape 2 : Créer une file d'attente SQS

Créez une file d'attente SQS pour suivre l'ajout d'objets dans le compartiment que vous avez créé. Utilisez pour l'instant les paramètres de configuration par défaut. 

Une file d'attente SQS doit être unique au niveau mondial (par exemple, une seule peut être utilisée pour une synchronisation CDI et ne peut pas être réutilisée dans un autre espace de travail).

{% alert important %}
Veillez à créer cette file SQS dans la même région que celle dans laquelle vous avez créé le compartiment.
{% endalert %}

Pensez à noter l'ARN et l'URL de la file SQS, car vous les utiliserez fréquemment au cours de cette configuration.

![Sélectionnez « Avancé » avec un exemple d'objet JSON pour définir qui peut accéder à une file d'attente.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Étape 3 : Configurer une politique d'accès

Pour configurer la politique d'accès, sélectionnez **Options avancées**. 

Ajoutez la déclaration suivante à la politique d'accès de la file d'attente, en prenant soin de remplacer `YOUR-BUCKET-NAME-HERE` par le nom de votre compartiment, `YOUR-SQS-ARN` par l'ARN de votre file d'attente SQS, et `YOUR-AWS-ACCOUNT-ID` par l'ID de votre compte AWS : 

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

1. Dans le compartiment créé à l'étape 1, allez dans **Properties** > **Event notifications**.
2. Donnez un nom à la configuration. Vous pouvez également spécifier un préfixe ou un suffixe à cibler si vous souhaitez que seul un sous-ensemble de fichiers soit ingéré par Braze.
3. Sous **Destination**, sélectionnez **SQS queue** et indiquez l'ARN du SQS que vous avez créé à l'étape 2.

{% alert note %}
Si vous téléchargez vos fichiers dans le dossier racine d'un compartiment S3, puis que vous déplacez certains de ces fichiers vers un dossier spécifique du compartiment, vous risquez de rencontrer une erreur inattendue. Au lieu de cela, vous pouvez modifier les notifications d'événements pour qu'elles soient envoyées uniquement pour les fichiers du préfixe, éviter de placer des fichiers dans le compartiment S3 en dehors de ce préfixe, ou mettre à jour l'intégration sans préfixe, ce qui entraînera alors l'ingestion de tous les fichiers.
{% endalert %}

### Étape 5 : Créer une politique IAM

Créez une politique IAM pour permettre à Braze d'interagir avec votre compartiment source. Pour commencer, connectez-vous à la console de gestion AWS en tant qu'administrateur de compte. 

1. Allez dans la section IAM de la console AWS, sélectionnez **Policies** dans la barre de navigation, puis cliquez sur **Create Policy**.<br><br>![Le bouton « Create Policy » dans la console AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

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
3. Sélectionnez **Review Policy** lorsque vous avez terminé.

4. Donnez un nom et une description à la politique, puis sélectionnez **Create Policy**.  

![Une politique d'exemple nommée « new-policy-name ».]({% image_buster /assets/img/create_policy_3_name.png %})

![Le champ de description de la politique.]({% image_buster /assets/img/create_policy_4_created.png %})

### Étape 6 : Créer un rôle IAM

Pour terminer la configuration sur AWS, créez un rôle IAM et associez-y la politique IAM de l'étape 5. 

1. Dans la même section IAM de la console où vous avez créé la politique IAM, allez dans **Roles** > **Create Role**. 

![Le bouton « Create Role ».]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. Dans AWS, sélectionnez **Another AWS Account** comme type de sélecteur d'entité de confiance. Indiquez votre ID de compte Braze. Cochez la case **Require external ID**.
3. Dans Braze, accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources**, sélectionnez **Ajouter une source de données**, puis choisissez **Amazon S3** dans la section des sources de fichiers.
4. Copiez l'**ID de compte Braze** généré automatiquement. 

![La page « Ajouter une nouvelle source » affichant les sections Nom de la source et Détails de connexion S3.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. Dans AWS, collez l'ID du compte, puis sélectionnez **Next**.

![Page S3 « Create Role ». Cette page comporte des champs pour le nom du rôle, la description du rôle, les entités de confiance, les politiques et les restrictions d'autorisations.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Attachez la politique créée à l'étape 4 au rôle. Recherchez la politique dans la barre de recherche et cochez la case à côté de la politique pour la joindre. Sélectionnez **Next** lorsque vous avez terminé.

![Rôle ARN avec le nom de la nouvelle politique sélectionné.]({% image_buster /assets/img/create_role_3_attach.png %})

Donnez un nom et une description au rôle, puis sélectionnez **Create Role**.

![Un exemple de rôle nommé « new-role-name ».]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Notez l'ARN du rôle que vous avez créé et l'ID externe que vous avez généré, car vous en aurez besoin pour créer l'intégration Cloud Data Ingestion.

## Configuration de Cloud Data Ingestion dans Braze

1. Commencez par créer une nouvelle source dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Sources**, sélectionnez **Ajouter une source de données**, puis choisissez **Amazon S3**.
2. Choisissez un nom pour votre source et saisissez les informations issues du processus de configuration AWS pour créer une nouvelle source. Précisez les éléments suivants :

  - ARN du rôle
  - ID externe
  - Nom du compartiment
  - Région

![La section Détails de connexion S3 affichant les identifiants (configuration AWS et configuration Braze) et les champs de configuration.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Sélectionnez **Tester la connexion** pour confirmer que Braze peut accéder à votre compartiment. Après un test réussi, sélectionnez **Se connecter à la source**. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{: start="4"}
4. Ensuite, créez une nouvelle synchronisation. Accédez à **Paramètres des données** > **Ingestion de données dans le cloud** > **Synchronisations** et sélectionnez **Créer une synchronisation de données**.

![La page « Créer une nouvelle synchronisation » affichant le nom de la synchronisation et la configuration de la source de données.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})

{: start="5"}
5. Choisissez un nom pour votre synchronisation. Sélectionnez ensuite une source S3 active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Tester la connexion**.

![Une option permettant de tester la connexion avec un aperçu des données.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Saisissez les informations restantes issues du processus de configuration AWS. Précisez les éléments suivants :
- URL SQS (doit être unique pour chaque nouvelle intégration)
- Chemin d'accès au dossier (facultatif, doit être unique pour toutes les synchronisations d'un espace de travail)

7. Sélectionnez un type de données et cliquez sur **Tester la connexion** pour confirmer que Braze peut lister les fichiers disponibles à l'ingestion (et non les données contenues dans ces fichiers). Une fois le test réussi, sélectionnez **Suivant : Notifications**.
8. Ajoutez une ou plusieurs adresses e-mail de contact pour recevoir des notifications si la synchronisation est interrompue en raison de problèmes d'accès ou d'autorisations. Si vous le souhaitez, activez les notifications pour les erreurs au niveau de l'utilisateur et les synchronisations réussies.
9. Créez la synchronisation.

{% details Expérience en disponibilité générale %}

1. Pour créer une nouvelle intégration, accédez à **Paramètres des données** > **Ingestion de données dans le cloud**, sélectionnez **Créer une nouvelle synchronisation de données**, puis sélectionnez **Importation S3** dans la section des sources de fichiers. 
2. Saisissez les informations issues du processus de configuration AWS pour créer une nouvelle synchronisation. Précisez les éléments suivants :

  - ARN du rôle
  - ID externe
  - URL SQS (doit être unique pour chaque nouvelle intégration)
  - Nom du compartiment
  - Chemin d'accès au dossier (facultatif, doit être unique pour toutes les synchronisations d'un espace de travail)
  - Région

{: start="3"}
3. Donnez un nom à votre intégration et sélectionnez le type de données pour cette intégration. 

{: start="4"}
4. Ajoutez une adresse e-mail de contact pour recevoir des notifications si la synchronisation est interrompue en raison de problèmes d'accès ou d'autorisations. Si vous le souhaitez, activez les notifications pour les erreurs au niveau de l'utilisateur et les synchronisations réussies. 

{: start="5"}
5. Enfin, sélectionnez **Tester la connexion** pour confirmer que Braze peut accéder à votre compartiment et lister les fichiers disponibles à l'ingestion (et non les données contenues dans ces fichiers). Ensuite, enregistrez la synchronisation. 

{% enddetails %}

## Formats de fichiers requis

Cloud Data Ingestion prend en charge les fichiers JSON, CSV et Parquet. Les colonnes requises dépendent du type de données :

- Les données utilisateur (attributs, événements personnalisés, événements d'achat) utilisent des identifiants utilisateur et un payload
- Les données de catalogue utilisent des identifiants de catalogue

Braze n'impose pas d'exigences supplémentaires en matière de noms de fichiers au-delà de celles imposées par AWS. Les noms de fichiers doivent être uniques. Nous vous recommandons d'ajouter un horodatage pour garantir l'unicité.

Pour obtenir des exemples de tous les types de fichiers pris en charge (attributs, événements personnalisés, achats, catalogues et suppressions d'utilisateurs), consultez les fichiers d'exemple dans [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Identifiants des utilisateurs {#user-identifiers}

Pour les synchronisations de données utilisateur (attributs, événements personnalisés, événements d'achat), chaque ligne de votre fichier source doit contenir exactement un identifiant utilisateur et une colonne `PAYLOAD`. Un fichier source peut contenir des lignes avec différents types d'identifiants, mais chaque ligne individuelle ne doit en utiliser qu'un seul.

| Identifiant | Description |
| --- | --- |
| `EXTERNAL_ID` | Identifie l'utilisateur que vous souhaitez mettre à jour. Doit correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`. |
| `BRAZE_ID` | L'identifiant utilisateur Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via Cloud Data Ingestion. Pour créer de nouveaux utilisateurs, spécifiez un ID externe ou un alias d'utilisateur. |
| `EMAIL` | L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil mis à jour le plus récemment sera prioritaire. Si vous indiquez à la fois l'e-mail et le téléphone, l'e-mail sera utilisé comme identifiant principal. |
| `PHONE` | Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil mis à jour le plus récemment sera prioritaire. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

En plus d'un identifiant, chaque ligne doit contenir une colonne `PAYLOAD` avec une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

{% alert note %}
Contrairement aux sources d'entrepôt de données, la colonne `UPDATED_AT` n'est ni requise ni prise en charge pour les synchronisations de stockage de fichiers.
{% endalert %}

### Identifiants de catalogue {#catalog-identifiers}

Pour les synchronisations de catalogue, votre fichier source doit contenir les colonnes suivantes. Les fichiers de catalogue utilisent des identifiants différents de ceux des fichiers de données utilisateur.

| Colonne | Requis | Description |
| --- | --- | --- |
| `ID` | Oui | L'identifiant unique de l'élément de catalogue. Utilisé pour créer, mettre à jour ou supprimer l'élément dans Braze. |
| `PAYLOAD` | Oui | Une chaîne JSON des champs et valeurs du catalogue à synchroniser. Doit correspondre au schéma de votre catalogue dans Braze. |
| `DELETED` | Non | Lorsque la valeur est `true`, l'élément de catalogue correspondant à l'`ID` est supprimé du catalogue dans Braze. Omettez cette colonne ou définissez-la sur `false` pour les opérations de création ou de mise à jour. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Exemples

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
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
Incluez une colonne `DELETED` facultative. Lorsque `DELETED` est `true`, cet élément de catalogue est supprimé du catalogue dans Braze. Pour la liste complète des colonnes requises, consultez [Identifiants de catalogue](#catalog-identifiers). Pour le comportement de suppression, consultez [Suppression d'éléments de catalogue](#deleting-catalog-items).
{% endtab %}

{% endtabs %}  

## Suppression des données

Cloud Data Ingestion pour S3 prend en charge la suppression d'utilisateurs et d'éléments de catalogue via le téléchargement de fichiers. Utilisez des synchronisations et des formats de fichiers distincts pour chaque type.

- **[Suppression d'utilisateurs](#deleting-users)** – Créez une synchronisation avec le type de données **Supprimer les utilisateurs** et téléchargez des fichiers contenant uniquement les identifiants des utilisateurs (sans payload).
- **[Suppression d'éléments de catalogue](#deleting-catalog-items)** – Utilisez votre synchronisation de catalogue existante et ajoutez une colonne `deleted` (ou `DELETED`) pour marquer les éléments à supprimer.

### Suppression d'utilisateurs

Pour supprimer des profils utilisateurs dans Braze à l'aide de fichiers dans S3 :

1. Créez une nouvelle synchronisation Cloud Data Ingestion (même [configuration AWS et Braze](#setting-up-cloud-data-ingestion-in-aws) que pour les autres synchronisations).
2. Lors de la configuration de la synchronisation dans Braze, définissez le **Type de données** sur **Supprimer les utilisateurs**.
3. Téléchargez vers votre compartiment S3 des fichiers contenant uniquement des colonnes d'identifiant utilisateur. N'incluez pas de colonne `PAYLOAD` — la synchronisation échouera si un payload est présent, afin d'éviter toute suppression accidentelle.

Chaque ligne du fichier doit identifier exactement un utilisateur à l'aide de l'un des éléments suivants :

| Identifiant | Description |
| --- | --- |
| `EXTERNAL_ID` | Correspond à l'`external_id` utilisé dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Les deux colonnes ensemble identifient l'utilisateur par son alias. |
| `BRAZE_ID` | ID utilisateur généré par Braze (utilisateurs existants uniquement). |

{% alert important %}
La suppression d'utilisateurs est définitive et irréversible. N'incluez que les utilisateurs que vous avez l'intention de supprimer. Pour plus d'informations, consultez [Supprimer des utilisateurs avec Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users/).
{% endalert %}

**Exemple – JSON (suppression d'utilisateurs) :**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**Exemple – CSV (suppression d'utilisateurs) :**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

Lorsque la synchronisation s'exécute, Braze traite les nouveaux fichiers dans le compartiment et supprime les profils utilisateurs correspondants.

### Suppression d'éléments de catalogue

Pour supprimer des éléments d'un catalogue à l'aide du stockage de fichiers :

1. Utilisez la même synchronisation S3 que celle utilisée pour [synchroniser les données du catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) (type de données **Catalogues**).
2. Dans vos fichiers CSV ou JSON, ajoutez une colonne facultative **`deleted`** (ou **`DELETED`**).
3. Définissez `deleted` sur `true` pour tout élément de catalogue que vous souhaitez supprimer du catalogue dans Braze.

Chaque ligne nécessite toujours `ID` et `PAYLOAD`. Pour les lignes marquées pour suppression, le payload peut être minimal ; Braze supprime l'élément par `ID`.

**Exemple – JSON (suppression d'un élément de catalogue) :**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Exemple – CSV (suppression d'un élément de catalogue) :**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Lorsque la synchronisation s'exécute, les lignes contenant `deleted: true` entraînent la suppression de l'élément de catalogue correspondant dans Braze. Pour en savoir plus sur le comportement de synchronisation et de suppression des catalogues, consultez [Synchronisation et suppression des données du catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/).

## Bon à savoir

- Les fichiers ajoutés au compartiment S3 source ne doivent pas dépasser 512&nbsp;Mo. Les fichiers de plus de 512&nbsp;Mo entraîneront une erreur et ne seront pas synchronisés vers Braze.
- Bien qu'il n'y ait pas de limite supplémentaire au nombre de lignes par fichier, nous vous recommandons d'utiliser des fichiers plus petits pour accélérer vos synchronisations. Par exemple, l'ingestion d'un fichier de 500&nbsp;Mo prendrait beaucoup plus de temps que celle de cinq fichiers distincts de 100&nbsp;Mo.
- Il n'y a pas de limite supplémentaire au nombre de fichiers téléchargés dans un temps donné.
- L'ordonnancement n'est pas pris en charge au sein des fichiers ni entre les fichiers. Nous vous recommandons de regrouper les mises à jour périodiquement si vous surveillez d'éventuelles conditions de concurrence.

## Résolution des problèmes

### Téléchargement et traitement des fichiers

CDI ne traite que les fichiers ajoutés après la création de la synchronisation. Au cours de ce processus, Braze recherche les nouveaux fichiers ajoutés, ce qui déclenche un nouveau message vers SQS. Cela lance une nouvelle synchronisation pour traiter le nouveau fichier.

Vous pouvez utiliser les fichiers existants pour vérifier que Braze peut accéder à votre compartiment et détecter les fichiers à ingérer, mais ils ne sont pas synchronisés vers Braze. Pour que CDI puisse les traiter, vous devez télécharger à nouveau sur S3 tous les fichiers existants que vous souhaitez synchroniser. 

### Gestion des erreurs de fichiers inattendues

Si vous observez un nombre élevé d'erreurs ou de fichiers en échec, il se peut qu'un autre processus ajoute des fichiers au compartiment S3 dans un dossier autre que le dossier cible pour CDI.

Lorsque des fichiers sont téléchargés dans le compartiment source mais pas dans le dossier source, CDI traite la notification SQS mais n'entreprend aucune action sur le fichier, ce qui peut apparaître comme une erreur.