---
nav_title: Assistant rédaction IA
article_title: Assistant rédaction IA
page_order: 4
description: "L’assistant rédaction IA transmet un nom de produit bref ou une description à l’outil de génération de texte GPT3 de OpenAI pour générer un texte marketing semblable à celui produit par un humain pour une utilisation dans votre messagerie."

---

# Assistant rédaction IA

L’assistant rédaction IA transmet un nom de produit bref ou une description à l’outil de génération de texte GPT3 de OpenAI pour générer un texte marketing semblable à celui produit par un humain pour une utilisation dans votre envoi de messages. Cette fonctionnalité est disponible par défaut pour la plupart des composeurs de messages dans le tableau de bord de Braze.

## Étapes

Pour générer une copie à l’aide de l’assistant de rédaction IA, procédez comme suit :

1. Dans votre composeur de messages, sélectionnez <i class="fa-solid fa-wand-magic-sparkles"></i> **Lancer l’IA de rédaction**.
2. Saisissez un nom ou une description de produit dans le champ de saisie.
3. Sélectionnez la langue de sortie. Elle peut être différente de votre langue de saisie.
4. Sélectionnez une longueur de sortie approximative. Ces longueurs sont basées sur les meilleures pratiques pour chaque canal.
5. Cliquez sur **Generate Copy (Générer une copie)**.

La réponse sera récupérée depuis OpenAI et vous sera fournie. N’hésitez pas à expérimenter et à essayer toutes les variations de contenu que vous désirez.

![Le modal de l’assistant rédaction IA, montrant l’entrée « Automatisation du marketing Braze », qui a généré la sortie : « Vous cherchez à passer votre marketing au niveau supérieur ? L’automatisation du marketing Braze est la solution pour vous ! Grâce à nos outils puissants, vous pourrez créer, envoyer et suivre facilement vos campagnes marketing. Alors pourquoi attendre ? Inscrivez-vous dès aujourd’hui et voyez les résultats par vous-même ! »][1]

Ce que nous faisons en coulisses est de demander à GPT3 de « générer une copie marketing pour » votre nom de produit. Aucune autre personnalisation n’est effectuée. Le reste est la magie de GPT3 !

{% alert important %}
Nous filtrons les réponses présentant un contenu offensant qui viole la [politique de contenu](https://beta.openai.com/docs/usage-guidelines/content-policy) d’OpenAI.
{% endalert %}

## Qu’est-ce que GPT3 ?

[GPT3](https://openai.com/blog/gpt-3-apps/) est l’outil de génération d’expressions naturelles, à la pointe de la technologie, d’OpenAI alimenté par l’intelligence artificielle. Il peut effectuer diverses tâches linguistiques naturelles telles que la génération de texte, sa finalisation et sa classification. Nous l’avons inclus dans le tableau de bord de Braze pour vous aider à inspirer et à diversifier votre texte directement lorsque vous travaillez.

## Plus d’outils IA

Vous pouvez également [générer une image à l’aide de l’IA]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai) à partir de la bibliothèque multimédia. Ce processus permet de tirer parti de DALL·E 2, un système IA d’OpenAI pouvant créer des images et des représentations artistiques réalistes à partir d’une description en langage naturel.

[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"
