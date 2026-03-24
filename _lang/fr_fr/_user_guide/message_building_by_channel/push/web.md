---
nav_title: "Push Web"
article_title: Notifications push Web
page_order: 8.5
page_type: reference
description: "Cette page de référence couvre brièvement les notifications push pour Web et renvoie vers les étapes nécessaires à leur création."
platform: Web
channel:
  - push

---

# Push Web

> Découvrez les notifications push web avec Braze et trouvez des ressources pour créer les vôtres.

Les notifications push web sont un excellent moyen d'interagir avec les utilisateurs de votre application web. Les clients qui visitent votre site web à partir de [navigateurs compatibles](#supported-browsers) peuvent s'abonner aux notifications push de votre application web, que la page web soit chargée ou non.

## Aperçu

Les notifications push web fournissent des informations urgentes et exploitables qui favorisent des conversions rapides. Avec les notifications push web, vous pouvez :

- Déclencher des messages dès que des données importantes changent, comme une baisse de prix
- Ramener les visiteurs vers votre site web grâce à des boutons d'action clairs
- Personnaliser vos notifications push avec des informations sur le produit et le client pour rendre votre message pertinent

Les notifications push web fonctionnent de la même façon que les notifications push sur votre téléphone. Pour plus d'informations sur la composition d'une notification push web, consultez [Créer une notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

![Exemple de push web avec le même message push affiché sur un ordinateur portable et un téléphone.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Cas d'utilisation potentiels

Voici quelques exemples courants de cas d'utilisation des messages push web.

| Cas d'utilisation | Description |
| --- | --- | 
| Essai gratuit | Encouragez les nouveaux visiteurs de votre site web à s'inscrire à des essais gratuits. En donnant aux utilisateurs la possibilité de juger par eux-mêmes ce qui fait votre différence, vous multipliez vos chances de les convertir en clients payants. |
| Téléchargement de l'application | Attirez les internautes vers votre application mobile pour les aider à tirer encore plus de valeur de vos produits. Jouez la carte de la personnalisation pour mettre en avant les avantages de l'application en fonction de leurs habitudes d'engagement actuelles. |
| Promotions et soldes | Sensibilisez davantage les clients aux événements et aux promotions limités dans le temps. Envoyez des messages sur plusieurs canaux, y compris des notifications push web, afin de faire connaître les promotions de votre marque. |
| Abandon de panier | Envoyez des rappels automatisés aux utilisateurs qui n'ont pas terminé leurs transactions pour les ramener dans le flux de paiement. <br><br>Selon une étude menée par Braze, les notifications push web sont 53 % plus efficaces que l'e-mail et 23 % plus impactantes que les notifications push mobiles pour inciter les destinataires à revenir et à finaliser un achat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conditions préalables à l'utilisation du push web

Avant de pouvoir créer et envoyer des messages push avec Braze, vous devez travailler avec vos développeurs pour intégrer les notifications push dans votre site web. Pour connaître les étapes détaillées, consultez notre [guide d'intégration des notifications push web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Autorisation des notifications push

Toute marque peut intégrer et utiliser les notifications push web sur son site web. Les notifications peuvent atteindre à la fois les visiteurs actuels et précédents, à condition qu'ils disposent d'un navigateur web ouvert. Cependant, les visiteurs doivent [s'abonner pour recevoir des notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission), comme pour les notifications push classiques d'une application mobile.

{% alert tip %}
Envisagez d'utiliser un message dans le navigateur pour inciter les utilisateurs à s'abonner aux notifications push web, ce que l'on appelle également une [amorce de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Navigateurs pris en charge

Les navigateurs suivants prennent en charge les notifications push web.

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome (et Chrome pour Android mobile)
- Safari (version 16 ou ultérieure)
- Firefox (et Firefox pour Android mobile)
- Opera
- Edge

Pour plus d'informations sur les normes de protocole des notifications push et la compatibilité des navigateurs, vous pouvez consulter les ressources correspondant à votre navigateur :

- [Safari (bureau)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (mobile)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)