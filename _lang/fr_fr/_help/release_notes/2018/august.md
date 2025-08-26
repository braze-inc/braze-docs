---
nav_title: août
page_order: 6
noindex: true
page_type: update
description: "Cet article contient les notes de version d’août 2018."
---
# Août 2018

## Groupes de notification iOS 12

La version iOS 12 récente prend en charge les notifications en groupes (similaires aux canaux de notification Android) pour les applications. [Braze vous permet d'utiliser cette fonctionnalité de regroupement dans iOS ceci à l'aide de notre compositeur de messages.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## Déclenchement de push story

Vous pouvez maintenant recibler les utilisateurs en fonction de leurs clics sur une diapo spécifique d’une Push Story. Utilisez le filtre supplémentaire pour la **campagne Interacted with.**

## Événements de données S3 et Azure pour les utilisateurs anonymes

Les clients qui exportent des données vers Amazon S3 et Microsoft Azure peuvent désormais inclure des événements d’utilisateurs anonymes. Cette fonctionnalité sera activée par défaut pour toutes les intégrations nouvellement créées, mais restera désactivée sur toutes les intégrations existantes. Si vous avez des questions, adressez-vous à votre gestionnaire de compte ou ouvrez un [ticket d'assistance.]({{site.baseurl}}/braze_support/)

## Intégration des cohortes Mixpanel

Les clients de Braze et de Mixpanel peuvent désormais intégrer et [envoyer les cohortes de Mixpanel vers Braze en tant que filtres de segmentation]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import). Vous pouvez configurer une exportation manuelle unique ou une exportation dynamique toutes les deux heures. Chaque utilisateur mis à jour comptera comme un point de données, mais Mixpanel envoie uniquement les modifications depuis la dernière synchronisation.

