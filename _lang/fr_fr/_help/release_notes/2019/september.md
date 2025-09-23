---
nav_title: septembre
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2019."
---

# Septembre 2019

## Application Braze dans OneLogin

Les clients pourront simplement rechercher et sélectionner Braze dans [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/) pour l'identifiant SP ou IdP Initiated. Cela signifie que les clients n’auront pas à ajouter une application personnalisée dans OneLogin. Par conséquent, certains paramètres devraient être préremplis, notamment les attributs que nous avons vu apparaître depuis le lancement de SAML SSO.

## Partenariat Rokt Calendar

[Rokt Calendar]({{site.baseurl}}/partners/home/) offre aux clients de Braze la possibilité d'aligner leurs initiatives de marketeur personnalisé et d'étendre le contenu personnalisé au calendrier de l'utilisateur final. Ce qui rend l’expérience encore plus harmonieuse pour l’utilisateur final, et développe davantage l’Adhérence aux services de nos clients. Les clients pourront...

- Envoyer une invitation du calendrier via la plateforme Braze pour « noter cette date » et étendre notre communication
- Mettez à jour une invitation existante si le contenu de l’événement change.

## Partenariat avec Passkit

Avec [Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit/), les clients de Braze pourront étendre leur engagement client au portefeuille mobile. Ils pourront personnaliser les campagnes de leur portefeuille en utilisant la segmentation puissante  de Braze et en orchestrant les divers canaux, comme push, les messages in-app, etc.

## Retour de la valeur d’ID d’expédition via les endpoints de messagerie

Le `dispatch_id` du message sera inclus dans les réponses suivantes de l’endpoint de messagerie :
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

Ainsi, les clients qui utilisent des messages transactionnels peuvent retracer l’appel via Currents.

## Journal des modifications Canvas

Vous aimeriez en savoir plus sur les personnes qui travaillent sur un Canvas dans votre compte ? Ne vous posez plus la question ! Vous pouvez maintenant accéder au Journal des modifications de Canvas.

![Journal des modifications de Canvas]({% image_buster /assets/img/canvas-changelog1.png %})
![Journal des modifications de Canvas]({% image_buster /assets/img/canvas-changelog2.png %})
