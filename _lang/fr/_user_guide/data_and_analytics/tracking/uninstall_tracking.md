---
nav_title: Suivi des désinstallations
article_title: Suivi des désinstallations
page_order: 6
page_type: reference
description: "Cet article de référence couvre la mise en œuvre du suivi des désinstallations pour les statistiques au niveau de la campagne et de l’application."
tool: Reports

---

# Suivi des désinstallations

Le suivi des désinstallations par Braze fournit les détails suivants :

1. Statistiques de désinstallation quotidiennes au niveau Application dans un graphique de séries temporelles sur la page **Overview**.
2. Statistiques de désinstallation quotidiennes au niveau de la Campagne dans un graphique de séries temporelles sur la page **Campaign Details (Détails de la campagne)** d’une campagne spécifique. Cette statistique spécifie le nombre de destinataires de campagne qui désinstallent chaque jour.

L’affichage des désinstallations globales au fil du temps peut vous aider à visualiser les tendances et les anomalies pour vous permettre de suivre facilement les désinstallations de votre application. De même, le suivi des désinstallations de la campagne peut révéler si une campagne spécifique encourage ou limite les désinstallations de l’application.

Braze collecte automatiquement des informations basiques sur la désinstallation dans le cadre de vos campagnes de notification push. Cependant, étant donné que la fréquence des campagnes de notifications push peut varier en fonction des utilisateurs, Braze permet le Suivi des désinstallations pour fournir un instantané plus précis des désinstallations chez vos utilisateurs.

{% alert note %} Vous devez vous abonner pour suivre les désinstallations sur le tableau de bord. Cette fonctionnalité est actuellement disponible pour les applications iOS, Android et FireOS. {% endalert %}

## Mise en œuvre

Vous pouvez activer le suivi de désinstallation dans l’onglet **Settings (Paramètres)** de la page **Manage Settings (Gérer les paramètres)** pour chaque application que vous souhaitez suivre.

Lorsque le suivi de désinstallation est activé pour une application, les messages de notification push en background (arrière-plan) seront envoyés chaque soir aux utilisateurs qui n’ont pas enregistré de session ou reçu une notification push depuis 24 heures. 

Si vous souhaitez filtrer les notifications push de Braze en arrière plan sur iOS, vous pouvez utiliser une [méthode utilitaire][iOS docs]. Sur Android, vous pouvez utiliser [`BrazeNotificationUtils.isUninstallTrackingPush()`][8] pour détecter les notifications push de désinstallation. Lorsque Braze détecte une désinstallation, que ce soit depuis le suivi des désinstallations ou lors de l’envoi de campagnes de notification push normales, nous enregistrerons la meilleure estimation de la date de désinstallation pour l’utilisateur. Cette heure est stockée dans le profil utilisateur en tant qu’attribut standard.

Cette fois-ci, vous pouvez définir un segment d’utilisateurs pour des campagnes de reconquête. En utilisant le filtre « Désinstallé » sur la page **Segments**, vous pouvez sélectionner les utilisateurs qui ont désinstallé votre application dans une période donnée. Comme la détermination de la date exacte d’une désinstallation est difficile, nous recommandons que les filtres de désinstallation aient des plages de temps plus étendues pour s’assurer que ceux qui désinstallent soient dans le segment à un moment ou à un autre.

![Désinstallation du segment][5]

## Analyse au niveau de l’application

Les statistiques quotidiennes sur les désinstallations sont sur la page **Overview (Aperçu)**. La visualisation peut être ventilée par segment, comme pour les autres statistiques fournies par Braze. Définissez **Afficher les statistiques pour** sur « Analyse de l’utilisation », puis sélectionnez « Désinstallations » » dans la liste déroulante pour afficher le graphique.

Le graphique peut ensuite être ventilé par segment et applis grâce aux menus déroulants.

{% alert note %}
Les applications sans Suivi de Désinstallation activé montreront les désinstallations d’un sous-ensemble des utilisateurs (ceux qui ont été ciblés avec des notifications push), et le nombre total de désinstallations quotidiennes peut donc être plus élevé que celui qui est affiché.
{% endalert %}

![Sélection du graphique sur la désinstallation][2]

![Graphique de désinstallation][3]

## Suivi des désinstallations pour les campagnes

Le suivi de désinstallation de campagne vous permet de voir le nombre d’utilisateurs ayant reçu une campagne spécifique et qui ont ensuite désinstallé votre application dans la plage de temps sélectionnée. Cet outil donne aux marketeurs une idée de la manière dont les campagnes peuvent encourager les comportements négatifs non souhaités des utilisateurs, et il aide à mesurer l’efficacité globale de la campagne.

Braze suit les désinstallations en observant lorsque les messages de notification push envoyés aux appareils des utilisateurs renvoient un signal provenant soit de Firebase Cloud Messaging (FCM) soit d’Apple Push Notification Service (APN) indiquant que l’application n’est plus installée. Si le suivi global des désinstallations est activé pour une application particulière, Braze envoie un message de notification push silencieux quotidien aux utilisateurs pour détecter si ils l’ont désinstallé. Cette notification push « silencieuse » est envoyée à tous les utilisateurs (sauf si l’utilisateur a désactivé les notifications push silencieuses dans les paramètres de son application), mais elle n’est pas visible pour les utilisateurs. Si Braze détecte qu’un utilisateur a désinstallé, la plate-forme :

* Incrémente de 1 le nombre total de désinstallations de l’application.
* Incrémente de 1 le nombre de désinstallations pour chaque campagne que l’utilisateur a reçue avec succès au cours des dernières 24 heures.
* Si un utilisateur reçoit 3 campagnes sur une période de 24 heures, puis désinstalle, nous incrémenterons le nombre de « désinstallations » pour les 3 campagnes.

Le suivi des désinstallations est soumis aux restrictions imposées par les FCM et les APN. Braze comptabilise la désinstallation lorsque FCM ou APN nous indique qu’un utilisateur a désinstallé, mais ces systèmes tiers se réservent le droit de nous notifier des désinstallations quand bon leur semble. Par conséquent, le suivi des désinstallations doit être utilisé pour détecter les tendances plutôt que pour obtenir des statistiques précises.

Pour plus d’informations sur le suivi des désinstallations, allez sur [ce blog][7].

Les statistiques de désinstallation des campagnes sont sur la page Détails de la campagne. Pour les campagnes multicanaux et multivariées, les désinstallations peuvent être ventilées par canal et variante, respectivement.

![Niveau de Désinstallation de la Campagne][6]

## Résolution des problèmes

### Pourquoi est-ce que je constate un pic soudain de désinstallations ?

Si vous constatez un pic de désinstallations de l’application, la raison peut être la révocation des anciens jetons à une fréquence différente par Firebase Cloud Messaging (FCM) et Apple Push Notification Service (APNS). 

[1]: {% image_buster /assets/img_archive/Uninstall_Tracking2.png %} "Uninstall Tracking Checkbox"
[2]: {% image_buster /assets/img_archive/Uninstall_Tracking_App2.png %} "Uninstall Graph Selection"
[3]: {% image_buster /assets/img_archive/Uninstall_232.png %} "Uninstall Graph"
[4]: {% image_buster /assets/img_archive/User_Profile.png %} "Uninstall Attribute"
[5]: {% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment"
[6]: {% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %}
[7]: https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/
[iOS docs]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/uninstall_tracking/
[8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/is-uninstall-tracking-push.html
