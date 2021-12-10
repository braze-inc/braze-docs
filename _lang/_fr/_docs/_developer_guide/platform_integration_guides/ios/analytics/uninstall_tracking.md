---
nav_title: Désinstaller le suivi
article_title: Désinstaller le suivi pour iOS
platform: iOS
page_order: 7
description: "Cet article explique comment configurer le suivi de désinstallation pour votre application iOS."
---

# Désinstaller le suivi pour iOS

> Cet article explique comment configurer le suivi de désinstallation pour votre application iOS, et comment tester pour s'assurer que votre application ne prend aucune action automatique indésirable lors de la réception d'une Push de suivi de la désinstallation de Braze.

Désinstaller le suivi utilise les notifications push en arrière-plan avec un drapeau Braze dans le bloc de charge. Pour plus d'informations, consultez notre page [Désinstaller Tracking][6] dans notre Guide d'utilisation.

## Étape 1 : Activation du push en arrière-plan

Assurez-vous d'avoir activé l'option "Notifications à distance" dans la section "Modes d'arrière-plan" de l'onglet Capacités de votre projet Xcode. Pour plus de détails, reportez-vous à notre documentation sur [Notifications push silencieuses][5].

## Étape 2 : Vérification de la poussée d'arrière-plan Braze

Braze utilise les notifications push en arrière-plan pour collecter des analyses de suivi de désinstallation. Suivez les instructions [ici][4] pour vous assurer que votre application ne prend aucune action indésirable après avoir reçu les notifications de suivi de la désinstallation de Brase.

## Étape 3 : Tester depuis le tableau de bord

Pour s'assurer que votre application ne prend aucune action automatique indésirable lors de la réception d'une Push de suivi de la désinstallation de Braze, vous envoyer une poussée de test depuis le tableau de bord [][7]. Ce test push ne mettra pas à jour votre profil d'utilisateur.

1. Sur la page **Campagnes** , créez une campagne de notification Push et sélectionnez iOS Push comme plate-forme.<br><br>
2. Sur la page des paramètres de messages additionnels,
- Ajoute la clé `appboy_uninstall_tracking` avec la valeur correspondante `true`
- Vérifier **Ajouter le drapeau disponible sur le contenu** <br><br>!\[Paires Key-Value\]\[9\]{:style="max-width:60%;"}<br><br>
3. Use the Preview Message page to send yourself a test uninstall tracking push.<br><br>!\[Test User\]\[10\]{:style="max-width:60%;"}<br><br>
4. Vérifiez que votre application ne prend aucune action automatique indésirable lors de la réception de la push.

{% alert important %}
Les étapes ci-dessus sont un proxy pour envoyer un push de suivi de désinstallation de Braze. Si le nombre de badges est activé, un numéro de badge sera envoyé avec la poussée de test, mais Braze désinstallera les pushes de suivi de désinstallation ne définira pas de numéro de badge sur votre application.
{% endalert %}

## Étape 4 : Activer le suivi de désinstallation

Suivez les instructions pour activer le suivi de la désinstallation en utilisant notre [article sur le suivi de désinstallation][6].
[9]: {% image_buster /assets/img_archive/ios-uninstall-tracking-2.png %} [10]: {% image_buster /assets/img_archive/ios-uninstall-tracking-3.png %}

[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/ignoring_internal_push/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking
[6]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking
[7]: https://dashboard-01.braze.com/
[7]: https://dashboard-01.braze.com/
