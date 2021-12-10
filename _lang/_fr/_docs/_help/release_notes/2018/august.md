---
nav_title: Août
page_order: 6
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour août 2018."
---

# Août 2018

## Groupes de notifications iOS 12

La version récente d'iOS 12 prend en charge le regroupement des notifications (similaire aux canaux de notification Android) pour les applications. [Braze vous permet d'utiliser cette fonctionnalité de regroupement dans iOS en utilisant notre compositeur de messages.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## Déclenchement de l'histoire

Vous pouvez maintenant rediriger les utilisateurs en fonction des clics de page spécifiques sur les diapositives push. Utilisez le filtre supplémentaire pour __Interagi avec la Campagne__.

## Événements de données S3 et Azure provenant d'utilisateurs anonymes

Les clients qui exportent des données vers Amazon S3 et Microsoft Azure peuvent maintenant inclure des événements provenant d'utilisateurs anonymes. Cette fonctionnalité sera activée par défaut pour toutes les intégrations nouvellement créées, mais restera désactivée pour toutes les intégrations existantes. Si vous avez des questions, contactez votre responsable de compte ou ouvrez un [ticket d'assistance][support].

## Intégration de Mixpanel Cohorts

Les clients de Braze et de Mixpanel peuvent maintenant intégrer et [envoyer des Mixpanel Cohorts à Braze en tant que filtres de segment]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import). Vous pouvez soit configurer une exportation manuelle à usage unique soit une exportation dynamique toutes les deux heures. Chaque utilisateur mis à jour comptera comme un point de données, mais Mixpanel n'envoie que des changements depuis la dernière synchronisation.

[support]: {{site.baseurl}}/braze_support/