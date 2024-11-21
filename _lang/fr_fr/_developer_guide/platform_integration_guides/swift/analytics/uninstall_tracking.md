---
nav_title: Suivi des désinstallations
article_title: Désinstaller le suivi pour iOS
platform: Swift
page_order: 7
description: "Cet article explique comment configurer le suivi de la désinstallation pour le SDK Swift."

---

# Suivi des désinstallations

> Découvrez comment configurer le suivi de désinstallation pour votre application iOS, afin de vous assurer que votre application n'entreprend pas d'actions automatiques indésirables à la réception d'un push de suivi de désinstallation de Braze. Le suivi de désinstallation utilise des notifications push contextuelles avec un indicateur Braze dans la charge utile. Pour des informations générales, voir [uninstall tracking][6].

{% alert important %}
Gardez à l'esprit que le suivi des désinstallations peut être imprécis. Les indicateurs que vous voyez sur Braze peuvent être retardés ou inexacts.
{% endalert %}

## Étape 1 : Activer les notifications push d’arrière-plan

Dans votre projet Xcode, allez dans **Capacités** et assurez-vous que les **Modes d'arrière-plan** sont activés. Pour plus d'informations, voir la [notification push silencieuse]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/).

## Étape 2 : Vérifier les notifications push en arrière-plan Braze

Braze utilise des notifications push contextuelles pour collecter les analyses de suivi de désinstallation. Veillez à ce que votre application [ne prenne aucune mesure indésirable]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/) à la réception de nos notifications de suivi de désinstallation.

## Étape 3 : Test à partir du tableau de bord de Braze

Ensuite, envoyez-vous un push de test depuis le tableau de bord de Braze. Gardez à l'esprit que cette poussée de test ne mettra pas à jour votre profil utilisateur.

1. Sur la page **Campagnes**, créez une campagne de notification push et sélectionnez **iOS push** comme plateforme.
2. Sur la page **Paramètres**, ajoutez la clé `appboy_uninstall_tracking` avec la valeur correspondante `true` et cochez la case **Ajouter un indicateur de contenu disponible**.
3. Utilisez la page **Aperçu** pour vous envoyer une notification push de suivi de désinstallation test.
4. Vérifiez que votre application n’effectue pas d’actions automatiques indésirables à la réception de la notification push.

{% alert important %}
Ces étapes de test sont un proxy pour l’envoi d’un push de suivi de désinstallation depuis Braze. Si vous avez activé le compte de badges, un numéro de badge sera envoyé avec la notification push de test, mais les notifications push de suivi de désinstallation de Braze ne définiront pas de numéro de badge sur votre application.
{% endalert %}

## Étape 4 : Activer le suivi de désinstallation

Suivez les instructions pour [activer le suivi de la désinstallation]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

