---
nav_title: ActionIQ
article_title: ActionIQ
description: "Cet article de référence présente l’intégration de Braze et d’ActionIQ. ActionIQ est une plateforme de données client d’entreprise pour les spécialistes du marketing, les analystes et les technologues. Cette intégration permet aux marques de synchroniser et de mapper leurs données ActionIQ directement dans Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ

---

# ActionIQ

> [ActionIQ][2] apporte la commande au chaos de l’expérience client. Le hub d’expérience client (CX) ActionIQ offre à toutes les équipes un accès direct mais contrôlé en libre-service aux données client pour découvrir des audiences et orchestrer des expériences à grande échelle.

L’intégration de Braze et ActionIQ permet aux marques de synchroniser et de mapper leurs données ActionIQ directement dans Braze, ce qui permet de fournir des expériences client extraordinaires basées sur l’ensemble de leurs données client. L’intégration permet aux utilisateurs de :
- Mapper des segments d’audience ou des attributs personnalisés dans Braze directement à partir d’ActionIQ
- Transmettre les événements suivis par ActionIQ vers Braze en temps réel pour déclencher des campagnes personnalisées et ciblées

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte ActionIQ | Un compte ActionIQ est requis pour profiter de cette intégration. |
| Clé d’API REST Braze | Une clé API REST Braze avec des autorisations `users.track` et `user.export.ids`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Appartenance à une audience

Cette intégration est utilisée pour synchroniser l’appartenance à l’audience ActionIQ avec Braze en créant des attributs personnalisés qui indiquent si un profil Braze fait partie d’un segment. Chaque audience ActionIQ correspond à un attribut personnalisé booléen unique.

La convention de dénomination standard pour l’attribut personnalisé créé est : `AIQ_<Audience ID>_<Split ID>`.

Pour créer un segment avec ces utilisateurs, dans Braze accédez à **Segments**, créez un nouveau segment et choisissez **Custom Attributes (Attributs personnalisés)** comme filtre. À partir de là, vous pouvez choisir l'attribut personnalisé ActionIQ. Une fois créé, vous pouvez sélectionner votre segment comme filtre d’audience au moment de créer une campagne ou un Canvas.

#### Conditions

Dans ActionIQ, configurez une connexion Braze en fournissant votre clé API REST et votre endpoint REST de Braze. 

Pour faire correspondre les consommateurs de la plateforme Braze, les identifiants suivants doivent être inclus dans votre paramètre d’activation :
- `braze_id`
- `external_id`

Une fois votre intégration connectée, les informations commenceront à être envoyées à Braze.

### Événements

La plateforme ActionIQ peut être configurée pour recevoir des informations sur les événements à l’aide de son service d’ingestion en continu. Cette autre option d’intégration transmet ces événements à Braze pour que les marketeurs les utilisent pour orchestrer ou déclencher des campagnes marketing.

L’intégration d’événements peut envoyer des attributs ActionIQ supplémentaires dans le cadre des propriétés de la charge utile de l’événement.

#### Conditions

L’intégration des événements envoie les informations suivantes à Braze :
- Nom de l’événement
- Identifiant du consommateur (soit le `braze_id`, soit l’`external_id`)
- Horodatage
- Propriétés de l’événement, renseignées par des attributs supplémentaires dans le paramètre d’exportation


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/