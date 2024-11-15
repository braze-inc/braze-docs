---
nav_title: "Approbation de la population cible"
article_title: "Approbation de la population cible"
permalink: "/target_approvals/"
hidden: true
description: "Cet article décrit comment utiliser les approbations de la population cible pour les campagnes et les Canevas avec un grand volume d'envoi."
---

# Approbation de la population cible

> Cette page explique comment configurer les approbations de la population cible pour vos règles d'envoi de messages. Grâce à l'approbation de la population cible, vous pouvez définir des seuils de volume pour les campagnes et les canevas afin d'exiger une approbation supplémentaire pour vos règles d'envoi de messages. Ainsi, vous pouvez procéder à un examen supplémentaire lorsqu'une audience plus large est visée par votre message.

{% alert important %}
L'approbation de la population cible est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Prérequis

Avant de pouvoir configurer l'approbation de la population cible, les flux de travail d'approbation de Canvas et de la campagne doivent être activés.

Pour activer les flux d'approbation des canvas et des campagnes, accédez à **Paramètres** > **Flux d'approbation** > **Approbations toujours actives.** 

## Mise en place de l'approbation de la population cible

1. Allez dans **Réglages** > **Workflow d'approbation** > **Règles d'envoi de messages.**
2. Sélectionnez **Créer une règle**.
3. Donnez un nom à votre règle pour l'identifier d'un coup d'œil (par exemple, "Tous les abonnements d'utilisateur").
4. Pour **Objet**, sélectionnez **Campagne**, **Canvas** ou **à la fois Canvas et Campagnes** pour appliquer la règle d'approbation.
5. Saisissez un nombre pour le **seuil d'utilisateurs joignables**. Pour plus d'informations, reportez-vous aux [statistiques d'audience]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Sélectionnez **Enregistrer**.

![Exemple de règle d'envoi de messages "Règle 1" pour les Canvas et les campagnes avec un seuil de 100 000 utilisateurs. Trois utilisateurs peuvent approuver le canvas et la campagne à lancer.][1]

Vous pouvez définir jusqu'à cinq règles d'envoi de messages. Lors de la mise en place de votre règle d'envoi de messages, deux règles peuvent exister avec le même seuil de volume pour le même objet. Par exemple, vous pouvez définir un seuil de 10 000 utilisateurs pour Canvas et de 10 000 utilisateurs pour Canvas et les campagnes. 

De même, si vous définissez deux seuils de 10 000 utilisateurs pour Canvas avec des approbateurs différents, cette règle peut être enregistrée. De cette façon, vous pouvez organiser et séparer vos approbateurs (tels que votre équipe juridique et votre équipe de conception) selon des règles spécifiques.

Notez que vous ne pouvez pas définir des règles avec des seuils de volume qui se chevauchent pour le même objet. Par exemple, la règle d'envoi de messages suivante **ne peut pas être** définie : une règle avec un seuil de 10 000 utilisateurs pour Canvas et une autre règle avec un seuil de 1 000 000 d'utilisateurs pour Canvas.

### Sélection des approbateurs

{% alert important %}
Vous pouvez éventuellement sélectionner des approbateurs qui, si le seuil est atteint, ont la permission d'approuver le canvas ou la campagne. Si vous ne sélectionnez pas d'approbateurs, le canvas ou la campagne ne pourra pas être lancé.
{% endalert %}

Seuls les administrateurs de Braze peuvent définir des règles d'envoi de messages, mais tout utilisateur de Braze peut être un approbateur de population cible (y compris les utilisateurs ne disposant pas d'autorisations générales d'approbation). 

Si un seuil est atteint et qu'un approbateur est sélectionné, l'utilisateur disposant de l'autorisation d'approbation pourra sélectionner **Approuvé** dans le menu déroulant d'approbation de l'**audience cible.** 

### Règles dans les canvas et les campagnes

L'approbation de la population cible contrôle qui peut approuver l'étape de l'**audience cible** d'un canvas et d'une campagne. Si une règle est respectée mais que les approbateurs ne sont pas sélectionnés, le bouton de **lancement** ou de **mise à jour du** canvas ou de la campagne sera désactivé.

![L'étape "Résumé" du flux de travail Canvas qui montre que vous avez besoin d'une approbation pour lancer le processus.][2]

## Foire aux questions

### Y a-t-il des changements automatiques lorsque cette fonctionnalité est activée ?

Non. Une fois cette fonctionnalité activée, vous devez saisir manuellement un seuil de volume et sélectionner les approbateurs pour utiliser la fonctionnalité.

### Dois-je reconfigurer mes autorisations pour utiliser cette fonctionnalité ?

Non. Vous n'avez pas besoin de modifier les autorisations existantes. Tout utilisateur, quelles que soient ses autorisations actuelles, peut être sélectionné comme approbateur de la population cible.

### Le même seuil s'applique-t-il à tous les espaces de travail ?

Non. Vous devez définir des règles d'envoi de messages pour chaque espace de travail.

### Le ciblage de la population est-il approuvé sur la base de l'étape "Public cible" ?

Oui. L'approbation de la population cible ne tient pas compte de détails tels que les événements déclencheurs. Par exemple, une campagne peut cibler tous vos utilisateurs ; cependant, la campagne est déclenchée par un événement, de sorte que le nombre d'utilisateurs réels qui la reçoivent est plus faible.

[1]: {% image_buster /assets/img/target_population_approval_example.png %}
[2]: {% image_buster /assets/img/non_approver_banner.png %}