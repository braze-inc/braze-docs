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

## Comment cela fonctionne-t-il ?

Cette fonctionnalité vous permet de cibler les utilisateurs qui effectuent les interactions suivantes avec des campagnes actives :

- Voir le message in-app
- Cliquez sur le message in-app.
- Cliquez sur les boutons d'envoi de messages in-app.
- Cliquez sur e-mail
- Cliquez sur l'alias dans l'e-mail
- Ouvrir l'e-mail
- Ouvrir directement la notification push
- Cliquez sur le bouton de notification push
- Cliquez sur la page du contenu push
- Effectuer un événement de conversion
- Recevoir un e-mail
- Recevoir des SMS
- Cliquez sur le lien SMS abrégé
- Recevoir une notification push
- Recevoir un webhook
- sont inscrits dans un groupe de contrôle
- Voir la carte de contenu
- Cliquez sur la carte de contenu
- Fermeture de la carte de contenu

### Règles de réception/distribution

Notez que vous ne pouvez pas utiliser Campaign Connector pour envoyer un message à un utilisateur après qu'il a terminé une interaction avec une campagne. Par exemple, si vous menez une campagne marketing pendant neuf semaines et que vous mettez en place une campagne de suivi qui utilise Campaign Connector au début de la quatrième semaine, la campagne de suivi n'enverra des messages qu'aux utilisateurs qui ont interagi avec la campagne marketing après la publication de la campagne de suivi (semaines 4 à 9). Par conséquent, afin de vous assurer que vos campagnes de suivi atteignent chaque utilisateur que vous ciblez, vous devez :

- Implantez votre campagne originale en tant que brouillon
- Implémentez et publiez votre campagne de suivi
- Publier la campagne originale

Ces règles de réception/distribution sont particulièrement pertinentes si vous ciblez des utilisateurs inscrits dans un groupe de contrôle, recevant un e-mail ou recevant une notification push. Étant donné que les utilisateurs seront inscrits dans le groupe de contrôle dès la publication de la campagne initiale, vous devez publier la campagne de suivi avant de publier la campagne initiale. De même, si vous publiez la campagne d'origine avant la campagne de suivi, de nombreux utilisateurs risquent de recevoir votre e-mail et/ou votre notification push avant la publication de la campagne de suivi.

## Utiliser Campaign Connector avec vos campagnes

### Étape 1 : Créer une nouvelle campagne

Composez les messages que vous souhaitez envoyer à vos utilisateurs. Vous pouvez sélectionner une campagne monocanal ou multicanal, en fonction de votre cas d'utilisation.

### Étape 2 : Sélectionnez l'interaction et le ciblage de la campagne

1. Sélectionnez la [réception/distribution basée sur l'action]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) et ajoutez le déclencheur "Interagir avec la campagne" pour cibler les utilisateurs qui interagissent avec une campagne active. 
2. Choisissez l'interaction du déclencheur. 
3. Ensuite, vous sélectionnerez la campagne active que vous souhaitez cibler.

\![]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### Étape 3 : Définir le délai de la planification et ajouter des exceptions (facultatif)

Si vous choisissez de fixer un délai de planification, vous pouvez ajouter une exception à l'action de déclenchement. Par exemple, vous pourriez vouloir renvoyer une campagne d'e-mails aux utilisateurs qui n'ont pas ouvert l'e-mail original.  Dans ce scénario, vous pouvez choisir "Courriel reçu" comme déclencheur et fixer un délai de planification d'une semaine. Ensuite, vous pouvez ajouter "Ouvrir un e-mail" comme exception. Vous allez maintenant renvoyer l'e-mail aux utilisateurs qui n'ont pas ouvert l'e-mail original dans la semaine suivant sa réception.

\![]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

Les événements d'exception ne se déclenchent que lorsqu'un utilisateur attend de recevoir le message auquel ils sont associés. Si un utilisateur effectue l'action avant d'attendre le message, l'événement d'exception ne se déclenche pas.

### Étape 4 : Procéder à la création de la campagne

Continuez à créer votre campagne comme vous le feriez normalement. Notez que si vous voulez vous assurer d'envoyer un message à chaque utilisateur qui va interagir avec une campagne spécifique, alors il serait préférable de cibler un segment qui contient tous les utilisateurs de votre appli.

## Cas d'utilisation

Vous pouvez utiliser Campaign Connector pour cibler les utilisateurs qui s'engagent ou non dans des campagnes actives.

Par exemple, vous pouvez choisir de cibler les utilisateurs qui ont cliqué sur un message push promotionnel annonçant des frais de port gratuits afin de leur envoyer un message push promotionnel annonçant une réduction de 15 % sur un achat.

Vous pouvez également assurer le suivi des utilisateurs qui ont cliqué sur un lien profond dans un message in-app d'onboarding en leur envoyant un autre message in-app qui met en avant des fonctionnalités supplémentaires.  De cette façon, vous pouvez cibler les utilisateurs qui ont démontré qu'ils étaient intéressés par la découverte des fonctionnalités de votre application et éviter d'ennuyer les utilisateurs qui préfèrent découvrir ces fonctionnalités par eux-mêmes.

Campaign Connector peut également cibler les utilisateurs qui reçoivent une notification push leur rappelant qu'ils ont abandonné leur panier. Par exemple, vous pouvez renvoyer la notification aux utilisateurs qui ne l'ont pas ouverte directement. Cependant, vous souhaiterez probablement exclure les utilisateurs qui ont effectué un achat depuis l'envoi de la notification initiale, même s'ils ne l'ont pas ouverte directement. Vous pouvez réaliser ce cas d'utilisation en ajoutant un déclencheur "Received push notification" pour la campagne "Abandoned Cart", en définissant un délai de planification et en ajoutant "Makes Purchase" et "Directly opened push notifications" comme exceptions.

