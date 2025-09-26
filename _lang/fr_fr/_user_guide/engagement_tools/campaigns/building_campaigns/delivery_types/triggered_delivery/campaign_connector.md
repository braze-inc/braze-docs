---
nav_title: Connecteur de campagne
article_title: Connecteur de campagne
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Cet article pratique passe en revue ce qu'est Campaign Connector et comment l'utiliser pour diffuser un contenu ciblé et pertinent au bon moment."

---
# Connecteur de campagne

> Campaign Connector vous permet de créer des campagnes qui sont déclenchées lorsque les utilisateurs interagissent avec des campagnes actives. Vous pouvez diffuser un contenu ciblé et pertinent au bon moment.

## Fonctionnement

Cette fonction vous permet de cibler les utilisateurs qui effectuent les interactions suivantes avec les campagnes actives :

- Consultent un message in-app
- Cliquent sur un message in-app
- Cliquez sur le bouton de message in-app
- Cliquer sur l’e-mail
- Cliquez sur l’alias dans l’e-mail
- Ouvrir l’e-mail
- Ouvrent directement une notification push
- Cliquez sur le bouton de notification push
- Cliquez sur la page de push story
- Effectuent un événement de conversion
- Recevoir un e-mail
- Reçoit un SMS
- Cliquez sur le lien SMS raccourci
- Reçoivent une notification push
- Reçoit le webhook
- Sont inscrits dans un groupe de contrôle
- Consulte une carte de contenu
- Cliquez une carte de contenu
- Rejette une carte de contenu

### Règles de livraison

Notez que vous ne pouvez pas utiliser Campaign Connector pour envoyer un message à un utilisateur après qu'il a terminé une interaction avec une campagne. Par exemple, si vous menez une campagne marketing pendant neuf semaines et que vous configurez une campagne de suivi qui utilise Campaign Connector au début de la quatrième semaine, la campagne de suivi n'enverra des messages qu'aux utilisateurs qui ont interagi avec la campagne marketing après la publication de la campagne de suivi (semaines 4 à 9). Par conséquent, afin de garantir que vos campagnes de suivi atteignent tous les utilisateurs que vous ciblez, vous devez :

- Préparer votre campagne d’origine en tant que brouillon
- Configurer et publier votre campagne de suivi
- Publier la campagne originale

Ces règles de livraison sont particulièrement pertinentes si vous ciblez des utilisateurs qui sont inscrits dans un groupe de contrôle, qui reçoivent un e-mail ou une notification push. Étant donné que les utilisateurs seront inscrits dans le groupe de contrôle dès que vous publierez la campagne originale, vous devez publier la campagne de suivi avant de publier la campagne originale. De même, si vous publiez la campagne originale avant la campagne de suivi, de nombreux utilisateurs peuvent recevoir votre e-mail ou votre notification push avant la publication de la campagne de suivi.

## Utiliser Campaign Connector avec vos campagnes

### Étape 1 : Créer une nouvelle campagne

Composez les messages que vous souhaitez envoyer à vos utilisateurs. Vous pouvez sélectionner une campagne monocanal ou multicanal, en fonction de votre cas d'utilisation.

### Étape 2 : Sélectionner une interaction et cibler une campagne

1. Sélectionnez la [réception/distribution basée sur l'action]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) et ajoutez le déclencheur "Interagir avec la campagne" pour cibler les utilisateurs qui interagissent avec une campagne active. 
2. Choisissez l'interaction du déclencheur. 
3. Ensuite, vous sélectionnerez la campagne active que vous souhaitez cibler.

![]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### Étape 3 : Définir le délai de la planification et ajouter des exceptions (facultatif)

Si vous choisissez de définir un délai de planification, vous pouvez ajouter une exception à l’action de déclenchement. Par exemple, vous pouvez désirer renvoyer une campagne e-mail aux utilisateurs qui n’ont pas ouvert l’e-mail d’origine.  Dans ce scénario, vous pouvez choisir « Recevoir un e-mail » comme déclencheur et définir un délai de planification d’une semaine. Ensuite, vous pouvez ajouter « Ouvrir l’e-mail » en tant qu’exception. Vous allez maintenant renvoyer l’e-mail aux utilisateurs qui n’ont pas ouvert l’e-mail d’origine dans la semaine qui suit la réception.

![]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

Les événements d’exception sont uniquement déclenchés lorsqu’un utilisateur attend de recevoir le message qui lui est associé. Si un utilisateur effectue l’action avant d’avoir à attendre le message, l’événement d’exception ne sera pas déclenché.

### Étape 4 : Poursuivre la création de la campagne

Continuez à créer votre campagne comme vous le feriez normalement. Notez que si vous souhaitez vous assurer que vous envoyez un message à chaque utilisateur qui va interagir avec une campagne spécifique, il serait préférable de cibler un segment qui contient tous les utilisateurs de votre application.

## Cas d’utilisation

Vous pouvez utiliser le connecteur de campagne pour cibler les utilisateurs qui s’engagent ou ne s’engagent pas avec des campagnes actives.

Par exemple, vous pouvez choisir de cibler les utilisateurs qui ont cliqué sur un message publicitaire de notification push qui promouvait une expédition gratuite afin que vous puissiez leur envoyer un message publicitaire en notification push annonçant 15 % de réduction sur un achat.

Vous pouvez également effectuer un suivi avec les utilisateurs qui ont cliqué sur un lien profond dans un message in-app d’onboarding en leur envoyant un autre message in-app qui met en valeur des fonctionnalités supplémentaires.  De cette façon, vous pouvez cibler les utilisateurs qui ont démontré qu’ils souhaitaient en savoir plus sur les caractéristiques de votre application et éviter d’ennuyer les utilisateurs qui préfèrent découvrir ces fonctionnalités par eux-mêmes.

Le connecteur de campagne peut également cibler les utilisateurs qui reçoivent une notification push leur rappelant qu’ils ont abandonné leur panier. Par exemple, vous pouvez renvoyer la notification aux utilisateurs qui ne l’ont pas directement ouverte. Cependant, vous souhaiterez probablement exclure les utilisateurs qui ont effectué un achat depuis que vous avez envoyé la notification d’origine, même s’ils ne l’ont pas directement ouverte. Vous pouvez effectuer ce cas d’utilisation en ajoutant un déclencheur « Notification push reçue » pour la campagne « Panier abandonné », en définissant un délai de planification et en ajoutant « Effectuer l’achat » et « Notifications push ouvertes directement » en tant qu’exceptions.

