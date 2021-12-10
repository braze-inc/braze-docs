---
nav_title: Création de messages personnalisés d'opt-in
article_title: Création de messages personnalisés d'opt-in
page_order: 2
page_type: Référence
description: "Cet article couvre les meilleures pratiques pour la création de messages opt-in personnalisés qui listent et démontrent clairement les avantages de la messagerie push."
channel: Pousser
---

# Création d'invitations opt-in personnalisées

Même si vous gardez à l'esprit les meilleures pratiques lors de la conception et de l'envoi de messages push. Certains utilisateurs peuvent les désactiver avant de réaliser les avantages qu'ils pourraient leur offrir. Il se peut que les utilisateurs aient déjà eu des expériences négatives avec le spammy, messages push non pertinents provenant d'autres applications et va maintenant refuser toute demande de recevoir des messages push depuis n'importe quelle application.

En outre, l'environnement juridique entourant la messagerie électronique dans certaines régions devient de plus en plus strict. Par exemple, [la législation antispam du Canada][13] exige le consentement explicite des utilisateurs pour leur envoyer des messages liés au marketing. D'autres pays peuvent prendre des mesures législatives similaires, donc obtenir le consentement explicite de vos utilisateurs devrait être une priorité. Le fait de ne pas disposer d'un système double opt-in en place peut vous faire passer du temps à un système conforme dans le futur.

Créer une invite de participation qui répertorie clairement et démontre les avantages de la poussée ne peut que vous aider étant donné les attitudes évolutives des consommateurs et des gouvernements à l’égard du message incitatif. Au lieu d'embusquer vos utilisateurs avec une demande d'autorisation lorsqu'ils ouvrent l'application pour la première fois expliquez les avantages de vos messages push, puis demandez la permission.

!\[Breaking News 1\]\[16\]

!\[Breaking News 2\]\[17\]

Ajouter une fenêtre pop-up simple pour une action utilisateur rapide peut vous permettre de demander l'autorisation à vos utilisateurs plus d'une fois, si nécessaire. En se basant sur la seule demande de permission d'iOS, la plupart des utilisateurs ne réfléchiront jamais à l'activation de vos messages push.

Par exemple, l'application Fandango a une fenêtre pop-up qui indique les avantages de l'activation des notifications push de manière claire et concise. Après avoir reçu cette notification, les utilisateurs ont suffisamment d'informations pour décider s'ils trouveront que Fandango a de la valeur et peuvent agir en conséquence.

!\[fandango_prompt\]\[37\]

Un autre exemple d'application qui fait un excellent travail avec des instructions opt-in personnalisées est textPlus. Lors du téléchargement de textPlus, un utilisateur reçoit une invite pop-up qui explique les avantages des notifications push et guide l'utilisateur à travers le processus de leur activation.

!\[textplus_prompt\]\[24\]

Après que l'utilisateur ait tapé **Next**, l'utilisateur reçoit la véritable invite push iOS. Si l'utilisateur n'active pas les notifications push à ce stade, il devra les activer dans les paramètres. textPlus permet aux utilisateurs de le faire plus facilement en mettant en place un rappel sur leur page Boîte de réception.

!\[textplus_reminder\]\[25\]

Si les utilisateurs tapent sur **Activer**, ils se voient proposer des étapes détaillées pour activer les notifications push. Cela supprime une partie des efforts impliqués dans l'activation des notifications push

!\[textplus_directions\]\[26\]

Une autre application qui fait un travail merveilleux en démarrant ses utilisateurs pour accepter les notifications push est Hopper. Voir leur [article moyen][49] sur la meilleure façon de monter à bord quand il s'agit de pousser.

> Si vous avez implémenté une invite push personnalisée comme décrit ci-dessus dans une application iOS, assurez-vous que vous [vous réinscrivez avec les APN][44] à chaque fois que l'application s'exécute après qu'ils accordent des autorisations push à votre application. Apple conseille cela car les [jetons de l'appareil peuvent changer arbitrairement][45].

Pour plus d'informations, reportez-vous à notre article sur [Gestion des abonnements d'utilisateurs][36].
[16]: {% image_buster /assets/img_archive/bn_push1.png %} [17]: {% image_buster /assets/img_archive/bn_push2. ng %} [24]: {% image_buster /assets/img_archive/textplus_prompt.png %} [25]: {% image_buster /assets/img_archive/textplus_reminder. ng %} [26]: {% image_buster /assets/img_archive/textplus_directions.png %} [37]: {% image_buster /assets/img_archive/PushPrimeFandango. ng %} [46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %} [47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}

[13]: {{site.baseurl}}/help/best_practices/spam_regulations/#can-spam
[36]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[44]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/
[45]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html
[49]: https://medium.com/@hopper_travel/the-notification-problem-50267cbabad2#.auax13q52
