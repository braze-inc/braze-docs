---
nav_title: Messages in-app push primer
article_title: Push Primer Messages in-app
page_order: 1
page_type: reference
description: "Cet article couvre les prérequis pour les messages in-app de l'amorce push et la manière de les configurer."
channel: push

---

# Messages in-app push primer

Message in-app pour l'application de diffusion en continu. La notification indique "Recevoir des notifications push de Movie Cannon ? Les notifications peuvent concerner de nouveaux films, des émissions de télévision ou d'autres avis et peuvent être désactivées à tout moment".]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Vous n'avez qu'une seule chance de demander aux utilisateurs l'autorisation de pousser, il est donc crucial d'optimiser votre enregistrement de poussée pour maximiser la portée de vos messages de poussée. Pour y parvenir, vous pouvez utiliser des messages in-app pour expliquer le type de messages que vos utilisateurs peuvent s'attendre à recevoir s'ils choisissent l'abonnement, avant de leur montrer la demande d'abonnement native. C'est ce que l'on appelle une amorce de poussée.

Pour créer un message in-app d'amorce de push dans Braze, vous pouvez utiliser le comportement on-click du bouton "Demander l'autorisation de push" lors de la création d'un message in-app pour iOS, Android ou Web.

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

- L'invite push ne peut être affichée qu'une seule fois par installation, ce qui est imposé par le système d'exploitation.
- L'invite ne s'affichera pas si le paramètre "push" de l'application est explicitement activé ou désactivé ; elle ne s'affichera que pour les utilisateurs disposant d'une [autorisation provisoire](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **Le paramètre "push" de l'application est activé :** Braze n'affichera pas le message in-app, car l'utilisateur a déjà opté pour l'abonnement.
  - **Le paramètre de poussée de l'application est désactivé :** Vous devrez rediriger l'utilisateur vers les paramètres de notification push de votre application dans les paramètres de l'appareil.

### Suppression manuelle du code

Le message in-app que vous avez configuré à l'aide de ce tutoriel appellera automatiquement le code d'invite push natif lorsqu'un utilisateur cliquera sur le bouton du message in-app. Pour éviter de demander l'autorisation de notification push deux fois, ou au mauvais moment, un développeur doit modifier toute intégration de notification push existante qu'il a mise en œuvre pour s'assurer que votre message in-app est la première amorce de notification push que vos utilisateurs voient.

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

## Étape 1 : Créer un message in-app

Tout d'abord, [créez un message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), puis sélectionnez votre type de message et sa mise en page.

Pour vous assurer que vous disposez de suffisamment d'espace pour votre message et vos boutons, utilisez une fenêtre modale/boîte de dialogue modale ou plein écran. Si vous choisissez le plein écran, notez qu'une image est nécessaire.

## Étape 2 : Créez votre message

Il est maintenant temps d'ajouter votre copie ! N'oubliez pas qu'un amorçage de push est censé inciter l'utilisateur à activer les notifications push. Dans le corps de votre message, nous vous suggérons de mettre en évidence les raisons pour lesquelles vos utilisateurs devraient activer les notifications push. Soyez précis quant au type de notifications que vous souhaitez envoyer et à la valeur qu'elles peuvent apporter.

Par exemple, une application d'actualités peut utiliser l'amorce de poussée suivante :

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Alors qu'une application de diffusion en continu peut utiliser les éléments suivants :

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Pour connaître les meilleures pratiques et obtenir des ressources supplémentaires, reportez-vous à la section [Créer des demandes d'abonnement personnalisées]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Étape 3 : Spécifiez le comportement des boutons {#button-actions}

Pour ajouter des boutons à votre message in-app, faites glisser deux blocs **Bouton** dans votre message, qui feront office de boutons principal et secondaire dans votre message in-app. Vous pouvez également faire glisser une rangée dans votre message, puis faire glisser les boutons dans la rangée, de manière à ce que les boutons se trouvent sur la même rangée horizontale (et non pas empilés les uns sur les autres). Nous recommandons d'utiliser les boutons "Autoriser les notifications" et "Pas maintenant" comme boutons de démarrage, mais il existe de nombreuses invites différentes que vous pouvez assigner à ces boutons.

Après avoir ajouté la copie des boutons, spécifiez le comportement au clic pour chaque bouton :

- **Bouton 1 :** Réglez ce paramètre sur "Fermer le message". Il s'agit de votre bouton secondaire, ou de l'option "Pas maintenant".
- **Bouton 2 :** Réglez ce paramètre sur "Demander l'autorisation de pousser". Il s'agit de votre bouton principal, ou de l'option "Autoriser les notifications".

Composez votre message in-app à l'aide de deux boutons : "Autoriser les notifications" et "Pas maintenant".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Étape 4 : Planification de la réception/distribution

Pour que votre push primer soit envoyé à un moment pertinent, vous devez planifier votre message in-app en tant que message basé sur une action avec **Perform Custom Event** comme action déclencheur.

Bien que le moment idéal varie, Braze suggère d'attendre qu'un utilisateur effectue une [action à forte valeur ajoutée](https://www.braze.com/resources/videos/mapping-high-value-actions), ce qui indique qu'il commence à voir la valeur de votre application ou de votre site, ou qu'il existe un besoin impérieux auquel les notifications push peuvent répondre (par exemple, après qu'il a passé une commande et que vous souhaitez lui offrir des informations sur le suivi de l'expédition). De cette façon, l'invite est bénéfique pour le client et non seulement pour votre marque.

\![Paramètres de réception/distribution par événement à envoyer aux utilisateurs qui ont effectué l'événement personnalisé "Ajouter à la liste de surveillance".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Étape 5 : Utilisateurs ciblés

L'objectif d'une campagne d'amorçage push est d'inviter les utilisateurs sur tout appareil sur lequel ils n'ont pas encore accordé de permissions push. Il peut s'agir de nouveaux utilisateurs ou d'utilisateurs existants qui obtiennent un nouvel appareil ou réinstallent votre application. Pour cibler correctement votre campagne de push primer, ajoutez un filtre où `Foreground Push Enabled For App is false`. Ce filtre identifie les installations d'apps individuelles qui n'ont pas encore opté pour les notifications push au premier plan.

{% alert important %}
L'utilisation d'un filtre au niveau de l'utilisateur comme `Push Subscription Status is not Opted In` exclura les utilisateurs qui sont déjà abonnés sur un autre appareil, ce qui les empêchera de recevoir la demande d'abonnement sur leur nouvel appareil.
{% endalert %}

Au-delà, vous pouvez décider des segmentations supplémentaires qui vous semblent les plus appropriées. Par exemple, vous pouvez cibler les utilisateurs qui ont effectué un deuxième achat, les utilisateurs qui viennent de créer un compte pour devenir membre, ou même les utilisateurs qui visitent votre appli plus de deux fois par semaine. Le ciblage des utilisateurs pour ces segments cruciaux augmente la probabilité que les utilisateurs s'abonnent et deviennent compatibles avec le push.

## Étape 6 : Événements de conversion

Braze propose des paramètres par défaut pour les conversions, mais vous pouvez souhaiter mettre en place des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) entourant les amorces de poussée.

