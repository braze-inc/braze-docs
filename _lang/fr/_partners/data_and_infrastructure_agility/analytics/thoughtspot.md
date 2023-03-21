---
nav_title: ThoughtSpot
article_title: ThoughtSpot
description: "Cet article de référence décrit le partenariat entre Braze et ThoughtSpot, une plateforme d’analyse de nouvelle génération qui permet aux utilisateurs de rechercher sans limite leurs données d’interaction Braze et de découvrir des Insights exploitables."
alias: /partners/thoughtspot/
page_type: partner
search_tag: Partenaire

---

# ThoughtSpot

> ThoughtSpot est le nuage analytique moderne, une plateforme d’analyses de nouvelle génération qui fournit des analyses en direct à votre pile de données moderne - permettant à vos collègues, partenaires et clients de transformer les données en insights exploitables.

L'intégration de Braze et de ThoughtSpot s'appuie sur les ThoughtSpot TML Blocks qui permettent aux utilisateurs de Braze d'accélérer leurs analyses du comportement des utilisateurs grâce à des modèles préétablis de feuilles de travail et de modèles. Cette intégration permet aux utilisateurs d'effectuer des recherches illimitées dans leurs données d'interaction Braze et de découvrir des insights exploitables. 

## Conditions préalables

Pour commencer à utiliser ThoughtSpot sur Braze, vos données doivent être envoyées à un entrepôt de données sur cloud avant que ThoughtSpot puisse les interroger en direct.

| Condition | Description |
| ----------- | ----------- |
| Compte ThoughtSpot | Un compte ThoughtSpot est requis pour profiter de ce partenariat. |
| Entrepôt de données sur cloud| Les données de Braze sont stockées dans un entrepôt de données sur cloud à l'aide de Currents Braze. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Blocs TML

Les utilisateurs de Braze peuvent facilement accéder et rechercher toutes leurs données d'interaction numérique. Nos modèles permettent aux utilisateurs de mettre rapidement en place leurs analyses grâce à des visualisations et des feuilles de travail préétablies. Analysez l'acquisition et le comportement des utilisateurs de votre site Web grâce aux recherches, aux analyses approfondies et à spotIQ.

## Intégration

### Étape 1 : Connecter ThoughtSpot 

Connectez-vous à votre instance ThoughtSpot et créez une connexion Embrace à chaque tableau importé depuis Braze en utilisant Currents Braze.

#### Étape 2 : Importer TML

Importez le fichier zippé des feuilles de travail et des tableaux interactifs dans Thoughtspot et vérifiez qu'ils ont été importés sans erreur. 

Une fois importé, vous pouvez commencer à rechercher et à personnaliser les tableaux interactifs. 

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints