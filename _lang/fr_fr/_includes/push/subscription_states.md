## Statuts d’abonnement aux notifications push {#push-sub-states}

Un "état d'abonnement push" dans Braze identifie la préférence globale d'un **utilisateur** quant à son souhait de recevoir des notifications push. Étant donné que le statut d’abonnement est basé sur l’utilisateur, il n’est pas spécifique à une application donnée. Les états de l’abonnement deviennent des indicateurs utiles lorsque vous décidez quels utilisateurs cibler avec les notifications push.

{% alert note %}
L’état de l’abonnement aux notifications push d’un utilisateur s’applique à l’ensemble de son profil utilisateur, ce qui inclut tous les appareils de celui-ci.
{% endalert %}

Les options d'état d'abonnement suivantes sont disponibles : `Subscribed`, `Opted-In`, et `Unsubscribed`.

Par défaut, pour que vos utilisateurs puissent recevoir vos messages via des notifications push, leur statut d'abonnement aux notifications push doit être défini`Subscribed`sur « activé » ou `Opted-In`« autorisé », et les notifications push en avant-plan doivent être activées. Vous pouvez écraser cette configuration si nécessaire lors de la rédaction d’un message.

|État autorisé|Description|
|---|---|
|`Subscribed`| État d’abonnement aux notifications push par défaut lorsqu’un profil utilisateur est créé dans Braze. |
|`Opted-In`| Un utilisateur a explicitement exprimé une préférence pour recevoir des notifications push. Braze modifie automatiquement le statut d'abonnement d'un utilisateur à « `Opted-In`opt-in » si l'utilisateur accepte une invite push au niveau du système d'exploitation.<br><br>Ceci ne s’applique pas aux utilisateurs d’Android 12 ou antérieur.|
|`Unsubscribed`| Un utilisateur s’est explicitement désabonné des notifications push par le biais de votre application ou d’autres méthodes fournies par votre marque. Par défaut, les campagnes push Braze ciblent uniquement les utilisateurs qui sont`Subscribed`autorisés`Opted-in`à recevoir des notifications push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze ne change pas automatiquement le statut de l’abonnement aux notifications push d’un utilisateur vers `Unsubscribed`. Veuillez noter que si l'état d'abonnement push d'un utilisateur est `Unsubscribed`, alors le filtre `Foreground Push Enabled`de l'utilisateur dans la segmentation est `false`.
{% endalert %}

### Mise à jour des états d’abonnement aux notifications push {#update-push-subscription-state}

Veuillez examiner les méthodes suivantes pour mettre à jour l'état d'abonnement push d'un utilisateur :

#### Abonnement automatique (par défaut)

Par défaut, Braze définit l'état de l'abonnement push d'un utilisateur sur `Opted-In` lorsqu'il autorise pour la première fois les notifications push pour votre application. Braze procède également de la sorte lorsqu'un utilisateur réactive les autorisations push dans les paramètres de son système après les avoir précédemment désactivées.

{% tabs local %}
{% tab android %}
Pour désactiver ce comportement par défaut, ajoutez la propriété suivante au fichier `braze.xml` de votre projet Android Studio :

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
À partir de la [version 7.5.0 du SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), vous pouvez désactiver ou personnaliser davantage ce comportement en ajoutant la configuration `optInWhenPushAuthorized` au fichier `AppDelegate.swift` de votre projet Xcode :

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### Intégration SDK

Vous pouvez mettre à jour l'état de l'abonnement d'un utilisateur avec le SDK de Braze à l'aide de la méthode `setPushNotificationSubscriptionType` sur le [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) ou [iOS.](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)) Par exemple, vous pouvez utiliser cette méthode pour créer une page de paramètres dans votre appli où les utilisateurs peuvent activer ou désactiver manuellement les notifications push.

#### API REST

Vous pouvez mettre à jour l'état de l'abonnement d'un utilisateur avec l'API REST de Braze en utilisant l' [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour l'attribut [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) attribut.

### Vérifier le statut de l’abonnement aux notifications push

![Profil utilisateur de John Doe dont l'état de l'abonnement push est défini sur Abonné.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Vous pouvez vérifier l'état de l'abonnement push d'un utilisateur avec Braze de l'une des manières suivantes :

* **Profil utilisateur :** Vous pouvez accéder aux profils utilisateurs individuels via le tableau de bord de Braze dans la rubrique **[Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** de Braze. Après avoir trouvé le profil d'un utilisateur (via l'adresse e-mail, le numéro de téléphone ou l'ID externe), vous pouvez sélectionner l'onglet **Engagement** pour afficher et ajuster manuellement l'état de l'abonnement d'un utilisateur.
* **Exportation de l'API REST :** Vous pouvez exporter des profils utilisateurs individuels au format JSON à l'aide des endpoints d'exportation [Utilisateurs par segmentation]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Braze renvoie un objet push tokens contenant les informations d'activation push par appareil.