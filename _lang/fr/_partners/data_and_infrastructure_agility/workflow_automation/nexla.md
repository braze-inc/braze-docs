---
nav_title: Nexla
article_title: Nexla
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et Nexla, une plateforme d’opérations de données unifiées qui permet aux utilisateurs de Currents Braze d’extraire, de transformer et de charger des données d’un data lake vers d’autres sites dans un format personnalisé."
alias: /partners/nexla/
page_type: partner
search_tag: Partenaire

---

# Nexla

> [Nexla](https://www.nexla.com) est un leader des opérations de données unifiées qui a été nommé parmi les Gartner Cool Vendors 2021. La plateforme Nexla permet à quiconque de créer des flux de données évolutifs, en fournissant des opérations de données gouvernées, une meilleure collaboration et une plus grande agilité pour les équipes commerciales et de données. Avec Nexla, les équipes travaillant avec des données bénéficient d’une expérience unifiée sans code ou à faible code pour intégrer, transformer, provisionner et surveiller des données pour n’importe quel cas d’utilisation. 

L’intégration de Braze et Nexla permet aux clients qui utilisent [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/) de tirer parti de Nexla pour extraire, transformer et charger des données d’un data lake vers d’autres sites dans un format personnalisé, rendant les données facilement accessibles dans l’ensemble de l’écosystème.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Nexla | Un compte [Nexla][2] est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][1]. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

[Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), le data-as-a-product de Nexla, permet de travailler facilement avec des données de n’importe quel format sans vous soucier des métadonnées. Les outils sans code de Nexla vous permettent de configurer facilement vos flux de données vers ou depuis Braze et les rendent disponibles en quelques minutes. Après avoir défini la destination de votre flux de données, Nexla surveillera le flux et s’adaptera pour prendre en charge n’importe quel volume de données.

## Intégration

### Étape 1 : Créer un compte Nexla

Si vous n’avez pas déjà de compte Nexla, rendez-vous sur le [site Web](https://www.nexla.com) de Nexla pour demander une démonstration et un essai gratuits. Ensuite, accédez à [www.dataops.nexla.io](https://www.dataops.nexla.io) et connectez-vous avec vos nouveaux identifiants.

### Étape 2 : Ajouter votre source

#### Si Braze est votre source de données
1. Dans la plateforme Nexla, accédez à **Flows (Flux) > Create a New Flow (Créer un nouveau flux)** dans la barre d’outils de gauche.
2. Cliquez sur **Create New Source (Créer une nouvelle source)**, sélectionnez le connecteur Braze, puis cliquez sur **Next (Suivant)**. 
3. Sélectionner **Add a New Credential (Ajouter un nouvel identifiant)**, nommez l’identifiant, ajoutez votre clé API et votre endpoint REST Braze, puis cliquez sur **Save (Enregistrer)**.
4. Enfin, sélectionnez vos données et cliquez sur **Save (Enregistrer)**. 

Nexla recherchera la source de toutes les données qu’il trouve et générera un [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) pour transformer les données ou les envoyer à leur destination.

#### Si Braze est votre destination

Consultez la documentation Nexla [Connecter des sources à Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Étape 3 : Transformation (facultatif)

Si vous souhaitez effectuer des [transformations](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) personnalisées sur vos données ou utiliser les connecteurs préconçus de Nexla, cliquez sur le bouton **Transformation** du jeu de données pour accéder au Transform Builder. Vous trouverez des conseils sur l’utilisation du Transform Builder dans la [documentation Nexla](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data).

### Étape 4 : Envoyer des données à une destination

Pour envoyer des données à une destination, cliquez sur la flèche **Send to Destination (Envoyer à la destination)** du jeu de données, et sélectionnez l’un des connecteurs de destination de Nexla ou de Braze si vous avez une source différente. Saisissez vos informations d’identification, configurez les options de destination et cliquez sur **Save (Enregistrer)**. Les données commenceront instantanément à affluer vers la destination de votre choix et au format que vous avez indiqué.

## Comment utiliser cette intégration

Une fois le flux configuré, aucune autre action n’est nécessaire. Nexla traitera les modifications des données sources, prendra en charge toutes les nouvelles données et vous informera de tout changement de schéma ou de toute erreur pour triage. Si vous souhaitez modifier les transformations, la source ou la destination, vous pouvez cliquer sur ces options et effectuer les modifications nécessaires, après quoi Nexla mettra immédiatement le flux à jour.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: https://www.nexla.com/get-demo