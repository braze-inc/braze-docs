---
nav_title: Tellius
article_title: Tellius
alias: /partners/Tellius/
description: "Cet article de référence décrit le partenariat entre Braze et Tellius, une plateforme d’intelligence décisionnelle et d’analyses augmentée, vous permettant d’exploiter les données, sans avoir à dépendre des ingénieurs BI, pour créer des tableaux de bord et générer des informations afin de prendre de meilleures décisions marketing."
page_type: partner
search_tag: Partenaire

---

# Tellius

> [Tellius](https://www.tellius.com/), une plateforme d'intelligence décisionnelle et d'analyse augmentée, vous permet de répondre à des questions ponctuelles sur vos données à l'aide d'une recherche en langage naturel et d'aller plus loin pour comprendre le "pourquoi" grâce à des insights guidés par l'IA.

L'intégration de Braze et de Tellius permet aux utilisateurs d'exploiter les données, sans avoir recours à des ingénieurs BI, pour créer des tableaux de bord et générer des insights afin de prendre de meilleures décisions marketing. Cette intégration nécessite que les données Braze soient stockées dans Snowflake, où Tellius peut se connecter directement et d’appuyer des requêtes avec une intégration en mode direct.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Tellius | Un compte Tellius est nécessaire pour tirer parti de ce partenariat. Vous pouvez commencer votre parcours avec Tellius par un [essai gratuit](https://www.tellius.com/free-trial/)|
| Programme de partage de données Snowflake | Pour les clients actuels de Snowflake, contactez votre conseiller Braze au sujet du programme de partage de données Snowflake afin d'intégrer vos données Braze dans votre instance Snowflake.|
| Compte Snowflake Reader | Si vous n'êtes pas un client Snowflake, contactez votre conseiller Braze pour obtenir un compte Snowflake Reader qui vous permettra d'accéder à vos données Braze.|
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Obtenir l'accès à Braze via Snowflake

Braze stocke les données granulaires des clients dans Snowflake. Vous pouvez exploiter vos données Braze pour générer des insights grâce au programme de partage de données Snowflake de Braze ou en obtenant un compte de lecteur Snowflake. 

Suivez [l'intégration de Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) pour le paramétrage. 

### Étape 2 : Connecter Tellius aux données de Braze dans Snowflake

Connectez Tellius aux données Braze dans Snowflake via l'une des méthodes suivantes :

- Accès direct : Pour charger des données dans Tellius, suivez les étapes pour [Load datasets (Charger des ensembles de données)](https://help.tellius.com/article/jn6o59d5gk-load-datasets).
- Accès OAuth : Pour un accès OAuth à Snowflake, suivez les étapes [OAuth authentication (authentification OAuth)](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake).

### Étape 3 : Créer une Business View dans Tellius à partir de données chargées

Pour commencer à utiliser la recherche en langage naturel et les insights automatisés, créez une [Business View](https://help.tellius.com/article/hy9yvh5tom-create-business-view) et sélectionnez des ensembles de données à partir de votre connexion Snowflake.

### Étape 4 : Tirez le meilleur parti de vos données grâce à Tellius

Dans Tellius, une interface guidée vous permet de découvrir les fonctionnalités de la plateforme. Pour des questions supplémentaires et des instructions, consultez leur [base de connaissances](https://help.tellius.com/) complète.