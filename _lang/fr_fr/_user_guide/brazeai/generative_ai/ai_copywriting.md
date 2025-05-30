---
nav_title: Assistant de rédaction IA
article_title: Assistant de rédaction IA
page_order: 4
description: "Cet article de référence présente l’assistant de rédaction basé sur l’IA, une fonctionnalité qui transmet un nom de produit bref ou une description à l’outil de génération de texte GPT de OpenAI pour rédiger un texte marketing semblable à celui produit par un humain, que vous pourrez ensuite utiliser dans vos communications."
---

# Assistant rédaction IA

> L'assistant de rédaction avec l'IA transmet un bref nom ou une brève description de produit à l’outil de génération de textes GPT du fournisseur OpenAI, afin de générer des textes marketing semblables à ceux rédigés par un humain, que vous pouvez ensuite utiliser dans vos communications. Cette fonctionnalité est disponible par défaut pour la plupart des composeurs de messages dans le tableau de bord de Braze.

## Créer un texte {#steps}

Pour générer une copie à l’aide de l’assistant de rédaction IA, procédez comme suit :

1. Dans votre composeur de messages, sélectionnez <i class="fa-solid fa-wand-magic-sparkles"></i> **Lancer le rédacteur IA**.
   * Dans l'éditeur par glisser-déposer pour les messages in-app, sélectionnez un bloc de texte et choisissez <i class="fa-solid fa-wand-magic-sparkles" title="Rédacteur IA"></i> dans la barre d'outils du bloc.
2. Saisissez un nom ou une description de produit dans le champ de saisie.
3. Sélectionnez une longueur de sortie approximative. Vous pouvez choisir un canal spécifique pour une longueur de sortie basée sur les bonnes pratiques spécifiques au canal ou sélectionner entre court (1 phrase), moyen (2-3 phrases) ou long (1 paragraphe). 
4. (Facultatif) Créez ou appliquez une directive de marque pour adapter ce texte à votre marque. Ces directives sont enregistrées dans votre espace de travail et réutilisables après leur création. Pour plus d'informations, voir [Création de directives de marque]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/).
5. (Facultatif) Choisissez un ton pour votre message parmi les options disponibles. Ceci déterminera le style du texte généré.
6. (Facultatif) Disponible pour les notifications push : Sélectionnez **Faire référence aux données d’anciennes campagnes** pour utiliser vos précédents messages de notifications push mobiles (campagnes et étapes du canvas) comme référence stylistique pour générer un nouveau texte. Lorsque cette option est sélectionnée, le texte généré reprend le style de vos messages précédents.
7. Sélectionnez la langue de sortie. Elle peut être différente de votre langue de saisie.
8. Sélectionnez **Générer**.

Nous utilisons les informations que vous fournissez pour décrire à GPT les textes à rédiger. La réponse sera récupérée depuis OpenAI et vous sera fournie. 

![Fenêtre modale de l'assistant de rédaction avec l’IA montrant les différentes fonctionnalités disponibles][1]{: style="max-width:70%;"}

{% alert important %}
Nous filtrons les réponses au contenu offensant qui viole la [politique de contenu](https://beta.openai.com/docs/usage-guidelines/content-policy) d'OpenAI.
{% endalert %}

## Utiliser les données des campagnes précédentes

Lorsque vous utilisez les notifications push comme longueur de sortie, si vous sélectionnez **Faire référence aux données d’anciennes campagnes**, des campagnes de notifications push mobiles antérieures, sélectionnées au hasard, sont envoyées à OpenAI afin que GPT puisse s'en servir comme base pour sa génération de texte. Ne cochez pas cette case si vous ne souhaitez pas utiliser cette fonctionnalité. Consultez les sections suivantes pour en savoir plus sur la façon dont Braze et OpenAI utilisent vos données. 

Si cette fonctionnalité est utilisée en conjonction avec une [directive de marque]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/), la directive de marque et les données de la campagne antérieure seront incorporées dans le texte final généré.

## Qu’est-ce que GPT ?

[GPT](https://openai.com/product/gpt-4) est l'outil de pointe d'OpenAI pour la génération de langage naturel alimenté par l'IA. Il peut effectuer diverses tâches linguistiques naturelles telles que la génération de texte, sa finalisation et sa classification. Nous l’avons inclus dans le tableau de bord de Braze pour vous aider à inspirer et à diversifier votre texte directement lorsque vous travaillez.

## Comment mes données sont-elles utilisées et envoyées à OpenAI ?

Braze envoie votre requête à OpenAI afin de pouvoir générer le texte. Toutes les requêtes envoyées à OpenAI depuis Braze sont anonymisées, ce qui signifie qu'OpenAI ne sera pas en mesure d'identifier l’origine de la requête, à moins que vous n'incluiez des informations identifiables dans les données que vous fournissez ou dans les données de vos compagnes antérieures si vous activez l’option « Faire référence aux données d’anciennes campagnes ». Conformément à la [politique d'OpenAI](https://openai.com/policies/api-data-usage-policies), les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer leurs modèles et seront supprimées après 30 jours. Entre vous et Braze, tout contenu généré à l'aide de GPT constitue votre propriété intellectuelle. Braze ne fera valoir aucune revendication de propriété intellectuelle sur ce contenu et ne donne aucune garantie de quelque nature que ce soit concernant tout contenu généré par l’IA.

## Plus d’outils IA

Vous pouvez également [générer une image à l'aide de l'intelligence artificielle]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai) à partir de la bibliothèque multimédia. Ce processus permet de tirer parti de [DALL·E 3](https://openai.com/index/dall-e-3/), un système IA d’OpenAI pouvant créer des images et des représentations artistiques réalistes à partir d’une description en langage naturel.

[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} « GPT3 »
