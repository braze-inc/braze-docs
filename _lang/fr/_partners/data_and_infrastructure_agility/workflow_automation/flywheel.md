---
nav_title: Flywheel
article_title: Flywheel
description: "Cet article présente le partenariat entre Braze et Flywheel, une plateforme qui vous permet de segmenter les données client directement depuis l’entrepôt de données et de les envoyer à Braze."
alias: /partners/flywheel/
page_type: partner
search_tag: Partenaire

---

# Flywheel 

> [Flywheel](https://getflywheel.com/) aide les équipes marketing à activer les données client de l’entrepôt de données cloud sur Braze et d’autres canaux. Automatisez, faites évoluer et mesurez les programmes marketing à partir de votre entrepôt de données cloud, en conservant les données dans un emplacement unique et centralisé.

L’intégration de Braze et Flywheel vous permet de segmenter les données client directement à partir de l’entrepôt de données et de les envoyer à Braze, garantissant ainsi que les utilisateurs peuvent optimiser l’ensemble de fonctionnalités approfondies de Braze en tandem avec une source unique de vérité. Rationalisez les efforts marketing pour la segmentation et l’activation des clients, en réduisant le temps nécessaire pour segmenter, lancer, tester et mesurer les résultats des campagnes ciblées envoyées à Braze.

## Conditions préalables 

| Condition | Description |
| ----------- | ----------- |
| Croissance Flywheel ou compte d’entreprise | Un compte Flywheel est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec toutes les autorisations.<br><br>Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | URL de votre endpoint REST. Votre endpoint dépendra de l’URL Braze pour [votre instance][2].|
{: .reset-td-br-1 .reset-td-br-2} 

## Cas d’utilisation

Envoyez des listes de clients depuis votre entrepôt de données vers Braze, en ciblant les campagnes d’e-mail et de notification push en un seul clic, et gardez-les toujours synchronisées.

- E-mails basés sur l’activation de l’inscription : envoyez des e-mails pour aider les utilisateurs qui entrent dans votre flux d’inscription et convertissez-les en utilisateurs actifs.
- E-mails basés sur n’importe quel comportement d’utilisateur : envoyez des e-mails basés sur le comportement de l’utilisateur, tel que « Ajouter au panier »."
- E-mails aux clients qui se désabonnent : réengagez les clients désabonnés par e-mail à l’aide d’une offre.

## Intégration

### Configurer la connexion Braze dans Flywheel

Lorsque vous vous connectez à la plateforme de segmentation dans Flywheel, accédez à l’onglet **Destinations** sur la barre latérale gauche et cliquez sur **New Destination (Nouvelle destination)** dans le coin supérieur droit.

Faites défiler jusqu’à ce que vous trouviez Braze, puis cliquez sur **Add Braze (Ajouter Braze)**.

Une fenêtre contextuelle s’affiche pour configurer la connexion à la destination.

- **Nom de la destination** : C’est ainsi que la destination sera nommée et mentionnée dans l’application à l’avenir
- **Fréquence de synchronisation** : Sélectionnez Quotidien ou Horaire. Elle contrôlera la fréquence à laquelle Flywheel exporte les audiences vers Braze
- **Clé API** : Clé API créée dans les prérequis, avec les autorisations nécessaires
- **URL de l’API** : URL telle que définie dans les prérequis

Cliquez sur **Create (Créer)** pour exporter votre première audience vers Braze ! Pour créer une audience dans Flywheel, consultez [Créer une audience](https://www.flywheelsoftware.com/help-center-articles/create-an-audience).

### Après l’exportation

Une fois votre audience exportée, toutes les 15 minutes, Flywheel générera une version mise à jour de vos listes de clients et l’enverra à Braze.

En même temps, Flywheel supprimera de votre audience les utilisateurs qui n’y sont plus éligibles et lui ajoutera les utilisateurs nouvellement qualifiés. 

Braze fera correspondre les utilisateurs et créera un drapeau, ce qui signifie qu’ils font partie d’une audience Flywheel.

Lorsque vous créez une campagne dans Braze, vous pouvez sélectionner des clients dans cette audience Flywheel. 

## Résolution des problèmes

Contactez l’équipe Flywheel à l’adresse e-mail solutions@flywheelsoftware.com pour plus d’informations ou pour obtenir de l’aide.

[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints