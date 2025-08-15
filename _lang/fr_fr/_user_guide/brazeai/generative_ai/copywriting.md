---
nav_title: Rédaction
article_title: Assistant de rédaction IA
page_order: 2.1
description: "Cet article de référence présente l’assistant de rédaction basé sur l’IA, une fonctionnalité qui transmet un nom de produit bref ou une description à l’outil de génération de texte GPT de OpenAI pour rédiger un texte marketing semblable à celui produit par un humain, que vous pourrez ensuite utiliser dans vos communications."
---

# Générer une copie avec <sup>BrazeAITM</sup>

> L'assistant de rédaction avec l'IA transmet un bref nom ou une brève description de produit à l’outil de génération de textes GPT du fournisseur OpenAI, afin de générer des textes marketing semblables à ceux rédigés par un humain, que vous pouvez ensuite utiliser dans vos communications. Cette fonctionnalité est disponible par défaut pour la plupart des composeurs de messages dans le tableau de bord de Braze.

## Création d'un texte

### Étape 1 : Rédacteur en intelligence artificielle pour le lancement

Dans votre composeur de messages, sélectionnez <i class="fa-solid fa-wand-magic-sparkles"></i> **Lancer le rédacteur IA**.

Dans l'éditeur par glisser-déposer pour les messages in-app, sélectionnez un bloc de texte et choisissez <i class="fa-solid fa-wand-magic-sparkles" title="Rédacteur IA"></i> dans la barre d'outils du bloc.

### Étape 2 : Saisissez les détails

Saisissez un nom ou une description de produit dans le champ de saisie, puis sélectionnez une longueur de sortie approximative.

Vous pouvez choisir un canal spécifique pour une longueur de sortie basée sur les bonnes pratiques spécifiques au canal ou sélectionner entre court (1 phrase), moyen (2-3 phrases) ou long (1 paragraphe).

### Étape 3 : Personnalisez-le davantage (facultatif)

Pour personnaliser davantage votre copie, vous pouvez :

- **Appliquer les lignes directrices de la marque :** Après avoir [créé des directives de marque avec <sup>BrazeAITM</sup>]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), vous pouvez les utiliser pour générer votre texte.
- **Choisissez un ton :** Chaque ton génère une copie dans un style différent. Choisissez le ton qui correspond le mieux à la voix de votre marque.
- **Faites référence aux données des campagnes précédentes**: Lorsque cette option est activée, les notifications push mobiles précédentes envoyées dans le cadre de vos campagnes ou étapes du canvas sont utilisées comme référence stylistique pour générer votre nouvelle copie. Pour plus d'informations, reportez-vous à la section [Utilisation des données des campagnes précédentes](#past-campaign-data).
- **Copie de la traduction automatique :** Vous pouvez choisir une langue de sortie différente pour votre copie. Le contenu généré sera produit dans cette langue.

### Étape 4 : Créez votre texte

Lorsque vous avez terminé, sélectionnez **Générer**. Nous utiliserons les informations que vous nous fournissez pour demander à GPT de rédiger un texte pour vous. La réponse sera récupérée depuis OpenAI et vous sera fournie. Pour plus d'informations, consultez la rubrique [Comment mes données sont-elles utilisées et envoyées à OpenAI ?](#ai-policy)

![Modale de l'assistant de rédaction de l'intelligence artificielle montrant les différentes fonctionnalités disponibles"]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3").{: style="max-width:70%;"}

{% alert important %}
Nous filtrons les réponses au contenu offensant qui viole la [politique de contenu](https://beta.openai.com/docs/usage-guidelines/content-policy) d'OpenAI.
{% endalert %}

## À propos des données relatives aux campagnes antérieures {#past-campaign-data}

Lorsque vous utilisez les notifications push comme longueur de sortie, si vous sélectionnez **Faire référence aux données d’anciennes campagnes**, des campagnes de notifications push mobiles antérieures, sélectionnées au hasard, sont envoyées à OpenAI afin que GPT puisse s'en servir comme base pour sa génération de texte. Ne cochez pas cette case si vous ne souhaitez pas utiliser cette fonctionnalité. Consultez les sections suivantes pour en savoir plus sur la façon dont Braze et OpenAI utilisent vos données. 

Si cette fonctionnalité est utilisée en conjonction avec une [directive de marque]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/), la directive de marque et les données de la campagne antérieure seront incorporées dans le texte final généré.

{% multi_lang_include brazeai/generative_ai/policy.md %}
