---
nav_title: Désinstaller le suivi
article_title: Désinstaller le suivi
page_order: 6
page_type: Référence
description: "Cet article de référence traite de la manière d'implémenter le suivi de désinstallation."
tool: Rapports
---

# Désinstaller le suivi

Le suivi de la désinstallation de Braze fournit les détails suivants :

1. Désinstallation quotidienne des statistiques au niveau de l'application dans un graphique de séries temporelles sur la page **Aperçu**.
2. Le niveau de la campagne désinstalle les statistiques dans un graphique de séries temporelles sur la page **Détails de la campagne** d'une campagne spécifique. Cette statistique spécifie le nombre de destinataires de la campagne qui se désinstallent chaque jour.

Afficher les désinstallations agrégées au fil du temps peut vous aider à visualiser les tendances et les anomalies afin que vous puissiez surveiller les désinstallations de l'application en toute simplicité. De même, les désinstallations au niveau de la campagne de suivi peuvent révéler si une campagne spécifique conduit ou empêche la désinstallation d'applications.

Braze __collecte automatiquement un niveau de base d'informations de désinstallation__ de vos campagnes de push régulières. Cependant, parce que la fréquence à laquelle différents utilisateurs reçoivent des campagnes de push peut varier, Braze offre le suivi de désinstallation pour fournir un instantané plus précis des activités de désinstallation parmi vos utilisateurs.

{% alert note %} Vous devez opter pour désinstaller le suivi sur le tableau de bord. Cette fonctionnalité est actuellement disponible pour les applications sur iOS, Android et Fire OS. {% endalert %}

## Implémentation

Vous pouvez activer le suivi de la désinstallation dans l'onglet **Paramètres** de la page **Gérer les paramètres**. pour chaque application que vous souhaitez suivre, cochez la case dans la section de suivi de désinstallation.

!\[Désinstaller Checkbox de suivi\]\[1\]

Lorsque le suivi de la désinstallation est activé pour une application, les messages push en arrière-plan seront envoyés par nuit aux utilisateurs qui n'ont pas enregistré de session ou qui n'ont pas reçu de push en 24 heures.

Si vous êtes intéressé à filtrer Braze background push sur iOS, vous pouvez utiliser une [méthode utilitaire][iOS docs]. Sur Android, vous pouvez utiliser [`AppboyNotificationUtils.isUninstallTrackingPush()`][8] pour détecter la poussée de désinstallation. Lorsque Braze détecte une désinstallation, que ce soit à partir du suivi de désinstallation ou de l'envoi normal de campagnes push, nous enregistrerons le meilleur temps estimé de la désinstallation sur l'utilisateur. Cette heure est stockée dans le profil de l'utilisateur comme attribut par défaut.

!\[Désinstaller l'attribut\]\[4\]

Ce temps peut être utilisé pour définir un segment des utilisateurs pour les campagnes de retour en arrière. En utilisant le filtre "Désinstallé" sur la page **Segments** , vous pouvez sélectionner les utilisateurs qui ont désinstallé votre application dans un laps de temps. La détermination de l'heure exacte de la désinstallation est difficile, nous recommandons que les filtres de désinstallation aient des intervalles de temps plus larges pour s'assurer que tous ceux qui désinstallent entrent dans le segment à un moment donné.

!\[Désinstaller Segment\]\[5\]

## Analyse au niveau de l'application

Des statistiques quotidiennes sur les désinstallations sont trouvées sur la page **Aperçu**. La visualisation peut être divisée par segment, similaire à d'autres statistiques fournies par Braze. Définissez **Voir les statistiques pour** à "Analyses d'utilisation", puis sélectionnez "Désinstaller" dans la liste déroulante pour afficher le graphique.

Le graphique peut ensuite être réparti par segment et par application en utilisant les listes déroulantes.

{% alert note %}
Les applications sans suivi de désinstallation activées rapporteront les désinstallations d'un seul sous-ensemble de leurs utilisateurs (ceux qui ont été ciblés avec des notifications push), donc les totaux de désinstallation quotidienne peuvent être plus élevés que ce qui est affiché.
{% endalert %}

!\[Désinstaller Graph Selection\]\[2\]

!\[Désinstaller Graph\]\[3\]

## Désinstaller le suivi des campagnes

Campagnes de suivi de désinstallation vous permet de voir le nombre d'utilisateurs qui ont reçu une campagne spécifique et ont ensuite désinstallé votre application dans la période sélectionnée. Cet outil donne aux marketeurs un aperçu de la façon dont les campagnes peuvent encourager les comportements négatifs non voulus des utilisateurs et aider à mesurer l'efficacité globale de la campagne.

Braze suit les désinstallations en observant lorsque les messages push envoyés aux appareils des utilisateurs retournent un signal de Firebase Cloud Messaging (FCM) ou Apple Push Notification Service (APN) que l'application n'est plus installée. Si le suivi global de désinstallation est activé pour une application particulière, Braze envoie un message push quotidien silencieux aux utilisateurs pour détecter s'ils ont désinstallé. Ce push « silencieux » est envoyé à tous les utilisateurs (sauf si l'utilisateur a désactivé les poussées silencieuses dans ses paramètres), Cependant, il ne semble pas pour les utilisateurs. Si Braze détecte qu'un utilisateur a été désinstallé, cette plateforme:

* Incrémente le nombre total de désinstallation de l'application de 1.
* Incrémente le nombre de désinstallation pour chaque campagne que l'utilisateur a reçue avec succès dans les dernières 24 heures par 1.
* Si un utilisateur reçoit 3 campagnes sur une période de 24 heures puis se désinstalle, nous incrémenterons le nombre de « désinstallations » pour les 3 campagnes.

Le suivi de la désinstallation est soumis aux restrictions imposées à cette information par FCM et APN. Braze n'incrémente le nombre de désinstallation que lorsque FCM ou APN nous dit qu'un utilisateur a désinstallé, mais ces systèmes tiers se réservent le droit de nous avertir des désinstallations à tout moment. Par conséquent, le suivi de désinstallation devrait être utilisé pour détecter les tendances directionnelles par opposition à des statistiques précises.

Pour plus d'informations sur l'utilisation du suivi de désinstallation, voir [ce billet de blog][7].

Les statistiques de désinstallation des campagnes se trouvent sur la page Détails de la campagne. Pour les campagnes multi-canaux et multivariées, les désinstallations peuvent être réparties par canal et variante, respectivement.

!\[Désinstaller le niveau de la campagne\]\[6\]
[1]: {% image_buster /assets/img_archive/Uninstall_Tracking2.png %} "Désinstaller Tracking Checkbox" [2]: {% image_buster /assets/img_archive/Uninstall_Tracking_App2. ng %} "Désinstaller la sélection graphique" [3]: {% image_buster /assets/img_archive/Uninstall_232. ng %} "Désinstaller Graph" [4]: {% image_buster /assets/img_archive/User_Profile.png %} "Désinstaller Attribut" [5]: {% image_buster /assets/img_archive/Uninstall_Segment. ng %} "Désinstaller Segment" [6]: {% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %}

[7]: https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/
[iOS docs]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/uninstall_tracking/
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/push/AppboyNotificationUtils.html#isUninstallTrackingPush-android.os.Bundle-
