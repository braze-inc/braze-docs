---
nav_title: Créer des agents
article_title: Créer des agents personnalisés
description: "Découvrez comment créer des agents, ce qu'il convient de préparer avant de commencer et comment les mettre en œuvre dans les domaines de l'envoi de messages, de la prise de décision et de la gestion des données."
page_order: 1
alias: /creating-agents/
---

# Créer des agents personnalisés

> Découvrez comment créer des agents personnalisés, ce qu'il convient de préparer avant de commencer et comment les mettre en œuvre dans les domaines de l'envoi de messages, de la prise de décision et de la gestion des données. Pour obtenir des informations générales, veuillez consulter [la section Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents).

## Conditions préalables

Avant de commencer, vous aurez besoin des éléments suivants :

- [Autorisation]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) d'accéder à la **console d'agent** dans votre espace de travail. Veuillez vérifier auprès de vos administrateurs Braze si cette option n'apparaît pas.  
- Autorisation de créer et de modifier des agents d’intelligence artificielle personnalisés.
- Une idée de ce que vous souhaitez que l'agent accomplisse. Les agents Braze peuvent prendre en charge les actions suivantes :  
   - **Envoi de messages :** Générez des lignes d'objet, des titres, des textes intégrés au produit ou tout autre contenu.  
   - **Prise de décision :** Dirigez les utilisateurs dans Canvas en fonction de leur comportement, de leurs préférences ou d'attributs personnalisés.  
   - **Gestion des données :** Veuillez calculer les valeurs, enrichir les entrées du catalogue ou actualiser les champs du profil.  

## Fonctionnement

Lorsque vous créez un agent, vous définissez son objectif et établissez des garde-fous quant à son comportement. Une fois en ligne/en production/instantané, l'agent peut être déployé dans Braze pour générer des copies personnalisées, prendre des décisions en temps réel ou mettre à jour les champs du catalogue. Vous pouvez suspendre ou mettre à jour un agent à tout moment depuis le tableau de bord.

Les cas d'utilisation suivants illustrent quelques façons de tirer parti des agents personnalisés.

| Cas d’utilisation | Description |
| --- | --- |
| Gestion des commentaires des clients | Transmettez les commentaires des utilisateurs à un agent afin qu'il analyse leur sentiment et génère des messages de suivi empathiques. Pour les utilisateurs de grande valeur, l'agent peut escalader la réponse ou inclure des avantages. |
| Localiser le contenu | Traduisez le texte du catalogue dans une autre langue pour les campagnes mondiales, ou ajustez le ton et la longueur pour les canaux spécifiques à chaque région. Par exemple, traduisez « Lunettes de soleil Classic Clubmaster » en espagnol par « Gafas de sol Classic Clubmaster » ou raccourcissez les descriptions pour les campagnes SMS. |
| Veuillez résumer les avis ou les commentaires. | Résumez les sentiments ou les commentaires dans un nouveau champ, par exemple en attribuant des notes telles que « Positif », « Neutre » ou « Négatif », ou en rédigeant un bref résumé tel que « La plupart des clients mentionnent une excellente qualité, mais soulignent la lenteur de la livraison ». |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Créer un agent

### Étape 1 : Veuillez sélectionner un type d'agent

Pour créer votre agent personnalisé :

1. Veuillez vous rendre dans **la console des agents** > **Gestion des agents** dans le tableau de bord de Braze.  
2. Veuillez sélectionner **Créer un agent**.
3. Veuillez choisir de créer un agent canvas ou un agent catalogue.

### Étape 2 : Détails de la configuration

Veuillez ensuite configurer les détails de votre agent :

1. Veuillez saisir un nom et une description afin d'aider votre équipe à comprendre son objectif.
2. (facultatif) Veuillez ajouter des étiquettes pour filtrer votre agent.
3. Veuillez sélectionner le [modèle]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) que votre agent devra utiliser.
4. Veuillez sélectionner le niveau de réflexion du modèle. Vous avez le choix entre minimal, faible, moyen ou élevé. Nous vous recommandons de commencer par **le mode Minimal**, de tester les réponses de votre agent et de l'ajuster si nécessaire.

