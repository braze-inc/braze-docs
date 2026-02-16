---
nav_title: Messages in-app d’amorce de notification push
article_title: Messages in-app d’amorce de notification push
page_order: 1
page_type: reference
description: "Cet article couvre les conditions préalables pour les messages in-app d’amorce de notification push et la manière de les configurer."
channel: push

---

# Messages in-app d’amorce de notification push

![Messages in-app d’amorce de notification push pour une application de streaming. La notification affiche « Get push notifications from Movie Cannon? (Voulez-vous recevoir des notifications push de Movie Cannon ?) Les notifications peuvent inclure de nouveaux films, émissions télévisées ou autres avis et peuvent être désactivées à tout moment ».]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

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
- L'invite ne s'affiche pas si le paramètre "push" de l'application est explicitement activé ou désactivé. Elle ne s'affiche que pour les utilisateurs disposant d'une [autorisation provisoire](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **Le paramètre "push" de l'application est activé :** Braze n'affiche pas le message in-app, car l'utilisateur a déjà opté pour l'abonnement.
  - **Le paramètre de poussée de l'application est désactivé :** Vous devez rediriger l'utilisateur vers les paramètres de notification push de votre application dans les paramètres de l'appareil.

### Enlever manuellement le code

Le message in-app que vous avez configuré à l'aide de ce tutoriel appelle automatiquement le code d'invite push natif lorsqu'un utilisateur clique sur le bouton du message in-app. Pour éviter de demander une autorisation de notification push deux fois ou au mauvais moment, les développeurs doivent modifier toute intégration de notification push existante qu’ils ont mise en œuvre afin de s’assurer que votre message in-app est la première amorce de notification push que vos utilisateurs verront.

Votre équipe de développement doit examiner votre mise en œuvre des notifications push pour votre app ou votre site et supprimer manuellement tout code qui demande une autorisation push. Par exemple, supprimez les références au code suivant :

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

## Étape 2 : Créer votre message

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

## Étape 3 : Spécifier le comportement du bouton {#button-actions}

Pour ajouter des boutons à votre message in-app, faites glisser deux blocs **Bouton** dans votre message, qui font office de boutons principal et secondaire dans votre message in-app. Vous pouvez également faire glisser une rangée dans votre message, puis faire glisser les boutons dans la rangée, de manière à ce que les boutons se trouvent sur la même rangée horizontale (et non pas empilés les uns sur les autres). Nous vous recommandons d'utiliser les boutons "Autoriser les notifications" et "Pas maintenant" comme boutons de démarrage, mais vous pouvez assigner de nombreuses invites différentes aux boutons.

Après avoir ajouté la copie du bouton, spécifiez le comportement en cas de clic pour chaque bouton :

- **Bouton 1:** Définissez celui-ci sur « Close Message » (Fermer le message). Il s’agit de votre bouton secondaire ou de l’option « Not now » (Pas maintenant).
- **Bouton 2 :** Définissez cette option sur « Request Push Permission » (Demander l’autorisation de notification push). Il s’agit du bouton principal ou de l’option « Allow notifications » (Autoriser les notifications).

