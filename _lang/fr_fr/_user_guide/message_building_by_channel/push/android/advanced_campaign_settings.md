---
nav_title: "Paramètres avancés des campagnes de push"
article_title: Paramètres avancés de la campagne de Push
page_order: 5
page_layout: reference
description: "Cet article de référence couvre certains paramètres avancés des campagnes Push, tels que la priorité, les URL personnalisées, les options de réception/distribution, etc."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# Paramètres avancés des campagnes de push

> De nombreux paramètres avancés sont disponibles pour les notifications push Android et Fire OS envoyées via le tableau de bord Braze. Cet article décrit ces fonctionnalités et explique comment les utiliser avec succès.

## ID de la notification {#notification-id}

Un ID de notification est un identifiant unique pour une catégorie de message de votre choix qui informe le service de messages de ne respecter que le message le plus récent de cet ID. La définition d'un ID de notification vous permet d'envoyer uniquement le message le plus récent et le plus pertinent, plutôt qu'une pile de messages périmés et non pertinents.

Pour attribuer un ID de notification, accédez à la page de composition du push auquel vous souhaitez ajouter l'ID et sélectionnez l'onglet **Paramètres**. Saisissez un nombre entier dans la section **ID de la notification.**  Pour mettre à jour cette notification après l'avoir émise, envoyez une autre notification avec le même ID que celui utilisé précédemment.

\![Champ ID de la notification.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## Durée en ligne/en production/instantanée (TTL) {#ttl}

Le champ **Durée en vie** vous permet de définir une durée personnalisée de stockage des messages avec le service de production/instantané. Si l'appareil reste hors ligne au-delà du TTL, le message expirera et ne sera pas délivré.

Pour modifier la durée en vie de votre push Android, accédez au compositeur et sélectionnez l'onglet **Paramètres**. Recherchez le champ **Durée en vie** et saisissez une valeur en jours, heures ou secondes.

Les valeurs par défaut de la durée en ligne/en [production/instantanée]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/) sont définies par votre administrateur sur la page [Paramètres Push.]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/)  Par défaut, Braze définit le TTL des notifications push à la valeur maximale pour chaque service d'envoi de messages. Bien que les paramètres généraux TTL s'appliquent globalement, vous pouvez les modifier au niveau du message lors de la création de la campagne. Ceci est utile lorsque différentes campagnes nécessitent des urgences ou des fenêtres de réception/distribution différentes.

Par exemple, supposons que votre application organise un concours hebdomadaire de jeux-questionnaires. Vous envoyez une notification push une heure avant qu'elle ne commence. En fixant le TTL à 1 heure, vous vous assurez que les utilisateurs qui ouvrent l'application après le début du concours ne recevront pas de notification concernant un événement qui a déjà commencé.

{% details Best practices %}

#### Quand utiliser un TTL plus court ?

Des TTL plus courts permettent de s'assurer que les utilisateurs reçoivent des notifications en temps voulu pour des événements ou des promotions qui perdent rapidement de leur pertinence. Par exemple :

- **Retail :** Envoi d'une notification push pour une vente flash qui se termine dans 2 heures (TTL : 1-2 heures)
- **Réception/distribution de nourriture :** Notifier les utilisateurs lorsque leur commande est proche (TTL : 10-15 minutes)
- **Applications de transport :** Partage de mises à jour sur l'arrivée des véhicules (TTL : quelques minutes)
- **Rappels d'événements :** Notifier les utilisateurs lorsqu'un webinaire commence bientôt (TTL : moins d'une heure)

#### Quand éviter un TTL plus court ?

- Si le message de votre campagne reste pertinent pendant plusieurs jours ou semaines, comme les rappels de renouvellement d'abonnement ou les promotions en cours.
- Lorsque maximiser la portée est plus important que l'urgence, comme pour les annonces de mises à jour d'applis ou les promotions de fonctionnalités.

{% enddetails %}

## Priorité de réception/distribution des messages Firebase {#fcm-priority}

Le champ **Priorité d'envoi/distribution de la messagerie Firebase** vous permet de contrôler si un push est envoyé avec une priorité "normale" ou "élevée" à la messagerie cloud Firebase. Ce paramètre détermine la vitesse d'envoi des messages et leur incidence sur l'autonomie de la batterie de l'appareil.

| Priorité | Description | Meilleur pour |
|---------|-------------|----------|
| Normal | Réception/distribution optimisée pour la batterie, pouvant être retardée pour économiser la batterie. | Contenu non urgent, offres promotionnelles, actualités |
| Haut | Réception/distribution immédiate avec une consommation de batterie plus élevée | Notifications sensibles au facteur temps, alertes critiques, mises à jour en ligne/en production/instantanée, alertes sur les comptes, nouvelles de dernière minute ou rappels urgents. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Considérations

- **Réglage par défaut**: Vous pouvez définir une priorité FCM par défaut pour toutes les campagnes Android dans vos [paramètres de Push.]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/) Ce paramètre au niveau de la campagne remplacera la valeur par défaut si nécessaire.
- **La dépriorisation**: Si la FCM détecte que votre application envoie fréquemment des messages à priorité élevée qui ne donnent pas lieu à des notifications visibles par l'utilisateur ou à un engagement de sa part, ces messages peuvent être automatiquement dépriorisés et revenir à une priorité normale.
- **Impact de la batterie**: Les messages à priorité élevée réveillent les appareils endormis de manière plus agressive et consomment davantage de batterie. Utilisez cette priorité de manière judicieuse.

