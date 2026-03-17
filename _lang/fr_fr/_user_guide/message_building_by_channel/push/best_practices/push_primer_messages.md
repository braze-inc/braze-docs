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
- L'invite ne s'affiche pas si le paramètre push de l'application est explicitement activé ou désactivé. Il s'affiche uniquement pour les utilisateurs disposant [d'une autorisation provisoire](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **Le paramètre "push" de l'application est activé :** Braze n'affiche pas le message in-app, car l'utilisateur a déjà effectué l'abonnement.
  - **Le paramètre de poussée de l'application est désactivé :** Il est nécessaire de rediriger l'utilisateur vers les paramètres de notification push de votre application dans les paramètres de l'appareil.

### Enlever manuellement le code

Le message in-app que vous avez configuré à l'aide de ce tutoriel appelle automatiquement le code natif de notification push lorsqu'un utilisateur clique sur le bouton du message in-app. Pour éviter de demander une autorisation de notification push deux fois ou au mauvais moment, les développeurs doivent modifier toute intégration de notification push existante qu’ils ont mise en œuvre afin de s’assurer que votre message in-app est la première amorce de notification push que vos utilisateurs verront.

Votre équipe de développement est priée de vérifier la mise en œuvre des notifications push pour votre application ou votre site et de supprimer manuellement tout code demandant l'autorisation d'envoyer des notifications push. Par exemple, veuillez supprimer les références au code suivant :

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

Pour ajouter des boutons à votre message in-app, veuillez glisser deux blocs **Bouton** dans votre message. Ceux-ci serviront de boutons principal et secondaire dans votre message in-app. Vous pouvez également faire glisser une rangée dans votre message, puis faire glisser les boutons dans la rangée, de manière à ce que les boutons se trouvent sur la même rangée horizontale (et non pas empilés les uns sur les autres). Nous recommandons « Autoriser les notifications » et « Pas maintenant » comme boutons de démarrage, mais vous pouvez attribuer de nombreux autres messages aux boutons.

Après avoir ajouté la copie du bouton, spécifiez le comportement en cas de clic pour chaque bouton :

- **Bouton 1:** Définissez celui-ci sur « Close Message » (Fermer le message). Il s’agit de votre bouton secondaire ou de l’option « Not now » (Pas maintenant).
- **Bouton 2 :** Définissez cette option sur « Request Push Permission » (Demander l’autorisation de notification push). Il s’agit du bouton principal ou de l’option « Allow notifications » (Autoriser les notifications).

![Compositeur de messages in-app avec deux boutons : « Autoriser les notifications » et « Pas maintenant ».]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Étape 4 : Planifier la livraison

Pour définir votre amorce push pour l'envoyer à un moment pertinent, vous devez programmer votre message intégré à l'application comme un message basé sur une action avec **Effectuer un événement personnalisé** comme action déclencheuse.

Bien que le moment idéal puisse varier, Braze suggère d'attendre qu'un utilisateur effectue une sorte de [action de grande valeur](https://www.braze.com/resources/videos/mapping-high-value-actions), indiquant qu'il commence à voir la valeur de votre application ou site, ou lorsqu'il y a un besoin impérieux que les notifications push peuvent répondre (comme après qu'ils aient passé une commande et que vous souhaitiez leur offrir des informations de suivi d'expédition). De cette façon, l’invite représente un avantage pour le client plutôt que pour votre marque.

![Livraison par événement pour les utilisateurs qui ont effectué l'événement personnalisé « Ajouter à la liste de surveillance ».]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Étape 5 : Utilisateurs cibles

L'objectif d'une campagne de promotion des notifications push est d'inciter les utilisateurs à accorder les autorisations de notifications push sur tous les appareils où ils ne l'ont pas encore fait. Cela peut inclure les nouveaux utilisateurs ou les utilisateurs existants qui acquièrent un nouvel appareil ou réinstallent votre application.

{% alert important %}
**Suppression automatique avec amorce push sans code** : Si vous utilisez l'outil Push Primer sans code (l'action du bouton « Demander l'autorisation Push »), il n'est pas nécessaire d'ajouter des filtres d'abonnement Push à votre segmentation. Le SDK supprime automatiquement le message in-app sur les appareils qui disposent déjà d'un jeton push actif, quel que soit le statut push de l'utilisateur sur d'autres appareils. Pour plus d'informations sur le ciblage des utilisateurs possédant plusieurs appareils, veuillez consulter [la section Ciblage des utilisateurs possédant plusieurs appareils](#targeting-users-with-multiple-devices).
{% endalert %}

Si vous n'utilisez pas le guide d'introduction sans code, veuillez ajouter un filtre où `Foreground Push Enabled For App is false`. Ce filtre identifie les installations d'applications individuelles qui n'ont pas encore souscrit à l'abonnement pour les notifications push en avant-plan.

{% alert important %}
L'utilisation d'un filtre au niveau de l'utilisateur tel que`Push Subscription Status is not Opted In`exclut les utilisateurs qui ont déjà souscrit à un abonnement sur un autre appareil, les empêchant ainsi de recevoir la demande d'abonnement sur leur nouvel appareil.
{% endalert %}

Au-delà de cela, vous pouvez décider des segments supplémentaires qui vous semblent les plus appropriés. Par exemple, vous pouvez cibler les utilisateurs qui ont effectué un deuxième achat, les utilisateurs qui viennent de créer un compte pour devenir membre ou même ceux qui visitent votre application plus de deux fois par semaine. Cibler les utilisateurs pour ces segments essentiels augmente la probabilité que les utilisateurs s’abonnent et activent les notifications push.

### Ciblage des utilisateurs possédant plusieurs appareils

Étant donné que Braze collecte les données utilisateur au niveau du profil plutôt qu'au niveau de l'appareil, le ciblage des utilisateurs qui possèdent plusieurs appareils peut s'avérer difficile. Les filtres d'abonnement push dans la segmentation incluent ou excluent les utilisateurs en fonction de l'état d'abonnement d'un seul appareil plutôt que de l'état d'abonnement de l'appareil ciblé spécifique. De plus, les états provisoires sur iOS ajoutent à la complexité, car ces appareils disposent techniquement de jetons push en avant-plan, mais les utilisateurs n'ont pas de contrat d'abonnement.

#### Le problème avec les filtres d'abonnement push

Lorsqu'un utilisateur possède plusieurs appareils avec différents états d'abonnement aux notifications push, les filtres d'abonnement aux notifications push de votre segmentation peuvent ne pas cibler certains appareils. Veuillez considérer les scénarios suivants :

{% details Scenario 1: User has two devices on different platforms %}

**L'utilisateur dispose de deux appareils :**
- Appareil A : Android, abonnement pour les notifications push
- Appareil B : iOS, pas d'abonnement au service de notification push

**Filtres de segment qui ne fonctionnent pas :**
- `Push enabled = false` - L'utilisateur a activé la fonction push sur son appareil Android, il n'est donc pas inclus dans le segment. Ce segment n'inclut pas les appareils iOS.
- `Push subscription status is not opted in` - L'utilisateur a activé la fonction push sur son appareil Android, il n'est donc pas inclus dans le segment. Ce segment n'inclut pas les appareils iOS.

**Filtres de segment efficaces :**
- `Push enabled for iOS = false` - L'utilisateur a activé la fonction push sur son appareil Android, mais le ciblage se fait uniquement sur les appareils iOS, donc l'utilisateur fait partie du segment. Ce segment inclut les appareils iOS.

{% enddetails %}

{% details Scenario 2: User has two iOS devices with different states %}

**L'utilisateur dispose de deux appareils iOS :**
- Appareil A : A fait un abonnement pour recevoir des notifications push
- Appareil B : Activé provisoirement, mais sans abonnement

**Filtres de segment qui ne fonctionnent pas :**
- `Push enabled = false` - L'appareil A a un abonnement pour la diffusion, donc l'utilisateur n'est pas inclus dans le segment. Le segment n'inclut pas l'appareil B.
- `Provisionally opted in = true` - L'appareil A a un abonnement complet, ce qui signifie qu'il n'est pas dans un état provisoire. L'utilisateur n'appartient pas à ce segment. Le segment n'inclut pas l'appareil B.
- `Push enabled for app > iOS = false` - L'appareil A a un abonnement pour envoyer des notifications push sur iOS, donc l'utilisateur n'est pas inclus dans le segment. Le segment n'inclut pas l'appareil B.
- `Push subscription status is not opted in` - L'appareil A a un abonnement pour la diffusion, donc l'utilisateur n'est pas inclus dans le segment. Le segment n'inclut pas l'appareil B.

**Résultat :** L'utilisation de n'importe quelle combinaison de ces filtres push entraîne l'exclusion d'au moins un appareil du segment.

{% enddetails %}

{% details Scenario 3: User has three or more devices on the same OS %}

**L'utilisateur dispose de trois appareils :**
- Appareil A : A fait un abonnement pour recevoir des notifications push
- Appareil B : Non en possession d'un abonnement au service Push
- Appareil C : Non en possession d'un abonnement au service Push

**Filtres de segment qui ne fonctionnent pas :**
- `Push enabled = false` - L'appareil A a un abonnement pour la diffusion, donc l'utilisateur n'est pas inclus dans le segment. Le segment n'inclut pas les appareils B et C.
- `Push enabled for app > X = false` - L'appareil A a un abonnement pour envoyer des notifications push sur l'application spécifiée, de sorte que l'utilisateur n'est pas inclus dans le segment. Le segment n'inclut pas les appareils B et C.
- `Push subscription status is not opted in` - L'appareil A a un abonnement pour la diffusion, donc l'utilisateur n'est pas inclus dans le segment. Le segment n'inclut pas les appareils B et C.

**Résultat :** L'utilisation de n'importe quelle combinaison de ces filtres push laisse au moins un appareil non ciblé.

{% enddetails %}

#### Solution : Veuillez utiliser le guide d'introduction au push sans code.

La solution recommandée consiste à utiliser le déclencheur push sans code (l'action du bouton « Demander l'autorisation push ») sans filtres de segmentation d'état push supplémentaires.

{% alert important %}
**Suppression automatique** : Le programme d'initiation sans code supprime automatiquement les notifications push sur les appareils qui disposent déjà d'un jeton push actif. Le SDK vérifie si un utilisateur sur son appareil spécifique dispose déjà d'un jeton push. Si le SDK détecte que l'utilisateur a déjà donné son consentement (par exemple, lors d'une demande précédente ou via les paramètres de l'appareil), il supprime automatiquement le message in-app sans qu'il soit nécessaire d'utiliser des filtres de segmentation supplémentaires. Le guide présente tous les autres scénarios, y compris celui où un utilisateur a provisoirement souscrit à un abonnement pour recevoir des notifications push.
{% endalert %}

L'avantage d'utiliser le push primer sans code réside dans le fait que cette fonctionnalité est prise en charge par le SDK Braze. Étant donné que le SDK peut détecter l'état du jeton push sur l'appareil spécifique qui affiche le message, il n'est pas nécessaire de s'appuyer sur des filtres de segmentation au niveau du profil qui pourraient exclure les utilisateurs disposant de plusieurs appareils.

#### Considérations

**Aucune connaissance en programmation n'est requise** : Il est nécessaire d'utiliser le programme d'amorçage sans code pour que la suppression automatique fonctionne. Si vous configurez une logique personnalisée ou des liens profonds au lieu d'utiliser l'action du bouton « Demander l'autorisation de push », le SDK ne peut pas identifier que vous essayez d'afficher une notification push. Cela entraîne l'affichage du message, quel que soit l'état d'abonnement de cet appareil.

**Suppression pour les utilisateurs qui se sont désinscrits** : Il peut être souhaitable de supprimer le message in-app pour les utilisateurs qui ont explicitement choisi de ne pas recevoir de notifications push (par exemple, à partir de la demande native ou des paramètres de l'appareil) et de recibler ces utilisateurs avec une campagne de fidélisation distincte. Pour ce faire, veuillez utiliser la logique Liquid suivante en combinaison avec le guide d'introduction sans code :

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %} 
{% abort_message('user turned off push notifications') %} 
{% endif %}
- message goes here -
```
{% endraw %}

Le filtre`targeted_device` Liquid examine uniquement l'appareil sur lequel le message s'affiche, et non le profil utilisateur. Sur cet appareil,`foreground_push_enabled`  est défini sur`true`  lorsqu'il existe un jeton push actif en avant-plan et sur`false`  lorsque le système d'exploitation signale que les notifications push ont été désactivées (par exemple, si l'utilisateur les a explicitement désactivées). Pour les appareils entièrement nouveaux qui n'ont pas encore répondu à une autorisation push,`foreground_push_enabled`  n'est pas défini et n'a aucune valeur. Étant donné que la condition Liquid vérifie spécifiquement`{% raw %}``false`{% endraw %}, elle supprime l'amorce uniquement pour les appareils ayant explicitement choisi de ne pas participer, tandis que les appareils dans cet état inconnu restent éligibles et peuvent recevoir l'amorce push.

## Étape 6 : Événements de conversion

Braze suggère des paramètres par défaut pour les conversions, mais vous voudrez peut-être configurer des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) autour des amorces push.