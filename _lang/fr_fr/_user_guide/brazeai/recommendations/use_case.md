---
nav_title: "Cas d'utilisation"
article_title: "Cas d'utilisation Piloter la découverte de contenu après visionnage"
description: "Cet exemple montre comment une marque fictive utilise les recommandations d'articles de l'intelligence artificielle de Braze pour offrir un contenu personnalisé et des recommandations de produits à travers des moments clés pour les clients."
page_type: tutorial
---

# Cas d'utilisation : Favoriser la découverte du contenu après sa visualisation

> Cet exemple montre comment une marque fictive utilise les recommandations d'articles de l'intelligence artificielle de Braze pour offrir un contenu personnalisé et des recommandations de produits à travers des moments clés pour les clients. Découvrez comment la logique de recommandation peut améliorer l'engagement, augmenter les conversions et réduire les efforts manuels.

Imaginons que Camila soit gestionnaire CRM chez MovieCanon, une plateforme de streaming proposant des films et des séries sélectionnés. 

L'objectif de Camila est de maintenir l'intérêt des téléspectateurs après qu'ils aient fini de regarder quelque chose. Jusqu'à présent, les messages "You might also like" de MovieCanon étaient basés sur des correspondances de genre et envoyés à des moments arbitraires, souvent des heures ou des jours après une session. Le taux d'engagement était faible et son équipe savait qu'elle pouvait faire mieux.

En utilisant les [recommandations d'éléments d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/), Camila met en place un système pour recommander automatiquement de nouveaux titres en fonction de l'historique de visionnage de chaque spectateur, délivrés immédiatement après que l'utilisateur a terminé un film ou un épisode. C'est une façon plus intelligente et plus personnalisée d'aider les utilisateurs à découvrir du contenu qu'ils voudront réellement regarder ensuite et de maintenir leur engagement sur la plateforme.

\![Message in-app lisant "Prochaine étape, juste pour vous. Parce que vous avez regardé "Nomads of the Sun", avec une image, un titre, une description et un CTA pour "Regarder maintenant" ou "Passer" à la recommandation suivante.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

Ce tutoriel explique comment Camila :

- Un message personnalisé déclenché lorsqu'un utilisateur finit de regarder quelque chose.
- Recommandations adaptées aux préférences du spectateur - automatiquement extraites du catalogue de MovieCanon et insérées dans le message. 

## Étape 1 : Créer un modèle de prédiction du taux d'attrition

Camila commence par créer une recommandation qui fera apparaître des titres pertinents chaque fois qu'un utilisateur finit de regarder quelque chose. Elle souhaite qu'il soit dynamique, afin que les utilisateurs reçoivent des suggestions différentes en fonction de ce qu'ils ont regardé récemment.

1. Dans le tableau de bord de Braze, Camila navigue jusqu'à **Recommandations d'éléments d'intelligence artificielle**.
2. Elle crée une nouvelle recommandation et la nomme "Suggestions après visionnage".
3. Pour le type de recommandation, elle choisit **Intelligence artificielle personnalisée**, afin que chaque utilisateur voie des recommandations sur mesure basées sur ses comportements passés.
4. Elle sélectionne l'option **Ne pas recommander les éléments avec lesquels les utilisateurs ont déjà interagi**, afin que les utilisateurs ne reçoivent pas de recommandations pour quelque chose qu'ils ont déjà regardé. 
5. Elle sélectionne le catalogue contenant la bibliothèque de contenu actuelle de MovieCanon. Camila n'ajoute pas de sélection de catalogue, car elle souhaite que tous les articles du catalogue soient éligibles à la recommandation.
6. Camila relie la recommandation à l'événement personnalisé `Watched Content`, qui permet de suivre les affichages terminés, et définit le **nom de la propriété** comme étant le titre du contenu.
7. Elle crée la recommandation.

## Étape 2 : Créer un message in-app

Une fois l'entraînement de la recommandation terminé, Camila crée un flux d'envoi de messages qui atteint l'utilisateur au bon moment : immédiatement après qu'il a terminé un titre. Le message comprend une liste de trois suggestions personnalisées tirées directement du catalogue.

1. Camila crée une campagne de messages in-app à l'aide de l'éditeur par glisser-déposer.
2. Elle associe le déclencheur à son événement personnalisé : `Watched Content`.
3. Elle conçoit un message in-app de plusieurs pages avec des images de titre, des noms et un CTA "Regarder maintenant".

! la fenêtre modale/boîte de dialogue "Ajouter une personnalisation" s'ouvre dans l'éditeur Braze, avec "Recommandation d'article" sélectionné comme type de personnalisation.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. Dans le corps du message, Camila utilise la [fenêtre modale/boîte de dialogue de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) pour ajouter des variables telles que le nom, la description et la vignette du titre recommandé à l'aide de Liquid, qui alimente dynamiquement le contenu du catalogue. Elle a créé un attribut personnalisé pour `Last Watched Movie` afin d'indiquer aux utilisateurs que cette recommandation est basée sur l'historique de leurs montres. 

L'éditeur de messages in-app avec le liquide brut pour modéliser dans des champs spécifiques des éléments du catalogue de la recommandation.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

{% details Show Liquid used in image %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. Camila duplique ensuite sa page et incrémente le tableau Liquid {% raw %} (`{{ items[0]}}` to `{{items[1]}}`) {% endraw %} dans chaque variable pour insérer le modèle dans l'élément suivant de la liste de recommandations.

## Étape 3 : Mesurer et optimiser

Une fois la campagne en ligne/en production/instantanée, Camila surveille les taux d'ouverture, les CTR et les comportements de visionnage ultérieurs. Elle compare les performances aux campagnes de recommandations statiques précédentes et constate un engagement plus important, ainsi qu'un plus grand nombre de sessions de contenu par utilisateur.

Elle prévoit également de procéder à des tests A/B :

- Délai (immédiat ou 10 minutes après le visionnage)
- Disposition du contenu (carrousel ou liste)
- Variations des CTA ("Regarder maintenant" ou "Ajouter à la file d'attente")

En associant l'envoi de messages pilotés par les événements aux recommandations d'articles par l'intelligence artificielle, Camila transforme la découverte de contenu en une expérience automatique et personnalisée. MovieCanon maintient l'intérêt des utilisateurs sans les désabonner, en leur fournissant un contenu pertinent au bon moment.





