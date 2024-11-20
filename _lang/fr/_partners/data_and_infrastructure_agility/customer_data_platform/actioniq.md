---
nav_title: ActionIQ
article_title: ActionIQ
description: "Cet article de référence couvre l'intégration de Braze et d'ActionIQ. ActionIQ est une plateforme de données clients d'entreprise pour les marketeurs, les analystes et les technologues. Cette intégration permet aux marques de synchroniser et de mapper leurs données ActionIQ directement sur Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ][2] met de l'ordre dans le chaos de l'expérience client. Le Customer Experience (CX) Hub d'ActionIQ donne à toutes les équipes un accès direct mais contrôlé en libre-service aux données des clients pour découvrir des audiences et orchestrer des expériences à grande échelle.

L'intégration de Braze et d'ActionIQ permet aux marques de synchroniser et de mapper leurs données ActionIQ directement sur Braze, ce qui favorise l’offre d'expériences clients extraordinaires basées sur l'ensemble de leurs données clients. L'intégration permet aux utilisateurs de :
- Mappez des segments d'audience ou des attributs personnalisés à Braze directement à partir d'ActionIQ.
- Transmettre les événements suivis par ActionIQ à Braze en temps réel pour déclencher des campagnes personnalisées et ciblées.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte ActionIQ | Un compte ActionIQ est nécessaire pour profiter de cette intégration. |
| Clé API REST de Braze | Une clé d’API REST de Braze avec les autorisations `users.track` et `user.export.ids`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Membres de l'audience

Cette intégration permet de synchroniser l'appartenance de l'audience ActionIQ avec Braze en créant des attributs personnalisés qui indiquent si un profil Braze fait partie d'une segmentation. Chaque audience ActionIQ correspond à un attribut personnalisé booléen unique.

La convention de déignation standard pour l'attribut personnalisé créé est la suivante : `AIQ_<Audience ID>_<Split ID>`.

Pour créer un segment de ces utilisateurs, dans Braze, naviguez vers **Segments**, créez un nouveau segment et sélectionnez **Attributs personnalisés** comme filtre. À partir de là, vous pouvez choisir l'attribut personnalisé ActionIQ. Une fois le segment créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

#### Exigences

Dans ActionIQ, établissez une connexion avec Braze en fournissant votre clé d’API REST et l’endpoint REST de Braze. 

Pour correspondre aux consommateurs de la plateforme Braze, les identifiants suivants doivent être inclus dans votre paramètre d'activation :
- `braze_id`
- `external_id`

Une fois votre intégration connectée, les informations commenceront à être envoyées à Braze.

### Evénements

La plateforme ActionIQ peut être configurée pour recevoir des informations sur les événements par l'intermédiaire de son service d'ingestion de flux. Cette autre option d'intégration transmet ces événements à Braze, afin que les marketeurs puissent les utiliser pour l'orchestration ou le déclenchement de campagnes marketing.

L'intégration de l'événement peut envoyer des attributs ActionIQ supplémentaires dans le cadre des propriétés de la charge utile de l'événement.

#### Exigences

L'intégration des événements envoie les informations suivantes à Braze :
- Nom de l'événement
- Identifiant du consommateur (soit `braze_id` ou `external_id`)
- Horodatage
- Propriétés d'événement, qui sont complétées par tout attribut supplémentaire dans le paramètre d'exportation


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/