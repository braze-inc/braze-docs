---
nav_title: Suivi des désinstallations
article_title: Désinstaller le suivi pour iOS
platform: iOS
page_order: 7
description: "Cet article montre comment désinstaller le suivi pour votre application iOS."

---

# Désinstaller le suivi pour iOS

> Cet article explique comment configurer le suivi de désinstallation pour votre application iOS et comment effectuer des tests pour vous assurer que votre application n’effectue aucune action automatique indésirable lors de la réception d’un push de suivi de désinstallation Braze.

Le suivi de désinstallation utilise des notifications push contextuelles avec un indicateur Braze dans la charge utile. Consultez [Désinstaller le suivi][6] dans notre guide de l’utilisateur pour plus d’informations.

## Étape 1 : Activer les notifications push d’arrière-plan

Assurez-vous d’avoir activé l’option **Notifications à distance** dans la section **Modes d’arrière-plan** de votre onglet **Fonctionnalités** du projet Xcode. Consultez notre documentation [notification push silencieuse][5] pour plus d’informations.

## Étape 2 : Vérifier les notifications push en arrière-plan Braze

Braze utilise des notifications push contextuelles pour collecter les analyses de suivi de désinstallation. Assurez-vous que votre application [n’effectue aucune action indésirable][4] après avoir reçu les notifications de suivi de désinstallation de Braze.

## Étape 3 : Test du tableau de bord

Ensuite, envoyez-vous une notification push test depuis le tableau de bord. Ce test de notification push ne mettra pas à jour votre profil utilisateur.

1. Sur la page **Campagnes**, créez une campagne de notification push et sélectionnez **iOS Push** comme plateforme.<br><br>
2. Sur la page **Paramètres**, ajoutez la clé `appboy_uninstall_tracking` avec la valeur correspondante `true` et cochez **Ajouter un indicateur de contenu disponible**.<br><br>
3. Utilisez la page **Aperçu** pour vous envoyer un test de suivi de désinstallation.<br><br>
4. Vérifiez que votre application n’effectue pas d’actions automatiques indésirables à la réception de la notification push.

{% alert important %}
Ces étapes de test sont un proxy pour l’envoi d’un push de suivi de désinstallation depuis Braze. Si vous avez activé le compte de badges, un numéro de badge sera envoyé avec la notification push de test, mais les notifications push de suivi de désinstallation de Braze ne définiront pas de numéro de badge sur votre application.
{% endalert %}

## Étape 4 : Activer le suivi de désinstallation

Suivez les instructions pour [l’activation du suivi de désinstallation][6].

[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/ignoring_internal_push/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking
[9]: {% image_buster /assets/img_archive/ios-uninstall-tracking-2.png %}
[10]: {% image_buster /assets/img_archive/ios-uninstall-tracking-3.png %}
