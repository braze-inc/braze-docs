---
nav_title: Erneute Qualifizierung
article_title: Erneute Qualifizierung
page_order: 8
page_type: reference
description: "Dieser referenzierte Artikel definiert die Wiederzulassung für Kampagnen und Canvase."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Wiederzulassung für Kampagnen und Canvas

> Wenn Sie einen Zeitplan für eine wiederkehrende oder getriggerte Kampagne oder ein Canvas erstellen, können Sie Nutzern:innen die Möglichkeit geben, sich erneut für diese Kampagne zu qualifizieren. Wiederholbarkeit bedeutet, dass Nutzer:innen die Kampagne oder den Canvas je nach Trigger mehrfach betreten können.

## Funktionsweise

Standardmäßig sendet Braze eine Nachricht nur einmal an einen Nutzer:innen, auch wenn dieser sich mehrfach qualifiziert hat, da die Wiederzulassung separat aktiviert werden muss. Nach der Aktivierung ist es qualifizierten Mitgliedern zulässig, erneut Nachrichten zu erhalten, nachdem sie die erste Instanz der Kampagne oder des Canvas erhalten haben. Sie können den Zeitrahmen angeben, in dem Nutzer:innen letztendlich wieder zugelassen werden würden.

## Wiederwählbarkeit einschalten

{% tabs local %}
{% tab campaign %}
Um die Wiederzulassung für eine Kampagne zu aktivieren, wählen Sie im Abschnitt **Zustellungssteuerung** das Kontrollkästchen **Nutzer:innen wieder für den Empfang von Kampagnen zulassen** aus. Die maximale Frist für die erneute Qualifizierung für eine Kampagne beträgt 720 Tage.

Bei getriggerten Kampagnen mit aktivierter Wiederzulassung werden Nutzer:innen, die [die Nachricht der Kampagne nicht erhalten haben]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (obwohl sie das Trigger-Ereignis abgeschlossen haben), automatisch für die Nachricht qualifiziert, wenn sie das nächste Mal das Trigger-Ereignis abschließen. Das liegt daran, dass die erneute Qualifizierung auf dem Empfang der Nachrichten und nicht auf dem Kampagnen-Entry beruht. Wenn Sie Nutzern die Möglichkeit geben, sich erneut für eine ausgelöste Kampagne zu qualifizieren, ermöglichen Sie ihnen, die Nachricht mehr als einmal zu erhalten (und nicht nur auszulösen).

Wenn Sie außerdem versuchen, eine Nachricht mit einer Wiederholungsfrist von null Minuten sofort zu versenden, werden wir immer versuchen, sie sofort zu planen, unabhängig davon, wie ein Nutzer:innen frühere Versionen der Kampagne oder des Canvas erhalten hat.

#### Erneute Qualifizierung mit API-getriggerten Kampagnen

Die Anzahl, wie oft ein:e Nutzer:in eine über die API getriggerte Kampagne erhält, kann mit den Einstellungen für die erneute Qualifizierung begrenzt werden. Das bedeutet, dass der Benutzer die Kampagne nur einmal oder einmal in einem bestimmten Fenster erhält, unabhängig davon, wie oft der API-Auslöser ausgelöst wird.

Nehmen wir zum Beispiel an, Sie verwenden eine API-getriggerte Kampagne, um dem Nutzer:innen eine Kampagne zu einem Artikel zu schicken, den er kürzlich angesehen hat. In diesem Fall können Sie die Kampagne darauf beschränken, maximal eine Nachricht pro Tag zu senden, unabhängig davon, wie viele Artikel sie angesehen haben, während Sie den API-Trigger für jeden Artikel auslösen. Wenn Ihre API-ausgelöste Kampagne hingegen transaktionsabhängig ist, möchten Sie sicherstellen, dass der Benutzer die Kampagne jedes Mal erhält, wenn er die Transaktion durchführt, indem Sie die Verzögerung auf null Minuten einstellen.
{% endtab %}

{% tab canvas %}

Um die Wiederzulassung eines Canvas zu aktivieren, wählen Sie **Nutzer:innen den erneuten Zugang zu diesem Canvas** im Bereich **Eingangskontrollen**. Sie können wählen, ob Sie Nutzern:innen den Wiedereintritt nach der maximalen Dauer des Canvas oder nach einem bestimmten Zeitfenster erlauben.

Die erneute Qualifizierung für Canvas-Varianten ist an den Canvas-Entry und nicht an den Empfang von Nachrichten gebunden. Benutzer, die ein Canvas betreten und keine Nachrichten erhalten, können das Canvas nicht erneut betreten, es sei denn, die Wiederzulassung ist aktiviert.

