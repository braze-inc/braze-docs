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

Amperity prend en charge la plateforme Braze en fournissant une vue unifiée de vos clients à travers sa plate-forme de données client et Braze. Cette intégration vous permet de :
- Synchroniser les segments de l'Amperity : Synchroniser les segments pour mapper les données de l'utilisateur d'Amperity aux comptes utilisateur de Braze.
- Données Unify : Unify data across various Amperity supported platform and Braze.
- Envoyer des données d'Amperity via AWS S3 Buckets au Brésil : Utilisez une fonction Lambda sans serveur pour téléverser les segments des utilisateurs d'Amperity dans votre seau AWS S3 qui affichera les données des attributs utilisateurs au Brésil.
- Téléchargez manuellement les données d'Amperity au Brésil : téléversez manuellement les segments CSV de l'utilisateur sur la plateforme Braze via le tableau de bord.

## Pré-requis

| Exigences         | Libellé                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------- |
| Compte d'ampérité | Un [compte d'ampérité](https://amperity.com/request-a-demo) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer un segment utilisateur d'ampérité

Pour télécharger des données utilisateur d'Amperity au Brésil, vous devez d'abord créer un segment des utilisateurs d'Amperity existants.
1. Naviguez vers l'onglet __Segments__ dans le tableau de bord de l'ampérité.<br>!\[Amperity Segments Overview\]\[2\]<br><br>
2. Cliquez sur __Créer__ pour filtrer et définir un segment d'utilisateurs à capturer. Sous l'onglet __Résumé__ , vous pouvez consulter des informations précieuses telles que les revenus historiques et les revenus prédits pour l'année à venir en fonction du segment utilisateur donné. <br>!\[Constructeur de Segment d'Amperity\]\[3\] <br><br>
3. Sélectionnez l'onglet __Clients__ , et choisissez quels champs d'utilisateur vous souhaitez inclure en utilisant le sélecteur __Afficher les colonnes__ sur la droite.<br>!\[Constructeur de Segment d'Amperity\]\[4\]<br><br>
4. Ensuite, cliquez sur __Exécuter le segment__.

### Étape 2 : Sélectionnez la méthode de téléchargement

Une fois le segment exécuté, vous pouvez soit :
- [Configurer le téléchargement automatique](#automatic-upload) - __Recommandé__
  - Configurez un flux de travail de destination pour télécharger automatiquement des données d'attribut d'utilisateur d'Amperity à Braze via un AWS S3 Bucket.
- [Configurer le téléchargement manuel](#manual-upload)
  - Téléchargez manuellement les segments de l'utilisateur CSV sur la plateforme Braze via le tableau de bord.

### Téléchargement automatique - téléchargement via un compartiment AWS S3 {#automatic-upload}

#### Étape 3 : Fixer la destination de Braze

##### Étape 3.1a : Activer le segment
!\[Segment 1\]\[7\]{: style="float:right;max-width:30%;margin-left:15px;"}

Tout d'abord, vous devez activer le segment en sélectionnant __Activer le segment__ dans le coin supérieur droit de la page.

Dans la fenêtre qui s'ouvre :
- Nommez votre destination __Braze__
- Définir le modèle de données à __par défaut__
- Entrez votre seau S3
- Entrez votre région S3
- Définir un modèle de nom de fichier
- Définir la fréquence de requête du workflow

Cliquez sur __Activer__.

##### Étape 3.2a : Configurer la destination

!\[Configuration de destination\]\[8\]{: style="float:right;max-width:37%;margin-left:15px;"}

Ensuite, vous devez configurer le workflow de destination de Braze en sélectionnant l'onglet __Destination__ et en cliquant sur __Ajouter une destination__.

Dans la fenêtre qui s'ouvre :
- Nommez votre destination __Braze__ et ajoutez une description facultative
- Sélectionnez le plugin __Amazon S3__
- Définir le type d'authentification à __iam-credential__
- Nommez et configurez les identifiants en fonction de vos paramètres Amazon S3
- Entrez votre seau S3
- Entrez votre région S3
- Encodage à __Aucun__
- Inclure la ligne d'en-tête dans les fichiers de sortie

Cliquez sur __Enregistrer__.

Vous trouverez une documentation supplémentaire d'Amperity sur la configuration d'Amazon S3 [ici](https://docs.amperity.com/configure/destination_amazon_s3.html).

#### Étape 4 : Envoyer des données via un seau AWS S3

##### Fonction Lambda

La fonction [Lambda suivante](https://github.com/braze-inc/growth-shares-lambda-user-csv-import) est une application sans serveur qui vous permet de publier facilement des données d'attributs utilisateur à partir d'un fichier d'Amperity CSV directement à Braze à travers le point de terminaison de Braze User Track. Ce processus se lance immédiatement lorsque vous téléchargez un fichier CSV vers un compartiment AWS S3 configuré. Pour en savoir plus, visitez notre [article de la fonction Lambda consacré](https://www.braze.com/docs/user_csv_lambda/).

##### Exigences et limitations

- __Compte AWS :__ Un compte AWS est requis pour utiliser les services S3 et Lambda.
- __L'URL de l'API Braze :__ Braze [API REST Endpoint]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) est nécessaire pour se connecter aux serveurs de Braze.
- __Clé API Braze :__ Une clé d'API [Braze]({{site.baseurl}}/api/basics/#app-group-rest-api-keys) avec une permission `utilisateur/piste` est requise pour envoyer des requêtes à [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) terminal.
- __Fichier CSV :__ Utilisez l'étape 1 des étapes d'intégration de l'ampérité pour obtenir un CSV avec des identifiants externes utilisateur et des attributs à mettre à jour.

La fonction Lambda peut gérer les gros fichiers et les envois, mais la fonction arrêtera l'exécution après 10 minutes en raison des limites de temps de Lambda. Ce processus lancera ensuite une autre instance Lambda pour terminer le traitement de la partie restante du fichier.

##### Formatage et traitement CSV

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

Pour commencer à traiter vos fichiers CSV d'Attribut Utilisateur, nous avons besoin de déployer l'application sans serveur pour gérer le traitement pour vous. Cette application créera automatiquement les ressources suivantes pour se déployer avec succès :

- Fonction Lambda
- S3 Seau pour vos fichiers CSV que le processus Lambda peut lire (_Note : cette fonction Lambda ne recevra que des notifications pour `. sv` fichiers d'extension_)
- Rôle permettant la création de ce qui précède
- Politique permettant à Lambda de recevoir un événement de téléchargement S3 dans le nouveau seau

Suivez le lien direct vers l'application [](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import) ou ouvrez le [dépôt d'application sans serveur AWS](https://serverlessrepo.aws.amazon.com/applications) et recherchez _l'attribut-utilisateur braze-import_. Notez que vous devez cocher la case __Afficher les applications qui créent des rôles personnalisés IAM et des politiques de ressources__ pour voir cette application. L'application crée une politique pour que les Lambda lisent à partir du compartiment S3 nouvellement créé.

Cliquez sur **Déployer** et laissez AWS créer toutes les ressources nécessaires.

Vous pouvez surveiller le déploiement et vérifier que la pile (c'est-à-dire toutes les ressources requises) est en cours de création dans la [CloudFormation](https://console.aws.amazon.com/cloudformation/). Trouvez la pile nommée __serverlessrepo-braze-user-attribute-import__. Une fois que le **Statut** tourne à `CREATE_COMPLETE`, la fonction est prête à être utilisée. Vous pouvez cliquer sur la pile et ouvrir **Ressources** et regarder les différentes ressources en cours de création.

Les ressources suivantes ont été créées :

- [S3 Bucket](https://s3.console.aws.amazon.com/s3/) - un seau nommé `braze-user-csv-import-aaa123` où `aaa123` est une chaîne générée aléatoirement
- [Lambda Function](https://console.aws.amazon.com/lambda/) - une fonction Lambda appelée `braze-user-attribute-import`
- [Rôle IAM](https://console.aws.amazon.com/iam/) - politique nommée `braze-user-csv-import-BrazeUserCSVImportRole` pour permettre à Lambda de lire à partir de S3 et d'enregistrer la sortie de la fonction

###### Exécuter

Pour exécuter la fonction, déposez un fichier CSV d'attribut utilisateur dans le compartiment S3 nouvellement créé.

{% alert important %}
Pour en savoir plus sur les différents aspects de la fonction Lambda tels que la surveillance et l'enregistrement, la mise à jour d'une fonction existante, les erreurs fatales, et plus encore. Visitez notre [article consacré à la fonction Lambda](https://www.braze.com/docs/user_csv_lambda/).
{% endalert %}

### Téléchargement manuel - téléchargement via CSV {#manual-upload}

#### Étape 3b: Plate-forme d'ampérité

1. Une fois le segment exécuté, cliquez sur __Voir SQL__. Cela générera une requête SQL qui préformatera les données pour qu'elles fonctionnent correctement avec ce qui est requis par la plate-forme Braze. Assurez-vous que les noms des champs correspondent aux champs de Braze dans lesquels vous voulez charger les données. Si vous souhaitez le personnaliser, vous pouvez convertir le segment en SQL et l'alias des champs. Cliquez sur __Exécuter la requête__ pour exécuter la requête SQL.<br>!\[Amperity Segment Builder\]\[5\]<br><br>
2. Enfin, cliquez sur __Télécharger__ pour télécharger une version CSV de ce segment d'utilisateur. C'est le fichier que vous allez télécharger sur Braze.

#### Étape 4b: Plateforme Braze

1. Depuis la plate-forme de Braze, allez à la page __Import d'utilisateur__ listée sous __Utilisateurs__.
2. Télécharger le fichier CSV téléchargé à partir de l'ampérité.
3. Une fois téléchargé, confirmez les attributs par défaut et personnalisés, attribuez un nom d'importation, et éventuellement créer un groupe au sein de la plate-forme Braze à partir du segment d'Amperity téléchargé.
4. Cliquez sur __Démarrer l'import__.
[2]: {% image_buster /assets/img/amperity/amperity2.png %} [3]: {% image_buster /assets/img/amperity/amperity3.png %} [4]: {% image_buster /assets/img/amperity/amperity4. ng %} [5]: {% image_buster /assets/img/amperity/amperity5.png %} [7]: {% image_buster /assets/img/amperity/activate2. ng %} [8]: {% image_buster /assets/img/amperity/destinationconfiguration.png %} 
