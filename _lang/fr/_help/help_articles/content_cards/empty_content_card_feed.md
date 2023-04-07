---
nav_title: Flux de carte de contenu vide
article_title: Flux de carte de contenu vide
page_order: 0

page_type: solution
description: "Cet article d’aide décrit pourquoi les nouveaux utilisateurs peuvent ne pas avoir de cartes de contenu dans leur flux et comment résoudre ce problème."
channel: cartes de contenu
---

# Flux de carte de contenu vide

Lors de l’envoi d’une campagne de carte de contenu avec livraison planifiée, l’option que vous choisissez pour la [création de carte]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#overview) peut affecter le fait que les nouveaux utilisateurs aient des cartes dans leur flux lors de leur première session. Si **Card Creation (Création de carte)** est définie sur **At campaign launch (Au lancement de campagne)**, les utilisateurs qui sont créés après le lancement de la campagne ne recevront pas la carte de contenu dans leur flux, car Braze évalue l’appartenance à l’audience lorsque la campagne est envoyée.

Si vous souhaitez qu’un nouvel utilisateur reçoive des cartes, effectuez l’une des opérations suivantes :

- Créez une campagne de livraison planifiée et définissez **Card Creation (Création de carte)** sur **At first impression (À la première impression)**. Ils recevront cette carte à leur prochaine session.
- Créez une campagne à livraison par événement. Ils recevront cette carte la prochaine fois qu’ils effectueront l’action sélectionnée.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 17 mars 2023_