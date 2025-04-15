---
nav_title: "Paramètres avancés de campagne de notifications push"
article_title: Paramètres avancés de campagne de notifications push
page_order: 5
page_layout: reference
description: "Le présent article de référence couvre certains paramètres avancés de campagne de notification push comme la priorité, les URL personnalisées, les options de livraison, etc."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# Paramètres avancés de campagne de notifications push

> Il existe de nombreux paramètres avancés disponibles pour les notifications push Android et FireOS envoyées via le tableau de bord de Braze. Le présent article décrit ces fonctionnalités et la manière de les utiliser avec succès.

## ID de notification {#notification-id}

Un ID de notification est un identifiant unique pour une catégorie de message de votre choix qui informe le service de messages de ne respecter que le message le plus récent de cet ID. Définir un ID de notification vous permet d’envoyer uniquement le message le plus récent et le plus pertinent, plutôt qu’une pile de données obsolètes et non pertinentes.

Pour attribuer un ID de notification, accédez à la page de composition du push auquel vous souhaitez ajouter l'ID et sélectionnez l'onglet **Paramètres.**  Saisissez un nombre entier dans la section **ID de la notification.** Pour mettre à jour cette notification après l'avoir émise, envoyez une autre notification avec le même ID que celui utilisé précédemment.

![]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:80%;" }

## TTL (Durée de vie) {#ttl}

Le champ **Durée en vie** vous permet de définir une durée personnalisée de stockage des messages avec le service de production/instantané. Si l'appareil reste hors ligne au-delà du TTL, le message expirera et ne sera pas délivré.

Pour modifier la durée en vie de votre push Android, accédez au compositeur et sélectionnez l'onglet **Paramètres**. Recherchez le champ **Durée en vie** et saisissez une valeur en jours, heures ou secondes.

Les valeurs par défaut de la durée en vie sont définies par votre administrateur sur la page [Paramètres TTL des notifications push.]({{site.baseurl}}/user_guide/administrative/app_settings/push_ttl_settings/)  Par défaut, Braze définit le TTL des notifications push à la valeur maximale pour chaque service d'envoi de messages. Bien que les paramètres généraux TTL s'appliquent globalement, vous pouvez les modifier au niveau du message lors de la création de la campagne. Ceci est utile lorsque différentes campagnes nécessitent des urgences ou des fenêtres de réception/distribution différentes.

Par exemple, supposons que votre application organise un concours hebdomadaire de jeux-questionnaires. Vous envoyez une notification push une heure avant qu'elle ne commence. En fixant le TTL à 1 heure, vous vous assurez que les utilisateurs qui ouvrent l'application après le début du concours ne recevront pas de notification concernant un événement qui a déjà commencé.

{% details Meilleures pratiques %}

#### Quand utiliser un TTL plus court ?

Des TTL plus courts permettent de s'assurer que les utilisateurs reçoivent des notifications en temps voulu pour des événements ou des promotions qui perdent rapidement de leur pertinence. Par exemple :

