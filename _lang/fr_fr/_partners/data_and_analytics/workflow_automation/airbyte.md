---
nav_title: Airbyte
article_title: Airbyte
description: "Cet article de référence couvre l'intégration de Braze et Airbyte. Airbyte est un moteur d'intégration de données open-source qui vous aide à consolider vos données dans vos entrepôts de données, lacs et bases de données, en transférant des événements en temps réel d'Airbyte à Braze."
alias: /partners/airbyte/
page_type: partner
search_tag: Airbyte

---

# Airbyte

> [Airbyte](https://airbyte.com/) est un moteur d'intégration de données open-source qui vous aide à consolider vos données dans vos entrepôts, lacs et bases de données.

_Cette intégration est maintenue par Airbyte._

## À propos de l'intégration

L'intégration de Braze et Airbyte permet aux utilisateurs de créer un pipeline de données pour collecter et analyser les données de Braze en connectant toutes vos applications et bases de données à un entrepôt central. Une fois les données collectées dans l'entrepôt central, les équipes chargées des données peuvent explorer efficacement les données de Braze à l'aide de leurs outils d'aide à la décision préférés.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| compte Airbyte Cloud | Un compte [Airbyte Cloud](https://cloud.airbyte.io/workspaces) est requis pour profiter de cette intégration. |
| Clé d'API REST Braze | Une clé API REST Braze avec toutes les permissions. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze | Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

1. Dans votre compte Airbyte Cloud, accédez à **Sources > + Nouvelle source > Configurer la source**.
2. Entrez "Braze" comme nom de source et sélectionnez **Braze** dans le menu déroulant de la source.
3. Spécifiez l’URL de l'endpoint, la clé API REST Braze et la date de début. Cliquez sur **Configurer la source**.

### Modes de synchronisation pris en charge

Le connecteur de source Braze d'Airbyte prend en charge les [modes de synchronisation](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes) suivants :
- **Actualisation complète | Remplacer** : synchroniser tous les enregistrements de la source et remplacer les données dans la destination en les écrasant.
- **Synchronisation incrémentielle | Ajouter**: Synchroniser les nouveaux enregistrements de la source et les ajouter à la destination sans supprimer aucune donnée.

### Flux pris en charge

- [`campaigns`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18)
- [`campaigns_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1)
- [`canvases`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1)
- [`canvases_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73)
- [`events`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1)
- [`events_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c)
- [`kpi_daily_new_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01)
- [`kpi_daily_active_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986)
- [`kpi_daily_app_uninstalls`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae)
- [`cards`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e)
- [`cards_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8)
- [`segments`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f)
- [`segments_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e)

{% alert note %}
Les limites de débit varient selon le flux. Visitez le [tableau des limites de taux]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type) pour plus d'informations.
{% endalert %}
