---
nav_title: Avril
page_order: 9
noindex: true
page_type: update
description: "Cet article contient les notes de version d’avril 2018."
---
# Avril 2018

## Une mise à jour des webhooks arrive

En mai, Braze mettra en œuvre une initiative de sécurité pour les redirections de webhooks. À l’avenir, l’expéditeur du webhook ne pourra pas suivre ces redirections. Au lieu de cela, les redirections seront traitées comme des erreurs pour éviter des boucles de redirection infinies. Braze ne s’attend pas à ce que quelqu’un soit impacté, mais si vous avez des webhooks avec redirection, nous vous conseillons de réviser et de modifier cette campagne.

## Augmentation du stockage CSV

Braze a mis à jour le filtre CSV X pour inclure les 100 CSV les plus récents, dans lesquels un utilisateur a été mis à jour, au lieu de 10 CSV auparavant.

## Suivi des désinstallations activé par défaut pour les applications Android

La fonction [Suivi des désinstallations][94] sera activée par défaut pour toutes les nouvelles applications Android. Toutes les applications Android existantes avec suivi des désinstallations désactivé auront désormais ce paramètre sur « Activé ». Le suivi des désinstallations sur Android n’envoie plus de push vers l’appareil, et aucune autre mise à jour ou action n’est requise de votre part.

## Fonctions de recherche modifiées et améliorées

Nous avons amélioré les tags et la fonctionnalité de recherche dans la plateforme Braze pour améliorer votre expérience lors des déploiements à grande échelle, quand vous recherchez des [attributs ou événements personnalisés][92], des modèles etc.

## Push Stories

[Créez des notifications][95] avec plusieurs pages, une image, un comportement en cas de clic, un titre et un sous-titre facultatifs. Créez simplement un message push et sélectionnez **Push Story** dans la liste déroulante.

Notez que vous devez avoir la dernière version d’Android (version 2.2.0+) ou iOS (version 3.2.0+) pour utiliser cette fonctionnalité.


## Inbox vision

Vous pouvez maintenant [prévisualiser vos e-mails][96] en fonction de la plateforme de votre client, soit via une page de miniatures, soit par une vue en liste qui inclut une grande capture d’écran et une analyse spécifique de tout problème pouvant exister avec le rendu HTML pour chaque client. Contactez votre gestionnaire du succès des clients  ou votre gestionnaire de compte pour plus d’informations.


[92]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management
[94]: {{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking-for-campaigns
[95]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/#push-stories
[96]: {{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision
