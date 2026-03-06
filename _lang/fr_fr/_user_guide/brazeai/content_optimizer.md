---
nav_title: Optimiseur de contenu
article_title: Optimiseur de contenu
alias: "/content_optimizer/"
description: "Content Optimizer est un agent qui vous aide à tester et à optimiser le contenu des messages à l'échelle, en utilisant l'intelligence artificielle pour générer et évaluer automatiquement de grands volumes de variantes de contenu."
page_type: reference
page_order: 4
---

# Optimiseur de contenu

> Content Optimizer est un agent qui vous aide à tester et à optimiser le contenu des messages à l'échelle, en utilisant l'intelligence artificielle pour générer et évaluer automatiquement de grands volumes de variantes de contenu.

{% alert important %}
Content Optimizer est actuellement en version bêta et n'est disponible que pour les messages e-mail. Pour obtenir de l'aide, contactez votre gestionnaire satisfaction client.
{% endalert %}

## A propos de Content Optimizer

Content Optimizer est un agent qui s'exécute dans une étape du canvas. Il vous aide à définir les composants des messages à tester, à générer des variantes à l'aide de l'intelligence artificielle générative ou d'une saisie manuelle, et à optimiser automatiquement les combinaisons de contenus qui sont envoyées aux utilisateurs. Cette fonctionnalité vous aide à :

- Optimisez les lignes d'objet, l'en-tête du corps, le contenu du corps ou le CTA principal des e-mails.
- Améliorez continuellement les performances de vos messages sans configuration manuelle de tests A/B.
- Testez rapidement de grands volumes de variantes de contenu, en tirant parti de l'intelligence artificielle pour l'idéation.
- Éliminez automatiquement les contenus peu performants et augmentez les contenus gagnants.

Découvrez comment créer une [étape de l'Optimiseur de contenu]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).

## Cas d’utilisation

### E-mail

| Cas d'utilisation de l'optimisation | Objectif | Description |
| --- | --- | --- |
| Variations de la ligne d'objet | Augmenter le taux d'ouverture | Testez le ton, l'urgence, la personnalisation et l'utilisation des emojis. |
| Styles d'envoi des messages dans les en-têtes | Stimulez l'engagement | Comparez les envois de messages émotionnels, axés sur la valeur des messages et clairs dans le corps de l'en-tête. | 
| Format du corps du texte | Améliorer la lisibilité et l'engagement | Testez la narration par rapport aux listes de fonctionnalités, les puces par rapport aux paragraphes et la longueur du contenu. |
| Copie du CTA & ton | Augmenter le nombre de clics | Comparez les formulations des CTA axées sur l'action, sur les avantages et sur la première personne. |
| Combinaisons de contenus thématiques | Découvrez les combinaisons les plus performantes | Mélangez les éléments du sujet, du corps de texte et du CTA pour trouver la meilleure combinaison possible. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Fonctionnement

L'optimiseur de contenu utilise un algorithme de [bandit multi-bras](https://en.wikipedia.org/wiki/Multi-armed_bandit) non contextuel pour attribuer plus d'envois aux variantes les plus performantes et réduire l'attribution aux variantes les moins performantes. Au fil du temps, il en résulte une amélioration continue du contenu de vos messages, avec une intervention manuelle minimale.

Lors du premier lancement de l'étape, Content Optimizer envoie des variantes de manière aléatoire pour collecter les données de performance initiales. Après cette période d'exploration initiale, l'algorithme commence à déplacer le trafic vers les combinaisons de contenu les plus performantes, en réduisant progressivement l'allocation aux options moins performantes. Pendant la période d'exploration, le trafic est généralement réparti entre les variantes disponibles pour permettre à l'algorithme d'apprendre de leurs performances relatives.

L'Optimiseur de contenu est similaire à l'étape du message dans Canvas, avec des fonctionnalités telles que les heures calmes, le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing) et l'enregistrement des événements. Vous pouvez configurer une étape de l'Optimiseur de contenu en créant un message de base et en définissant les composants du contenu (tels que la ligne d'objet, le corps du texte ou l'appel à l'action) à optimiser. Les variantes de chaque composant peuvent être générées par l'intelligence artificielle ou saisies manuellement, et des étiquettes Liquid doivent être ajoutées au message de base pour mapper les composants dans le contenu du message.

Chaque utilisateur reçoit un message par entrée dans l'étape de l'Optimiseur de contenu. Les réinscriptions sont traitées comme des nouveautés, sans mémoire des variantes précédentes.

Pour obtenir les meilleurs résultats, utilisez l'Optimiseur de contenu dans les canevas où les utilisateurs entrent progressivement dans l'étape, par exemple dans les canevas récurrents ou toujours actifs avec un volume quotidien constant. Si tous les utilisateurs entrent dans l'étape en même temps, l'agent n'aura pas le temps de tirer des enseignements des premiers résultats. L'étape se comportera davantage comme un test A/B statique que comme un moteur d'optimisation en ligne/en production/instantanée.

Cela signifie que vous pouvez toujours utiliser l'Optimiseur de contenu dans les Canvas à envoi unique ou à court terme, mais uniquement si les utilisateurs entrent dans l'étape sur une période prolongée (par exemple, par le biais d'une étape de retard, d'une entrée planifiée ou d'un flux déclenché par l'API). Veillez à ce que l'étape ait suffisamment de trafic et de temps pour observer les différences de performance avant d'atteindre la plupart des utilisateurs.


### Concepts clés

| Terme                    | Description |
|-------------------------|-------------|
| Message de base   | Le modèle de message principal à partir duquel les variantes sont créées, y compris tous les paramètres d'envoi. |
| Éléments de contenu  | Éléments d'un message (par exemple, ligne d'objet ou CTA principal) qui peuvent être testés et optimisés. Les marketeurs doivent insérer l'étiquette Liquid correspondante dans le message à l'endroit où le composant doit apparaître. |
| Variantes de contenu    | Les différentes valeurs que peut prendre un composant de contenu. |
| Combinaisons de contenus| Messages uniques créés par l'envoi de variantes de contenu. |
| Événement d'optimisation       | Détermine la manière dont Content Optimizer évalue les performances et attribue le trafic aux combinaisons de contenu au fil du temps, comme les clics ou les ouvertures pour les e-mails. S'applique à tous les éléments de contenu d'une étape. Content Optimizer tire continuellement des enseignements de cet événement et oriente automatiquement la réception/distribution vers des combinaisons de contenus plus performantes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Restrictions

- Content Optimizer est actuellement en version bêta et n'est disponible que pour les messages e-mail.
- L'agent peut générer jusqu'à 125 combinaisons par étape :
   - Jusqu'à 3 composants par étape
   - Jusqu'à 5 variantes pour chaque composant
- Un seul message est envoyé par utilisateur et par inscription. Il n'y a pas de mémoire des envois précédents pour les réinscriptions.
- Les marketeurs doivent insérer manuellement des étiquettes Liquid pour chaque composant dans le compositeur de messages où les variantes de composants de contenu définies doivent être rendues.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Étapes suivantes

- Contactez votre gestionnaire de la satisfaction client pour rejoindre la version bêta ou pour bénéficier d'une assistance à l'onboarding.
- Découvrez comment créer une [étape de l'Optimiseur de contenu]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).
