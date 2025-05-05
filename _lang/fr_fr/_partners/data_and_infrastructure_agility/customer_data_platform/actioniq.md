---
nav_title: ActionIQ
article_title: ActionIQ
description: "Cet article de référence couvre l'intégration de Braze et d'ActionIQ. ActionIQ est une plateforme de données client d'entreprise pour les marketeurs, les analystes et les technologues. Cette intégration permet aux marques de synchroniser et de mapper leurs données ActionIQ directement sur Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ][2] est une plateforme de données client pour les marques d'entreprise qui donne aux marketeurs des moyens faciles et sécurisés d'activer les données n'importe où dans l'expérience client. Grâce à l'architecture composable unique d'ActionIQ, les données peuvent rester en toute sécurité là où elles se trouvent, et les équipes marketing n'utilisent que les outils dont elles ont besoin.

_Cette intégration est maintenue par ActionIQ._

## À propos de l'intégration

L'intégration de Braze et d'ActionIQ permet aux marques de synchroniser et de mapper leurs données ActionIQ directement sur Braze, ce qui favorise la réception/distribution d'expériences clients extraordinaires basées sur l'ensemble de leurs données clients. Les intégrations disponibles permettent aux utilisateurs de :

- Mettez à jour les profils utilisateurs dans Braze avec les informations sur l'appartenance à l'audience et tous les attributs directement à partir d'ActionIQ.
- Transmettre les événements suivis par ActionIQ à Braze en temps réel pour déclencher des campagnes personnalisées et ciblées.
- Diffusez des campagnes déclenchées par l'API dans Braze directement à partir des points de contact d'un parcours ActionIQ.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte ActionIQ | Un compte ActionIQ est nécessaire pour profiter de cette intégration. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations requises pour l'intégration concernée. Pour plus de détails, voir la section "Exigences". <br><br>Cette clé peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API.** |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Membres de l'audience

Cette intégration permet de synchroniser l'appartenance de l'audience ActionIQ avec Braze en créant des attributs personnalisés qui indiquent si un profil Braze fait partie d'une segmentation. Chaque audience ActionIQ correspond à un attribut personnalisé booléen unique.

La convention de déignation standard pour l'attribut personnalisé créé est la suivante : `AIQ_<Audience ID>_<Split ID>`.

Pour créer une segmentation de ces utilisateurs, procédez comme suit :
1. Dans Braze, accédez à **Segments**.
2. Créer une nouvelle segmentation.
3. Sélectionnez **Attributs personnalisés** comme filtre.
4. Choisissez ensuite l'attribut personnalisé ActionIQ. 
5. Une fois le segment créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

En outre, cette intégration mettra à jour tout attribut personnalisé ou standard dans un profil utilisateur Braze avec leurs valeurs d'attribut ActionIQ.

#### Exigences

Une clé API REST Braze avec les autorisations `users.track` et `user.export.ids` est nécessaire. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. 

Dans ActionIQ, établissez une connexion avec Braze en fournissant votre clé d’API REST et l’endpoint REST de Braze. 

Pour correspondre aux consommateurs de la plateforme Braze, les identifiants suivants doivent être inclus dans votre paramètre d'activation :
- `braze_id`
- `external_id`

### Evénements

Vous pouvez configurer la plateforme ActionIQ pour qu'elle reçoive des informations sur les événements par l'intermédiaire de son service d'ingestion de flux. Cette option d'intégration transmet ces événements à Braze pour que les marketeurs puissent les utiliser à des fins d'orchestration ou pour déclencher des campagnes marketing. L'intégration des événements peut envoyer des attributs ActionIQ supplémentaires dans le cadre des propriétés de la charge utile de l'événement.

#### Exigences

Une clé API REST Braze avec les autorisations `users.track` et `user.export.ids` est nécessaire. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. 

L'intégration des événements envoie les informations suivantes à Braze :
- Nom de l'événement
- Identifiant du consommateur (soit `braze_id` ou `external_id`)
- Horodatage
- Propriétés d'événement, qui sont complétées par tout attribut supplémentaire dans le paramètre d'exportation

### Campagnes déclenchées

Cette intégration déclenchera une campagne dans Braze pour tous les utilisateurs d'un segment ActionIQ. Après avoir configuré le texte de votre campagne, les tests multivariés et les règles de rééligibilité, vous pouvez la déclencher à partir de n'importe quel point de contact du parcours ActionIQ en ajoutant l'ID de la campagne Braze à vos paramètres d'exportation.

En option, vous pouvez inclure d'autres attributs ActionIQ dans votre exportation afin d'alimenter le texte de votre campagne. Ceux-ci sont envoyés avec l'objet `trigger_properties`.

#### Exigences

Une clé API REST Braze avec les autorisations `campaigns.trigger.send` et `campaigns.list` est nécessaire. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**.

Les valeurs suivantes doivent être envoyées dans votre exportation ActionIQ vers Braze :
- Identifiant du consommateur (soit `braze_id` ou `external_id`)
- ID de campagne


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/