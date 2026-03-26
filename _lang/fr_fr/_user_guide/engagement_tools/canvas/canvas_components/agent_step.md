---
nav_title: Agent
article_title: "Étape Agent"
alias: /agent_step/
page_order: 2
page_type: reference
description: "Cet article de référence explique comment utiliser l'étape Agent dans Canvas pour générer du contenu ou prendre des décisions intelligentes en temps réel."
tool: Canvas
toc_headers: h2
---

# Étape Agent  

> L'étape Agent vous permet d'intégrer directement dans votre flux de travail Canvas la prise de décision et la génération de contenu basées sur l'intelligence artificielle. Pour en savoir plus, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Une étape Agent dans un parcours utilisateur Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Fonctionnement

Lorsqu'un utilisateur atteint une étape Agent dans un Canvas, Braze transmet les données d'entrée que vous avez configurées (contexte complet ou champs sélectionnés) à l'agent de votre choix. L'agent traite ensuite ces données à l'aide de son modèle et de ses instructions, puis renvoie une sortie. Cette sortie est enregistrée dans la variable de sortie que vous avez définie dans l'étape.

Vous pouvez ensuite utiliser cette variable de trois manières principales :

- **Prise de décision :** Orientez les utilisateurs vers différents chemins Canvas en fonction de la réponse de l'agent. Par exemple, un agent de notation des prospects peut renvoyer un nombre compris entre 1 et 10. Vous pouvez utiliser ce score pour décider de continuer à envoyer des messages à un utilisateur ou de l'exclure du parcours.
- **Personnalisation :** Insérez la réponse de l'agent directement dans un message. Par exemple, un agent pourrait analyser les commentaires des clients et générer un e-mail de suivi empathique qui fait référence au commentaire du client et propose une solution.
- **Traitement des données utilisateur :** Analysez et normalisez vos données utilisateur, puis enregistrez-les dans le profil utilisateur ou envoyez-les via un webhook. Par exemple, un agent pourrait renvoyer un score de sentiment ou une attribution d'affinité produit. Vous pouvez enregistrer ces données dans un profil utilisateur pour une utilisation ultérieure.

## Prérequis

Les étapes Agent utilisent [les variables de contexte Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) pour ingérer le contexte pertinent et générer une variable exploitable dans le Canvas.

## Création d'une étape Agent

### Étape 1 : Ajouter une étape

Glissez-déposez le composant **Agent** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et choisissez **Agent**.  

### Étape 2 : Choisir votre agent  

Sélectionnez l'agent qui traitera les données au cours de cette étape. Choisissez un agent existant. Pour obtenir des conseils sur la configuration, consultez [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Étape 3 : Définir la sortie de votre agent {#define-the-output-variable}

Les sorties de l'agent sont appelées « variables de sortie » et sont stockées dans une [variable de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) pour faciliter leur accès. Pour définir la variable de sortie, attribuez-lui un nom.

Le type de données de la variable de sortie est défini depuis la [console Agent]({{site.baseurl}}/user_guide/brazeai/agents). Les résultats de l'agent peuvent être enregistrés sous forme de chaînes de caractères, de nombres, de valeurs booléennes ou d'objets. Cela leur confère une grande flexibilité, aussi bien pour la personnalisation du texte que pour la logique conditionnelle dans votre Canvas. Voici quelques utilisations courantes pour chaque type :

