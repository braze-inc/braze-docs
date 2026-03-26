---
nav_title: Console des agents
article_title: Agents Braze
page_order: 1
description: "Les agents Braze peuvent générer du contenu, prendre des décisions intelligentes et enrichir vos données afin que vous puissiez offrir des expériences client plus personnalisées."
---

# Agents Braze dans la console d'agent

> Les agents Braze sont des assistants alimentés par l'intelligence artificielle que vous pouvez créer dans Braze. Les agents peuvent générer du contenu, prendre des décisions éclairées et enrichir vos données afin que vous puissiez offrir des expériences client plus personnalisées.

{% alert important %}
Des crédits de messagerie sont nécessaires pour accéder à Braze Agents et l'utiliser. Si vous ne disposez pas actuellement de crédits de messages et que vous souhaitez utiliser Braze Agents, veuillez contacter votre gestionnaire de compte pour connaître les étapes suivantes.
{% endalert %}

## Pourquoi utiliser Braze Agents ?

Les agents Braze assistent votre équipe dans la fourniture d'expériences plus intelligentes et personnalisées, sans charge de travail supplémentaire. Ils agissent en tant qu'agents autonomes qui ne se contentent pas de répondre à des invites, mais comprennent le contexte, prennent des décisions et agissent pour atteindre un objectif.

En pratique, les agents peuvent générer automatiquement des messages, tels que des lignes d'objet ou du texte intégré au produit, afin que chaque client reçoive une communication personnalisée. Ils peuvent également s'adapter en temps réel, en orientant les personnes vers différents parcours canvas en fonction de leurs préférences, de leurs comportements ou d'autres données.

Au-delà de l’envoi de messages, les agents peuvent enrichir vos catalogues en calculant ou en générant des valeurs de champs pour les produits et les profils, ce qui permet de maintenir vos données à jour et dynamiques. En prenant en charge les tâches répétitives ou complexes, ils permettent à votre équipe de se concentrer sur la stratégie et la créativité plutôt que sur la configuration manuelle. Les agents Braze agissent davantage comme des collaborateurs que comme des processus en arrière-plan, vous aidant à résoudre les problèmes et à avoir un impact à grande échelle.

### Quand utiliser les agents Braze par rapport aux autres fonctionnalités de BrazeAI

Utilisez des agents pour réaliser la personnalisation du contenu à la volée en fonction du contexte spécifique de l'utilisateur. Par exemple, si un agent sait que la saveur de crème glacée préférée d'un utilisateur particulier est le chocolat et que sa garniture préférée est les oursons en gélatine, il peut proposer un message push spécifique à cette combinaison pour cet utilisateur lorsqu'il passe par le canvas.

Cependant, l'agent n'apprend pas par essais et erreurs, et il n'a aucune idée de l'objectif marketing ultime qu'il cherche à mesurer et à maximiser. Même si vous lui demandez de rédiger des textes qui favorisent les conversions, il ne dispose d'aucun mécanisme pour « surveiller » l'impact de ses textes sur les conversions et réaliser l'intégration des données dans ses futures communications. Vous pouvez considérer cela comme une prise de décision basée sur l'« ambiance », et non comme une prise de décision basée sur la récompense par l'intelligence artificielle.

En revanche, les autres outils BrazeAI sont conçus pour optimiser les indicateurs qu'ils mesurent. Par exemple, les agents sont particulièrement compétents pour évaluer de manière qualitative comment les caractéristiques d'un utilisateur influencent sa probabilité ou sa propension à réaliser une certaine action ou à apprécier un certain produit. Cependant, comme l'agent n'apprend pas par essais et erreurs, il ne sait pas comment mesurer sa précision dans les prédictions des probabilités et l'amélioration du signal au fil du temps. À ce titre, l'utilisation de Predictive Suite surpasse l'étape Agent lorsqu'on évalue la précision de ses prédictions et les améliorations apportées au fil du temps.

## Fonctionnalités

Les fonctionnalités pour les agents Braze comprennent :

