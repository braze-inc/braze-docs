---
nav_title: "Cas d'utilisation"
article_title: "Cas d'utilisation Réduire le désabonnement grâce à un contenu opportun"
description: "Cet exemple montre comment une marque fictive utilise la méthode Prediction du taux d'attrition pour réduire de manière proactive le nombre d'utilisateurs désabonnés."
page_type: tutorial
---

# Cas d'utilisation : Réduisez le désabonnement grâce à un réengagement opportun du contenu.

> Cet exemple montre comment une marque fictive utilise la méthode Prediction du taux d'attrition pour réduire de manière proactive le nombre d'utilisateurs désabonnés. Au lieu d'attendre que le désabonnement se produise, prédisez quels utilisateurs sont à risque et envoyez des messages sur mesure pendant qu'ils sont encore actifs.

Disons que Camila est gestionnaire CRM chez MovieCanon, une plateforme de streaming de films indépendants, de documentaires et de séries internationales.

L'équipe de Teams a repéré une tendance inquiétante : les utilisateurs s'inscrivent, diffusent un ou deux films, puis disparaissent. Historiquement, ils ont essayé d'envoyer un e-mail générique "Vous nous manquez" une semaine plus tard, mais avec un taux de conversion de seulement 3 %, c'est trop peu, trop tard. La plupart des utilisateurs désabonnés ne se réengagent pas et le désabonnement devient inévitable.

Camila veut changer cela. Au lieu de réagir au désabonnement après coup, elle utilise le taux prédiction d'attrition pour identifier les utilisateurs qui risquent de devenir inactifs dans les 14 jours à venir, ce qui donne à son équipe la possibilité de réengager les utilisateurs pendant qu'ils sont encore actifs.

Ce tutoriel explique comment Camila :

- Crée un modèle de prédiction du taux d'attrition basé sur le comportement de l'utilisateur.
- Segmentation des utilisateurs par niveau de risque
- Crée une campagne de réengagement adaptée aux personnes les plus à risque.
- Évalue l'impact à l'aide d'analyses/analytiques de la campagne.

## Étape 1 : Créer un modèle de prédiction du taux d'attrition

Camila commence par modéliser le résultat qu'elle veut éviter : les utilisateurs deviennent inactifs. Pour MovieCanon, la prédiction du taux d'attrition signifie ne pas commencer un flux dans les 14 jours - c'est donc le comportement qu'elle veut prédire.

1. Dans le tableau de bord de Braze, Camila se rend dans **Analyse/analytique** (si utilisé comme anjective désabonner).
2. Elle crée une nouvelle prédiction du taux d'attrition et la nomme "Risque d'attrition dans 2 semaines".
3. Pour définir le désabonnement, elle sélectionne `do not` et l'événement personnalisé `stream_started`, qui indique un engagement actif.
4. Elle fixe la fenêtre de prédiction à 14 jours, ce qui signifie que le modèle identifiera les utilisateurs susceptibles de passer 14 jours sans commencer un nouveau flux.

\![Définition du désabonnement montrant que le désabonnement est défini comme un utilisateur qui n'effectue pas d'événement personnalisé "stream_started" au cours des 14 derniers jours.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5\. Elle sélectionne une audience de prédictions qui comprend tous les utilisateurs ayant déclenché des événements pertinents au cours des 30 derniers jours, ce qui permet au modèle d'apprendre à partir d'un nombre suffisant de comportements récents.
6\. Elle fixe la planification de la mise à jour des prédictions à une fois par semaine afin que les scores restent à jour.
7\. Elle sélectionne **Créer des prédictions**.

Le modèle commence alors à s'entraîner, en analysant les comportements tels que les sessions récentes, la fréquence de visionnage et les interactions avec le contenu, afin de mettre en évidence des prédictions d'abandon. Une heure plus tard, Camila reçoit un e-mail l'informant que sa prédiction a fini de s'entraîner. Elle l'ouvre donc dans Braze et vérifie le score de [qualité de la prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#prediction_quality). Il est qualifié de "bon", ce qui signifie que les prédictions du modèle sont susceptibles d'être exactes et fiables. Confiante dans la performance du modèle, elle poursuit sa route.

## Étape 2 : Segmenter les utilisateurs en fonction du risque de désabonnement

Une fois l'apprentissage du modèle terminé, Braze attribue à chaque utilisateur [désabonné]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) un [score de risque de désabonnement]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) compris entre 0 et 100. 

Pour déterminer un seuil de départ pour le ciblage, Camila utilise le curseur d'audience de prédiction pour prévisualiser combien d'utilisateurs se situent dans chaque plage de score et quelle est la précision de la prédiction à ce niveau. Elle établit un équilibre entre la couverture et la précision en fonction des résultats positifs attendus. Sur cette base, elle décide de cibler les scores de risque supérieurs à 70. 

1. Camila navigue vers Segments dans Braze.
2. Elle crée un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) à l'aide du [filtre Score de risque de désabonnement]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#churn-risk-score) et sélectionne la prédiction du taux d'attrition qu'elle a créée :
   - **Susceptibles de se désabonner :** Score supérieur à 70

