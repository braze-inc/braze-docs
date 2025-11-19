---
nav_title: Test-Leinwände verschicken
article_title: Test-Canvase verschicken
page_order: 1
description: "In diesem Referenzartikel erfahren Sie, wie Sie ein Canvas vor dem Start testen und wie Sie dabei am besten vorgehen."
page_type: reference
tool: Canvas
---

# Test-Leinwände verschicken

> Nachdem [Sie Ihr Canvas erstellt haben]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), sollten Sie vor dem Start mehrere Prüfungen durchführen, je nach Details wie der Größe Ihrer Zielgruppe oder der Anzahl der Segmentierungsfilter.

Wenn möglich, empfiehlt Braze, ein Canvas vor dem Start zu testen. Dieser Test findet normalerweise in Ihrer Braze-Umgebung statt. Das Testen Ihres Canvas kann beinhalten, dass Sie es duplizieren, Testnutzer:innen durch die User Journey führen und prüfen, ob das Verhalten der Nutzer:innen mit dem übereinstimmt, was Sie in Ihrem Canvas skizziert haben.

## Schritt 1: Erstellen Sie Ihren Testplan

Bevor Sie mit dem Testen Ihres Canvas beginnen, müssen Sie einen Testplan erstellen. Ein Testplan kann helfen, bestimmte Bereiche Ihrer Canvas-Reise zu identifizieren und zu tracken.

Wenn Sie Ihren Testplan erstellen, sollten Sie die folgenden Fragen berücksichtigen:
- Wurde für jeden Canvas-Zweig und Pfad mindestens ein Benutzer erstellt?
- Werden in Ihrem Canvas irgendwelche Segmente verwendet? 
	- Wenn Segmente verwendet werden, kann es sein, dass ein:e Nutzer:in erst in den Canvas fallen muss, bevor sie:er für eine User Journey in Frage kommt.
- Enthalten die Nachrichten im Test-Canvas irgendwelche Liquids in den Nachrichtentiteln, die auf die ID oder E-Mail-Adresse der Nutzerin oder des Nutzers verweisen, um sicherzustellen, dass sowohl die Nachricht als auch die:der Nutzer:in zu Testzwecken leicht zu identifizieren sind?

## Schritt 2: Identifizieren Sie Testnutzer:innen

Als Nächstes bestimmen Sie eine Reihe von Testnutzer:innen, die die Canvas-Schritte durchlaufen, ohne tatsächlich Nachrichten an Ihre Nutzer:innen zu senden. Bei den Testbenutzern kann es sich entweder um bestehende E-Mail-Adressen handeln, die nicht für die eigentlichen Dienste auf Ihrem Braze-Dashboard verwendet werden, oder um neue E-Mail-Adressen, die ausschließlich zu Testzwecken verwendet werden. 

## Schritt 3: Richten Sie Ihr Canvas ein

Als Nächstes ist es an der Zeit, Ihr Canvas zu testen! Um die Informationen Ihres Original-Canvas und des Test-Canvas zu organisieren, erstellen Sie zu Testzwecken ein Duplikat Ihres Canvas.

Es gibt zwei Möglichkeiten, wie Sie Ihr Canvas testen können. 

- **Methode 1:** Bearbeiten Sie in dem duplizierten Canvas den Teil **Entry-Zielgruppe** des Canvas-Builders so, dass nur Testnutzer:innen für das Canvas in Frage kommen. Sie können auch Ihre eigene E-Mail-Adresse als Testnutzer:in eingeben, indem Sie den Testfilter **E-Mail-Adresse** hinzufügen. Im folgenden Beispiel haben wir den Canvas auf zwei Testnutzer:innen beschränkt, die die App vor weniger als drei Tagen zum ersten Mal verwendet haben.

