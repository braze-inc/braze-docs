---
nav_title: Directives de marque
article_title: Directives de marque pour la rédaction avec l’IA
page_order: 1
description: "Cet article de référence traite des directives de marque pour l'assistant de rédaction avec l’IA. Cette fonctionnalité vous permet d'adapter le style des textes générés par l'assistant de rédaction basé sur l'intelligence artificielle à la voix et au style de votre marque."
---

# Directives de marque pour l’assistant de rédaction avec l’IA

> Adaptez le style de votre texte généré par l’IA à la voix et à la personnalité de votre marque, grâce à des directives de marque personnalisées.

## Créer des directives de marque {#steps}

Procédez comme suit pour créer des directives de marque dans l'assistant de rédaction avec l’IA.

### Étape 1 : Créer une directive de marque

1. Dans votre composeur de messages, sélectionnez <i class="fa-solid fa-wand-magic-sparkles"></i> **Lancer le rédacteur IA**.
   * Dans l'éditeur par glisser-déposer pour les messages in-app, sélectionnez un bloc de texte et choisissez <i class="fa-solid fa-wand-magic-sparkles" title="Rédacteur IA"></i> dans la barre d'outils du bloc.
2. Sélectionnez **Appliquer la directive de marque**, puis **Créer une directive de marque**.
3. Saisissez un nom pour cette directive. Il s'agira de l'étiquette qui apparaît dans la sélection précédente.
4. Pour la rubrique **Dans quels cas utiliserez-vous ces directives de marque ?**, ajoutez des détails afin d’aider vos collègues (et vous à l'avenir) à comprendre le contexte d'utilisation de ces directives.

![Vue de la création des directives de marque.][1]

### Étape 2 : Décrire la personnalité de votre marque

Pour la **personnalité de la marque**, réfléchissez à ce qui rend votre marque unique. Incluez les caractéristiques, les valeurs, la voix et tous les archétypes qui définissent votre marque. Voici quelques caractéristiques à prendre en compte :

| **Caractéristique**       | **Définition**                                                                       | **Exemple**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Réputation               | Comment vous souhaitez que votre marque soit perçue sur le marché.                               | Nous sommes connus comme la marque la plus fiable et la plus orientée client dans notre secteur. |
| Traits de personnalité       | Caractéristiques humaines qui décrivent le caractère de votre marque.                     | Notre marque est conviviale, accessible et toujours optimiste.          |
| Valeurs                   | Les valeurs fondamentales qui orientent les actions et les décisions de votre marque.                           | Nous accordons de l'importance à la durabilité, à la transparence et à la communauté.            |
| Différenciation          | Les qualités uniques qui distinguent votre marque de ses concurrents.                         | Nous nous distinguons en offrant un service client personnalisé qui va au-delà des attentes. |
| Voix de la marque              | Le ton et le style de communication de votre marque.                                 | Notre voix est décontractée mais informative, claire sans être trop formelle. |
| Archétype de la marque          | L'archétype qui illustre le persona de votre marque (le héros, le créateur, etc.).    | Nous incarnons l'archétype de l'explorateur, toujours à la recherche de nouveaux défis et de nouvelles aventures. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Étape 3 : Définir le langage à éviter (facultatif)

Pour les **exclusions**, énumérez tout langage ou style qui ne correspond pas à votre marque. Par exemple, vous voudrez peut-être éviter le « sarcasme », les « attitudes négatives » ou le ton « condescendant ».

### Étape 4 : Tester vos directives

Testez vos directives pour en évaluer le résultat. Développez la section **Tester vos directives** pour générer des exemples de textes et, le cas échéant, les peaufiner.

### Étape 5 : Enregistrer vos directives

Lorsque vous êtes satisfait de vos directives, sélectionnez **Enregistrer la directive de marque**. Vos nouvelles directives seront enregistrées dans votre espace de travail pour une utilisation ultérieure.

{% alert important %}
Vous pouvez changer la langue du texte final, quelle que soit la langue du texte généré, mais ni Braze ni OpenAI ne garantissent la qualité de la traduction. Testez et vérifiez toujours les traductions avant de les utiliser.
{% endalert %}

## Modifier les directives

Pour modifier vos directives de marque :

1. Ouvrez l'assistant de rédaction basé sur l’IA.
2. Appliquez les directives de marque que vous souhaitez modifier. Un bouton apparaît à côté du champ.
3. Sélectionnez **Modifier les directives**.

## Comment mes données sont-elles utilisées et envoyées à OpenAI ?

Pour générer des textes à l'aide d'une directive de marque, Braze envoie votre requête, y compris le contenu de votre directive, à OpenAI. Toutes les requêtes envoyées à OpenAI depuis Braze sont anonymisées, ce qui signifie qu'OpenAI ne sera pas en mesure d'identifier l’origine de la requête, à moins que vous n'incluiez des informations identifiables dans les données que vous fournissez ou dans les données de vos compagnes antérieures si vous activez l’option « Faire référence aux données d’anciennes campagnes ». Conformément à la [politique d'OpenAI](https://openai.com/policies/api-data-usage-policies), les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer leurs modèles et seront supprimées après 30 jours. Entre vous et Braze, tout contenu généré à l'aide de GPT constitue votre propriété intellectuelle. Braze ne fera valoir aucune revendication de propriété intellectuelle sur ce contenu et ne donne aucune garantie de quelque nature que ce soit concernant tout contenu généré par l’IA.


[1]: {% image_buster /assets/img/ai_copywriter/manual_brand_guidelines.png %} « Directives de marque »
