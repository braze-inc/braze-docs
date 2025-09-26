---
nav_title: Suivi des désinstallations
article_title: Suivi des désinstallations
page_order: 6
page_type: reference
description: "Cet article de référence couvre la mise en œuvre du suivi des désinstallations pour les statistiques au niveau de la campagne et de l’application."
tool: Reports

---

# Suivi des désinstallations

> Cet article montre comment vous pouvez visualiser l'ensemble des désinstallations d'applications au fil du temps pour repérer les tendances et les anomalies, et suivre les désinstallations au niveau des campagnes pour déterminer si une campagne spécifique favorise ou empêche les installations d'applications.

Le suivi de la désinstallation dans Braze fournit les détails suivants :

1. Statistiques quotidiennes de désinstallation d'applications dans un graphique chronologique sur la page **d'accueil**.
2. Statistiques de désinstallation au niveau de la campagne dans un graphique chronologique sur la page **Détails de la campagne** d'une campagne spécifique. Cette statistique spécifie le nombre de destinataires de campagne qui désinstallent chaque jour.

{% alert note %}
Vous devez vous abonner au suivi des désinstallations dans votre tableau de bord de Braze. Cette fonctionnalité est actuellement disponible pour les applications iOS, Android et FireOS.
{% endalert %}

## Fonctionnement

Braze collecte automatiquement des informations basiques sur la désinstallation dans le cadre de vos campagnes de notification push. Cependant, comme la fréquence à laquelle les différents utilisateurs reçoivent des campagnes push peut varier, nous proposons un suivi des désinstallations pour fournir un aperçu plus précis de l'activité de désinstallation parmi vos utilisateurs.

## Activer le suivi des désinstallations

Vous pouvez activer le suivi des désinstallations sur la page **Paramètres des applications**, sous **Paramètres**, pour chaque application que vous souhaitez suivre.

Lorsque le suivi des désinstallations est activé pour une application, des messages push en arrière-plan seront envoyés chaque nuit aux utilisateurs qui n'ont pas enregistré de session ou reçu de push depuis 24 heures.

### Configuration

Pour configurer le suivi des désinstallations pour votre application iOS, utilisez une [méthode utilitaire]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift). Pour votre application Android, utilisez [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Lorsque Braze détecte une désinstallation, qu'il s'agisse d'un suivi de désinstallation ou de la réception/distribution normale d'une campagne push, nous enregistrons la meilleure heure estimée de la désinstallation sur l'utilisateur. Cette durée est stockée dans le profil utilisateur en tant qu'attribut standard et peut être utilisée pour définir un segment d'utilisateurs pour les campagnes de reconquête.

## Filtrage des segments en fonction des désinstallations

Le filtre **Désinstallé** sélectionne les utilisateurs qui ont désinstallé votre application dans une période donnée. Comme il est difficile de déterminer l'heure exacte d'une désinstallation, nous recommandons que les filtres de désinstallation aient des plages de temps plus larges afin de s'assurer que toutes les personnes qui désinstallent tombent dans le segment à un moment ou à un autre.

Des statistiques quotidiennes sur les désinstallations sont disponibles sur la page **d'accueil**. 

![Désinstallez le segment.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

Le graphique peut être décomposé par app et par segment, à l'instar d'autres statistiques fournies par Braze. Dans la section **Aperçu des performances**, sélectionnez votre plage de dates et, si vous le souhaitez, une appli. Ensuite, faites défiler la page jusqu'au graphique des **performances dans le temps** et procédez comme suit :

1. Dans le menu déroulant **Statistiques pour**, sélectionnez **Désinstallations**.
2. Dans le menu déroulant **Répartition**, sélectionnez **Par segment**.
3. Dans le menu déroulant **Valeurs de ventilation**, sélectionnez les segments à inclure dans le graphique.

{% alert note %}
Les applications sans Suivi de Désinstallation activé montreront les désinstallations d’un sous-ensemble des utilisateurs (ceux qui ont été ciblés avec des notifications push), et le nombre total de désinstallations quotidiennes peut donc être plus élevé que celui qui est affiché.
{% endalert %}

## Suivi des désinstallations pour les campagnes

Le suivi des désinstallations de campagnes indique le nombre d'utilisateurs qui ont reçu une campagne spécifique et qui ont ensuite désinstallé votre application dans le délai sélectionné. Cet outil donne des informations sur la manière dont les campagnes peuvent encourager des comportements négatifs involontaires de la part des utilisateurs et aide à mesurer l'efficacité globale de la campagne.

Les statistiques de désinstallation des campagnes sont situées sur la page **Analyse de campagne** d'une campagne spécifique. Pour les campagnes multicanaux et multivariées, les désinstallations peuvent être ventilées par canal et variante, respectivement.

![Désinstallation au niveau de la campagne.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Fonctionnement

Braze suit les désinstallations en observant lorsque les messages de notification push envoyés aux appareils des utilisateurs renvoient un signal provenant soit de Firebase Cloud Messaging (FCM) soit d’Apple Push Notification Service (APN) indiquant que l’application n’est plus installée. Si le suivi global des désinstallations est activé pour une app particulière, nous envoyons quotidiennement un message push silencieux aux utilisateurs pour détecter s'ils ont désinstallé. Ce push "silencieux" est envoyé à tous les utilisateurs (sauf si l'utilisateur a désactivé les pushs silencieux dans les paramètres de son application) ; cependant, le push n'apparaît pas aux utilisateurs. Si nous détectons qu'un utilisateur a procédé à une désinstallation, nous :

* Augmentez d'une unité le nombre total de désinstallations de l'application.
* Augmentez d'une unité le nombre de désinstallations pour chaque campagne que l'utilisateur a reçue avec succès au cours des dernières 24 heures.
* Si un utilisateur reçoit trois campagnes au cours d'une période de 24 heures, puis procède à une désinstallation, nous incrémentons le nombre de « désinstallations » pour les trois campagnes.

Le suivi des désinstallations est soumis aux restrictions imposées par les FCM et les APN. Braze n'incrémente le nombre de désinstallations que lorsque le FCM ou l'APN nous indique qu'un utilisateur a désinstallé, mais ces systèmes tiers se réservent le droit de nous informer des désinstallations à tout moment. Par conséquent, le suivi des désinstallations devrait être utilisé pour détecter des tendances directionnelles plutôt que des statistiques précises.

Pour en savoir plus sur l'utilisation du suivi des désinstallations, consultez notre article de blog [Uninstall Tracking : Le regard du secteur sur ses forces et ses limites](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Résolution des problèmes

### Pourquoi le nombre de désinstallations augmente-t-il soudainement ?

Si vous constatez un pic de désinstallations de l’application, la raison peut être la révocation des anciens jetons à une fréquence différente par Firebase Cloud Messaging (FCM) et Apple Push Notification Service (APNS).

### Pourquoi le nombre de désinstallations d'applications diffère-t-il de ce qui figure dans les APN ?

La différence est attendue. 

Apple utilise une planification aléatoire pour retarder le signalement lorsqu'un jeton push devient invalide, ce qui signifie que même après qu'un utilisateur a désinstallé une application, les APN peuvent continuer à renvoyer des réponses réussies aux notifications push pendant un certain temps. Ce délai est intentionnel et vise à protéger la vie privée des utilisateurs. Aucun rebond ou échec ne sera signalé jusqu'à ce que l'APN renvoie un statut `410` pour un jeton non valide.