| Type de données | Utilisations courantes |
| --- | --- |
| Chaîne de caractères | Personnalisation des messages (lignes d'objet, texte, réponses) |
| Nombre | Notation, seuils, routage dans [les parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Valeur booléenne | Branchement Oui/Non dans [les arbres décisionnels]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Objet | Exploitez un ou plusieurs des types de données ci-dessus avec un seul appel LLM dans une structure de données prévisible |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Vous pouvez utiliser une variable de sortie dans l'ensemble du Canvas en employant la même syntaxe de modèle que pour une variable de contexte. Utilisez le filtre de segment **Variable de contexte**, ou intégrez directement les réponses de l'agent à l'aide de Liquid : {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Pour accéder à une propriété spécifique d'une variable de sortie de type objet, utilisez la notation par points avec Liquid : {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Étape Agent pour Body HTML Writer avec une sortie de type objet pour la variable « agent_output ».]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Étape 4 : Ajouter du contexte supplémentaire (facultatif)

Vous pouvez inclure des valeurs de contexte supplémentaires auxquelles l'étape Agent pourra se référer lors de son exécution. Vous pouvez saisir toutes les valeurs Liquid que vous utiliseriez normalement dans un Canvas.

{% alert note %}
L'agent reçoit déjà automatiquement le contexte configuré dans la section **Instructions**. Les variables Liquid déjà configurées à cet endroit n'ont pas besoin d'être saisies à nouveau ici.
{% endalert %}

![La possibilité d'ajouter du contexte supplémentaire à une étape Agent à l'aide de Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Étape 5 : Tester l'agent

Après avoir configuré votre étape Agent, vous pouvez tester et prévisualiser le résultat de cette étape.

![Prévisualisez la sortie de l'agent en tant qu'utilisateur aléatoire.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Gestion des erreurs  

- Si le modèle connecté renvoie une erreur de limite de débit, Braze effectue jusqu'à cinq nouvelles tentatives avec des délais exponentiels.  
- Si l'agent échoue pour toute autre raison (délai d'attente dépassé, clé API non valide, etc.), la variable de sortie est définie sur `null`.
    - Si un agent atteint sa limite quotidienne d'invocations, la variable de sortie est définie sur `null`. 
- Utilisez [les valeurs Liquid par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values) pour vous prémunir contre les erreurs. Par exemple, dans la boîte de dialogue modale **Ajouter une personnalisation**, vous pouvez saisir une valeur Liquid par défaut telle que {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} ou {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Les réponses sont mises en cache pour les entrées identiques et peuvent être réutilisées pour des invocations identiques répétées dans les minutes qui suivent.
    - Les réponses utilisant des valeurs mises en cache sont toujours comptabilisées dans le nombre total et quotidien d'invocations.
- Les étapes Agent peuvent nécessiter un certain temps pour traiter un grand nombre d'utilisateurs. Si vous constatez que des utilisateurs sont encore en attente à cette étape, vérifiez vos journaux pour vous assurer que les invocations sont bien en cours.

## Analyse  

Consultez les indicateurs suivants pour suivre les performances de vos étapes Agent :  

| Indicateur | Description |
| --- | --- |
| _Entrées_ | Le nombre de fois où des utilisateurs ont accédé à l'étape Agent. |
| _A poursuivi vers l'étape suivante_ | Le nombre d'utilisateurs ayant poursuivi vers l'étape suivante du flux après avoir franchi l'étape Agent. |
| _Sortie du Canvas_ | Le nombre d'utilisateurs ayant quitté le Canvas après avoir franchi l'étape Agent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Foire aux questions

### Quand utiliser une étape Agent ?

De manière générale, nous recommandons d'utiliser une étape Agent lorsque vous souhaitez fournir des données contextuelles spécifiques à un LLM et lui faire attribuer intelligemment une variable de contexte Canvas, à une échelle impossible à atteindre manuellement.

Supposons que vous envoyiez un message personnalisé pour recommander un nouveau parfum de crème glacée à un client qui a précédemment commandé chocolat et fraise. Voici la différence entre l'utilisation d'une étape Agent et les recommandations d'articles par l'intelligence artificielle :

- **Étape Agent :** Utilise des LLM pour prendre une décision qualitative sur ce que l'utilisateur pourrait souhaiter, en fonction des instructions et des points de donnée contextuels fournis à l'agent. Dans cet exemple, une étape Agent pourrait recommander un nouveau parfum en partant du principe que l'utilisateur souhaite peut-être essayer quelque chose de différent.
- **Recommandations d'articles par l'intelligence artificielle :** Utilise des modèles de machine learning pour prédire les produits qu'un utilisateur est le plus susceptible de vouloir, en fonction de ses événements passés (comme ses achats). Dans cet exemple, les recommandations d'articles suggéreraient un parfum (vanille) en se basant sur les deux dernières commandes de l'utilisateur (chocolat et fraise) et sur leur comparaison avec les comportements des autres utilisateurs de votre espace de travail.

### Comment les étapes Agent utilisent-elles les données d'entrée ?

Une étape Agent analyse les données contextuelles que l'agent est configuré pour utiliser, ainsi que tout contexte supplémentaire [fourni à l'agent](#step-4-add-any-additional-context-optional).

## Articles connexes  

- [Aperçu des agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
- [Article de référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)