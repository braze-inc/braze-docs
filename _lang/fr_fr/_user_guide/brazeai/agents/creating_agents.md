---
nav_title: Créer des agents
article_title: Créer des agents personnalisés
description: "Apprenez à créer des agents, à les préparer avant de commencer et à les utiliser pour l'envoi de messages, la prise de décision et la gestion des données."
page_order: 1
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
   - **Envoi de messages :** Générer des lignes d'objet, des titres, des textes dans les produits ou d'autres contenus.  
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

### Étape 1 : Détails de l'installation

Pour créer votre agent personnalisé :

1. Dans le tableau de bord de Braze, accédez à **Console des agents** > **Gestion des agents**.  
2. Sélectionnez **Créer un agent**.
3. Saisissez un nom et une description pour aider votre équipe à comprendre son objectif.
4. (facultatif) Ajoutez des tags pour filtrer votre agent.
5. Sélectionnez le site d'interaction, c'est-à-dire l'emplacement/localisation de l'agent. Notez que le site d'interaction ne peut pas être mis à jour après la création d'un agent.
6. Choisissez le [modèle]({{site.baseurl}}/docs/user_guide/brazeai/agents/reference/#models) que votre agent utilisera.

![Interface de la console d'agent permettant de créer un agent personnalisé dans Braze. L'écran affiche des champs permettant de saisir le nom et la description de l'agent et de sélectionner un modèle.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

### Étape 2 : Rédiger les instructions

Donnez des instructions à l'agent. Reportez-vous à la [référence des agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/) pour obtenir des conseils.

{% alert tip %}
Vous pouvez utiliser Liquid dans vos instructions pour faire référence aux attributs de l'utilisateur, tels que son nom et son prénom, ou à des attributs personnalisés.
{% endalert %}

#### Étape 2.1 : Ajouter un contexte

Sélectionnez **Ajouter un contexte** pour choisir ce que votre agent peut référencer. Ceci comprend :

- [Champs du catalogue]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Fournissez des champs de catalogue pour que l'agent puisse s'y référer.
- L'[appartenance à un segment]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Tenez compte de l'appartenance d'un utilisateur à un segment lors de la personnalisation des messages. Vous pouvez sélectionner jusqu'à trois segmentations.
- [Lignes directrices de la marque]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines): Faites référence à la voix de la marque et aux lignes directrices en matière de style que l'agent doit suivre. Par exemple, si vous souhaitez que votre agent génère un texte SMS pour encourager les utilisateurs à s'inscrire à une salle de sport, vous pouvez utiliser ce champ pour faire référence à votre ligne directrice prédéfinie, audacieuse et motivante.
- [Canvas Variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables): Analyser toutes les variables du contexte Canvas pour un utilisateur lorsque cet agent est invoqué.

#### Étape 2.2 : Ajouter des paramètres optionnels

Dans les **paramètres optionnels**, vous pouvez ajuster la [température de]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) la copie générée par l'agent. Une température plus élevée permet à l'agent d'utiliser les informations fournies pour être plus créatif.

Vous pouvez également définir la limite d'exécution quotidienne pour votre agent. Par défaut, cette valeur est fixée à 50 000, mais elle peut être portée à 100 000. Si vous souhaitez augmenter la limite au-delà de 100 000, contactez votre gestionnaire de satisfaction client pour en savoir plus.

### Étape 3 : Sélectionnez la sortie

Dans la section **Sortie**, vous pouvez organiser et définir la sortie de l'agent par schémas de base ou schémas avancés.

#### Schémas de base

Les schémas de base sont des résultats simples renvoyés par un agent. Il peut s'agir d'une chaîne de caractères, d'un nombre, d'un booléen, d'un tableau de chaînes de caractères ou d'un tableau de nombres.

Imaginons que vous souhaitiez recueillir les notes de sentiment des utilisateurs à partir d'une simple enquête de satisfaction afin de déterminer le degré de satisfaction de vos clients après avoir reçu un produit. Vous pouvez sélectionner **Numéro** comme schéma de base pour structurer le format de sortie.

