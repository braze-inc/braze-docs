---
nav_title: Optimiseur de contenu
article_title: Optimiseur de contenu
alias: "/content_optimizer/"
description: "Content Optimizer est un outil qui vous aide à tester et à optimiser le contenu de vos messages à grande échelle, en utilisant l'intelligence artificielle pour générer et évaluer automatiquement de grands volumes de variantes de contenu."
page_type: reference
page_order: 3
---

# Optimiseur de contenu

> Content Optimizer est un outil qui vous aide à tester et à optimiser le contenu de vos messages à grande échelle, en utilisant l'intelligence artificielle pour générer et évaluer automatiquement de grands volumes de variantes de contenu.

{% alert important %}
Content Optimizer est actuellement en version bêta et n'est disponible que pour les messages d'e-mail. Pour obtenir de l'aide pour démarrer, veuillez contacter votre gestionnaire de la satisfaction client.
{% endalert %}

## À propos de l'optimiseur de contenu

Content Optimizer est un agent qui s'exécute dans une étape du canvas. Il vous aide à définir les composants du message à tester, à générer des variantes à l'aide de l'intelligence artificielle générative ou d'une saisie manuelle, et à optimiser automatiquement les combinaisons de contenu envoyées aux utilisateurs. Cette fonctionnalité vous permet de :

- Optimisez les lignes d'objet, l'en-tête, le contenu ou l'appel à l'action principal des e-mails.
- Améliorez continuellement les performances de vos messages sans avoir à réaliser manuellement la configuration des tests A/B.
- Testez rapidement de grands volumes de variantes de contenu en utilisant l'intelligence artificielle pour la conceptualisation.
- Supprimez automatiquement les contenus peu performants et développez ceux qui ont du succès.

