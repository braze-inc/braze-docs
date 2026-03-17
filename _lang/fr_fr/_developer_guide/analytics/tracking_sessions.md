---
nav_title: Suivre les sessions
article_title: Suivez les sessions grâce au SDK Braze.
page_order: 3.3
description: "Apprenez à suivre les sessions à l'aide du SDK de Braze."

---

# Suivre les sessions

> Apprenez à suivre les sessions à l'aide du SDK de Braze.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Définition de l'inactivité

Il est essentiel de comprendre comment l'inactivité est définie et mesurée pour gérer efficacement les cycles de vie des sessions dans le SDK Web. L'inactivité désigne une période pendant laquelle le SDK Web Braze ne détecte aucun événement suivi de la part de l'utilisateur.

### Comment l'inactivité est-elle évaluée ?

Le SDK Web surveille l'inactivité en fonction [des événements suivis par le SDK]({{site.baseurl}}/user_guide/data/activation/custom_data/events/#events). Le SDK gère un minuteur interne qui se réinitialise à chaque fois qu'un événement suivi est envoyé. Si aucun événement suivi par le SDK ne se produit pendant la période d'expiration configurée, la session est considérée comme inactive et prend fin.

Pour plus d'informations sur la manière dont le cycle de vie des sessions est implémenté dans le SDK Web, veuillez consulter le code source de gestion des sessions dans le [référentiel GitHub du SDK Web Braze](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts).

