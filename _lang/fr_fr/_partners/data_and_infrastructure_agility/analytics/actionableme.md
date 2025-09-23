---
nav_title: actionable.me
article_title: actionable.me
description: "Cet article de référence présente le partenariat entre Braze et actionable.me, un logiciel et des processus propriétaires, qui vous permettent de tirer immédiatement le meilleur parti de votre investissement dans Braze."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me][2], créé par l'équipe de Massive Rocket, une agence de données et de CRM, est une approche standardisée et automatisée de l'exécution des programmes de CRM, fournissant des outils et des processus conçus pour que les clients de Braze obtiennent de la valeur rapidement, de manière cohérente et prédictive. 

_Cette intégration est maintenue par actionable.me._

## À propos de l'intégration

L'intégration de Braze et de actionable.me vous permet de déployer un service pour suivre vos progrès dans l'utilisation de Braze. Grâce à une combinaison d'outils et de processus, ils évalueront rapidement les performances de votre CRM, identifieront de nouvelles opportunités et fourniront des recommandations sur la manière d'être plus performant.

## Prérequis

| Condition | Description |
| --- | --- |
| actionable.me compte | Un compte actionable.me est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations énumérées dans la section suivante.<br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Pour intégrer Braze et actionable.me, la plateforme actionable.me doit être configurée et une clé API Braze doit être créée dans Braze et configurée dans le tableau de bord actionable.me.

### Étape 1 : Créez votre clé API Braze

Dans Braze, accédez à **Paramètres** > **Clés API**. Sélectionnez **Créer une nouvelle clé API** et assurez-vous que les autorisations suivantes sont ajoutées :

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### Étape 2 : Fournissez des informations à l'équipe actionable.me

Pour terminer l'intégration, vous devez fournir votre clé API REST et l'[URL de l'endpoint REST][1] à votre équipe d'exploitation actionable.me. actionable.me établira alors la connexion et vous contactera une fois la configuration terminée pour commencer à partager des informations.

![La page "ajouter une plateforme" actionable.me que l'équipe actionable.me configurera.][5]

## Résolution des problèmes

Contactez l'équipe actionable.me ou Massive Rocket pour obtenir une aide supplémentaire : [info@massiverocket.com][3]


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://actionable.me
[3]: mailto:info@massiverocket.com
[4]: {% image_buster /assets/img/actionableme/image1.png %}
[5]: {% image_buster /assets/img/actionableme/image2.png %}
