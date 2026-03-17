---
nav_title: Erneute Qualifizierung
article_title: Erneute Qualifizierung
page_order: 10
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

Wenn Sie versuchen, eine Nachricht sofort mit einer erneuten Berechtigung von null Minuten zu versenden, werden wir stets versuchen, diese umgehend in den Zeitplan aufzunehmen, unabhängig davon, wie ein Nutzer:in frühere Versionen der Kampagne oder von Canvas erhalten hat.

#### Erneute Qualifizierung mit API-getriggerten Kampagnen

Die Anzahl, wie oft ein:e Nutzer:in eine über die API getriggerte Kampagne erhält, kann mit den Einstellungen für die erneute Qualifizierung begrenzt werden. Das bedeutet, dass der Benutzer die Kampagne nur einmal oder einmal in einem bestimmten Fenster erhält, unabhängig davon, wie oft der API-Auslöser ausgelöst wird.

Nehmen wir zum Beispiel an, Sie verwenden eine API-getriggerte Kampagne, um dem Nutzer:innen eine Kampagne zu einem Artikel zu schicken, den er kürzlich angesehen hat. In diesem Fall können Sie die Kampagne so einschränken, dass maximal eine Nachricht pro Tag versendet wird, unabhängig davon, wie viele Artikel angesehen wurden, während der API-Trigger für jeden Artikel ausgelöst wird. Wenn Ihre API-ausgelöste Kampagne hingegen transaktionsabhängig ist, möchten Sie sicherstellen, dass der Benutzer die Kampagne jedes Mal erhält, wenn er die Transaktion durchführt, indem Sie die Verzögerung auf null Minuten einstellen.
{% endtab %}

{% tab canvas %}

Um die Wiederzulassung eines Canvas zu aktivieren, wählen Sie **Nutzer:innen den erneuten Zugang zu diesem Canvas** im Bereich **Eingangskontrollen**. Es ist zulässig, den Nutzer:innen zu gestatten, nach Ablauf der maximalen Dauer des Canvas oder nach einem festgelegten Zeitfenster erneut beizutreten.

Die erneute Qualifizierung für Canvas-Varianten ist an den Canvas-Entry und nicht an den Empfang von Nachrichten gebunden. Benutzer, die ein Canvas betreten und keine Nachrichten erhalten, können das Canvas nicht erneut betreten, es sei denn, die Wiederzulassung ist aktiviert.

Bitte beachten Sie, dass eine Nutzer:in Canvas nicht zuerst verlassen muss, bevor sie es erneut betreten kann, wenn die Wiederzugangsberechtigung auf null Sekunden gesetzt ist. Das bedeutet, dass eine Nutzer:in dasselbe Canvas erneut betreten kann. Ein weiteres Beispiel: Wenn die Canvas-Dauer auf 7 Tage und die Wiederzulassungsfrist auf 3 Tage festgelegt ist, kann eine Nutzer:in den Canvas erneut betreten, bevor sie ihre erste Reise durch ihn abgeschlossen hat.

Sie können zusätzliche Filter hinzufügen, um zu verhindern, dass Nutzer:innen denselben Schritt oder dieselbe Nachricht mehrfach erhalten. Wenn ein Nutzer:in jedoch zum zweiten Mal einen Canvas aufruft, sind die Schritte, die er beim ersten Mal im Canvas erhalten hat, für ihn nicht mehr sichtbar. Dies bedeutet, dass der Nutzer:in möglicherweise dieselbe Nachricht erneut erhält. Um dies zu verhindern, können Sie den Canvas so konfigurieren, dass eine erneute Teilnahme verhindert wird, oder die erneute Teilnahmeberechtigung für die maximale Dauer des Canvas festlegen.

Sie können einen [Benutzeraktualisierungsschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) auch verwenden, damit die Nutzer:innen, die den Schritt erhalten, diesen als angepasstes Attribut protokollieren. Dieses Attribut kann verwendet werden, um Nutzer:innen herauszufiltern, die den Schritt während ihrer Canvas-Reise erhalten haben.

### Beispiel

