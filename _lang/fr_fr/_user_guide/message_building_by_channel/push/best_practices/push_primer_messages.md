---
nav_title: Messages in-app d’amorce de notification push
article_title: Messages in-app d’amorce de notification push
page_order: 1
page_type: reference
description: "Cet article couvre les conditions préalables pour les messages in-app d’amorce de notification push et la manière de les configurer."
channel: push

---

# Messages in-app d’amorce de notification push

![Messages in-app d’amorce de notification push pour une application de streaming. La notification affiche « Get push notifications from Movie Cannon? (Voulez-vous recevoir des notifications push de Movie Cannon ?) Les notifications peuvent concerner de nouveaux films, des émissions de télévision ou d'autres avis et peuvent être désactivées à tout moment."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Vous n’avez qu’une seule chance de demander aux utilisateurs la permission de les joindre par notification push. L’optimisation de l’inscription aux notifications est donc cruciale pour maximiser la portée de vos messages push. Pour y parvenir, vous pouvez utiliser des messages in-app pour expliquer le type de messages auquel vos utilisateurs peuvent s’attendre à recevoir s’ils choisissent de s’inscrire, avant de leur montrer l’invite de notification push native. C’est ce qu’on appelle amorce de notification push.

Pour créer un message in-app d’amorce de notification push dans Braze, vous pouvez utiliser le bouton de comportement en cas de clic « Request Push Permission (Demander l’autorisation de notification push) » lors de la création d’un message in-app pour iOS, Android ou le Web.

## Conditions préalables

Cette fonctionnalité nécessite un [comportement de clic sur le bouton](#button-actions), qui est pris en charge dans les versions minimales suivantes ou ultérieures :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

En outre, notez les détails suivants, spécifiques à la plate-forme :

{% tabs local %}
{% tab android %}
|Version du système d'exploitation|Informations complémentaires|
\|----------|----------------------|
| **Android 12 et versions antérieures** | La mise en œuvre d'amorces de push n'est pas recommandée, car le push est accepté par défaut. |
| **Android 13+** | Si un utilisateur refuse deux fois votre demande d'autorisation push, Android bloque les autres messages, y compris les messages d'amorce push de Braze. Pour accorder l'autorisation après cela, les utilisateurs doivent activer manuellement le push pour votre application dans les paramètres de leur appareil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab swift %}
### Informations générales

- L'invite "push" ne peut être affichée qu'une seule fois par installation, ce qui est imposé par le système d'exploitation.
- L'invite ne s'affichera pas si le paramètre de notification de l'application est explicitement activé ou désactivé, elle ne s'affichera que pour les utilisateurs avec [autorisation provisoire](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **Le paramètre "push" de l'application est activé :** Braze n'affichera pas le message in-app, car l'utilisateur a déjà opté pour l'abonnement.
  - **Le paramètre de poussée de l'application est désactivé :** Vous devrez rediriger l'utilisateur vers les paramètres de notification push de votre application dans les paramètres de l'appareil.

### Enlever manuellement le code

Le message in-app que vous configurez à l’aide de ce tutoriel appellera automatiquement le code d’invite push natif lorsqu’un utilisateur clique sur le bouton du message in-app. Pour éviter de demander une autorisation de notification push deux fois ou au mauvais moment, les développeurs doivent modifier toute intégration de notification push existante qu’ils ont mise en œuvre afin de s’assurer que votre message in-app est la première amorce de notification push que vos utilisateurs verront.

Votre équipe de développement doit examiner votre mise en œuvre des notifications push pour votre app ou votre site et supprimer manuellement tout code qui demanderait une autorisation push. Par exemple, vous pouvez supprimer les références au code suivant :

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Étape 1 : Créer un message in-app

Tout d'abord, [créez un message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), puis sélectionnez votre type de message et sa mise en page.

Pour vous assurer que vous disposez de suffisamment d'espace pour votre message et vos boutons, utilisez une fenêtre modale/boîte de dialogue modale ou plein écran. Si vous choisissez le plein écran, notez qu'une image est nécessaire.

## Étape 2 : Créer votre message

Maintenant, il est temps d’ajouter votre copie ! Rappelez-vous qu’une amorce de notification push a l’objectif de pousser l’utilisateur à activer les notifications push. Dans votre corps de message, nous vous suggérons de mettre en exergue les raisons pour lesquelles vos utilisateurs devraient activer les notifications push. Soyez précis quant au type de notifications que vous souhaitez envoyer et à la valeur qu’ils peuvent fournir.

Par exemple, une application d’actualités peut utiliser l’amorce de notification push suivante :

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Une application de streaming pourrait utiliser ce qui suit :

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Pour connaître les meilleures pratiques et obtenir des ressources supplémentaires, reportez-vous à la section [Créer des demandes d'abonnement personnalisées]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Étape 3 : Spécifier le comportement du bouton {#button-actions}

Pour ajouter des boutons à votre message in-app, faites glisser deux blocs **Bouton** dans votre message, qui feront office de boutons principal et secondaire dans votre message in-app. Vous pouvez également faire glisser une rangée dans votre message, puis faire glisser les boutons dans la rangée, de manière à ce que les boutons se trouvent sur la même rangée horizontale (et non pas empilés les uns sur les autres). Nous recommandons d’activer les boutons « Allow notifications » (Autoriser les notifications) et « Not now » (Pas maintenant) comme boutons d’amorce, mais il existe de nombreuses invites de bouton différentes que vous pouvez attribuer.

Après avoir ajouté la copie du bouton, spécifiez le comportement en cas de clic pour chaque bouton :

- **Bouton 1:** Définissez celui-ci sur « Close Message » (Fermer le message). Il s’agit de votre bouton secondaire ou de l’option « Not now » (Pas maintenant).
- **Bouton 2 :** Définissez cette option sur « Request Push Permission » (Demander l’autorisation de notification push). Il s’agit du bouton principal ou de l’option « Allow notifications » (Autoriser les notifications).

![Compositeur de messages in-app avec deux boutons : "Autoriser les notifications" et "Pas maintenant".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Étape 4 : Planifier la livraison

Pour définir votre amorce push pour l'envoyer à un moment pertinent, vous devez programmer votre message intégré à l'application comme un message basé sur une action avec **Effectuer un événement personnalisé** comme action déclencheuse.

Bien que le moment idéal puisse varier, Braze suggère d'attendre qu'un utilisateur effectue une sorte de [action de grande valeur](https://www.braze.com/resources/videos/mapping-high-value-actions), indiquant qu'il commence à voir la valeur de votre application ou site, ou lorsqu'il y a un besoin impérieux que les notifications push peuvent répondre (comme après qu'ils aient passé une commande et que vous souhaitiez leur offrir des informations de suivi d'expédition). De cette façon, l’invite représente un avantage pour le client plutôt que pour votre marque.

![Paramètres de réception/distribution par événement à envoyer aux utilisateurs ayant effectué l'événement personnalisé "Ajouter à la liste de surveillance".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Étape 5 : Utilisateurs cibles

Étant donné que l’objectif d’une campagne de notification push est d’inciter les utilisateurs à s’abonner aux messages push, vous ne voulez pas cibler les utilisateurs qui y sont déjà abonnés. Pour ce faire, ajoutez un segment ou un filtre pour ces utilisateurs, à savoir, `Push Subscription Status is not Opted In`.

Au-delà de cela, vous pouvez décider des segments supplémentaires qui vous semblent les plus appropriés. Par exemple, vous pouvez cibler les utilisateurs qui ont effectué un deuxième achat, les utilisateurs qui viennent de créer un compte pour devenir membre ou même ceux qui visitent votre application plus de deux fois par semaine. Cibler les utilisateurs pour ces segments essentiels augmente la probabilité que les utilisateurs s’abonnent et activent les notifications push.

## Étape 6 : Événements de conversion

Braze suggère des paramètres par défaut pour les conversions, mais vous voudrez peut-être configurer des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) autour des amorces push.

