---
nav_title: Agents
article_title: Agents Braze
page_order: 0.5
description: "Les agents Braze peuvent générer du contenu, prendre des décisions intelligentes et enrichir vos données afin que vous puissiez offrir des expériences client plus personnalisées."
---

# Agents Braze

> Les agents Braze sont des assistants dotés d'une intelligence artificielle que vous pouvez créer à l'intérieur de Braze. Les agents peuvent générer du contenu, prendre des décisions intelligentes et enrichir vos données afin que vous puissiez proposer des expériences client plus personnalisées.

{% alert important %}
Les Braze Currents sont actuellement en version bêta. Pour obtenir de l'aide, contactez votre gestionnaire satisfaction client.
{% endalert %}

## Pourquoi utiliser des agents de Braze ?

Les Teams de Braze aident votre équipe à proposer des expériences plus intelligentes et plus personnalisées, sans ajouter de travail supplémentaire. Ils agissent comme des assistants intelligents qui ne se contentent pas de répondre à des invites, mais qui comprennent le contexte, prennent des décisions et agissent pour atteindre un objectif.

En pratique, les agents peuvent créer automatiquement des messages, tels que des lignes d'objet ou des textes dans les produits, afin que chaque client reçoive une communication qui lui soit adaptée. Ils peuvent également s'adapter en temps réel, en orientant les personnes vers différents chemins de Canvas en fonction de leurs préférences, de leurs comportements ou d'autres données.

Au-delà de l'envoi de messages, les agents peuvent enrichir vos catalogues en calculant ou en générant des valeurs de champs de produits et de profils, ce qui permet de conserver des données fraîches et dynamiques. En prenant en charge les tâches répétitives ou complexes, ils libèrent votre équipe pour qu'elle se concentre sur la stratégie et la créativité plutôt que sur la configuration manuelle. Les agents Braze agissent davantage comme des collaborateurs que comme des processus d'arrière-plan - ils vous aident à résoudre des problèmes et à avoir un impact à grande échelle.

### Quand utiliser les agents Braze par rapport aux autres fonctionnalités de BrazeAI ?

Agents d'utilisation pour personnaliser le contenu à la volée en fonction du contexte spécifique de l'utilisateur. Par exemple, si un agent sait que le parfum de glace préféré d'un utilisateur est le chocolat et que sa garniture préférée est les oursons en gélatine, il peut proposer à cet utilisateur des messages push spécifiques à cette combinaison lors de son passage dans le Canvas.

Cependant, l'agent n'apprend pas par essais et erreurs, et il n'a aucune idée d'un objectif marketing ultime qu'il cherche à mesurer et à maximiser. Même si vous lui demandez de rédiger des textes qui génèrent des conversions, il ne dispose d'aucun mécanisme lui permettant de "surveiller" l'impact de ses écrits sur les conversions et d'intégrer ces données dans ses futurs appels d'offres. Vous pouvez considérer qu'il s'agit d'une prise de décision "vibratoire", et non d'une prise de décision d'intelligence artificielle basée sur la récompense.

En revanche, d'autres outils de BrazeAI sont conçus pour maximiser les indicateurs qu'ils mesurent. Par exemple, les agents sont très doués pour évaluer qualitativement la façon dont les caractéristiques d'un utilisateur influent sur sa probabilité ou sa propension à participer à un certain événement ou à aimer un certain produit. Cependant, comme l'agent n'apprend pas par essais et erreurs, il n'a aucune idée de la manière de mesurer sa précision dans la prédiction des prédictions et l'amélioration du signal au fil du temps. Ainsi, l'utilisation de la Predictive Suite est plus performante que l'étape de l'Agent si l'on en juge par la précision de ses prédictions et les améliorations qu'elle apporte au fil du temps.

## Fonctionnalités

Les fonctionnalités des agents de Braze sont les suivantes :

- **Configuration flexible :** Utilisez un LLM fourni par Braze ou connectez votre propre fournisseur de modèle (comme OpenAI, Anthropic, Google Gemini ou AWS Bedrock).
- **Intégration fluide/sans heurts :** Déployez des agents directement dans les étapes du canvas ou les champs du catalogue.
- **Outils de test et d'enregistrement :** Prévisualisez le résultat de votre agent en le testant avec des échantillons d'entrées avant de le lancer. Consultez les journaux à chaque fois que l'agent s'exécute, y compris les données d'entrée et de sortie pour cette exécution.
- **Contrôle de l'utilisation :** Les limites journalières permettent de gérer les performances et les coûts.

