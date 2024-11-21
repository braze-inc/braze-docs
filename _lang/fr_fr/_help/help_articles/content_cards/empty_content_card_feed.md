---
nav_title: Flux de carte de contenu vide
article_title: Flux de carte de contenu vide
page_order: 0

page_type: solution
description: "Cet article d’aide décrit pourquoi les nouveaux utilisateurs peuvent ne pas avoir de cartes de contenu dans leur flux et comment résoudre ce problème."
channel: content cards
---

# Flux de carte de contenu vide

Lors de l'envoi d'une campagne de cartes de contenu avec réception/distribution planifiée, l'option que vous choisissez pour la [création des cartes]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#overview) peut avoir une incidence sur l'affichage des cartes dans le fil d'actualité des nouveaux utilisateurs lors de leur première session. Si la **création de cartes** est définie sur **Au lancement de la campagne**, les utilisateurs créés après le lancement de la campagne ne recevront pas la carte de contenu dans leur flux, car Braze évalue l'appartenance à l'audience au moment où la campagne est lancée.

Si vous souhaitez qu’un nouvel utilisateur reçoive des cartes, effectuez l’une des opérations suivantes :

- Créez une campagne de réception/distribution planifiée et définissez la **création de la carte** sur **À la première impression.** Ils recevront cette carte lors de leur première séance.
- Créez une campagne à livraison par événement. Ils recevront cette carte la prochaine fois qu’ils effectueront l’action sélectionnée.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 17 avril 2023_
