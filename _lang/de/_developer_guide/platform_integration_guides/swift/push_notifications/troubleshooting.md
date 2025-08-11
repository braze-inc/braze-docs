---
nav_title: Fehlersuche
article_title: Fehlerbehebung bei Push-Benachrichtigungen für iOS
platform: Swift
page_order: 28
description: "In diesem Artikel werden mehrere Szenarien zur Fehlerbehebung bei iOS Push für das Swift SDK beschrieben."
channel:
  - push

---

# Fehlerbehebung {#push-troubleshooting}

> In diesem Artikel werden mehrere Szenarien zur Fehlerbehebung bei iOS Push für das Swift SDK beschrieben.

## Den Arbeitsablauf von Braze/APNs verstehen

Der Apple Push Notification Service (APNs) ist die Infrastruktur für das Senden von Push-Benachrichtigungen an Anwendungen, die auf den Plattformen von Apple laufen. Hier ist die vereinfachte Struktur, wie Push-Benachrichtigungen für die Geräte Ihrer Benutzer aktiviert werden und wie Braze Push-Benachrichtigungen an sie senden kann:

1. Sie konfigurieren das Push-Zertifikat und das Bereitstellungsprofil
2. Geräte registrieren sich für APNs und versorgen Braze mit Push-Tokens
3. Sie starten eine Braze Push-Kampagne
4. Braze entfernt ungültige Token

### Schritt 1: Konfigurieren des Push-Zertifikats und des Bereitstellungsprofils

Bei der Entwicklung Ihrer App müssen Sie ein SSL-Zertifikat erstellen, um Push-Benachrichtigungen zu aktivieren. Dieses Zertifikat wird in das Bereitstellungsprofil Ihrer App aufgenommen und muss außerdem in das Braze-Dashboard hochgeladen werden. Das Zertifikat ermöglicht es Braze, APNs mitzuteilen, dass wir in Ihrem Namen Push-Benachrichtigungen senden dürfen.

Es gibt zwei Arten von [Bereitstellungsprofilen](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) und Zertifikaten: Entwicklung und Verteilung. Um Unklarheiten zu vermeiden, empfehlen wir, nur Verteilungsprofile und Zertifikate zu verwenden. Wenn Sie unterschiedliche Profile und Zertifikate für die Entwicklung und Verteilung verwenden möchten, stellen Sie sicher, dass das in das Dashboard hochgeladene Zertifikat mit dem derzeit verwendeten Bereitstellungsprofil übereinstimmt.

{% alert warning %}
Ändern Sie nicht die Push-Zertifikat-Umgebung (Entwicklung oder Produktion). Wenn Sie das Push-Zertifikat in die falsche Umgebung ändern, kann dies dazu führen, dass Ihren Benutzern versehentlich ihr Push-Token entzogen wird, so dass sie nicht mehr per Push erreichbar sind.
{% endalert %}

### Schritt 2: Geräte registrieren sich für APNs und versorgen Braze mit Push-Tokens

Wenn Nutzer Ihre App öffnen, werden sie aufgefordert, Push-Benachrichtigungen zu akzeptieren. Stimmen sie der Aufforderung zu, generieren die APNs ein Push-Token für das betreffende Gerät. Das Swift SDK sendet das Push-Token für Apps, die die [standardmäßige Auto-Flush-Richtlinie]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing) verwenden, sofort und asynchron. Nachdem wir ein Push-Token mit einem Benutzer verknüpft haben, wird dieser im Dashboard auf seinem Benutzerprofil unter der Registerkarte **Engagement** als "Push registriert" angezeigt und ist berechtigt, Push-Benachrichtigungen von Braze-Kampagnen zu erhalten.

