---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "Cet article de référence décrit le partenariat entre Braze et Amperity, une plateforme de données client complète pour les entreprises, vous permettant de synchroniser les utilisateurs d'Amperity, d'unifier les données, d'envoyer des données en utilisant des buckets AWS S3 vers Braze, et plus encore."
page_type: partner
search_tag: Partner

---

# Amperity

> [Amperity](https://amperity.com/) est une plateforme de données client complète pour les entreprises, aidant les marques à mieux connaître leurs clients, à prendre des décisions stratégiques et à adopter systématiquement la bonne démarche pour mieux servir leurs consommateurs. Amperity fournit des capacités intelligentes dans l'unification de la gestion des données, l'analyse, les informations et l'activation.

_Cette intégration est maintenue par Amperity._

{% multi_lang_include video.html ID="06G0lxaSjgk" align="right" %}

L'intégration de Braze et Amperity offre une vue unifiée de vos clients sur les deux plateformes. Cette intégration vous permet de :
- **Synchroniser les profils clients**: Mapper les données utilisateur et les attributs personnalisés d'Amperity à Braze. 
- **Créer et envoyer des audiences** : Créez des segments qui renvoient des listes de clients actifs et leurs attributs personnalisés associés à Braze, et envoyez-les à Braze.
- **Gérer les mises à jour des données**: Contrôlez la fréquence d'envoi des mises à jour des attributs personnalisés à Braze.
- **Unifier les données** : Unifier les données sur diverses plateformes prises en charge par Amperity et Braze.
- **Synchroniser les données de Braze avec Amazon S3**: Utilisez Braze Currents pour intégrer les données d'engagement des campagnes Braze, vous permettant de synchroniser les données vers Amazon S3 au format Apache Avro.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| compte Amperity | Un [compte Amperity](https://amperity.com/request-a-demo) est requis pour profiter de ce partenariat. |
| Clé d'API REST Braze | Une clé API REST de Braze avec des autorisations `users.track`. <br> Cela peut être créé dans le tableau de bord de Braze en accédant à la **console de développement** > **clé API REST** > **Créer une nouvelle clé API**. |
| instance Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'onboarding Braze ou sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics#endpoints). |
| Endpoint REST Braze | Votre URL d'endpoint Braze. Votre endpoint dépendra de votre instance Braze. |
| Connecteur Currents (facultatif) | Le connecteur S3 Currents. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mappage des données

Les attributs standard et personnalisés peuvent être envoyés d'Amperity à Braze, vous permettant d'enrichir les profils clients dans Braze avec des données provenant de diverses sources via Amperity. Les attributs spécifiques que vous pouvez envoyer dépendront des données dans votre système Amperity et des attributs que vous avez configurés dans Braze.

Lisez ci-dessous pour en savoir plus sur ces attributs.

### Attributs standard 

Les [attributs de profil]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) décrivent qui sont vos clients. Ils sont souvent associés à l'identité du client, tels que :
- Noms
- Dates de naissance
- adresses e-mail
- Numéros de téléphone

### Attributs personnalisés 

[Attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) dans Braze sont des champs déterminés par votre marque. Si vous souhaitez qu'Amperity gère des attributs personnalisés qui existent déjà dans Braze, alignez la sortie envoyée par Amperity avec les noms déjà présents dans votre espace de travail Braze. Cela peut inclure les éléments suivants :
- Historiques d'achats
- Statut de fidélité
- Niveaux de valeur
- Données d'engagement récentes

Vérifiez les noms des attributs personnalisés qui seront envoyés à Braze depuis Amperity. Amperity ajoutera un attribut personnalisé chaque fois qu'il n'y aura pas de nom correspondant.

Les attributs personnalisés ne seront mis à jour que pour les utilisateurs ayant une correspondance `external_id` ou `braze_id` dans Braze.

### Audiences Amperity

Les audiences synchronisées d'Amperity à Braze seront enregistrées dans les profils utilisateurs en tant qu'attributs personnalisés. Ils peuvent ensuite être utilisés pour cibler ces utilisateurs dans Braze.

