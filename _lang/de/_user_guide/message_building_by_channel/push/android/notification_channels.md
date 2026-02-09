---
nav_title: "Kanäle für Benachrichtigungen"
article_title: Kanäle für Push-Benachrichtigungen 
page_order: 4
page_type: reference
description: "Dieser Referenzartikel behandelt Themen zu Android-Push-Benachrichtigungskanälen wie den Übergang zu Android O, das Hinzufügen eines Kanals zu Braze, das Einrichten eines Fallback-Kanals und mehr."
platform: Android
channel:
  - push

---

# Kanäle für Benachrichtigungen

> [Benachrichtigungskanäle](https://www.braze.com/blog/android-o-push-notifications-channels/) sind eine Möglichkeit, Push-Benachrichtigungen zu organisieren, die mit Android O hinzugefügt wurde. Ab O müssen alle Push-Benachrichtigungen einen Benachrichtigungskanal haben, der die Art der Nachricht angibt (z. B. "Chat-Benachrichtigungen" oder "Folgen-Benachrichtigungen"). Ihre Nutzer:innen können dann Aspekte ihrer Benachrichtigung (z. B. Schlummern, Geräusch-/Vibrationseinstellungen oder Opt-out usw.) auf der Grundlage einzelner Kanäle steuern.

## Der Übergang zu Android O

Benachrichtigungskanäle können nur im Code Ihrer Anwendung erstellt werden und können nicht programmatisch im Braze Dashboard erstellt werden. Wir empfehlen, dass Ihr technisches Team mit Ihren Marketingfachleuten zusammenarbeitet, um sicherzustellen, dass die gewünschten Benachrichtigungskanäle ordnungsgemäß zum Dashboard hinzugefügt werden.

Ab Android O benötigen Push-Benachrichtigungen einen gültigen Kanal, um angezeigt zu werden. Wenn Ihre App für Android O oder höher ausgelegt ist, müssen Sie Braze SDK Version 2.1.0 oder höher verwenden. Ihr Entwicklungsteam sollte die Kanäle, die Sie verwenden möchten, sowie die vorgeschlagenen Benachrichtigungseinstellungen (z.B. Wichtigkeit, Ton, Licht) für jeden Kanal in Ihrem Anwendungscode definieren. Die Android-Entwicklerdokumentation finden Sie [hier](https://developer.android.com/preview/features/notification-channels.html) und die Entwicklerdokumentation von Braze [hier.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels)

{% alert note %}
Android unterstützt die Lokalisierung von Kanalnamen, so dass Sie im Code Ihrer Anwendung eine Kanal-ID mit mehreren Übersetzungen eines Kanalnamens verknüpfen können.
{% endalert %}

Sobald diese Kanäle erstellt sind, müssen Ihre Techniker die zugehörigen Kanal-IDs an Ihr Marketingteam weitergeben. Ihr Team sollte Ihre Kanalnamen und Kanal-IDs in das Braze Dashboard eingeben, um sie in Ihren Kampagnen und Canvases zu verwenden.

Um einen Kanal zum Braze-Dashboard hinzuzufügen, navigieren Sie zum Android Push Composer, wählen Sie das Feld „Benachrichtigungskanäle“ aus und wählen Sie dann „Kanäle verwalten“.
{% alert important %}
Nur Benutzer mit der Berechtigung "Apps verwalten" können Kanäle verwalten.
{% endalert %}

## SDK Standard-Kanal

Android erfordert einen gültigen Kanal, um Push-Benachrichtigungen auf API-Ebene 26 (Android O) oder höher anzuzeigen. Braze Android SDK 2.1.0 enthält einen Standardkanal namens „Allgemein“, der erstellt und verwendet wird, wenn Sie keine zusätzlichen Kanäle im Dashboard angeben oder wenn Sie versuchen, an einen ungültigen Kanal zu senden. Sie können diese Bezeichnung im SDK umbenennen und eine Beschreibung des Kanals angeben. Wir empfehlen Ihnen, dies zu berücksichtigen, um eine bessere Nutzererfahrung zu gewährleisten.  

Sobald ein Kanal zu Ihrer Anwendung hinzugefügt wurde, können Sie ihn auch wieder entfernen. Verbraucher:in können jedoch immer die Anzahl der Kanäle sehen, die Sie [entfernt] haben.[3] Das Braze-Dashboard bietet keine Unterstützung für die programmatische Erstellung von Kanälen - Kanäle müssen im Code Ihrer Anwendung erstellt und definiert werden, um ein nahtloses Erlebnis zu bieten.

Wir empfehlen Ihnen erneut, sich mit Ihrem Entwicklerteam abzustimmen, um einen nahtlosen Übergang zur Ausrichtung auf Android O zu gewährleisten.

## Ausweichkanal für das Dashboard

Mit Braze können Sie einen Fallback-Kanal für das Dashboard festlegen. Der Zweck des Dashboard-Fallback-Kanals ist die Bereitstellung einer Kanal-ID für ältere Push-Nachrichten ohne explizite Kanalauswahl. Wir definieren eine Kanalauswahl als die Auswahl eines Kanals in unserem Android Push Composer.

Nachrichten, für die kein Kanal ausgewählt wurde, werden mit der Fallback-Kanal-ID des Dashboards gesendet. Wenn Sie Ihren Dashboard-Fallback-Kanal ändern, werden alle Nachrichten, für die nicht explizit ein Kanal ausgewählt wurde, mit der ID des neuen Fallback-Kanals gesendet.

Hier sehen Sie ein Beispiel für das erwartete Verhalten des Dashboard-Fallback-Channels:

Ihr Dashboard-Fallback-Kanal heißt „Marketing“ und Sie haben 10 Android-Push-Nachrichten, für die Sie noch nie einen Kanal ausgewählt haben. Diese Kampagnen werden über den Kanal "Marketing" gesendet, da der Kanal "Marketing" der Fallback-Kanal des Dashboards ist.

Zusätzlich haben Sie 15 Nachrichten, die Sie über den Kanal „Soziale Benachrichtigungen“ senden möchten, und fünf Nachrichten, die Sie über den Kanal „Marketing“ senden möchten.

Sie entscheiden sich dann, den Standardkanal Ihres Dashboards von „Marketing“ in „Updates“ zu ändern.

In diesem Fall werden alle 10 Kampagnen ohne Kanalauswahl, die zuvor über den Kanal "Marketing" gesendet wurden, nun über den Kanal "Updates" gesendet, da diese Nachrichten über den Fallback-Kanal gesendet werden. Die 15 Nachrichten, die über den Kanal "Soziale Benachrichtigungen" gesendet wurden, werden weiterhin über den Kanal "Soziale Benachrichtigungen" gesendet. Die fünf Nachrichten, die über den Kanal „Marketing“ gesendet wurden, werden weiterhin über den Kanal „Marketing“ gesendet.

Falls Braze eine ungültige Kanal-ID bereitgestellt wird (z. B. wenn Sie eine Kanal-ID bereitstellen, die Ihre Entwickler:innen nicht im SDK erstellt haben), senden wir die Benachrichtigung über Ihren SDK-Standardkanal. Daher empfehlen wir Ihnen dringend, Ihre Benachrichtigungskanäle während der Entwicklung über das Dashboard von Braze zu testen.

Um das erwartete Verhalten der Kanäle besser zu verstehen, sehen Sie sich die folgende Tabelle an:

|Szenario |Ergebnis  |    
| ---|-------------
|**Unternehmen ABC** aktualisiert auf ein SDK, das Android O unterstützt<br>**Unternehmen ABC** fügt dem Braze Dashboard keine Kanäle hinzu<br>**Unternehmen ABC** benennt seinen SDK-Standardkanal nicht um | Für Push-Benachrichtigungen, die an Android O-Geräte gesendet werden, wird ein Kanal mit dem Namen "Allgemein" erstellt und die Benachrichtigungen werden über den Kanal "Allgemein" gesendet.
|**Unternehmen XYZ** aktualisiert auf ein SDK, das Android O unterstützt <br>**Unternehmen XYZ** fügt dem Braze Dashboard keine Kanäle hinzu<br>**Unternehmen XYZ** benennt seinen SDK Standard-Kanal in „Marketing“ um. | Für Push-Benachrichtigungen, die an Android O-Geräte gesendet werden, wird ein Kanal namens "Marketing" erstellt und die Benachrichtigungen werden über den Kanal "Marketing" gesendet.
|**Unternehmen LMN** aktualisiert auf ein SDK, das Android O unterstützt <br>**Unternehmen LMN** definiert in seinem Code zwei Kanäle: „Aktionen“ und „Updates für Bestellungen“. <br>**Unternehmen LMN** fügt dem Braze-Dashboard die Kanal-IDs für „Aktionen“ und „Updates für Bestellungen“ hinzu <br>**Unternehmen LMN** benennt „Aktionen“ als Fallback-Kanal für das Dashboard<br>**Unternehmen LMN** benennt seinen SDK-Standard-Kanal in „Marketing“ um. | Push-Benachrichtigungen, die an Android O-Geräte gesendet werden, erstellen keinen Kanal<br><br>Sofern der Marketer nicht ausdrücklich angibt, dass Benachrichtigungen über den Kanal „Bestellaktualisierungen“ oder „Marketing“ gesendet werden sollen, werden alle Benachrichtigungen, die vor dem Hinzufügen der Kanäle zum Dashboard erstellt wurden, über den Kanal „Werbeaktionen“ gesendet.<br><br>Der Standardkanal des SDK, „Marketing“, wird nur erstellt und verwendet, wenn das Unternehmen versucht, eine Benachrichtigung über eine ungültige Kanal-ID zu senden, oder wenn er explizit ausgewählt wird.
|**Unternehmen HIJ** aktualisiert auf Android O, aber nicht auf Braze Android SDK auf 2.1.0 oder höher | Benachrichtigungen, die an Benutzer mit Android O oder höher gesendet werden, erscheinen nicht |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Hinzufügen von Kanälen zum Braze Dashboard

1. Öffnen Sie eine Kampagne oder ein Canvas, das einen Android-Push enthält, und klicken Sie auf **Kampagne bearbeiten**.
2. Navigieren Sie zum Android-Nachrichten-Editor für Push-Nachrichten.
3. Klicken Sie auf **Benachrichtigungskanäle verwalten**. Alle hier hinzugefügten Kanäle sind global für alle Kampagnen und Canvases verfügbar. Sie müssen über die [Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) „Apps verwalten“ für Ihren Arbeitsbereich verfügen, um Kanäle verwalten zu können.

Wenn Sie einen Benachrichtigungskanal auf eine bestimmte Kampagne oder einen Canvas-Schritt anwenden, scheint sich die Anzahl der **erreichbaren Benutzer** (im Schritt Zielgruppe) für Android Push nicht zu ändern. Allerdings sehen nur Benutzer, die den ausgewählten Benachrichtigungskanal abonniert haben, die Nachricht, und Ihre Kampagnenanalyse (z. B. Klicks) wird auf der Grundlage dieser Zielgruppe gemessen.

![]({% image_buster /assets/img_archive/Click_Here.png %})

{:start="4"}
4\. Klicken Sie auf **Benachrichtigungskanal hinzufügen**.
5\. Geben Sie den Namen und die ID des Benachrichtigungskanals ein, den Sie hinzufügen möchten.<br><br>![]({% image_buster /assets/img_archive/Enter_Channel.png %})<br><br>
6\. Wiederholen Sie die Schritte 4 und 5 für jeden Benachrichtigungskanal, den Sie hinzufügen möchten.
7\. Drücken Sie **Speichern**, um Ihre Änderungen zu speichern.

## Festlegen Ihres Fallback-Kanals

Ihr Fallback-Kanal ist der Kanal, über den Braze versucht, Ihre Android-Nachricht zu senden, wenn Sie keinen Kanal für die Nachricht ausgewählt haben. Die einzigen Kampagnen und Canvases, die Android-Nachrichten ohne Kanalauswahl enthalten, sind Kampagnen und Canvases, die erstellt wurden, bevor Ihr Team dem Braze Dashboard Kanäle hinzugefügt hat. Wenn Sie Ihren Fallback-Kanal ändern, wird die Änderung global auf alle Kampagnen und Canvases ohne explizite Kanalauswahl angewendet.

1. Öffnen Sie eine bestehende Kampagne oder ein Canvas.
2. Navigieren Sie zum Android Push Composer.
3. Wählen Sie **Benachrichtigungskanäle verwalten**, nachdem Sie die Optionen für den Benachrichtigungskanal erweitert haben. <br><br>![]({% image_buster /assets/img_archive/Change_Fallback.png %}){: style="max-width:80%;"}<br><br>
4. Fügen Sie den Kanal zum Dashboard hinzu (falls er nicht bereits hinzugefügt wurde).
5. Wählen Sie das Optionsfeld neben dem Kanal, den Sie als Ausweichkanal festlegen möchten.
6. Speichern Sie Ihre Änderungen. Ihre Änderungen werden global übernommen.

## Hinzufügen von Kanälen zu Ihren Android-Push-Nachrichten

1. Navigieren Sie auf einer beliebigen Kampagne oder einem Canvas zum Android Push Composer.
2. Wählen Sie den gewünschten Kanal aus der Dropdown-Liste. Wenn Sie kein Dropdown haben, sondern die folgende Ansicht verwenden, müssen Sie Kanäle hinzufügen, bevor Sie sie für Kampagnen auswählen.

![]({% image_buster /assets/img_archive/No_Select.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels
