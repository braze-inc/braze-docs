---
nav_title: A/B-Test Projektion
article_title: A/B-Test Projektion
page_order: 20
hidden: true
page_type: reference
description: "Dieser Artikel erklärt, wie A/B-Testprojektionen funktionieren, wie Sie eine Projektion durchführen und wie Braze Ihre Daten verwendet."
---

# A/B-Test Projektion

> Die A/B-Testprojektion verwendet neuronale Netzwerke, um vorherzusagen, welche Betreffzeilen am besten funktionieren. Unser Modell extrahiert linguistische Merkmale aus erfolgreichen A/B-Tests, die auf Braze durchgeführt wurden, und verwendet diese statistischen Sprachmuster, um unserer KI beizubringen, welche Betreffzeilen besser sind.

{% alert important %}
Diese Funktion befindet sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Braze Customer-Success-Manager oder Account Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind.
{% endalert %}

## Ausführen einer Projektion

Fügen Sie bei der Kampagnengestaltung Ihre Nachrichtenvarianten und deren Betreffzeilen in den Editor ein. Wenn Sie fertig sind, gehen Sie zum Schritt **Zielgruppe** des Kampagnenerstellungsprozesses. Wählen Sie im Fenster **A/B-Tests** die Option **Projektion ausführen**.

<img width="518" alt="Bild" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

Es öffnet sich ein Modal mit den Betreffzeilen aller bereits erstellten Nachrichtenvarianten. Optional können Sie weitere Betreffzeilen einfügen (bis zu maximal zehn), indem Sie eine manuell in das Feld eingeben und die Vorhersage ausführen. Wählen Sie **Projektion ausführen**.

<img width="722" alt="Bild" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

Die Betreffzeile, die unsere KI als die beste vorhersagt, wird mit dem Label **Prognostizierter Gewinner** hervorgehoben.

{% alert note %}
Für [schnelle Push-Kampagnen]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/) werden A/B-Tests unterstützt, wenn Sie mehrere Plattformen auswählen.
{% endalert %}

### Wie genau sind die Prognosen?

In Tests haben wir festgestellt, dass die Projektionen bei der Auswahl zwischen Nachrichtenpaaren in echten A/B-Tests zu etwa 70 % genau sind. Berücksichtigen Sie dies bei der Interpretation der Botschaften, die das Modell vermittelt, um zu gewinnen.

### Wie verwenden wir Ihre Daten?

Diese Funktion lernt aus früheren A/B-Tests, die auf Braze durchgeführt wurden. Die tatsächliche Kopie Ihrer Nachrichten oder der Nachrichten anderer Kunden von Braze wird dem Modell niemals zur Verfügung gestellt. Zunächst extrahieren wir die übergeordneten Sprachmuster, die die Gewinnerbotschaften in A/B-Tests vorhersagen. Dann geben wir diese Muster an unsere KI weiter, damit sie lernt, welche sprachlichen Merkmale bessere Betreffzeilen ausmachen.