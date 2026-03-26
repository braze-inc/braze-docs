---
nav_title: FAQs
article_title: Push-FAQs
page_order: 25
description: "Dieser Artikel behandelt einige der am häufigsten gestellten Fragen, die bei der Einrichtung von Push-Kampagnen auftreten."
page_type: FAQ
channel:
  - Push
---

# Häufig gestellte Fragen

> In diesem Artikel finden Sie Antworten auf einige häufig gestellte Fragen zum Push-Kanal.

### Was passiert, wenn sich mehrere Nutzer:innen an einem einzelnen Gerät anmelden?

Wenn sich ein:e Nutzer:in von einem Gerät oder einer Website abmeldet, bleibt er/sie per Push erreichbar, bis sich ein:e andere:r Nutzer:in anmeldet. Zu diesem Zeitpunkt wird das Push-Token dem/der neuen Nutzer:in neu zugewiesen. Das liegt daran, dass jedes Gerät nur ein aktives Push-Abo pro App oder Website haben kann.

Wenn ein Push-Token neu zugewiesen wird, wird die Änderung im **Push Changelog** des Nutzerprofils angezeigt. Sie finden dies unter dem Tab **Engagement** im Nutzerprofil.

![Das „Push Changelog" im Abschnitt „Contact Settings".]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### Wenn ich einen Test-Push sende, wird er an alle meine Geräte gesendet?

Ja. Der Test-Push wird an jedes Push-fähige Gerät gesendet, das mit dem ausgewählten Nutzerprofil verknüpft ist. Wenn Sie mehrere Telefone oder Tablets haben, die mit demselben Nutzerprofil angemeldet sind, erhält jedes Gerät mit einem gültigen Push-Token die Benachrichtigung.

Um den Test-Push nur an ein Gerät zu senden, können Sie vor dem Testen die Push-Token für die anderen Geräte aus dem Nutzerprofil entfernen. Alternativ können Sie beim Senden über den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) `send_to_most_recent_device_only` im `apple_push`- oder `android_push`-Objekt auf `true` setzen, sodass nur das zuletzt aktive Gerät den Push erhält.

### Was bedeutet „Fehler beim Senden der Push-Benachrichtigung, da die Nutzlast ungültig war"?

Diese Nachricht weist darauf hin, dass APNs die Push-Anfrage aufgrund einer ungültigen Nutzlast abgelehnt hat (z. B. eine leere Nutzlast oder eine zu große Nutzlast).

Weitere Informationen und nächste Schritte finden Sie unter [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_error_codes/).

### Warum hat ein:e Nutzer:in mit Opt-in kein Push-Token?

Dies kann passieren, wenn das Push-Token des/der Nutzers/Nutzerin einer anderen Person zugewiesen wurde, die dasselbe Gerät verwendet hat.

1. Gehen Sie zum **Push Changelog** im Tab **Engagement** des Profils des/der betroffenen Nutzers/Nutzerin.
2. Suchen Sie nach einer Nachricht, die besagt, dass das Push-Token auf eine:n andere:n Nutzer:in übertragen wurde.
3. Kopieren Sie das Push-Token und fügen Sie es in die Leiste für die Nutzersuche ein. 
4. Wenn das Push-Token noch existiert, werden Sie zu dem/der Nutzer:in weitergeleitet, der/die sich zuletzt auf dem Gerät angemeldet hat.

Wenn Sie möchten, dass das Push-Token dem/der ursprünglichen Nutzer:in wieder zugewiesen wird:

1. Lassen Sie den/die ursprüngliche:n Nutzer:in sich bei dem Profil mit dem fehlenden Push-Token anmelden.
2. Triggern Sie einen neuen Push-Versand. Dadurch wird das Token zurück auf das Konto übertragen, sofern Push auf Geräteebene noch aktiviert ist.

### Was ist der Unterschied zwischen „Send to Production" und „Send to Development" bei iOS-Push-Zertifikaten?

Beim Hinzufügen eines Apple-Push-Zertifikats in Braze bestimmen die Optionen **Send to Production** und **Send to Development**, welches APNs-Gateway (Apple Push Notification Service) Braze für die Zustellung von Push-Benachrichtigungen verwendet:

- **Send to Development:** Wählen Sie diese Option, wenn die App im Entwicklungsmodus in Xcode erstellt und mit einem Entwicklungs-Provisioning-Profil signiert wurde. Push-Benachrichtigungen werden über Apples Entwicklungs-Gateway (Sandbox) geroutet.
- **Send to Production:** Wählen Sie diese Option, wenn die App über Apples TestFlight, den App Store oder die Enterprise-Distribution verteilt wird. Push-Benachrichtigungen werden über Apples Produktions-Gateway geroutet.

Wenn die falsche Option ausgewählt wird, schlagen Push-Benachrichtigungen stillschweigend fehl, da der Push-Token-Typ nicht zum Gateway passt. In der Regel sollten Apps, die über TestFlight oder den App Store verteilt werden, **Send to Production** verwenden.