Découvrez comment créer une [étape d'optimisation de contenu]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).

## Cas d’utilisation

### E-mail

| Cas d'utilisation de l'optimisation | Objectif | Description |
| --- | --- | --- |
| Variantes de la ligne d'objet | Augmenter le taux d’ouverture | Ton de test, urgence, personnalisation et utilisation d'émojis. |
| Styles d'envoi de messages d'en-tête | Renforcez l'engagement | Veuillez comparer les messages émotionnels, axés sur les valeurs et clairs dans l'en-tête du corps du texte. | 
| Format du contenu du corps | Améliorer la lisibilité et l'engagement | Testez la narration par rapport aux listes de fonctionnalités, les puces par rapport aux paragraphes et la longueur du contenu. |
| Ton du& texte CTA | Augmenter les clics | Veuillez comparer les formulations d'appel à l'action axées sur l'action, axées sur les avantages et à la première personne. |
| Combinaisons de contenus thématiques | Découvrez des combinaisons performantes | Combinez les éléments thématiques, le corps du texte et les composants CTA afin de déterminer la meilleure combinaison globale. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Fonctionnement

Content Optimizer utilise un algorithme [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) non contextuel pour attribuer davantage d'envois aux variantes les plus performantes et réduire l'attribution aux variantes moins performantes. Au fil du temps, cela se traduit par une amélioration continue du contenu de vos messages, avec une intervention manuelle minimale.

L'algorithme d'optimisation Bandit exclusif de Braze est spécialement créé pour la nature combinatoire de l'étape d'optimisation du contenu. Étant donné que chaque message est composé de plusieurs éléments, le système apprend simultanément les performances de chaque élément (tel que la ligne d'objet, le corps du message, le CTA) ainsi que leurs interactions lorsqu'ils sont combinés dans un message. Plus précisément, lorsqu'une combinaison donnée est envoyée, toutes les combinaisons qui partagent les mêmes composants bénéficient des données de cet envoi. Cela permet au bandit d'apprendre beaucoup plus rapidement à partir d'une même quantité de données, par rapport à un algorithme bandit standard.

Lorsque l'étape est lancée pour la première fois, Content Optimizer envoie des variantes de manière aléatoire afin de collecter des données de performance initiales. Après cette période d'exploration initiale, l'algorithme commence à rediriger le trafic vers les combinaisons de contenus les plus performantes, réduisant progressivement l'allocation aux options moins performantes. Pendant la période d'exploration, le trafic est généralement réparti entre les variantes disponibles afin de permettre à l'algorithme d'apprendre à partir de leurs performances respectives.

Content Optimizer est similaire à l'étape Message dans Canvas, avec des fonctionnalités telles que les heures calmes, [le timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing) et la journalisation des événements. Vous pouvez configurer une étape d'optimisation de contenu en créant un message de base et en définissant les composants de contenu (tels que la ligne d'objet, le corps du texte ou l'appel à l'action) à optimiser. Les variantes pour chaque composant peuvent être générées à l'aide de l'intelligence artificielle ou saisies manuellement, et des étiquettes Liquid doivent être ajoutées au message de base afin de réaliser le mappage des composants dans le contenu du message.

Chaque utilisateur reçoit un message par entrée dans l'étape Optimiseur de contenu. Les réinscriptions sont considérées comme nouvelles, sans référence aux variantes précédentes.

Pour obtenir les meilleurs résultats, veuillez utiliser l'optimiseur de contenu dans les canevas où les utilisateurs entrent progressivement au fil du temps, par exemple dans les canevas récurrents ou toujours actifs avec un volume quotidien constant. Si tous les utilisateurs passent à l'étape suivante simultanément, l'agent n'aura pas le temps de tirer des enseignements des premiers résultats. Cette étape s'apparentera davantage à un test A/B statique qu'à un moteur d'optimisation en ligne/en production/instantané.

Cela signifie que vous pouvez toujours utiliser Content Optimizer dans des canevas à envoi unique ou à court terme, mais uniquement si les utilisateurs passent à l'étape suivante sur une période prolongée (par exemple, via une étape de délai, une entrée de planification ou un flux déclenché par un déclencheur d'API). Veuillez vous assurer que l'étape dispose d'un trafic suffisant et d'un délai adéquat pour observer les différences de performances avant d'atteindre la majorité des utilisateurs.

### Concepts clés

| Terme                    | Description |
|-------------------------|-------------|
| Message de base   | Modèle de message principal à partir duquel les variantes sont créées, y compris tous les paramètres d'envoi. |
| Éléments de contenu  | Éléments d'un message (par exemple, ligne d'objet ou CTA principal) pouvant être testés et optimisés. Les marketeurs doivent insérer l'étiquette Liquid appropriée dans le message à l'endroit où le composant doit apparaître. |
| Variantes de contenu    | Les différentes valeurs qu'un composant de contenu peut prendre. |
| Combinaisons de contenu| Messages uniques créés en combinant et en assortissant différentes variantes de contenu. |
| Événement d'optimisation       | Détermine la manière dont Content Optimizer évalue les performances et répartit le trafic vers les combinaisons de contenus au fil du temps, par exemple les clics ou les ouvertures pour les e-mails. S'applique à tous les composants de contenu d'une étape. Content Optimizer tire continuellement des enseignements de cet événement et oriente automatiquement la réception/distribution vers des combinaisons de contenus plus performantes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Restrictions

- Content Optimizer est actuellement en version bêta et n'est disponible que pour les messages d'e-mail.
- L'agent peut générer jusqu'à 125 combinaisons par étape :
   - Jusqu'à 3 composants par étape
   - Jusqu'à 5 variantes pour chaque composant
- Un seul message est envoyé par utilisateur et par entrée. Il n'y a pas de trace des envois précédents pour les nouvelles entrées.
- Les marketeurs doivent insérer manuellement des étiquettes Liquid pour chaque composant dans l'éditeur de message où les variantes de composant de contenu définies doivent s'afficher.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Étapes suivantes

- Veuillez contacter votre gestionnaire de la satisfaction client pour participer à la version bêta ou pour obtenir une assistance à l'onboarding.
- Découvrez comment créer une [étape d'optimisation de contenu]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).
