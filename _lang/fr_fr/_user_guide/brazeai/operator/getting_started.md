---
nav_title: Démarrer
article_title: Démarrer avec BrazeAI Operator<sup>TM</sup>
page_order: 1
description: "Apprenez à accéder et à utiliser BrazeAI Operator<sup>TM</sup>, l'assistant IA de Braze intégré au tableau de bord, notamment ses fonctionnalités et bonnes pratiques."
---

# Démarrer avec BrazeAI Operator

> Apprenez à accéder et à utiliser BrazeAI Operator<sup>TM</sup>, votre assistant IA intégré au tableau de bord, notamment ses fonctionnalités et bonnes pratiques.

## Accéder à Operator

Ouvrez Operator depuis n'importe quelle page du tableau de bord Braze.

1. Sélectionnez **BrazeAI Operator<sup>TM</sup>** à côté de votre profil utilisateur.

![L'icône BrazeAI Operator à côté d'un profil utilisateur.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. Le panneau de chat Operator s'ouvre sur le côté droit de l'écran.

![Le panneau de chat Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Agrandissez le panneau pour une lecture plus facile, ou réduisez-le pour garder Operator disponible pendant que vous travaillez.
{% endalert %}

## Utiliser Operator

Décrivez ce que vous essayez d'accomplir en langage naturel. Les invites peuvent aller de questions simples à des demandes complexes :

- **Simple :** Pourquoi mon Liquid ne s'affiche-t-il pas correctement ?
- **Complexe :** Comment faire en sorte que la balise `abort_message` de mon message inclue l'attribut utilisateur qui a provoqué l'abandon ?

Operator peut fournir des instructions étape par étape, des liens vers la documentation Braze et des explications en langage clair. Des questions claires et précises donnent des réponses plus utiles. Operator utilise [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), qui offre un raisonnement solide et convient aux tâches complexes en plusieurs étapes.

## Bonnes pratiques

Traitez Operator comme une conversation, pas comme un moteur de recherche. Les invites courtes et naturelles fonctionnent le mieux.

- **Soyez précis :** Au lieu de « Parle-moi de Canvas », demandez « Comment utiliser les parcours d'action dans Canvas ? ».
- **Posez des questions de suivi :** Si la première réponse ne correspond pas à votre besoin, demandez des précisions ou des détails supplémentaires.
- **Utilisez le contexte de la page :** Operator comprend votre emplacement dans Braze. Ouvrez Operator en consultant la page concernée pour des résultats plus précis.

## Personnaliser votre expérience

### Appliquer les directives de marque

Ajoutez les directives de marque comme contexte aux requêtes Operator pour que les réponses correspondent à la voix, au ton et à la personnalité de votre marque. Operator utilise les directives de marque configurées dans votre espace de travail, ce qui garantit une messagerie cohérente lorsqu'il suggère du contenu ou explique des fonctionnalités.

Pour configurer les directives de marque, allez dans **Paramètres** > **Directives de marque**. Pour en savoir plus, consultez les [Directives de marque]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Sélection des directives de marque dans le panneau de chat Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Tirer parti du contexte de la page

Operator comprend automatiquement votre emplacement dans Braze et adapte les réponses en conséquence. Par exemple, si vous ouvrez Operator lors de la création d'un Canvas, il peut suggérer des étapes pertinentes ou fournir des conseils sur les fonctionnalités Canvas sans que vous ayez à expliquer où vous en êtes.

Vous pouvez donc poser des questions plus courtes et naturelles comme « Comment ajouter un délai ? » au lieu de « Comment ajouter une étape de délai dans un workflow Canvas ? ».

## Travailler avec les réponses d'Operator

### Démarrer avec les invites suggérées

Lorsque vous ouvrez Operator, des invites suggérées apparaissent en fonction des tâches courantes et de votre page actuelle. Sélectionnez-en une pour démarrer rapidement ou saisissez votre propre question.

### Comprendre le raisonnement d'Operator

Operator affiche ses étapes de raisonnement dans des sections repliables intitulées **Reasoned**. Sélectionnez le menu déroulant pour développer ces sections et voir comment Operator a déterminé une réponse.

![Le menu déroulant « Reasoned » replié dans une réponse Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Passer à l'action avec Operator

Operator peut proposer et exécuter des modifications directement dans le tableau de bord Braze, par exemple remplir des champs de formulaire, mettre à jour des paramètres ou générer du contenu. Chaque modification proposée est présentée sous forme de carte d'action à examiner et à approuver avant qu'elle ne prenne effet. Pour en savoir plus, consultez [Examen des actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Gérer votre session

### Arrêter une réponse

Pendant qu'Operator génère une réponse, le bouton **Envoyer** devient **Arrêter**. Sélectionnez **Arrêter** pour mettre fin à la réponse plus tôt si vous devez reformuler votre question ou si la réponse part dans la mauvaise direction.

### Effacer l'historique

Pour repartir de zéro ou supprimer des informations sensibles de la conversation, sélectionnez **Effacer l'historique du chat**. Cela supprime tout le contenu actuel et réinitialise le contexte de la conversation.

### Donner un avis

En bas de chaque réponse, utilisez les boutons pouce vers le haut ou pouce vers le bas pour donner un avis rapide. Vos retours aident à améliorer les réponses d'Operator au fil du temps.

## Prochaines étapes

- [Examen des actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) – Apprenez à examiner et approuver les modifications proposées par Operator
- [Résolution des problèmes]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) – Problèmes courants et solutions
