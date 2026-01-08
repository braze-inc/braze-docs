---
nav_title: "Règles d'envoi des messages"
article_title: "Règles d'envoi des messages"
page_order: 1
page_type: reference
description: "Cette page explique comment utiliser les règles d'envoi de messages dans le flux de travail d'approbation pour les campagnes et les canevas avec un volume d'envoi important."
---

# Règles d'envoi des messages

> Utilisez des règles d'envoi de messages dans votre flux de travail d'approbation pour limiter le nombre d'utilisateurs atteignables avant qu'une approbation supplémentaire ne soit requise. De cette façon, vous pouvez revoir vos campagnes et vos canevas avant de cibler un public plus large.

## Comment cela fonctionne-t-il ?

Les règles d'envoi des messages s'appliquent à un espace de travail et sont constituées d'un type de message et d'un nombre maximum d'utilisateurs joignables.

- **Type de message :** Définit le type de message auquel la règle sera appliquée : campagne, Canvas, ou à la fois Canvas et campagnes.
- **Nombre maximum d'utilisateurs joignables :** Détermine la taille de l'audience qui nécessitera une approbation supplémentaire.

### Types d'envois de messages partagés et nombre maximal d'utilisateurs atteignables

Deux règles peuvent exister avec le même nombre d'utilisateurs joignables pour le même type de message. Par exemple, vous pouvez définir un maximum de 10 000 utilisateurs pour Canvas et de 10 000 utilisateurs pour Canvas et les campagnes. 

### Séparer les approbateurs

Deux règles peuvent partager le même maximum d'utilisateurs, ce qui vous permet d'organiser et de séparer vos règles par approbateur. Par exemple, vous créez les deux règles suivantes :

- Règle A pour les Canvas ayant un maximum de 100 000 utilisateurs avec des approbateurs au sein de votre équipe juridique.
- Règle B pour les Canvas ayant un maximum de 100 000 utilisateurs avec des approbateurs au sein de votre équipe de marketeurs. 

### Pas de chevauchement des utilisateurs joignables

Vous ne pouvez pas définir de règles avec un nombre d'utilisateurs qui se chevauchent pour le même type de message. Par exemple, la règle d'envoi de messages suivante **ne peut pas** être définie : 

- Règle C pour les canvas avec un maximum de 10 000 utilisateurs 
- Règle D pour les canvas avec un maximum de 1 000 000 d'utilisateurs

## Création d'une règle d'envoi des messages

### Conditions préalables

Seuls les administrateurs de Braze peuvent définir des règles de messages, mais tout utilisateur de Braze peut approuver des règles de messages (y compris les utilisateurs ne disposant pas d'autorisations générales d'approbation).

### Étape 1 : Ajouter une règle

{% alert note %}
Vous pouvez créer jusqu'à cinq règles d'envoi de messages.
{% endalert %}

1. Allez dans **Réglages** > **Workflow d'approbation** > **Règles d'envoi de messages.**
2. Sélectionnez **Créer une règle**.
3. Donnez un nom à cette règle (par exemple, "Tous les abonnements d'utilisateurs").
4. Pour le **type de message**, sélectionnez **Campagne**, **Canvas** **ou à la fois Canvas et Campagnes** pour appliquer la règle d'approbation.
5. Entrez un nombre pour le **nombre maximum d'utilisateurs joignables**. Pour plus d'informations, reportez-vous aux [statistiques d'audience]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Sélectionnez **Enregistrer**.

\![Exemple de règle d'envoi de messages "Règle 1" pour des campagnes dont le maximum est de 100 000 utilisateurs. Un seul utilisateur peut approuver le canvas et lancer la campagne.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### Étape 2 : Déterminer le lancement avec approbation (facultatif)

Sélectionnez **Autoriser le lancement avec approbation.** Ensuite, pour **Avec l'approbation de**, sélectionnez les approbateurs qui ont la permission d'approuver le Canvas ou la campagne si le maximum est atteint.

Notez les détails suivants sur l'envoi de messages avec approbation :

- Si le maximum est atteint et qu'un approbateur est sélectionné, l'utilisateur de Braze disposant de l'autorisation d'approbation pourra sélectionner **Approuvé** dans le menu déroulant d'approbation de l'**audience cible.** 
- Si le maximum est atteint et qu'une approbation n'est pas sélectionnée, le Canvas ou la campagne ne pourra pas être lancé.

\![L'étape "Résumé" du flux de travail Canvas qui montre que vous avez besoin d'une approbation pour lancer le processus.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## Questions fréquemment posées

### Dois-je reconfigurer mes autorisations pour utiliser les règles d'envoi de messages ?

Non. Tout utilisateur, quelles que soient ses autorisations actuelles, peut être sélectionné comme approbateur de la population cible.

### Quel est le lien entre les règles d'envoi de messages et l'étape de l'audience cible ?

Les règles d'envoi des messages ne tiennent pas compte de détails tels que les événements déclencheurs. Par exemple, une campagne peut cibler tous vos utilisateurs. Cependant, la campagne étant déclenchée par un événement, le nombre d'utilisateurs qui la reçoivent est plus faible.

### Y a-t-il des changements automatiques lorsque les règles d'envoi des messages sont activées ?

Non. Une fois cette fonctionnalité activée, vous devez saisir manuellement le nombre maximum d'utilisateurs et sélectionner les approbateurs pour utiliser la fonctionnalité.

