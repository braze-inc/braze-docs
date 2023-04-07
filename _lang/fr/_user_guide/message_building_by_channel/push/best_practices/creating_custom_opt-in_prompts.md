---
nav_title: Création de demandes d'inscription personnalisées
article_title: Création de demandes d'inscription personnalisées
page_order: 2
page_type: reference
description: "Le présent article couvre les bonnes pratiques pour créer des demandes d'inscription personnalisées qui listent clairement et démontrent les avantages de la messagerie par notification push."
channel: push

---

# Création de demandes d'inscription personnalisées

Même si vous gardez ces bonnes pratiques à l’esprit lors de la conception et de l’envoi de messages de notification push, certains utilisateurs peuvent les désactiver avant de réaliser les avantages qu’elles fournissent. Les utilisateurs ont peut-être déjà eu des expériences négatives antérieures avec des messages de notification push indésirables et non pertinents provenant d’autres applications et refuseront désormais toute demande d’en recevoir depuis n’importe quelle application.

De plus, l’environnement juridique entourant les messages électroniques dans certaines régions devient de plus en plus strict. Par exemple, la [législation anti-spam canadienne][13] exige un consentement explicite des utilisateurs pour pouvoir leur envoyer des messages marketing. D’autres pays peuvent entreprendre des actions législatives similaires ce qui fait que l’obtention du consentement explicite de vos utilisateurs doit être une priorité. Le fait de ne pas disposer d’un double système d’abonnement en place peut donc vous laisser devant la nécessité de réaliser dans l’avenir une migration chronophage vers un système conforme.

Créer une demande d'inscription qui énumère clairement et démontre les avantages de la notification push ne peut que vous aider, compte tenu des attitudes en évolution des consommateurs et des gouvernements concernant la messagerie par notification push. Au lieu de piéger vos utilisateurs avec une demande d’autorisation lorsqu’ils ouvrent l’application pour la première fois, expliquez les avantages de vos messages par notification push puis demandez l’autorisation.

L’ajout d’un message simple pour inviter une action de l’utilisateur peut vous permettre de demander plusieurs fois et efficacement son autorisation, si nécessaire. S’appuyer seulement sur la demande d’autorisation d’iOS signifie que la plupart des utilisateurs ne réfléchiront jamais à deux fois à l’activation de vos messages de notification push.

## Cas d’utilisation

Par exemple, l’application Fandango a une invite qui indique les avantages de l’activation des notifications push de manière claire et concise. Après avoir reçu cette notification, les utilisateurs disposent d’assez d’informations pour décider s’ils considèrent que les notifications push de Fandango s’avèrent utiles et peuvent agir en conséquence.

![][37]

Un autre exemple d’une application qui a fait un excellent travail avec ses demandes d’inscription personnalisées est textPlus. Lors du téléchargement de textPlus, l’utilisateur reçoit une demande contextuelle qui explique les avantages des notifications push et le processus pour les activer.

![][24]

Après que l’utilisateur sélectionne **Suivant**, il reçoit la vraie demande de notification push d’iOS. Si l’utilisateur n’autorise pas les notifications push à ce stade, il devra les activer dans les paramètres. textPlus simplifie ce processus en affichant un rappel sur sa page de réception.

![][25]

Si un utilisateur sélectionne **Activer**, il reçoit des étapes détaillées sur la manière d’activer les notifications push. Cela supprime certains des efforts impliqués par l’activation des notifications push

![][26]

Une autre application qui fait un merveilleux travail de préparation des utilisateurs à l’acceptation des notifications push est Hopper. Découvrez leur [article concernant les moyens][49] sur la manière de réaliser le meilleur onboarding en termes de notifications push.

> Si vous avez implémenté une demande de notifications push personnalisée dans une application iOS, assurez-vous que vous vous [enregistrez à nouveau avec APN][44] chaque fois que l’application s’exécute après qu’elle ait attribué les autorisations de notification push à votre application. Apple le recommande car les [jetons d’appareil][45] peuvent changer arbitrairement.

Pour plus d’informations, consultez notre article sur [Gérer les abonnements utilisateur][36].

[13]: {{site.baseurl}}/help/best_practices/spam_regulations/#can-spam
[16]: {% image_buster /assets/img_archive/bn_push1.png %}
[17]: {% image_buster /assets/img_archive/bn_push2.png %}
[24]: {% image_buster /assets/img_archive/textplus_prompt.png %}
[25]: {% image_buster /assets/img_archive/textplus_reminder.png %}
[26]: {% image_buster /assets/img_archive/textplus_directions.png %}
[36]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[37]: {% image_buster /assets/img_archive/PushPrimeFandango.png %}
[44]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/
[45]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
[49]: https://medium.com/@hopper_travel/the-notification-problem-50267cbabad2#.auax13q52
