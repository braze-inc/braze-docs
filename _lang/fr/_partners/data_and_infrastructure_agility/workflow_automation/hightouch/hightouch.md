---
nav_title: Hightouch
article_title: Hightouch
description: "Cet article de référence présente le partenariat entre Braze et Hightouch, une plateforme qui vous permet de synchroniser les données client stockées dans votre entrepôt avec des outils métier."
page_type: partner
search_tag: Partenaire

---

# Hightouch

> [Hightouch][1] est une plateforme d’intégration de données moderne qui vous permet de synchroniser les données client, produit ou propriétaire stockées dans votre entrepôt ou votre data lake avec n’importe quelle application, et sans l’aide de vos équipes informatiques ou techniques.

L’intégration de Braze et de Hightouch vous permet de créer de meilleures campagnes Braze en utilisant les données client actualisées de votre entrepôt de données. En synchronisant automatiquement vos données client avec Braze, vous n’aurez plus à vous soucier de la cohérence des données et vous gagnerez un temps précieux pour créer des expériences client de premier plan. 

Cette intégration vous permet également d’[importer des cohortes d’utilisateurs dans Braze](#data-import-integration), en envoyant des campagnes ciblées basées sur des données qui n’existent peut-être que dans votre entrepôt.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Hightouch | Un compte Hightouch est requis pour profiter de ce partenariat.
| Clé d’API REST Braze | Une clé API REST Braze avec des autorisations `users.track` et `users.export.ids`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][2].<br><br>Hightouch doit connaître le nom du cluster sur lequel se trouve votre instance Braze. Par exemple, si votre endpoint Braze est `https://rest.iad-01.braze.com`, vous avez uniquement besoin de `iad-01`.|
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

* Synchroniser les données sur vos utilisateurs et comptes avec Braze pour créer des campagnes hyper-personnalisées.
* Mettre automatiquement à jour vos segments Braze avec les données les plus récentes de votre entrepôt.
* Offrir de meilleures expériences en transférant dans Braze des données issues d’autres points de contact client.
* Importer des cohortes d’utilisateurs dans Braze pour envoyer des campagnes et des Canvas ciblés. 

## Intégration

### Étape 1 : Créer votre destination Braze dans Hightouch

1. Sur la plateforme Hightouch, dans la section **Destinations** cliquez sur **Add destination (Ajouter une destination)**.
2. Sélectionnez **Braze** dans la liste des destinations disponibles.
3. Fournissez votre endpoint REST Braze (sans « https://rest. ») et votre clé API REST Braze.<br><br>![][3]

### Étape 2 : Synchronisation des objets et des événements

Hightouch prend en charge la synchronisation des objets et des événements utilisateur.

| Destination | Description | Modes pris en charge |
|---|---|---|
| Objet | Synchronise les enregistrements vers des objets, tels que des utilisateurs ou des organisations, dans votre destination.| Mettre à jour ou mettre à jour et insérer |
| Événements | Synchronise les enregistrements en tant qu’événements sur votre destination (souvent sous la forme d’un appel de suivi). | Suivre un événement ou suivre un achat |

{% alert note %}
Reportez-vous à [Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption) pour plus d'informations sur la façon dont les synchronisations affectent votre consommation de points de données Braze.
{% endalert %}

#### Synchroniser des objets Braze

Vous pouvez synchroniser des objets Hightouch (champs utilisateur) aux champs par défaut ou personnalisés équivalents de Braze. Vous pouvez également mettre en correspondance des enregistrements pour unifier les données sur les deux plateformes.

#### Synchroniser des événements Braze

Hightouch vous permet de suivre les données d’événement et d’achat et de les synchroniser sur Braze. Plusieurs options peuvent être définies dans Hightouch pour modifier le comportement de synchronisation, comme configurer des données de suivi et définir un comportement utilisateur inexistant.

{% alert important %}
Vous trouverez des instructions supplémentaires sur la synchronisation des objets et des événements dans la [documentation Hightouch](https://hightouch.io/docs/destinations/braze/).
{% endalert %}

## Intégration de l’importation de données

### Étape 1 : Obtenir la clé d’importation des données Braze
Dans Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **Hightouch**. Ici, vous trouverez votre endpoint REST et pourrez générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante.<br><br>![][6]{: style="max-width:90%;"} 

### Étape 2 : Ajouter des cohortes Braze comme destination dans Hightouch
Accédez à la page **Destination** de votre espace de travail Hightouch, recherchez **Braze Cohorts**, et cliquez sur **Continue (Continuer)**. À partir de là, prenez votre endpoint REST et votre clé d’importation des données, puis cliquez sur **Continue (Continuer)**.<br><br>![][7]{: style="max-width:90%;"}

### Étape 3 : Synchroniser un modèle (ou une audience) dans des cohortes Braze
Dans Hightouch, créez une nouvelle synchronisation en utilisant votre [modèle](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) ou l’[audience](https://hightouch.io/docs/audiences/usage/) que vous avez créé. Ensuite, sélectionnez la destination de la cohorte Braze que vous avez créée à l’étape précédente. Enfin, dans la configuration de destination Braze Cohorts, sélectionnez l’identifiant que vous souhaitez associer et décidez si vous souhaitez que Hightouch crée une nouvelle cohorte Braze ou qu’il mette à jour une cohorte existante.<br><br>![][8]{: style="max-width:90%;"}

### Étape 4 : Créer un segment Braze à partir d’une audience Hightouch personnalisée
Dans Braze, accédez à **Segments**, créez un nouveau segment, puis sélectionnez **Hightouch Cohorts (Cohortes Hightouch)** comme filtre. À partir de là, vous pouvez choisir la cohorte Hightouch que vous souhaitez inclure. Une fois créé, vous pourrez sélectionner votre segment de cohorte Hightouch comme filtre d’audience au moment de créer une campagne ou un Canvas.<br><br>![][9]{: style="max-width:90%;"}

### Comment utiliser cette intégration
Pour utiliser votre segment Hightouch, créez une campagne Braze ou Canvas et sélectionnez le segment comme audience cible.<br><br>![][10]{: style="max-width:90%;"}

## Démo de l’intégration

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

[1]: https://hightouch.io
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: {% image_buster /assets/img/hightouch/hightouch_braze_setup.png %}
[4]: https://hightouch.io/docs/destinations/braze/
[6]: {% image_buster /assets/img/hightouch/data_import_key.png %} 
[7]: {% image_buster /assets/img/hightouch/cohort1.png %} 
[8]: {% image_buster /assets/img/hightouch/cohort2.png %}  
[9]: {% image_buster /assets/img/hightouch/cohort3.png %}  
[10]: {% image_buster /assets/img/hightouch/cohort4.png %}  
