---
page_order: 1.2
nav_title: Authentifizierung
article_title: Einrichten der Authentifizierung für das Braze SDK
description: "Dieser Referenzartikel die SDK-Authentifizierung und wie Sie dieses Feature im Braze SDK aktivieren können."
platform:
  - iOS
  - Android
  - Web
  
---

# SDK-Authentifizierung einrichten

> Mit der SDK-Authentifizierung können Sie SDK-Anfragen, die im Namen von angemeldeten Nutzern gestellt werden, einen (serverseitig generierten) kryptografischen Beweis liefern.

## Funktionsweise

Nachdem Sie dieses Feature in Ihrer App aktiviert haben, können Sie das Braze-Dashboard so konfigurieren, dass alle Anfragen mit einem ungültigen oder fehlenden JSON Internet Token (JWT) abgelehnt werden:

- Versenden von angepassten Events, Attributen, Käufen und Sitzungsdaten
- Erstellen neuer Nutzer:innen in Ihrem Braze Workspace
- Update der Attribute des Standard Nutzerprofils
- Empfangen oder Triggern von Nachrichten

Jetzt können Sie verhindern, dass nicht authentifizierte, angemeldete Nutzer:innen den SDK-API-Schlüssel Ihrer App verwenden, um bösartige Aktionen durchzuführen, wie z.B. sich als Ihre anderen Nutzer:innen auszugeben.

## Authentifizierung einrichten

### Schritt 1: Richten Sie Ihren Server ein {#server-side-integration}

#### Schritt 1.1: Erzeugen eines Public-Private-Key-Paars {#generate-keys}

Erzeugen Sie ein RSA256 Public/Private Key-Paar. Der Public Key wird schließlich dem Braze-Dashboard hinzugefügt, während der Private Key sicher auf Ihrem Server gespeichert sein muss.

Wir empfehlen einen RSA-Schlüssel mit 2048 Bit für die Verwendung mit dem RS256 JWT-Algorithmus.

{% alert warning %}
Denken Sie daran, Ihre Private Keys immer _geheim_ zu halten. Geben Sie Ihren Private Key niemals in Ihrer App oder auf Ihrer Website preis. Jeder, der Ihren Private Key kennt, kann sich als Nutzer ausgeben oder Nutzer für Ihre Anwendung erstellen.
{% endalert %}

#### Schritt 1.2: Erstellen Sie ein JSON Internet Token für den aktuellen Nutzer:in {#create-jwt}

Sobald Sie Ihren Private Key haben, sollte Ihre Server-seitige Anwendung ihn verwenden, um ein JWT für den aktuell angemeldeten Nutzer:in an Ihre App oder Website zurückzugeben.

Typischerweise könnte diese Logik überall dort zum Einsatz kommen, wo Ihre App normalerweise das Profil des aktuellen Nutzers anfragen würde, z.B. an einem Endpunkt für die Anmeldung oder wo Ihre App das Profil des aktuellen Nutzers aktualisiert.

Bei der Erstellung des JWT werden die folgenden Felder erwartet:

**JWT-Kopfzeile**

| Feld | Erforderlich | Beschreibung                         |
| ----- | -------- | ----------------------------------- |
| `alg` | Ja  | Der unterstützte Algorithmus ist `RS256`. |
| `typ` | Ja  | Der Typ sollte `JWT` entsprechen.        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

**JWT-Payload**