\![Segmentation du filtrage pour les utilisateurs dont le score de risque de désabonnement est supérieur à 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## Étape 3 : Cibler les utilisateurs à risque avec un contenu de réengagement récurrent.

Sa prédiction et son segment étant prêts, Camila met en place une campagne récurrente qui touche automatiquement les utilisateurs qui deviennent à risque chaque semaine.

1. Camila crée une campagne récurrente et active le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), de sorte que chaque message est envoyé au moment où chaque utilisateur est le plus susceptible de s'engager, plutôt que de dépendre d'un jour et d'une heure fixes.
2. Elle cible le segment "susceptible de désabonner" qu'elle vient de créer.
3. Elle attribue à l'événement de conversion de la campagne l'événement personnalisé `stream_started`, afin de déterminer le nombre d'utilisateurs qui reviennent consulter le contenu.
4. Camila choisit l'e-mail comme canal principal, car il lui donne la possibilité de mettre en avant plusieurs contenus personnalisés dans un format visuellement riche, sans trop de pression. L'e-mail comprend :
   - Une liste de surveillance personnalisée alimentée par les [recommandations d'éléments de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/), sélectionnées dynamiquement à partir du catalogue de MovieCanon.
   - Un appel à l'action qui les amène directement dans l'application.

Ainsi, chaque semaine, MovieCanon ne touche que les utilisateurs qui ont besoin d'un coup de pouce - pas d'envoi de messages excessifs, pas de devinettes.

### Exemple d'e-mail

- **Ligne d'objet :** Ne laissez pas ces titres en suspens
- **En-tête :** Votre prochaine grande montre vous attend
- **Corps :** Vous n'avez pas joué depuis longtemps ? Ne vous inquiétez pas, nous avons fait quelques choix pour vous. Des thrillers aux documentaires primés, il y a quelque chose qui porte votre nom.
- **CTA :** Voir plus de pics

## Étape 4 : Mesurer les performances

Après quelques semaines, Camila consulte les [analyses/analytiques de]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) sa [campagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) pour évaluer l'efficacité de la stratégie. 

Elle voit :

- *Taux d'ouverture :* 31%
- *Taux de clics :* 15%
- *Taux de conversion* (flux commencé dans les 48 heures) : 11%

Par rapport à l'ancienne campagne "Vous nous manquez" (où les taux de conversion oscillaient autour de 3 %), ce nouveau flux réduit de 28 % le taux de désabonnement dans le groupe cible. Elle se penche sur le [rapport d'entonnoir]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) pour repérer les points de chute des utilisateurs. Alors que les taux d'ouverture et de clics sont élevés, elle constate un léger décalage entre le clic et la conversion, ce qui l'amène à envisager de tester le texte de l'appel à manifestation d'intérêt ou de modifier la mise en page.

Pour comprendre l'impact à long terme, Camila suit également le volume d'utilisateurs entrant dans le segment "susceptibles de désabonner" d'une semaine à l'autre. Cela lui permet d'évaluer la santé globale du cycle de vie et d'informer la stratégie de rétention à un niveau plus large. Enfin, elle consulte à nouveau la page [Analyses prédictives]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) pour sa prédiction de désabonnement afin de comparer les désabonnés prédits aux désabonnés réels - une vérification utile pour s'assurer que le modèle fonctionne comme prévu.

Sur la base de ces informations, Camila prévoit d'effectuer des tests A/B sur les lignes d'objet, de tester différentes fenêtres temporelles et d'expérimenter des formats de contenu tels que des recommandations de type carrousel dans un message in-app.

Grâce à la prédiction du taux d'attrition, au timing intelligent et à la personnalisation basée sur l'intelligence artificielle, l'équipe de Camila ne se contente pas de réagir au taux d'attrition, elle le devance. Et sa campagne se déroule tranquillement en arrière-plan, atteignant les bonnes personnes, au bon moment, avec un contenu qui les intéressera vraiment.
