---
nav_title: Nutzer-IDs festlegen
article_title: Nutzer-IDs über das Braze SDK festlegen
page_order: 1.1
description: "Erfahren Sie, wie Sie Nutzer-IDs über das Braze SDK festlegen."

---

# Nutzer-IDs festlegen

> Erfahren Sie, wie Sie Nutzer-IDs über das Braze SDK festlegen. Dabei handelt es sich um eindeutige Bezeichner, mit denen Sie Nutzer:innen geräte- und plattformübergreifend tracken, ihre Daten über die [Nutzerdaten-API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) importieren und gezielte Nachrichten über die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) versenden können. Wenn Sie einer Nutzer:in keine eindeutige ID zuweisen, weist Braze stattdessen eine anonyme ID zu. Solange Sie dies nicht tun, können Sie diese Features jedoch nicht nutzen.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

## Über anonyme Nutzer:innen

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

### Anonymes Nutzer-Tracking verhindern

Wenn Ihr Anwendungsfall erfordert, dass keine Daten erfasst werden, bevor eine Nutzer:in identifiziert wurde, können Sie die Initialisierung des Braze SDK verzögern, bis sich die Nutzer:in anmeldet und eine `external_id` verfügbar ist. Setzen Sie in Ihrem Code ein Flag, das auf `true` wechselt, wenn sich die Nutzer:in anmeldet, und initialisieren Sie das SDK erst, wenn dieses Flag gesetzt ist.

{% alert warning %}
Verzögern Sie die Initialisierung nur beim **ersten Mal**, wenn eine Nutzer:in Ihre App herunterlädt (bevor eine `external_id` gesetzt wurde). Wenn Sie verhindern, dass das SDK bei jeder Abmeldung oder jedem neuen Sitzungsstart initialisiert wird, beeinträchtigt dies das Vorladen von In-App-Nachrichten und Content-Card-Assets, was zu Zustellbarkeitsfehlern bei diesen Kampagnen führen kann.
{% endalert %}

## Nutzer-ID festlegen

