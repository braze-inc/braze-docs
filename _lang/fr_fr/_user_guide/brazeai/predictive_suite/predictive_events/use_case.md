---
nav_title: Cas d’utilisation
article_title: "Cas d'utilisation : prévoir les mises à niveau d'abonnement"
description: "Cet exemple illustre comment une marque fictive utilise Braze Predictive Events pour définir les résultats qui comptent pour son activité, comme la mise à niveau vers un abonnement pro, et créer des stratégies ciblées qui améliorent les résultats."
page_type: tutorial
---

# Cas d’utilisation : Prévoyez les mises à niveau d'abonnement grâce à un ciblage plus intelligent.

> Cet exemple illustre comment une marque fictive utilise Braze Predictive Events pour définir les résultats qui comptent pour son activité, comme la mise à niveau vers un abonnement pro, et créer des stratégies ciblées qui améliorent les résultats. 

Supposons que Jordan soit stratège en cycle de vie chez Steppington, une application de santé et de remise en forme proposant des formules gratuites et payantes. L'équipe de Jordan a pour objectif d'augmenter le nombre de mises à niveau vers le forfait Pro sans inonder l'ensemble de ses utilisateurs gratuits de messages promotionnels. Actuellement, ils envoient une promotion « Essayez la version Pro à 50 % de réduction » à tous les utilisateurs de la version gratuite après sept jours. Bien que cela génère certaines conversions (environ 5 % sur 7 jours), cela entraîne également une portée excessive, notamment en accordant des remises à des utilisateurs qui auraient probablement effectué la mise à niveau de toute façon.

Afin d'améliorer le ciblage et de réduire la lassitude liée à l'envoi de messages, Jordan utilise Predictive Events pour modéliser la probabilité qu'un utilisateur passe à la version Pro dans les 7 prochains jours. Il définit un événement personnalisé : `upgraded_to_pro`, puis l'utilise pour former un modèle de prédiction et réaliser la segmentation des utilisateurs en groupes intelligents et orientés vers l'action. 

Ce tutoriel explique comment Jordan a créé :

- Modèle prédictif pour les 7 `upgraded_to_pro`jours à venir
- Segments qui contribuent à augmenter les conversions tout en réduisant le nombre total de messages envoyés

## Étape 1 : Élaborer un modèle prédictif pour les mises à niveau

Jordan commence par définir le résultat le plus important pour sa stratégie de mise à niveau : un utilisateur passant de la version gratuite à la version Pro. Plutôt que de s'appuyer sur des déclencheurs génériques tels que « le temps écoulé depuis l'inscription », il souhaite prévoir quels utilisateurs sont réellement susceptibles de se convertir. De cette manière, son équipe peut agir sur la base de signaux réels, et non pas seulement d'hypothèses.

