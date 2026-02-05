---
nav_title: Créer des agents
article_title: Créer des agents personnalisés
description: "Apprenez à créer des agents, à les préparer avant de commencer et à les utiliser pour l'envoi de messages, la prise de décision et la gestion des données."
alias: /creating-agents/
---

# Créer des agents personnalisés

> Découvrez comment créer des agents personnalisés, ce qu'il faut préparer avant de commencer et comment les mettre en œuvre dans les domaines de l'envoi de messages, de la prise de décision et de la gestion des données. Pour plus d'informations générales, consultez la section [Agents de Braze]({{site.baseurl}}/user_guide/brazeai/agents). 

{% alert important %}
Les Braze Currents sont actuellement en version bêta. Pour obtenir de l'aide, contactez votre gestionnaire satisfaction client.
{% endalert %}

## Conditions préalables

Avant de commencer, vous aurez besoin des éléments suivants :

- Accès à la **console de l'agent** dans votre espace de travail. Vérifiez auprès de vos administrateurs Braze si vous ne voyez pas cette option.  
- Autorisations du client à créer et modifier des agents d'intelligence artificielle personnalisés. 
- Une idée de ce que vous voulez que l'agent accomplisse. Les agents Braze peuvent prendre en charge les actions suivantes :  
   - **Envoi de messages :** Générez des lignes d'objet, des titres, des textes dans les produits ou d'autres contenus.  
   - **Prise de décision :** Acheminez les utilisateurs dans Canvas en fonction de leur comportement, de leurs préférences ou d'attributs personnalisés.  
   - **Gestion des données :** Calculer des valeurs, enrichir les entrées du catalogue ou actualiser les champs du profil.  

## Fonctionnement

Lorsque vous créez un agent, vous définissez son objectif et établissez des garde-fous sur la manière dont il doit se comporter. Une fois en ligne/en production/instantanée, l'agent peut être déployé dans Braze pour générer des textes personnalisés, prendre des décisions en temps réel ou mettre à jour les champs du catalogue. Vous pouvez mettre en pause ou actualiser un agent à tout moment depuis le tableau de bord.

Les cas d'utilisation suivants illustrent quelques façons d'exploiter les agents personnalisés.

| Cas d’utilisation | Description |
| --- | --- |
| Traitement du retour d'information des clients | Transmettez les commentaires des utilisateurs à un agent pour analyser les sentiments et générer des messages de suivi empathiques. Pour les utilisateurs de grande valeur, l'agent peut accélérer la réponse ou offrir des avantages. |
| Localiser le contenu | Traduisez le texte du catalogue dans une autre langue pour les campagnes mondiales, ou ajustez le ton et la longueur pour les canaux spécifiques à une région. Par exemple, traduisez "Classic Clubmaster Sunglasses" en espagnol par "Gafas de sol Classic Clubmaster", ou raccourcissez les descriptions pour les campagnes SMS. |
| Résumez les critiques ou le retour d'information | Résumez les sentiments ou les commentaires dans un nouveau champ, par exemple en attribuant des notes de sentiment comme Positif, Neutre ou Négatif, ou en créant un court résumé textuel comme "La plupart des clients mentionnent une bonne coupe, mais notent la lenteur de la livraison." |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Créer un agent

Pour créer votre agent personnalisé :  

