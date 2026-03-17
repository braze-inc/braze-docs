---
nav_title: Opérateur
article_title: Opérateur BrazeAI
page_order: 7
alias: /operator/
toc_headers: h2
description: "Découvrez comment accéder et utiliser BrazeAI Operator<sup>TM</sup>, un assistant alimenté par l'intelligence artificielle créé dans le tableau de bord de Braze, y compris ses fonctionnalités et ses meilleures pratiques."
---

# Opérateur BrazeAI

> BrazeAI Operator<sup>TM</sup> est un assistant alimenté par l'intelligence artificielle créé dans le tableau de bord. L'opérateur contribue à la réalisation des tâches : il répond aux questions, guide la configuration, effectue la résolution des problèmes et propose des idées.

## Opérateur d'accès

Veuillez ouvrir l'opérateur depuis n'importe quelle page du tableau de bord de Braze.  

1. Veuillez sélectionner **BrazeAI Operator<sup>TM</sup>** à côté de votre profil utilisateur.

![L'icône BrazeAI Operator à côté d'un profil utilisateur.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2\. Le panneau de discussion de l'opérateur s'ouvre sur le côté droit de l'écran.

![Le panneau de discussion de l'opérateur.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Veuillez agrandir la fenêtre pour faciliter la lecture ou la réduire pour garder l'opérateur accessible pendant le travail.  
{% endalert %} 

## Utiliser l'opérateur

Veuillez décrire ce que vous essayez d'accomplir en utilisant un langage naturel. Les invites peuvent aller de simples questions à des demandes complexes :

- **Simple :** Pourquoi mon liquid ne s'affiche-t-il pas correctement ?
- **Complexe :** Comment puis-je faire en sorte que`abort_message`l'étiquette de mon message inclue l'attribut utilisateur qui a provoqué l'interruption ?

L'opérateur peut fournir des instructions étape par étape, des liens vers la documentation Braze et des explications en langage clair. Des questions claires et précises permettent d'obtenir des réponses plus utiles. L'opérateur utilise [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), qui offre un raisonnement solide et convient aux tâches complexes en plusieurs étapes. 

## Bonnes pratiques

Considérez l'opérateur comme une conversation, et non comme un moteur de recherche. Les invites courtes et naturelles sont les plus efficaces.

- **Soyez précis :** Au lieu de « Pouvez-vous me parler de Canvas ? », essayez plutôt « Comment puis-je utiliser les parcours d’action dans Canvas ? ».  
- **Posez des questions complémentaires :** Si la première réponse ne répond pas à votre demande, veuillez demander des précisions ou des informations supplémentaires.
- **Utiliser le contexte sensible à la page :** L'opérateur identifie votre localisation à Braze. Veuillez ouvrir l'opérateur tout en consultant la page correspondante pour obtenir les résultats les plus précis.

## Personnalisez votre expérience

### Appliquer les directives relatives à la marque

Ajoutez les directives de marque comme contexte aux requêtes de l'opérateur afin que les réponses correspondent au ton, au style et à la personnalité de votre marque. L'opérateur utilise les directives de marque configurées dans votre espace de travail, ce qui contribue à garantir la cohérence de l'envoi de messages lorsqu'il suggère des textes ou explique des fonctionnalités.

Pour configurer les directives relatives à la marque, veuillez vous rendre dans **Paramètres** > **Directives relatives à la marque**. Pour plus d'informations, veuillez consulter [les directives relatives à la marque]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Sélectionner les directives relatives à la marque dans le panneau de discussion de l'opérateur.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Tirer parti du contexte sensible à la page

L'opérateur identifie automatiquement votre localisation dans Braze et adapte ses réponses en fonction de ce contexte. Par exemple, lorsque vous ouvrez Operator pendant la création d'un Canvas, il peut vous suggérer des étapes pertinentes ou vous fournir des conseils sur les fonctionnalités de Canvas sans que vous ayez à expliquer où vous en êtes dans votre flux de travail.

Cette prise en compte du contexte vous permet de poser des questions plus courtes et plus naturelles, telles que « Comment puis-je ajouter un délai ? » au lieu de « Comment puis-je ajouter une étape de délai dans un workflow Canvas ? ».

## Collaborer avec les réponses de l'opérateur

### Commencez avec les suggestions proposées

Lorsque vous ouvrez Operator, des suggestions s'affichent en fonction des tâches courantes et de la page sur laquelle vous vous trouvez. Veuillez sélectionner une option pour commencer rapidement ou saisir votre propre question personnalisée.

### Comprendre la perspective de l'opérateur

L'opérateur affiche ses étapes de raisonnement dans des sections repliables intitulées **« Raisonnement** ». Veuillez sélectionner le menu déroulant pour développer ces sections et découvrir comment l'opérateur a déterminé une réponse. Cela est utile lorsque vous souhaitez comprendre la logique derrière une suggestion ou vérifier l'approche.

![Le menu déroulant « Raisonnable » s'est affiché dans une réponse de l'opérateur.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Agissez avec l'opérateur

L'opérateur peut proposer et effectuer des modifications directement dans le tableau de bord de Braze, telles que remplir des champs de formulaire, mettre à jour des paramètres ou générer du contenu. Chaque modification proposée est présentée sous forme de carte d'action que vous devez examiner et approuver avant qu'elle ne prenne effet. Pour en savoir plus sur le fonctionnement de cette fonctionnalité, veuillez consulter [la section Révision des actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Veuillez gérer votre session.

### Interrompre une réponse

Pendant que l'opérateur génère une réponse, le bouton **Envoyer** devient un bouton **Arrêter**. Veuillez sélectionner **« Arrêter** » pour mettre fin prématurément à la réponse si vous avez besoin de reformuler votre question ou si la réponse ne va pas dans la bonne direction.

### Veuillez effacer votre historique.

Pour recommencer à zéro ou supprimer des informations sensibles de la conversation, veuillez sélectionner **Effacer l'historique des discussions**. Cela supprime tout le contenu actuel et réinitialise le contexte de la conversation.

### Veuillez nous faire part de vos commentaires.

Au bas de chaque réponse, veuillez utiliser les boutons « pouce vers le haut » ou « pouce vers le bas » pour fournir un commentaire rapide. Vos commentaires contribuent à améliorer les réponses de l'opérateur au fil du temps.

## Confidentialité des données et sécurité des données

### Conformité HIPAA

Intelligence artificielle Operator utilise une technologie de conversation multitours qui n'est actuellement pas éligible à la politique de rétention zéro des données d'OpenAI. L'intelligence artificielle applique la politique de conservation des données de surveillance des abus modifiée d'OpenAI, mais l'intelligence artificielle n'est pas couverte par l'accord de partenariat commercial (BAA) entre Braze et OpenAI. Les utilisateurs ne doivent pas demander à l'opérateur d'intelligence artificielle d'accéder aux informations médicales protégées (PHI) stockées dans Braze ni soumettre de PHI à cette fonctionnalité.

### Fournisseurs modèles en tant que sous-traitants ou fournisseurs tiers

Lorsque vous utilisez une intégration avec un fournisseur LLM fourni par Braze via les Services Braze (« LLM fourni par Braze »), les fournisseurs dudit LLM fourni par Braze agissent en tant que sous-traitants de Braze, sous réserve des conditions de l'Addendum relatif au traitement des données (DPA) conclu entre vous et Braze. BrazeAI Operator<sup>TM</sup> effectue l'intégration avec OpenAI.

### Utilisation des données avec OpenAI

Afin de générer des résultats d'intelligence artificielle grâce aux fonctionnalités BrazeAI qui exploitent OpenAI (« Résultats »), Braze transmettra certaines informations (« Données d'entrée ») à OpenAI. Les données d'entrée comprennent vos invites, le contenu affiché dans le tableau de bord et les données de l'espace de travail pertinentes pour vos requêtes. Conformément [aux engagements de la plateforme API d'OpenAI](https://openai.com/enterprise-privacy/), les données transmises à l'API d'OpenAI via Braze ne sont pas utilisées pour former ou améliorer les modèles d'OpenAI. Entre vous et Braze, Output constitue votre propriété intellectuelle. Braze ne fera valoir aucun droit d'auteur sur ces Résultats. Braze n'offre aucune garantie de quelque nature que ce soit concernant tout contenu généré par l'intelligence artificielle, y compris les résultats.

## Étapes suivantes

- [Examen des actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) : Veuillez apprendre comment examiner et approuver les modifications proposées par l'opérateur.
- [Résolution des problèmes]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) : Veuillez consulter les problèmes courants et leurs solutions.
