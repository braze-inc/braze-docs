---
nav_title: Livrabilité pour les appareils Android chinois
article_title: Livrabilité des messages push pour les appareils Android chinois
page_order: 10

page_type: reference
description: "Cet article traite des nuances de livrabilité en push que vous devez connaître lorsque vous ciblez des utilisateurs d'appareils Android fabriqués par des équipementiers chinois."
channel: push

---

# Livrabilité des messages push pour les appareils Android chinois

> Certains appareils Android fabriqués par des équipementiers chinois, tels que Xiaomi, OPPO et Vivo, optimisent l'autonomie de la batterie par une gestion agressive du cycle de vie des applications. Cette optimisation peut avoir pour conséquence involontaire d'arrêter le traitement des apps en arrière-plan, ce qui peut réduire la livrabilité de vos notifications push.<br><br>Pour vous assurer que les performances d'envoi de messages de votre appli fonctionnent comme prévu sur ces appareils, vos équipes de marketing et d'ingénierie doivent collaborer et suivre les étapes décrites dans cet article.

## Étapes pour les développeurs
Ces équipementiers procèdent à des optimisations en tuant de manière agressive les applications en arrière-plan et en les empêchant d'exécuter elles-mêmes des tâches en arrière-plan. En tant que développeur, vous devrez configurer votre application pour demander à l'utilisateur d'assouplir ces restrictions dans la mesure du possible.

Pour ce faire, votre application doit démarrer automatiquement sur l'appareil de votre utilisateur final, ce qui lui donne la permission de s'exécuter en arrière-plan et d'écouter les messages de Braze. Malheureusement, comme il s'agit d'un problème spécifique aux OEM et non d'un problème Android, il n'existe pas d'API documentée pour faire apparaître l'invite d'autorisation de démarrage automatique pour chaque OEM.

Pour résoudre ce problème, intégrez une bibliothèque comme [AutoStarter](https://github.com/judemanutd/AutoStarter) dans votre application. AutoStarter prend en charge plusieurs fabricants, ce qui vous permet d'appeler facilement le gestionnaire des autorisations de démarrage sur un large éventail d'appareils. Après avoir intégré AutoStarter, appelez `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` pour faire apparaître le gestionnaire des autorisations de démarrage sur l'appareil de votre utilisateur final. Associez cette action à une invite encourageant l'utilisateur final à activer le "démarrage automatique" de votre application. Votre équipe de marketing élaborera ce message - voir la section suivante !

## Marche à suivre pour les marketeurs
Une fois que vos utilisateurs ont choisi de recevoir des notifications push, ils peuvent prendre des mesures supplémentaires de leur côté pour améliorer la réception/distribution des messages pour ces appareils. Nous vous recommandons de faire suivre votre [message d'amorce push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) d'un message in-app ciblant les utilisateurs d'appareils OEM chinois avec ces étapes supplémentaires :

- Activer le démarrage automatique de l'application
- Désactiver l'optimisation de la batterie pour l'application

Pour amplifier encore votre message, ajoutez d'autres canaux pour faire resurgir l'information des notifications push non ouvertes via des canaux out-of-app tels que SMS, WhatsApp et LINE et des canaux in-app tels que les messages in-app et les cartes de contenu. Vos utilisateurs pourront voir tout ce qu'ils ont pu manquer la prochaine fois qu'ils ouvriront l'application.