1. Dans le tableau de bord de Braze, accédez à **Console des agents** > **Gestion des agents**.  
2. Sélectionnez **Créer un agent**.  
3. Saisissez un nom et une description pour aider votre équipe à comprendre son objectif.
4. Choisissez le [modèle](#models) que votre agent utilisera.  

![Interface de la console d'agent permettant de créer un agent personnalisé dans Braze. L'écran affiche des champs permettant de saisir le nom et la description de l'agent et de sélectionner un modèle.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Donnez des instructions à l'agent. Reportez-vous aux [instructions d'écriture](#writing-instructions) pour obtenir des conseils.
6\. [Testez la](#testing-your-agent) sortie de l'[agent](#testing-your-agent) et ajustez les instructions si nécessaire.
7\. Lorsque vous êtes prêt, sélectionnez **Créer un agent** pour activer l'agent. 

Votre agent est maintenant prêt à l'emploi ! Pour plus d'informations, voir [Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Modèles

Lorsque vous configurez un agent, vous pouvez choisir le modèle qu'il utilise pour générer des réponses. Vous avez deux possibilités : utiliser un modèle alimenté par Braze ou apporter votre propre clé API.

{% alert important %}
Lors de l'utilisation du modèle **Auto** alimenté par Braze, nous avons optimisé les modèles dont les capacités de réflexion sont suffisantes pour effectuer des tâches telles que la recherche d'un catalogue et l'appartenance à une segmentation d'utilisateurs. Si vous utilisez d'autres modèles, nous vous recommandons de faire des essais pour confirmer que votre modèle convient à votre cas d'utilisation. Il se peut que vous deviez ajuster vos [instructions](#writing-instructions) pour donner différents niveaux de détails ou de raisonnement étape par étape à des modèles ayant des vitesses et des capacités différentes.
{% endalert %}

### Option 1 : Utilisez un modèle alimenté par la Braze

Il s'agit de l'option la plus simple, qui ne nécessite aucune configuration supplémentaire. Braze permet d'accéder directement aux grands modèles de langage (LLM). Pour utiliser cette option, sélectionnez **Auto**, qui utilise les modèles Gemini.

### Option 2 : Apportez votre propre clé API

Grâce à cette option, vous pouvez connecter votre compte Braze à des fournisseurs tels qu'OpenAI, Anthropic, AWS Bedrock ou Google Gemini. Si vous apportez votre propre clé API d'un fournisseur de LLM, les coûts des jetons sont facturés directement par votre fournisseur, et non par Braze.

{% alert important %}
Nous vous recommandons de tester régulièrement les modèles les plus récents, car les anciens modèles peuvent être abandonnés ou obsolètes au bout de quelques mois.
{% endalert %}

Pour mettre en place ce système :

1. Allez dans **Intégrations partenaires** > **Partenaires technologiques** et trouvez votre fournisseur.
2. Saisissez votre clé API fournie par le fournisseur.
3. Sélectionnez **Enregistrer**.

Ensuite, vous pouvez retourner chez votre agent et sélectionner votre modèle.

{% alert important %}
Lorsque vous utilisez un LLM fourni par Braze, les fournisseurs d'un tel modèle agissent en tant que sous-traitants secondaires de Braze, sous réserve des conditions de l'addendum relatif au traitement des données (DPA) conclu entre vous et Braze. Si vous choisissez d'apporter votre propre clé API, le fournisseur de votre abonnement LLM est considéré comme un fournisseur tiers dans le cadre du contrat entre vous et Braze.  
{% endalert %}

## Instructions de rédaction

Les instructions sont les règles ou les directives que vous donnez à l'agent (invite du système). Ils définissent le comportement de l'agent à chaque fois qu'il s'exécute. Les instructions du système peuvent contenir jusqu'à 25 Ko.

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
10. Mesurez et documentez ce qui fonctionne en interne afin de pouvoir le réutiliser et l'étendre.

Nous vous recommandons d'inclure également une réponse par défaut comme réponse fourre-tout si l'agent reçoit une réponse qui ne peut pas être analysée. Ce traitement des erreurs permet à l'agent de vous informer d'une variable de résultat inconnue. Par exemple, plutôt que de demander à l'agent d'indiquer uniquement des valeurs de sentiment "positives" ou "négatives", demandez-lui d'indiquer "incertain" s'il n'arrive pas à se décider.

### Demande simple

Cet exemple d'invite prend une enquête en entrée et produit une simple analyse des sentiments :

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

### Invite complexe 

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

Pour plus de détails sur les meilleures pratiques en matière d'incitation, consultez les guides des fournisseurs de modèles suivants :

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropique](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gémeaux](https://support.google.com/a/users/answer/14200040?hl=en)

### Format de sortie

Utilisez le champ **Format de sortie** pour organiser et définir la sortie de l'agent en structurant manuellement les champs ou en utilisant JSON. 

- **Domaines :** Un moyen sans code d'imposer une sortie d'agent que vous pouvez utiliser de manière cohérente. 
- **JSON :** Une approche par code pour créer un format de sortie précis, où vous pouvez imbriquer des variables et des objets dans le schéma JSON.

#### Champs

Supposons que vous souhaitiez mettre en forme les réponses à une simple enquête de satisfaction afin de déterminer dans quelle mesure les personnes interrogées sont susceptibles de recommander le nouveau parfum de crème glacée de votre restaurant. Vous pouvez définir les champs suivants pour structurer le format de sortie :

| Nom du champ | Valeur
| --- | --- |
| **likelihood_score** | Nombre |
| **explication** | Texte |
| **confidence_score** | Nombre |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Console de l'agent montrant trois champs de sortie pour le score de vraisemblance, l'explication et le score de confiance.]( {% image_buster /assets/img/ai_agent/output_format_fields.png %} )

### Schéma JSON

Supposons que vous souhaitiez recueillir les commentaires des utilisateurs sur leur dernière expérience dans votre chaîne de restaurants. Vous pouvez sélectionner **JSON Schema** comme format de sortie et insérer le JSON suivant pour renvoyer un objet de données comprenant une variable de sentiment et une variable de raisonnement.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

Si vous essayez d'utiliser un agent avec une sortie JSON dans un catalogue, il ne suivra pas votre schéma. Pensez plutôt à utiliser les [champs de sortie définis](#fields).

{% alert important %}
Les formats de sortie ne sont pas actuellement pris en charge par l'intelligence artificielle de Claude. Si vous utilisez une clé Anthropic, nous vous recommandons d'ajouter manuellement la structure à l'invite de l'agent.
{% endalert %}

## Paramètres optionnels

### Lignes directrices de la marque

Vous pouvez sélectionner des [directives de marque]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) que votre agent devra respecter dans ses réponses. Par exemple, si vous souhaitez que votre agent génère un texte SMS pour encourager les utilisateurs à s'inscrire à une salle de sport, vous pouvez utiliser ce champ pour faire référence à votre ligne directrice prédéfinie, audacieuse et motivante.

### Catalogues

Choisissez des catalogues spécifiques pour qu'un agent puisse s'y référer et pour donner à votre agent le contexte dont il a besoin pour comprendre vos produits et d'autres données non liées à l'utilisateur, le cas échéant.

![Le catalogue "restaurants" et la colonne "Loyalty_Program" sont sélectionnés pour la recherche de l'agent.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

### Contexte d'appartenance à un segment

Vous pouvez sélectionner jusqu'à trois segments pour l'agent afin de croiser l'appartenance de chaque utilisateur à un segment lorsque l'agent est utilisé dans un Canvas. Supposons que l'appartenance de votre agent à un segment soit sélectionnée pour un segment "Utilisateurs fidèles" et que l'agent soit utilisé dans un canvas. Lorsque des utilisateurs entrent dans une étape de l'agent, ce dernier peut vérifier si chaque utilisateur est membre de chaque segment que vous avez spécifié dans la console de l'agent, et utiliser l'appartenance (ou la non-appartenance) de chaque utilisateur comme contexte pour le LLM.

![Le segment "Utilisateurs fidèles" est sélectionné pour l'accès à l'adhésion des agents.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

### Température

Si votre objectif est d'utiliser un agent pour générer un texte incitant les utilisateurs à se connecter à votre application mobile, vous pouvez fixer une température plus élevée pour que votre agent soit plus créatif et utilise les nuances des variables contextuelles. Si vous utilisez un agent pour générer des scores de sentiment, il peut être idéal de fixer une température plus basse afin d'éviter toute spéculation de l'agent sur les réponses négatives de l'enquête. Nous vous recommandons de tester ce paramètre et d'examiner les résultats générés par l'agent pour les adapter à votre scénario.

{% alert note %}
Les températures ne sont actuellement pas prises en charge par l'OpenAI.
{% endalert %}

## Testez votre agent

La ligne/en **production/instantanée** est une instance de l'agent qui s'affiche comme un panneau côte à côte dans l'expérience de configuration. Vous pouvez l'utiliser pour tester l'agent pendant que vous le créez ou que vous le mettez à jour, afin d'en faire l'expérience de la même manière que les utilisateurs finaux. Cette étape vous permet de confirmer qu'il se comporte comme vous le souhaitez et vous donne l'occasion de le peaufiner avant qu'il ne soit mis en ligne/en production/instantané.

![La console des agents affiche le volet de prévisualisation instantanée pour tester un agent personnalisé. L'interface affiche un champ Exemple d'entrées avec des données personnalisées, un bouton Exécuter le test et une zone de réponse où apparaît le résultat de l'agent.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. Dans le champ **Exemples de données**, saisissez des exemples de données ou de réponses de clients, c'est-à-dire tout ce qui reflète les scénarios réels auxquels votre agent sera confronté. 
2. Sélectionnez **Exécuter le test**. L'agent s'exécutera en fonction de votre configuration et affichera sa réponse. Les tests sont pris en compte dans votre limite d'exécution quotidienne.

Examinez les résultats avec un œil critique. Réfléchissez aux questions suivantes :

- Le texte est-il conforme à la marque ? 
- La logique décisionnelle achemine-t-elle les clients comme prévu ? 
- Les valeurs calculées sont-elles exactes ? 

Si vous avez l'impression que quelque chose ne va pas, mettez à jour la configuration de l'agent et testez à nouveau. Exécutez quelques entrées différentes pour voir comment l'agent s'adapte aux différents scénarios, en particulier aux cas extrêmes tels que l'absence de données ou les réponses non valides.

### Surveillez votre agent

Dans l'onglet **Logs** de votre agent, vous pouvez surveiller les appels réels de l'agent qui se produisent dans vos toiles et catalogues. Vous pouvez filtrer en fonction d'informations telles que la plage de dates, le résultat (succès ou échec) ou l'emplacement/localisation de l'appel.

![Journaux d'un agent Random Sport Assignment, qui indiquent quand et où l'agent a été appelé.]( {% image_buster /assets/img/ai_agent/agent_activity_logs.png %} )

Sélectionnez **Afficher** pour un appel d'agent spécifique afin de voir l'entrée, la sortie et l'ID de l'utilisateur.

![Journaux d'un agent City Trends et Recommendation Booking. Le panneau des détails indique l'invite de saisie, la réponse de sortie et l'ID de l'utilisateur associé.]( {% image_buster /assets/img/ai_agent/agent_logs.png %} )
