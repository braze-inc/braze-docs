---
nav_title: Étape d’IA
article_title: Étape d’IA
permalink: /ai_step/
description: "Cet article de référence traite de l'étape IA du canvas."
Tool:
  - Canvas
hidden: true
---

# Étape IA

> L'étape de l'intelligence artificielle au sein de Canvas s'appuie sur ChatGPT pour automatiser le marketing personnalisé en interprétant les entrées générées par les utilisateurs (telles que les retours d'enquête), en déterminant la réponse appropriée et en déclenchant des messages - le tout au sein de Braze. ChatGPT est un outil OpenAI, une tierce partie.

{% alert note %}
L'étape de l'intelligence artificielle est actuellement disponible en tant que fonctionnalité bêta. Si vous souhaitez participer à cet essai bêta, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

## Création d'une étape d'intelligence artificielle {#create-ai-step}
 
1. Ajoutez une nouvelle étape à votre canvas et sélectionnez l'**étape de l'intelligence artificielle**. <br><br>![L'étape de l'intelligence artificielle dans le générateur de canvas][1]{: style="max-width: 30%;"}<br><br>
2. Créez une invite qui indique à l'intelligence artificielle comment réagir à diverses actions de l'utilisateur. Les réponses peuvent comprendre la mise à jour d'un attribut personnalisé ou l'envoi d'un message. Cette invite peut utiliser Liquid pour attribuer des réponses différentes en fonction des attributs ou des entrées de l'utilisateur. <br><br>Pour attribuer des sorties qui pourront ensuite être utilisées pour personnaliser les futurs messages dans le même Canvas, créez une invite qui enregistre des variables avec des noms spécifiques (par exemple, "message" et "score de sentiment"). <br><br> ![Exemple d'invite d'intelligence artificielle utilisée dans les paramètres de l'étape d'intelligence artificielle pour envoyer un message personnalisé sur la base d'un score de sentiment généré. Cet exemple est présenté dans la section « Réponses au sentiment des clients ».][2] <br><br>
3. Utilisez l'onglet " **Aperçu"** pour tester ce que l'intelligence artificielle pourrait produire pour des utilisateurs spécifiques.<br><br> ![L'onglet Aperçu des paramètres de l'étape d'intelligence artificielle montrant un message personnalisé généré par l'intelligence artificielle pour trois paramètres : un prénom de Cameron, un nom de produit de chaussures, et le texte " confortable mais mon lacet de chaussure s'est déjà cassé "][3]

## Référencement des résultats de l'intelligence artificielle à l'aide de Liquid
Faites référence à la sortie de l'IA dans les étapes ultérieures en insérant la logique Liquid `{% raw %}{{ai_step_output.${key_name}}}{% endraw %}`. Vous pouvez définir le `key_name` dans l'invite de l'étape IA.

Par exemple, si vous utilisez les variables « message » et « score de sentiment , vous pouvez utiliser `{% raw %}{{ai_step_output.${message}}}{% endraw %}` pour personnaliser un message ultérieur dans ce même canvas.

Vous pouvez également enregistrer la sortie d'une étape IA en tant qu'attribut personnalisé en utilisant l'étape Canvas de mise à jour de l'utilisateur, dans laquelle vous lisez la sortie de l'étape IA (par exemple, `{% raw %}{{ai_step_output.${sentiment_score}}}{% endraw %}`). Si la sortie générée n'est pas stockée en tant qu'attribut personnalisé, elle ne peut pas être utilisée ailleurs que dans les étapes ultérieures du même canvas.

## Statistiques sur les étapes de l'intelligence artificielle

Les étapes IA présentent les caractéristiques suivantes au niveau de l'étape :

- **Passez à l'étape suivante :** Nombre d'utilisateurs qui sont passés à l'étape(s) suivante(s) dans le Canvas
- **Sortis du canvas :** Nombre d'utilisateurs ayant quitté le canvas parce que l'étape de votre intelligence artificielle était la dernière.
- **Réussite de la sortie générée :** Nombre d'utilisateurs pour lesquels l'étape d'intelligence artificielle a généré des résultats avec succès.
- **Échec de la sortie générée :** Nombre d'utilisateurs pour lesquels l'étape de l'intelligence artificielle n'a pas produit de résultats, auquel cas les utilisateurs passeront quand même aux étapes suivantes.

### Comprendre les résultats de vos étapes d'intelligence artificielle

Il existe quelques scénarios dans lesquels Braze écarte le résultat de l'étape d'intelligence artificielle et envoie le client à l'étape suivante :
- Si l'édition dépasse 1 024 caractères
- Si la sortie n'est pas en JSON
- Si l'invite ne satisfait pas aux exigences de [modération](https://platform.openai.com/docs/guides/moderation/overview) d'OpenAI, qui signale les contenus inappropriés générés par l'utilisateur

## Cas d'utilisation des étapes de l'intelligence artificielle

### Réponses au sentiment des clients

Comme le montre l'exemple de la [création d'une étape d'intelligence artificielle](#create-ai-step), vous pouvez demander à l'intelligence artificielle d'envoyer des messages de suivi en fonction des scores de sentiment générés à partir des commentaires des clients.
- Notes de sentiment positives - Déclenchez une notification push qui demande aux utilisateurs de laisser un avis.
- Notes de sentiment moyennes - Déclencher un e-mail demandant aux utilisateurs s'ils souhaitent une aide supplémentaire
- Scores de sentiments faibles - Déclencher un webhook qui notifie le service d'assistance aux utilisateurs, afin qu'un conseiller puisse élaborer un suivi nuancé

#### Exemple d'invite à l'intelligence artificielle

Cet exemple a été utilisé dans l'[étape Créer une intelligence artificielle](#create-ai-step).

Un client a acheté "`{% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}`", et a donné son avis sur le produit : "`{% raw %}{{canvas_entry_properties.${text}}}{% endraw %}`". Créez un score de sentiment sous la forme d'un nombre entier compris entre 0 et 100. Créez ensuite un message personnalisé. Vous devriez obtenir deux variables, « message » et « score de sentiment ».

### Suivi des enquêtes

Si vous réalisez un sondage in-app ou in-browser avec une section à réponse libre, vous pouvez utiliser les étapes de l'intelligence artificielle pour analyser les réponses libres et effectuer un suivi approprié. 

Par exemple, si un détaillant de produits de maquillage propose une enquête demandant « Quels produits aimeriez-vous nommer pour les prix de beauté de cette année ?» , il peut utiliser une invite qui identifie et affecte un attribut aux types de produits et marques préférés de l'utilisateur, puis personnaliser le contenu futur sur la base de ces données.

#### Exemple d'invite à l'intelligence artificielle

Identifiez la marque préférée de l'utilisateur à l'aide de sa réponse. Créez ensuite un message qui remercie les utilisateurs d'avoir répondu à l'enquête et qui mentionne que les experts en beauté ont également leur marque préférée. Vous devriez obtenir deux variables, "message" et "marque préférée".

![Onglet de prévisualisation des paramètres de l'étape IA montrant un message personnalisé généré par l'intelligence artificielle pour le paramètre de réponse à l'enquête « J'adore les crèmes pour le visage Estee Lauder » qui remercie l'utilisateur d'avoir répondu à l'enquête et lui recommande ensuite une crème pour le visage.][4]

### Recommandations basées sur le comportement

Les clients peuvent demander à l'intelligence artificielle d'analyser les comportements des clients et d'envoyer des messages de recommandation. 

Par exemple, vous pouvez créer une invite pour analyser les 50 achats les plus récents des utilisateurs et définir leur catégorie la plus achetée comme un nouvel attribut personnalisé. Vous pouvez ensuite envoyer des recommandations personnalisées par e-mail pour la catégorie préférée de chaque utilisateur.

#### Exemple d'invite à l'intelligence artificielle

Un client a acheté les produits suivants : "`{% raw %}{{custom_attribute.${Products Purchased}}}{% endraw %}`". Identifiez la catégorie de produits la plus achetée par l'utilisateur. Vous devriez obtenir une nouvelle variable pour la "catégorie la plus achetée".

![L'onglet de prévisualisation des paramètres de l'étape d'intelligence artificielle montre la variable "livre" générée par l'intelligence artificielle pour le paramètre de la catégorie la plus achetée.][5]

## Limites de débit

Il y a une limite de 10 requêtes par minute (RPM) par entreprise. Cela signifie que pour toute étape de l'intelligence artificielle, jusqu'à 10 utilisateurs peuvent recevoir cette étape au cours d'une minute donnée et que tout utilisateur au-delà de ces 10 utilisateurs passera automatiquement à l'étape suivante. Lorsque la minute suivante commence, les utilisateurs peuvent à nouveau recevoir l'étape d'intelligence artificielle, mais les utilisateurs précédents qui ont déclenché la limite de débit ne seront pas réessayés.

## Limites des étapes de l'intelligence artificielle

- Cette fonctionnalité s'appuie sur la norme GPT-3.5.
- Cette fonctionnalité utilise la clé API OpenAI de Braze. Vous ne pouvez pas utiliser votre propre clé API OpenAI.
- Il y a une limite de 5 requêtes par minute (RPM) par espace de travail et de 10 RPM par entreprise.
- Cette fonctionnalité n'est pas conforme à la loi HIPAA et les clients ne doivent pas envoyer d'informations personnelles identifiables (PII) ou d'informations de santé protégées (PHI).

## Comment mes données sont-elles utilisées et envoyées à OpenAI ?

Afin d'analyser et de créer le contenu de vos messages, Braze enverra vos messages-guides à la plateforme API d'OpenAI. Toutes les requêtes envoyées à OpenAI depuis Braze sont anonymisées, ce qui signifie qu'OpenAI ne sera pas en mesure d'identifier l’origine de la requête, à moins que vous n'incluiez des informations identifiables dans le contenu de message que vous fournissez. Comme décrit dans les [engagements de la plateforme API d’OpenAI](https://openai.com/policies/api-data-usage-policies), les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer leurs modèles et seront supprimées après 30 jours. Veuillez vous assurer que vous respectez les politiques d'OpenAI qui vous concernent, y compris la [politique d'utilisation](https://openai.com/policies/usage-policies). Braze n'offre aucune garantie de quelque nature que ce soit en ce qui concerne tout contenu généré par l'intelligence artificielle. 

[1]: {% image_buster /assets/img/ai_step1.png %}
[2]: {% image_buster /assets/img/ai_step2.png %}
[3]: {% image_buster /assets/img/ai_step3.png %}
[4]: {% image_buster /assets/img/ai_step4.png %}
[5]: {% image_buster /assets/img/ai_step5.png %} 