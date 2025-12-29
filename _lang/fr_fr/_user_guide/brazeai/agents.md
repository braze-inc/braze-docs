---
nav_title: Agents
article_title: Agents de Braze
page_order: 0.5
description: "Les agents Braze peuvent générer du contenu, prendre des décisions intelligentes et enrichir vos données afin que vous puissiez proposer des expériences client plus personnalisées."
---

# Agents de Braze

> Les agents Braze sont des assistants dotés d'une intelligence artificielle que vous pouvez créer à l'intérieur de Braze. Les agents peuvent générer du contenu, prendre des décisions intelligentes et enrichir vos données afin que vous puissiez proposer des expériences client plus personnalisées.

{% alert important %}
Les Braze Currents sont actuellement en version bêta. Pour obtenir de l'aide, contactez votre gestionnaire satisfaction client.
{% endalert %}

## Pourquoi utiliser des agents de Braze ?

Les Teams de Braze aident votre équipe à proposer des expériences plus intelligentes et plus personnalisées, sans ajouter de travail supplémentaire. Ils agissent comme des assistants intelligents qui ne se contentent pas de répondre à des invites, mais qui comprennent le contexte, prennent des décisions et agissent pour atteindre un objectif.

En pratique, les agents peuvent créer automatiquement des messages, tels que des lignes d'objet ou des textes dans les produits, afin que chaque client reçoive une communication qui lui soit adaptée. Ils peuvent également s'adapter en temps réel, en orientant les personnes vers différents chemins de Canvas en fonction de leurs préférences, de leurs comportements ou d'autres données.

Au-delà de l'envoi de messages, les agents peuvent enrichir vos catalogues en calculant ou en générant des valeurs de champs de produits et de profils, ce qui permet de conserver des données fraîches et dynamiques. En prenant en charge les tâches répétitives ou complexes, ils libèrent votre équipe pour qu'elle se concentre sur la stratégie et la créativité plutôt que sur la configuration manuelle. Les agents Braze agissent davantage comme des collaborateurs que comme des processus d'arrière-plan - ils vous aident à résoudre des problèmes et à avoir un impact à grande échelle.

## Fonctionnalités

Les fonctionnalités des agents de Braze sont les suivantes :

- **Configuration flexible :** Utilisez un LLM fourni par Braze ou connectez votre propre fournisseur de modèle (comme OpenAI, Anthropic, Google Gemini ou AWS Bedrock).
- **Intégration fluide/sans heurts :** Déployez des agents directement dans les étapes du canvas ou les champs du catalogue.
- **Outils de test et d'enregistrement :** Prévisualisez le résultat de votre agent en le testant avec des échantillons d'entrées avant de le lancer. Consultez les journaux à chaque fois que l'agent s'exécute, y compris les données d'entrée et de sortie pour cette exécution.
- **Contrôle de l'utilisation :** Les limites d'invocation et de taille créées permettent de gérer les performances et les coûts.

## À propos des agents de Braze

Les agents sont configurés avec des instructions (invites du système) qui définissent leur comportement. Lorsqu'un agent s'exécute, il utilise vos instructions ainsi que les données que vous lui transmettez pour générer une réponse. 

### Concepts clés

| Durée | Définition |
| --- | --- |
| [Modèle]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#models) | Le "cerveau" de l'agent, en l'occurrence un grand modèle linguistique (LLM). Il interprète les entrées, génère des réponses et effectue des raisonnements. Un modèle plus solide (formé sur des données plus pertinentes) rend l'agent plus capable et plus polyvalent. |
| [Instructions]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#writing-instructions) | Les règles ou directives que vous donnez à l'agent (invite du système). Ils définissent le comportement de l'agent à chaque fois qu'il s'exécute. Des prédictions claires rendent l'agent plus fiable et plus prévisible. |
| Contexte | Données transmises à l'agent au moment de l'exécution, quel que soit l'endroit où il est déployé, telles que les champs du profil utilisateur ou les lignes du catalogue. Ces données fournissent les informations que l'agent utilise pour générer des résultats. |
| [Variable de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#step-3-define-the-output-variable) | Le résultat produit par l'agent lorsqu'il est utilisé dans les étapes du canvas. Les variables de sortie stockent le résultat de l'agent pour personnaliser le contenu ou guider les chemins de flux de travail. Les variables de sortie peuvent être des chaînes de caractères, des nombres ou des données booléennes.  |
| Invocation | Une seule exécution de l'agent. Cela est pris en compte dans vos limites quotidiennes et totales. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limites

Les agents traitent les demandes à raison d'environ 1 000 invocations par minute. Chaque espace de travail peut accueillir jusqu'à 1 000 agents. Si cette limite est atteinte, vous devrez supprimer un agent existant avant d'en créer un nouveau. 

En outre, pendant la période bêta :

- L'invocation est limitée à 50 000 exécutions par jour et à 500 000 exécutions au total.
- Chaque course doit être terminée en moins de 30 secondes. Après 30 secondes, l'agent renvoie une réponse nulle lorsqu'il est utilisé.
- Les données d'entrée sont limitées à 10 Ko par demande. Les entrées plus longues sont tronquées.
- Pour les catalogues, les champs agentiques ne mettent à jour que les 10 000 premières lignes.

## Prochaines étapes

Maintenant que vous connaissez les agents Braze, vous êtes prêt pour les étapes suivantes :

- [Création d'agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Déploiement d'agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
