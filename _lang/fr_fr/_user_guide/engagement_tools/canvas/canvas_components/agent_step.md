---
nav_title: Agent
article_title: "Étape de l'agent"
alias: /agent_step/
page_order: 2
page_type: reference
description: "Cet article de référence explique comment utiliser l'étape Agent dans Canvas pour générer du contenu ou prendre des décisions intelligentes en temps réel."
tool: Canvas
toc_headers: h2
---

# Étape de l'agent  

> L'étape Agent vous permet d'intégrer directement dans votre flux de travail Canvas la prise de décision et la génération de contenu basées sur l'intelligence artificielle. Pour obtenir des informations générales, veuillez consulter [la section Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Une étape Agent dans le parcours utilisateur Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Fonctionnement

Lorsqu'un utilisateur atteint l'étape Agent dans un Canvas, Braze transmet les données d'entrée que vous avez configurées (contexte complet ou champs sélectionnés) à l'agent de votre choix. L'agent traite ensuite les données d'entrée à l'aide de son modèle et de ses instructions, puis renvoie une sortie. Cette sortie est enregistrée dans la variable de sortie que vous avez définie à l'étape.

Vous pouvez ensuite utiliser cette variable de trois manières principales :

- **Prise de décision :** Dirigez les utilisateurs vers différents chemins canvas en fonction de la réponse de l'agent. Par exemple, un agent de notation des prospects peut renvoyer un nombre compris entre 1 et 10. Vous pouvez utiliser ce score pour décider de continuer à effectuer l'envoi de messages à un utilisateur ou de l'exclure du parcours.
- **Personnalisation :** Veuillez insérer la réponse de l'agent directement dans un message. Par exemple, un agent pourrait analyser les commentaires des clients et générer un e-mail de suivi empathique qui fait référence au commentaire du client et propose une solution.
- **Traitement des données utilisateur :** Veuillez analyser et normaliser vos données utilisateur, puis les enregistrer dans le profil utilisateur ou les envoyer à l'aide d'un webhook. Par exemple, un agent pourrait renvoyer une note de sentiment ou une attribution d'affinité avec un produit. Vous pouvez enregistrer ces données dans un profil utilisateur pour une utilisation ultérieure.

## Prérequis

Les étapes de l'agent utilisent [les variables de contexte canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) pour ingérer le contexte pertinent et générer une variable pouvant être exploitée dans canvas.

## Création d'une étape Agent

### Étape 1 : Ajouter une étape

Veuillez glisser-déposer le composant **Agent** depuis la barre latérale ou sélectionner le bouton<i class="fas fa-plus-circle"></i> plus en bas d'une étape et choisir **Agent**.  

### Étape 2 : Choisissez votre agent  

Sélectionnez l'agent qui traitera les données au cours de cette étape. Veuillez sélectionner un agent existant. Pour obtenir des conseils sur la configuration, veuillez consulter [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Étape 3 : Définissez la sortie de votre agent {#define-the-output-variable}

Les sorties de l'agent sont appelées « variables de sortie » et sont stockées dans une [variable de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) pour faciliter leur accès. Pour définir la variable de sortie, veuillez attribuer un nom à la variable.

