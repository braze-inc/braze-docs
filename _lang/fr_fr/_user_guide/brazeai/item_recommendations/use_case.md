---
nav_title: Cas d’utilisation
article_title: "Cas d'utilisation : découverte de contenu après visionnage"
description: "Cet exemple illustre comment une marque fictive utilise les recommandations d'articles basées sur l'intelligence artificielle de Braze pour proposer du contenu personnalisé et des recommandations de produits à des moments clés pour les clients."
page_type: tutorial
---

# Cas d’utilisation : Favorisez la découverte de contenu après le visionnage

> Cet exemple illustre comment une marque fictive utilise les recommandations d'articles basées sur l'intelligence artificielle de Braze pour proposer du contenu personnalisé et des recommandations de produits à des moments clés pour les clients. Découvrez comment la logique de recommandation peut améliorer l'engagement, augmenter les conversions et réduire les efforts manuels.

Supposons que Camila occupe le poste de gestionnaire CRM chez MovieCanon, une plateforme de streaming proposant une sélection de films et de séries. 

L'objectif de Camila est de maintenir l'intérêt des spectateurs après qu'ils aient terminé de regarder un contenu. Historiquement, les messages « Vous pourriez également aimer » de MovieCanon étaient basés sur une correspondance générique large et envoyés à des moments arbitraires, souvent plusieurs heures ou jours après une session. L'engagement était faible, et son équipe était consciente qu'elle pouvait faire mieux.

Grâce [aux recommandations d'articles basées sur l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/), Camila met en place un système qui recommande automatiquement de nouveaux titres en fonction de l'historique de chaque spectateur, immédiatement après qu'un utilisateur a terminé un film ou un épisode. Il s'agit d'une méthode plus intelligente et plus personnalisée pour aider les utilisateurs à découvrir le contenu qu'ils souhaitent réellement regarder ensuite et les fidéliser à la plateforme.

![Message in-app indiquant « À suivre, spécialement pour vous. » Parce que vous avez visionné « Nomads of the Sun », avec une image, un titre, une description et un appel à l'action « Regarder maintenant » ou « Passer » pour passer à la recommandation suivante.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

Ce tutoriel explique comment Camila :

- Un message personnalisé qui s'affiche lorsqu'un utilisateur termine de visionner un contenu.
- Recommandations adaptées aux préférences du spectateur, automatiquement extraites du catalogue MovieCanon et intégrées au message. 

## Étape 1 : Créer un modèle de prédiction du taux de désabonnement

Camila commence par créer une recommandation qui affichera des titres pertinents chaque fois qu'un utilisateur aura terminé de regarder un contenu. Elle souhaite que ce soit dynamique, afin que les utilisateurs reçoivent différentes suggestions en fonction de ce qu'ils ont récemment regardé.

1. Dans le tableau de bord de Braze, Mme Camila accède à **la section « Recommandations d'articles par intelligence artificielle** ».
2. Elle crée une nouvelle recommandation et la nomme « Suggestions après visionnage ».
3. Pour le type de recommandation, elle choisit « **Personnalisée par intelligence artificielle** », de sorte que chaque utilisateur voit des recommandations adaptées en fonction de ses comportements passés.
4. Elle sélectionne **« Ne pas recommander les éléments avec lesquels les utilisateurs ont déjà interagi** » afin que les utilisateurs ne reçoivent pas de recommandations pour des contenus qu'ils ont déjà visionnés. 
5. Elle sélectionne le catalogue contenant la bibliothèque de contenu actuelle de MovieCanon. Camila n'ajoute pas de sélection au catalogue, car elle souhaite que tous les articles du catalogue puissent être recommandés.
6. Camila associe la recommandation à l'événement`Watched Content`personnalisé, qui suit les vues terminées, et définit le **nom de la propriété** sur le titre du contenu.
7. Elle formule la recommandation.

## Étape 2 : Configurer un message in-app

Une fois la recommandation formée, Camila crée un flux d'envoi de messages qui parvient à l'utilisateur au moment opportun : immédiatement après qu'il ait terminé un titre. Le message comprend une liste de trois suggestions de personnalisation extraites directement du catalogue.

1. Camila crée une campagne de messages in-app à l'aide de l'éditeur par glisser-déposer.
2. Elle définit le déclencheur de son événement personnalisé : `Watched Content`.
3. Elle conçoit un message in-app de plusieurs pages avec des images de titre, des noms et un CTA « Regarder maintenant ».

![La fenêtre modale « Ajouter une personnalisation » s'ouvre dans l'éditeur Braze, avec « Recommandation d'articles » sélectionné comme type de personnalisation.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. Dans le corps du message, Camila utilise la fenêtre [modale Ajouter une personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) pour ajouter des variables telles que le nom, la description et la vignette du titre recommandé à l'aide de Liquid, qui remplit dynamiquement le contenu à partir du catalogue. Elle crée un modèle dans un attribut personnalisé pour`Last Watched Movie`informer les utilisateurs que cette recommandation est basée sur leur historique de visionnage. 

![Éditeur de messages in-app avec Liquid brut pour créer des modèles dans des champs spécifiques à partir des articles du catalogue issus de la recommandation.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

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

5. Camila duplique ensuite sa page et incrémente le tableau liquid{% raw %} (`{{ items[0]}}`to`{{items[1]}}`){% endraw %}dans chaque variable pour créer un modèle dans l'élément suivant de la liste de recommandations.

## Étape 3 : Mesurer et optimiser

Une fois la campagne en ligne/en production/instantanée, Camila surveille les taux d’ouverture, les CTR et le comportement des utilisateurs après le visionnage. Elle compare les performances par rapport aux campagnes de recommandations statiques précédentes et constate un engagement plus élevé, ainsi qu'un plus grand nombre de sessions de contenu par utilisateur.

Elle prévoit également de réaliser un test A/B :

- Moment choisi (immédiatement après la surveillance ou 10 minutes après)
- Disposition du contenu (carrousel ou liste)
- Variantes de CTA (« Regarder maintenant » ou « Ajouter à la file d'attente »)

En associant l'envoi de messages événementiels aux recommandations d'articles basées sur l'intelligence artificielle, Camila transforme la découverte de contenu en une expérience automatisée et de personnalisation. MovieCanon maintient l'intérêt des utilisateurs sans laisser place au hasard, en leur proposant du contenu pertinent au moment opportun afin d'approfondir leur expérience et de réduire le taux de désabonnement.





