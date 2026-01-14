---
nav_title: Datadog
article_title: "Datadog"
description: "Cet article de référence décrit le partenariat avec Braze et Datadog, un service d'observabilité pour les applications à l'échelle du cloud, fournissant une surveillance des serveurs, des bases de données, des outils et des services via une plateforme d'analyse de données basée sur le SaaS."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) est un service d'observabilité pour les applications à l'échelle du cloud, fournissant une surveillance des serveurs, des bases de données, des outils et des services via une plateforme d'analyse de données basée sur le SaaS.

L'intégration de Braze et Datadog permet aux clients de collecter les données de Braze dans Datadog et de créer des alertes sur les données que nous envoyons. Par exemple, configurer un moniteur et une alerte si votre campagne de newsletter hebdomadaire envoie un volume anormalement bas de messages ou si une étape du canvas qui n'envoie habituellement que quelques messages par jour commence à en envoyer des milliers. 

## Conditions préalables 

| Condition | Description |
|---|---|
| Compte Datadog | Un compte Datadog est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Générer la clé Datadog

Dans Datadog, vous devrez créer une [clé API](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). Pour ajouter une clé API, accédez à **Paramètres de l'organisation** > **Clés API** > **Nouvelle clé**.

### Étape 2 : Ajouter une clé à Braze

Dans le tableau de bord de Braze, accédez à **Intégrations de partenaires** > **Partenaires technologiques** puis recherchez **Datadog**. Sur la page partenaire Datadog, fournissez la clé API Datadog. Cela créera une connexion pour permettre à Braze d'envoyer des données à Datadog.

## Événements Braze

Après l'intégration de la connexion, Braze enverra les événements suivants à Datadog :

- `braze.messaging.sent` - Le nombre d'envois

Chacun de ces événements aura des métadonnées sous forme de tags Datadog pour vous donner des informations telles que :

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (si disponible)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (si disponible)

Ces événements et balises peuvent être surveillés dans la page **Indicateurs Explorer** de Datadog. Ces indicateurs sont enregistrés en tant que [distributions](https://docs.datadoghq.com/metrics/distributions/) dans DataDog. Étant donné la nature des indicateurs et l'imprécision des agrégations et des rollups de DataDog, Braze ne réessaie pas les erreurs réseau intermittentes ou d'autres erreurs de l'API DataDog qui peuvent être rencontrées lors de la transmission. Cela signifie que ces décomptes de métriques peuvent différer légèrement des décomptes observés dans le tableau de bord de Braze et/ou via Currents.

![]({% image_buster /assets/img/datadog.png %})

