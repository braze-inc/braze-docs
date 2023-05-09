---
nav_title: Datadog
article_title: "Datadog"
description: "Cet article de référence présente le partenariat entre Braze et DataDog, un service d’observabilité pour les applications cloud permettant de surveiller des serveurs, des bases de données, des outils et des servies à l’aide d’une plateforme d'analyses de données en SaaS."
alias: /partners/datadog/
page_type: partner
search_tag: Partenaire


---

# Datadog

> [Datadog](https://www.datadoghq.com/) est un service d’observabilité pour les applications cloud permettant de surveiller des serveurs, des bases de données, des outils et des servies à l’aide d’une plateforme d'analyses de données en SaaS.

L’intégration entre Braze et Datadog permet aux clients de collecter des données Braze dans Datadog et de créer des alertes sur les données envoyées. Par exemple, configurer un moniteur et vous alerter si votre campagne de newsletter hebdomadaire envoie une quantité de messages anormalement basse, ou si un Canvas step envoyant habituellement quelques messages seulement en envoie soudainement des milliers. 

## Conditions préalables 

| Condition | Description |
|---|---|
| Compte Datadog | Un compte Datadog est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Générer une clé Datadog

Dans Datadog, vous devrez créer une [clé API](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). Pour ajouter une clé API, accédez à **Organization Settings (Paramètres de l’organisation)** > **API Keys (Clés API)** > **New Key (Nouvelle clé)**.

### Étape 2 : Ajouter la clé à Braze

Sur le tableau de bord de Braze, accédez à **Technology Partners (Partenaires technologiques)** puis recherchez **Datadog**. Sur la page partenaire de Datadog, fournissez la clé API Datadog. Une connexion permettant l’envoi de données Braze à Datadog sera alors crée.

Si vous êtes hébergé sur les sites Datadog EU1 ou US1-FED, veuillez contacter l’assistance pour que votre intégration Datadog soit configurée pour envoyer des indicateurs à ces sites, sinon l’intégration ne fonctionnera pas.

## Événements Braze

Une fois la connexion intégrée, Braze enverra les événements suivants à Datadog :

- `braze.messaging.sent` - Le nombre d’envois

Chacun de ces événements contiendra des métadonnées prenant la forme de balises Datadog pour transmettre des informations comme :

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (si disponible)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (si disponible)

Ces événements et ces balises peuvent être suivis sur la page **Metrics Explorer (Exploreur d’indicateurs)** de Datadog. Ces indicateurs sont consignés sur Datadog en tant que [distributions](https://docs.datadoghq.com/metrics/distributions/). Compte tenu de la nature des indicateurs et de l’imprécision des agrégations et des synthèses de DataDog, Braze ne tente pas de résoudre les erreurs de réseau intermittentes ou les autres erreurs d’API DataDog pouvant être rencontrées lors de la transmission. Cela signifie que ces nombres d’indicateurs peut être légèrement différents des nombres vus sur le tableau de bord de Braze et/ou via les Currents.

![][1]

[1]: {% image_buster /assets/img/datadog.png %}
