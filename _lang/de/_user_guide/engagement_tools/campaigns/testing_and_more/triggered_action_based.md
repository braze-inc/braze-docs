---
nav_title: API-ausgelöste und aktionsbasierte Kampagnen
article_title: Testen von API-getriggerten und aktionsbasierten Kampagnen
page_order: 2
page_type: reference
description: "Dieser Referenzartikel erklärt, wie Sie API-getriggerte und aktionsbasierte Kampagnen testen können."

---

# API-ausgelöste und aktionsbasierte Kampagnen

> Wenn Sie Kampagnen einrichten, ist es immer eine gute Praxis, Ihre Nachrichten vor dem Start zu testen. Dieser Referenzartikel behandelt die Erstellung eines Testbenutzersegments, mit dem Sie API-Anfragen und Nutzdaten prüfen und Zustellbarkeitsprotokolle anzeigen können.

## Schritt 1: Erstellen Sie ein Testbenutzersegment

Die einzige Möglichkeit, das Auslösen einer Kampagne mit der API oder einem benutzerdefinierten Ereignis zu testen, besteht darin, die Kampagne live zu schalten. Im Rahmen der Einführung einer neuen Kampagne empfehlen wir dringend, ein Testnutzersegment zu Kampagnen hinzuzufügen, um die Triggering-Zustellbarkeit zu testen. Damit haben Sie ein Sicherheitsnetz, das sicherstellt, dass eine versehentlich versandte Kampagne nur an interne Nutzer:innen geht.

1. **Testnutzer:innen importieren**<br>Testbenutzer können über eine CSV-Datei oder eine einmalige Stapelabfrage über [Postman]({{site.baseurl}}/api/postman_collection/) in Braze importiert werden. Wir empfehlen, beim Import dieser Nutzer:innen ein angepasstes Attribut in ihren Profilen zu setzen (z. B. `internal_test_user: true`), das zur Erstellung eines Segments für eine Testgruppe verwendet werden kann. <br><br>
2. **Testnutzer:innen als von Braze anerkannte Testnutzer:innen hinzufügen**<br>[Wenn Sie Ihre Testnutzer:innen im Dashboard als von Braze anerkannte Testnutzer:innen markieren]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), haben Sie Zugriff auf die ausführliche Protokollierung für je:den Nutzer:in, so dass Sie API-Anfragen und deren Nutzdaten prüfen und Zustellbarkeitsprotokolle anzeigen können. Anhand dieser Protokolle können Sie feststellen, ob es Probleme bei der Zustellung von Kampagnen an Endbenutzer gab. <br><br>
3. **Segmente erstellen**<br>Um ein Testnutzersegment zu erstellen, legen Sie ein Segment von Nutzer:innen an, bei dem das angepasste Attribut `internal_test_user` auf `true` gesetzt ist. Dieses Segment kann entfernt werden, wenn die Kampagne live geht. 

## Schritt 2: Testen sendet

Als Nächstes können Sie einen Testversand über das Braze-Dashboard durchführen oder Inbox Vision (nur E-Mail) verwenden, um zu sehen, wie das Layout aussehen wird, während die Kampagne noch im Entwurfsmodus ist. Sie können die Kampagne dann an Ihr Testbenutzersegment senden, um zu überprüfen, ob sie sich wie erwartet verhält. Unabhängig davon, ob die Kampagne API-ausgelöst oder aktionsbasiert ist, verwenden Sie Postman, um eine einmalige Anfrage an die Braze-API zu senden und damit die Kampagne auszulösen. 

## Schritt 3: Verwenden Sie die Braze-Protokollierung, um eingehende Ergebnisse zu prüfen

Verwenden Sie die Braze-Protokollierung zur Fehlerbehebung von Problemen beim Triggern, Senden und bei Events. 
- Das [Event-Nutzerprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) zeigt Ihnen die rohen Nutzdaten der API-Trigger-Anfrage, das angepasste Event, das die Kampagne triggert, und alle damit verbundenen Trigger- oder Event-Eigenschaften.
- Das [Protokoll der Nachrichtenaktivität]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) protokolliert alle Fehler und hilft Ihnen zu verstehen, warum eine bestimmte Nachricht nicht zugestellt werden konnte.

## Schritt 4: Entfernen Sie das Testsegment und starten Sie die Kampagne

Sobald die Nachricht ausgelöst und korrekt wiedergegeben wird und alle angeklickten Links registriert sind, können Sie das Segment entfernen und die Kampagne aktualisieren. Wenn Sie es vorziehen, die Kampagne von Grund auf neu zu starten, so dass die wenigen Impressionen der Testnutzer:innen nicht enthalten sind, können Sie die Kampagne duplizieren und ohne das Testnutzersegment neu starten. 
