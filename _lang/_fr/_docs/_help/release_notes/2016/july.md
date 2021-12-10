---
nav_title: Juillet
page_order: 6
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour juillet 2016."
---

# Juillet 2016

## Filtrer le journal des erreurs de la console du développeur par type d'erreur

Cette mise à jour vous permet d'utiliser plus facilement le message d'erreur de la console développeur pour résoudre les problèmes liés à leur intégration à Braze. Il s'agit d'une mise à jour conviviale qui vous permet de filtrer le journal d'erreur de message par type et il est beaucoup plus facile de trouver et d'identifier des problèmes d'intégration spécifiques.

## Horodatage ajouté pour le dernier push de suivi de désinstallation envoyé

Braze détecte les désinstallations en envoyant un push silencieux aux applications du client pour voir quels appareils répondent. Cette fonctionnalité ajoute un horodatage discret indiquant la dernière fois que le suivi de la désinstallation a été effectué. Cet horodatage peut être trouvé sur votre page de paramètres où le suivi de la désinstallation est configuré. En savoir plus sur le suivi de désinstallation [ici]({{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking).

!\[désinstaller la case à cocher de suivi\]\[6\]

## Améliorations de test du webhook ajoutées

Vous pouvez maintenant test-envoyer un message de webhook en direct de Braze avant de définir une campagne pour aller en direct. Envoyer un message de test vous permettra de vérifier que vos messages et que les terminaux du serveur ont été correctement configurés dans un environnement sable. En savoir plus sur les webhooks [ici]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook).

## Ajout d'une variation de message reçue à l'exportation CSV des destinataires de la campagne

Nous avons ajouté une colonne indiquant la variation de message reçue pour l'exportation CSV des destinataires de la campagne. En savoir plus sur l'exportation de données depuis Braze [ici]({{site.baseurl}}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-dashboard-data).

## Limite approximative du nombre d'impressions

Une fois qu'un message In-App a reçu un certain nombre d'impressions, Braze cessera de permettre aux utilisateurs de recevoir le message. En savoir plus sur la définition de limites approximatives pour les impressions [ici]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap).

!\[Capsule IAM impression cap\]\[11\]
[6]: {% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %} [11]: {% image_buster /assets/img_archive/approx_limit_for_IAM.png %}