1. Dans le tableau de bord de Braze, Jordan accède à **Analytics** > **Événements prédictifs**.
2. Il [crée une nouvelle prédiction d'événement]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/) et la nomme « Passer à la version Pro en 7 jours ».
3. Comme événement cible, il sélectionne son événement personnalisé : `upgraded_to_pro`.
4. Jordan définit la fenêtre de prévision sur 7 jours, établit une planification de mise à jour et génère la prévision.

![Paramètres de prévision indiquant la définition, la fenêtre, l'audience et la planification de mise à jour des prédictions.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Étape 2 : Segmenter les utilisateurs en fonction de la probabilité de mise à niveau

Une fois la formation terminée, Braze attribue un [score de probabilité d'événement]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#purchase_score) (0-100) à chaque utilisateur éligible. Jordan utilise ce score pour créer des segments exploitables : l'un pour les utilisateurs ayant une forte intention de conversion qui n'ont peut-être pas besoin de remise, et l'autre pour les utilisateurs qui ne se convertiront probablement pas sans aide.

1. Jordan accède à la section Segments dans Braze.
2. Il crée deux [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) à l'aide du [filtre « Event Likelihood Score]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#event-likelihood-score) » (score de probabilité d'événement) et sélectionne la prédiction qu'il a créée. Les deux segments sont les suivants :
  - **Susceptible d'être mis à niveau :** Obtenir un score supérieur à 70
  - **Nécessite une mise à niveau :** Obtenir un score supérieur à 40 et inférieur à 70

{% alert tip %}
Les filtres prédictifs peuvent être combinés avec n'importe quel autre attribut ou comportement utilisateur. La Jordanie prévoit d'affiner davantage ces segments en fonction des intérêts des utilisateurs, par exemple en accordant la priorité aux utilisateurs qui utilisent fréquemment les fonctionnalités de suivi de la condition physique. Cela lui permet de réaliser un ciblage plus précis de quatre sous-groupes, afin d'adapter le contenu et l'envoi de messages aux besoins de chaque utilisateur.
{% endalert %}

![Générateur de segments avec deux filtres pour le score de probabilité d'événement.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Étape 3 : Personnalisez l'envoi de messages en fonction du niveau d'intention

Maintenant que Jordan a des signaux clairs indiquant une intention de mise à niveau et des sous-groupes affinés en fonction du comportement des utilisateurs, il crée une stratégie d'envoi de messages qui s'adapte aux besoins de chaque utilisateur. Fini les messages standardisés.

Il choisit l'e-mail comme principal canal pour cette campagne. Pourquoi ? En effet, Jordan souhaite expliquer la valeur ajoutée de Pro aux utilisateurs ayant une forte intention et convaincre les utilisateurs plus hésitants, ce qui nécessite de l'espace, des visuels et un appel à l'action fort. L'e-mail lui offre la flexibilité nécessaire pour y parvenir sans exercer de pression sur les utilisateurs, et lui permet de suivre les performances grâce au comportement des clics.

Jordan [crée un canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) qui divise l'expérience en fonction des segments qu'il vient de créer. Il ajoute une étape « Audience Paths » (Parcours d'audience) pour le ciblage :

- Utilisateurs ayant une grande intention et axés sur le fitness
- Intention élevée, autres utilisateurs
- Utilisateurs avec une intention faible, axés sur la forme physique
- Faible intention, autres utilisateurs

![Parcours d'audience Canvas avec quatre parcours pour chaque type d'intention.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

Il définit également l'événement de conversion Canvas comme événement personnalisé`upgraded_to_pro`, de sorte que Braze suit automatiquement les conversions de mise à niveau à mesure que les utilisateurs progressent dans le flux.

### Exemples de messages par chemin

{% tabs %}
{% tab High intent, fitness %}

Ces utilisateurs sont déjà actifs et très impliqués dans les fonctionnalités de suivi de la condition physique. Ils sont susceptibles de passer à une version supérieure sans incitations supplémentaires. Le message met donc l'accent sur la découverte d'informations plus approfondies et d'outils avancés qui s'appuient sur leurs habitudes existantes.

- **Ligne d'objet :** Atteignez vos objectifs de remise en forme
- **En-tête :** Vos progrès méritent le meilleur
- **Corps :** Vous avez déjà créé une routine solide. Avec Pro, vous pouvez aller plus loin : suivez vos progrès pour chaque groupe musculaire, fixez-vous des objectifs de performance hebdomadaires et accédez à des analyses avancées adaptées à votre façon de bouger.
- **CTA :** Commencez votre essai gratuit de la version Pro

{% endtab %}
{% tab High intent, other %}
Ces utilisateurs manifestent un engagement fort, par exemple en consultant les fonctionnalités Pro ou en utilisant fréquemment l'application, mais ne se concentrent pas spécifiquement sur le suivi de leur condition physique. Le message met en avant les avantages plus généraux de Pro, tels que le coaching et la personnalisation, afin de les inciter à franchir le pas.

- **Ligne d'objet :** Vous y êtes presque — Pro est prêt lorsque vous l'êtes.
- **En-tête :** Découvrez de nouvelles façons de vous déplacer
- **Corps :** Vous avez découvert ce que Pro a à offrir. C'est l'occasion d'accéder à des programmes personnalisés, à des contenus de coaching individuel et à des programmes guidés créés pour répondre à vos objectifs uniques, qu'il s'agisse de force, d'équilibre ou de régularité.
- **CTA :** Commencez votre essai gratuit de la version Pro

{% endtab %}
{% tab Low intent, fitness %}
Ces utilisateurs s'intéressent aux fonctionnalités de fitness, mais n'ont pas encore entrepris de mesures pour passer à un niveau supérieur. Le message met l'accent sur leurs intérêts en matière de fitness tout en réduisant les frictions grâce à une offre à durée limitée, ce qui les aide à considérer Pro comme un moyen peu risqué d'améliorer leur routine.

- **Ligne d'objet :** Êtes-vous prêt à vous entraîner de manière plus intelligente ? Essayez la version Pro avec une réduction de 50 %.
- **En-tête :** Votre mise à niveau d'entraînement est disponible.
- **Corps :** Pro vous fournit tout ce dont vous avez besoin pour démarrer efficacement : des programmes d'entraînement faciles à suivre, des conseils d'experts et un suivi réel de vos progrès. Essayez-le dès maintenant avec une réduction de 50 % et résiliez à tout moment.
- **CTA :** Bénéficiez de 50 % de réduction sur la version Pro

{% endtab %}
{% tab Low intent, other %}

Ces utilisateurs démontrent un engagement global minimal. Il est peu probable qu'ils procèdent à une mise à niveau sans incitation convaincante. Le message adopte donc une approche simple, axée sur les avantages, avec une remise et un langage modéré pour les inviter à explorer l'offre sans pression.

- **Ligne d'objet :** 50 % de réduction sur la version Pro, uniquement ce week-end.
- **En-tête :** Nous sommes prêts dès que vous l'êtes.
- **Corps :** Créez votre premier programme de remise en forme personnalisé, suivez vos progrès et accédez à des entraînements exclusifs, le tout à moitié prix. Essayez la version Pro à moindre coût et résiliez à tout moment.
- **CTA :** Bénéficiez de 50 % de réduction sur la version Pro

{% endtab %}
{% endtabs %}

## Étape 4 : Mesurez les résultats et optimisez votre stratégie

Une fois la campagne terminée, Jordan examine les performances dans [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) afin de comprendre l'efficacité des parcours personnalisés et de déterminer si la combinaison des intentions prédictives et des signaux comportementaux a amélioré les taux de mise à niveau.

Performance de l'e-mail par chemin d'accès :

- **Intention élevée, forme physique**
   - *Taux d’ouverture :* 34%
   - *Taux de clics :* 20%
   - *Taux de conversion :* 13 %
   - Aucune remise appliquée
- **Intention élevée, autre**
   - *Taux d’ouverture :* 30%
   - *Taux de clics :* 17 %
   - *Taux de conversion :* 11%
   - Aucune remise appliquée
- **Faible intention, forme physique**
   - *Taux d’ouverture :* 27%
   - *Taux de clics :* 12%
   - *Taux de conversion :* 8 %
   - Offre de réduction de 50 % incluse
- **Faible intention, autre**
   - *Taux d’ouverture :* 23%
   - *Taux de clics :* 9 %
   - *Taux de conversion :* 6 %
   - Offre de réduction de 50 % incluse

Par rapport à la campagne précédente de l'équipe, qui était uniforme (une remise générale après 7 jours n'avait généré que 5 % de conversions et un excès d'envoi de messages), l'approche ciblée montre une augmentation significative dans tous les groupes, avec une efficacité améliorée et moins de remises inutiles.

Le [rapport d'entonnoir]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) montre également une nette réduction du taux d'abandon à chaque étape clé, en particulier chez les utilisateurs ayant peu d'intention qui ont reçu des messages personnalisés. De plus en plus d'utilisateurs ouvrent, cliquent et effectuent des mises à niveau, ce qui démontre la valeur du ciblage basé sur l'intention.

Jordan utilise ces informations pour :

- Veuillez explorer les tests A/B sur les lignes d'objet et la formulation des CTA.
- Réévaluer le seuil de remise pour les utilisateurs ayant une intention modérée
- Continuer à affiner les segments en fonction de comportements supplémentaires tels que les consultations de contenu ou l'utilisation des fonctionnalités de l'application.

Grâce à Predictive Events et à la segmentation par couches, son équipe dispose désormais d'une stratégie évolutive qui adapte les messages en fonction des intentions et du comportement des utilisateurs, ce qui favorise les mises à niveau tout en préservant la confiance envers la marque.
