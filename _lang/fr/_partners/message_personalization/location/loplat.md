---
nav_title: loplat
article_title: loplat
description: "Cet article de référence décrit le partenariat entre Braze et loplat, une plateforme marketing hors ligne basée sur la localisation, pour vous permettre d’exécuter des campagnes marketing de proximité en ajoutant un contexte de localisation."
alias: /partners/loplat/
page_type: partner
search_tag: Partenaire

---

# loplat

> [Loplat][1] est la principale plateforme hors ligne basée sur la localisation. Utilisez le SDK loplat pour augmenter intelligemment la fréquentation de votre magasin et exécutez des campagnes marketing qui encouragent les achats en magasin. Vous pouvez mesurer les performances du magasin grâce à l’analyse de la fréquentation une fois la campagne terminée.

L’intégration de Braze et de loplat vous permet d’utiliser les services de localisation de loplat (stockage de POI et geofence personnalisé) pour déclencher des campagnes de marketing géocontextuel et créer des événements personnalisés à l’aide de la segmentation hors ligne. Lorsque les utilisateurs visitent l’emplacement ciblé que vous avez défini dans loplat X, les informations de campagne et de localisation sont envoyées immédiatement à Braze.

## Conditions préalables

| Condition | Description |
| --- | --- |
| compte loplat X | Un compte loplat X est requis pour profiter de cette intégration.<br><br>Envoyez un e-mail à [support@loplat.com][3] pour demander un compte loplat X. |
| SDK loplat | loplat Le SDK reconnaît les visites en magasin des utilisateurs, traite les événements de localisation et distingue si les utilisateurs restent en place ou sont en mouvement. Vous pouvez utiliser le SDK loplat pour analyser la fréquentation de votre magasin, envoyer des messages de notification push lorsque les utilisateurs entrent dans votre magasin, etc.<br><br>Notez que le SDK est uniquement disponible pour Android et iOS. |
| Clé d’API REST Braze | Une clé API REST Braze avec les autorisations suivantes :<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

Les informations sur les lieux d’événements personnalisés fournis par loplat peuvent être utilisées dans vos campagnes pour obtenir des exemples d’utilisation comme :

- [Alerte de promotion Duty-free][2]
    - Envoyez des bons de réduction duty-free aux utilisateurs situés près des portes d’embarquement à l’aéroport.
- Notification push de l’emplacement de la station de recharge du véhicule électrique (VE)
    - Définissez des geofences autour des stations de recharge des véhicules électriques, informez les utilisateurs lorsqu’ils sont à proximité de la station et encouragez-les à charger.

## Intégration

### Étape 1 : Intégrer les SDK

Intégrez le SDK loplat et le SDK Braze dans votre application en suivant les étapes indiquées dans la documentation [Intégration loplat-Braze][4].

### Étape 2 : Synchronisez les tableaux de bord Braze et loplat X et créez une campagne

Créer une nouvelle clé API dans le tableau de bord de Braze. Copiez la clé API et collez-la dans **Settings (Paramètres) > API Settings (Paramètres API)** dans le tableau de bord loplat X. Voir le [guide de l’utilisateur du loplat X](https://loplat-loplat.gitbook.io/loplat-x-user-guide-en/integration/braze) pour plus de détails.

#### Livraison déclenchée par API

1. Créez une campagne ou Canvas Braze qui envoie avec une **livraison déclenchée par API** et copiez l’ID de campagne.
2. Lancez la campagne dans Braze après avoir terminé toutes les étapes.
3. Allez sur loplat X et créez une campagne en suivant les instructions du [guide de l’utilisateur de loplat X][5].
4. Collez l’ID de campagne Braze dans les **paramètres de message de campagne** et lancez la campagne.

![][7]

#### Livraison par événement

Avec l’intégration, vous pouvez appliquer des conditions d’emplacement en envoyant des informations de geofence, de région, de nom de marque ou de nom de magasin. En outre, vous pouvez ajouter des segments ou affecter une conversion à l’aide de l’événement personnalisé que vous avez créé.
1. Créez une campagne loplat X en suivant les instructions du [guide de l’utilisateur de loplat X][6].
2. Ajoutez un événement personnalisé dans les **paramètres de message de campagne** et lancez la campagne.
3. Naviguez vers le tableau de bord de Braze et créez une campagne ou un Canvas qui envoie via une **Livraison par événement**.
4. Sélectionnez l’événement personnalisé que vous avez créé dans loplat X pour définir une action de déclenchement d’emplacement.

![][8]

[1]: https://www.loplat.com/
[2]: https://www.loplat.com/loplat-x#usecase
[3]: mailto:support@loplat.com
[4]: https://developers.loplat.com/braze/
[5]: https://loplat-loplat.gitbook.io/loplat-x-user-guide-en/campaigns/create/campaign-integration#1.-braze-greater-than-loplat-x-api-triggered-delivery
[6]: https://loplat-loplat.gitbook.io/loplat-x-user-guide-en/campaigns/create/campaign-integration
[7]: {% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %}
[8]: {% image_buster /assets/img/loplat/loplat_action_based_delivery.png %}