Beachten Sie, dass ein Nutzer:innen einen Canvas nicht erst verlassen muss, bevor er ihn erneut betreten kann, wenn die Wiederholbarkeit auf null Sekunden eingestellt ist. Das bedeutet, dass ein Nutzer:innen denselben Canvas erneut betreten kann. Sie können zusätzliche Filter hinzufügen, um zu verhindern, dass Nutzer:innen denselben Schritt oder dieselbe Nachricht mehrfach erhalten. Wenn ein Nutzer:innen jedoch zum zweiten Mal einen Canvas betritt, sind die Schritte, die er beim ersten Mal im Canvas erhalten hat, für ihn nicht sichtbar. Das bedeutet, dass der Nutzer:innen die gleiche Nachricht noch einmal erhalten kann. Um dies zu verhindern, können Sie den Canvas so konfigurieren, dass ein erneuter Eintritt nicht möglich ist, oder die Wiederzulassung für die maximale Dauer des Canvas festlegen.

Sie können auch eine [User Update-Komponente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) für den Nutzer, der den Schritt erhält, verwenden, um dies als angepasstes Attribut zu protokollieren. Damit können Sie Nutzer:innen herausfiltern, die den Schritt während ihrer Canvas-Journey erhalten haben.

### Beispiel

Nehmen wir zum Beispiel an, ein Nutzer:innen ohne E-Mail Adresse gibt ein täglich wiederkehrendes Canvas ein, das einen Schritt in der User Journey enthält. Dieser Schritt enthält nur eine E-Mail Nachricht, so dass der Nutzer:innen das Engagement nicht erhält. Diese Nutzer:innen können den Canvas nur dann wieder betreten, wenn die Wiederzulassung im Canvas aktiviert ist. 

Wenn Sie ein aktives wiederkehrendes oder getriggertes Canvas ohne Wiederzulassung haben und möchten, dass Nutzer:innen das Canvas erneut betreten können, bis sie eine Nachricht davon erhalten, können Sie in Erwägung ziehen, Nutzern:innen die Wiederzulassung zu erlauben, indem Sie einen Filter zu den Eingangskriterien hinzufügen, der Kunden ausschließt, die eine Nachricht vom Canvas erhalten haben.

Wenn die erneute Teilnahme an einem Canvas kürzer als die Dauer des Canvas eingestellt ist, ist es möglich, dass Nutzer:innen den Canvas mehr als einmal betreten, was zu einem irreführenden Verhalten bei Canvase führen kann, die In-App-Nachrichten mit besonders langen Verzögerungen verwenden. Da mehrere In-App-Nachrichten von Canvas durch denselben Sitzungsstart getriggert werden können, könnte der oder die Nutzer:in möglicherweise die Erfahrung machen, wiederholt dieselbe Nachricht zu erhalten, wenn eine bestimmte Komponente schneller gerendert wird als andere.
{% endtab %}
{% endtabs %}

## Berechnungen der Verzögerung bei der Wiedererlangung der Anspruchsberechtigung

Die erneute Qualifizierung von Kampagnen und Canvase wird in Sekunden und nicht in Kalendertagen berechnet. Das bedeutet, dass ein Tag als 24 Stunden (oder 86.400 Sekunden) ab dem Zeitpunkt gezählt wird, an dem ein Benutzer die Nachricht erhält, und nicht der nächste Kalendertag um Mitternacht. In ähnlicher Weise zählt ein Monat genau 2.592.000 Sekunden, was ungefähr 30 Tagen entspricht.

### Beispiel

Betrachten Sie das folgende Szenario:

* Eine Kampagne soll monatlich am 15\. gesendet werden, wobei die erneute Qualifizierung auf 30 Tage festgelegt ist.
* Zwischen dem 15\. Februar und dem 15\. März liegen weniger als 30 Tage. 

Das bedeutet, dass Nutzer, die die Kampagne am 15\. Februar erhalten haben, nicht für die am 15\. März zu versendende Kampagne in Frage kommen. Wenn die Kampagne so eingestellt ist, dass sie täglich um 8 Uhr mit einer Wiederzulässigkeit von 1 Tag versendet wird und es eine Latenzzeit bei der Versendung der Nachricht gibt, sind Nutzer:innen, die die Kampagne um 8:30 Uhr erhalten haben, am nächsten Tag um 8 Uhr noch nicht wieder zulassungsfähig.

## Mehrvariantentests

Für multivariate Tests bestimmt Braze die Wiederzulässigkeit von Varianten für alle Kampagnen, getriggerten In-App-Nachrichten und Canvase anhand der folgenden Regeln:

- Wenn die prozentualen Anteile der Varianten nicht geändert werden, wird jede/r Nutzer:in immer dieselbe Variante einer Kampagne, einer getriggerten In-App-Nachricht oder eines Canvas-Entry eingeben, wenn er oder sie sich erneut qualifiziert.
- Wenn sich die Prozentsätze der Varianten ändern, werden die Nutzer:innen möglicherweise auf andere Varianten umverteilt.
- Die Kontrollgruppen bleiben konsistent, wenn der Variantenprozentsatz unverändert bleibt. Kein Benutzer, der zuvor eine Nachricht erhalten hat, wird bei einem späteren Versand in die Kontrollgruppe aufgenommen, und kein Benutzer in der Kontrollgruppe wird jemals eine Nachricht erhalten.