![Interface de la console d'agent pour la création d'un agent personnalisé dans Braze. L'écran affiche des champs permettant de saisir le nom et la description de l'agent, ainsi que de sélectionner un modèle.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Étape 3 : Veuillez rédiger les instructions. {#agent-instructions}

Veuillez donner des instructions à l'agent. Nous recommandons d'inclure des instructions sur la conduite à tenir par l'agent dans des situations imprévues ou ambiguës. Cela minimise le risque que la confusion des agents entraîne des erreurs. Par exemple, plutôt que de demander à l'agent uniquement des valeurs de sentiment « positives » ou « négatives », veuillez lui demander de renvoyer « incertain » s'il ne parvient pas à se prononcer.

Veuillez consulter les [instructions de rédaction]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) pour connaître les meilleures pratiques et [les exemples]({{site.baseurl}}/user_guide/brazeai/agents/reference/#examples) pour trouver l'inspiration sur la manière de guider votre agent.

{% alert tip %}
Pour les agents Canvas, vous pouvez utiliser Liquid dans vos instructions afin de faire référence aux attributs utilisateur, tels que leur prénom et leur nom, ou à des attributs personnalisés. Toute variable liquid dans les instructions de l'agent est automatiquement transmise à l'étape Agent lorsqu'un utilisateur accède à cette étape.
{% endalert %}

#### Étape 3.1 : Ajouter un contexte

Veuillez sélectionner **Ajouter un contexte** pour choisir les éléments auxquels votre agent peut se référer. Ceci comprend :

- [Champs du catalogue]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields) : Veuillez autoriser l'agent à accéder aux données de votre catalogue afin d'obtenir des réponses plus précises.
- [Appartenance au segment]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context) : Permettez à l'agent de réaliser la personnalisation des réponses en fonction des segments auxquels appartient l'utilisateur. Vous pouvez sélectionner jusqu'à cinq segments.
- [Directives relatives à la marque]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) : Veuillez vous référer aux directives relatives au ton et au style de la marque que l'agent doit respecter. Par exemple, si vous souhaitez que votre agent génère un SMS pour encourager les utilisateurs à effectuer une inscription à une salle de sport, vous pouvez utiliser ce champ pour faire référence à votre directive prédéfinie, rédigée en gras et motivante.
- [Contexte général]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) : [canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) Analysez toutes les données de contexte canvas pour un utilisateur lorsque cet agent est invoqué, y compris toutes les variables qui ne sont pas référencées dans la section **Instructions**.

#### Étape 3.2 : Ajouter des paramètres facultatifs

Dans les **paramètres optionnels**, vous pouvez ajuster la [température]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) de la copie générée par l'agent. Une température plus élevée permet à l'agent d'utiliser les informations fournies de manière plus créative.

Vous pouvez également définir la limite d'exécution quotidienne pour votre agent. Par défaut, cette valeur est définie sur 250 000, mais elle peut être augmentée jusqu'à 1 000 000. Si vous souhaitez augmenter la limite au-delà de 1 000 000, veuillez contacter votre gestionnaire de la satisfaction client pour en savoir plus.

### Étape 4 : Veuillez sélectionner la sortie {#select-output}

Dans la section **Sortie**, vous pouvez organiser et définir la sortie de l'agent à l'aide de schémas de base ou de schémas avancés.