{% alert important %}
Les tableaux ne sont disponibles que pour les agents Canvas, pas pour les agents catalogues.
{% endalert %}

![Console des agents avec le numéro sélectionné comme schéma de base.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Schémas avancés

Les options de schéma avancées comprennent la structuration manuelle des champs ou l'utilisation de JSON.

- **Domaines :** Un moyen sans code d'imposer une sortie d'agent que vous pouvez utiliser de manière cohérente. 
- **JSON :** Une approche par code pour créer un format de sortie précis, où vous pouvez imbriquer des variables et des objets dans le schéma JSON.

{% tabs %}
{% tab Fields %}

Supposons que vous souhaitiez mettre en forme les réponses à une simple enquête de satisfaction afin de déterminer dans quelle mesure les personnes interrogées sont susceptibles de recommander le nouveau parfum de crème glacée de votre restaurant. Vous pouvez définir les champs suivants pour structurer le format de sortie :

| Nom du champ | Valeur
| --- | --- |
| **likelihood_score** | Nombre |
| **explication** | Texte |
| **confidence_score** | Nombre |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Console de l'agent montrant trois champs de sortie pour le score de vraisemblance, l'explication et le score de confiance.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

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

{% endtab %}
{% endtabs %}

### Étape 4 : Tester et créer l'agent

Le volet de **prévisualisation** est une instance de l'agent qui s'affiche sous la forme d'un panneau côte à côte dans l'expérience de configuration. Vous pouvez l'utiliser pour tester l'agent pendant que vous le créez ou que vous le mettez à jour, afin d'en faire l'expérience de la même manière que les utilisateurs finaux. Cette étape vous permet de confirmer qu'il se comporte comme vous le souhaitez et vous donne l'occasion de le peaufiner avant qu'il ne soit mis en ligne/en production/instantané.

1. Dans le champ **Testez votre agent**, entrez des exemples de données ou de réponses de clients - tout ce qui reflète les scénarios réels que votre agent devra traiter.
2. Prévisualisez la réponse de l'agent pour un utilisateur aléatoire, un utilisateur existant ou un utilisateur personnalisé.
3. Sélectionnez **Simuler la réponse**. L'agent s'exécutera en fonction de votre configuration et affichera sa réponse. Les tests sont pris en compte dans votre limite d'exécution quotidienne.

![Console d'agent affichant le volet de prévisualisation pour tester un agent personnalisé. L'interface affiche un champ Exemple d'entrées avec des données personnalisées, un bouton Exécuter le test et une zone de réponse où apparaît le résultat de l'agent.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Examinez les résultats avec un œil critique. Réfléchissez aux questions suivantes :

- Le texte est-il conforme à la marque ?
- La logique décisionnelle achemine-t-elle les clients comme prévu ?
- Les valeurs calculées sont-elles exactes ?

Si vous avez l'impression que quelque chose ne va pas, mettez à jour la configuration de l'agent et testez à nouveau. Exécutez quelques entrées différentes pour voir comment l'agent s'adapte aux différents scénarios, en particulier aux cas extrêmes tels que l'absence de données ou les réponses non valides.

### Étape 5 : Utilisez et contrôlez votre agent

Votre agent est maintenant prêt à l'emploi ! Pour plus d'informations, reportez-vous à la section [Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

Dans l'onglet **Logs** de votre agent, vous pouvez surveiller les appels réels de l'agent qui se produisent dans vos toiles et catalogues. Vous pouvez filtrer en fonction d'informations telles que la plage de dates, le résultat (succès ou échec) ou l'emplacement/localisation de l'appel.

![Journaux d'un agent Story Teller, qui indiquent quand et où l'agent a été appelé.]({% image_buster /assets/img/ai_agent/agent_activity_logs.png %})

Sélectionnez **Voir** pour un appel d'agent spécifique afin de voir l'entrée, la sortie et l'ID de l'utilisateur.

![Journal de bord d'un agent Raconteur d'histoires. Le panneau des détails indique l'invite de saisie, la réponse de sortie et l'ID de l'utilisateur associé.]({% image_buster /assets/img/ai_agent/agent_logs.png %})