- **Configuration flexible :** Veuillez utiliser un modèle LLM fourni par Braze ou connecter vos propres [fournisseurs de modèles d'intelligence artificielle]({{site.baseurl}}/partners/ai_model_providers) (tels que OpenAI, Anthropic ou Google Gemini).
- **Intégration fluide :** Veuillez déployer les agents directement dans les étapes du canvas ou les champs du catalogue.
- **Outils de test et de journalisation :** Veuillez prévisualiser les résultats de votre agent en effectuant des tests avec des exemples d'entrées avant le lancement. Consultez les journaux pour chaque exécution de l'agent, y compris les entrées et sorties pour cette exécution.
- **Contrôles d'utilisation :** Les limites quotidiennes facilitent la gestion des performances et des coûts.

## À propos des agents Braze

Les agents sont configurés avec des instructions (invites système) qui définissent leur comportement. Lorsqu'un agent s'exécute, il utilise vos instructions ainsi que toutes les données que vous lui transmettez pour générer une réponse.

### Concepts clés

| Terme | Définition |
| --- | --- |
| [Modèle]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) | Le « cerveau » de l'agent, dans ce cas un modèle linguistique de grande taille (LLM). Il interprète les entrées, génère des réponses et effectue des raisonnements. Un modèle plus performant (entraîné sur des données plus pertinentes) rend l'agent plus efficace et polyvalent. |
| [Instructions]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) | Les règles ou directives que vous fournissez à l'agent (invite du système). Ils définissent comment l'agent doit se comporter à chaque fois qu'il s'exécute. Des instructions claires rendent l'agent plus fiable et prévisible. |
| Contexte | Données transmises à l'agent lors de l'exécution, quel que soit son lieu de déploiement, telles que les champs du profil utilisateur ou les lignes du catalogue. Cette entrée fournit les informations que l'agent utilise pour générer des sorties. |
| [Variable de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#define-the-output-variable) | Le résultat généré par l'agent lorsqu'il est utilisé dans les étapes du canvas. Les variables de sortie enregistrent les résultats de l'agent afin de réaliser la personnalisation du contenu ou de guider les chemins de workflow. Les variables de sortie peuvent être de type chaîne de caractères, nombre ou booléen.  |
| [Exécution](#limitations) | Une seule exécution de l'agent. Cela est déduit de vos limites quotidiennes. |
| [Format de sortie]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#select-output) | La structure de données prédéfinie de la réponse de l'agent. |
| [Température]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) | Le niveau de déviation pour la production de l'agent. Cela détermine le niveau de précision ou de créativité dont votre agent est capable. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Restrictions

Les restrictions suivantes s'appliquent :

- Chaque agent dispose d'une limite d'exécution quotidienne par défaut de 250 000 exécutions, qui peut être augmentée jusqu'à un maximum de 1 000 000 exécutions par jour. Veuillez contacter votre gestionnaire de la satisfaction client si vous souhaitez augmenter cette limite.
- Par défaut, chaque exécution doit être terminée dans les 15 secondes. Après 15 secondes, l'agent renvoie une`null`réponse là où il est utilisé.
    - Si vos agents dépassent régulièrement le délai imparti, veuillez contacter votre gestionnaire de compte Braze afin d'augmenter cette limite.
- Les données saisies sont limitées à 25 Ko par demande. Les entrées plus longues sont tronquées.

## Comment mes données sont-elles utilisées et transmises aux LLM fournis par Braze ?

Afin de générer des résultats d'intelligence artificielle grâce aux fonctionnalités d'intelligence artificielle de Braze que Braze identifie comme exploitant les LLM fournis par Braze (« Résultats »), Braze enverra votre invite système ou toute autre entrée, selon le cas (« Entrée »), au LLM fourni par Braze. Les données transmises au modèle LLM fourni par Braze ne sont pas utilisées pour entraîner ou améliorer ledit modèle. Entre vous et Braze, Output constitue votre propriété intellectuelle. Braze ne fera valoir aucun droit d'auteur sur ces Résultats. Braze n'offre aucune garantie de quelque nature que ce soit concernant tout contenu généré par l'intelligence artificielle en général, y compris les résultats.

Le modèle LLM fourni par Braze pour les agents Braze, identifié comme « Auto », utilise les modèles Google Gemini. Google conserve les données d'entrée et de sortie soumises via Braze pendant 55 jours, après quoi les données sont supprimées.

## Étapes suivantes

Maintenant que vous connaissez Braze Agents, vous êtes prêt pour les étapes suivantes :

- [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Déployer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
