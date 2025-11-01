---
nav_title: Agent
article_title: "Étape de l'agent"
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "Cet article de référence traite de l'utilisation de l'étape du canvas Agent pour générer du contenu ou prendre des décisions intelligentes en temps réel."
tool: Canvas
---

# Étape de l'agent  

> L'étape du canvas vous permet d'ajouter la prise de décision et la génération de contenu basées sur l'intelligence artificielle directement dans votre flux de travail Canvas. Pour plus d'informations générales, consultez la section [Agents de Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

Une étape du canvas dans le parcours de l'utilisateur.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Comment cela fonctionne-t-il ?

Lorsqu'un utilisateur atteint une étape de l'agent dans un canvas, Braze envoie les données d'entrée que vous avez configurées (contexte complet ou champs sélectionnés) à l'agent de votre choix. L'agent traite ensuite l'entrée à l'aide de son modèle et de ses instructions, et renvoie une sortie. Ce résultat est stocké dans la variable de sortie que vous avez définie dans l'étape.

Vous pouvez ensuite utiliser cette variable de deux manières principales :

- **Prise de décision :** Acheminer les utilisateurs vers différents canvas en fonction de la réponse de l'agent. Par exemple, un agent d'évaluation des prospects peut renvoyer un nombre compris entre 1 et 10. Vous pouvez utiliser ce score pour décider de poursuivre l'envoi de messages à un utilisateur ou de l'abandonner.
- **Personnalisation :** Insérez la réponse de l'agent directement dans un message. Par exemple, un agent pourrait analyser les commentaires des clients et générer un e-mail de suivi empathique qui fait référence au commentaire du client et propose une résolution.

## Création d'une étape pour l'agent

### Étape 1 : Ajouter une étape

Glissez-déposez le composant **Agent** depuis la barre latérale ou cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus au bas d'une étape et sélectionnez **Agent**.  

### Étape 2 : Sélectionnez votre agent  

Sélectionnez l'agent qui traitera les données au cours de cette étape. Choisissez un agent existant ou créez-en un nouveau directement à partir de cette étape. Pour des conseils sur la configuration, voir [Création d'agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Étape 3 : Définir la variable de sortie

Les sorties de l'agent sont appelées "variables de sortie" et sont stockées dans une [variable de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) pour en faciliter l'accès. Pour définir la variable de sortie :

1. Donnez un nom à la variable.
2. Sélectionnez un type de données. 

Les sorties de l'agent peuvent être enregistrées sous forme de chaînes de caractères, de nombres ou de booléens. Cela les rend flexibles à la fois pour la personnalisation du texte et pour la logique conditionnelle dans votre Canvas. Voici quelques utilisations courantes de chaque type :

| Type de données | Utilisations courantes |
| --- | --- |
| Chaîne de caractères | Personnalisation des messages (ligne d'objet, texte, réponses) |
| Nombre | Notation, seuils, routage dans les [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Booléen | Oui/Non à l'embranchement dans les [arbres décisionnels]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Une fois définie, vous pouvez utiliser une variable de sortie dans tout le Canvas en utilisant la même syntaxe de modèle que pour une variable de contexte. Vous pouvez soit utiliser le filtre de segmentation **Context Variable**, soit modeler les réponses de l'agent directement à l'aide de Liquid : {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

### Étape 4 : Décider du contexte à fournir à l'agent  

Vous devez décider des données que l'agent doit recevoir au moment de l'exécution. Les options suivantes sont disponibles :  

- **Incluez tout le contexte des toiles :** Transmet toutes les variables de contexte Canvas disponibles (telles que les [propriétés d'entrée Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)) et tout autre contexte qui lui a été attribué par le biais des étapes du canvas.  
- **Fournir des valeurs :** Ne transmettez que les propriétés sélectionnées, telles que le prénom ou la couleur préférée d'un utilisateur. Choisissez cette option pour que l'agent n'ait accès qu'aux valeurs que vous attribuez ici. Pour chaque **clé**, saisissez l'[étiquette Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) qui définit le champ spécifique du profil utilisateur ou la variable contextuelle.  

{% alert note %}
Braze ne transmet à l'agent que les 10 premiers Ko du contenu. La fourniture de valeurs dont la valeur totale est supérieure à 10 Ko entraînera une troncature. Pour aider à enregistrer les coûts, les agents Braze dans Canvas utilisent des caches à courte durée de vie pour les réponses LLM pour des entrées identiques. L'inclusion de tous les Canvas Context augmente la probabilité que les résultats mis en cache ne puissent pas être utilisés, ce qui pourrait augmenter les coûts de votre LLM.
{% endalert %}

## Gestion des erreurs  

- Si le modèle connecté renvoie une erreur de limite de débit, Braze effectue jusqu'à cinq tentatives avec des délais exponentiels.  
- Si l'agent échoue pour une autre raison (telle qu'une clé API non valide), la variable de sortie prend la valeur `null`.  
- Les réponses sont mises en cache pour les entrées identiques afin de réduire les invocations répétées.  

## Analyse/analytique (si utilisé comme adjectif)  

Reportez-vous aux indicateurs suivants pour suivre les performances de vos étapes d'agent :  

| Indicateurs | Description |
| --- | --- |
| _Entré_ | Nombre de fois où les utilisateurs sont entrés dans l'étape Agent. |
| _Passage à l'étape suivante_ | Le nombre d'utilisateurs qui sont passés à l'étape suivante du flux après avoir franchi l'étape de l'agent. |
| _Exited Canvas_ | Le nombre d'utilisateurs qui ont quitté le canvas après avoir franchi l'étape de l'agent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Articles connexes  

- [Aperçu des agents de Braze]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Création d'agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Déploiement d'agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  