| Feld | Erforderlich | Beschreibung                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | Ja  | "Subject" muss die Nutzer-ID sein, die Sie Braze SDK beim Aufruf übergeben. `changeUser`  |
| `exp` | Ja | "Expiration" ist der Zeitpunkt, an dem das Token ablaufen soll.                                |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Um mehr über JSON Web Token zu erfahren oder die vielen Öffnungen von Bibliotheken zu durchsuchen, die diesen Signierungsprozess vereinfachen, besuchen Sie [https://jwt.io.](https://jwt.io)
{% endalert %}

### Schritt 2: SDK konfigurieren {#sdk-integration}

Dieses Feature ist ab den folgenden [SDK-Versionen verfügbar]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
Für iOS-Integrationen finden Sie auf dieser Seite die Schritte für das Braze Swift SDK. Für Beispiele zur Verwendung im iOS SDK von AppboyKit referenzieren Sie [diese Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) und [diese Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m).
{% endalert %}

#### Schritt 2.1: Aktivieren Sie die Authentifizierung im Braze SDK.

Wenn dieses Feature aktiviert ist, fügt das Braze SDK das letzte bekannte JWT des aktuellen Nutzers an Netzwerkanfragen an Braze Server an.

{% alert note %}
Keine Sorge, die Initialisierung mit dieser Option allein hat keinerlei Auswirkungen auf die Datenerfassung, solange Sie nicht im Braze-Dashboards die [Authentifizierung erzwingen](#braze-dashboard).
{% endalert %}

{% tabs %}
{% tab JavaScript %}
Wenn Sie `initialize` aufrufen, setzen Sie die optionale Eigenschaft `enableSdkAuthentication` auf `true`.
```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab Java %}
Wenn Sie die Braze-Instanz konfigurieren, rufen Sie `setIsSdkAuthenticationEnabled` auf `true` auf.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

Alternativ können Sie auch `<bool name="com_braze_sdk_authentication_enabled">true</bool>` zu braze.xml hinzufügen.
{% endtab %}
{% tab KOTLIN %}
Wenn Sie die Braze-Instanz konfigurieren, rufen Sie `setIsSdkAuthenticationEnabled` auf `true` auf.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

Alternativ können Sie auch `<bool name="com_braze_sdk_authentication_enabled">true</bool>` zu braze.xml hinzufügen.
{% endtab %}
{% tab Objective-C %}
Um die SDK-Authentifizierung zu aktivieren, setzen Sie die Eigenschaft `configuration.api.sdkAuthentication` Ihres `BRZConfiguration`-Objekts auf `YES`, bevor Sie die Braze-Instanz initialisieren:

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Swift %}
Um die SDK-Authentifizierung zu aktivieren, setzen Sie die Eigenschaft `configuration.api.sdkAuthentication` Ihres `Braze.Configuration`-Objekts auf `true`, wenn Sie das SDK initialisieren:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
Derzeit muss die SDK-Authentifizierung im Rahmen der Initialisierung des SDK im nativen iOS- und Android-Code aktiviert werden. Um die SDK-Authentifizierung im Flutter SDK zu aktivieren, folgen Sie den Integrationen für iOS und Android auf den anderen Tabs. Nachdem die SDK-Authentifizierung aktiviert ist, kann der Rest des Features in Dart integriert werden.
{% endtab %}
{% endtabs %}

#### Schritt 2.2: Setzen Sie das JWT des aktuellen Nutzer:innen

Wann immer Ihre App die Methode Braze `changeUser` aufruft, geben Sie auch das JWT an, das [serverseitig generiert](#braze-dashboard) wurde.

Sie können das Token auch so konfigurieren, dass es mitten in der Sitzung für den aktuellen Nutzer aktualisiert wird.

{% alert note %}
Denken Sie daran, dass `changeUser` nur aufgerufen werden sollte, wenn die Nutzer-ID _sich tatsächlich geändert hat_. Sie sollten diese Methode nicht zum Update des Authentifizierungs-Tokens (JWT) verwenden, wenn sich die Nutzer:innen-ID nicht geändert hat.
{% endalert %}

{% tabs %}
{% tab JavaScript %}
Geben Sie das JWT beim Aufruf an [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
):

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Oder wenn Sie das Token des Nutzers mitten in der Sitzung erneuert haben:

```javascript
import * as braze from"@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

Geben Sie das JWT beim Aufruf an [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Oder wenn Sie das Token des Nutzers mitten in der Sitzung erneuert haben:

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

Geben Sie das JWT beim Aufruf an [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER")
```

Oder wenn Sie das Token des Nutzers mitten in der Sitzung erneuert haben:

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

Geben Sie das JWT beim Aufruf an [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"JWT-FROM-SERVER"];
```

Oder wenn Sie das Token des Nutzers mitten in der Sitzung erneuert haben:

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"NEW-JWT-FROM-SERVER"];
```
{% endtab %}
{% tab Swift %}

Geben Sie das JWT beim Aufruf an [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
Oder wenn Sie das Token des Nutzers mitten in der Sitzung erneuert haben:

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Dart %}

Geben Sie das JWT beim Aufruf an [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```dart
braze.changeUser("userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
Oder wenn Sie das Token des Nutzers mitten in der Sitzung erneuert haben:

```dart
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```

{% endtab %}
{% endtabs %}

#### Schritt 2.3: Registrieren Sie eine Callback-Funktion für ungültige Token {#sdk-callback}

Wenn dieses Feature auf [Erforderlich](#enforcement-options) gesetzt ist, werden SDK-Anfragen in den folgenden Fällen von Braze abgelehnt:
- JWT ist zu dem Zeitpunkt, an dem es von der Braze API empfangen wurde, abgelaufen
- JWT war leer oder fehlte
- JWT konnte für die öffentlichen Schlüssel, die Sie auf das Braze-Dashboard hochgeladen haben, nicht überprüft werden

Mit `subscribeToSdkAuthenticationFailures` können Sie sich benachrichtigen lassen, wenn SDK-Anfragen aus einem dieser Gründe fehlschlagen. Eine Callback-Funktion enthält ein Objekt mit dem entsprechenden [`errorCode`](#error-codes), `reason` für den Fehler, die `userId` der Anfrage (wenn der Nutzer:innen nicht anonym ist) und das Authentifizierungs-Token (JWT), das den Fehler verursacht hat. 

Fehlgeschlagene Anfragen werden regelmäßig wiederholt, bis Ihre App ein neues gültiges JWT liefert. Wenn dieser Nutzer:innen noch angemeldet ist, können Sie diesen Callback als Opportunity nutzen, um ein neues JWT von Ihrem Server anzufordern und das Braze SDK mit diesem neuen gültigen Token zu versorgen.

{% alert tip %}
Diese Callback-Methoden eignen sich hervorragend, um Ihren eigenen Überwachungs- oder Fehlerprotokollierungsdienst hinzuzufügen, damit Sie verfolgen können, wie oft Ihre Anfragen an Braze abgelehnt werden.
{% endalert %}

{% tabs %}
{% tab JavaScript %}
```javascript
import * as braze from"@braze/web-sdk";
braze.subscribeToSdkAuthenticationFailures((error) => {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  const updated_jwt = await getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(updated_jwt);
});
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    // TODO: Optionally log to your error-reporting service
    // TODO: Check if the error user matches the currently logged-in user
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    // TODO: Optionally log to your error-reporting service
    // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  NSLog(@"Invalid SDK Authentication Token.");
  NSString *newSignature = getNewTokenSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% endtabs %}

### Schritt 3: Aktivieren Sie die Authentifizierung im Dashboard {#braze-dashboard}

Als nächstes können Sie im Braze-Dashboard die Authentifizierung für die Apps aktivieren, die Sie zuvor eingerichtet haben.

Beachten Sie, dass SDK-Anfragen ohne Authentifizierung wie gewohnt weiterlaufen, es sei denn, die SDK-Authentifizierung der App ist im Braze-Dashboard auf **Erforderlich** eingestellt.

Sollte bei Ihrer Integration etwas schief gehen (z.B. wenn Ihre App Token fälschlicherweise an das SDK weitergibt oder Ihr Server ungültige Token generiert), deaktivieren Sie dieses Feature im Braze-Dashboard, und die Daten fließen ohne Überprüfung wie gewohnt weiter.

#### Durchsetzungsoptionen {#enforcement-options}

Auf der Dashboard-Seite **Einstellungen verwalten** verfügt jede App über drei SDK-Authentifizierungsstatus, die steuern, wie Braze Anfragen überprüft.

| Einstellung| Beschreibung|
| ------ | ---------- |
| **Deaktiviert** | Braze überprüft die JWT, die für einen Nutzer:innen bereitgestellt wird, nicht. (Standardeinstellung)|
| **Optional** | Braze überprüft Anfragen für angemeldete Nutzer, weist aber ungültige Anfragen nicht zurück. |
| **Erforderlich** | Braze überprüft Anfragen für eingeloggte Nutzer:innen und weist ungültige JWTs zurück.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/sdk-auth-settings.png %})

Die Einstellung **Optional** ist eine nützliche Möglichkeit, die möglichen Auswirkungen dieses Features auf den SDK-Traffic Ihrer App zu überwachen.

Ein ungültiges JWT wird sowohl im **Optional-** als auch im **Required-Status** gemeldet, aber nur im **Required-Status** werden SDK-Anfragen abgelehnt, so dass Apps es erneut versuchen und ein neues JWT anfordern müssen.

## Öffentliche Schlüssel verwalten {#key-management}

### Hinzufügen eines Public Keys

Sie können bis zu drei öffentliche Schlüssel für jede App hinzufügen: einen primären, einen sekundären und einen tertiären. Sie können denselben Schlüssel bei Bedarf auch zu mehreren Apps hinzufügen. Um einen öffentlichen Schlüssel hinzuzufügen:

1. Gehen Sie zum Braze-Dashboard und wählen Sie **Einstellungen** > **App-Einstellungen**.
2. Wählen Sie eine App aus Ihrer Liste der verfügbaren Apps.
3. Wählen Sie unter **SDK-Authentifizierung** **Public Key hinzufügen**.
4. Geben Sie eine optionale Beschreibung ein, fügen Sie Ihren Public Key ein und wählen Sie **Public Key hinzufügen**.

### Einen neuen Primärschlüssel zuweisen

So weisen Sie einen Sekundär- oder Tertiärschlüssel als Ihren neuen Primärschlüssel zu:

1. Gehen Sie zum Braze-Dashboard und wählen Sie **Einstellungen** > **App-Einstellungen**.
2. Wählen Sie eine App aus Ihrer Liste der verfügbaren Apps.
3. Wählen Sie unter **SDK-Authentifizierung** einen Schlüssel und wählen Sie **Verwalten** > **Primärschlüssel erstellen**.

### Schlüssel löschen

Um einen Primärschlüssel zu löschen, [weisen Sie zunächst einen neuen Primärschlüssel zu](#assign-a-new-primary-key) und löschen dann Ihren Schlüssel. So löschen Sie einen nicht-primären Schlüssel:

1. Gehen Sie zum Braze-Dashboard und wählen Sie **Einstellungen** > **App-Einstellungen**.
2. Wählen Sie eine App aus Ihrer Liste der verfügbaren Apps.
3. Wählen Sie unter **SDK-Authentifizierung** einen nicht primären Schlüssel und wählen Sie **Verwalten** > **Public Key löschen**.

## Analytics {#analytics}

Jede App zeigt eine Aufschlüsselung der SDK-Authentifizierungsfehler, die gesammelt wurden, während sich dieses Feature im Status **Optional** und **Erforderlich** befindet.

Die Daten sind in Realtime verfügbar, und Sie können den Mauszeiger über Datenpunkte im Chart bewegen, um eine Aufschlüsselung der Fehler für ein bestimmtes Datum zu sehen.

![Ein Chart, das die Anzahl der Instanzen von Authentifizierungsfehlern anzeigt. Außerdem werden die Gesamtzahl der Fehler, die Fehlerart und der einstellbare Datumsbereich angezeigt.]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## Fehlercodes {#error-codes}

| Fehlercode| Fehlerursache | Beschreibung |
| --------  | ------------ | ---------  |
| (10 %) | `EXPIRATION_REQUIRED` | Der Ablauf ist ein Pflichtfeld für die Verwendung von Braze.|
| 20 | `DECODING_ERROR` | Nicht übereinstimmender Public Key oder ein allgemeiner nicht abgefangener Fehler.|
| 21 | `SUBJECT_MISMATCH` | Die erwarteten und tatsächlichen Themen sind nicht identisch.|
| 22 | `EXPIRED` | Das angegebene Token ist abgelaufen.|
| 23 | `INVALID_PAYLOAD` | Die Nutzdaten des Tokens sind ungültig.|
| 24 | `INCORRECT_ALGORITHM` | Der Algorithmus des Tokens wird nicht unterstützt.|
| 25 | `PUBLIC_KEY_ERROR` | Der Public Key konnte nicht in das richtige Format umgewandelt werden.|
| 26 | `MISSING_TOKEN` | Es wurde kein Token in der Anfrage angegeben.|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | Es gibt keine öffentlichen Schlüssel, die mit dem angegebenen Token übereinstimmen.|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | Nicht alle Nutzer:innen IDs in der Payload der Anfrage stimmen überein.|
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 role="presentation" }

## Häufig gestellte Fragen (FAQ) {#faq}

#### Muss dieses Feature in allen meinen Apps gleichzeitig aktiviert werden? {#faq-app-by-app}

Nein, dieses Feature kann für bestimmte Apps aktiviert werden und muss nicht für alle Ihre Apps auf einmal verwendet werden.

#### Was passiert mit Nutzer:innen, die noch ältere Versionen meiner App verwenden? {#faq-sdk-backward-compatibility}

Wenn Sie damit beginnen, dieses Feature zu erzwingen, werden Anfragen von älteren App-Versionen von Braze abgelehnt und vom SDK erneut versucht. Nachdem Nutzer ihre App auf eine unterstützte Version aktualisiert haben, werden diese Anfragen in der Warteschlange wieder akzeptiert.

Wenn möglich, sollten Sie die Nutzer zum Upgraden pushen, wie Sie es bei jedem anderen Pflichtfeld tun würden. Alternativ können Sie das Feature [optional](#enforcement-options) lassen, bis Sie sehen, dass ein akzeptabler Prozentsatz der Nutzer:innen geupgradet hat.

#### Welche Gültigkeitsdauer sollte ich bei der Erstellung eines JWTs verwenden? {#faq-expiration}

Wir empfehlen, den höheren Wert der durchschnittlichen Sitzungsdauer, des Ablaufs von Cookies/Token oder der Häufigkeit zu verwenden, mit der Ihre Anwendung sonst das Profil des aktuellen Nutzers aktualisieren würde.

#### Was passiert, wenn ein JWT mitten in der Sitzung eines Nutzers abläuft? {#faq-jwt-expiration}

Sollte das Token eines Nutzers mitten in der Sitzung ablaufen, verfügt das SDK über eine [Callback-Funktion](#sdk-callback), die Ihre App darüber informiert, dass ein neues JWT erforderlich ist, um weiterhin Daten an Braze zu senden.

#### Was passiert, wenn meine Server-seitige Integration nicht mehr funktioniert und ich kein JWT mehr erstellen kann? {#faq-server-downtime}

Wenn Ihr Server kein JWT bereitstellen kann oder Sie ein Problem bei der Integration feststellen, können Sie das Feature jederzeit im Braze-Dashboard deaktivieren.

Nach der Deaktivierung werden alle ausstehenden fehlgeschlagenen SDK-Anfragen vom SDK erneut versucht und von Braze akzeptiert.

#### Warum verwendet dieses Feature Public und Private Keys und nicht Shared Secrets? {#faq-shared-secrets}

Bei der Verwendung gemeinsamer Geheimnisse könnte jeder, der Zugriff auf dieses gemeinsame Geheimnis hat, z. B. die Seite Braze-Dashboard, Token generieren und sich als Ihre Nutzer:innen ausgeben.

Stattdessen verwenden wir öffentliche/private Schlüssel, so dass nicht einmal Braze-Mitarbeiter (geschweige denn Ihre Nutzer:innen des Dashboards) Zugriff auf Ihre Private Keys haben.

#### Wie werden abgelehnte Anfragen erneut versucht? {#faq-retry-logic}

Wenn eine Anfrage aufgrund eines Authentifizierungsfehlers abgelehnt wird, ruft das SDK Ihren Callback auf, mit dem Sie die JWT des Nutzer:innen aktualisieren können. 

Anfragen werden in regelmäßigen Abständen mit einem exponentiellen Backoff-Verfahren wiederholt. Nach 50 aufeinanderfolgenden Fehlversuchen werden die Versuche bis zum nächsten Sitzungsstart pausiert. Jedes SDK verfügt auch über eine Methode zur manuellen Anfrage eines Data Flush.