Pour des informations plus détaillées sur la gestion des messages et la hiérarchisation des priorités, consultez la [documentation du FCM](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) et la rubrique [Gestion des messages et hiérarchisation des priorités sur Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize).

## Texte de synthèse

Le texte du résumé vous permet de définir un texte supplémentaire dans la vue élargie de la notification. Il sert également de légende pour les notifications contenant des images.

\![Un message Android avec le titre "Ceci est le titre de la notification" et le texte du résumé "Ceci est le texte du résumé de la notification".]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

Le texte du résumé s'affiche sous le corps du message dans la vue développée. 

\![Un message Android avec le titre "Ceci est le titre de la notification" et le texte du résumé "Ceci est le texte du résumé de la notification".]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Pour les notifications push qui incluent des images, le texte du message sera affiché dans la vue réduite, tandis que le texte du résumé sera affiché en tant que légende de l'image lorsque la notification sera développée. 

## URI personnalisés

La fonctionnalité **URI personnalisé** vous permet de spécifier une URL Web ou une ressource Android vers laquelle naviguer lorsque l'on clique sur la notification. Si aucune URI personnalisée n'est spécifiée, le fait de cliquer sur la notification amène les utilisateurs dans votre application. Vous pouvez utiliser l'URI personnalisé pour créer des liens profonds à l'intérieur de votre application, mais aussi pour diriger les utilisateurs vers des ressources qui existent en dehors de votre application. Vous pouvez le spécifier via notre [API Messages]({{site.baseurl}}/api/endpoints/messaging/) ou dans l'onglet **Composer** du compositeur de messages push.

