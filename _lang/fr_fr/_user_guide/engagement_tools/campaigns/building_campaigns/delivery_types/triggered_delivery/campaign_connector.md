---
nav_title: Connecteur de campagne
article_title: Connecteur de campagne
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Cet article pratique passe en revue ce qu'est Campaign Connector et comment l'utiliser pour diffuser un contenu ciblé et pertinent au bon moment."

---
# Connecteur de campagne

> Campaign Connector vous permet de créer des campagnes qui se déclenchent lorsque les utilisateurs interagissent avec des campagnes actives ou des cartes du fil d'actualité. Cette fonctionnalité est utile car elle vous permet de fournir des contenus ciblés et pertinents au bon moment. 

{% alert note %}
Cet article comprend des informations sur les fils d’actualité, qui deviennent obsolètes. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

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

Ainsi que les utilisateurs qui effectuent les interactions suivantes avec les cartes de fil d’actualité actives :

- Afficher
- Clic

## Règles de livraison

La fonction de connecteur de campagne marche uniquement avec des campagnes actives. De plus, vous ne pouvez pas utiliser le connecteur de campagne pour envoyer un message à un utilisateur après qu’ils aient effectué une interaction avec une campagne. Par exemple, si vous faites fonctionner une campagne marketing pendant neuf semaines et que vous avez mis en place une campagne de suivi qui utilise le connecteur de campagne au début de la quatrième semaine, la campagne de suivi ne livrera des messages qu’aux utilisateurs qui ont interagi avec la campagne marketing après la publication de la campagne de suivi (semaines 4 à 9). Par conséquent, afin de garantir que vos campagnes de suivi atteignent tous les utilisateurs que vous ciblez, vous devez :

- Préparer votre campagne d’origine en tant que brouillon
- Configurer et publier votre campagne de suivi
- Publier la campagne originale

Ces règles de livraison sont particulièrement pertinentes si vous ciblez des utilisateurs qui sont inscrits dans un groupe de contrôle, qui reçoivent un e-mail ou une notification push. Étant donné que les utilisateurs seront inscrits dans le groupe de contrôle dès que vous publierez la campagne originale, vous devez publier la campagne de suivi avant de publier la campagne originale. De même, si vous publiez la campagne originale avant la campagne de suivi, de nombreux utilisateurs peuvent recevoir votre e-mail ou votre notification push avant la publication de la campagne de suivi.

## Comment utiliser la fonction de connecteur de campagne

### Étape 1 : Créer une nouvelle campagne

Composez les messages que vous souhaitez envoyer à vos utilisateurs. Vous pouvez sélectionner une campagne classique ou une campagne sur un canal unique, selon votre cas d’usage.

### Étape 2 : Sélectionner une interaction et cibler une campagne

Vous pouvez cibler les utilisateurs qui interagissent avec une campagne active ou les utilisateurs qui interagissent avec une carte de fil d’actualité active.

#### Cibler les utilisateurs qui interagissent avec une campagne

Sélectionnez [Livraison par événement][7] et ajoutez le déclencheur « Interagir avec la campagne ». Ensuite, choisissez l’interaction de déclenchement. Ensuite, vous sélectionnerez la campagne active que vous souhaitez cibler.

![][4]

#### Cibler des utilisateurs qui interagissent avec une carte de fil d’actualité (en cours d’obsolescence)

Sélectionnez la **livraison/distribution par événement** et ajoutez le déclencheur "Interagir avec la carte". Choisissez ensuite si vous souhaitez cibler les utilisateurs qui consultent une carte de fil d’actualité ou des utilisateurs qui cliquent dessus. Sélectionnez la carte de fil d’actualité active que vous souhaitez cibler.

![][5]

### Étape 3 : Définir le délai de planification et ajouter des exceptions si nécessaire

Si vous choisissez de définir un délai de planification, vous pouvez ajouter une exception à l’action de déclenchement. Par exemple, vous pouvez désirer renvoyer une campagne e-mail aux utilisateurs qui n’ont pas ouvert l’e-mail d’origine.  Dans ce scénario, vous pouvez choisir « Recevoir un e-mail » comme déclencheur et définir un délai de planification d’une semaine. Ensuite, vous pouvez ajouter « Ouvrir l’e-mail » en tant qu’exception. Vous allez maintenant renvoyer l’e-mail aux utilisateurs qui n’ont pas ouvert l’e-mail d’origine dans la semaine qui suit la réception.

![][6]

Les événements d’exception sont uniquement déclenchés lorsqu’un utilisateur attend de recevoir le message qui lui est associé. Si un utilisateur effectue l’action avant d’avoir à attendre le message, l’événement d’exception ne sera pas déclenché.

### Étape 4 : Poursuivre la création de la campagne

Continuez à créer votre campagne comme vous le feriez normalement. Notez que si vous souhaitez vous assurer que vous envoyez un message à chaque utilisateur qui va interagir avec une campagne spécifique, il serait préférable de cibler un segment qui contient tous les utilisateurs de votre application.

## Cas d’utilisation

Vous pouvez utiliser le connecteur de campagne pour cibler les utilisateurs qui s’engagent ou ne s’engagent pas avec des campagnes actives.

Par exemple, vous pouvez choisir de cibler les utilisateurs qui ont cliqué sur un message publicitaire de notification push qui promouvait une expédition gratuite afin que vous puissiez leur envoyer un message publicitaire en notification push annonçant 15 % de réduction sur un achat.

Vous pouvez également effectuer un suivi avec les utilisateurs qui ont cliqué sur un lien profond dans un message in-app d’onboarding en leur envoyant un autre message in-app qui met en valeur des fonctionnalités supplémentaires.  De cette façon, vous pouvez cibler les utilisateurs qui ont démontré qu’ils souhaitaient en savoir plus sur les caractéristiques de votre application et éviter d’ennuyer les utilisateurs qui préfèrent découvrir ces fonctionnalités par eux-mêmes.

Le connecteur de campagne peut également cibler les utilisateurs qui reçoivent une notification push leur rappelant qu’ils ont abandonné leur panier. Par exemple, vous pouvez renvoyer la notification aux utilisateurs qui ne l’ont pas directement ouverte. Cependant, vous souhaiterez probablement exclure les utilisateurs qui ont effectué un achat depuis que vous avez envoyé la notification d’origine, même s’ils ne l’ont pas directement ouverte. Vous pouvez effectuer ce cas d’utilisation en ajoutant un déclencheur « Notification push reçue » pour la campagne « Panier abandonné », en définissant un délai de planification et en ajoutant « Effectuer l’achat » et « Notifications push ouvertes directement » en tant qu’exceptions.

[4]: {% image_buster /assets/img_archive/Campaign_Connector1.png %}
[5]: {% image_buster /assets/img_archive/Campaign_Connector2.png %}
[6]: {% image_buster /assets/img_archive/Campaign_Connector3.png %}
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/