Nehmen wir zum Beispiel an, ein Nutzer:innen ohne E-Mail Adresse gibt ein täglich wiederkehrendes Canvas ein, das einen Schritt in der User Journey enthält. Dieser Schritt enthält nur eine E-Mail Nachricht, so dass der Nutzer:innen das Engagement nicht erhält. Diese Nutzer:innen können den Canvas nur dann wieder betreten, wenn die Wiederzulassung im Canvas aktiviert ist. 

Wenn Sie ein aktives wiederkehrendes oder getriggertes Canvas ohne Wiederzulassung haben und möchten, dass Nutzer:innen das Canvas erneut betreten können, bis sie eine Nachricht davon erhalten, können Sie in Erwägung ziehen, Nutzern:innen die Wiederzulassung zu erlauben, indem Sie einen Filter zu den Eingangskriterien hinzufügen, der Kunden ausschließt, die eine Nachricht vom Canvas erhalten haben.

Wenn die erneute Teilnahme an einem Canvas kürzer als die Dauer des Canvas eingestellt ist, ist es möglich, dass Nutzer:innen den Canvas mehr als einmal betreten, was zu einem irreführenden Verhalten bei Canvase führen kann, die In-App-Nachrichten mit besonders langen Verzögerungen verwenden. Da mehrere Canvas-In-App-Nachrichten durch denselben Sitzungsstart getriggert werden können, könnte es vorkommen, dass der Nutzer:in dieselbe Nachricht wiederholt erhält, wenn eine bestimmte Komponente schneller als andere gerendert wird.
{% endtab %}
{% endtabs %}

## Berechnungen der Verzögerung bei der Wiedererlangung der Anspruchsberechtigung

Die erneute Berechtigung für Kampagnen und Canvases wird in Sekunden berechnet, nicht in Kalendertagen. Das bedeutet, dass ein Tag als 24 Stunden (oder 86.400 Sekunden) ab dem Zeitpunkt gezählt wird, an dem ein Benutzer die Nachricht erhält, und nicht der nächste Kalendertag um Mitternacht. In ähnlicher Weise zählt ein Monat genau 2.592.000 Sekunden, was ungefähr 30 Tagen entspricht.

### Beispiel

Betrachten Sie das folgende Szenario:

* Eine Kampagne soll monatlich am 15\. gesendet werden, wobei die erneute Qualifizierung auf 30 Tage festgelegt ist.
* Zwischen dem 15\. Februar und dem 15\. März liegen weniger als 30 Tage. 

Das bedeutet, dass Nutzer, die die Kampagne am 15\. Februar erhalten haben, nicht für die am 15\. März zu versendende Kampagne in Frage kommen. Wenn die Kampagne so eingestellt ist, dass sie täglich um 8 Uhr morgens mit einer erneuten Berechtigung von 1 Tag versendet wird und es zu einer Verzögerung beim Versand der Nachricht kommt, sind Nutzer:innen, die die Kampagne um 8:30 Uhr morgens erhalten haben, am folgenden Tag um 8 Uhr morgens noch nicht erneut berechtigt.

## Mehrvariantentests

Für multivariate Tests bestimmt Braze die Wiederzulässigkeit von Varianten für alle Kampagnen, getriggerten In-App-Nachrichten und Canvase anhand der folgenden Regeln:

- Wenn die prozentualen Anteile der Varianten nicht geändert werden, wird jede/r Nutzer:in immer dieselbe Variante einer Kampagne, einer getriggerten In-App-Nachricht oder eines Canvas-Entry eingeben, wenn er oder sie sich erneut qualifiziert.
- Wenn sich die Prozentsätze der Varianten ändern, werden die Nutzer:innen möglicherweise auf andere Varianten umverteilt.
- Die Kontrollgruppen bleiben konsistent, wenn der Variantenprozentsatz unverändert bleibt. Kein Benutzer, der zuvor eine Nachricht erhalten hat, wird bei einem späteren Versand in die Kontrollgruppe aufgenommen, und kein Benutzer in der Kontrollgruppe wird jemals eine Nachricht erhalten.
