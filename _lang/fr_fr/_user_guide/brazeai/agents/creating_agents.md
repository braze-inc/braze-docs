---
nav_title: "Création d'agents"
article_title: "Création d'agents personnalisés"
description: "Apprenez à créer des agents, à les préparer avant de commencer et à les utiliser pour l'envoi de messages, la prise de décision et la gestion des données."
alias: /creating-agents/
---

# Création d'agents personnalisés

> Découvrez comment créer des agents personnalisés, ce qu'il faut préparer avant de commencer et comment les mettre en œuvre dans les domaines de l'envoi de messages, de la prise de décision et de la gestion des données. Pour plus d'informations générales, consultez la section [Agents de Braze]({{site.baseurl}}/user_guide/brazeai/agents). 

{% alert important %}
Les Braze Currents sont actuellement en version bêta. Pour obtenir de l'aide, contactez votre gestionnaire satisfaction client.
{% endalert %}

## Conditions préalables

Avant de commencer, vous aurez besoin des éléments suivants :

- Accès à la **console de l'agent** dans votre espace de travail. Vérifiez auprès de vos administrateurs Braze si vous ne voyez pas cette option.  
- Autorisations du client à créer et modifier des agents d'intelligence artificielle personnalisés. 
- Une idée de ce que vous voulez que l'agent accomplisse. Les agents Braze peuvent prendre en charge les actions suivantes :  
   - **Envoi de messages :** Générer des lignes d'objet, des titres, des textes dans les produits ou d'autres contenus.  
   - **Prise de décision :** Acheminez les utilisateurs dans Canvas en fonction de leur comportement, de leurs préférences ou d'attributs personnalisés.  
   - **Gestion des données :** Calculer des valeurs, enrichir les entrées du catalogue ou actualiser les champs du profil.  

## Comment cela fonctionne-t-il ?

Lorsque vous créez un agent, vous définissez son objectif et établissez des garde-fous sur la manière dont il doit se comporter. Une fois en ligne/en production/instantanée, l'agent peut être déployé dans Braze pour générer des textes personnalisés, prendre des décisions en temps réel ou mettre à jour les champs du catalogue. Vous pouvez mettre en pause ou actualiser un agent à tout moment depuis le tableau de bord.

## Créer un agent

Pour créer votre agent personnalisé :  

