---
nav_title: Testen
article_title: Inhaltskarten testen
page_order: 3
description: "In diesem Referenzartikel erfahren Sie, wie Sie Content-Cards in der Vorschau anzeigen und testen können, sowie einige bewährte Praktiken."
channel:
  - content cards
  
---

# Inhaltskarten testen

> Es ist äußerst wichtig, dass Sie Ihre Content-Cards immer testen, bevor Sie Ihre Kampagnen versenden. Unsere Vorschau- und Testfunktionen bieten zwei Möglichkeiten, einen Blick auf Ihre Content Cards zu werfen. Sie können Ihre Nachricht in der Vorschau anzeigen, um sie zu visualisieren, während Sie sie verfassen, und eine Testnachricht an sich selbst oder an das Gerät eines bestimmten Benutzers senden. Wir empfehlen Ihnen, beides in Anspruch zu nehmen.

## Vorschau

Sie können eine Vorschau Ihrer Karte anzeigen, während Sie sie zusammenstellen. So können Sie sich ein Bild davon machen, wie Ihre endgültige Nachricht aus der Sicht des Benutzers aussehen wird.

Auf der Registerkarte **Vorschau** Ihres Composers ist die Ansicht Ihrer Nachricht möglicherweise nicht mit der tatsächlichen Darstellung auf dem Gerät des Benutzers identisch. Wir empfehlen, immer eine Testnachricht an ein Gerät zu senden, um sicherzustellen, dass Ihre Medien, Texte, Personalisierung und benutzerdefinierten Attribute korrekt generiert werden.

## Testen

Um einen Test entweder an [Inhaltstestgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) oder an einzelne Benutzer zu senden, muss Push auf Ihren Testgeräten aktiviert sein und es müssen gültige Push-Token für den Testbenutzer registriert sein, bevor Sie den Test senden. Für iOS Nutzer:innen müssen Sie auf die Push-Benachrichtigung tippen, die von Braze gesendet wird, um die Content-Card für den Test anzuzeigen. Dieses Verhalten gilt nur für Test-Inhaltskarten.

### Nachrichtenvorschau als Nutzer:in anzeigen

Sie können auch auf der Registerkarte **Test** eine Vorschau der Nachrichten anzeigen, als ob Sie ein Benutzer wären. Sie können eine:n bestimmte:n oder zufällige:n Nutzer:in auswählen oder eine:n angepasste:n Nutzer:in erstellen.

\![Eine Content-Card Vorschau im Tab "Test".]({% image_buster /assets/img/cc-user-preview.png %}){: style="max-width:80%;"}

### Test-Checkliste

- Werden die Bilder und Medien angezeigt und verhalten sie sich wie erwartet?
- Funktioniert das Liquid wie erwartet? Haben Sie einen [Standardattribut-Wert ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) für den Fall vorgesehen, dass das Liquid keine Informationen liefert?
- Ist Ihr Text klar, prägnant und korrekt?
- Führen Ihre Links den Benutzer dorthin, wohin er gehen soll?

## Debuggen

Nachdem Ihre Content Cards versendet wurden, können Sie im [Ereignisbenutzerprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) in der Entwicklerkonsole eventuelle Probleme aufschlüsseln oder beheben. 

Ein häufiger Anwendungsfall ist die Fehlersuche, wenn ein:e Nutzer:in eine bestimmte Content-Card nicht sehen kann. Dazu können Sie in den **Event-Nutzerprotokollen** nach den Content-Cards suchen, die dem SDK beim Sitzungsstart, aber vor einer Impression zugestellt wurden, und diese zu einer bestimmten Kampagne zurückverfolgen:

1. Gehen Sie zu **Einstellungen** > **Ereignisbenutzerprotokoll**.
2. Suchen Sie die SDK-Anfrage für Ihren Testbenutzer und erweitern Sie sie.
3. Klicken Sie auf **Rohdaten**.
4. Finden Sie die `id` für Ihre Sitzung. Im Folgenden sehen Sie einen Beispielauszug:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

5. Verwenden Sie ein Dekodierungstool wie [Base64 Decode and Encode](https://www.base64decode.org/), um die `id` aus dem Base64-Format zu dekodieren und die zugehörige `campaign_id` zu finden. In unserem Beispiel ergibt sich daraus folgendes:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Wobei `4861692e-6fce-4215-bd05-3254fb9e9057` die `campaign_id` ist.<br><br>

6. Gehen Sie auf die Seite **Kampagnen** und suchen Sie nach der `campaign_id`.

\![Suchen Sie auf der Seite Kampagnen nach campaign_id ]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

Von dort aus können Sie Ihre Nachrichteneinstellungen und Inhalte überprüfen, um herauszufinden, warum ein Benutzer eine bestimmte Inhaltskarte nicht sehen kann.