## À propos des agents de Braze

Les agents sont configurés avec des instructions (invites du système) qui définissent leur comportement. Lorsqu'un agent s'exécute, il utilise vos instructions ainsi que les données que vous lui transmettez pour générer une réponse. 

### Concepts clés

| Terme | Définition |
| --- | --- |
| [Modèle :]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#models) | Le "cerveau" de l'agent, en l'occurrence un grand modèle linguistique (LLM). Il interprète les entrées, génère des réponses et effectue des raisonnements. Un modèle plus solide (formé sur des données plus pertinentes) rend l'agent plus capable et plus polyvalent. |
| [Instructions]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#writing-instructions) | Les règles ou directives que vous donnez à l'agent (invite du système). Ils définissent le comportement de l'agent à chaque fois qu'il s'exécute. Des prédictions claires rendent l'agent plus fiable et plus prévisible. |
| Contexte | Données transmises à l'agent au moment de l'exécution, quel que soit l'endroit où il est déployé, telles que les champs du profil utilisateur ou les lignes du catalogue. Cette entrée fournit les informations que l'agent utilise pour générer des sorties. |
| [Variable de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#step-3-define-the-output-variable) | Le résultat produit par l'agent lorsqu'il est utilisé dans les étapes du canvas. Les variables de sortie stockent le résultat de l'agent pour personnaliser le contenu ou guider les chemins de flux de travail. Les variables de sortie peuvent être des chaînes de caractères, des nombres ou des données booléennes.  |
| [Exécution](#limitations) | Une seule exécution de l'agent. Cela est pris en compte dans vos limites journalières. |
| [Format de sortie]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format) | La structure de données prédéfinie de la réponse de l'agent. |
| [Température]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) | Le niveau d'écart pour la production de l'agent. Cela définit le degré de précision ou de créativité de votre agent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Restrictions

Pendant la période bêta, les limitations suivantes s'appliquent :

- Chaque agent a une limite d'exécution quotidienne par défaut de 50 000 exécutions, qui peut être augmentée jusqu'à un maximum de 100 000 exécutions par jour.
- Par défaut, chaque exécution doit se terminer dans les 15 secondes. Après 15 secondes, l'agent renvoie une réponse `null` à l'endroit où il est utilisé. 
    - Si vos agents dépassent régulièrement le temps imparti, contactez votre gestionnaire de compte Braze pour augmenter cette limite.
- Les données d'entrée sont limitées à 25 Ko par demande. Les entrées plus longues sont tronquées.

## Étapes suivantes

Maintenant que vous connaissez les agents Braze, vous êtes prêt pour les étapes suivantes :

- [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Déployer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)

## Modèles de fournisseurs en tant que sous-traitants secondaires ou fournisseurs tiers

Lorsque le Client utilise une intégration avec des modèles fournis par Braze par le biais des Services de Braze (" LLM fourni par Braze "), les fournisseurs de ces LLM fournis par Braze agiront en tant que Sous-traitants de Braze, sous réserve des termes de l'Addendum au traitement des données (DPA) entre le Client et Braze. 

Si le Client choisit d'apporter sa propre clé API pour s'intégrer aux fonctionnalités de l'intelligence artificielle de Braze, le fournisseur de l'abonnement LLM du Client sera considéré comme un Fournisseur tiers, tel que défini dans le contrat entre le Client et Braze. 

### Comment mes données sont-elles utilisées et envoyées aux centres d'éducation et de formation tout au long de la vie fournis par Braze ?

Afin de générer une sortie d'intelligence artificielle par le biais des fonctionnalités d'intelligence artificielle de Braze que Braze identifie comme exploitant les LLM fournis par Braze ("Sortie"), Braze enverra votre invite système ou toute autre entrée, selon le cas ("Entrée"), au LLM fourni par Braze. Les données envoyées au LLM applicable fourni par Braze ne sont pas utilisées pour former ou améliorer le LLM fourni par Braze. Entre vous et Braze, le produit est votre propriété intellectuelle. Braze ne revendiquera pas la propriété des droits d'auteur sur ces sorties. Braze n'offre aucune garantie de quelque nature que ce soit en ce qui concerne le contenu généré par l'intelligence artificielle en général, y compris la sortie.

Le LLM fourni par Braze pour les agents de Braze, identifié comme "Auto", utilise les modèles de Google Gemini. Google conserve les entrées et sorties soumises par l'intermédiaire de Braze pendant 55 jours, après quoi les données sont supprimées.