Pour obtenir les meilleurs résultats, veuillez vous assurer que les informations que vous avez saisies dans la section **Sortie** correspondent aux instructions de l'agent que vous avez saisies à [l'étape 3](#agent-instructions). Par exemple, si vous avez indiqué dans les instructions de l'agent que vous souhaitez un objet avec deux chaînes de caractères, veuillez vous assurer de spécifier un objet avec deux chaînes de caractères dans la section **Sortie**. Si les instructions de votre agent ne correspondent pas au résultat souhaité, l'agent peut être désorienté, expirer ou générer des résultats indésirables.

#### Schémas de base

Les schémas de base sont une sortie simple renvoyée par un agent. Il peut s'agir d'une chaîne de caractères, d'un nombre, d'une valeur booléenne, d'un tableau de chaînes de caractères ou d'un tableau de nombres.

Par exemple, si vous souhaitez recueillir les notes attribuées par les utilisateurs dans le cadre d'un simple sondage afin de déterminer leur niveau de satisfaction après avoir reçu un produit, vous pouvez sélectionner **Nombre** comme schéma de base pour structurer le format de sortie.

{% alert important %}
Les tableaux ne sont disponibles que pour les agents canvas, et non pour les agents catalogue.
{% endalert %}

![Console d'agent avec le numéro sélectionné comme schéma de base.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Schémas avancés

Les options avancées du schéma comprennent la structuration manuelle des champs ou l'utilisation de JSON.

- **Domaines :** Une méthode sans code pour appliquer une sortie d'agent que vous pouvez utiliser de manière cohérente.
- **JSON :** Une approche par code pour créer un format de sortie précis, où vous pouvez imbriquer des variables et des objets dans le schéma JSON. Uniquement disponible pour les agents canvas, pas pour les agents catalogue.

Nous vous recommandons d'utiliser des schémas avancés lorsque vous souhaitez que l'agent renvoie une structure de données avec plusieurs valeurs définies de manière structurée, plutôt qu'une sortie à valeur unique. Cela permet de mieux formater la sortie en tant que variable de contexte cohérente.

Par exemple, vous pouvez utiliser un format de sortie dans un agent destiné à créer un exemple d'itinéraire de voyage pour un utilisateur en fonction d'un formulaire qu'il a soumis. Le format de sortie vous permet de définir que chaque réponse de l'agent doit renvoyer les valeurs ,`tripStartDate` `tripEndDate`, et`destination`. Chacune de ces valeurs peut être extraite des variables de contexte et placée dans une étape Message pour être soumise à une personnalisation à l'aide de Liquid.

{% tabs %}
{% tab Fields %}

Si vous souhaitez formater les réponses à un simple sondage afin de déterminer dans quelle mesure les répondants sont susceptibles de recommander la nouvelle saveur de crème glacée de votre restaurant, vous pouvez configurer les champs suivants pour structurer le format de sortie :

| Nom du champ | Valeur |
| --- | --- |
| **likelihood_score** | Nombre |
| **explication** | Chaîne de caractères |
| **confidence_score** | Nombre |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Console de l'agent affichant trois champs de sortie pour le score de probabilité, l'explication et le score de confiance.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

Si vous souhaitez recueillir les commentaires des utilisateurs sur leur dernière expérience culinaire dans votre chaîne de restaurants, vous pouvez sélectionner **JSON Schema** comme format de sortie et insérer le JSON suivant pour renvoyer un objet de données comprenant une variable de sentiment et une variable de raisonnement.

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

{% endtab %}
{% endtabs %}

### Étape 5 : Veuillez tester et créer l'agent.

Le volet **Aperçu** est une instance de l'agent qui s'affiche sous la forme d'un panneau côte à côte dans l'expérience de configuration. Vous pouvez l'utiliser pour tester l'agent pendant que vous le créez ou le mettez à jour afin de le découvrir de la même manière que les utilisateurs finaux. Cette étape vous permet de vérifier que tout fonctionne comme prévu et vous donne l'occasion d'effectuer des ajustements avant que le système ne soit en ligne/en production/instantané.

1. Dans le champ **Testez votre agent**, veuillez saisir des exemples de données clients ou de réponses clients, c'est-à-dire tout ce qui reflète des scénarios réels auxquels votre agent sera confronté.
2. Prévisualisez la réponse de l'agent pour un utilisateur aléatoire, un utilisateur existant ou un utilisateur personnalisé.
3. Veuillez sélectionner **Simuler la réponse**. L'agent exécutera en fonction de votre configuration et affichera sa réponse. Les essais comptent dans votre limite d'exécution quotidienne.

![Console d'agent affichant le volet Aperçu pour tester un agent personnalisé. L'interface affiche un champ « Exemples d'entrées » contenant des exemples de données client, un bouton « Lancer le test » et une zone de réponse où s'affiche la sortie de l'agent.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Veuillez examiner attentivement le résultat. Veuillez prendre en considération les questions suivantes :

- Le texte correspond-il à l'image de marque ?
- La logique décisionnelle oriente-t-elle les clients comme prévu ?
- Les valeurs calculées sont-elles exactes ?

Si quelque chose ne semble pas fonctionner correctement, veuillez mettre à jour la configuration de l'agent et réessayer. Veuillez tester plusieurs entrées différentes afin d'observer comment l'agent s'adapte à différents scénarios, en particulier dans les cas extrêmes tels que l'absence de données ou les réponses non valides.

{% alert tip %}
Veuillez éviter d'indiquer à l'agent précisément ce que vous ne souhaitez pas qu'il fasse. Les LLM peuvent toujours générer ce contenu si vous le mentionnez dans les instructions.
{% endalert %}

### Étape 6 : Veuillez utiliser votre agent

Votre agent est désormais prêt à l'emploi. Pour plus de détails, veuillez vous référer à [la section Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Articles connexes  

- [Référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