1. Dans le tableau de bord de Braze, accédez à **Console des agents** > **Gestion des agents**.  
2. Sélectionnez **Créer un agent**.  
3. Saisissez un nom et une description pour aider votre équipe à comprendre son objectif.  
4. Choisissez le [modèle](#models) que votre agent utilisera.  

!Interface de la console d'agent permettant de créer un agent personnalisé dans Braze. L'écran affiche des champs permettant de saisir le nom et la description de l'agent et de sélectionner un modèle.]( {% image_buster /assets/img/ai_agent/create_custom_agent.png %} )

5. Donnez des instructions à l'agent. Reportez-vous aux [instructions d'écriture](#writing-instructions) pour obtenir des conseils.
6. [Testez la](#testing-your-agent) sortie de l'[agent](#testing-your-agent) et ajustez les instructions si nécessaire.
7. Lorsque vous êtes prêt, sélectionnez **Créer un agent** pour activer l'agent. 

## Prochaine étape

Votre agent est maintenant prêt à l'emploi ! Pour plus d'informations, voir [Déploiement des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/). 

## Référence

### Modèles

Lorsque vous créez un agent, vous choisissez le modèle qu'il utilise pour générer des réponses. Vous avez deux possibilités :

#### Option 1 : Utilisez un modèle alimenté par la Braze

Il s'agit de l'option la plus simple, qui ne nécessite aucune configuration supplémentaire. Braze permet d'accéder directement aux grands modèles de langage (LLM). Pour utiliser cette option, sélectionnez **Auto.**

{% alert note %}
Si vous utilisez le LLM alimenté par Braze, vous n'aurez aucun coût à supporter pendant la période de bêta. L'invocation est limitée à 50 000 exécutions par jour et à 500 000 exécutions au total. Voir les [limitations]({{site.baseurl}}/user_guide/brazeai/agents/#limitations) pour plus de détails.
{% endalert %}

#### Option 2 : Apportez votre propre clé API

Grâce à cette option, vous pouvez connecter votre compte Braze à des fournisseurs tels qu'OpenAI, Anthropic, AWS Bedrock ou Google Gemini. Si vous apportez votre propre clé API d'un fournisseur de LLM, les coûts sont facturés directement par votre fournisseur, et non par Braze.

Pour mettre en place ce système :
1. Allez dans **Intégrations partenaires** > **Partenaires technologiques** et trouvez votre fournisseur.
2. Saisissez votre clé API fournie par le fournisseur.
3. Sélectionnez **Enregistrer**.

Ensuite, vous pouvez retourner chez votre agent et sélectionner votre modèle.

### Instructions de rédaction

Les instructions sont les règles ou les directives que vous donnez à l'agent (invite du système). Ils définissent le comportement de l'agent à chaque fois qu'il s'exécute. Les instructions du système peuvent contenir jusqu'à 10 Ko.

{% tabs %}
{% tab Best practices %}

Voici quelques bonnes pratiques générales pour vous aider à commencer à utiliser les messages-guides :

1. Commencez en pensant à la fin. Énoncez d'abord l'objectif.
2. Donnez au modèle un rôle ou un personnage ("Vous êtes un ...").
3. Définissez clairement le contexte et les contraintes (audience, longueur, ton, format).
4. Demandez une structure ("Retournez JSON/liste de puces/tableau...").
5. Montrez, ne dites pas. Incluez quelques exemples de qualité.
6. Décomposer les tâches complexes en étapes ordonnées ("Étape 1... Étape 2...").
7. Encouragez le raisonnement ("Réfléchissez à haute voix, puis répondez").
8. Pilotez, inspectez et itérez. De petites modifications peuvent conduire à des gains de qualité importants.
9. Traitez les cas particuliers, ajoutez des garde-fous et des instructions de refus.
10. Mesurez et documentez ce qui fonctionne en interne afin de le réutiliser et de l'étendre.

Pour plus de détails sur les meilleures pratiques en matière d'incitation, consultez les guides des fournisseurs de modèles suivants :

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropique](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gémeaux](https://support.google.com/a/users/answer/14200040?hl=en)

{% endtab %}
{% tab Examples %}

{% details Simple prompt %}

Cet exemple d'invite prend une enquête en entrée et produit une simple analyse des sentiments :

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

{% enddetails %}

{% details Complex prompt %}

Cet exemple d'invite reprend les données d'une enquête réalisée par un utilisateur et les classe en une seule étiquette de sentiment. Le résultat peut ensuite être utilisé pour orienter les utilisateurs vers différents chemins Canvas (tels que les commentaires positifs par rapport aux commentaires négatifs) ou stocker le sentiment en tant qu'attribut personnalisé sur leur profil pour un ciblage ultérieur.

{% raw %}
```
You are a customer research AI for a retail brand.  
Input: one open-text survey response from a user.  
Output: A single structured JSON object with:  
- sentiment (Positive, Neutral, Negative)  
- topic (Product, Delivery, Price, Other)  
- action_recommendation (Route: High-priority follow-up | Low-priority follow-up | No action)  

Rules:  
- Always return valid JSON.  
- If the topic is unclear, default to Other.  
- If sentiment is mixed, default to Neutral.  
- If sentiment is Negative and topic = Product or Delivery → action_recommendation = High-priority follow-up.  
- Otherwise, action_recommendation = Low-priority follow-up.  

Example Input:  
"The product works great, but shipping took forever and the cost felt too high."  

Example Output:  
{  
  "sentiment": "Neutral",  
  "topic": "Delivery",  
  "action_recommendation": "High-priority follow-up"  
}  
```
{% endraw %}
{% enddetails %}

{% endtab %}
{% endtabs %}


#### Tester votre agent  

La ligne/en **production/instantanée** est une instance de l'agent qui s'affiche comme un panneau côte à côte dans l'expérience de configuration. Vous pouvez l'utiliser pour tester l'agent pendant que vous le créez ou que vous le mettez à jour, afin d'en faire l'expérience de la même manière que les utilisateurs finaux. Cette étape vous permet de confirmer qu'il se comporte comme vous le souhaitez et vous donne l'occasion de le peaufiner avant qu'il ne soit mis en ligne/en production/instantané.

La console d'agent affiche le volet de prévisualisation instantanée pour tester un agent personnalisé. L'interface affiche un champ Exemple d'entrées avec des données personnalisées, un bouton Exécuter le test et une zone de réponse où apparaît le résultat de l'agent.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. Dans le champ **Exemples de données**, saisissez des exemples de données ou de réponses de clients, c'est-à-dire tout ce qui reflète les scénarios réels auxquels votre agent sera confronté. 
2. Sélectionnez **Exécuter le test**. L'agent s'exécutera en fonction de votre configuration et affichera sa réponse. Les tests sont pris en compte dans votre limite quotidienne et totale d'invocations.

Examinez les résultats avec un œil critique. Réfléchissez aux questions suivantes :

- Le texte est-il conforme à la marque ? 
- La logique décisionnelle achemine-t-elle les clients comme prévu ? 
- Les valeurs calculées sont-elles exactes ? 

Si vous avez l'impression que quelque chose ne va pas, mettez à jour la configuration de l'agent et testez à nouveau. Exécutez quelques entrées différentes pour voir comment l'agent s'adapte aux différents scénarios, en particulier aux cas extrêmes tels que l'absence de données ou les réponses non valides.

