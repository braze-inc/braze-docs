---
nav_title: Rédaction
article_title: Intelligence artificielle Copywriting Assistant
page_order: 2.1
description: "Cet article de référence couvre l'assistant de rédaction d'intelligence artificielle, fonctionnalité qui transmet un bref nom ou une brève description de produit à l'outil de génération de communication individualisée (GPT) d'OpenAI pour générer un produit marketing semblable à celui d'un humain, à utiliser dans vos messages."
---

# Générer une copie avec <sup>BrazeAITM</sup>

> L'assistant de rédaction de l'intelligence artificielle transmet un bref nom ou une brève description de produit à un outil de génération de communication individualisée du fournisseur tiers GPT appartenant à OpenAI afin de générer des textes marketing semblables à ceux d'un humain, qui seront utilisés dans vos messages. Cette fonctionnalité est disponible par défaut pour la plupart des compositeurs de messages dans le tableau de bord de Braze.

## Création d'un texte

### Étape 1 : Rédacteur en intelligence artificielle pour le lancement

Dans votre compositeur de messages, sélectionnez <i class="fa-solid fa-wand-magic-sparkles"></i> **Launch AI Copywriter**.

Dans l'éditeur par glisser-déposer pour les messages in-app, sélectionnez un bloc de texte et choisissez <i class="fa-solid fa-wand-magic-sparkles" title="Rédacteur d&apos;intelligence artificielle"></i> dans la barre d'outils du bloc.

### Étape 2 : Saisissez les détails

Saisissez un nom ou une description de produit dans le champ de saisie, puis sélectionnez une longueur de sortie approximative.

Vous pouvez choisir un canal spécifique pour une longueur de sortie basée sur les meilleures pratiques spécifiques au canal ou sélectionner entre court (1 phrase), moyen (2-3 phrases), ou long (1 paragraphe).

### Étape 3 : Personnalisez-le davantage (facultatif)

Pour personnaliser davantage votre copie, vous pouvez :

- **Appliquer les lignes directrices de la marque :** Après avoir [créé des directives de marque avec <sup>BrazeAITM</sup>]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), vous pouvez les utiliser pour générer votre texte.
- **Choisissez un ton :** Chaque ton génère une copie dans un style différent. Choisissez le ton qui correspond le mieux à la voix de votre marque.
- **Faites référence aux données des campagnes précédentes**: Lorsque cette option est activée, les notifications push mobiles précédentes envoyées dans le cadre de vos campagnes ou étapes du canvas sont utilisées comme référence stylistique pour générer votre nouvelle copie. Pour plus d'informations, reportez-vous à la section [Utilisation des données des campagnes précédentes](#past-campaign-data).
- **Copie de la traduction automatique :** Vous pouvez choisir une langue de sortie différente pour votre copie. Le contenu généré sera produit dans cette langue.

### Étape 4 : Créez votre texte

Lorsque vous avez terminé, sélectionnez **Générer**. Nous utiliserons les informations que vous nous fournissez pour demander à GPT de rédiger un texte pour vous. La réponse sera récupérée par OpenAI et vous sera communiquée. Pour plus d'informations, consultez la rubrique [Comment mes données sont-elles utilisées et envoyées à OpenAI ?](#ai-policy)

Modale de l'assistant de rédaction de l'intelligence artificielle montrant les différentes fonctionnalités disponibles".]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
Nous filtrons les réponses au contenu offensant qui viole la [politique de contenu](https://beta.openai.com/docs/usage-guidelines/content-policy) d'OpenAI.
{% endalert %}

## À propos des données relatives aux campagnes antérieures {#past-campaign-data}

Lorsque vous utilisez push comme longueur de sortie, si vous sélectionnez **Reference past campaign data**, des campagnes push mobiles antérieures sélectionnées au hasard seront envoyées à OpenAI afin que GPT puisse les utiliser comme base pour sa génération de copie. Actuellement, le rédacteur de l'intelligence artificielle enverra à OpenAI des campagnes de push qui n'ont pas la syntaxe Liquid. Ne cochez pas cette case si vous ne souhaitez pas exploiter cette possibilité. Consultez les sections suivantes pour en savoir plus sur la façon dont Braze et OpenAI utilisent vos données. 

S'il est utilisé en conjonction avec une [ligne directrice de marque]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/), la ligne directrice de marque et les données de la campagne passée seront incorporées dans le résultat final.

{% multi_lang_include brazeai/generative_ai/policy.md %}