**Ce qui est considéré comme une activité par défaut :**
- Ouverture ou actualisation de l'application Web
- Interagir avec les éléments de l'interface utilisateur générés par Braze (tels que [les messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/) ou [les cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/))
- Appel de méthodes SDK qui envoient des événements suivis (tels que [des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/) ou [des mises à jour d'attributs utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/))

**Ce qui n'est pas considéré comme une activité par défaut :**
- Passer à un autre onglet du navigateur
- Réduire la fenêtre du navigateur
- Événements de mise au point ou de flou du navigateur
- Défilement ou mouvements de la souris sur la page

{% alert note %}
Le SDK Web ne suit pas automatiquement les changements de visibilité du navigateur web, les changements d'onglet ou la focalisation de l'utilisateur. Cependant, il est possible de suivre ces interactions au niveau du navigateur en implémentant des écouteurs d'événements personnalisés à l'aide de l'[API Page Visibility](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) du navigateur et en envoyant [des custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web) à Braze. Pour un exemple de mise en œuvre, veuillez vous référer à [Suivi de l'inactivité personnalisée](#tracking-custom-inactivity).
{% endalert %}

### Configuration du délai d'expiration de la session

Par défaut, le SDK Web considère qu'une session est inactive après 30 minutes sans aucun événement suivi. Vous pouvez rendre ce seuil personnalisé lors de l'initialisation du SDK à l'aide du`sessionTimeoutInSeconds`paramètre. Pour plus de détails sur la configuration de ce paramètre, y compris des exemples de code, veuillez consulter [la section Modification du délai d'expiration par défaut de la session](#changing-the-default-session-timeout).

### Exemple : Comprendre les scénarios d'inactivité

Considérez le scénario suivant :

1. Un utilisateur accède à votre site Web et le SDK démarre une session en appelant [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession).
2. L'utilisateur passe à un autre onglet du navigateur pour consulter un autre site web pendant 30 minutes.
3. Pendant cette période, aucun événement suivi par le SDK ne se produit sur votre site Web.
4. Après 30 minutes d'inactivité, la session prendra automatiquement fin.
5. Lorsque l'utilisateur revient à l'onglet de votre site Web et déclenche un événement SDK (tel que la consultation d'une page ou l'interaction avec du contenu), une nouvelle session commence.

### Suivi de l'inactivité personnalisée

Si vous avez besoin de suivre l'inactivité en fonction de la visibilité du navigateur ou du changement d'onglet, veuillez implémenter des écouteurs d'événements personnalisés dans votre code JavaScript. Veuillez utiliser les événements du navigateur tels que`visibilitychange`pour détecter le moment où les utilisateurs quittent votre page, et envoyez manuellement [des custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/) à Braze ou appelez[`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession)lorsque cela est approprié.

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

Pour plus d'informations sur la journalisation des événements personnalisés, veuillez vous référer à [la section Journalisation des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/). Pour plus d'informations sur le cycle de vie des sessions et la configuration des délais d'expiration, veuillez vous référer à [la section Modification du délai d'expiration par défaut des sessions](#change-session-timeout).

## S’abonner aux mises à jour de session

### Étape 1 : S'abonner aux mises à jour

Pour s'abonner aux mises à jour de la session, utilisez la méthode `subscribeToSessionUpdates()`.

{% tabs %}
{% tab web %}
Pour l'instant, s'abonner aux mises à jour de session n'est pas pris en charge pour le SDK Web Braze.
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
Si vous enregistrez un rappel de fin de session, il se déclenche lorsque l'application revient au premier plan. La durée de la session est mesurée entre le moment où l'application s'ouvre (en avant-plan) et le moment où elle se ferme (en arrière-plan).

{% subtabs %}
{% subtab swift %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

Pour s'abonner à un flux asynchrone, vous pouvez utiliser [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) à la place.

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
Le SDK React native ne fournit pas de méthode permettant de s'abonner directement aux mises à jour de session. Le cycle de vie de la session est géré par le SDK natif sous-jacent. Par conséquent, pour vous abonner aux mises à jour, veuillez utiliser l'approche native de la plateforme pour l'onglet **Android** ou **Swift**.
{% endtab %}
{% endtabs %}

### Étape 2 : Suivi de la session de test (optionnel)

Pour tester le suivi des sessions, démarrez une session sur votre appareil, puis ouvrez le tableau de bord de Braze et recherchez l'utilisateur concerné. Dans son profil utilisateur, sélectionnez **Aperçu des sessions.** Si les indicateurs se mettent à jour comme prévu, le suivi de session fonctionne correctement.

![La section « Aperçu des sessions » d'un profil utilisateur affiche le nombre de sessions, la date de la dernière utilisation et la date de la première utilisation.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
Les détails spécifiques aux applications ne sont affichés que pour les utilisateurs qui ont utilisé plus d'une application.
{% endalert %}

## Modifier le délai de session par défaut {#change-session-timeout}

Vous pouvez modifier le délai qui s'écoule avant qu'une session ne se termine automatiquement.

{% tabs %}
{% tab web %}
Par défaut, le délai d'expiration de la session est fixé à `30` minutes. Pour changer cela, passez l'option `sessionTimeoutInSeconds` à votre fonction [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) fonction. Il peut être défini comme tout nombre entier supérieur ou égal à `1`. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
Par défaut, le délai d'attente de la session est fixé à `10` secondes. Pour modifier cela, ouvrez votre fichier `braze.xml` et ajoutez le paramètre `com_braze_session_timeout`. Il peut être défini comme tout nombre entier supérieur ou égal à `1`.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
Par défaut, le délai d'attente de la session est fixé à `10` secondes. Pour modifier cela, définissez `sessionTimeout` dans l'objet `configuration` qui est transmis à [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). Il peut être défini comme tout nombre entier supérieur ou égal à `1`.

{% subtabs %}
{% subtab swift %}
```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
Le SDK React native s'appuie sur les SDK natifs pour gérer les sessions. Pour modifier le délai d'expiration de session par défaut, veuillez le configurer dans la couche native :

- **Android :** Veuillez définir`com_braze_session_timeout`dans votre`braze.xml`fichier. Pour plus de détails, veuillez sélectionner l'onglet **Android**.
- **iOS :** Veuillez définir`sessionTimeout`sur votre`Braze.Configuration`objet. Pour plus de détails, veuillez sélectionner l'onglet **Swift**.
{% endtab %}
{% endtabs %}

{% alert note %}
Si vous définissez un délai de session, toute la sémantique de la session s'étendra automatiquement jusqu'au délai défini.
{% endalert %}
