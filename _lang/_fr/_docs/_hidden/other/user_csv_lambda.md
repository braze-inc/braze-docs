---
nav_title: Processus Lambda d'attribut utilisateur CSV
permalink: /fr/user_csv_lambda/
description: "L'article suivant fait référence à une application sans serveur qui vous permet de déployer facilement un processus Lambda qui affichera directement des données d'attributs d'utilisateur d'un fichier CSV à Braze à travers le point de terminaison de la piste utilisateur de Braze."
hidden: vrai
---

{% alert important %}
Cette application est construite et maintenue par le département de la croissance de Braze. Si vous souhaitez contacter les créateurs de cette application, veuillez créer un problème [github](https://github.com/braze-inc/growth-shares-lambda-user-csv-import/issues) pour tout commentaire ou problème qui pourrait survenir.
{% endalert %}

# Attribut utilisateur CSV à l'importation de Braze

> L'article suivant fait référence à une application sans serveur qui vous permet de déployer facilement un processus Lambda qui affichera directement des données d'attributs utilisateur à partir d'un fichier CSV à Braze via le point de terminaison de l'API [User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Cette intégration d'application a été testée avec notre partenaire d'Amperity et peut être trouvée sur notre Github [ici](https://github.com/braze-inc/growth-shares-lambda-user-csv-import).

Ce processus se lance immédiatement lorsque vous téléchargez un fichier CSV vers un compartiment AWS S3 configuré. Il peut gérer les gros fichiers et les envois, mais en raison des limites de temps de Lambda, la fonction arrêtera l'exécution après 10 minutes. Ce processus lancera ensuite une autre instance Lambda pour terminer le traitement de la partie restante du fichier. Pour plus de détails sur le chronométrage de la fonction, consultez les [durées d'exécution estimées](#estimated-execution-times).

#### Attributs d'utilisateur CSV

Les attributs utilisateur à mettre à jour sont attendus au format `.csv` suivant :

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

La première colonne doit spécifier l'ID externe de l'utilisateur à mettre à jour et les colonnes suivantes doivent spécifier les noms et valeurs de l'attribut. Le nombre d'attributs que vous spécifiez peut varier. Si le fichier CSV à traiter ne suit pas ce format, la fonction échouera.

Exemple de fichier CSV :

```
external_id,Points de fidélité,Dernière marque achetée
abc123,1982, Salomon
def456,578,Hunter-Hayes
```

#### Traitement CSV

N'importe quelle valeur dans un tableau (ex. `"['Valeur1', 'Value2']"`) sera automatiquement détruit et envoyé à l'API dans un tableau plutôt qu'une représentation de chaîne de caractères d'un tableau.

## Exigences

Pour exécuter avec succès cette fonction Lambda, vous aurez besoin de :
- **Compte AWS** pour utiliser les services S3 et Lambda
- **URL API Braze** pour se connecter aux serveurs Braze
- **Braze API Key** pour pouvoir envoyer des requêtes à `/users/track` endpoint
- **Fichier CSV** avec les identifiants externes de l'utilisateur et les attributs à mettre à jour

{% tabs %}
{% tab API URL %}

Vous pouvez trouver votre URL API, ou REST endpoint, dans la documentation de l'API Braze et via le tableau de bord.

- __Documentation API__<br>Par [documentation API]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances), il suffit de faire correspondre l'URL de votre instance Braze à l'URL de terminaison REST. Par exemple, si votre tableau de bord affiche `le tableau de bord -01.braze.com/` URL, votre point de terminaison REST serait `https://rest.iad-01.braze.com`. <br><br>
- __Dashboard__<br>À partir du panneau de navigation gauche, faites défiler vers le bas et sélectionnez **Gérer les paramètres**. Là, vous pouvez trouver votre `point de terminaison SDK`. Remplacez `sdk` par `repos` pour obtenir votre point de terminaison REST. Par exemple, si vous voyez `sdk.iad-01.braze.com`, votre URL API serait `rest.iad-01.braze.com`

{% endtab %}
{% tab API Key %}

Pour vous connecter avec les serveurs Braze, vous aurez besoin d'une clé API. Cet identifiant unique permet à Braze de vérifier votre identité et de télécharger vos données.

Pour obtenir votre clé API, ouvrez le tableau de bord et descendez dans la section de navigation de gauche. Sélectionnez **Console développeur** sous _Paramètres_. Vous aurez besoin d'une clé API qui a la permission de publier sur `users.track` point de terminaison de l'API. Si vous savez qu'une de vos clés API prend en charge ce point de terminaison, vous pouvez utiliser cette clé.

Pour en créer une nouvelle, cliquez sur `Créer une nouvelle clé API` sur le côté droit de votre écran. Ensuite, nommez votre clé API et sélectionnez `users.track` sous le groupe de terminaisons _Données Utilisateurs_. Faites défiler vers le bas et cliquez sur **Enregistrer la clé API**.

{% endtab %}
{% endtabs %}

## Instructions d'utilisation

##### Aperçu
1. Déployer le traitement CSV public de Braze Lambda depuis le dépôt d'applications sans serveur AWS
2. Déposer un fichier CSV avec les attributs de l'utilisateur dans le segment S3 nouvellement créé
3. Les utilisateurs seront automatiquement importés dans Braze

#### Déployer

Pour commencer à traiter vos fichiers CSV d'Attribut Utilisateur, nous devons déployer l'application sans serveur qui gérera le traitement pour vous. Cette application créera automatiquement les ressources suivantes pour déployer avec succès :

- Fonction Lambda
- S3 Seau pour vos fichiers CSV que le processus Lambda peut lire (_Note : cette fonction Lambda ne recevra que des notifications pour `. sv` fichiers d'extension_)
- Rôle permettant la création de ce qui précède
- Politique permettant à Lambda de recevoir un événement de téléchargement S3 dans le nouveau seau

Suivez le lien direct vers l'application [](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import) ou ouvrez le [dépôt d'application sans serveur AWS](https://serverlessrepo.aws.amazon.com/applications) et recherchez _l'attribut-utilisateur braze-import_. Notez que vous devez cocher la case `Afficher les applications qui créent des rôles personnalisés IAM et des politiques de ressources` pour voir cette application. L'application crée une politique pour que lambda puisse lire à partir du segment S3 nouvellement créé.

Cliquez sur **Déployer** et laissez AWS créer toutes les ressources nécessaires.

Vous pouvez surveiller le déploiement et vérifier que la pile (c.-à-d. toutes les ressources requises) est en cours de création dans la [CloudFormation](https://console.aws.amazon.com/cloudformation/). Trouvez la pile nommée _serverlessrepo-braze-user-attribute-import_. Une fois que le **Statut** tourne à `CREATE_COMPLETE`, la fonction est prête à être utilisée. Vous pouvez cliquer sur la pile et ouvrir **Ressources** et regarder les différentes ressources en cours de création.

Les ressources suivantes ont été créées :

- [S3 Bucket](https://s3.console.aws.amazon.com/s3/) - un seau nommé `braze-user-csv-import-aaa123` où `aaa123` est une chaîne générée aléatoirement
- [Lambda Function](https://console.aws.amazon.com/lambda/) - une fonction lambda nommée `braze-user-attribute-import`
- [Rôle IAM](https://console.aws.amazon.com/iam/) - politique nommée `braze-user-csv-import-BrazeUserCSVImportRole` pour permettre lambda de lire à partir de S3 et enregistrer la sortie de la fonction

#### Exécuter

Pour exécuter la fonction, déposez un fichier CSV d'attribut utilisateur dans le compartiment S3 nouvellement créé.

## Surveillance et journalisation

Pour vous assurer que la fonction s'exécute correctement, vous pouvez lire les journaux d'exécution de la fonction. Ouvrez la fonction Import CSV de Braze (en la sélectionnant dans la liste de Lambdas dans la console) et accédez à **Moniteur**. Ici, vous pouvez voir l'historique de l'exécution de la fonction. Pour lire la sortie, cliquez sur **Voir les logs dans CloudWatch**. Sélectionnez l'événement d'exécution lambda que vous voulez vérifier.

## Nombre d'exécutions estimées
_Fonction Lambda 2048Mo_

| # de lignes | Exécutif Date et heure |
| ------------ | ---------------------- |
| 10Ko         | 3s                     |
| 100Ko        | 30s                    |
| 1 Mo         | 5 minutes              |
| 5Mo          | 30 minutes             |

## Mise à jour d'une fonction existante

Si vous avez déjà déployé l'application et qu'une nouvelle version est disponible dans le référentiel, vous pouvez mettre à jour en redéployant la fonction comme si vous le faisiez pour la première fois. Cela signifie que vous devez passer à nouveau la clé d'API Braze et l'URL de l'API Braze. La mise à jour n'écrasera que le code de la fonction. Il ne modifiera pas ou ne supprimera pas les autres ressources existantes comme le compartiment S3.

## Erreur fatale

En cas d'erreur inattendue qui empêche le traitement ultérieur du fichier, un événement est enregistré (accessible via CloudWatch décrit dans [Surveillance et Logging](#monitoring-and-logging)) qui peut être utilisé pour redémarrer le Lambda à partir du moment où le programme a cessé de traiter le fichier. Il est important de ne pas réimporter les mêmes données pour enregistrer les Data Points. Vous pouvez trouver des instructions pour cela dans notre [dépôt Github](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error).

{% alert important %}
Visitez notre dépôt Github pour en savoir plus sur comment gérer les [erreurs fatales](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error) ou [configuration lambda](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#lambda-configuration).
{% endalert%}