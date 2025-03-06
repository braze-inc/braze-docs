---
nav_title: Globale Kontrollgruppe 
article_title: Globale Kontrollgruppen-Berichterstattung
page_type: reference
description: "Dieser Artikel behandelt die Berichtskennzahlen, die Sie auf der Seite Globale Kontrollgruppenberichte im Dashboard finden."
tool: 
  - Reports

---

# Bericht zur globalen Kontrollgruppe

> Mit dem globalen Kontrollgruppenbericht können Sie Ihre Gruppe mit einer Stichprobe vergleichen. Dabei handelt es sich um eine zufällige Auswahl von Nutzern, die nicht aus der Kontrollgruppe stammt, ungefähr dieselbe Personenanzahl wie Ihre Kontrollgruppe umfasst und mit der Random-Bucket-Number-Methode erzeugt wurde.

Um einen Bericht für Ihre [Globale Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) vom Dashboard aus anzuzeigen, navigieren Sie zu **Analytics** > **Global Control Group Report**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie diese Seite unter **Daten**.
{% endalert %}

Wählen Sie dann den Parameter, mit dem Sie Ihren Bericht ausführen möchten (Sitzungen oder ein bestimmtes benutzerdefiniertes Ereignis) und klicken Sie auf **Bericht ausführen**.

![][6]

## Über Ihren Bericht

Wenn Sie einen Bericht erstellen, wählen Sie ein Ereignis (Sitzungen oder ein benutzerdefiniertes Ereignis), um Ihre Behandlungs- und Kontrollgruppen zu vergleichen. Wählen Sie dann einen Zeitraum, für den Sie Daten anzeigen möchten. Wenn Sie mehrere Kontrollgruppenexperimente zu unterschiedlichen Zeitpunkten gespeichert haben, sollten Sie besser keine Daten von mehreren Experimenten in den Bericht aufnehmen.

Denken Sie daran, dass die Prozentzahlen im Bericht gerundet sind. In Fällen, in denen die Anzahl der Konversionen einen sehr geringen Anteil der Kontroll- bzw. Behandlungsgruppe ausmacht, kann die Konversionsrate daher auch 0 % betragen.

Schließlich zeigt dieser Bericht, wie auch einige andere Berichte auf unserer Plattform, einen prozentualen [Konfidenzgrad]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#understanding-confidence) für die Veränderung Ihrer Kontrollkennzahl an. Beachten Sie auch, dass bei einer gleich hohen Konversionsrate in Kontroll- und Behandlungsgruppe eine Konfidenz von 0 % zu erwarten ist. Das bedeutet, dass die Wahrscheinlichkeit eines Performance-Unterschieds zwischen beiden Gruppen 0 % beträgt.

### Gruppengrößen

Bis Mai 2024 war die globale Kontrollgruppe von der Archivierung ausgeschlossen, die Behandlungsgruppenstichprobe jedoch nicht. Seit Mai 2024 sind nun beide Gruppen von der Archivierung ausgeschlossen. Das kann dazu führen, dass Ihre Behandlungsgruppenstichprobe und die globale Kontrollgruppe signifikant unterschiedliche Größen aufweisen. Wenn Sie Ihre globale Kontrollgruppe das nächste Mal zurücksetzen, wird sich diese Diskrepanz auflösen und Sie werden ähnliche Gruppengrößen sehen.

## Kennzahlenberichte erstellen

| Metrisch | Definition | Berechnung |
| -- | -- | -- |
| Veränderung gegenüber Kontrollgruppe | Damit wird der Unterschied zwischen der Konversionsrate der Behandlungs- und der Kontrollgruppe berechnet. | ((Konversionsrate der Behandlung - Konversionsrate der Kontrolle) ÷ Konversionsrate der Kontrolle) * 100 |
| Inkrementeller Uplift | Die Differenz der Gesamtzahl der Ereignisse zwischen Ihrer Behandlungs- und Kontrollgruppe. Mit dieser Kennzahl soll die Frage beantwortet werden, wie viele zusätzliche Konversionsereignisse die Behandlungsgruppe erzielt. | Ereignisanzahl Behandlung abzgl. Ereignisanzahl Kontrolle |
| Inkrementeller Uplift (%) | Der prozentuale Ereignisanteil in der Behandlungsgruppe, die (anders als gewöhnliches Nutzerverhalten) auf Ihre Behandlung zurückgeführt werden kann. Dies wird berechnet, indem der inkrementelle Uplift (Anzahl) durch die Gesamtzahl der Ereignisse in Ihrer Behandlungsgruppe geteilt wird. | Zusätzliche Steigerung (Zahl) ÷ Ereignisanzahl in der Behandlungsgruppe |
| Konversionsrate | Der durchschnittliche prozentuale Anteil der Kontroll- bzw. Behandlungsgruppe, der das ausgewählte Ereignis im gewählten Zeitraum pro Tag abschließt. Wenn die Konversionsanzahl sehr gering und die Kontroll- bzw. Behandlungsgruppe sehr groß ist, kann die Konversionsrate auf 0 % abgerundet werden. | Durchschnittlicher prozentualer Nutzeranteils (Mittelwert), der das ausgewählte Ereignis im gewählten Zeitraum pro Tag abschließt. |
| Gruppengröße (geschätzt) | Die geschätzte Anzahl der Nutzer:innen in Ihrer Kontroll- und Behandlungsgruppe während des ausgewählten Zeitraums. | Die maximale Mitgliederzahl der Kontroll- bzw. Behandlungsgruppe im Berichtszeitraum. |
| Events gesamt | Die Ereignisanzahl im Berichtszeitraum. Keine eindeutige Angabe (wenn ein Benutzer z.B. ein Ereignis zweimal innerhalb des Zeitraums ausführt, wird das Ereignis zweimal hochgezählt). | Absolute Häufigkeit des Ereignisses im gewählten Zeitraum pro Tag. |
| Events pro Nutzer:in | Die geschätzte durchschnittliche Häufigkeit abgeschlossener Konversionsereignisse im ausgewählten Zeitraum. | Ereignisse insgesamt ÷ geschätzte Gruppengröße. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[6]: {% image_buster /assets/img/control_group/control_group6.png %}