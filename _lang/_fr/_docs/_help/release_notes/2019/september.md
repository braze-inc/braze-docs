---
nav_title: Septembre
page_order: 4
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour septembre 2019."
---

# Septembre 2019

## Braze application dans OneLogin

Les clients pourront simplement rechercher et sélectionner Braze dans [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/) pour une connexion SP ou IdP initiée. Cela signifie que les clients n'auront pas à ajouter une application personnalisée dans OneLogin. En conséquence, cela devrait pré-remplir certains paramètres comme les attributs que nous avons vu apparaître depuis le lancement de SAML SSO.

## Partenariat du calendrier Rokt

[Le calendrier Rokt]({{site.baseurl}}/partners/additional_channels/calendar/rokt_calendar/) fournit aux clients Braze la possibilité d'aligner leurs initiatives marketing personnalisées et d'étendre le contenu personnalisé au calendrier de l'utilisateur final. Ainsi, en faisant une expérience plus homogène pour l'utilisateur final et en développant davantage la coloration avec les services de nos clients. Les clients seront en mesure de...

- Envoyer une invitation de calendrier via la plateforme Braze pour "sauvegarder la date" et prolonger notre communication
- Mettre à jour une invitation existante si le contenu de l'événement a changé.

## Partenariat Passkit

Avec [Passkit]({{site.baseurl}}/partners/additional_channels/mobile_wallet/passkit/), les clients de Braze pourront étendre leur engagement client à leur portefeuille mobile. Ils seront en mesure de personnaliser des campagnes de portefeuille tout en utilisant la segmentation puissante de Braze et orchestrent aux côtés de canaux tels que push, messages dans l'application, et plus encore.

## Retour de la valeur de l'ID d'envoi via les terminaux de messagerie

Un message `dispatch_id` sera inclus dans les réponses de terminaison suivantes :

- [`/fr/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/fr/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/fr/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/fr/messages/Schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/fr/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/fr/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

De cette façon, les clients qui utilisent la messagerie transactionnelle peuvent retracer le rappel à travers les courants.

## Logs des modifications de la toile

Vous êtes-vous même demandé plus de détails sur qui travaille sur un Canvas dans votre compte ? Ne vous étonnez plus! Vous pouvez maintenant accéder aux Changelogs de Canvas .

![Historique des modifications de la toile]({% image_buster /assets/img/canvas-changelogs.gif %})
