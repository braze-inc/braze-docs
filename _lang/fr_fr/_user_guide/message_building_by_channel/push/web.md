---
nav_title: "Notification push Web"
article_title: Notifications push Web
page_order: 8.5
page_type: reference
description: "Cette page de référence couvre brièvement les notifications push pour Web et relie les étapes nécessaires à leur création."
platform: Web
channel:
  - push

---

# Push Web

> Découvrez les notifications push web chez Braze et trouvez des ressources pour créer les vôtres.

Les notifications push pour Web sont un autre excellent moyen d’interagir avec les utilisateurs de votre application Web. Les clients qui visitent votre site web à partir de [navigateurs compatibles](#supported-browsers) peuvent s'abonner à la fonction "web push" de votre application web, que la page web soit chargée ou non.

## Aperçu

Les notifications push Web fournissent des informations urgentes et exploitables qui favorisent des conversions rapides. Avec les notifications push Web :

- Déclenchez des messages dès que des données importantes changent, comme une baisse de prix.
- Renvoyez les internautes vers votre site web à l'aide de boutons d'appel à l'action simples.
- Personnalisez votre push avec des informations sur le produit et le client pour rendre votre message pertinent.

Les notifications push pour Web fonctionnent de la même façon que les notifications push de l’application sur votre téléphone. Pour plus d'informations sur la composition d'une notification push Web, consultez la rubrique [Création d'une notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

![Exemple de communication web avec le même message affiché sur un ordinateur portable et un téléphone.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Cas d’usage potentiels

Voici quelques exemples d'utilisation courante des messages web push.

| Cas d’utilisation | Description |
| --- | --- | 
| Essai gratuit | Encouragez les nouveaux visiteurs de votre site web à s'inscrire à des essais gratuits. En donnant aux utilisateurs la possibilité de juger par eux-mêmes ce qui fait votre différence, vous multipliez vos chances de conversion vers votre offre payante. |
| Téléchargement de l'application | Attirez les internautes vers votre application mobile pour les aider à tirer encore plus de valeur de vos produits. Jouez la carte de la personnalisation pour mettre en avant les avantages de l’application en fonction des schémas d’engagement actuels. |
| Promotions et rabais | Sensibilisez davantage les clients aux événements et aux promotions limités dans le temps. Envoyez des messages sur plusieurs canaux, y compris des notifications push Web, afin de faire connaître les promotions de votre marque. |
| Abandon de panier | Envoyez des rappels automatisés aux utilisateurs qui n'ont pas terminé leurs transactions pour les ramener dans le flux de paiement. <br><br>Selon une étude menée par Braze, les notifications push Web sont 53 % plus efficaces que l'e-mail et 23 % plus impactantes que les notifications push mobiles pour inciter les destinataires à revenir et à finaliser un achat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conditions préalables à l'utilisation de web push

Avant de pouvoir créer et envoyer des messages push à l'aide de Braze, vous devez travailler avec vos développeurs pour intégrer push dans votre site web. Pour connaître les étapes détaillées, consultez notre [guide d'intégration des notifications push Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Autorisation des notifications push

Toute marque peut intégrer et utiliser les notifications push web sur son site web. Les notifications peuvent atteindre à la fois les visiteurs actuels et antérieurs sur le Web, à condition qu’ils disposent d’un navigateur Web ouvert, mais les visiteurs doivent [s’abonner pour recevoir des notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission), comme avec les notifications push traditionnelles d'une application mobile.

{% alert tip %}
Envisagez d'utiliser un message dans le navigateur pour inciter les utilisateurs à s’abonner aux notifications push Web, ce que l’on appelle également une [amorce de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Navigateurs pris en charge

Les navigateurs suivants prennent en charge les notifications push web. Cependant, les fenêtres de navigation privée ne prennent actuellement pas en charge les notifications push Web.

- Chrome (et Chrome pour Android mobile)
- Safari
- Firefox (et Firefox pour Android mobile)
- Opera
- Edge

Pour plus d’informations sur les normes de protocole de notifications push et la prise en charge du navigateur, vous pouvez consulter les ressources de votre navigateur :

- [Safari (bureau)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (mobile)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


