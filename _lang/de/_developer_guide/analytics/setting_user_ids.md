---
nav_title: "Nutzer:innen einstellen"
article_title: "Festlegen von Nutzer:innen IDs über das Braze SDK"
page_order: 1.1
description: "Lernen Sie, wie Sie Nutzer:innen IDs über das Braze SDK festlegen."

---

# Nutzer:innen IDs festlegen

> Lernen Sie, wie Sie Nutzer:innen IDs über das Braze SDK festlegen. Dabei handelt es sich um eindeutige Bezeichner, mit denen Sie Nutzer:innen geräte- und plattformübergreifend tracken, ihre Daten über die [Nutzerdaten-API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) importieren und gezielte Nachrichten über die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) versenden können. Wenn Sie einem Nutzer:in keine eindeutige ID zuweisen, weist Braze ihm stattdessen eine anonyme ID zu. Solange Sie dies nicht tun, können Sie diese Features jedoch nicht nutzen.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

## Über anonyme Nutzer:innen

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

## Einstellen einer Nutzer:in ID

Um eine ID festzulegen, rufen Sie die Methode `changeUser()` auf, nachdem sich der Nutzer:innen das erste Mal angemeldet hat. IDs sollten eindeutig sein und unseren [Best Practices für die Namensgebung](#naming-best-practices) entsprechen.

Wenn Sie stattdessen einen eindeutigen Bezeichner hashen, stellen Sie sicher, dass Sie die Eingabe Ihrer Hashing-Funktion normalisieren. Wenn Sie zum Beispiel eine E-Mail Adresse hashen, entfernen Sie alle führenden und nachfolgenden Leerzeichen und berücksichtigen Sie die Lokalisierung.

{% tabs local %}
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

{% tab WEB %}
Für eine Standard Internet SDK-Implementierung können Sie die folgende Methode verwenden:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Wenn Sie stattdessen den Google Tag Manager verwenden möchten, können Sie den Tag-Typ **Nutzer:innen ändern** verwenden, um die [Methode`changeUser` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) aufzurufen. Verwenden Sie es immer dann, wenn sich ein Nutzer:in anmeldet oder anderweitig mit seinem eindeutigen Bezeichner `external_id` identifiziert wird.

Achten Sie darauf, die eindeutige ID des aktuellen Benutzers in das Feld **Externe Benutzer-ID** einzugeben, die in der Regel mit einer von Ihrer Website gesendeten Datenschichtvariablen gefüllt wird.

![Ein Dialogfeld mit den Konfigurationseinstellungen für Braze Action Tags. Zu den Einstellungen gehören "Tag-Typ" und "Externe Nutzer-ID".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
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

{% tab UNREAL ENGINE %}
```cpp
UBraze->ChangeUser(TEXT("YOUR_USER_ID_STRING"));
```
{% endtab %}
{% endtabs %}

{% alert warning %}
**Weisen Sie keine statische Standard ID zu oder rufen Sie `changeUser()` an, wenn sich ein Nutzer:innen abmeldet.** Auf diese Weise können Sie keine erneute Interaktion mit zuvor eingeloggten Nutzer:innen auf gemeinsam genutzten Geräten durchführen. Verfolgen Sie stattdessen alle Nutzer:innen IDs separat und stellen Sie sicher, dass der Abmeldeprozess Ihrer App den Wechsel zu einem zuvor angemeldeten Nutzer:innen zulässt. Wenn eine neue Sitzung beginnt, aktualisiert Braze automatisch die Daten für das neu aktive Profil.
{% endalert %}

## Nutzer-Aliasse

### Funktionsweise

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Einrichten eines Nutzer:in-Alias

Ein Nutzer-Alias besteht aus zwei Teilen: einem Namen und einer Bezeichnung. Der Name referenziert auf den Bezeichner selbst, während die Bezeichnung auf den Typ des Bezeichners verweist, zu dem er gehört. Wenn Sie z.B. einen Nutzer:in einer Kunden:innen-Plattform eines Drittanbieters mit der externen ID `987654` haben, können Sie ihm in Braze einen Alias mit dem Namen `987654` und dem Label `support_id` zuweisen, damit Sie ihn plattformübergreifend tracken können.

{% tabs local %}
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

{% tab schnell %}
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

{% tab Internet %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab rest api %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}
{% endtabs %}

## Bewährte ID-Benennungsmethoden {#naming-best-practices}

Wir empfehlen Ihnen, Nutzer:innen IDs nach dem [UUID-Standard (Universally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) ) zu erstellen, d.h. es handelt sich um 128-Bit-Strings, die zufällig und gut verteilt sind.

Alternativ können Sie einen vorhandenen eindeutigen Bezeichner (z.B. einen Namen oder eine E-Mail Adresse) hashen, um stattdessen Ihre Nutzer:innen zu generieren. Wenn Sie dies tun, stellen Sie sicher, dass Sie eine [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/authentication/) implementieren, damit Sie Nutzer:innen vor einem Identitätswechsel schützen können.

Es ist zwar wichtig, dass Sie Ihre Nutzer:innen IDs von Anfang an richtig benennen, aber Sie können sie in Zukunft jederzeit mit dem [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/) Endpunkt.

| Empfohlen | Nicht empfohlen |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | Firmenname-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Vermeiden Sie die Weitergabe von Details über die Erstellung von Nutzer:innen IDs, da dies Ihr Unternehmen bösartigen Angriffen oder der Löschung von Daten aussetzen könnte.
{% endalert %}
