---
nav_title: Agent
article_title: "Étape de l'agent"
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "Cet article de référence traite de l'utilisation de l'étape du canvas Agent pour générer du contenu ou prendre des décisions intelligentes en temps réel."
tool: Canvas
toc_headers: h2
---

# Étape de l'agent  

> L'étape du canvas vous permet d'ajouter la prise de décision et la génération de contenu basées sur l'intelligence artificielle directement dans votre flux de travail Canvas. Pour plus d'informations générales, consultez la section [Agents de Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Une étape de l'agent dans le parcours de l'utilisateur de Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Fonctionnement

Lorsqu'un utilisateur atteint une étape de l'agent dans un canvas, Braze envoie les données d'entrée que vous avez configurées (contexte complet ou champs sélectionnés) à l'agent de votre choix. L'agent traite ensuite l'entrée à l'aide de son modèle et de ses instructions, et renvoie une sortie. Ce résultat est stocké dans la variable de sortie que vous avez définie dans l'étape.

Vous pouvez ensuite utiliser cette variable de deux manières principales :

- **Prise de décision :** Acheminez les utilisateurs vers différents canvas en fonction de la réponse de l'agent. Par exemple, un agent d'évaluation des prospects peut renvoyer un nombre compris entre 1 et 10. Vous pouvez utiliser ce score pour décider de poursuivre l'envoi de messages à un utilisateur ou de l'abandonner.
- **Personnalisation :** Insérer la réponse de l'agent directement dans un message. Par exemple, un agent pourrait analyser les commentaires des clients et générer un e-mail de suivi empathique qui fait référence au commentaire du client et propose une résolution.

## Création d'une étape pour l'agent

### Étape 1 : Ajouter une étape

Glissez-déposez le composant **Agent** depuis la barre latérale ou cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus au bas d'une étape et sélectionnez **Agent**.  

### Étape 2 : Sélectionnez votre agent  

Sélectionnez l'agent qui traitera les données au cours de cette étape. Choisissez un agent existant ou créez-en un nouveau directement à partir de cette étape. Pour des conseils sur la configuration, voir [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Étape 3 : Définir la variable de sortie

Les sorties de l'agent sont appelées "variables de sortie" et sont stockées dans une [variable de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) pour en faciliter l'accès. Pour définir la variable de sortie :

1. Donnez un nom à la variable.
2. Sélectionnez un type de données. 

Les sorties de l'agent peuvent être enregistrées sous forme de chaînes de caractères, de nombres, de booléens ou d'objets. Cela les rend flexibles à la fois pour la personnalisation du texte et pour la logique conditionnelle dans votre Canvas. Voici quelques utilisations courantes de chaque type :

| Type de données | Utilisations courantes |
| --- | --- |
| Chaîne de caractères | Personnalisation des messages (ligne d'objet, texte, réponses) |
| Nombre | Notation, seuils, routage dans les [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Valeur booléenne | Oui/Non à l'embranchement dans les [arbres décisionnels]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Objet | Exploitez un ou plusieurs des types de données ci-dessus avec un seul appel LLM dans une structure de données prévisible. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Une fois définie, vous pouvez utiliser une variable de sortie dans tout le Canvas en utilisant la même syntaxe de modèle que pour une variable de contexte. Vous pouvez soit utiliser le filtre de segmentation **Context Variable**, soit modeler les réponses des agents directement à l'aide de Liquid : {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Pour utiliser une propriété spécifique d'une variable de sortie d'objet, utilisez la notation par points pour accéder à cette propriété à l'aide de Liquid : {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Étape de l'agent pour Body HTML Writer avec une sortie de type de données objet pour la variable "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

Utilisez les modèles de syntaxe Liquid présentés ci-dessus pour faire référence à des champs particuliers de la sortie de l'agent dans les étapes Canvas à venir.

### Étape 4 : Décider du contexte à fournir à l'agent  

Vous devez décider des données que l'agent doit recevoir au moment de l'exécution. Les options suivantes sont disponibles :  

- **Incluez tout le contexte des toiles :** Transmettez toutes les variables de contexte Canvas disponibles (telles que les [propriétés d'entrée Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)) à l'étape de l'agent. Vous pouvez utiliser les étapes de Contexte en amont des étapes de l'agent pour ajouter davantage de données à Contexte avant celui-ci.
- **Fournir des valeurs :** Ne transmettez que les propriétés sélectionnées, telles que le prénom ou la couleur préférée d'un utilisateur. Choisissez cette option pour ne donner à l'agent que l'accès aux valeurs que vous attribuez ici. Pour chaque **clé**, saisissez l'[étiquette Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) qui définit le champ spécifique du profil utilisateur ou la variable contextuelle.  

{% alert note %}
Braze transmet les 10 premiers Ko de contenu à l'agent. La fourniture de valeurs dont la valeur totale dépasse 10 Ko entraîne une troncature.
{% endalert %}

### Étape 5 : Testez l'agent

Après avoir configuré votre étape Agent, vous pouvez tester et prévisualiser le résultat de cette étape.

## Gestion des erreurs  

- Si le modèle connecté renvoie une erreur de limite de débit, Braze effectue jusqu'à cinq tentatives avec des délais exponentiels.  
- Si l'agent échoue pour une autre raison (telle qu'une clé API non valide), la variable de sortie prend la valeur `null`.
    - Si un agent atteint sa limite d'invocation quotidienne, la variable de sortie est fixée à `null`. Si vous utilisez l'envoi d'un agent dans une étape de message, pensez à utiliser la logique d'abandon du liquide.
- Les réponses sont mises en cache pour des entrées identiques et peuvent être réutilisées pour des invocations identiques répétées en l'espace de quelques minutes.
    - Les réponses qui utilisent des valeurs mises en cache sont toujours prises en compte dans le nombre total d'invocations et dans le nombre d'invocations quotidiennes.

## Analyse  

Reportez-vous aux indicateurs suivants pour suivre les performances de vos étapes d'agent :  

| Indicateurs | Description |
| --- | --- |
| _Saisie_ | Nombre de fois où les utilisateurs sont entrés dans l'étape Agent. |
| _A poursuivi vers l’étape suivante_ | Le nombre d'utilisateurs qui sont passés à l'étape suivante du flux après avoir franchi l'étape de l'agent. |
| _Utilisateurs sortis du canvas_ | Le nombre d'utilisateurs qui ont quitté le canvas après avoir franchi l'étape de l'agent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Foire aux questions

### Quand dois-je utiliser une étape d'agent ?

En général, nous recommandons l'utilisation d'une étape d'agent lorsque vous souhaitez introduire des données contextuelles particulières dans un LLM et lui demander d'attribuer des variables contextuelles de Canvas de manière intelligente à une échelle impossible pour les humains.

Imaginons que vous envoyiez un message personnalisé pour recommander un nouveau parfum de glace à un utilisateur qui a déjà commandé du chocolat et de la fraise. Voici la différence entre l'utilisation d'une étape d'agent et les recommandations d'articles de l'intelligence artificielle :

- **Étape de l'agent :** Utilise les LLM pour prendre une décision qualitative sur ce que l'utilisateur pourrait vouloir sur la base des instructions et des points de données contextuelles donnés à l'agent. Dans cet exemple, une étape de l'agent pourrait recommander un nouveau parfum en se basant sur la possibilité que l'utilisateur veuille essayer différents parfums.
- **Recommandations sur les points de l'intelligence artificielle :** Utilise des modèles d'apprentissage automatique pour prédire les produits qu'un utilisateur est le plus susceptible de vouloir en fonction des événements utilisateurs passés, tels que les achats. Dans cet exemple, les recommandations d'articles de l'intelligence artificielle suggéreraient un parfum (vanille) en fonction des deux commandes précédentes de l'utilisateur (chocolat et fraise) et de leur comparaison avec les comportements des autres utilisateurs de votre espace de travail.

### Quand dois-je utiliser un format de sortie standard pour un agent ?

Nous vous recommandons d'utiliser le format de sortie lorsque vous souhaitez que l'agent renvoie une structure de données avec plusieurs valeurs définies de manière structurée, plutôt qu'une sortie à valeur unique. Cela permet à la sortie d'être mieux formatée en tant que variable contextuelle cohérente.

Par exemple, vous pouvez utiliser un format de sortie au sein d'un agent destiné à créer un exemple d'itinéraire de voyage pour un utilisateur sur la base d'un formulaire qu'il a soumis. Le format de sortie vous permet de définir que chaque réponse de l'agent doit contenir les valeurs `tripStartDate`, `tripEndDate` et `destination`. Chacune de ces valeurs peut être extraite des variables contextuelles et placée dans une étape d'envoi de messages pour la personnalisation à l'aide de Liquid.

### Comment les étapes de l'agent utilisent-elles les données d'entrée ?

Les étapes de l'agent utilisent des données contextuelles spécifiques qui sont [fournies à l'agent](#step-4-decide-what-context-to-provide-the-agent). 

Vous pouvez choisir de transmettre l'intégralité du contexte de Canvas à l'agent en tant que contexte, ou de transmettre des valeurs spécifiques à l'aide d'étiquettes Liquid dans le contexte de cette étape de l'agent. Vous pouvez également utiliser le contenu connecté comme valeur d'entrée dans une étape Agent.

## Articles connexes  

- [Aperçu des agents de Braze]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  