- **pour la vente au détail** Envoi d'une notification push pour une vente flash qui se termine dans 2 heures (TTL : 1-2 heures)
- **Réception/distribution de nourriture :** Notifier les utilisateurs lorsque leur commande est proche (TTL : 10-15 minutes)
- **Applications de transport :** Partage de mises à jour sur l'arrivée des véhicules (TTL : quelques minutes)
- **Rappels d'événements :** Notifier les utilisateurs lorsqu'un webinaire commence bientôt (TTL : moins d'une heure)

#### Quand éviter un TTL plus court ?

- Si le message de votre campagne reste pertinent pendant plusieurs jours ou semaines, comme les rappels de renouvellement d'abonnement ou les promotions en cours.
- Lorsque maximiser la portée est plus important que l'urgence, comme pour les annonces de mises à jour d'applis ou les promotions de fonctionnalités.

{% enddetails %}

## Priorité de livraison de messagerie Firebase {#fcm-priority}

Le champ **Priorité d'envoi/distribution de la messagerie Firebase** vous permet de contrôler si un push est envoyé avec une priorité "normale" ou "élevée" à la messagerie Firebase Cloud. Pour en savoir plus, consultez la [documentation du FCM](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message).

## Texte récapitulatif

Le texte résumé vous permet de définir un texte supplémentaire dans la vue de la **notification élargie.**  Le texte récapitulatif s’affiche sous le corps du message dans la vue étendue. Il sert également de légende pour les notifications avec des images.

![][9]

Pour les notifications push qui incluent des images, le texte du message s’affiche dans la vue réduite tandis que le texte récapitulatif s’affiche comme légende d’image lorsque la notification est étendue. Consultez l’animation suivante pour voir un exemple de ce comportement.

![Comportement du texte récapitulatif][15]

## URI personnalisés

La fonctionnalité **URI personnalisé** vous permet de spécifier une URL Web ou une ressource Android vers laquelle naviguer lorsque l'on clique sur la notification. Si aucun URI personnalisé n’est spécifié, cliquer sur la notification amène les utilisateurs dans votre application. Vous pouvez utiliser l’URI personnalisé pour créer un lien profond à l’intérieur de votre application ainsi que diriger les utilisateurs vers des ressources qui existent également en dehors de votre application. Vous pouvez le spécifier via notre [API de messagerie][13] ou dans les **paramètres** du composeur de notifications push.

![URI personnalisé][12]

## Priorité d’affichage de la notification

{% alert important %}
Le paramètre de priorité d’affichage de notification n’est plus utilisé sur les appareils exécutant Android O ou plus récents. Pour les appareils plus récents, définissez la priorité par le biais de la [configuration du canal de notification.](https://developer.android.com/training/notify-user/channels#importance)
{% endalert %}

Le niveau de priorité d’une notification push affecte la manière dont votre notification est affichée dans la barre de notification par rapport à d’autres notifications. Il peut également affecter la vitesse et la manière de livrer, car les messages normaux et moins prioritaires peuvent être envoyés avec une latence légèrement plus élevée ou groupés pour préserver la durée de vie de la batterie, alors que les messages haute priorité sont toujours envoyés immédiatement.

Cette fonctionnalité est utile pour différencier vos messages en fonction de leur importance ou de leur sensibilité au temps. Par exemple, une notification sur des conditions routières dangereuses serait un bon candidat pour recevoir une priorité élevée, tandis qu’une notification sur une vente en cours devrait recevoir une priorité inférieure. Vous devez réfléchir à la nécessité de l’utilisation ou non d’une priorité perturbatrice pour la notification que vous envoyez, étant donné que se positionner constamment au sommet de la boîte de réception de votre utilisateur ou interrompre ses autres activités, peut avoir un impact négatif.

Dans Android O, la priorité de notification est devenue une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir la priorité d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos sons de notification. Pour les appareils exécutant des versions d’Android antérieures à O, il est possible de spécifier un niveau de priorité pour les notifications Android et FireOS via le tableau de bord de Braze et l’API de messagerie.

Pour envoyer un message prioritaire à l'ensemble de votre base d'utilisateurs, nous vous recommandons de spécifier indirectement la priorité via [configuration du canal de communication][17] (pour cibler les appareils O+) et d'envoyer la priorité individuelle à partir du tableau de bord (pour cibler les appareils <O).

Référez-vous au tableau suivant concernant les niveaux de priorité que vous pouvez définir sur les notifications push Android ou Fire OS :

| Priorité | Description| Valeur de `priority` (pour les messages API) |
|------|-----------|----------------------------|
| Max | Messages urgents ou à délai de réponse critique. | `2` |
| Élevée | Communication importante, telle que le nouveau message d’un ami. | `1` |
| Par défaut | La plupart des notifications. Utilisez « par défaut » si votre message ne tombe pas explicitement dans les autres types de priorité. | `0` |
| Faible | Informations que vous voulez que les utilisateurs connaissent, mais ne nécessitant pas d’action immédiate. | `-1`|
| Min | Informations contextuelles ou d’arrière-plan. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour plus d'informations, consultez la documentation de Google sur les [notifications Android][2].

## Catégorie de notification push

Les notifications push Android permettent de spécifier si votre notification tombe dans une catégorie prédéfinie. L’IU du système Android peut utiliser cette catégorie pour prendre des décisions de classement ou de filtrage concernant la localisation de la notification dans la zone de notification de l’utilisateur.

![Onglet Paramètres avec la catégorie définie sur Aucun, qui est le paramètre par défaut.][52]

| Catégorie | Description |
|---|-------|
| Aucun | Option par défaut. |
| Alarme | Alarme ou minuterie. |
| Appel | Appel entrant (voix ou vidéo) ou demande de communication synchrone similaire. |
| E-mail | Message groupé asynchrone (e-mail). |
| Erreur | Erreur dans l’opération en arrière-plan ou du statut d’authentification. |
| Événement | Événements du calendrier. |
| Message | Message direct entrant (SMS, message instantané, etc.). |
| Progression | Progression d’une opération de longue durée en arrière plan. |
| Promotion | Promotion ou publicité. |
| Recommandation | Une recommandation spécifique et opportune pour une seule chose. |
| Rappel | Rappel planifié par l’utilisateur. |
| Service | Indication de l’exécution du service en arrière plan. |
| Réseaux sociaux | Réseau social ou mise à jour de partage. |
| État | Informations continues sur l’appareil ou le statut contextuel. |
| Système | Mise à jour du statut du système ou de l’appareil. Réservé à l’utilisation par le système. |
| Transport | Contrôle du transport des médias pour la réécoute. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Visibilité de notification push

Les notifications push Android fournissent un champ facultatif pour déterminer comment une notification apparaît sur l’écran de verrouillage de l’utilisateur. Reportez-vous au tableau suivant pour des options de visibilité ainsi que des descriptions.

| Visibilité | Description |
|---|-----|
| Publique | La notification apparaît sur l’écran de verrouillage |
| Privée | La notification est affichée avec le message « Contenu masqué » |
| Secrète | La notification n’est pas affichée sur l’écran de verrouillage |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

De plus, les utilisateurs d’Android peuvent modifier la façon dont les notifications push apparaissent sur leur écran de verrouillage en changeant le paramètre de confidentialité des notifications sur leur appareil. Ce paramètre remplacera la visibilité de la notification push.

![Emplacement de la priorité de la notification push sur le tableau de bord avec l’option Définir la visibilité activée et définie sur Privé.][53]{: style="float:right;max-width:60%;margin-left:15px;"}

Quelle que soit la visibilité, toutes les notifications seront affichées sur l'écran de verrouillage de l'utilisateur si le paramètre de confidentialité des notifications sur son appareil est **Afficher tout le contenu** (paramètre par défaut). De même, les notifications ne s'afficheront pas sur l'écran de verrouillage si la confidentialité des notifications est réglée sur **Ne pas afficher les notifications.** La visibilité n'a d'effet que si la confidentialité des notifications est réglée sur **Masquer les contenus sensibles**.

La visibilité n’a aucun effet sur les appareils antérieurs à Android Lollipop 5.0.0, ce qui signifie que toutes les notifications seront affichées sur ces appareils.

Pour plus d’informations, reportez-vous à notre [documentation Android][51].

## Sons de notification

Dans Android O, les sons de notification sont devenus une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir le son d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos notifications.

Pour les appareils fonctionnant dans des versions d’Android antérieures à Android O, Braze vous permet de définir le son d’un message de notification push individuel via le composeur du tableau de bord. Vous pouvez le faire en spécifiant une ressource sonore locale sur l'appareil (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`). 

Si vous sélectionnez **Défaut** dans ce champ, le son de notification par défaut de l'appareil sera diffusé. Vous pouvez le spécifier via notre [API de messagerie][13] ou dans les **paramètres** du composeur de notifications push.

![][11]

Ensuite, saisissez l'URI complet de la ressource sonore (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`) dans l'invite du tableau de bord.

Pour envoyer un message à la totalité de votre base d’utilisateurs avec un son spécifique, nous vous recommandons de spécifier indirectement le son au moyen de la [configuration du canal de notification][16] (pour cibler les appareils O et ultérieurs) et d’envoyer le son individuel à partir du tableau de bord (pour cibler les appareils <O).

[2]: http://developer.android.com/design/patterns/notifications.html
[9]: {% image_buster /assets/img_archive/summary_text.png %}
[11]: {% image_buster /assets/img_archive/sound_android.png %}
[12]: {% image_buster /assets/img_archive/deep_link.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging/
[15]: {% image_buster /assets/img_archive/messagesummary.gif %}
Il y a [17]: https://developer.android.com/training/notify-user/channels#importance
Il y a [16]: https://developer.android.com/training/notify-user/channels
Il y a [51]: https://developer.android.com/guide/topics/ui/notifiers/notifications
[52]: {% image_buster /assets/img_archive/braze_category.png %}
[53]: {% image_buster /assets/img_archive/braze_visibility.png %}