![Ein Canvas mit der Zielgruppe "Diese Apps wurden vor weniger als 3 Tagen zum ersten Mal verwendet" und den E-Mail-Adressen von zwei Testnutzer:innen.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Methode 2:** [Zeigen Sie Ihre Benutzerpfadein der Vorschau an]({{site.baseurl}}/preview_user_paths/), indem Sie in der Fußzeile des Canvas-Builders auf die Schaltfläche **Canvas testen** klicken.

## Schritt 4: Starten Sie Ihren Test

Starten Sie Ihr Test Canvas, damit Nutzer:innen mit der Eingabe beginnen können. Vervollständigen Sie die Nutzer:in Ihrer Anwendung, die die Nutzer:innen durch die jeweilige Canvas-Reise schicken würden.

Vergewissern Sie sich, dass Ihre Testbenutzer die gewünschten Nachrichten von Ihren Canvas-Schritten erhalten. Beachten Sie, dass Ihre Testnutzer:innen aus verschiedenen Gründen möglicherweise keine Nachricht erhalten:

- Nicht teilnahmeberechtigt an der Globalen Kontrollgruppe
- Einschränkungen bei der Frequenzbegrenzung
- Nicht übereinstimmende Segmentzugehörigkeit
- Abgebrochene Nachrichten
- Push-Tokens, die mit verschiedenen Benutzern verbunden sind

Setzen Sie die Iteration der Canvas-Tests fort, um sicherzustellen, dass Ihr Canvas die beabsichtigte Performance aufweist.

## Allgemeine Tipps

### Bezeichnen Sie Ihre Canvas-Schritte

In einigen Fällen kann ein:e Nutzer:in beim Durchlaufen eines Canvas möglicherweise mehrere Nachrichten erhalten. Wenn die Verzögerung zwischen den Schritten zum Testen deutlich verringert wurde, ist möglicherweise nicht immer klar, welche Nachricht während des Testens ausgelöst wird. Wenn Sie sicherstellen, dass die Testnachrichten den Schrittnamen oder die Benutzer-ID (mit Liquid) enthalten, können Sie leichter feststellen und bestätigen, ob die richtige Nachricht an die richtigen Benutzer gesendet wurde.

### Eine interne Gruppe erstellen

Anstatt einzelne Testbenutzer zu erstellen, können Sie eine [Inhalts-Testgruppe]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) erstellen, d.h. eine interne Gruppe, deren Zweck es ist, den Inhalt Ihrer Nachricht zu überprüfen. Dazu gehört eine Gruppe von Nutzern, die Testnachrichten von Kampagnen und Canvases erhalten werden. Dann können Sie diese Testgruppe in das Feld **Inhaltstestgruppen hinzufügen** unter **Testempfänger** hinzufügen.

### Reduzieren Sie Zeitverzögerungen

Um Tests effizienter durchführen zu können, empfehlen wir Ihnen, die Zeitverzögerung zu Testzwecken auf Minuten oder Sekunden zu reduzieren, damit Sie Nachrichten zeitnah anzeigen können. Lassen Sie z. B. mindestens 2-3 Minuten zwischen den Tests zu, damit Sie bestimmte Aktionen auf bestimmte Canvas-Reisen isolieren können.

### Content-Blöcke nutzen

Wenn sich Inhalte in Ihrem Test-Framework wiederholen sollen (z.B. komplexes Liquid zum Filtern von Benutzern in verschiedenen Canvas-Schritten), sollten Sie diese wiederholten Inhalte als [Inhaltsblock]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) speichern. Jetzt können Sie den Inhaltsblock in die einzelnen Canvas-Schritte einbinden.

### Verwenden Sie Postman und den Tracking Endpunkt für Nutzer:innen

Sie können Tests mit Postman und der [Braze Postman Collection]({{site.baseurl}}/api/postman_collection/) durchführen. Verwenden Sie den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), um angepasste Events und Käufe für Ihre verschiedenen Testnutzer:innen aufzuzeichnen und zu tracken.

Beachten Sie, dass das Senden von Daten an die Nutzer:in Tracking API nur mit einer externen ID möglich ist. Daher müssen Testnutzer:innen einer internen Gruppe im Braze-Dashboard als Testnutzer:in hinzugefügt werden, damit bestimmte Fehler weiter untersucht werden können. 

#### Tests für mehrere Branches

Wenn Sie ein Canvas mit mehreren Zweigen testen, die Nutzer:innen auf der Grundlage verschiedener Attribute und Events zusammenstellen, folgen Sie diesem Testplan:

1. Ermitteln Sie für jeden Branch die Attribute und Events, über die die:der Nutzer:in verfügen muss, um in die Canvas-Reise aufgenommen zu werden.
2. Bauen Sie diese in JSON-Nutzdaten auf, die über den Endpunkt `/users/track` gepostet werden.

