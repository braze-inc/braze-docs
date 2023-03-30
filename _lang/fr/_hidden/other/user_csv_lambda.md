---
nav_title: Processus Lambda avec CSV attribut utilisateur
permalink: /user_csv_lambda/
description: "L'article suivant fait référence à une application sans serveur qui vous permet de déployer facilement un processus Lambda qui enverra les données d'attributs d'utilisateur d'un fichier CSV directement à Braze via l’endpoint du suivi des utilisateurs de Braze."
hidden: true
---

# Importation Braze avec CSV attribut utilisateur

> La fonction Lambda ci-dessous est une application sans serveur qui vous permet de publier facilement des données d’attributs utilisateur d’un fichier CSV Amperity dans Braze via [le suivi des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze. Cette intégration de l’application a été testée avec notre partenaire Amperity et est disponible sur [GitHub](https://github.com/braze-inc/growth-shares-lambda-user-csv-import).

Ce processus démarre immédiatement lors du téléchargement d’un fichier CSV dans un compartiment AWS S3 configuré. Elle peut gérer des fichiers et des téléchargements volumineux, mais en raison des limites de temps Lambda, la fonction s’arrêtera après 10 minutes. Ce processus lancera ensuite une autre instance Lambda pour traiter la partie restante du fichier. Pour plus d’informations sur le minutage, consultez les [durées d’exécution estimées](#estimated-execution-times).

{% alert important %}
Cette application est développée et gérée par le service Braze Growth. Si vous souhaitez contacter les créateurs de cette application, créez un [problème GitHub](https://github.com/braze-inc/growth-shares-lambda-user-csv-import/issues) et signalez tout commentaire ou problème existant. 
{% endalert %}

#### Attributs utilisateur CSV

Les attributs utilisateur à mettre à jour doivent être au format `.csv` suivant :

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

La première colonne doit indiquer l’ID externe de l’utilisateur à mettre à jour, et les colonnes suivantes doivent indiquer les noms et valeurs des attributs. Le nombre d’attributs que vous indiquerez peut varier. Si le fichier CSV à traiter ne respecte pas ce format, la fonction échouera.  

Exemple de fichier CSV :

```
external_id,Loyalty Points,Last Brand Purchased
abc123,1982,Solomon
def456,578,Hunter-Hayes
```

#### Traitement CSV

Toutes les valeurs d’une matrice (par ex. `"['Value1', 'Value2']"`) seront automatiquement déstructurées et envoyées à l’API dans un tableau plutôt que dans une représentation de chaîne de caractères d’un tableau.

## Conditions

Pour exécuter avec succès cette fonction Lambda, vous aurez besoin de :
- **Compte AWS** pour utiliser les services S3 et Lambda.
- **URL d’API Braze** pour se connecter aux serveurs Braze
- **Clé d’API Braze** pour envoyer des demandes au endpoint `/users/track`.
- **Fichier CSV** avec les attributs et ID externes de l’utilisateur à mettre à jour

{% tabs %}
{% tab API URL %}

Vous pouvez trouver votre URL d’API, ou l’endpoint REST, dans la documentation de l’API de Braze et via le tableau de bord.

- **Documentation API**<br>Comme le précise la [Documentation API]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances), il vous suffit de faire correspondre votre URL de l’instance Braze à l’URL d’endpoint REST. Par exemple, si votre URL de tableau de bord est `dashboard-01.braze.com/`, votre endpoint REST sera `https://rest.iad-01.braze.com`. <br><br>
- **Tableau de bord**<br>Dans le panneau de navigation gauche, faites défiler vers le bas et sélectionnez **Manage Settings (Gérer les paramètres)**. Là, vous pouvez voir votre `SDK Endpoint`. Remplacer `sdk` par `rest` pour obtenir votre endpoint REST. Par exemple, si vous voyez `sdk.iad-01.braze.com`, votre URL API sera `rest.iad-01.braze.com`

{% endtab %}
{% tab API Key %}

Pour vous connecter aux serveurs Braze, vous aurez besoin d’une clé API. Cet identifiant unique permet à Braze de vérifier votre identité et de télécharger vos données. 

Pour obtenir votre clé API, ouvrez le tableau de bord et faites défiler le volet de navigation vers le bas. Sélectionnez **Developer Console (Console du développeur)** dans _Settings (Paramètres)_. Vous aurez besoin d’une clé d’API avec l’autorisation de publier sur l’endpoint d’API `users.track`. Si vous savez que l’une de vos clés API prend en charge cet endpoint, vous pouvez utiliser cette clé. 

Pour en créer une nouvelle, cliquez sur `Create New API Key`. Ensuite, nommez votre clé API et sélectionnez `users.track` dans le groupe d’endpoints _User Data (Données utilisateur)_. Faites défiler vers le bas et cliquez sur **Enregistrer la clé API**.

{% endtab %}
{% endtabs %}

## Instructions d’utilisation

##### Aperçu
1. Déployer la fonction Lambda de traitement CSV disponible publiquement de Braze depuis le référentiel d’applications sans serveur AWS
2. Déposez un fichier CSV avec des attributs utilisateur dans le nouveau compartiment S3
3. Les utilisateurs seront automatiquement importés dans Braze.

#### Déployer

Pour commencer à traiter les fichiers CSV de vos attributs utilisateur, nous devons déployer l’application sans serveur afin qu’elle gère le traitement pour vous. Cette application créera automatiquement les ressources ci-dessous pour assurer un déploiement réussi :

- Fonction Lambda
- Compartiment S3 pour vos fichiers CSV que le processus Lambda peut lire (_Remarque : cette fonction Lambda ne recevra que des notifications pour les `.csv`fichiers d’extension_)
- Rôle permettant de créer un compartiment S3
- Politique permettant à Lambda de recevoir un événement de chargement S3 dans le nouveau compartiment

Suivez le lien direct vers l’[application](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import) ou ouvrez le [Référentiel d’applications sans serveur AWS](https://serverlessrepo.aws.amazon.com/applications) et recherchez « braze-user-attribute-import ». Notez que vous devez cocher la case `Show apps that create custom IAM roles and resource policies` pour voir cette application. L’application crée une politique pour que Lambda puisse lire le nouveau compartiment S3.

Cliquez sur **Deploy (Déployer)** et laissez AWS créer toutes les ressources nécessaires.

Vous pouvez suivre le déploiement et vérifier que la pile (c.-à-d. toutes les ressources requises) est créée dans [CloudFormation](https://console.aws.amazon.com/cloudformation/). Trouvez la pile appelée « serverlessrepo-braze-user-attribute-import ». La fonction est prête à être utilisée dès que le **Status (Statut)** passe sur `CREATE_COMPLETE`. Vous pouvez cliquer sur la pile, ouvrir **Resources (Ressources)** et suivre les différentes ressources qui sont en train d’être créées.

Les ressources suivantes ont été créées :

- [Compartiment S3](https://s3.console.aws.amazon.com/s3/) : un compartiment nommé `braze-user-csv-import-aaa123` où `aaa123` est une chaîne générée aléatoirement.
- [Fonction Lambda](https://console.aws.amazon.com/lambda/) : une fonction Lambda nommée `braze-user-attribute-import`.
- [Rôle IAM](https://console.aws.amazon.com/iam/) - une politique nommée `braze-user-csv-import-BrazeUserCSVImportRole` pour permettre à Lambda de lire les fichiers S3 et de consigner les résultats de la fonction.

#### Exécuter

Pour exécuter cette fonction, déposez un fichier CSV d’attributs utilisateur dans le nouveau compartiment S3.

## Surveillance et enregistrement

Pour vous assurer que la fonction fonctionne correctement, vous pouvez lire les journaux d’exécution de la fonction. Ouvrez la fonction Importation CSV des utilisateurs Braze (en la sélectionnant dans la liste de Lambdas dans la console) et naviguez jusqu’à **Surveiller**. Ici, vous pouvez voir l’historique d’exécution de la fonction. Pour lire la sortie, cliquez sur **Afficher les journaux dans CloudWatch**. Sélectionnez l’événement d’exécution lambda que vous souhaitez vérifier.

## Temps d’exécution estimés
_Fonction Lambda 2048MB_

| Nombre de lignes | Durée d’exécution |
| --------- | ---------- |
| 10 000       | 3 s         |
| 100 000      | 30 s        |
| 1 000 000        | 5 min      |
| 5 000 000        | 30 min     |

## Mise à jour d’une fonction existante

Si vous avez déjà déployé l’application et qu’une nouvelle version est disponible dans le référentiel, vous pouvez effectuer la mise à jour en redéployant la fonction comme si vous le faisiez pour la première fois. Cela signifie que vous devez transmettre à nouveau la clé d’API Braze et l’URL d’API Braze. La mise à jour n’écrasera que le code de fonction. Aucune modification ou suppression de ressources existantes n’aura lieu (à l’inverse du compartiment S3).

## Erreur fatale

En cas d’erreur empêchant le traitement ultérieur du fichier, un événement est enregistré (accessible par CloudWatch, voir [Surveillance et enregistrement](#monitoring-and-logging)) et peut être utilisé pour redémarrer Lambda à partir de l’interruption de traitement du fichier par le programme. Il est important de ne pas réimporter les mêmes données pour enregistrer des points de données. Vous pouvez trouver des instructions pour réaliser cette opération dans notre [Référentiel GitHub](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error).

{% alert important %}
Visitez notre référentiel GitHub pour en savoir plus sur la manière de gérer [erreurs fatales](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error) ou la [configuration de Lambda](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#lambda-configuration).
{% endalert%}