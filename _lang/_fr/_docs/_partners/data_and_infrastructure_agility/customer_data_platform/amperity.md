---
nav_title: Amperité
article_title: Amperité
alias: /fr/partners/amperity/
description: "Cet article traite de l’intégration de Braze et de l’Amperity. L'ampérité fournit des capacités intelligentes à travers l'unification de la gestion des données, l'analyse et les connaissances et l'activation."
page_type: partenaire
page_order: 2.2
search_tag: Partenaire
---

# Amperité

> [Amperity](https://amperity.com/) est une plate-forme de données globale pour les clients d'entreprise, aidant les marques à connaître leurs clients, prendre des décisions stratégiques et prendre systématiquement la bonne voie pour mieux servir les consommateurs. L'ampérité fournit des capacités intelligentes à travers l'unification de la gestion des données, l'analytique, les connaissances et l'activation.

{% include video.html id="06G0lxaSjgk" align="right" %}

L'intégration de Braze et d'Amperity offre une vision unifiée de vos clients sur les deux plateformes. Cette intégration vous permet de :
- **Synchroniser les segments d'ampérité**: Synchroniser les segments pour mapper les données de l'utilisateur d'Amperity à Braze.
- **Données Unify**: Unify data across various Amperity supported platform and Braze.
- **Envoyer des données d'Amperity via des seaux AWS S3 à Braze**: Utilisez une fonction Lambda sans serveur pour télécharger des segments d'utilisateur d'Amperity sur votre seau AWS S3 qui affichera les données d'attribut utilisateur au Brésil.
- **Télécharger manuellement des données d'Amperity sur Braze**: Téléchargez manuellement les segments CSV de l'utilisateur sur la plateforme Braze via le tableau de bord.

## Pré-requis

| Exigences         | Libellé                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------- |
| Compte d'ampérité | Un [compte d'ampérité](https://amperity.com/request-a-demo) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer un segment utilisateur d'ampérité

Pour télécharger des données utilisateur d'Amperity au Brésil, vous devez d'abord créer un segment des utilisateurs d'Amperity existants.
1. Naviguez vers l'onglet **Segments** dans le tableau de bord de l'ampérité.<br>!\[Aperçu des segments d'ampérité\]\[2\]<br><br>
2. Cliquez sur **Créer** pour filtrer et définir un segment d'utilisateurs à capturer. Sous l'onglet **Résumé** , vous pouvez consulter des informations précieuses telles que les revenus historiques et les revenus prédits pour l'année à venir en fonction du segment utilisateur donné. <br>!\[Constructeur de segment d'ampérité\]\[3\] <br><br>
3. Sélectionnez l'onglet **Clients** , et choisissez quels champs d'utilisateur vous souhaitez inclure en utilisant le sélecteur **Afficher les colonnes** sur la droite.<br>!\[Générateur de segment d'ampérité\]\[4\]<br><br>
4. Ensuite, cliquez sur **Exécuter le segment**.

### Étape 2 : Sélectionnez la méthode de téléchargement

Une fois le segment exécuté, vous pouvez soit :
- [Configurer le téléchargement automatique](#automatic-upload) - **recommandé**
  - Configurez un flux de travail de destination pour télécharger automatiquement des données d'attribut d'utilisateur d'Amperity à Braze via un AWS S3 Bucket.
- [Configurer le téléchargement manuel](#manual-upload)
  - Téléchargez manuellement les segments de l'utilisateur CSV sur la plateforme Braze via le tableau de bord.

### Téléchargement automatique via bucket AWS S3 {#automatic-upload}

#### Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                           |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte AWS                      | Un compte AWS est requis pour utiliser les services S3 et Lambda.                                                                                                                                                 |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API**      |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).                                             |
| Fichier CSV                     | Consultez les [spécifications de formatage CSV](#csv), et utiliser l'étape 1 de l'intégration de l'Amperity pour obtenir un CSV avec les identifiants externes de l'utilisateur et les attributs à mettre à jour. |
{: .reset-td-br-1 .reset-td-br-2}

#### Étape 3 : Fixer la destination de Braze

##### Activer le segment

Tout d'abord, vous devez activer le segment en sélectionnant **Activer le segment** dans le coin supérieur droit de la page.

Dans la fenêtre qui s'ouvre :
- Nommez votre destination **Braze**
- Définir le modèle de données à **par défaut**
- Entrez votre seau S3
- Entrez votre région S3
- Définir un modèle de nom de fichier
- Définir la fréquence de requête du workflow

!\[Segment 1\]\[7\]{: style="max-width:60%;"}

Cliquez sur **Activer**.

##### Configurer la destination

Ensuite, vous devez configurer le workflow de destination de Braze en sélectionnant l'onglet **Destination** et en cliquant sur **Ajouter une destination**.

Dans la fenêtre qui s'ouvre :
- Nommez votre destination **Braze** et ajoutez une description facultative
- Sélectionnez le plugin **Amazon S3**
- Définir le type d'authentification à **iam-credential**
- Nommez et configurez les identifiants en fonction de vos paramètres Amazon S3
- Entrez votre seau S3
- Entrez votre région S3
- Encodage à **Aucun**
- Inclure la ligne d'en-tête dans les fichiers de sortie

!\[Configuration de destination\]\[8\]{: style="max-width:60%;"}

Cliquez sur **Enregistrer**.

Vous trouverez une documentation supplémentaire d'Amperity sur la configuration d'Amazon S3 [ici](https://docs.amperity.com/configure/destination_amazon_s3.html).

#### Étape 4 : Envoyer des données via un seau AWS S3

##### Fonction Lambda

La fonction [Lambda suivante](https://github.com/braze-inc/growth-shares-lambda-user-csv-import) est une application sans serveur qui vous permet de publier facilement des données d'attributs utilisateur à partir d'un fichier d'Amperity CSV directement à Braze à travers les utilisateurs/tracks/endpoint de Braze. Ce processus se lance immédiatement lorsque vous téléchargez un fichier CSV vers un compartiment AWS S3 configuré. Pour en savoir plus, visitez notre [article de la fonction Lambda consacré](https://www.braze.com/docs/user_csv_lambda/).

La fonction Lambda peut gérer les gros fichiers et les envois, mais la fonction arrêtera l'exécution après 10 minutes en raison des limites de temps de Lambda. Ce processus lancera ensuite une autre instance Lambda pour terminer le traitement de la partie restante du fichier.

##### Formatage et traitement CSV {#csv}

###### Attributs utilisateur CSV

Les attributs de l'utilisateur à mettre à jour doivent être au format `.csv` suivant :

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

La première colonne doit spécifier l'ID externe de l'utilisateur à mettre à jour, et les colonnes suivantes doivent spécifier les noms et valeurs des attributs. Le nombre d'attributs que vous spécifiez peut varier. Si le fichier CSV à traiter ne suit pas ce format, la fonction échouera.

Exemple de fichier CSV :

```
external_id,Points de fidélité,Dernière marque achetée
abc123,1982, Salomon
def456,578,Hunter-Hayes
```

###### Traitement CSV

N'importe quelle valeur dans un tableau (ex. `"['Valeur1', 'Value2']"`) sera automatiquement détruit et envoyé à l'API dans un tableau plutôt qu'une représentation de chaîne de caractères d'un tableau.

##### Instructions d'utilisation

1. Déployer le traitement CSV de Braze disponible publiquement Lambda à partir du dépôt d'applications sans serveur AWS.
2. Déposez un fichier CSV avec les attributs utilisateur dans le compartiment S3 nouvellement créé.
3. Les utilisateurs seront automatiquement importés en Brésil.

###### Déployer

Pour commencer à traiter vos fichiers CSV d'attribut utilisateur, nous devons déployer l'application sans serveur pour gérer le traitement pour vous. Cette application créera automatiquement les ressources suivantes pour se déployer avec succès :
- Fonction Lambda
- S3 Seau pour vos fichiers CSV que le processus Lambda peut lire à partir de cette fonction Lambda ne recevra que des notifications pour `. sv` fichiers d'extension.
- Rôle permettant la création de ce qui précède
- Politique permettant à Lambda de recevoir un événement de téléchargement S3 dans le nouveau seau

Suivez le lien direct vers l'application [](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import) ou ouvrez le [dépôt d'application sans serveur AWS](https://serverlessrepo.aws.amazon.com/applications) et recherchez **l'attribut-utilisateur braze-import**. Vous devez cocher la case **Afficher les applications qui créent des rôles personnalisés IAM et des politiques de ressources** pour voir cette application. L'application crée une politique pour que les Lambda lisent à partir du compartiment S3 nouvellement créé.

Cliquez sur **Déployer** et laissez AWS créer toutes les ressources nécessaires.

Vous pouvez surveiller le déploiement et vérifier que la pile (c'est-à-dire toutes les ressources requises) est en cours de création dans la [CloudFormation](https://console.aws.amazon.com/cloudformation/). Trouvez la pile nommée **serverlessrepo-braze-user-attribute-import**. Une fois que le **Statut** tourne à `CREATE_COMPLETE`, la fonction est prête à être utilisée. Vous pouvez cliquer sur la pile, ouvrir **Ressources**et regarder les différentes ressources créées.

Les ressources suivantes ont été créées :

- [S3 bucket](https://s3.console.aws.amazon.com/s3/) - un bucket nommé `braze-user-csv-import-aaa123` où `aaa123` est une chaîne générée aléatoirement
- [Fonction Lambda](https://console.aws.amazon.com/lambda/) - une fonction Lambda appelée `braze-user-attribute-import`
- [Rôle IAM](https://console.aws.amazon.com/iam/) - politique nommée `braze-user-csv-import-BrazeUserCSVImportRole` pour permettre à Lambda de lire à partir de S3 et d'enregistrer la sortie de la fonction

###### Exécuter

Pour exécuter la fonction, déposez un fichier CSV d'attribut utilisateur dans le compartiment S3 nouvellement créé.

{% alert important %}
Pour en savoir plus sur les différents aspects de la fonction Lambda tels que la surveillance et l'enregistrement, la mise à jour d'une fonction existante, erreurs fatales, et plus encore, visitez notre [article de fonction Lambda dédié](https://www.braze.com/docs/user_csv_lambda/).
{% endalert %}

### Téléchargement manuel via CSV {#manual-upload}

#### Étape 3b: Créer une ampérité CSV

1. Une fois le segment exécuté, cliquez sur **Voir SQL**. Cela générera une requête SQL qui préformatera les données pour qu'elles fonctionnent correctement avec ce qui est requis par la plate-forme Braze. Assurez-vous que les noms des champs correspondent aux champs de Braze dans lesquels vous voulez charger les données. Si vous souhaitez le personnaliser, vous pouvez convertir le segment en SQL et l'alias des champs. Cliquez sur **Exécuter la requête** pour exécuter la requête SQL.<br>!\[Générateur de segment d'ampérité\]\[5\]<br><br>
2. Enfin, cliquez sur **Télécharger** pour télécharger une version CSV de ce segment d'utilisateur. C'est le fichier que vous allez télécharger sur Braze.

#### Étape 4b: Importer CSV

1. Depuis la plate-forme de Braze, allez à la page **Import d'utilisateur** listée sous **Utilisateurs**.
2. Télécharger le fichier CSV téléchargé à partir de l'ampérité.
3. Une fois téléchargé, confirmez les attributs par défaut et personnalisés, attribuez un nom d'importation, et éventuellement créer un groupe au sein de la plate-forme Braze à partir du segment d'Amperity téléchargé.
4. Cliquez sur **Démarrer l'import**.
[2]: {% image_buster /assets/img/amperity/amperity2.png %} [3]: {% image_buster /assets/img/amperity/amperity3.png %} [4]: {% image_buster /assets/img/amperity/amperity4. ng %} [5]: {% image_buster /assets/img/amperity/amperity5.png %} [7]: {% image_buster /assets/img/amperity/activate2. ng %} [8]: {% image_buster /assets/img/amperity/destinationconfiguration.png %} 
