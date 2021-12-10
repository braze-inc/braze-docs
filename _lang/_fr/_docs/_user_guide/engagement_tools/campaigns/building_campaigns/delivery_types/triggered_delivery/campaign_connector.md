---
nav_title: Connecteur de campagne
article_title: Connecteur de campagne
page_order: 2
tool: Campagnes
page_type: tutoriel
description: "Cet article sur le mode d'emploi va au-delà de ce qu'est le connecteur de campagne de Braze et comment l'utiliser pour livrer du contenu ciblé et pertinent au bon moment."
---

# Connecteur de campagne

> Cet article sur le mode d'emploi va au-delà de ce qu'est le connecteur de campagne de Braze et comment l'utiliser pour livrer du contenu ciblé et pertinent au bon moment.

## Aperçu

Le connecteur de campagne de braze vous permet de créer des campagnes qui sont déclenchées lorsque les utilisateurs interagissent avec des campagnes actives ou des cartes de flux d'actualités. Cette fonctionnalité est utile car elle vous permet de fournir des contenus ciblés et pertinents au bon moment. Cette fonctionnalité vous permet de cibler les utilisateurs qui complètent les interactions suivantes avec les campagnes actives :

- Afficher le message dans l'application
- Cliquez sur le message dans l'application
- Cliquez sur l'e-mail
- Ouvrir l'e-mail
- Ouvrir directement la notification push
- Effectuer un événement de conversion
- Recevoir un e-mail
- Recevoir une notification push
- Sont inscrits à un groupe de contrôle

En plus des utilisateurs qui complètent les interactions suivantes avec les cartes de flux d'actualités actives :

- Voir
- Click

## Règles de livraison

La fonction de connecteur de campagne ne fonctionne qu'avec les campagnes actives. De plus, vous ne pouvez pas utiliser Campaign Connector pour envoyer un message à un utilisateur après avoir terminé une interaction avec une campagne. Par exemple, si vous êtes une campagne marketing pendant 9 semaines et que vous avez mis en place une campagne de suivi qui utilise le connecteur de campagne au début de la semaine 4, la campagne suivante ne transmettra aux utilisateurs que des messages qui ont interagi avec la campagne de marketing après la publication de la campagne suivante (semaines 4-9). Par conséquent, afin de vous assurer que vos campagnes de suivi atteignent tous les utilisateurs que vous visez, vous devriez :

- Configurez votre campagne originale comme brouillon
- Configurer et publier votre campagne de suivi
- Publier la campagne originale

Ces règles de livraison sont particulièrement pertinentes si vous ciblez les utilisateurs qui sont inscrits dans un groupe de contrôle, recevoir un courriel ou recevoir une notification push. Parce que les utilisateurs seront inscrits au groupe de contrôle dès que vous publierez la campagne originale, vous devez publier la campagne suivante avant de publier la campagne originale. De même, si vous publiez la campagne originale avant la campagne suivante, de nombreux utilisateurs peuvent recevoir votre courriel et/ou une notification push avant la publication de la campagne suivante.

## Comment utiliser la fonction de connecteur de campagne

### Étape 1 : Créer une nouvelle campagne

Écrivez les messages que vous souhaitez envoyer à vos utilisateurs. Vous pouvez choisir une campagne classique ou une campagne à une seule chaîne, selon votre cas d'utilisation.

### Étape 2 : Sélectionnez l'interaction et la campagne cible

Vous pouvez cibler les utilisateurs qui interagissent avec une campagne active, ou les utilisateurs qui interagissent avec une fiche de nouvelles active.

#### Cibler les utilisateurs qui interagissent avec une campagne

Sélectionnez [Action-Based Delivery][7] et ajoutez le déclencheur "Interact with Campaign". Ensuite, choisissez l'interaction de déclenchement. Ensuite, vous sélectionnerez la campagne active que vous souhaitez cibler.

!\[Interact with Campaign\]\[4\]

#### Cibler les utilisateurs qui interagissent avec une carte de flux d'actualités

Sélectionnez **Action-Based Delivery** et ajoutez le déclencheur "Interact with Card". Choisissez ensuite si vous souhaitez cibler les utilisateurs qui affichent une fiche de flux d'actualités ou les utilisateurs qui cliquent sur une fiche d'actualité. Sélectionnez la carte de flux d'actualités que vous souhaitez cibler.

!\[Interact With Card\]\[5\]

### Étape 3: Définir le délai de programmation et ajouter des exceptions si nécessaire

Si vous choisissez de définir un délai de planification, vous pouvez ajouter une exception à l'action de déclencheur. Par exemple, vous voudrez peut-être renvoyer une campagne d'email aux utilisateurs qui n'ont pas ouvert l'e-mail original.  Dans ce scénario, vous pouvez choisir "Courriel reçu" comme déclencheur et définir un délai d'une semaine. Ensuite, vous pouvez ajouter "Ouvrir l'e-mail" comme une exception. Maintenant, vous allez renvoyer l’e-mail aux utilisateurs qui n’ont pas ouvert l’e-mail original dans la semaine suivant sa réception.

!\[Schedule Delay\]\[6\]

Les événements d'exception ne se déclencheront que lorsqu'un utilisateur attend de recevoir le message auquel il est associé. Si un utilisateur effectue l'action avant d'attendre le message, l'événement d'exception ne se déclenchera pas.

### Étape 4 : Procéder à la création de la campagne

Continuez à créer votre campagne comme vous le feriez normalement. Notez que si vous voulez vous assurer que vous envoyez un message à chaque utilisateur qui va interagir avec une campagne spécifique, il serait alors préférable de cibler un segment qui contient tous les utilisateurs de votre application.

## Cas d'utilisation

Vous pouvez utiliser Campaign Connector pour cibler les utilisateurs qui s'engagent ou ne s'engagent pas dans des campagnes actives.

Par exemple, vous pouvez choisir de cibler les utilisateurs qui ont cliqué sur un message promotionnel push qui a annoncé la livraison gratuite afin que vous puissiez leur envoyer un message promotionnel publicitaire de 15% de réduction sur un achat.

Ou, vous pouvez suivre les utilisateurs qui ont cliqué sur un lien profond dans un message intégré dans l'application en leur envoyant un autre message dans l'application qui met en évidence des fonctionnalités supplémentaires.  De cette façon, vous pouvez cibler les utilisateurs qui ont démontré qu'ils sont intéressés à en apprendre davantage sur les fonctionnalités de votre application et éviter d'ennuyer les utilisateurs qui préfèrent découvrir ces fonctionnalités par eux-mêmes.

Vous pouvez également utiliser cette fonctionnalité pour cibler les utilisateurs qui reçoivent une notification push leur rappelant qu'ils ont abandonné leur panier. Par exemple, vous pourriez vouloir renvoyer la notification aux utilisateurs qui ne l'ont pas ouverte directement. Cependant, vous voudrez probablement exclure les utilisateurs qui ont effectué un achat depuis que vous envoyez la notification originale, même s'ils ne l'ont pas ouvert directement. Vous pouvez atteindre ce cas d'utilisation en ajoutant un déclencheur "Notification push reçue" pour la campagne "Panier abandonné", en définissant un délai de temps et en ajoutant « Effectue l'achat» et « Notifications push ouvertes directement» en tant qu'exceptions.
[4]: {% image_buster /assets/img_archive/Campaign_Connector1.png %} [5]: {% image_buster /assets/img_archive/Campaign_Connector2.png %} [6]: {% image_buster /assets/img_archive/Campaign_Connector3.png %}

[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
