---
nav_title: "Zielnutzer:innen"
article_title: Zielgruppen zusammenstellen
page_order: 12
page_type: reference
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Ihre Zielgruppe in Ihrer Kampagne und in den Canvas-Editoren ansprechen können."
tool:
    - Campaigns
    - Canvas
---

# Zielnutzer:innen

> Die Festlegung des Targetings für Ihre Nutzer:innen ist einer der wichtigsten Schritte bei der Erstellung einer Kampagne oder eines Canvas. Wenn Sie verstehen, wie Sie Ihre Zielgruppe auf der Grundlage ihres Verhaltens, ihrer Vorlieben und ihrer demografischen Daten segmentieren können, können Sie Ihr Messaging maßgeschneidert und personalisiert gestalten.

## Erstellen einer Zielgruppe

### Schritt 1: Nutzer:innen auswählen

Unter **Targeting-Optionen** können Sie mit den folgenden Optionen auswählen, welche Nutzer:innen Sie für Ihre Kampagne oder Ihr Canvas ansprechen möchten. Nur die Nutzer:innen, die den von Ihnen festgelegten Kriterien entsprechen, erhalten die Nachricht. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Versand der Nachricht berechnet wird.

{% tabs local %}
{% tab single segment %}
Um Mitglieder eines zuvor erstellten Segments anzusprechen, wählen Sie ein Segment aus der Dropdown-Liste unter **Benutzer ansprechen nach Segment**.
{% endtab %}

{% tab multiple segments %}
Um Benutzer anzusprechen, die in mehrere zuvor erstellte Segmente fallen, fügen Sie mehrere Segmente aus der Dropdown-Liste unter **Benutzer ansprechen nach Segment** hinzu. Die resultierende Zielgruppe besteht aus Nutzer:innen des ersten Segments, des zweiten Segments, des dritten Segments usw.
{% endtab %}

{% tab multiple filters %}
Um Nutzer:innen zusammenzustellen, ohne ein Segment hinzuzufügen, können Sie eine Reihe von Filtern verwenden. Dies ist eine improvisierte Zielgruppe bei der Erstellung von Nachrichten und erlaubt es Ihnen, die Segmentierung zu überspringen, wenn Sie an einmalige Zielgruppen senden.

![Zusätzliche Filter für eine Nachricht, die sich an Nutzer:innen richtet, die eine App innerhalb des letzten Tages geöffnet haben, noch nie eine Kampagne oder einen Canvas-Schritt erhalten haben und vor weniger als 30 Tagen einen Kauf getätigt haben.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab segments & filters %}
Sie können auch Nutzer:innen aus einem oder mehreren zuvor erstellten Segmenten zusammenstellen, die ebenfalls unter zusätzliche Filter fallen. Nachdem Sie zunächst Ihre Segmente ausgewählt haben, können Sie Ihre Zielgruppe im Abschnitt **Zusätzliche Filter** weiter verfeinern. Dies wird im folgenden Screenshot veranschaulicht. Das Targeting zielt auf Nutzer:innen ab, die im Segment "Täglich aktive:r Nutzer:in" sind, im Segment "Niemals geöffnete E-Mail" und vor mehr als 30 Tagen einen Kauf getätigt haben.

![Targeting-Optionen für eine Nachricht, die zwei Segmente umfasst und einen zusätzlichen Filter für einen letzten Kauf vor weniger als 30 Tagen beinhaltet.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Specific apps %}

Sie können eine Kampagnen-Nachricht oder einen Canvas-Schritt an bestimmte Apps zustellen, z. B. eine In-App-Nachricht oder Push-Benachrichtigung nur an Android- oder iOS-Apps senden.

Denken Sie jedoch daran, dass ein Nutzer:innen mehrere Apps verwenden kann. Der Filter "Hat App" identifiziert alle Nutzer:in, die die ausgewählte App haben, steuert aber nicht, welche Nutzer:innen Nachrichten erhalten. Wenn Sie zum Beispiel einen Segment-Filter anwenden, bei dem "Hat App" auf Android eingestellt ist, erhalten alle Nutzer:innen, die auch die iOS-App haben, die Nachricht auch auf ihrer iOS-App.

![Ein Filter für Nutzer:innen, die die App „Hello, World (Android)“ besitzen.]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Nehmen wir an, Sie möchten eine In-App-Nachricht nur an Android-Apps senden.

1. Erstellen Sie ein Segment und legen Sie **Apps und Websites** fest, die auf **Nutzer:innen bestimmter Apps** abzielen, und wählen Sie dann Ihre Android-App aus.

