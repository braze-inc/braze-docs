---
nav_title: Suivi des désinstallations
article_title: Désinstaller le suivi pour iOS
platform: iOS
page_order: 7
description: "Cet article montre comment désinstaller le suivi pour votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Désinstaller le suivi pour iOS

> Cet article explique comment configurer le suivi de désinstallation pour votre application iOS, et comment effectuer des tests pour que votre application ne prenne pas d'actions automatiques indésirables à la réception d'un push de suivi de désinstallation de Braze.

Le suivi de désinstallation utilise des notifications push contextuelles avec un indicateur Braze dans la charge utile. Pour plus d'informations, consultez le [suivi de la désinstallation]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) dans notre guide de l'utilisateur.

## Étape 1 : Activer les notifications push d’arrière-plan

Assurez-vous d'avoir activé l'option **Notifications à distance** dans la section **Modes d'arrière-plan** de l'onglet **Capacités** de votre projet Xcode. Reportez-vous à notre documentation sur les [notifications push silencieuses]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications/) pour plus de détails.

## Étape 2 : Vérifier les notifications push en arrière-plan Braze

Braze utilise des notifications push contextuelles pour collecter les analyses de suivi de désinstallation. Veillez à ce que votre application [ne prenne aucune mesure indésirable]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push/) à la réception de nos notifications de suivi de désinstallation.

## Étape 3 : Test du tableau de bord

Ensuite, envoyez-vous une notification push test depuis le tableau de bord. Ce test de notification push ne mettra pas à jour votre profil utilisateur.

1. Sur la page **Campagnes**, créez une campagne de notification push et sélectionnez **iOS push** comme plateforme.<br><br>
2. Sur la page **Paramètres**, ajoutez la clé `appboy_uninstall_tracking` avec la valeur correspondante `true` et cochez la case **Ajouter un indicateur de contenu disponible**.<br><br>
3. Utilisez la page **Aperçu** pour vous envoyer une notification push de suivi de désinstallation test.<br><br>
4. Vérifiez que votre application n’effectue pas d’actions automatiques indésirables à la réception de la notification push.

{% alert important %}
Ces étapes de test sont un proxy pour l’envoi d’un push de suivi de désinstallation depuis Braze. Si vous avez activé le comptage des badges, un numéro de badge sera envoyé avec la poussée de test, mais les poussées de suivi de désinstallation de Braze ne définiront pas de numéro de badge sur votre application.
{% endalert %}

## Étape 4 : Activer le suivi de désinstallation

Suivez les instructions pour [activer le suivi de la désinstallation]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

