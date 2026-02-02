---
nav_title: avril
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

La fonction de [désinstallation du suivi pour]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/) toutes les nouvelles applications Android sera activée par défaut. Toutes les applications Android existantes avec suivi des désinstallations désactivé auront désormais ce paramètre sur « Activé ». Le suivi des désinstallations sur Android n’envoie plus de push vers l’appareil, et aucune autre mise à jour ou action n’est requise de votre part.

## Fonctions de recherche modifiées et améliorées

Braze a ajouté l'étiquetage et une meilleure fonctionnalité de recherche à Braze afin d'améliorer votre expérience de gestion des déploiements à grande échelle de Braze pendant que vous recherchez des [événements et attributs personnalisés]({{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management), des tags, etc.

## Contenu push

[Créez des notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/#push-stories) avec plusieurs pages, une image, un comportement de clic, un titre et un sous-titre facultatifs. Il suffit de créer un message push et de sélectionner **Push Story** dans le menu déroulant.

Notez que vous devez avoir la dernière version d’Android (version 2.2.0+) ou iOS (version 3.2.0+) pour utiliser cette fonctionnalité.


## Inbox vision

Vous pouvez désormais [prévisualiser vos e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision) en fonction de la plateforme de votre client, soit via une page d'aperçu de vignettes, soit via une vue de liste comprenant une grande capture d'écran et une analyse plus spécifique des éventuels problèmes de rendu HTML pour chaque client. Contactez votre gestionnaire du succès des clients  ou votre gestionnaire de compte pour plus d’informations.


