---
nav_title: "Cas d'utilisation"
article_title: "Cas d'utilisation Prédire les mises à niveau de l'abonnement"
description: "Cet exemple montre comment une marque fictive utilise les événements prédictifs de Braze pour définir les résultats qui comptent pour son entreprise - comme la mise à niveau vers un abonnement pro - et créer des stratégies ciblées qui améliorent les résultats."
page_type: tutorial
---

# Cas d'utilisation : Prédire les mises à niveau d'abonnement grâce à un ciblage plus intelligent.

> Cet exemple montre comment une marque fictive utilise les événements prédictifs de Braze pour définir les résultats qui comptent pour son entreprise - comme la mise à niveau vers un abonnement pro - et créer des stratégies ciblées qui améliorent les résultats. 

Supposons que Jordan soit un stratège du cycle de vie chez Steppington, une application de santé et de fitness avec des niveaux gratuits et payants. L'équipe de Teams a pour objectif d'augmenter le nombre de mises à niveau du plan Pro sans bombarder l'ensemble de sa base d'utilisateurs gratuits de messages de réduction. Actuellement, ils envoient une promotion "Essayez Pro avec 50% de réduction" à tous les utilisateurs de niveau gratuit après sept jours. Bien qu'elle permette d'obtenir quelques conversions (environ 5 % sur 7 jours), elle se traduit également par une portée excessive, notamment par des remises accordées à des utilisateurs qui, de toute façon, étaient susceptibles de passer à un niveau supérieur.

Pour améliorer le ciblage et réduire la fatigue des messages, Jordan utilise des événements prédictifs pour modéliser la probabilité qu'un utilisateur passe à la version Pro dans les 7 prochains jours. Il définit un événement personnalisé : `upgraded_to_pro` Il l'utilise ensuite pour former un modèle de prédictions et segmenter les utilisateurs en groupes intelligents et orientés vers l'action. 

Ce tutoriel explique comment Jordan a créé :

- Un modèle prédictif pour `upgraded_to_pro` dans les 7 jours
- Des segmentations qui permettent d'augmenter les conversions tout en envoyant moins de messages au total.

## Étape 1 : Créer un modèle prédictif pour les mises à niveau

Jordan commence par définir le résultat le plus important pour sa stratégie de mise à niveau : un utilisateur passant de la version gratuite à la version Pro. Plutôt que de s'appuyer sur des déclencheurs génériques tels que le "temps écoulé depuis l'inscription", il souhaite prévoir quels utilisateurs sont réellement susceptibles de se convertir. De cette façon, son équipe peut agir sur la base de signaux réels, et pas seulement d'hypothèses.

1. Dans le tableau de bord de Braze, Jordan va dans **Analyses/analytiques (si utilisé comme analyse** adjective) > Événements prédictifs.
2. Il [crée une nouvelle prédiction d'événement]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/) et la nomme "Passage à la version Pro dans 7 jours"
3. Il sélectionne son événement personnalisé comme événement cible : `upgraded_to_pro`.
4. Jordan fixe la fenêtre de prédiction à 7 jours, définit une planification de mise à jour et crée la prédiction.

\![Paramètres de la prédiction indiquant la définition, la fenêtre, l'audience et la planification de la mise à jour de la prédiction.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Étape 2 : Segmenter les utilisateurs en fonction de la probabilité de mise à niveau

Une fois la formation terminée, Braze attribue un [score de probabilité d'événement]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#purchase_score) (0-100) à chaque utilisateur éligible. Jordan utilise ce score pour créer des segmentations exploitables, l'une pour les utilisateurs à fort potentiel qui n'ont peut-être pas besoin d'une remise, l'autre pour les utilisateurs qui ne se convertiront probablement pas sans assistance.

1. Jordan navigue vers Segments dans Braze.
2. Il crée deux [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) à l'aide du [filtre Score de vraisemblance de l'événement]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#event-likelihood-score) et sélectionne la prédiction qu'il a créée. Les deux segments sont :
  - **Susceptibles d'être améliorés :** Score supérieur à 70
  - **Besoin d'un coup de pouce pour se mettre à niveau :** Score supérieur à 40 et inférieur à 70

{% alert tip %}
Les filtres prédictifs peuvent être combinés avec d'autres attributs ou comportements de l'utilisateur. Jordan prévoit d'affiner ces segments en fonction des intérêts des utilisateurs, par exemple en donnant la priorité à ceux qui utilisent fréquemment les fonctionnalités de suivi de la condition physique. Il dispose ainsi de quatre sous-groupes à cibler plus précisément, ce qui permet d'adapter le contenu et l'envoi des messages aux besoins de chaque utilisateur.
{% endalert %}

Générateur de segments avec deux filtres pour le score de vraisemblance des événements.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Étape 3 : Personnaliser les messages en fonction du niveau d'intention

Maintenant que Jordan dispose de signaux clairs d'intention de mise à niveau et de sous-groupes affinés en fonction du comportement des utilisateurs, il crée une stratégie d'envoi de messages qui s'adapte aux besoins de chaque utilisateur. Fini les messages publicitaires à taille unique.

Il choisit l'e-mail comme principal canal pour cette campagne. Pourquoi ? Parce que Jordan veut expliquer la valeur de Pro pour les utilisateurs à forte intention et présenter un argumentaire convaincant aux utilisateurs plus hésitants - deux choses qui nécessitent de l'espace, des visuels et un CTA fort. L'e-mail lui donne la souplesse nécessaire pour le faire sans mettre les utilisateurs sous pression, et lui permet de suivre les performances par le biais du comportement des clics.

Jordan [crée un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) qui divise l'expérience en fonction des segments qu'il vient de créer. Il ajoute une étape de parcours d'audience à la cible :

- Utilisateurs à forte intention, axés sur la forme physique
- Intention élevée, autres utilisateurs
- Utilisateurs peu intentionnés, axés sur la forme physique
- Faible intention, autres utilisateurs

!parcours d'audience Canvas avec quatre parcours pour chaque type d'intention.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

Il associe également l'événement de conversion Canvas à l'événement personnalisé `upgraded_to_pro`, afin que Braze suive automatiquement les conversions de mise à niveau au fur et à mesure que les utilisateurs progressent dans le flux.

### Exemples d'envois de messages par chemin d'accès

{% tabs %}
{% tab High intent, fitness %}

Ces utilisateurs sont déjà actifs et très attachés aux fonctionnalités de suivi de la condition physique. Il est probable qu'ils passeront à l'étape supérieure sans incitations supplémentaires, c'est pourquoi le message se concentre sur le déblocage d'informations plus approfondies et d'outils avancés qui créent des liens avec leurs habitudes existantes.

- **Ligne d'objet :** Allez plus loin dans vos objectifs de remise en forme
- **En-tête :** Vos progrès méritent Pro
- **Corps :** Vous avez déjà créé une routine solide. Avec la version Pro, vous pouvez aller plus loin : suivez vos progrès sur l'ensemble des groupes musculaires, définissez des objectifs de performance hebdomadaires et débloquez des analyses/analytiques avancées adaptées à votre façon de bouger.
- **CTA :** Commencez votre essai Pro gratuit

{% endtab %}
{% tab High intent, other %}
Ces utilisateurs montrent des signes forts d'engagement, comme la consultation des fonctionnalités Pro ou l'utilisation fréquente de l'application, mais ne sont pas spécifiquement intéressés par le suivi de la condition physique. Le message met en avant des avantages Pro plus larges tels que le coaching et la personnalisation pour les inciter à franchir le pas.

- **Ligne d'objet :** Vous y êtes presque-Pro est prêt quand vous l'êtes
- **En-tête :** Découvrez d'autres façons de bouger
- **Corps :** Vous avez exploré les possibilités offertes par Pro. C'est maintenant votre chance d'accéder à des plans personnalisés, à des contenus de coaching 1:1 et à des programmes guidés créés pour répondre à vos objectifs uniques, qu'il s'agisse de force, d'équilibre ou de constance.
- **CTA :** Commencez votre essai Pro gratuit

{% endtab %}
{% tab Low intent, fitness %}
Ces utilisateurs s'intéressent aux fonctionnalités de remise en forme, mais n'ont pas encore pris de mesures pour passer à la vitesse supérieure. Le message s'appuie sur leurs intérêts en matière de fitness tout en réduisant les frictions grâce à une offre limitée dans le temps, ce qui les aide à considérer Pro comme un moyen peu risqué d'améliorer leur routine.

- **Ligne d'objet :** Prêt à vous entraîner plus intelligemment ? Essayez Pro à 50% de réduction
- **En-tête :** Votre mise à jour d'entraînement vous attend
- **Corps :** Pro vous offre tout ce dont vous avez besoin pour commencer en force : des programmes d'entraînement faciles à suivre, des conseils d'experts et un véritable suivi des progrès. Essayez-le maintenant pour 50 % de réduction, et annulez à tout moment.
- **CTA :** Obtenez 50% de réduction sur Pro

{% endtab %}
{% tab Low intent, other %}

Ces utilisateurs font preuve d'un engagement minimal dans l'ensemble. Il est peu probable qu'ils passent à la vitesse supérieure sans une incitation convaincante. Le message adopte donc une approche simple, axée sur les avantages, avec une remise et un langage doux pour inviter à l'exploration sans pression.

- **Ligne d'objet :** 50% de réduction sur Pro-just pour ce week-end
- **En-tête :** Prêt quand vous l'êtes
- **Corps :** Créez votre premier programme de personnalisation, suivez vos progrès et accédez à des séances d'entraînement exclusives, le tout pour la moitié du prix. Essayez Pro pour moins cher et résiliez à tout moment.
- **CTA :** Obtenez 50% de réduction sur Pro

{% endtab %}
{% endtabs %}

## Étape 4 : Mesurez les résultats et optimisez votre stratégie

Après l'exécution de la campagne, Jordan examine les performances dans [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pour comprendre comment les chemins personnalisés ont fonctionné - et si la combinaison de l'intention prédictive avec les signaux comportementaux a permis d'améliorer les taux de mise à niveau.

Performance des e-mails par chemin d'accès :

- **Haute intention, forme physique**
   - *Taux d'ouverture :* 34%
   - *Taux de clics :* 20%
   - *Taux de conversion :* 13%
   - Aucune réduction n'a été utilisée
- **Haute intention, autre**
   - *Taux d'ouverture :* 30%
   - *Taux de clics :* 17%
   - *Taux de conversion :* 11%
   - Aucune réduction n'a été utilisée
- **Faible intention, remise en forme**
   - *Taux d'ouverture :* 27%
   - *Taux de clics :* 12%
   - *Taux de conversion :* 8%
   - Offre de réduction de 50 % incluse
- **Faible intention, autre**
   - *Taux d'ouverture :* 23%
   - *Taux de clics :* 9%
   - *Taux de conversion :* 6%
   - Offre de réduction de 50 % incluse

Par rapport à la campagne précédente de l'équipe (où une remise générale après 7 jours n'avait entraîné que 5 % de conversions et un envoi excessif de messages), l'approche ciblée a permis d'obtenir des résultats significatifs dans tous les groupes, tout en améliorant l'efficacité et en réduisant les remises inutiles.

Le [rapport d'entonnoir]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) montre également une nette réduction de l'abandon à travers les étapes clés, en particulier pour les utilisateurs à faible intention qui ont reçu des messages personnalisés. Davantage d'utilisateurs ouvrent, cliquent et mettent à niveau, ce qui prouve la valeur du ciblage basé sur l'intention.

Jordan utilise ces informations pour :

- Explorez les tests A/B sur les lignes d'objet et la formulation des CTA.
- Réévaluer le seuil de remise pour les utilisateurs en milieu d'intention
- Continuez à affiner les segments en fonction de comportements supplémentaires comme les consultations de contenu ou l'utilisation des fonctionnalités de l'app.

Grâce aux événements prédictifs et à la segmentation en couches, son équipe dispose désormais d'une stratégie évolutive qui adapte les messages en fonction de l'intention et du comportement des utilisateurs, ce qui permet d'augmenter le nombre de mises à niveau tout en préservant la confiance dans la marque.
