---
nav_title: Sitzungs-Tracking
article_title: Sitzungs-Tracking für iOS
platform: iOS
page_order: 0
description: "Dieser Referenzartikel beschreibt, wie Sie Sitzungsupdates für Ihre iOS-Anwendung abonnieren können."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Sitzungs-Tracking für iOS

Das Braze SDK meldet Sitzungsdaten, die vom Braze Dashboard verwendet werden, um das Nutzer-Engagement und andere Analysen zu berechnen, die für das Verständnis Ihrer Nutzer wichtig sind. Unser SDK generiert Datenpunkte für "Sitzung starten" und "Sitzung schließen", die die Sitzungslänge und die Anzahl der Sitzungen berücksichtigen und im Braze-Dashboard auf der Grundlage der folgenden Session-Semantik angezeigt werden können.

## Lebenszyklus einer Sitzung

Eine Sitzung wird gestartet, wenn Sie `[[Appboy sharedInstance]` `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions]` aufrufen. Danach beginnen Sitzungen standardmäßig, wenn die Benachrichtigung `UIApplicationWillEnterForegroundNotification` ausgelöst wird (z. B. wenn die App in den Vordergrund tritt). Sie enden, wenn die App den Vordergrund verlässt (z. B. wenn die Benachrichtigung `UIApplicationDidEnterBackgroundNotification` ausgelöst wird oder die App abstürzt).

{% alert note %}
Wenn Sie eine neue Sitzung erzwingen müssen, können Sie dies tun, indem Sie den Nutzer wechseln.
{% endalert %}

## Anpassen des Sitzungs-Timeouts

Ab Braze iOS SDK v3.14.1 können Sie das Sitzungs-Timeout über die Datei Info.plist einstellen. Fügen Sie das Wörterbuch `Braze` zu Ihrer Datei `Info.plist` hinzu. Fügen Sie im Wörterbuch `Braze` den Untereintrag `SessionTimeout` hinzu und legen Sie den Wert auf Ihr angepasstes Sitzungs-Timeout fest. Beachten Sie, dass vor Braze iOS SDK v4.0.2 der Wörterbuchschlüssel `Appboy` anstelle von `Braze` verwendet werden muss.

Alternativ können Sie in Ihrem `appboyOptions`-Objekt, das an [`startWithApiKey`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#afd911d60dfe7e5361afbfb364f5d20f9) übergeben wird, den Schlüssel `ABKSessionTimeoutKey` auf den gewünschten Integer-Wert setzen.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the session timeout to 60 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKSessionTimeoutKey : @(60) }];
```

{% endtab %}
{% tab schnell %}

```swift
// Sets the session timeout to 60 seconds
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKSessionTimeoutKey : 60 ])
```
{% endtab %}
{% endtabs %}

Wenn Sie einen Timeout für die Sitzung festgelegt haben, erstreckt sich die Session-Semantik auf diesen angepassten Timeout.

{% alert note %}
Der Mindestwert für `sessionTimeoutInSeconds` ist 1 Sekunde. Der Standardwert ist 10 Sekunden.
{% endalert %}

## Testen des Sitzungs-Trackings

Um Sitzungen über Ihren Benutzer zu erkennen, suchen Sie Ihren Benutzer im Dashboard und navigieren Sie im Benutzerprofil zu **App-Nutzung**. Um sicherzugehen, dass das Sitzungs-Tracking funktioniert, können Sie überprüfen, ob die Metrik "Sitzungen" ansteigt, wenn Sie es erwarten.

![Der Bereich "App-Nutzung" eines Nutzerprofils, in dem die Anzahl der Sitzungen, das Datum der letzten Nutzung und das Datum der ersten Nutzung angezeigt wird.]({% image_buster /assets/img_archive/test_session.png %})

