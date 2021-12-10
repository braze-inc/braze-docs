---
nav_title: Avril
page_order: 9
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour avril 2018."
---

# Avril 2018

## Mise à jour des Webhooks sur le chemin

En mai, Braze mettra en place une initiative de sécurité pour les redirections de webhook. En allant de l'avant, l'expéditeur du webhook ne pourra pas suivre ces redirections. À la place, les redirections seront traitées comme des erreurs pour éviter les boucles de redirection infinie. Braze ne s'attend pas à ce que cela affecte quiconque, mais si vous avez des webhooks qui redirigent, nous vous recommandons de revisiter et de modifier cette campagne.

## Stockage CSV augmenté

Braze a mis à jour le filtre CSV X pour inclure les 100 CSV les plus récents un utilisateur a été mis à jour, par opposition aux 10 précédents.

## Désinstaller le suivi par défaut pour les applications Android

La fonction [Désinstaller Tracking][94] pour toutes les nouvelles applications Android va par défaut "on". Toutes les applications Android existantes qui ont désactivé le suivi de désinstallation seront maintenant mises en mode "activé". Le suivi de la désinstallation d'Android n'envoie plus de push sur l'appareil, et aucune autre mise à jour ou action n'est requise de votre part.

## Mise à jour et amélioration des fonctions de recherche

Braze a ajouté des balises et une meilleure fonctionnalité de recherche à Braze pour améliorer votre expérience de gestion des déploiements à grande échelle de Braze pendant que vous recherchez des [événements et attributs personnalisés][92], , et plus encore.

## Envoyer des histoires

[Créer des notifications][95] avec plusieurs pages, une image, un comportement de clic et un titre facultatif & sous-titre. Il suffit de créer un message push et de sélectionner "Push Story" dans la liste déroulante.

_Veuillez noter que vous devez mettre à jour vers la dernière version d'Android (version 2.2.0+) et d'iOS (version 3.2.0+) pour utiliser cette fonctionnalité._


## Vision de la boîte de réception

Vous pouvez maintenant [prévisualiser vos e-mails][96] en fonction de la plate-forme de votre client, soit via une page de vue d'ensemble des vignettes ou une vue liste qui comprend une grande capture d'écran et une analyse plus spécifique de tous les problèmes qui peuvent exister avec le rendu HTML pour chaque client. Parlez à votre gestionnaire de service clientèle ou à votre gestionnaire de comptes pour connaître les prix et les options.


[92]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management
[94]: {{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking-for-campaigns
[95]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/#push-stories
[96]: {{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision
