---
nav_title: Wiederzulassung für Kampagne und Canvas
article_title: Wiederzulassung für Kampagne und Canvas
page_order: 3
page_type: reference
description: "Dieser referenzierte Artikel gibt eine Übersicht darüber, was es bedeutet, Nutzern:innen zu erlauben, sich erneut für eine Kampagne oder einen Canvas zu qualifizieren bzw. wieder einzutreten."
tool:
  - Campaigns
  - Canvas

---

# Erneute Qualifizierung mit Kampagnen und Canvas

> Wenn Sie eine wiederkehrende oder ausgelöste Kampagne oder ein Canvas planen, haben Sie die Möglichkeit, Benutzern zu erlauben, sich erneut dafür zu qualifizieren (so dass Benutzer die Kampagne oder das Canvas je nach Auslöser mehrmals betreten können). Standardmäßig sendet Braze eine Nachricht nur einmal an einen Nutzer:innen, auch wenn dieser sich mehrfach qualifiziert hat - die Wiederzulassung muss separat aktiviert werden. 

Wenn Sie die Wiederzulassung aktivieren, setzen Sie dieses Standardverhalten außer Kraft und erlauben qualifizierten Mitgliedern, erneut Nachrichten zu erhalten, nachdem sie die erste Instanz der Kampagne oder des Canvas erhalten haben. Sie können den Zeitrahmen angeben, in dem Nutzer:innen letztendlich wieder zugelassen werden würden.

## Canvas

Um die Wiederzulassung für ein Canvas zu aktivieren, markieren Sie im Abschnitt **Eingabesteuerung** die Option **Benutzern die erneute Eingabe dieses Canvas erlauben**. Sie können wählen, ob Sie Nutzern:innen den Wiedereintritt nach der maximalen Dauer des Canvas oder nach einem bestimmten Zeitfenster erlauben.

![Eingangskontrollen][2]

Die erneute Qualifizierung für Canvas-Varianten ist an den Canvas-Entry und nicht an den Empfang von Nachrichten gebunden. Benutzer, die ein Canvas betreten und keine Nachrichten erhalten, können das Canvas nicht erneut betreten, es sei denn, die Wiederzulassung ist aktiviert. 

Nehmen wir zum Beispiel an, ein Nutzer:innen ohne E-Mail Adresse gibt ein täglich wiederkehrendes Canvas ein, das einen Schritt in der User Journey enthält. Die Canvas-Komponente enthält nur eine E-Mail Nachricht, sodass der oder die Nutzer:in das Engagement nicht erhält. Diese Nutzer:innen können den Canvas nur dann erneut betreten, wenn die Wiederzulassung im Canvas aktiviert ist. Wenn Sie ein aktives wiederkehrendes oder getriggertes Canvas ohne Wiederzulassung haben und möchten, dass Nutzer:innen das Canvas erneut betreten können, bis sie eine Nachricht davon erhalten, können Sie in Erwägung ziehen, Nutzern:innen die Wiederzulassung zu erlauben, indem Sie einen Filter zu den Eingangskriterien hinzufügen, der Kunden ausschließt, die eine Nachricht vom Canvas erhalten haben.

Wenn die erneute Teilnahme an einem Canvas kürzer als die Dauer des Canvas eingestellt ist, ist es möglich, dass Nutzer:innen den Canvas mehr als einmal betreten, was zu einem irreführenden Verhalten bei Canvase führen kann, die In-App-Nachrichten mit besonders langen Verzögerungen verwenden. Da mehrere In-App-Nachrichten von Canvas durch denselben Sitzungsstart getriggert werden können, könnte der oder die Nutzer:in möglicherweise die Erfahrung machen, wiederholt dieselbe Nachricht zu erhalten, wenn eine bestimmte Komponente schneller gerendert wird als andere.

## Kampagnen

Um die Wiederzulassung für eine Kampagne zu aktivieren, wählen Sie im Abschnitt **Zustellungssteuerung** das Kontrollkästchen **Nutzer:innen wieder für den Empfang von Kampagnen zulassen** aus. Die maximale Frist für die erneute Qualifizierung für eine Kampagne beträgt 720 Tage.