{% alert note %}
Ab macOS 13 können Sie auf bestimmten Geräten Push-Benachrichtigungen mithilfe eines Simulators für iOS 16 testen, der unter Xcode 14 läuft. Weitere Einzelheiten finden Sie in den [Release Notes zu Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

### Schritt 3: Starten Sie eine Braze-Push-Kampagne

Beim Starten einer Push-Kampagne stellt Braze Anfragen an APNs, um Ihre Nachricht zuzustellen. Braze verwendet das im Dashboard hochgeladene SSL-Push-Zertifikat, um sich zu authentifizieren und zu überprüfen, ob wir Push-Benachrichtigungen an die angegebenen Push-Tokens senden dürfen. Wenn ein Gerät online ist, sollte die Benachrichtigung kurz nach dem Senden der Kampagne empfangen werden. Beachten Sie, dass Braze das [Ablaufdatum](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) der APNs für Benachrichtigungen standardmäßig auf 30 Tage festlegt.

### Schritt 4: Entfernen von ungültigen Token

Wenn [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) uns informiert, dass eines der Push-Token, an das wir eine Nachricht senden wollten, ungültig ist, entfernen wir diese Token aus den Benutzerprofilen, mit denen sie verknüpft waren.

## Verwendung der Push-Fehlerprotokolle

Das [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) bietet Ihnen die Möglichkeit, alle Nachrichten (insbesondere Fehlermeldungen) im Zusammenhang mit Ihren Kampagnen und Sendungen zu sehen, einschließlich Push-Benachrichtigungsfehler. Dieses Fehlerprotokoll enthält eine Reihe von Warnungen, die sehr hilfreich sein können, um festzustellen, warum Ihre Kampagnen nicht wie erwartet funktionieren. Wenn Sie auf eine Fehlermeldung klicken, werden Sie zur entsprechenden Dokumentation weitergeleitet, die Sie bei der Fehlerbehebung unterstützt.

![Push-Fehlerprotokolle, die den Zeitpunkt des Auftretens des Fehlers, den Namen der App, den Kanal, den Fehlertyp und die Fehlermeldung anzeigen.]({% image_buster /assets/img_archive/message_activity_log.png %})

Zu den häufigen Fehlern, die Ihnen hier angezeigt werden, gehören nutzerspezifische Benachrichtigungen wie ["Nicht registrierte Sendung an Push-Token empfangen".](#received-unregistered-sending)

Darüber hinaus stellt Braze unter dem Tab **Engagement** ein Push-Changelog für das Nutzerprofil bereit. Dieses Changelog enthält Insights zum Verhalten bei der Push-Registrierung, z. B. Token-Invalidierung, Fehler bei der Push-Registrierung, zu neuen Nutzern verschobene Token.

![]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Fehler im Nachrichtenaktivitäts-Protokoll

#### Nicht registrierte Sendung an Push-Token empfangen {#received-unregistered-sending}

- Stellen Sie sicher, dass das Push-Token, das über die Methode `AppDelegate.braze?.notifications.register(deviceToken:)` an Braze gesendet wird, gültig ist. Im **Protokoll der Nachrichtenaktivität** können Sie das Push-Token sehen. Sie sollte etwa so aussehen wie `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, eine lange Zeichenkette mit einer Mischung aus Buchstaben und Zahlen. Wenn Ihr Push-Token anders aussieht, überprüfen Sie Ihren [Code]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze) zum Senden der Push-Tokens an Braze.
- Vergewissern Sie sich, dass das Push-Bereitstellungsprofil mit der Test-Umgebung übereinstimmt. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die APNs-Entwicklungs- oder die Produktionsumgebung gesendet werden. Die Verwendung eines Entwicklungszertifikats für eine Produktionsanwendung oder eines Produktionszertifikats für eine Entwicklungsanwendung wird nicht funktionieren.
 - Überprüfen Sie, ob das Push-Token, das Sie auf Braze hochgeladen haben, mit dem Bereitstellungsprofil übereinstimmt, das Sie zum Erstellen der App verwendet haben, von der Sie das Push-Token gesendet haben.

#### Geräte-Token nicht zum Thema

Dieser Fehler zeigt an, dass das Push-Zertifikat Ihrer App und die Bundle-ID nicht übereinstimmen. Überprüfen Sie, ob das Push-Zertifikat, das Sie auf Braze hochgeladen haben, mit dem Bereitstellungsprofil übereinstimmt, das zur Erstellung der App verwendet wurde, von der das Push-Token gesendet wurde.

#### BadDeviceToken zum Senden von Push-Token

`BadDeviceToken` ist ein APNs-Fehlercode. Er stammt nicht von Braze. Es kann eine Reihe von Gründen dafür geben, dass diese Antwort zurückgegeben wird, wie beispielsweise:

- Die App hat ein für die auf das Dashboard hochgeladenen Zugangsdaten ungültiges Push-Token empfangen.
- Push wurde für diesen Arbeitsbereich deaktiviert.
- Der Benutzer hat die Push-Funktion abbestellt.
- Die App wurde deinstalliert.
- Apple hat das Push-Token erneuert, wodurch das alte Token ungültig wurde.
- Die App wurde für eine Produktionsumgebung erstellt, aber die auf Braze hochgeladenen Push-Anmeldedaten sind für eine Entwicklungsumgebung eingestellt (oder umgekehrt).

## Probleme bei der Push-Registrierung

### Keine Push-Registrierungsaufforderung

Wenn die Anwendung Sie nicht auffordert, sich für Push-Benachrichtigungen zu registrieren, liegt wahrscheinlich ein Problem mit der Integration der Push-Registrierung vor. Stellen Sie sicher, dass Sie unsere [Dokumentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) befolgt und unsere Push-Registrierung korrekt integriert haben. Sie können auch Haltepunkte in Ihrem Code setzen, um sicherzustellen, dass der Code für die Push-Registrierung ausgeführt wird.

### Keine Anzeige von "push-registrierten" Nutzern im Dashboard (vor dem Senden von Nachrichten)

Stellen Sie sicher, dass Ihre App richtig konfiguriert ist, um Push-Benachrichtigungen zuzulassen. Zu den häufig zu überprüfenden Fehlerpunkten gehören:

- Überprüfen Sie, ob Sie von Ihrer App aufgefordert werden, Push-Benachrichtigungen zuzulassen. Normalerweise erscheint diese Aufforderung beim ersten Öffnen der App, aber sie kann auch so programmiert werden, dass sie an anderen Stellen erscheint. Wenn sie nicht dort erscheint, wo sie sein sollte, liegt das Problem wahrscheinlich bei der Grundkonfiguration der Push-Funktionen Ihrer App.
  - Überprüfen Sie, ob die Schritte für die [Push-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) erfolgreich abgeschlossen wurden.
  - Vergewissern Sie sich, dass das Bereitstellungsprofil Ihrer App Berechtigungen für Push enthält. Stellen Sie sicher, dass Sie alle verfügbaren Bereitstellungsprofile aus Ihrem Apple-Entwicklerkonto abrufen. Um dies zu bestätigen, führen Sie die folgenden Schritte aus:
    1. Navigieren Sie in Xcode zu **Voreinstellungen > Konten** (oder verwenden Sie die Tastenkombination <kbd>Befehl+</kbd><kbd>,</kbd>).
    2. Wählen Sie die Apple ID, die Sie für Ihr Entwicklerkonto verwenden, und klicken Sie auf **Details anzeigen**.
    3. Klicken Sie auf der nächsten Seite auf **<i class="fas fa-redo-alt"></i> Aktualisieren** und bestätigen Sie, dass Sie alle verfügbaren Provisionierungsprofile abrufen.
- Überprüfen Sie, ob die [Push-Funktion in Ihrer App korrekt aktiviert ist]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-2-enable-push-capabilities).
- Stellen Sie sicher, dass das Push-Bereitstellungsprofil mit der Test-Umgebung übereinstimmt. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die APNs-Entwicklungs- oder die Produktionsumgebung gesendet werden. Die Verwendung eines Entwicklungszertifikats für eine Produktionsanwendung oder eines Produktionszertifikats für eine Entwicklungsanwendung wird nicht funktionieren.
- Überprüfen Sie, ob unsere Methode `registerPushToken` aufgerufen wird, indem Sie einen Haltepunkt in Ihrem Code setzen.
- Stellen Sie sicher, dass Sie ein Gerät zum Testen verwenden (Push funktioniert nicht auf einem Simulator) und eine gute Netzwerkverbindung haben.

## Push-Benachrichtigungen, die gesendet, aber nicht auf den Geräten der Benutzer angezeigt werden

### "Push-registrierte" Benutzer werden nach dem Senden von Nachrichten nicht mehr aktiviert

Dies deutet wahrscheinlich darauf hin, dass das Push-Token des Nutzers ungültig war. Dafür kann es mehrere Gründe geben:

#### Dashboard und App-Zertifikat stimmen nicht überein

Wenn das Push-Zertifikat, das Sie im Dashboard hochgeladen haben, nicht dasselbe ist wie das im Bereitstellungsprofil, mit dem Ihre App erstellt wurde, lehnen die APNs das Token ab. Vergewissern Sie sich, dass Sie das richtige Zertifikat hochgeladen und eine weitere Sitzung in der App abgeschlossen haben, bevor Sie eine weitere Testbenachrichtigung versuchen.

#### Anwendung wurde deinstalliert

Wenn ein Benutzer Ihre Anwendung deinstalliert hat, ist sein Push-Token ungültig und wird beim nächsten Senden entfernt.

#### Ihr Bereitstellungsprofil neu generieren

Als letzten Ausweg können Sie von vorne beginnen und ein völlig neues Bereitstellungsprofil erstellen, um Konfigurationsfehler zu beheben, die durch die gleichzeitige Arbeit mit mehreren Umgebungen, Profilen und Anwendungen entstehen. Bei der Einrichtung von Push-Benachrichtigungen gibt es viele "bewegliche Teile". Daher ist es mitunter sinnvoll, noch einmal von vorn zu beginnen. Diese Vorgehensweise ist auch hilfreich, um das Problem einzugrenzen, wenn Sie die Fehlerbehebung fortsetzen müssen.

### Nachrichten werden nicht an "push-registrierte" Benutzer zugestellt

#### App wird in den Vordergrund gestellt

Bei iOS-Versionen, die Push nicht über das Framework `UserNotifications` integrieren, wird die Nachricht nicht angezeigt, wenn sich die App beim Empfang der Push-Nachricht im Vordergrund befindet. Vor dem Senden von Testnachrichten sollten Sie die App auf Ihren Testgeräten im Hintergrund laufen lassen.

#### Testbenachrichtigung falsch geplant

Überprüfen Sie den Zeitplan, den Sie für Ihre Testnachricht festgelegt haben. Wenn sie auf Zustellung in der lokalen Zeitzone oder [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) eingestellt ist, haben Sie die Nachricht möglicherweise noch nicht erhalten (oder die App war im Vordergrund, als sie empfangen wurde).

### Nutzer ist für die zu testende App nicht "push-registriert"

Überprüfen Sie das Nutzerprofil des Nutzers, an den Sie eine Testnachricht senden möchten. Die "pushbaren Apps" sollten unter dem Tab **Engagement** aufgelistet sein. Vergewissern Sie sich, dass die App, an die Sie Testnachrichten senden möchten, in dieser Liste enthalten ist. Benutzer werden als "Push-registriert" angezeigt, wenn sie ein Push-Token für eine beliebige App in Ihrem Arbeitsbereich haben, es könnte sich also um ein falsches Positiv handeln.

Das Folgende deutet auf ein Problem mit der Push-Registrierung hin oder darauf, dass das Token des Benutzers von den APNs nach dem Push-Vorgang als ungültig an Braze zurückgegeben wurde:

![Ein Benutzerprofil, das die Kontakteinstellungen eines Benutzers anzeigt. Unter Push werden "Keine Apps" angezeigt.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Nicht protokollierte Push-Klicks {#push-clicks-not-logged}

- Stellen Sie sicher, dass Sie die [Schritte zur Push Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling) durchgeführt haben.
- Braze verarbeitet keine Push-Benachrichtigungen, die still im Vordergrund empfangen werden (Standardverhalten von Push im Vordergrund vor dem Framework `UserNotifications`). Das bedeutet, dass Links nicht geöffnet werden und Push-Klicks nicht protokolliert werden. Wenn das Framework `UserNotifications` noch nicht in Ihrer Anwendung integriert ist, verarbeitet Braze keine Push-Benachrichtigungen, wenn der Anwendungsstatus `UIApplicationStateActive` lautet. Stellen Sie sicher, dass Ihre App die Aufrufe von [Push-Verarbeitungsmethoden]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling) nicht verzögert. Andernfalls kann es sein, dass das Swift SDK Push-Benachrichtigungen als stille Push-Events im Vordergrund behandelt und sie nicht verarbeitet.

## Nicht funktionierende Deeplinks

### Weblinks von Push-Klicks werden nicht geöffnet

Links in Push-Benachrichtigungen müssen ATS-konform sein, damit sie in Webansichten geöffnet werden können. Stellen Sie sicher, dass Ihre Web-Links HTTPS verwenden. Weitere Informationen finden Sie in unserem Artikel zur [ATS-Konformität]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#app-transport-security-ats).

### Deeplinks von Push-Klicks werden nicht geöffnet

Der Großteil des Codes, der Deeplinks setzt, verarbeitet auch Push-Öffnungen. Stellen Sie zunächst sicher, dass Push-Öffnungen protokolliert werden. Wenn nicht, [beheben Sie das Problem](#push-clicks-not-logged) (hierdurch wird oftmals auch die Linkverarbeitung korrigiert).

Wenn Öffnungen protokolliert werden, prüfen Sie, ob es sich um ein Problem mit Deeplinks im Allgemeinen oder nur mit Deeplinks bei der Verarbeitung von Push-Klicks handelt. Um dies herauszufinden, testen Sie per Klick auf eine In-App-Nachricht, ob ein Deeplink funktioniert.

