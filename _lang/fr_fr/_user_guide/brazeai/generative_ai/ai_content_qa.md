---
nav_title: "Assurance qualité du contenu avec l'IA"
article_title: "Assurance qualité du contenu avec l'IA"
page_order: 10
description: "Cet article de référence explique comment effectuer l'assurance qualité du contenu de vos messages à l'aide de l'IA, directement à partir du composeur de messages."
---

# Assurance qualité du contenu avec l'IA

> Découvrez comment effectuer l’assurance qualité du contenu de vos messages avec l'IA, directement depuis le compositeur de messages.

L'assurance qualité du contenu avec l'IA utilise les capacités de GPT et d'OpenAI pour effectuer des vérifications sur le contenu de votre message et s'assurer qu'il respecte les normes de qualité en identifiant les éléments inefficaces, tels que les fautes d'orthographe, les problèmes de grammaire, le ton inapproprié et le langage offensant. Vous pouvez accéder à cette fonctionnalité depuis l'onglet **Test** lors de la composition d'une notification push, d’un SMS ou d’un message in-app dans une campagne ou un canvas.

## Principales fonctionnalités

L'assurance qualité du contenu avec l'IA offre les fonctionnalités clés suivantes pour améliorer la qualité du contenu de vos messages :

- **Vérification de l'orthographe et de la grammaire :** Vérifie automatiquement si votre message contient des fautes d'orthographe et de grammaire. L’outil suggère des corrections et formule des recommandations pour améliorer l’exactitude générale du contenu.
- **Analyse du ton :** Évalue le ton du message afin d'identifier tout problème potentiel. Ceci permet de s'assurer que le ton employé correspond au style de communication souhaité et d'éviter les malentendus ou les propos involontairement blessants.
- **Détection du langage offensant :** Analyse votre message pour détecter tout langage potentiellement offensant ou inapproprié, ce qui vous permet de réviser votre contenu et de maintenir une communication respectueuse.
- **Vérification du contenu inséré accidentellement :** Détecte toute inclusion de code, de langage de balisage ou de messages de test qui auraient pu être ajoutés involontairement, y compris tout code Liquid qui n'a pas été rendu pour un utilisateur test.

## Accéder à l'assurance qualité du contenu avec l’IA

{% alert note %}
Pour le moment, l'assurance qualité du contenu avec l’IA est uniquement disponible pour les canaux de notification push et SMS.
{% endalert %}

Pour accéder au vérificateur de contenu, procédez comme suit :

1. Après avoir composé une notification push ou un message SMS, sélectionnez l'onglet **Test**.
2. Recherchez la section **Assurance qualité du contenu avec l’IA**.
3. Cliquez sur **Tester le contenu**.

![Section AQ du contenu avec l’IA dans l’onglet Test.][1]{: style="max-width:60%"}

### Prise en charge linguistique

GPT est capable de comprendre [plusieurs langues](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages), même si OpenAI ne les prend pas officiellement en charge. Lorsque le contenu du message est envoyé à OpenAI, Braze ne transmet aucune information supplémentaire sur la langue ou le caractère régional de votre texte. C'est donc à GPT de déterminer cela.

Les résultats peuvent varier en fonction de la langue dans laquelle vous écrivez.

## Conseils pour une utilisation efficace

Tenez compte des conseils suivants pour valoriser au maximum la fonctionnalité d'assurance qualité du contenu avec l’IA :

- **Relire votre message :** Bien que le vérificateur de contenu puisse aider à identifier les erreurs, une relecture de votre contenu reste essentielle. Les suggestions générées par l'intelligence artificielle peuvent s’avérer un guide utile, mais faites preuve de discernement afin de garantir l’exactitude de votre texte.
- **Comprendre l'analyse du ton :** Les résultats de l'analyse du ton du texte sont subjectifs et basés sur la compréhension du modèle d'IA. Bien qu'ils puissent fournir des informations utiles, tenez compte du ton que vous souhaitez adopter et du contexte de la conversation pour procéder aux ajustements nécessaires.
- **Vérifier minutieusement le langage offensant signalé :** La détection du langage offensant est conçue pour être robuste, mais il peut arriver qu'elle signale certains faux positifs. Examinez attentivement les sections signalées et apportez les modifications nécessaires.

## Comment mes données sont-elles utilisées et envoyées à OpenAI ?

Braze l'envoie votre message à la plateforme API d'OpenAI dans le but d’en vérifier le contenu. Toutes les requêtes envoyées à OpenAI depuis Braze sont anonymisées, ce qui signifie qu'OpenAI ne sera pas en mesure d'identifier l’origine de la requête, à moins que vous n'incluiez des informations identifiables dans le contenu de message que vous fournissez. Comme décrit dans les [engagements de la plateforme API d’OpenAI](https://openai.com/policies/api-data-usage-policies), les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer leurs modèles et seront supprimées après 30 jours. Veuillez vous assurer que vous respectez les politiques d'OpenAI qui vous concernent, lesquelles peuvent inclure sa [politique d'utilisation](https://openai.com/policies/usage-policies) et sa [politique en matière de partage et de publication](https://openai.com/policies/sharing-publication-policy). Braze n'offre aucune garantie de quelque nature que ce soit en ce qui concerne tout contenu généré par l'IA.

[1]: {% image_buster /assets/img/content_qa_ai.png %}