![][1]

Bei getriggerten Kampagnen mit aktivierter erneuter Qualifizierung qualifizieren sich Nutzer:innen, die [die Nachricht der Kampagne nicht erhalten haben]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (obwohl sie das Trigger-Event abgeschlossen haben), automatisch für die Nachricht, wenn sie das nächste Mal das Trigger-Event abschließen, auch wenn Sie die Nutzer:innen nicht wieder qualifiziert haben. Das liegt daran, dass die erneute Qualifizierung auf dem Empfang der Nachrichten und nicht auf dem Kampagnen-Entry beruht. Wenn Sie Nutzern die Möglichkeit geben, sich erneut für eine ausgelöste Kampagne zu qualifizieren, ermöglichen Sie ihnen, die Nachricht mehr als einmal zu erhalten (und nicht nur auszulösen).

Wenn Sie außerdem versuchen, eine Nachricht mit einer Wiederholungsfrist von null Minuten sofort zu versenden, werden wir immer versuchen, sie sofort zu planen, unabhängig davon, wie ein Benutzer frühere Versionen der Kampagne oder Canvas erhalten hat.

![][24]

## Berechnungen der Verzögerung bei der Wiedererlangung der Anspruchsberechtigung

Die erneute Qualifizierung von Kampagnen und Canvase wird in Sekunden und nicht in Kalendertagen berechnet. Das bedeutet, dass ein Tag als 24 Stunden (oder 86.400 Sekunden) ab dem Zeitpunkt gezählt wird, an dem ein Benutzer die Nachricht erhält, und nicht der nächste Kalendertag um Mitternacht.

In ähnlicher Weise zählt ein Monat genau 2.592.000 Sekunden, was ungefähr 30 Tagen entspricht.

### Anwendungsfall

Betrachten Sie das folgende Szenario:
* Eine Kampagne soll monatlich am 15\. gesendet werden, wobei die erneute Qualifizierung auf 30 Tage festgelegt ist.
* Zwischen dem 15\. Februar und dem 15\. März liegen weniger als 30 Tage. 

Das bedeutet, dass Nutzer, die die Kampagne am 15\. Februar erhalten haben, nicht für die am 15\. März zu versendende Kampagne in Frage kommen.

Wenn die Kampagne so eingestellt ist, dass sie täglich um 8 Uhr mit einer Wiederzulässigkeit von 1 Tag versendet wird und es eine Latenzzeit bei der Versendung der Nachricht gibt, sind Nutzer:innen, die die Kampagne z.B. um 8:30 Uhr erhalten haben, am nächsten Tag um 8 Uhr noch nicht wieder zulassungsfähig.

## Mehrvariantentests

In Bezug auf multivariate Tests bestimmt Braze die erneute Qualifizierung von Varianten für alle Kampagnen, getriggerten In-App-Nachrichten und Canvase anhand der folgenden Regeln:

- Wenn die prozentualen Anteile der Varianten nicht geändert werden, wird jede/r Nutzer:in immer dieselbe Variante einer Kampagne, einer getriggerten In-App-Nachricht oder eines Canvas-Entry eingeben, wenn er oder sie sich erneut qualifiziert.
- Wenn sich die Prozentsätze der Varianten ändern, werden die Nutzer:innen möglicherweise auf andere Varianten umverteilt.
- Die Kontrollgruppen bleiben konsistent, wenn der Variantenprozentsatz unverändert bleibt. Kein Benutzer, der zuvor eine Nachricht erhalten hat, wird bei einem späteren Versand in die Kontrollgruppe aufgenommen, und kein Benutzer in der Kontrollgruppe wird jemals eine Nachricht erhalten.

[1]: {% image_buster /assets/img_archive/reeligibility_controls_campaign.png %}
[2]: {% image_buster /assets/img_archive/reeligibility_controls_canvas.png %}
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
