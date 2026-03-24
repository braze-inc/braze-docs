---
nav_title: Transférer les données vers Redshift
article_title: Transférer des données vers Redshift
page_order: 8
page_type: tutorial
description: "Cet article pratique vous explique comment transférer des données d'Amazon S3 vers Redshift par le biais d'un processus d'extraction, de transformation et de chargement (ETL)."
tool: Currents

---

# Transférer les données vers Redshift

> [Amazon Redshift](https://aws.amazon.com/redshift/) est un entrepôt de données populaire qui fonctionne sur Amazon Web Services aux côtés d'Amazon S3. Les données Braze provenant de Currents sont structurées de manière à pouvoir être transférées directement vers Redshift.

La procédure suivante décrit comment transférer des données depuis Amazon S3 vers Redshift via un processus ETL (extraire, transformer, charger). Pour obtenir le code source complet, veuillez consulter le [référentiel GitHub](https://github.com/Appboy/currents-examples) des exemples Currents.

{% alert important %}
Notez que ce n’est qu’une des nombreuses options que vous pouvez choisir lorsqu’il s’agit de transférer vos données vers les emplacements les plus avantageux pour vous.
{% endalert %}

## Aperçu du chargeur S3 vers Redshift

Le[`s3loader.py`](https://github.com/Appboy/currents-examples/tree/master/redshift-s3-loader)script utilise une table manifeste distincte dans la même base de données Redshift pour garder une trace des fichiers qui ont déjà été copiés. La structure générale est la suivante :

1. Veuillez répertorier tous les fichiers dans S3, puis identifier les nouveaux fichiers depuis la dernière exécution`s3loader.py`en comparant la liste avec le contenu du tableau manifeste.
2. Veuillez créer un fichier [manifeste](http://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html) contenant les nouveaux fichiers.
3. Exécutez une`COPY`requête pour copier les nouveaux fichiers de S3 vers Redshift à l'aide du fichier manifeste.
4. Veuillez insérer les noms des fichiers qui sont copiés dans le tableau de manifeste distinct dans Redshift.
5. Engagez-vous.

## Dépendances

Il est nécessaire d'installer le SDK Python AWS et Psycopg pour exécuter le chargeur :

```bash
pip install boto3
pip install psycopg2
```

## Autorisations

### Rôle Redshift avec accès en lecture S3

Si vous ne l'avez pas encore fait, veuillez suivre la [documentation AWS](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html) pour créer un rôle capable d'exécuter`COPY`des commandes sur vos fichiers dans AWS S3.

### Règles entrantes de Redshift VPC

Si votre cluster Redshift se trouve dans un VPC, il est nécessaire de configurer le VPC afin d'autoriser les connexions provenant du serveur sur lequel vous exécutez S3 Loader. Veuillez accéder à votre cluster Redshift et sélectionner l'entrée Groupes de sécurité VPC à laquelle vous souhaitez que le chargeur se connecte. Ensuite, veuillez ajouter une nouvelle règle entrante : **Type** = Redshift, **Protocole** = TCP, **Port** = le port de votre cluster, **Source** = l'adresse IP du serveur exécutant le chargeur (ou « Anywhere » pour les tests).

### Utilisateur de gestion des identités et des accès (IAM) avec accès complet à S3

Le chargeur S3 nécessite un accès en lecture aux fichiers contenant vos données Currents, ainsi qu'un accès complet à l'emplacement/localisation des fichiers manifestes qu'il génère pour les commandes `COPY`Redshift. Veuillez créer un nouvel utilisateur IAM (Identity and Access Management) avec `AmazonS3FullAccess`l'autorisation de la [console IAM](https://console.aws.amazon.com/iam/home#/users). Veuillez enregistrer les informations d'identification, car vous devrez les transmettre au chargeur.

Vous pouvez transmettre les informations d'identification d'accès au chargeur via des variables d'environnement, le fichier d'informations d'identification partagé (`~/.aws/credentials`) ou le [fichier de configuration AWS](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials). Vous pouvez également les inclure directement dans le chargeur en les attribuant aux`aws_secret_access_key`champs`aws_access_key_id`et  d'un`S3LoadJob`objet , mais nous déconseillons de coder en dur les informations d'identification dans votre code source.

## Utilisation

### Exemple d'utilisation

Le programme suivant charge les données relatives à`users.messages.contentcard.Impression`l'événement depuis S3 vers la`content_card_impression`table dans Redshift.

```
if __name__ == '__main__':
    host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
    port = 5439
    database = '{YOUR_DATABASE}'
    user = '{YOUR_USER}'
    password = '{YOUR_PASSWORD}'
    role = '{YOUR_REDSHIFT_ROLE_ARN}'

    # Do not hard code these credentials.
    aws_access_key_id = None
    aws_secret_access_key = None

    # Content Card Impression Avro fields:
    #   id            - string
    #   user_id       - string
    #   external_user_id - string (nullable)
    #   app_id        - string
    #   content_card_id  - string
    #   campaign_id   - string (nullable)
    #   send_id       - string (nullable)
    #   time          - int
    #   platform      - string (nullable)
    #   device_model  - string (nullable)

    print('Loading Content Card Impression...')
    cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
    cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
    cc_impression_redshift_table = 'content_card_impression'
    cc_impression_redshift_column_def = [
        ('id', 'text'),
        ('user_id', 'text'),
        ('external_user_id', 'text'),
        ('app_id', 'text'),
        ('content_card_id', 'text'),
        ('campaign_id', 'text'),
        ('send_id', 'text'),
        ('time', 'integer'),
        ('platform', 'text'),
        ('device_model', 'text')
    ]

    cc_impression_redshift = RedshiftEndpoint(host, port, database, user, password,
        cc_impression_redshift_table, cc_impression_redshift_column_def)
    cc_impression_s3 = S3Endpoint(cc_impression_s3_bucket, cc_impression_s3_prefix)

    cc_impression_job = S3LoadJob(cc_impression_redshift, cc_impression_s3, role,
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    cc_impression_job.perform()
```

### Identifiants

Pour exécuter le chargeur, il est nécessaire de fournir les identifiants `host`,`port` , et`database`  de votre cluster Redshift, ainsi que les identifiants`user`  et`password`  d'un utilisateur Redshift autorisé à exécuter`COPY`des requêtes . De plus, vous devez fournir l'ARN du rôle Redshift avec accès en lecture S3 que vous avez créé dans une section précédente.

```
host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
port = 5439
database = '{YOUR_DATABASE}'
user = '{YOUR_USER}'
password = '{YOUR_PASSWORD}'
role = '{YOUR_REDSHIFT_ROLE_ARN}'
```

### Configuration de la tâche

Veuillez fournir le compartiment S3 et le préfixe de vos fichiers d'événements, ainsi que le nom de la table Redshift dans laquelle vous souhaitez`COPY`les intégrer.

En outre, pour les fichiers`COPY` Avro avec l'option « auto » requise par le chargeur, la définition des colonnes dans votre table Redshift doit correspondre aux noms de champs dans le schéma Avro, comme indiqué dans l'exemple de programme, avec le mappage de types approprié (par exemple,`string`  à `text`,`int`  à `integer`).

Vous pouvez également transmettre une`batch_size`option au chargeur si vous constatez que la copie de tous les fichiers en une seule fois prend trop de temps. Le passage d'un paramètre`batch_size`permet au chargeur de copier et de valider progressivement un lot à la fois sans devoir tout copier simultanément. Le temps nécessaire au chargement d'un lot dépend de la configuration de votre cluster`batch_size` Redshift, ainsi que de la taille de vos fichiers.

```
# Content Card Impression Avro fields:
#   id            - string
#   user_id       - string
#   external_user_id - string (nullable)
#   app_id        - string
#   content_card_id  - string
#   campaign_id   - string (nullable)
#   send_id       - string (nullable)
#   time          - int
#   platform      - string (nullable)
#   device_model  - string (nullable)
cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
cc_impression_redshift_table = 'content_card_impression'
cc_impression_redshift_column_def = [
    ('id', 'text'),
    ('user_id', 'text'),
    ('external_user_id', 'text'),
    ('app_id', 'text'),
    ('content_card_id', 'text'),
    ('campaign_id', 'text'),
    ('send_id', 'text'),
    ('time', 'integer'),
    ('platform', 'text'),
    ('device_model', 'text')
]
cc_impression_batch_size = 1000
```