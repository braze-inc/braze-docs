---
nav_title: loplat
article_title: loplat
description: "Cet article de référence décrit le partenariat entre Braze et loplat, une plateforme de marketing basée sur la localisation hors ligne, pour vous permettre d'exécuter des campagnes de marketing de proximité en ajoutant un contexte de localisation."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [Loplat](https://www.loplat.com/) est la principale plateforme hors ligne basée sur l'emplacement. Utilisez le SDK loplat pour augmenter intelligemment la fréquentation de votre magasin et exécuter des campagnes marketing qui encouragent les achats en magasin. Vous pouvez mesurer la performance du magasin grâce à l'analyse de la fréquentation après la fin de la campagne.

_Cette intégration est maintenue par Loplat._

## À propos de l'intégration

L'intégration de Braze et loplat vous permet d'utiliser les services de localisation de loplat (POI de magasin et géorepérage personnalisé) pour déclencher des campagnes marketing géo-contextuelles et créer des custom events en utilisant la segmentation hors ligne. Lorsque les utilisateurs visitent l'emplacement ciblé que vous avez défini dans loplat X, les informations de la campagne et de l'emplacement sont envoyées immédiatement à Braze.

## Conditions préalables

| Condition | Description |
| --- | --- |
| compte loplat X | Un compte loplat X est requis pour profiter de cette intégration.<br><br>Envoyez un e-mail à [support@loplat.com](mailto:support@loplat.com) pour demander un compte loplat X. |
| loplat SDK | Le SDK loplat reconnaît les visites des utilisateurs en magasin, traite les événements de localisation et distingue si les utilisateurs restent à un endroit ou se déplacent. Vous pouvez utiliser le SDK loplat pour analyser la fréquentation de votre magasin, envoyer des messages push lorsque les utilisateurs entrent dans votre magasin, etc.<br><br>Notez que le SDK n'est disponible que pour Android et iOS. |
| Clé d'API REST Braze | Une clé API REST de Braze avec les autorisations suivantes :<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Les informations sur l'emplacement de l'événement personnalisé fournies par loplat peuvent être utilisées dans vos campagnes pour atteindre des cas d'utilisation tels que :

- [Alerte promotion hors taxes](https://www.loplat.com/loplat-x#usecase)
    - Envoyez des coupons de réduction hors taxes aux utilisateurs qui se trouvent près des portes d'embarquement à l'aéroport.
- Notifications push de localisation de station de recharge de véhicule électrique (VE)
    - Définissez des points de géorepérage autour des stations de recharge pour véhicules électriques et informez les utilisateurs lorsqu'ils sont à proximité de la station et encouragez-les à recharger leur véhicule.

## Intégration

### Étape 1 : Intégrer les SDKs

Intégrez le SDK loplat et le SDK Braze dans votre application en utilisant les étapes fournies dans la documentation de l'[intégration loplat-Braze](https://developers.loplat.com/braze/).

### Étape 2 : Synchronisez les tableaux de bord Braze et loplat X et créez une campagne

Créez une nouvelle clé API dans le tableau de bord de Braze. Copiez la clé API et collez-la dans **Paramètres > Paramètres de l'API** dans le tableau de bord loplat X. Consultez le [guide de l'utilisateur loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25) pour plus de détails.

#### Distribution déclenchée par l'API

1. Créez une campagne Braze ou un canvas qui envoie avec **distribution déclenchée par l'API**, et copiez l'ID de la campagne.
2. Lancez la campagne dans Braze après avoir terminé toutes les étapes.
3. Allez sur loplat X et créez une campagne en suivant les instructions dans le [guide de l'utilisateur de loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb).
4. Collez l'ID de campagne Braze sous les **Paramètres de message de campagne**, et lancez la campagne.

![]({% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %})

#### livraison par événement

Avec l'intégration, vous pouvez appliquer des conditions d'emplacement en envoyant des données de géorepérage, de région, de nom de marque ou de nom de magasin. De plus, vous pouvez ajouter des segments ou attribuer une conversion avec l'événement personnalisé que vous avez créé.
1. Créez une campagne loplat X en suivant les instructions dans le [guide de l'utilisateur loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598).
2. Ajoutez un événement personnalisé dans les **Paramètres de message de campagne** et lancez la campagne.
3. Allez au tableau de bord de Braze et créez une campagne ou un canvas qui envoie avec **livraison par événement**.
4. Sélectionnez l'événement personnalisé que vous avez créé dans loplat X pour définir une action de déclenchement de localisation.

![]({% image_buster /assets/img/loplat/loplat_action_based_delivery.png %})


