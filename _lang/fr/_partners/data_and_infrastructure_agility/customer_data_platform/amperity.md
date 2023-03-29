---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "Cet article de référence décrit le partenariat entre Braze et Amperity, une plateforme complète de données client d’entreprise, vous permettant de synchroniser les utilisateurs d’Amperity, d’unifier les données, d’envoyer des données à Braze à l’aide des compartiments AWS S3, etc."
page_type: partner
page_order: 2.2
search_tag: Partenaire

---

# Amperity

> [Amperity](https://amperity.com/) est une plateforme de données client complète qui aide les marques à connaître leurs clients, à prendre des décisions stratégiques et à adopter systématiquement la meilleure ligne de conduite pour mieux servir leurs consommateurs. Amperity fournit des capacités intelligentes d’unification de la gestion des données, d’analyses, de renseignements et d’activation.

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

L’intégration de Braze et d’Amperity fournit une vue unifiée de vos clients sur les deux plateformes. Cette intégration vous permet de :
- **Synchroniser des utilisateurs Amperity** : Synchronisez des listes d’utilisateurs pour mapper les données utilisateur d’Amperity aux comptes utilisateur Braze.
- **Unifier les données** : Unifiez les données sur Braze et diverses plateformes compatibles avec Amperity.
- **Envoyer des données d’Amperity à Braze via les compartiments AWS S3** : Utilisez une fonction Lambda sans serveur pour charger des listes d’utilisateurs Amperity dans votre compartiment AWS S3 qui publiera les données d’attributs utilisateur dans Braze.
- **Télécharger manuellement des données Amperity dans Braze** : Téléchargez manuellement des listes CSV d’utilisateurs sur la plateforme Braze via le tableau de bord.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Amperity | Un [compte Amperity](https://amperity.com/request-a-demo) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer une liste d’utilisateurs Amperity

Pour télécharger des données d’utilisateur Amperity dans Braze, vous devez configurer une destination qui permet d’envoyer les résultats de requête à Braze, créer une requête qui renvoie une liste d’utilisateurs et envoyer les résultats de cette requête à Braze en utilisant l’orchestration.

1. Ajoutez une [destination Braze](https://docs.amperity.com/datagrid/destination_braze.html) pour votre locataire.
2. Accédez à l’onglet **Queries (Requêtes)** dans le tableau de bord d’Amperity. 
3. Cliquez sur **Create (Créer)**, puis sur **Select SQL Query (Sélectionner la requête SQL)** pour définir la requête SQL qui renverra une liste d’utilisateurs. Par exemple :
``` sql
SELECT
 amperity_id
 ,external_id AS external_id
 ,email AS email
 ,given_name AS first_name
 ,surname AS last_name
 -- add more attributes, as desired
FROM Merged_Customers
```
4. Cliquez sur **Run (Exécuter)** pour valider votre requête. Lorsque vous avez terminé, cliquez sur **Activate (Activer)**. <br>![Le résumé d’une requête Amperity qui a créé avec succès une liste d’utilisateurs à envoyer à Braze.][9] <br><br>
5. Ajoutez cette requête à une orchestration configurée pour [envoyer une liste d’utilisateurs à Braze](https://docs.amperity.com/amp360/sendto_braze.html).<br>![Un résumé montrant l’activation de votre requête Braze, qui est ensuite ajoutée à une orchestration configurée pour Braze.][10]

### Étape 2 : Sélectionner la méthode de téléchargement

Une fois la requête exécutée, vous pouvez :
- [Configurer un téléchargement automatique](#automatic-upload) - **recommandé**
  - Configurez un flux de travail de destination pour charger automatiquement les données d’attributs utilisateur Amperity dans Braze via un compartiment AWS S3.
- [Configurer le téléchargement manuel](#manual-upload)
  - Téléchargez manuellement des listes CSV d’utilisateurs sur la plateforme Braze via le tableau de bord. 

### Chargement automatique via un compartiment S3 {#automatic-upload}

#### Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte AWS | Un compte AWS est requis pour utiliser les services S3 et Lambda. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| Fichier CSV | Consultez la section [Spécifications de formatage CSV](#csv), et suivez l’étape 1 de l’intégration Amperity pour obtenir un fichier CSV avec des ID externes et des attributs utilisateur à mettre à jour. |
{: .reset-td-br-1 .reset-td-br-2}

#### Étape 4a : Envoyer des données via un compartiment AWS S3

##### Fonction Lambda 

La [fonction Lambda](https://github.com/braze-inc/growth-shares-lambda-user-csv-import) ci-dessous est une application sans serveur qui vous permet de publier facilement des données d’attributs utilisateur d’un fichier CSV Amperity dans Braze via l’endpoint users/track de Braze. Ce processus démarre immédiatement lors du téléchargement d’un fichier CSV dans un compartiment AWS S3 configuré. Pour en savoir plus, consultez notre [article sur la fonction Lambda dédiée]({{site.baseurl}}/user_csv_lambda/).

La fonction Lambda peut gérer des fichiers et des téléchargements volumineux, mais la fonction s’arrêtera après 10 minutes en raison des limites de temps Lambda. Ce processus lancera ensuite une autre instance Lambda pour traiter la partie restante du fichier.

##### Formatage et traitement des CSV {#csv}

###### Attributs utilisateur CSV

Les attributs utilisateur à mettre à jour doivent présenter le format `.csv` suivant :

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

###### Traitement CSV

Toutes les valeurs d’une matrice (par ex. `"['Value1', 'Value2']"`) seront automatiquement déstructurées et envoyées à l’API dans un tableau plutôt que dans une représentation de chaîne de caractères d’un tableau.

##### Instructions d’utilisation

1. Déployer la fonction Lambda de traitement CSV disponible publiquement de Braze depuis le référentiel d’applications sans serveur AWS.
2. Déposez un fichier CSV avec des attributs utilisateur dans le nouveau compartiment S3.
3. Les utilisateurs seront automatiquement importés dans Braze.

###### Déployer

Pour commencer à traiter les fichiers CSV de vos attributs utilisateur, nous devons déployer l’application sans serveur afin qu’elle gère le traitement pour vous. Cette application créera automatiquement les ressources ci-dessous pour assurer un déploiement réussi :
- Fonction Lambda
- Compartiment S3 pour vos fichiers CSV que le processus Lambda peut lire. Cette fonction Lambda recevra uniquement des notifications pour les fichiers de type CSV.
- Rôle permettant de créer un compartiment S3
- Politique permettant à Lambda de recevoir un événement de chargement S3 dans le nouveau compartiment

Suivez le lien direct vers l’[application](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import) ou ouvrez le [Référentiel d’applications sans serveur AWS](https://serverlessrepo.aws.amazon.com/applications) et recherchez **braze-user-attribute-import**. Pour voir cette application, vous devez cocher la case **Show apps that create custom IAM roles and resource policies (Afficher les applications qui créent des rôles IAM et des politiques de ressources personnalisés)**. L’application crée une politique pour que Lambda puisse lire le nouveau compartiment S3.

Cliquez sur **Deploy (Déployer)** et laissez AWS créer toutes les ressources nécessaires.

Vous pouvez suivre le déploiement et vérifier que la pile (c.-à-d. toutes les ressources requises) est créée dans [CloudFormation](https://console.aws.amazon.com/cloudformation/). Trouvez la pile appelée **serverlessrepo-braze-user-attribute-import**. La fonction est prête à être utilisée dès que le **Status (Statut)** passe sur `CREATE_COMPLETE`. Vous pouvez cliquer sur la pile, ouvrir **Resources (Ressources)** et suivre les différentes ressources qui sont en train d’être créées.

Les ressources créées sont :

- [Compartiment S3](https://s3.console.aws.amazon.com/s3/) : un compartiment nommé `braze-user-csv-import-aaa123` où `aaa123` est une chaîne générée aléatoirement
- [Fonction Lambda](https://console.aws.amazon.com/lambda/) : une fonction Lambda nommée `braze-user-attribute-import`
- [Rôle IAM](https://console.aws.amazon.com/iam/) - une politique nommée `braze-user-csv-import-BrazeUserCSVImportRole` pour permettre à Lambda de lire les fichiers S3 et de consigner les résultats de la fonction

###### Exécuter

Pour exécuter cette fonction, déposez un fichier CSV d’attributs utilisateur dans le nouveau compartiment S3.

{% alert important %}
Pour en savoir plus sur les différents aspects de la fonction Lambda, tels que la surveillance et la journalisation, la mise à jour d’une fonction existante, les erreurs fatales et bien plus encore, consultez notre [article sur la fonction Lambda dédiée]({{site.baseurl}}/user_csv_lambda/). 
{% endalert %}

### Chargement manuel via CSV {#manual-upload}

#### Étape 3b : Créer un fichier CSV Amperity

1. Après avoir exécuté et activé votre requête, vous pouvez télécharger le fichier CSV de votre requête en cliquant sur **Download (Télécharger)**. Il s’agit du fichier que vous allez télécharger sur Braze.<br>![Le résumé d’une requête Amperity qui a créé avec succès une liste d’utilisateurs à envoyer à Braze.][9] 

#### Étape 4b : Importer un fichier CSV

1. Depuis la plateforme Braze, accédez à la page **User Import (Importation d’utilisateurs)** affichée sous **Users (Utilisateurs)**.
2. Téléchargez le fichier CSV que vous avez obtenu sur Amperity.
3. Une fois téléchargé, confirmez les attributs par défaut et personnalisés, attribuez un nom d’importation et créez un groupe (facultatif) dans la plateforme Braze à partir de la requête d’Amperity que vous avez téléchargé. 
4. Cliquez sur **Start Import (Démarrer l’importation)**.

[2]: {% image_buster /assets/img/amperity/amperity2.png %} 
[3]: {% image_buster /assets/img/amperity/amperity3.png %} 
[4]: {% image_buster /assets/img/amperity/amperity4.png %} 
[5]: {% image_buster /assets/img/amperity/amperity5.png %} 
[7]: {% image_buster /assets/img/amperity/activate2.png %} 
[8]: {% image_buster /assets/img/amperity/destinationconfiguration.png %} 
[9]: {% image_buster /assets/img/amperity/amperity6.png %} 
[10]: {% image_buster /assets/img/amperity/amperity7.png %} 
