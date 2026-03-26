---
nav_title: Rédaction
article_title: Assistant de rédaction IA
page_order: 2.1
description: "Cet article de référence présente l'assistant de rédaction basé sur l'intelligence artificielle, une fonctionnalité qui transmet un nom de produit ou une description à l'outil de génération de texte GPT d'OpenAI pour produire un texte marketing au style naturel, que vous pourrez ensuite utiliser dans vos messages."
---

# Générer du contenu avec BrazeAI

> L'assistant de rédaction basé sur l'intelligence artificielle transmet un bref nom ou une brève description de produit à l'outil de génération de textes GPT du fournisseur OpenAI, afin de produire des textes marketing au style naturel que vous pouvez utiliser dans vos messages. Cette fonctionnalité est disponible par défaut pour la plupart des composeurs de messages dans le tableau de bord de Braze.

## Générer un texte

### Étape 1 : Lancer le rédacteur IA

Dans votre composeur de messages, sélectionnez <i class="fa-solid fa-wand-magic-sparkles"></i> **Lancer le rédacteur IA**.

Dans l'éditeur par glisser-déposer pour les messages in-app, sélectionnez un bloc de texte puis cliquez sur <i class="fa-solid fa-wand-magic-sparkles" title="Rédacteur IA"></i> dans la barre d'outils du bloc.

### Étape 2 : Saisissez les détails

Saisissez un nom ou une description de produit dans le champ prévu, puis sélectionnez une longueur de sortie approximative.

Vous pouvez choisir un canal spécifique pour obtenir une longueur de sortie basée sur les bonnes pratiques propres à ce canal, ou opter pour court (1 phrase), moyen (2-3 phrases) ou long (1 paragraphe).

### Étape 3 : Personnalisez davantage (facultatif)

Pour affiner votre texte, vous pouvez :

- **Appliquer des directives de marque :** Après avoir [créé des directives de marque avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), vous pouvez les utiliser pour orienter la génération de votre texte.
- **Choisir un ton :** Chaque ton génère un texte dans un style différent. Choisissez celui qui correspond le mieux à la voix de votre marque.
  
  La sélection d'un ton ajoute une instruction de style au prompt envoyé à OpenAI. Le résultat exact peut donc varier en fonction du contenu saisi, de la longueur du canal, des directives de marque et du modèle utilisé. 
  
  Voici ce que chaque ton est censé produire par défaut :
  - **Formel :** Un vocabulaire plus professionnel et soigné. Des phrases complètes, un langage plus courtois, un minimum d'argot.
  - **Direct :** Plus concis et sans détour. Moins d'adjectifs, moins de « jargon marketing », des appels à l'action plus clairs.
  - **Décontracté :** Plus détendu et conversationnel. Des formulations plus amicales, des mots plus simples, une énergie plus légère.
  - **Personnel :** Plus intime et empathique. Utilise davantage le « vous », donne une impression plus sur mesure, surtout si vous ajoutez de la personnalisation comme {% raw %}`{{${first_name}}}`{% endraw %} au message que vous créez.
  - **Accrocheur :** Plus percutant et captivant. Des formulations plus incisives, une énergie plus forte, des accroches et des CTA plus marqués (le résultat a souvent un ton plus « promotionnel » que les autres).
  - **Sophistiqué :** Un langage plus élégant et raffiné. Moins familier, un positionnement plus « premium ».
  - **Professionnel :** Un ton business et clair. Plus moderne et accessible que le ton formel, tout en conservant une certaine autorité.
  - **Passif :** Un langage plus doux et moins insistant. Moins d'injonctions directes, des formulations plus suggestives.
  - **Urgent :** Met l'accent sur l'immédiateté et le sentiment d'urgence. Des CTA plus forts, des échéances, des indices de rareté.
  - **Enthousiaste :** Plus énergique et dynamique. Met en avant les émotions positives et la célébration (souvent plus axé sur l'engouement que l'approche par l'accroche du ton « Accrocheur »).
 
  
- **Faire référence aux données de campagnes précédentes :** Lorsque cette option est activée, les notifications push mobiles précédemment envoyées via vos campagnes ou étapes du canvas servent de référence stylistique pour générer votre nouveau texte. Pour en savoir plus, consultez la section [Utilisation des données de campagnes précédentes](#past-campaign-data).
- **Traduction automatique du texte :** Vous pouvez choisir une langue de sortie différente pour votre texte. Le contenu généré sera produit dans cette langue.

### Étape 4 : Générez votre texte

Lorsque vous avez terminé, sélectionnez **Générer**. Les informations fournies seront transmises à GPT pour rédiger un texte à votre place. La réponse sera récupérée auprès d'OpenAI et mise à votre disposition. Pour en savoir plus, consultez la rubrique [Comment mes données sont-elles utilisées et envoyées à OpenAI ?](#ai-policy)

![Fenêtre modale de l'assistant de rédaction IA montrant les différentes fonctionnalités disponibles]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
Nous filtrons les réponses contenant du contenu offensant qui enfreint la [politique de contenu](https://beta.openai.com/docs/usage-guidelines/content-policy) d'OpenAI.
{% endalert %}

## À propos des données de campagnes précédentes {#past-campaign-data}

Lorsque vous utilisez push comme longueur de sortie et que vous sélectionnez **Faire référence aux données de campagnes précédentes**, des campagnes push mobiles précédentes sélectionnées aléatoirement seront envoyées à OpenAI afin que GPT puisse s'en servir comme base pour la génération du texte. Actuellement, le rédacteur IA envoie à OpenAI uniquement les campagnes push qui ne contiennent pas de syntaxe Liquid. Ne cochez pas cette case si vous ne souhaitez pas utiliser cette fonctionnalité. Consultez les sections suivantes pour en savoir plus sur la façon dont Braze et OpenAI utilisent vos données. 

Si cette fonctionnalité est utilisée conjointement avec une [directive de marque]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/), la directive de marque et les données de campagnes précédentes seront toutes deux intégrées au texte final généré.

{% multi_lang_include brazeai/generative_ai/policy.md %}