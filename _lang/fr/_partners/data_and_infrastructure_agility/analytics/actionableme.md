---
nav_title: actionable.me
article_title: actionable.me
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et actionable.me, un logiciel propriétaire et des processus qui vous aident à tirer immédiatement le meilleur parti de votre investissement Braze."
alias: /partners/actionableme/
page_type: partner
search_tag: Partenaire

---

# actionable.me

> [actionable.me][2], conçu par l'équipe de Massive Rocket, une agence données et CRM, est une approche standardisée et automatisée de l'exécution de programmes CRM, fournissant des outils et des processus conçus pour permettre aux clients de Braze de créer rapidement de la valeur, de manière cohérente et prévisible. 

L’intégration Braze et actionable.me vous permet de déployer un service vous permettant de suivre vos progrès dans l’utilisation de Braze. Grâce à une combinaison d’outils et de processus, ils évalueront rapidement vos performances CRM, identifieront de nouvelles opportunités et fourniront des recommandations sur la façon d’améliorer vos performances.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte actionable.me | Un compte actionable.me est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé API REST Braze avec les autorisations répertoriées dans la section suivante.<br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Pour intégrer Braze et actionable.me, la plateforme actionable.me doit être configurée et une clé API Braze doit être créée dans Braze et être configurée dans le tableau de bord actionable.me.

### Étape 1 : Créez votre clé API Braze

Dans Braze, accédez à la **Developer Console (Console du développeur)** et sélectionnez l'onglet **REST API Keys (Clés API REST)**. Sélectionnez **Create New API Key (Créer une nouvelle clé API)** et assurez-vous que les autorisations suivantes sont ajoutées :

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

### Étape 2 : Fournir des informations à l'équipe actionable.me

Pour terminer l'intégration, vous devez fournir votre clé d'API REST et l'[URL de l’endpoint REST][1] à votre équipe d'exploitation actionable.me. actionable.me établira ensuite la connexion et vous contactera une fois la configuration terminée et vous contactera pour commencer à partager les insights.

![La page actionable.me « add platform » (ajouter une plateforme) que l'équipe d'exploitation actionable.me configurera.][5]

## Résolution des problèmes

Contactez l'équipe actionable.me ou Massive Rocket pour une assistance supplémentaire : [info@massiverocket.com][3]

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://actionable.me
[3]: mailto:info@massiverocket.com
[4]: {% image_buster /assets/img/actionableme/image1.png %}
[5]: {% image_buster /assets/img/actionableme/image2.png %}