Um eine Nutzer-ID festzulegen, rufen Sie die Methode `changeUser()` auf, nachdem sich die Nutzer:in das erste Mal angemeldet hat. IDs sollten eindeutig sein und unseren [Best Practices für die Namensgebung](#naming-best-practices) entsprechen.

Wenn Sie stattdessen einen eindeutigen Bezeichner hashen, stellen Sie sicher, dass Sie die Eingabe Ihrer Hashing-Funktion normalisieren. Wenn Sie zum Beispiel eine E-Mail-Adresse hashen, entfernen Sie alle führenden und nachfolgenden Leerzeichen und berücksichtigen Sie die Lokalisierung.

{% tabs local %}
{% tab WEB %}
Für eine Standard-Web-SDK-Implementierung können Sie die folgende Methode verwenden:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Wenn Sie stattdessen den Google Tag Manager verwenden möchten, können Sie den Tag-Typ **Nutzer:in ändern** verwenden, um die [`changeUser`-Methode](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) aufzurufen. Verwenden Sie ihn immer dann, wenn sich eine Nutzer:in anmeldet oder anderweitig mit dem eindeutigen `external_id`-Bezeichner identifiziert wird.

Achten Sie darauf, die eindeutige ID der aktuellen Nutzer:in in das Feld **Externe Nutzer-ID** einzugeben, das in der Regel mit einer von Ihrer Website gesendeten Datenschichtvariablen gefüllt wird.

![Ein Dialogfeld mit den Konfigurationseinstellungen für Braze Action Tags. Die enthaltenen Einstellungen sind „Tag-Typ" und „externe Nutzer-ID".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab ANDROID %}
{% subtabs %}
{% subtab JAVA %}
```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab SWIFT %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab CORDOVA %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ROKU %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab UNITY %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab REACT NATIVE %}
```javascript
Braze.changeUser("YOUR_USER_ID_STRING");
```
{% endtab %}
{% endtabs %}

### Funktionsweise von `changeUser()`

Wenn Sie `changeUser()` aufrufen, gelten die folgenden Verhaltensweisen:

- Der Aufruf von `changeUser()` mit **derselben** Nutzer-ID, die bereits gesetzt ist, hat keine Auswirkung auf die Sitzungsanzahl.
- Der Aufruf von `changeUser()` mit einer **anderen** Nutzer-ID beendet automatisch die aktuelle Sitzung und startet eine neue.
- Wenn eine anonyme Nutzer:in `changeUser()` mit einer **neuen** Nutzer-ID aufruft (die in Braze noch nicht existiert), werden die Daten des anonymen Profils in das neue identifizierte Profil zusammengeführt.
- Wenn eine anonyme Nutzer:in `changeUser()` mit einer **bestehenden** Nutzer-ID aufruft, werden die Daten des anonymen Profils nicht in das identifizierte Profil zusammengeführt.

{% alert note %}
Der Aufruf von `changeUser()` löst im Rahmen des Schließens der aktuellen Sitzung einen Daten-Flush aus. Das SDK sendet automatisch alle ausstehenden Daten der vorherigen Nutzer:in, bevor es zur neuen Nutzer:in wechselt. Daher ist es nicht erforderlich, vor dem Aufruf von `changeUser()` manuell einen Daten-Flush anzufordern.
{% endalert %}

{% alert warning %}
Weisen Sie keine einzelne, gemeinsam genutzte Nutzer-ID zu (z. B. eine statische Standard-externe-ID) und rufen Sie `changeUser()` nicht auf, wenn sich eine Nutzer:in abmeldet. Andernfalls können Sie keine erneute Interaktion mit zuvor eingeloggten Nutzer:innen auf gemeinsam genutzten Geräten durchführen, und alle Daten werden unter einer einzigen Nutzer-ID protokolliert, was dazu führen kann, dass andere Features nicht wie erwartet funktionieren. Verfolgen Sie stattdessen alle Nutzer-IDs separat und stellen Sie sicher, dass der Abmeldeprozess Ihrer App den Wechsel zu einer zuvor angemeldeten Nutzer:in ermöglicht. Wenn eine neue Sitzung beginnt, aktualisiert Braze automatisch die Daten für das neu aktive Profil.
{% endalert %}

## Nutzer-Aliasse

### Funktionsweise

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Nutzer-Alias einrichten

Ein Nutzer-Alias besteht aus zwei Teilen: einem Namen und einem Label. Der Name referenziert den Bezeichner selbst, während das Label auf den Typ des Bezeichners verweist, zu dem er gehört. Wenn Sie z. B. eine Nutzer:in in einer Kund:innen-Support-Plattform eines Drittanbieters mit der externen ID `987654` haben, können Sie in Braze einen Alias mit dem Namen `987654` und dem Label `support_id` zuweisen, damit Sie die Nutzer:in plattformübergreifend tracken können.

{% tabs local %}
{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab rest api %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}

{% tab react native %}
```javascript
Braze.addAlias("ALIAS_NAME", "ALIAS_LABEL");
```
{% endtab %}
{% endtabs %}

## Best Practices für die ID-Benennung {#naming-best-practices}

Wir empfehlen Ihnen, Nutzer-IDs nach dem [UUID-Standard (Universally Unique Identifier)](https://en.wikipedia.org/wiki/Universally_unique_identifier) zu erstellen, d. h. es handelt sich um 128-Bit-Strings, die zufällig und gut verteilt sind.

Alternativ können Sie einen vorhandenen eindeutigen Bezeichner (z. B. einen Namen oder eine E-Mail-Adresse) hashen, um Ihre Nutzer-IDs zu generieren. Wenn Sie dies tun, stellen Sie sicher, dass Sie eine [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/sdk_integration/authentication/) implementieren, damit Sie einen Identitätswechsel verhindern können.

{% alert warning %}
Verwenden Sie für Ihre Nutzer-ID keine leicht zu erratenden Werte oder fortlaufende Zahlen. Dies könnte Ihr Unternehmen böswilligen Angriffen oder Datenexfiltration aussetzen.

Für zusätzliche Sicherheit verwenden Sie die [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/sdk_integration/authentication/).
{% endalert %}

Es ist zwar wichtig, dass Sie Ihre Nutzer-IDs von Anfang an richtig benennen, aber Sie können sie in Zukunft jederzeit mit dem [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/)-Endpunkt umbenennen.

| Nicht empfohlene ID-Typen | Nicht empfohlenes Beispiel |
| ------------ | ----------- |
| Sichtbare Profil-ID oder Nutzername | JonDoe829525552 |
| E-Mail-Adresse | Anna@email.com |
| Automatisch inkrementierende Nutzer-ID | 123 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Vermeiden Sie es, Details darüber preiszugeben, wie Sie Nutzer-IDs erstellen, da dies Ihr Unternehmen böswilligen Angriffen oder Datenexfiltration aussetzen könnte.
{% endalert %}