![Liste déroulante de filtres avec attributs personnalisés s'affichant dans la catégorie Données personnalisées.]({% image_buster /assets/img/amperity/custom_attributes_filters.png %}){: style="max-width:60%;"}

![Liste déroulante d'attributs personnalisés tels que "l12m_frequency" et "l12m_monetary".]({% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}){: style="max-width:40%;"}

### Types de données

Les types de données pris en charge incluent :
- Booléen
- Date
- Date et heure
- Décimal
- float
- Entier
- Chaîne de caractères
- Varchar

Le type de données utilisé dépend de la nature de l'attribut. Par exemple, une adresse e-mail serait une chaîne de caractères, tandis que l'âge d'un client pourrait être un entier.

### Duplication des attributs

Évitez d'envoyer des attributs personnalisés qui dupliquent les champs de profil utilisateur par défaut. Par exemple, les dates de naissance doivent être envoyées à Braze sous la forme d'un champ de profil utilisateur nommé "dob" pour correspondre à l'attribut standard de Braze. S'ils sont envoyés comme "anniversaire", "Date de naissance" ou toute autre chaîne de caractères, un attribut personnalisé sera créé, et les valeurs dans le champ "dob" ne seront pas mises à jour.

### Points de données

Amperity suit les changements entre les synchronisations avec Braze et l'état des envois dans l'ensemble. Amperity n'enverra à Braze que l'appartenance à la liste et d'autres attributs choisis qui ont changé depuis la dernière synchronisation.  

## Intégration

### Étape 1 : Capturez les détails de configuration de Braze

1. Créez une clé API REST Braze pour votre espace de travail Braze avec les `users.track` autorisations sous **Données utilisateur**. L'endpoint `users.track` synchronise l'audience Amperity avec Braze en tant qu'attribut personnalisé.
2. Déterminez l'[endpoint de l'API REST]({{site.baseurl}}/api/basics#endpoints) pour votre instance Braze. Par exemple, si votre URL Braze est `https://dashboard-03.braze.com`, votre endpoint REST API est `https://rest.iad-03.braze.com` et votre instance est « US-03 ».
3. Déterminer une liste de [champs de profil utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) et [attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) qui peuvent être envoyés à Braze depuis Amperity.

### Étape 2 : Configurer Braze en tant que destination—Opérateur DataGrid

#### Étape 2a : Créer la table des profils clients

Créez une nouvelle table nommée "Attributs des clients Braze" dans votre base de données Customer 360 dans Amperity. Cette table doit contenir tous les attributs de Braze que votre marque souhaite gérer depuis Amperity, y compris les champs de profil utilisateur par défaut requis par Braze et tous les attributs personnalisés. Utilisez SQL pour définir la structure de cette table comme indiqué dans [la documentation Amperity](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table).

#### Étape 2b : Nommer, valider et enregistrer la table

Nommez la table "Braze Customer Attributes" et enregistrez-la. Vérifiez que la table est accessible à l'**Éditeur de segment** et à l'**éditeur de modifier les attributs** dans les campagnes.

#### Étape 2c: Ajouter Braze comme destination

Dans la plateforme Amperity, accédez à l'onglet **Destinations**. Cherchez l'option pour ajouter une nouvelle destination. Parmi les options disponibles, sélectionnez **Braze**.

![La section Nouvelle destination dont le nom est "API Braze", la description "Envoyer les attributs de l'audience à Braze" et le plugin "Braze".]({% image_buster /assets/img/amperity/destination_name.png %}){: style="max-width:60%;"}

#### Étape 2d : Configurer les détails de la destination

Sous les **Paramètres Braze**, fournissez les identifiants Braze et les paramètres de destination, comme indiqué dans [la documentation Amperity](https://docs.amperity.com/datagrid/destination_braze.html#add-destination). Saisissez les détails de configuration collectés à l'étape précédente et définissez l'identifiant Braze. Identifiants disponibles à correspondre sont :
- `braze_id`: Un identifiant Braze attribué automatiquement qui est immuable et associé à un utilisateur particulier lorsqu'il est créé dans Braze.
- `external_id`: Un identifiant attribué par le client, généralement un UUID. 

![La section Paramètres de Braze avec une instance de "US-03", un identifiant utilisateur de "external_id", un nom de segment vide, un compartiment S3 de "amperity-training-abc123" et un dossier S3 de "braze-attributes".]({% image_buster /assets/img/amperity/braze_settings.png %}){: style="max-width:60%;"}

#### Étape 2e : Ajouter un modèle de donnée

Dans l'**Destinations** onglet, ouvrez le menu pour la destination Braze et sélectionnez **Ajouter un modèle de donnée**. Entrez un nom et une description pour le modèle (par exemple, "Braze" et "Envoyer des attributs personnalisés à Braze"), vérifiez l'accès de l'utilisateur et vérifiez tous les paramètres de configuration. 

Si des paramètres requis n'ont pas été configurés dans le cadre de la destination, configurez-les dans le cadre du modèle de données. Enregistrer le modèle de données.

![La section Nom du modèle de données avec le nom "Attributs d'audience de Braze" et la description "Envoyer les attributs d'audience à Braze".]({% image_buster /assets/img/amperity/data_template_name.png %}){: style="max-width:60%;"}

#### Étape 2f: enregistrer la configuration 

Après avoir rempli les détails nécessaires, enregistrez la configuration. Maintenant que Braze est configuré comme destination, les utilisateurs d'Amp360 et d'AmpIQ peuvent synchroniser des données avec Braze.

### Étape 3 : Synchroniser les données avec Braze

Assurez-vous que Braze est activé pour votre locataire Amperity. Si ce n'est pas le cas, contactez votre opérateur DataGrid ou votre représentant Amperity pour obtenir de l'aide.

Ensuite, suivez les instructions de synchronisation pour Amp360 ou AmpIQ, selon ce qui est applicable à votre entreprise.

#### Option de synchronisation 1 : Envoyer les résultats de la requête à Braze via Amp360

Les utilisateurs d'Amp360 peuvent utiliser SQL pour écrire des requêtes libres, puis configurer une planification qui envoie les résultats à Braze.

##### Étape 1 : Créer une requête dans Amperity

Accédez à la fonction de requête dans Amperity et construisez une requête SQL qui produira l'ensemble de données client souhaité. Les résultats doivent inclure les attributs spécifiques que vous souhaitez envoyer à Braze. Voir cet exemple de requête Amperity pour renvoyer une liste d'utilisateurs avec leurs historiques d'achats.

##### Étape 2 : Ajouter une nouvelle orchestration dans Amperity

1. Allez à la section **Orchestration** et cliquez sur l'option pour ajouter une nouvelle orchestration. 
2. Spécifiez ce que l'orchestration doit faire. Cela implique généralement de spécifier la requête SQL qui doit être exécutée et où les résultats qui doivent être envoyés. Dans ce cas, sélectionnez la requête SQL que vous avez créée pour générer la liste des clients actifs et spécifiez Braze comme destination pour les résultats.
3. Définir quand et à quelle fréquence l'orchestration doit s'exécuter. Par exemple, vous pouvez orchestrer les données quotidiennement, à une heure précise.
4. Enregistrer l'orchestration après l'avoir configurée à votre goût. Il sera ajouté à votre liste d'orchestrations dans Amperity.
5. Testez l'orchestration pour vous assurer qu'elle fonctionne comme prévu. Vous pouvez le faire en déclenchant manuellement l'orchestration et en vérifiant les résultats dans Braze.

##### Étape 3 : Exécutez l'orchestration 

Exécutez l'orchestration pour exécuter la requête et envoyer les résultats à Braze. Cela peut être fait manuellement ou selon la planification que vous avez définie dans les paramètres d'orchestration.

#### Option de synchronisation 2 : Envoyez des audiences à Braze via AmpIQ

Les utilisateurs d'AmpIQ peuvent créer des segments dans Amperity via une interface non-SQL et les synchroniser vers des destinations en aval telles que Braze. Les utilisateurs peuvent sélectionner des destinations, puis configurer une liste d'attributs à envoyer à chaque destination.

##### Étape 1 : Créer un segment dans Amperity 

Créez un segment dans Amperity qui renvoie une liste de clients. Ce segment doit être associé aux attributs personnalisés que vous souhaitez mettre à jour dans Braze.

{% alert note %}
Consultez la documentation d'Amperity pour des exemples de différents types de segments que vous pourriez vouloir envoyer à Braze.
{% endalert %}

##### Étape 2 : Créer une campagne dans Amperity

1. Allez à la section **campagne** et cliquez sur l'option pour créer une nouvelle campagne.
2. Donnez à votre campagne un nom descriptif et unique qui vous aidera à l'identifier plus tard, surtout si vous avez plusieurs campagnes.
3. Sélectionnez le segment de clients que vous souhaitez cibler avec cette campagne. Cela devrait être le segment que vous avez créé plus tôt. <br>![Champ déroulant des segments à exclure du ciblage.]({% image_buster /assets/img/amperity/select_segments.png %}){: style="max-width:50%;"}<br><br>
4. Choisissez les données que vous souhaitez envoyer dans le cadre de la campagne. Cela peut inclure une gamme d'attributs de client. ![La fenêtre modale/boîte de dialogue de la campagne permet de sélectionner une destination et des attributs personnalisés. ]({% image_buster /assets/img/amperity/edit_campaign_attributes.png %}){: style="max-width:90%;"}<br><br>
5. Sélectionnez **Braze** comme destination où les données de la campagne seront envoyées.
6. Choisissez quand et à quelle fréquence vous souhaitez que la campagne se déroule. Cela peut être un événement unique ou une planification récurrente.
7. Enregistrer votre campagne et exécuter un test pour vous assurer qu'elle fonctionne comme prévu.

##### Étape 3 : Lancer la campagne

Exécutez la campagne pour envoyer le segment à Braze. Cela peut être fait manuellement ou en fonction de la planification que vous avez définie dans les paramètres de la campagne.


### Utilisation d'Amperity avec Braze Currents
Pour envoyer des données Braze Currents dans Amperity :
1. [Configurez un Braze Current]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/) pour envoyer des données dans un bucket Amazon S3.
2. Configurez Amperity pour [lire les fichiers Apache Avro depuis ce compartiment Amazon S3](https://docs.amperity.com/datagrid/source_amazon_s3.html).
3. Configurer les flux et automatiser les chargements de données en utilisant des flux de travail standard.


