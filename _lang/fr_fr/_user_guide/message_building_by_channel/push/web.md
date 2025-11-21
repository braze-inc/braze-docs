---
nav_title: "Poussée sur le web"
article_title: Notifications push web
page_order: 8.5
page_type: reference
description: "Cette page de référence présente brièvement les notifications push web et renvoie aux étapes nécessaires pour en créer une."
platform: Web
channel:
  - push

---

# Poussée sur le web

> Découvrez les notifications push web chez Braze et trouvez des ressources pour créer les vôtres.

Le push web est un autre excellent moyen d'engager le dialogue avec les utilisateurs de votre application web. Les clients qui visitent votre site web à partir de [navigateurs compatibles](#supported-browsers) peuvent s'abonner à la fonction "web push" de votre application web, que la page web soit chargée ou non.

## Aperçu

Les notifications push web délivrent des mises à jour urgentes et exploitables qui entraînent des conversions rapides. Avec web push, vous pouvez :

- Déclenchez des messages dès que des données importantes changent, comme une baisse de prix.
- Renvoyez les internautes vers votre site web à l'aide de boutons d'appel à l'action simples.
- Personnalisez votre push avec des informations sur le produit et le client pour rendre votre message pertinent.

Le Web push fonctionne de la même manière que les notifications push des applications sur votre téléphone. Pour plus d'informations sur la composition d'un push web, consultez la rubrique [Création d'une notification push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)

\![Exemple de push web avec le même message push affiché sur un ordinateur portable et un téléphone.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Cas d'utilisation potentiels

Voici quelques exemples d'utilisation courante des messages web push.

| Cas d'utilisation | Description |
| --- | --- | 
| Essai gratuit | Encouragez les nouveaux visiteurs de votre site web à s'inscrire à des essais gratuits. En offrant aux utilisateurs la possibilité de découvrir ce qui fait votre spécificité, vous augmentez les chances qu'ils deviennent des clients payants. |
| Télécharger l'application | Attirez les internautes vers votre application mobile pour les aider à tirer encore plus de valeur de vos produits. Envisagez de tirer parti de la personnalisation pour mettre en avant les avantages de l'app en fonction de leurs habitudes d'engagement actuelles. |
| Réductions et ventes | Sensibiliser davantage les clients aux événements et aux promotions sensibles au facteur temps. Envoi de messages sur plusieurs canaux, y compris le push sur le web, afin d'accroître la notoriété des promotions de votre marque. |
| Abandon de panier | Envoyez des rappels automatisés aux utilisateurs qui n'ont pas terminé leurs transactions pour les ramener dans le flux de paiement. <br><br>Une étude menée par Braze a révélé que le web push est 53 % plus efficace que l'e-mail et 23 % plus impactant que le push mobile pour inciter les destinataires à revenir et à finaliser un achat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conditions préalables à l'utilisation de web push

Avant de pouvoir créer et envoyer des messages push à l'aide de Braze, vous devez travailler avec vos développeurs pour intégrer push dans votre site web. Pour connaître les étapes détaillées, consultez notre [guide d'intégration Web push.]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

### Permission de pousser

Toute marque peut intégrer et utiliser les notifications push web sur son site web. Les notifications peuvent atteindre à la fois les visiteurs actuels et antérieurs du web tant qu'ils ont un navigateur web ouvert, mais les visiteurs doivent [opter pour recevoir des notifications - tout]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)comme avec le push traditionnel d'une application mobile.

{% alert tip %}
Envisagez d'utiliser un message dans le navigateur pour inciter les utilisateurs à opter pour l'[amorçage]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) de push web, également connu sous le nom de " [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)".
{% endalert %}

## Navigateurs pris en charge

Les navigateurs suivants prennent en charge les notifications push web. Cependant, les fenêtres de navigation privée ne prennent pas actuellement en charge le push web.

- Chrome (et Chrome pour Android mobile)
- Safari
- Firefox (et Firefox pour Android mobile)
- Opéra
- Bord

Pour plus d'informations sur les normes du protocole push et la prise en charge des navigateurs, vous pouvez consulter des ressources en fonction de votre navigateur :

- [Safari (bureau)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (mobile)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


