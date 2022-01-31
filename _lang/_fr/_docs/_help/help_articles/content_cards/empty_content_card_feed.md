---
nav_title: Flux de carte de contenu vide
article_title: Flux de carte de contenu vide
page_order: 0
page_type: Solution
description: "Cet article d'aide décrit pourquoi les nouveaux utilisateurs peuvent ne pas avoir de cartes de contenu dans leur flux et comment résoudre ce problème."
channel: cartes de contenu
---

# Flux de carte de contenu vide

Vous ne pouvez pas envoyer de cartes aux utilisateurs qui n'existent pas. Par définition, les nouveaux utilisateurs n'auront aucune carte dans leur flux lors de leur première session.

Si vous voulez qu'un nouvel utilisateur reçoive des cartes, [créez une campagne de Cartes de Contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/#content-cards) déclenchée sur l'événement [`SessionStart`]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/#session-start-event) sans rééligibilité pour que les utilisateurs ne reçoivent la campagne qu'une seule fois. Ils recevront cette carte lors de leur prochaine session.

Vous pouvez également envoyer la carte lors de leur première session. Appeler [`requestContentCardsRefresh`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/refreshing_the_feed/#refreshing-content-cards) sur le SDK durant cette session après avoir appelé `requestImmediateDataFlush`.

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 3 juin 2021_