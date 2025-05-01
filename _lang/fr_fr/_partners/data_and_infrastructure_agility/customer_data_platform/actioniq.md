---
nav_title: ActionIQ
article_title: ActionIQ
description: "Cet article de référence couvre l'intégration de Braze et d'ActionIQ.  Cette intégration permet aux marques de synchroniser et de mapper leurs données ActionIQ directement sur Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

>  



## À propos de l'intégration

 

- 
- Transmettre les événements suivis par ActionIQ à Braze en temps réel pour déclencher des campagnes personnalisées et ciblées.
- 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte ActionIQ | Un compte ActionIQ est nécessaire pour profiter de cette intégration. |
| Clé API REST de Braze |   <br><br> |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Membres de l'audience

Cette intégration permet de synchroniser l'appartenance de l'audience ActionIQ avec Braze en créant des attributs personnalisés qui indiquent si un profil Braze fait partie d'une segmentation. Chaque audience ActionIQ correspond à un attribut personnalisé booléen unique.

La convention de déignation standard pour l'attribut personnalisé créé est la suivante : `AIQ_<Audience ID>_<Split ID>`.


1. 
2. 
3. 
4.  
5. Une fois le segment créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.



#### Exigences

 Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. 

Dans ActionIQ, établissez une connexion avec Braze en fournissant votre clé d’API REST et l’endpoint REST de Braze. 

Pour correspondre aux consommateurs de la plateforme Braze, les identifiants suivants doivent être inclus dans votre paramètre d'activation :
- `braze_id`
- `external_id`

### Evénements

  

#### Exigences

 Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. 

L'intégration des événements envoie les informations suivantes à Braze :
- Nom de l'événement
- Identifiant du consommateur (soit `braze_id` ou `external_id`)
- Horodatage
- Propriétés d'événement, qui sont complétées par tout attribut supplémentaire dans le paramètre d'exportation

### Campagnes déclenchées

 

 

#### Exigences

 Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**.


- Identifiant du consommateur (soit `braze_id` ou `external_id`)
- ID de campagne


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/