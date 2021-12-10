---
nav_title: Paramètres avancés
article_title: Paramètres avancés pour FireOS
platform: Pare-feu
page_order: 4
page_type: Référence
description: "Cet article couvre les paramètres avancés disponibles pour les notifications push FireOS envoyées via le tableau de bord de Braze."
channel: Pousser
---

# Paramètres avancés

Il existe de nombreux paramètres avancés disponibles pour les notifications push FireOS envoyées via le tableau de bord Braze. Cet article décrira ces fonctionnalités et comment les utiliser avec succès.

!\[Paramètres avancés\]\[1\]

## Temps de vie (TTL) {#ttl}

Le champ __"Time to Live"__ (ttl) vous permet de définir une durée personnalisée pour stocker des messages avec le service de messagerie push. Les valeurs par défaut de Braze pour le temps de vivre sont de 4 semaines pour FCM et 31 jours pour ADM. Si l'utilisateur hypothétique de l'exemple ci-dessus devait reconnecter son appareil 4 semaines après le jeu avec le temps de mise à jour par défaut, alors ces messages auraient déjà expiré dans le service de messagerie et ne seraient pas livrés.

## Texte de résumé

Le texte de résumé vous permet de définir un texte supplémentaire dans la vue "Notification élargie". Il sert également de légende pour les notifications avec des images.

!\[Exemple de Texte Résumé\]\[9\]

Le texte du résumé s'affichera sous le corps du message dans la vue étendue.

Pour les notifications push qui incluent des images, le texte du message sera affiché dans la vue réduite. alors que le texte de résumé sera affiché comme légende de l'image lorsque la notification sera étendue. Voir l'animation ci-dessous pour un exemple de ce comportement.

!\[Résumé du texte comportement\]\[15\]

## URIs personnalisés

La fonction __"URI personnalisé"__ vous permet de spécifier une URL Web ou une ressource Android vers laquelle naviguer lorsque la notification est cliquée. Si aucune URI personnalisée n'est spécifiée, cliquer sur la notification amène des utilisateurs dans votre application. Vous pouvez utiliser l'URI personnalisé pour établir un lien profond dans votre application ainsi que diriger les utilisateurs vers des ressources qui existent en dehors de votre application. Ceci peut être spécifié via notre [API de messagerie][13] ou via notre tableau de bord sous "Paramètres avancés" dans l'assistant du compositeur de push, comme illustré ci-dessous:

> Pour activer l'URI personnalisé, le `BroadcastReceiver` de votre application doit être configuré pour gérer correctement l'ouverture de l'URI.  Cela implique d'analyser le contenu des messages entrants pour l'URI personnalisé et d'y accéder.  Notre [exemple de récepteur][14] fournit un exemple d'implémentation.

!\[Custom URI\]\[12\]

## Priorité d'affichage des notifications

Le niveau de priorité d'une notification push affecte la façon dont votre notification est affichée dans la zone de notification par rapport aux autres notifications. Cela peut également affecter la vitesse et la manière de livrer, car les messages de priorité normale et inférieure peuvent être envoyés avec une latence légèrement plus élevée ou par lots pour préserver la durée de vie de la batterie, tandis que les messages de haute priorité sont toujours envoyés immédiatement.

Cette fonctionnalité est utile pour différencier vos messages en fonction de leur caractère critique ou de leur caractère temporel. Par exemple, une notification sur les conditions routières dangereuses serait un bon candidat à recevoir une grande priorité, alors qu'une notification sur une vente en cours devrait recevoir une priorité plus faible. Vous devriez vous demander si une priorité perturbatrice est réellement nécessaire ou non pour la notification que vous envoyez en tant que constamment en haut de la boîte de réception de vos utilisateurs ou l'interruption de leurs autres activités peut avoir un impact négatif.

Dans Android O, la priorité de notification est devenue une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir la priorité d'un canal pendant sa configuration, puis utilisez le tableau de bord pour sélectionner le canal approprié lors de l'envoi de vos sons de notification. Pour les appareils qui utilisent des versions d'Android avant O, spécifier un niveau de priorité pour les notifications Android et Fire OS est possible via le tableau de bord Braze et l'API Messaging.

To message your full userbase with a specific priority, we recommend that you indirectly specify the priority through [notification channel configuration][17] (to target O+ devices) _and_ send the individual priority from the dashboard (to target <O devices).

Les niveaux de priorité que vous pouvez définir sur Android ou les notifications push Fire OS sont:

| Priorité   | Description/Utilisation prévue                                                                                        | `valeur de priorité` (pour les messages API) |
| ---------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Max.       | Messages urgents ou urgents                                                                                           | `2`                                          |
| Élevé      | Communication importante, comme un nouveau message d'un ami                                                           | `1`                                          |
| Par défaut | La plupart des notifications - utilisez si votre message ne tombe pas explicitement sous aucun autre type de priorité | `0`                                          |
| Bas        | Les informations que vous voulez que les utilisateurs sachent, mais ne nécessitent aucune action immédiate            | `-1`                                         |
| Min        | Informations contextuelles ou de fond.                                                                                | `-2`                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Pour plus d'informations, veuillez consulter la documentation de [Google sur les notifications Android][2].

## Sons

Dans Android O, les sons de notification sont devenus une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir le son d'un canal pendant sa configuration, puis utilisez le tableau de bord pour sélectionner le canal approprié lors de l'envoi de vos notifications.

Pour les appareils exécutant des versions d'Android avant O, Braze vous permet de définir le son d'un message push individuel à travers le compositeur du tableau de bord. Vous pouvez le faire en spécifiant une ressource sonore locale sur l'appareil (par exemple `android.resource://com.mycompany.myapp/raw/mysound`). Spécifier "default" dans ce champ jouera le son de notification par défaut sur l'appareil. Ceci peut être spécifié via notre [API de messagerie][13] ou via notre tableau de bord sous "Paramètres avancés" dans l'assistant du compositeur de push, comme illustré ci-dessous:

!\[Sounds\]\[11\]

Entrez l'URI de la ressource son complète (par exemple `android.resource://com.mycompany.myapp/raw/mysound`) dans l'invite du tableau de bord.

To message your full userbase with a specific sound, we recommend that you indirectly specify the sound through [notification channel configuration][16] (to target O+ devices) *and* send the individual sound from the dashboard (to target <O devices).
[1]: {% image_buster /assets/img_archive/android_advanced_settings.png %} [9]: {% image_buster /assets/img_archive/summary_text.png %} [11]: {% image_buster /assets/img_archive/sound_android. ng %} [12]: {% image_buster /assets/img_archive/deep_link.png %} [15]: {% image_buster /assets/img_archive/messagesummary.gif %}

[2]: http://developer.android.com/design/patterns/notifications.html
[13]: {{site.baseurl}}/developer_guide/rest_api/messaging/
[14]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/custom-broadcast/src/main/java/com/braze/custombroadcast/CustomBroadcastReceiver.java
[17]: https://developer.android.com/training/notify-user/channels#importance
[16]: https://developer.android.com/training/notify-user/channels