\![Champ URI personnalisé.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## Priorité d'affichage des notifications

{% alert important %}
Le paramètre Priorité d'affichage des notifications n'est plus utilisé sur les appareils fonctionnant sous Android O ou une version plus récente. Pour les appareils plus récents, définissez la priorité par le biais de la [configuration du canal de notification.](https://developer.android.com/training/notify-user/channels#importance)
{% endalert %}

Le niveau de priorité d'une notification push affecte l'affichage de votre notification dans le bac de notification par rapport aux autres notifications. Elle peut également affecter la vitesse et le mode de réception/distribution, car les messages normaux et moins prioritaires peuvent être envoyés avec un temps de latence légèrement plus élevé ou mis en lots pour préserver l'autonomie de la batterie, alors que les messages hautement prioritaires sont toujours envoyés immédiatement.

Cette fonctionnalité est utile pour différencier vos messages en fonction de leur degré de criticité ou d'urgence. Par exemple, une notification concernant des conditions routières dangereuses serait un bon candidat pour recevoir une priorité élevée, alors qu'une notification concernant une vente en cours devrait recevoir une priorité plus faible. Vous devez vous demander si l'utilisation d'une priorité perturbatrice est réellement nécessaire pour la notification que vous envoyez, car le fait d'occuper constamment la première place dans la boîte de réception de vos utilisateurs ou d'interrompre leurs autres activités peut avoir un impact négatif.

Dans Android O, la priorité des notifications est devenue une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir la priorité d'un canal lors de sa configuration, puis utiliser le tableau de bord pour sélectionner le canal adéquat lors de l'envoi de vos sons de notification. Pour les appareils exécutant des versions d'Android antérieures à O, la spécification d'un niveau de priorité pour les notifications Android et Fire OS est possible via le tableau de bord de Braze et l'API d'envoi de messages.

Pour envoyer un message à l'ensemble de votre base d'utilisateurs avec une priorité spécifique, nous vous recommandons de spécifier indirectement la priorité via la [configuration du canal de communication](https://developer.android.com/training/notify-user/channels#importance) (pour cibler les appareils O+) et d'envoyer la priorité individuelle à partir du tableau de bord (pour cibler les appareils <O).

Reportez-vous au tableau suivant pour connaître les niveaux de priorité que vous pouvez définir sur les notifications push Android ou Fire OS :

| Priorité | Description| `priority` valeur (pour les messages API) |
|------|-----------|----------------------------|
| Max | Messages urgents ou à délai de transmission critique. | `2` |
| Haut | Communication importante, comme un nouveau message d'un ami. | `1` |
| Défaut | Le plus grand nombre de notifications. À utiliser si votre message ne relève pas explicitement de l'un des autres types de priorité. | `0` |
| Faible | Informations que vous souhaitez porter à la connaissance des utilisateurs, mais qui ne nécessitent pas d'action immédiate. | `-1`|
| Min | Informations contextuelles. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour plus d'informations, consultez la documentation de Google sur les [notifications Android](http://developer.android.com/design/patterns/notifications.html).

## Catégorie de poussée

Les notifications push Android offrent la possibilité de spécifier si votre notification entre dans une catégorie prédéfinie. L'interface utilisateur du système Android peut utiliser cette catégorie pour prendre des décisions de classement ou de filtrage concernant l'emplacement de la notification dans le plateau de notification de l'utilisateur.

! l'onglet Paramètres avec la catégorie définie sur Aucun, qui est le paramètre par défaut.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| Catégorie | Description |
|---|-------|
| Aucun | Option par défaut. |
| Alarme | Alarme ou minuterie. |
| Appeler | Appel entrant (vocal ou vidéo) ou demande de communication synchrone similaire. |
| e-mail | Envoi de messages en masse asynchrones (e-mail). |
| Erreur | Erreur dans l'opération d'arrière-plan ou dans l'état d'authentification. |
| Événement | Événement de calendrier. |
| Message | Message direct entrant (SMS, message instantané, etc.). |
| Progrès | Progression d'une opération d'arrière-plan de longue durée. |
| Promotion | Promotion ou publicité. |
| Recommandation | Une recommandation spécifique et opportune pour une seule chose. |
| Rappel | Rappel programmé par l'utilisateur. |
| Service | Indication de l'exécution d'un service en arrière-plan. |
| Social | Réseau social ou mise à jour de partage. |
| Statut | Informations continues sur l'état de l'appareil ou du contexte. |
| Système | Mise à jour de l'état du système ou de l'appareil. Réservé à l'usage du système. |
| Transport | Contrôle du transport des médias pour la lecture. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Visibilité de la poussée

Les notifications push Android proposent un champ facultatif permettant de déterminer comment une notification apparaît sur l'écran de verrouillage de l'utilisateur. Reportez-vous au tableau suivant pour connaître les options de visibilité et leur description.

| Visibilité | Description |
|---|-----|
| Public | La notification apparaît sur l'écran de verrouillage |
| Privé | La notification s'affiche avec le message "Contenu caché". |
| Secret | Les notifications ne s'affichent pas sur l'écran de verrouillage |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

En outre, les utilisateurs d'Android peuvent modifier la façon dont les notifications push apparaissent sur leur écran de verrouillage en changeant le paramètre de confidentialité des notifications sur leur appareil. Ce paramètre remplacera la visibilité de la notification push.

!Emplacement/localisation prioritaire du tableau de bord avec l'option Définir la visibilité activée et définie sur Privé.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Quelle que soit la visibilité, toutes les notifications seront affichées sur l'écran de verrouillage de l'utilisateur si le paramètre de confidentialité des notifications sur son appareil est **Afficher tout le contenu** (paramètre par défaut). De même, les notifications ne s'afficheront pas sur l'écran de verrouillage si la confidentialité des notifications est réglée sur **Ne pas afficher les notifications.** La visibilité n'a d'effet que si la confidentialité des notifications est réglée sur **Masquer les contenus sensibles**.

La visibilité n'a aucun effet sur les appareils antérieurs à Android Lollipop 5.0.0, ce qui signifie que toutes les notifications seront affichées sur ces appareils.

Consultez notre [documentation Android](https://developer.android.com/guide/topics/ui/notifiers/notifications) pour plus d'informations.

## Sons de notification

Dans Android O, les sons de notification sont devenus une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir le son d'un canal lors de sa configuration, puis utiliser le tableau de bord pour sélectionner le canal adéquat lors de l'envoi de vos notifications.

Pour les appareils exécutant des versions d'Android antérieures à Android O, Braze vous permet de définir le son d'un message push individuel via le compositeur du tableau de bord. Vous pouvez le faire en spécifiant une ressource sonore locale sur l'appareil (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`). 

Si vous sélectionnez **Défaut** dans ce champ, le son de notification par défaut de l'appareil sera diffusé. Cela peut être spécifié via notre [API de messages]({{site.baseurl}}/api/endpoints/messaging/) ou dans les **paramètres** du compositeur de push.

\![Le champ "Sound".]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Ensuite, saisissez l'URI complet de la ressource sonore (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`) dans l'invite du tableau de bord.

Pour envoyer un message à l'ensemble de votre base d'utilisateurs avec un son spécifique, nous vous recommandons de spécifier indirectement le son via la [configuration du canal de communication](https://developer.android.com/training/notify-user/channels) (pour cibler les appareils O+) et d'envoyer le son individuel à partir du tableau de bord (pour cibler les appareils <O).

