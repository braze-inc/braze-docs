---
nav_title: Article de référence
article_title: Référence des agents
description: "Référencez les détails clés sur les agents de Braze."
page_order: 3
---

# Référence des agents

> Lorsque vous créez des agents personnalisés, reportez-vous à cet article pour plus d'informations sur les paramètres clés, tels que les instructions et les schémas de sortie. Pour une introduction, voir [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

{% alert important %}
Les Braze Currents sont actuellement en version bêta. Pour obtenir de l'aide, contactez votre gestionnaire satisfaction client.
{% endalert %}

## Modèles

Lorsque vous configurez un agent, vous pouvez choisir le modèle qu'il utilise pour générer des réponses. Vous avez deux possibilités : utiliser un modèle alimenté par Braze ou apporter votre propre clé API.

{% alert important %}
Le modèle **Auto** alimenté par Braze est optimisé pour les modèles dont les capacités de réflexion sont suffisantes pour effectuer des tâches telles que la recherche d'un catalogue et l'appartenance à une segmentation d'utilisateurs. Si vous utilisez d'autres modèles, nous vous recommandons de faire des essais pour confirmer que votre modèle est adapté à votre cas d'utilisation. Il se peut que vous deviez ajuster vos [instructions](#writing-instructions) pour donner différents niveaux de détails ou de raisonnement étape par étape à des modèles ayant des vitesses et des capacités différentes.
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
7. Encouragez le raisonnement ("Réfléchissez en interne aux différentes étapes, puis donnez une réponse finale concise" ou "expliquez brièvement votre décision").
8. Pilotez, inspectez et itérez. De petites modifications peuvent conduire à des gains de qualité importants.
9. Traitez les cas particuliers, ajoutez des garde-fous et des instructions de refus.
10. Mesurez et documentez ce qui fonctionne en interne afin de pouvoir le réutiliser et l'étendre.

Nous vous recommandons d'inclure également une réponse par défaut si l'agent reçoit une réponse qui ne peut pas être analysée. Ce traitement des erreurs permet à l'agent de vous informer d'une variable de résultat inconnue. Par exemple, plutôt que de demander à l'agent d'indiquer uniquement des valeurs de sentiment "positives" ou "négatives", demandez-lui d'indiquer "incertain" s'il n'arrive pas à se décider.

### Demande simple

Cet exemple d'invite prend une enquête en entrée et produit une simple analyse des sentiments :

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative.
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

### Invite complexe 

Cet exemple d'invite reprend les données d'une enquête réalisée par un utilisateur et les classe en une seule étiquette de sentiment. Le résultat peut ensuite être utilisé pour orienter les utilisateurs vers différents parcours Canvas (tels que les commentaires positifs par rapport aux commentaires négatifs) ou stocker le sentiment en tant qu'attribut personnalisé sur leur profil en vue d'un ciblage ultérieur.

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

### Utilisation de Liquid

L'inclusion de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) dans les instructions de votre agent peut ajouter une couche supplémentaire de personnalisation dans sa réponse. Vous pouvez spécifier la variable Liquid exacte que l'agent reçoit et l'inclure dans le contexte de votre invite. Par exemple, au lieu d'écrire explicitement "prénom", vous pouvez utiliser l'extrait de code Liquid {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Dans la section **Journaux de** la **console de l'agent**, vous pouvez examiner les détails des entrées et sorties de l'agent pour comprendre quelle valeur est rendue par le liquide.

![Les coordonnées d'un agent qui a du liquide dans ses instructions.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:65%;"}

## Catalogues et champs

Choisissez des catalogues spécifiques pour qu'un agent puisse s'y référer et pour donner à votre agent le contexte dont il a besoin pour comprendre vos produits et d'autres données non liées à l'utilisateur, le cas échéant. Les agents utilisent des outils pour trouver uniquement les éléments pertinents et les envoient au LLM afin de minimiser l'utilisation de jetons.

![Le catalogue "restaurants" et la colonne "Loyalty_Program" sont sélectionnés pour la recherche de l'agent.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

## Contexte d'appartenance à un segment

Vous pouvez sélectionner jusqu'à trois segments pour l'agent afin de croiser l'appartenance de chaque utilisateur à un segment lorsque l'agent est utilisé dans un Canvas. Supposons que votre agent ait une appartenance à un segment sélectionnée pour un segment "Utilisateurs de fidélité", et que l'agent soit utilisé dans un Canvas. Lorsque des utilisateurs entrent dans une étape de l'agent, ce dernier peut vérifier si chaque utilisateur est membre de chaque segment que vous avez spécifié dans la console de l'agent, et utiliser l'appartenance (ou la non-appartenance) de chaque utilisateur comme contexte pour le LLM.

![Le segment "Utilisateurs fidèles" est sélectionné pour l'accès à l'adhésion des agents.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

## Lignes directrices de la marque

Vous pouvez sélectionner des [directives de marque]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) que votre agent devra respecter dans ses réponses. Par exemple, si vous souhaitez que votre agent génère un texte SMS pour encourager les utilisateurs à s'inscrire à une salle de sport, vous pouvez utiliser ce champ pour faire référence à votre ligne directrice prédéfinie, audacieuse et motivante.

## Température

Si votre objectif est d'utiliser un agent pour générer un texte incitant les utilisateurs à se connecter à votre application mobile, vous pouvez fixer une température plus élevée pour que votre agent soit plus créatif et utilise les nuances des variables contextuelles. Si vous utilisez un agent pour générer des scores de sentiment, il peut être idéal de fixer une température plus basse afin d'éviter toute spéculation de l'agent sur les réponses négatives à l'enquête. Nous vous recommandons de tester ce paramètre et d'examiner les résultats générés par l'agent pour les adapter à votre scénario.

{% alert note %}
Les températures ne sont actuellement pas prises en charge par l'OpenAI.
{% endalert %}