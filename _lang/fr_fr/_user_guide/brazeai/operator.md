---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Découvrez comment accéder à BrazeAI Operator<sup>TM</sup> et l'utiliser. Cet assistant alimenté par l'intelligence artificielle est intégré au tableau de bord de Braze. Retrouvez ses fonctionnalités et les bonnes pratiques associées."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup> est un assistant alimenté par l'intelligence artificielle, intégré au tableau de bord. Operator vous aide à avancer dans vos tâches : répondre à vos questions, vous guider dans la configuration, résoudre des problèmes et générer des idées.

## Accéder à Operator

Ouvrez Operator depuis n'importe quelle page du tableau de bord de Braze.  

1. Sélectionnez **BrazeAI Operator<sup>TM</sup>** à côté de votre profil utilisateur.

![L'icône BrazeAI Operator à côté d'un profil utilisateur.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. Le panneau de discussion d'Operator s'ouvre sur le côté droit de l'écran.

![Le panneau de discussion d'Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Agrandissez le panneau pour faciliter la lecture, ou réduisez-le pour garder Operator accessible pendant que vous travaillez.  
{% endalert %} 

## Utiliser Operator

Décrivez ce que vous souhaitez accomplir en langage naturel. Vos requêtes peuvent aller de simples questions à des demandes complexes :

- **Simple :** Pourquoi mon Liquid ne s'affiche-t-il pas correctement ?
- **Complexe :** Comment puis-je faire en sorte que l'étiquette `abort_message` de mon message inclue l'attribut utilisateur qui a provoqué l'interruption ?

Operator peut fournir des instructions étape par étape, des liens vers la documentation Braze et des explications en langage clair. Des questions claires et précises permettent d'obtenir des réponses plus utiles. Operator utilise [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), qui offre un raisonnement solide et convient aux tâches complexes en plusieurs étapes. 

## Bonnes pratiques

Considérez Operator comme une conversation, et non comme un moteur de recherche. Les requêtes courtes et naturelles sont les plus efficaces.

- **Soyez précis :** Au lieu de « Parlez-moi de Canvas », essayez plutôt « Comment utiliser les parcours d'action dans Canvas ? ».  
- **Posez des questions complémentaires :** Si la première réponse ne correspond pas à votre besoin, demandez des précisions ou des informations supplémentaires.
- **Exploitez le contexte de page :** Operator identifie la page sur laquelle vous vous trouvez dans Braze. Ouvrez Operator en consultant la page concernée pour obtenir les résultats les plus pertinents.

## Personnaliser votre expérience

### Appliquer les directives de marque

Ajoutez les directives de marque comme contexte à vos requêtes Operator afin que les réponses correspondent au ton, au style et à la personnalité de votre marque. Operator utilise les directives de marque configurées dans votre espace de travail, ce qui contribue à garantir la cohérence de l'envoi de messages lorsqu'il suggère des textes ou explique des fonctionnalités.

Pour configurer les directives de marque, rendez-vous dans **Paramètres** > **Directives de marque**. Pour en savoir plus, consultez [Directives de marque]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Sélection des directives de marque dans le panneau de discussion d'Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Tirer parti du contexte de page

Operator identifie automatiquement votre emplacement dans Braze et adapte ses réponses en fonction de ce contexte. Par exemple, lorsque vous ouvrez Operator pendant la création d'un Canvas, il peut vous suggérer des étapes pertinentes ou vous fournir des conseils sur les fonctionnalités de Canvas sans que vous ayez à expliquer où vous en êtes dans votre flux de travail.

Cette prise en compte du contexte vous permet de poser des questions plus courtes et plus naturelles, comme « Comment ajouter un délai ? » au lieu de « Comment ajouter une étape de délai dans un workflow Canvas ? ».

## Exploiter les réponses d'Operator

### Commencer avec les suggestions proposées

Lorsque vous ouvrez Operator, des suggestions s'affichent en fonction des tâches courantes et de la page sur laquelle vous vous trouvez. Sélectionnez-en une pour démarrer rapidement, ou saisissez votre propre question.

### Comprendre le raisonnement d'Operator

Operator affiche ses étapes de raisonnement dans des sections repliables intitulées **Reasoned**. Sélectionnez le menu déroulant pour développer ces sections et découvrir comment Operator a déterminé sa réponse. C'est utile lorsque vous souhaitez comprendre la logique derrière une suggestion ou vérifier l'approche adoptée.

![Le menu déroulant « Reasoned » replié dans une réponse d'Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Passer à l'action avec Operator

Operator peut proposer et exécuter des modifications directement dans le tableau de bord de Braze, comme remplir des champs de formulaire, mettre à jour des paramètres ou générer du contenu. Chaque modification proposée est présentée sous forme de carte d'action que vous pouvez examiner et approuver avant qu'elle ne prenne effet. Pour en savoir plus, consultez [Vérifier les actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Gérer votre session

### Interrompre une réponse

Pendant qu'Operator génère une réponse, le bouton **Envoyer** devient un bouton **Arrêter**. Sélectionnez **Arrêter** pour mettre fin à la réponse si vous devez reformuler votre question ou si la réponse ne va pas dans la bonne direction.

### Effacer votre historique

Pour repartir de zéro ou supprimer des informations sensibles de la conversation, sélectionnez **Effacer l'historique des discussions**. Cela supprime tout le contenu actuel et réinitialise le contexte de la conversation.

### Donner votre avis

Au bas de chaque réponse, utilisez les boutons « pouce vers le haut » ou « pouce vers le bas » pour fournir un retour rapide. Vos retours contribuent à améliorer les réponses d'Operator au fil du temps.

## Confidentialité et sécurité des données

### Conformité HIPAA

AI Operator utilise une technologie de conversation multitours qui n'est actuellement pas éligible à la politique de rétention zéro des données d'OpenAI. AI Operator applique la politique de conservation des données de surveillance des abus modifiée d'OpenAI, mais AI Operator n'est pas couvert par l'accord de partenariat commercial (BAA) entre Braze et OpenAI. Les utilisateurs ne doivent pas demander à AI Operator d'accéder aux informations médicales protégées (PHI) stockées dans Braze ni soumettre de PHI à cette fonctionnalité.

### Fournisseurs de modèles en tant que sous-traitants ou fournisseurs tiers

Lorsque vous utilisez une intégration avec un fournisseur LLM fourni par Braze via les services Braze (« LLM fourni par Braze »), les fournisseurs dudit LLM fourni par Braze agissent en tant que sous-traitants de Braze, sous réserve des conditions de l'Addendum relatif au traitement des données (DPA) conclu entre vous et Braze. BrazeAI Operator<sup>TM</sup> s'intègre avec OpenAI.

### Utilisation des données avec OpenAI

Afin de générer des résultats d'intelligence artificielle grâce aux fonctionnalités BrazeAI qui exploitent OpenAI (« Résultats »), Braze transmettra certaines informations (« Données d'entrée ») à OpenAI. Les données d'entrée comprennent vos requêtes, le contenu affiché dans le tableau de bord et les données de l'espace de travail pertinentes pour vos demandes. Conformément aux [engagements de la plateforme API d'OpenAI](https://openai.com/enterprise-privacy/), les données transmises à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer les modèles d'OpenAI. Entre vous et Braze, les Résultats constituent votre propriété intellectuelle. Braze ne fera valoir aucun droit d'auteur sur ces Résultats. Braze n'offre aucune garantie de quelque nature que ce soit concernant tout contenu généré par l'intelligence artificielle, y compris les Résultats.

## Étapes suivantes

- [Vérifier les actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) : Découvrez comment examiner et approuver les modifications proposées par Operator.
- [Soumettre des tickets d'assistance]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/) : Créez des tickets d'assistance directement depuis Operator.
- [Résolution des problèmes]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) : Consultez les problèmes courants et leurs solutions.