Veuillez noter que le type de données de la variable de sortie est défini à partir de la [console de l'agent]({{site.baseurl}}/user_guide/brazeai/agents). Les résultats de l'agent peuvent être enregistrés sous forme de chaînes de caractères, de nombres, de booléens ou d'objets. Cela leur confère une grande flexibilité pour la personnalisation du texte et la logique conditionnelle dans votre Canvas. Voici quelques utilisations courantes pour chaque type :

| Type de données | Utilisations courantes |
| --- | --- |
| Chaîne de caractères | Personnalisation des messages (lignes d'objet, texte, réponses) |
| Nombre | Notation, seuils, routage dans [les parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Valeur booléenne | Branchement Oui/Non dans [les arbres décisionnels]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Objet | Exploitez un ou plusieurs des types de données ci-dessus à l'aide d'un seul appel LLM dans une structure de données prévisible. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Vous pouvez utiliser une variable de sortie dans l'ensemble du canvas en employant la même syntaxe de modèle que pour une variable de contexte. Veuillez utiliser le filtre de segment **Variable de contexte** ou modéliser directement les réponses de l'agent à l'aide de Liquid :{% raw %}`{{context.${response_variable_name}}}` {% endraw %} .

Pour utiliser une propriété spécifique d'une variable de sortie d'objet, veuillez utiliser la notation par points pour accéder à cette propriété à l'aide de liquid : {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Étape d'agent pour Body HTML Writer avec une sortie de type de données objet pour la variable/assets/img/ai_agent/test_agent_step.pngimage_buster"agent_output".]({%%}){: style="max-width:80%;"}

### Étape 4 : Veuillez ajouter tout contexte supplémentaire (facultatif)

Vous pouvez choisir d'inclure des valeurs de contexte supplémentaires auxquelles l'agent pourra se référer lors de son exécution. Vous pouvez saisir toutes les valeurs de modèle Liquid que vous utiliseriez normalement dans un canvas.

{% alert note %}
Veuillez noter que l'agent reçoit déjà automatiquement le contexte configuré dans la section **Instructions**. Les variables liquides qui ont déjà été configurées à cet endroit n'ont pas besoin d'être saisies à nouveau ici.
{% endalert %}

![La possibilité d'ajouter du contexte supplémentaire à une étape Agent à l'aide de Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Étape 5 : Veuillez tester l'agent.

Après avoir configuré votre étape Agent, vous pouvez tester et prévisualiser le résultat de cette étape.

![Prévisualisez la sortie de l'agent en tant qu'utilisateur aléatoire.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Gestion des erreurs  

- Si le modèle connecté renvoie une erreur de limite de débit, Braze effectue jusqu'à cinq tentatives supplémentaires avec des délais exponentiels.  
- Si l'agent échoue pour toute autre raison (telle qu'une erreur de délai d'attente ou une clé API non valide), la variable de sortie est définie sur `null`.
    - Si un agent atteint sa limite quotidienne d'invocations, la variable de sortie est définie sur `null`. Si vous utilisez la sortie d'un agent dans une étape Message, envisagez d'utiliser [les valeurs Liquid par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values).
- Les réponses sont mises en cache pour les entrées identiques et peuvent être réutilisées pour des invocations identiques répétées dans les minutes qui suivent.
    - Les réponses qui utilisent des valeurs mises en cache sont toujours comptabilisées dans le nombre total et quotidien d'invocations.

## Analyse  

Veuillez vous référer aux indicateurs suivants pour suivre les performances de vos agents :  

| Indicateurs | Description |
| --- | --- |
| _Saisie_ | Le nombre de fois où les utilisateurs ont accédé à l'étape Agent. |
| _A poursuivi vers l’étape suivante_ | Le nombre d'utilisateurs qui ont poursuivi vers l'étape suivante du flux après avoir franchi l'étape Agent. |
| _Utilisateurs sortis du canvas_ | Le nombre d'utilisateurs ayant quitté Canvas après avoir franchi l'étape Agent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Foire aux questions

### Quand dois-je utiliser une étape Agent ?

En général, nous recommandons d'utiliser une étape Agent lorsque vous souhaitez fournir des données contextuelles particulières à un LLM et lui demander d'attribuer intelligemment une variable de contexte Canvas à une échelle impossible pour les humains.

Supposons que vous envoyiez un message personnalisé pour recommander un nouveau parfum de crème glacée à un client qui a précédemment commandé des parfums chocolat et fraise. Voici la différence entre l'utilisation d'une étape Agent et les recommandations d'articles générées par l'intelligence artificielle :

- **Étape de l'agent :** Utilise des modèles linguistiques à grande échelle (LLM) pour prendre une décision qualitative sur ce que l'utilisateur pourrait souhaiter, en fonction des instructions et des points de donnée contextuels fournis à l'agent. Dans cet exemple, une étape Agent pourrait recommander une nouvelle saveur en fonction de la possibilité que l'utilisateur souhaite essayer différentes saveurs.
- **Recommandations d'articles par l'intelligence artificielle :** Utilise des modèles de machine learning pour prédire les produits qu'un utilisateur est le plus susceptible de vouloir en fonction de ses événements utilisateurs passés, tels que ses achats. Dans cet exemple, les recommandations d'articles basées sur l'intelligence artificielle suggéreraient une saveur (vanille) en fonction des deux dernières commandes de l'utilisateur (chocolat et fraise) et de leur comparaison avec les préférences des autres utilisateurs de votre espace de travail.

### Comment les étapes de l'agent utilisent-elles les données d'entrée ?

Une étape Agent analyse les données contextuelles que l'agent est configuré pour utiliser, ainsi que tout contexte supplémentaire qui [lui](#step-4-add-any-additional-context-optional) est [fourni](#step-4-add-any-additional-context-optional).

## Articles connexes  

- [Aperçu des agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
- [Référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)  