![Ein Segment, das Nutzer:innen einer bestimmten App anspricht,/assets/img_archive/app_test_android.pngimage_buster"Test_Android".]({%    %}){: style="max-width:60%;"}

{: start="2"}
2\. Gehen Sie in Ihrer Kampagne oder in Canvas zum Schritt **Zielgruppen** und bestätigen Sie, dass Ihr Segment im Abschnitt **Nutzer:innen nach Segmenten** zusammengestellt ist. 

![Der Schritt „Zielgruppen“ mit einem ausgewählten Beispielsegment.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Dies funktioniert nicht, wenn Sie Ihr Segment im Abschnitt **Zusätzliche Filter** über einen Filter für die Segmentzugehörigkeit hinzufügen. Sie müssen Ihr Segment in **Target Users By Segment** direkt referenzieren, um Ihre Nachricht nur an diese App zuzustellen.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Für E-Mail-Kampagnen können Sie Seed-Gruppen unter dem Abschnitt **Seed-Gruppen** gezielt ansprechen. Beachten Sie, dass Seed-Gruppen nicht für API-Kampagnen verfügbar sind, obwohl Sie Seed-Gruppen über einen API-getriggerten Entry in eine Kampagne aufnehmen können. Weitere Informationen finden Sie unter [Saatgutgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).
{% endalert %}

### Schritt 2: Testen Sie Ihre Zielgruppe

Nachdem Sie Ihrer Zielgruppe Segmente und Filter hinzugefügt haben, können Sie testen, ob Ihre Zielgruppe wie erwartet eingerichtet ist, indem Sie [nach einem Benutzer suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), um zu überprüfen, ob er den Kriterien der Zielgruppe entspricht.

![Der Abschnitt „Benutzersuche“ mit dem Button „Nutzer:innen suchen“.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Zusammenfassung der Zielgruppe

Die **Zielgruppenübersicht** gibt Ihnen eine Übersicht über die Personen, die zu Ihrer Zielgruppe gehören. Hier können Sie Ihre Zielgruppe weiter einschränken, indem Sie eine maximale Nutzer:innen-Begrenzung oder eine [Rate-Limiting-Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) festlegen.

![Der Abschnitt „Zielgruppenübersicht“ mit Optionen zur Festlegung einer maximalen Anzahl an Nutzer:innen oder von Rate-Limits für die Zustellung.]({% image_buster /assets/img_archive/audience_summary.png %})

#### A/B-Tests

Im Bereich **A/B-Tests** können Sie einen Test einrichten, um die Reaktionen der Nutzer:innen auf mehrere Versionen der gleichen Marketing-Kampagne zu vergleichen. Diese Versionen haben ähnliche Marketingziele, unterscheiden sich aber in Wortlaut und Stil. Ziel ist es, die Version der Kampagne zu ermitteln, die Ihre Marketingziele am besten erreicht. 

Weitere Informationen und bewährte Verfahren werden in der Referenz zu [Multivariate&A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) angegeben.

#### Zielgruppe Statistik

Braze bietet in der Fußzeile detaillierte Statistiken zu den Zielgruppen der Kanäle. Je größer Ihre Nutzerbasis ist, desto wahrscheinlicher ist die Anzahl der **erreichbaren Nutzer** eine grobe Schätzung. Die Anzahl der erreichbaren Benutzer kann sich verringern, wenn Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) verwenden oder die Berechtigung für Nachrichten einrichten. 

- Um eine genaue Zahl für Ihre erreichbaren Nutzer zu ermitteln, wählen Sie [Exakte Statistik berechnen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) aus, denn damit werden alle Nutzer:in Ihrer Nutzerbasis durchsucht.
- Um zu sehen, welcher Prozentsatz Ihrer Nutzerbasis angesprochen wird oder wie hoch der Lifetime Value (LTV) für dieses Segment ist, wählen Sie **Zusätzliche Statistiken anzeigen**.

##### Warum die Anzahl der Zielgruppen von der Anzahl der erreichbaren Nutzer:innen abweichen kann

{% multi_lang_include segments.md section='Differing audience size' %}

![Der Abschnitt „Gesamtbevölkerung“ enthält geschätzte Zahlen für erreichbare Nutzer:innen in jedem Zielkanal.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
Die Berechnung der genauen Statistiken kann einige Minuten in Anspruch nehmen. Diese Funktion berechnet die genauen Statistiken nur auf Segmentebene, nicht auf Filter- oder Filtergruppenebene.<br><br>
Bei großen Segmenten ist es normal, dass selbst bei der Berechnung exakter Statistiken leichte Abweichungen auftreten. Es wird erwartet, dass die Genauigkeit dieses Features 99,999 % oder mehr beträgt.
{% endalert %}

## Wie Zielgruppen und Zugangsvoraussetzungen zusammenwirken

Wenn Sie eine Kampagne oder ein Canvas in Braze erstellen, erfolgt das Targeting in zwei Schritten:

1. **Zielgruppe:** Wer ist berechtigt?
2. **Teilnahmebedingungen:** Was triggert die Zustellung?

Die Reihenfolge ist von Bedeutung: Braze überprüft, ob eine Person zur Zielgruppe gehört, bevor die Zugangskriterien bewertet werden. Wenn eine Nutzer:in zu diesem Zeitpunkt noch nicht für die Zielgruppe qualifiziert ist, wird sie nicht in die Kampagne oder Canvas aufgenommen, selbst wenn sie später das Eintrittsereignis triggert. Stellen Sie sich die Zielgruppe als einen Warteraum vor: Nur Nutzer:innen, die sich bereits im Raum befinden, wenn der Auslöser aktiviert wird, können fortfahren.

### Beispiel 1

Sie möchten während der ersten Sitzung eines Nutzers eine Push-Nachricht senden.

Sie haben festgelegt:

- **Zielgruppe:** Nutzer:innen mit Sitzungsanzahl = 0
- **Eingangsereignis:** Beginn der Sitzung

Bei der Öffnung der App durch den Nutzer erkennt Braze, dass seine Sitzungsanzahl nun 1 beträgt – und er nicht mehr für die Zielgruppe qualifiziert ist. Der Eingang erfolgt erst, nachdem sie teilnahmeberechtigt sind, daher wird die Nachricht nicht versendet.

Damit dies funktioniert, muss der Nutzer:in vor Beginn der Sitzung die Voraussetzungen für die Zielgruppe erfüllen (Zielgruppe und Auslöser für den Eintritt umkehren).

### Beispiel 2

Sie möchten eine E-Mail an Nutzer:innen senden, die in den letzten 7 Tagen mehr als 10 $ ausgegeben haben.

Sie haben festgelegt:

- **Zielgruppe:** Nutzer:innen, die in den letzten 7 Tagen mehr als 10 Dollar ausgegeben haben
- **Eingangsereignis:** Jeder Kauf

Stellen Sie sich nun vor, eine Nutzer:in gibt heute 12 Dollar aus. Dies triggert die Nachricht nicht – es macht sie lediglich berechtigt, Teil der Zielgruppe zu werden. Sie werden die E-Mail nur erhalten, wenn sie später einen weiteren Kauf tätigen.

Ein besserer Ansatz wäre es, eine breitere Zielgruppe anzusprechen und den Filter in die Zulassungskriterien zu integrieren:

- **Zielgruppe:** Alle Nutzer:innen (bzw. Ihre Kernzielgruppe)
- **Eingangsereignis:** Einen Kauf tätigen
- **Eingangsfilter:** Gesamtausgaben in den letzten 7 Tagen > 10 $

Auf diese Weise erfüllt ein qualifizierter Kauf sowohl den Filter als auch triggert die Nachricht – es ist keine zweite Aktion erforderlich.

## Bewährte Praktiken

- Bitte stellen Sie sicher, dass das Segment der Nutzer:innen umfasst, bevor die Einstiegskriterien erfüllt sind.
- Bitte vermeiden Sie die Verwendung von Zielgruppen-Filtern, die erst nach Ihrer Veranstaltung angewendet werden. Wenn ein Filter von einem Ereignis zum Zeitpunkt der Auslösung abhängt (z. B. „Sitzungsanzahl = 0“), erfüllt die Nutzer:in möglicherweise zum Zeitpunkt der Überprüfung durch Braze nicht mehr die Voraussetzungen.
- Bitte setzen Sie zeitbasierte Logik mit Bedacht ein. Wenn Sie beispielsweise neue Nutzer:innen ansprechen möchten:
    - Bitte stellen Sie Ihre Zielgruppe auf „App, die innerhalb der letzten 7 Tage zum ersten Mal verwendet wurde“ ein.
    - Bitte stellen Sie Ihr Eingangsevent auf „Sitzungsbeginn“ ein.
    - Auf diese Weise sind nur Nutzer:innen, die sich noch in ihrer ersten Woche befinden, teilnahmeberechtigt und nehmen teil, wenn sie eine Sitzung beginnen.
