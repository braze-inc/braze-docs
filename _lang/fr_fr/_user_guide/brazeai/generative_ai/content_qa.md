---
nav_title: Assurance qualité du contenu
article_title: "Assurance qualité du contenu avec l'IA"
page_order: 4
description: "Cet article de référence explique comment effectuer l'assurance qualité du contenu de vos messages à l'aide de l'IA, directement à partir du composeur de messages."
---

# Assurance qualité du contenu avec <sup>BrazeAITM</sup>

> Apprenez à contrôler votre contenu avec <sup>BrazeAITM</sup>, afin de détecter les fautes d'orthographe, les problèmes de grammaire, le ton inapproprié ou le langage offensant, avant d'appuyer sur le bouton d'envoi.

## Fonctionnalités prises en charge

Les fonctionnalités suivantes sont prises en charge pour améliorer la qualité de votre contenu :

| Fonctionnalité                     | Description |
|----------------------------|-------------|
| Vérification de l'orthographe et de la grammaire | Vérifie automatiquement si votre message contient des fautes d'orthographe et de grammaire. L’outil suggère des corrections et formule des recommandations pour améliorer l’exactitude générale du contenu. |
| Analyse de la tonalité              | Évalue le ton du message afin d'identifier tout problème potentiel. Ceci permet de s'assurer que le ton employé correspond au style de communication souhaité et d'éviter les malentendus ou les propos involontairement blessants. |
| Détection du langage offensant | Analyse votre message pour détecter tout langage potentiellement offensant ou inapproprié, ce qui vous permet de réviser votre contenu et de maintenir une communication respectueuse. |
| Vérification accidentelle du contenu   | Détecte toute inclusion de code, de langage de balisage ou de messages de test qui auraient pu être ajoutés involontairement, y compris tout code Liquid qui n'a pas été rendu pour un utilisateur test. |
| Prise en charge multilingue     | Bien qu'il ne soit pas officiellement pris en charge par l'OpenAI, le GPT peut comprendre [plusieurs langues](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages). Gardez à l'esprit que Braze ne transmet aucune information sur la langue ou la locale de votre copie lorsqu'elle est envoyée à OpenAI, de sorte que vos résultats peuvent varier en fonction de la langue dans laquelle vous écrivez. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Utiliser <sup>BrazeAITM</sup> pour l'assurance qualité du contenu

{% alert note %}
Cette fonctionnalité n'est disponible que pour les canaux SMS, Android push et iOS push pour le moment.
{% endalert %}

1. Après avoir composé un message mobile push ou SMS, accédez à l'onglet **Test**.
2. Recherchez la section **Assurance qualité du contenu avec l’IA**.
3. Cliquez sur **Tester le contenu**.

![AQ du contenu avec la section intelligence artificielle de l'onglet Test.]({% image_buster /assets/img/content_qa_ai.png %})

## Bonnes pratiques

Tenez compte des éléments suivants, afin de tirer le meilleur parti de l'assurance qualité du contenu avec l'intelligence artificielle :

- **Relire votre message :** Bien que le vérificateur de contenu puisse aider à identifier les erreurs, une relecture de votre contenu reste essentielle. Les suggestions générées par l'intelligence artificielle peuvent s’avérer un guide utile, mais faites preuve de discernement afin de garantir l’exactitude de votre texte.
- **Comprendre l'analyse du ton :** Les résultats de l'analyse du ton du texte sont subjectifs et basés sur la compréhension du modèle d'IA. Bien qu'ils puissent fournir des informations utiles, tenez compte du ton que vous souhaitez adopter et du contexte de la conversation pour procéder aux ajustements nécessaires.
- **Vérifier minutieusement le langage offensant signalé :** La détection du langage offensant est conçue pour être robuste, mais il peut arriver qu'elle signale certains faux positifs. Examinez attentivement les sections signalées et apportez les modifications nécessaires.

{% multi_lang_include brazeai/generative_ai/policy.md %}