![Compositeur de messages in-app avec deux boutons : "Autoriser les notifications" et "Pas maintenant".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Étape 4 : Planifier la livraison

Pour définir votre amorce push pour l'envoyer à un moment pertinent, vous devez programmer votre message intégré à l'application comme un message basé sur une action avec **Effectuer un événement personnalisé** comme action déclencheuse.

Bien que le moment idéal puisse varier, Braze suggère d'attendre qu'un utilisateur effectue une sorte de [action de grande valeur](https://www.braze.com/resources/videos/mapping-high-value-actions), indiquant qu'il commence à voir la valeur de votre application ou site, ou lorsqu'il y a un besoin impérieux que les notifications push peuvent répondre (comme après qu'ils aient passé une commande et que vous souhaitiez leur offrir des informations de suivi d'expédition). De cette façon, l’invite représente un avantage pour le client plutôt que pour votre marque.

![Paramètres de réception/distribution par événement à envoyer aux utilisateurs qui ont effectué l'événement personnalisé "Ajouter à la liste de surveillance".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Étape 5 : Utilisateurs cibles

L'objectif d'une campagne d'amorçage push est d'inviter les utilisateurs sur tout appareil sur lequel ils n'ont pas encore accordé de permissions push. Il peut s'agir de nouveaux utilisateurs ou d'utilisateurs existants qui obtiennent un nouvel appareil ou réinstallent votre application.

{% alert important %}
**Suppression automatique avec amorce de poussée sans code :** Si vous utilisez l'amorce de push sans code (l'action du bouton "Request Push Permission"), vous n'avez pas besoin d'ajouter des filtres d'abonnement au push à votre segmentation. Le SDK supprime automatiquement le message in-app sur les appareils qui ont déjà un jeton push actif, quel que soit le statut push de l'utilisateur sur les autres appareils. Pour plus d'informations sur le ciblage des utilisateurs disposant de plusieurs appareils, voir [Ciblage des utilisateurs disposant de plusieurs appareils](#targeting-users-with-multiple-devices).
{% endalert %}

Si vous n'utilisez pas l'amorce de poussée sans code, ajoutez un filtre à l'endroit où `Foreground Push Enabled For App is false`. Ce filtre identifie les installations d'apps individuelles qui n'ont pas encore opté pour les notifications push au premier plan.

{% alert important %}
L'utilisation d'un filtre au niveau de l'utilisateur tel que `Push Subscription Status is not Opted In` exclut les utilisateurs qui sont déjà abonnés sur un autre appareil, ce qui les empêche de recevoir la demande d'abonnement sur leur nouvel appareil.
{% endalert %}

Au-delà de cela, vous pouvez décider des segments supplémentaires qui vous semblent les plus appropriés. Par exemple, vous pouvez cibler les utilisateurs qui ont effectué un deuxième achat, les utilisateurs qui viennent de créer un compte pour devenir membre ou même ceux qui visitent votre application plus de deux fois par semaine. Cibler les utilisateurs pour ces segments essentiels augmente la probabilité que les utilisateurs s’abonnent et activent les notifications push.

### Ciblage des utilisateurs avec plusieurs appareils

Comme Braze saisit les données des utilisateurs au niveau du profil et non de l'appareil, le ciblage des utilisateurs qui possèdent plusieurs appareils peut s'avérer difficile. Les filtres d'abonnement en mode push dans la segmentation incluent ou excluent les utilisateurs en fonction de l'état de l'abonnement d'un seul appareil plutôt que de l'état de l'abonnement de l'appareil spécifique ciblé. En outre, les états provisoires sur iOS ajoutent de la complexité, car ces appareils disposent techniquement de jetons de poussée au premier plan, mais les utilisateurs ne sont pas explicitement abonnés.

#### Le problème des filtres d'abonnement push

Lorsqu'un utilisateur possède plusieurs appareils avec différents états d'abonnement push, les filtres d'abonnement push de votre segmentation peuvent ne pas cibler certains appareils. Envisagez les scénarios suivants :

{% details Scenario 1: User has two devices on different platforms %}

**L'utilisateur dispose de deux appareils :**
- Appareil A : Android, a opté pour le push
- Appareil B : iOS, pas d'abonnement au push

**Segmenter les filtres qui ne fonctionnent pas :**
- `Push enabled = false` - L'utilisateur a activé la fonction push sur son appareil Android, il n'entre donc pas dans le segment. Le segment ne comprend pas l'appareil iOS.
- `Push subscription status is not opted in` - L'utilisateur a activé la fonction push sur son appareil Android, il n'entre donc pas dans le segment. Le segment ne comprend pas l'appareil iOS.

**Des filtres de segmentation qui fonctionnent :**
- `Push enabled for iOS = false` - L'utilisateur a activé le push sur son appareil Android, mais nous ne ciblons que les appareils iOS, donc l'utilisateur tombe dans le segmentation. Le segment comprend l'appareil iOS.

{% enddetails %}

{% details Scenario 2: User has two iOS devices with different states %}

**L'utilisateur possède deux appareils iOS :**
- Appareil A : Abonné à la poussée
- Appareil B : Autorisé provisoirement mais non abonné

**Segmenter les filtres qui ne fonctionnent pas :**
- `Push enabled = false` - L'appareil A est abonné à la poussée, de sorte que l'utilisateur ne tombe pas dans le segment. Le segment n'inclut pas l'appareil B.
- `Provisionally opted in = true` - L'appareil A est pleinement abonné, ce qui signifie qu'il n'est pas dans un état provisoire. L'utilisateur ne tombe pas dans le segmentation. Le segment n'inclut pas l'appareil B.
- `Push enabled for app > iOS = false` - L'appareil A fait l'objet d'un abonnement au push sur iOS, de sorte que l'utilisateur ne tombe pas dans le segment. Le segment n'inclut pas l'appareil B.
- `Push subscription status is not opted in` - L'appareil A est abonné à la poussée, de sorte que l'utilisateur ne tombe pas dans le segment. Le segment n'inclut pas l'appareil B.

**Résultat :** L'utilisation de n'importe quelle combinaison de ces filtres push a pour effet d'exclure au moins un appareil du segment.

{% enddetails %}

{% details Scenario 3: User has three or more devices on the same OS %}

**L'utilisateur dispose de trois appareils :**
- Appareil A : Abonné à la poussée
- Appareil B : Pas d'abonnement à la poussée
- Appareil C : Pas d'abonnement à la poussée

**Segmenter les filtres qui ne fonctionnent pas :**
- `Push enabled = false` - L'appareil A est abonné à la poussée, de sorte que l'utilisateur ne tombe pas dans le segment. Le segment ne comprend pas les appareils B et C.
- `Push enabled for app > X = false` - L'appareil A fait l'objet d'un abonnement pour pousser sur l'application spécifiée, de sorte que l'utilisateur ne tombe pas dans le segment. Le segment ne comprend pas les appareils B et C.
- `Push subscription status is not opted in` - L'appareil A est abonné à la poussée, de sorte que l'utilisateur ne tombe pas dans le segment. Le segment ne comprend pas les appareils B et C.

**Résultat :** L'utilisation de n'importe quelle combinaison de ces filtres push laisse au moins un appareil non ciblé.

{% enddetails %}

#### Solution : Utilisez l'amorce de poussée sans code

La solution recommandée est d'utiliser l'amorce de push sans code (l'action du bouton d'appel "Request Push Permission") sans filtre supplémentaire de segmentation de l'état du push.

{% alert important %}
**Suppression automatique**: L'amorce de push sans code est automatiquement supprimée sur les appareils qui ont déjà un jeton de push actif. Le SDK vérifie si un utilisateur sur son appareil spécifique dispose déjà d'un jeton push. Si le SDK constate que l'utilisateur a déjà opté pour l'abonnement (par exemple, à partir d'une demande précédente ou via les paramètres de l'appareil), il supprime automatiquement le message in-app sans qu'il soit nécessaire d'utiliser des filtres de segmentation supplémentaires. L'amorce apparaît dans tous les autres scénarios, y compris si un utilisateur est provisoirement abonné à Push.
{% endalert %}

L'avantage de l'utilisation de l'amorce de poussée sans code est que la fonctionnalité est prise en charge par le SDK de Braze. Comme le SDK peut détecter l'état du jeton push sur l'appareil spécifique qui affiche le message, vous n'avez pas besoin de vous appuyer sur des filtres de segmentation au niveau du profil qui risquent d'exclure les utilisateurs possédant plusieurs appareils.

#### Considérations

**Aucune amorce de code n'est nécessaire :** Vous devez utiliser l'amorce de poussée sans code pour que la suppression automatique fonctionne. Si vous mettez en place une logique personnalisée ou des liens profonds au lieu d'utiliser l'action du bouton "Request Push Permission", le SDK ne peut pas identifier que vous essayez d'afficher un bouton d'action push. Le message s'affiche alors quel que soit l'état de l'abonnement de l'appareil.

**Suppression pour les utilisateurs qui se sont abonnés**: Vous pouvez vouloir supprimer le message in-app pour les utilisateurs qui ont explicitement refusé le push (par exemple, à partir de la demande native ou des paramètres de l'appareil) et recibler ces utilisateurs avec une campagne de maturation distincte. Pour ce faire, utilisez la logique liquide suivante en combinaison avec l'amorce d'absence de code :

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %} 
{% abort_message('user turned off push notifications') %} 
{% endif %}
- message goes here -
```
{% endraw %}

Le filtre `targeted_device` Liquid ne tient compte que de l'appareil sur lequel le message est affiché, et non du profil utilisateur. Sur cet appareil, `foreground_push_enabled` est défini sur `true` lorsqu'il y a un jeton push actif au premier plan et défini sur `false` lorsque le système d'exploitation signale que les notifications push ont été désactivées (par exemple, l'utilisateur les a explicitement désactivées). Pour les appareils entièrement nouveaux qui n'ont pas encore répondu à un état d'autorisation push, `foreground_push_enabled` n'est pas défini et n'a aucune valeur. Parce que la condition Liquid vérifie spécifiquement `{% raw %}``false`{% endraw %}, elle supprime l'amorce uniquement pour les appareils ayant un abonnement explicite, tandis que les appareils dans cet état inconnu sont toujours admissibles et peuvent recevoir l'amorce de poussée.

## Étape 6 : Événements de conversion

Braze suggère des paramètres par défaut pour les conversions, mais vous voudrez peut-être configurer des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) autour des amorces push.