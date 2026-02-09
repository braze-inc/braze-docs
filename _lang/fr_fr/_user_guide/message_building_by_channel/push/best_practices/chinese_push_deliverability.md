---
nav_title: Livrabilité pour les appareils Android chinois
article_title: Livrabilité des notifications push pour les appareils Android chinois
page_order: 10

page_type: reference
description: "Cet article couvre les nuances de livrabilité des notifications push que vous devez connaître lorsque vous ciblez des utilisateurs sur des appareils Android fabriqués par des OEM chinois."
channel: push

---

# Livrabilité des notifications push pour les appareils Android chinois

> Certains appareils Android fabriqués par des fabricants d'équipements d'origine chinois (OEM), tels que Xiaomi, OPPO et Vivo, optimisent la durée de vie des batteries grâce à une gestion agressive du cycle de vie des applications. Cette optimisation peut avoir pour conséquence involontaire l’arrêt du traitement d’arrière-plan des applications, ce qui peut réduire la capacité de livrabilité de vos notifications push.<br><br>Pour vous assurer que les performances de communication de votre application fonctionnent comme prévu sur ces appareils, vos équipes marketing et d’ingénierie doivent collaborer et suivre les étapes décrites dans cet article.

## Étapes pour les développeurs
Ces OEM effectuent leurs optimisations par le biais d’un arrêt agressif des applications d’arrière-plan et en les empêchant de se lancer eux-mêmes pour exécuter des tâches d’arrière-plan. En tant que développeur, vous devrez configurer votre application pour demander à l’utilisateur d’atténuer ces restrictions dans la mesure du possible.

Pour ce faire, votre application peut démarrer automatiquement sur l’appareil de votre utilisateur final, ce qui donne à votre application l’autorisation de s’exécuter en arrière-plan et d’écouter les messages de Braze. Malheureusement, étant donné qu’il s’agit d’un problème spécifique aux OEM et non d’un problème Android, il n’existe aucune API documentée pour afficher l’invite d’autorisation de démarrage automatique pour chaque OEM.

Pour résoudre ce problème, intégrez une bibliothèque comme [AutoStarter](https://github.com/judemanutd/AutoStarter) dans votre application. AutoStarter prend en charge plusieurs fabricants, ce qui vous permet d’appeler facilement le gestionnaire des autorisations de démarrage sur un large éventail d’appareils. Une fois que vous avez intégré AutoStarter, appelez `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` pour afficher le gestionnaire d’autorisations de démarrage sur l’appareil de votre utilisateur final. Associez cette action à une invite encourageant l’utilisateur final à activer le « démarrage automatique » pour votre application. Votre équipe marketing rédigera ce message, voir la section suivante  !

## Étapes pour les spécialistes du marketing
Une fois que vos utilisateurs s’abonnent pour recevoir des notifications push, il existe des étapes supplémentaires qu’ils peuvent entreprendre de leur côté pour améliorer la livraison des messages pour ces appareils. Nous vous recommandons de faire suivre votre [message d’amorce aux notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) par un message in-app destiné aux utilisateurs sur les appareils OEM chinois avec ces étapes supplémentaires :

- Activer le « démarrage automatique » pour l’application
- Désactiver l’optimisation de la batterie pour l’application

Pour amplifier davantage votre message, ajoutez d’autres canaux pour resurfacer les informations des notifications push non ouvertes via des canaux hors application tels que les SMS, WhatsApp et LINE, ainsi que des canaux intégrés à l’application tels que les messages in-app et les cartes de contenu. Vos utilisateurs pourront voir tout ce qu’ils auraient pu manquer, la prochaine fois qu’ils ouvriront l’application.