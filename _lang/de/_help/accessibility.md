---
nav_title: Zugängliche Nachrichten erstellen
article_title: Barrierefreie Nachrichten in Braze erstellen
page_order: 3.5
page_type: reference
description: "Dieser referenzierte Artikel erklärt, warum Barrierefreiheit bei Ihren Marketing-Inhalten wichtig ist und wie Sie in Braze barrierefreie Nachrichten erstellen können."
---

# Erstellen zugänglicher Nachrichten in Braze

> Verstehen Sie, warum Barrierefreiheit bei Ihren Marketing-Inhalten wichtig ist und wie Sie in Braze barrierefreie Nachrichten erstellen können. Weitere Anleitungen finden Sie in unserem Kurs [Grundlagen des barrierefreien Messaging](https://learning.braze.com/accessible-messaging-foundations) auf Braze Lernangebote.

Marketing-Inhalte, die Menschen mit Behinderungen ausschließen, selbst wenn dies unabsichtlich geschieht, können Millionen von Menschen davon abhalten, mit Ihrer Marke zu interagieren. Bei der Zugänglichkeit im Marketing geht es darum, es jedem leicht zu machen, Ihr Marketing zu erleben, Ihre Kommunikation zu erhalten und zu verstehen und die Opportunity zu haben, in Ihr Produkt, Ihren Dienst oder Ihre Marke zu investieren oder ein Fan davon zu werden. 

Nehmen Sie sich bei der Gestaltung Ihres Messagings besonders viel Zeit, um zu überlegen, wie Sie Ihre Designs allen Kund:innen zugänglich machen können.

{% alert important %}
Dieser Inhalt ist als allgemeine Anleitung gedacht und garantiert nicht die Einhaltung von Zugänglichkeitsstandards wie WCAG. Braze bietet Tools, die die Erstellung barrierefreier Nachrichten unterstützen, aber es liegt in Ihrer Verantwortung, sicherzustellen, dass Ihre endgültigen Inhalte alle geltenden Anforderungen erfüllen. Barrierefreiheit ist ein komplexes Thema mit vielen beweglichen Teilen. Viele Unternehmen arbeiten mit Spezialisten oder Beratern für Barrierefreiheit zusammen, um sicherzustellen, dass ihre Inhalte, ihr Design und ihre Entwicklungsverfahren den Bedürfnissen aller Nutzer:innen gerecht werden.
{% endalert %}

## Zugänglichkeit bei Braze

Zugängliche Kommunikation zu unterstützen bedeutet, offen, neugierig und lernbereit zu sein. Bei Braze ist es uns wichtig, Menschen zu helfen, Kontakte zu knüpfen - und wir wissen, dass es dazu gehört, Platz für alle zu schaffen. Barrierefreiheit ist nichts, was wir jemals als "erledigt" betrachten, und wir freuen uns über die Chance, weiter zu lernen.

{% multi_lang_include accessibility/feedback.md %}

## Zu berücksichtigende Bereiche der Behinderung

*Dieser Abschnitt ist teilweise angepasst von [W3C: Unterschiedliche Fähigkeiten und Hindernisse](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

{% tabs local %}
{% tab Visuell %}

Sehbehinderungen können von einem leichten oder mäßigen Sehverlust auf einem oder beiden Augen bis hin zu einem erheblichen oder vollständigen Verlust des Sehvermögens auf beiden Augen reichen. Manche Menschen haben eine verminderte oder fehlende Empfindlichkeit für bestimmte Farben oder eine erhöhte Empfindlichkeit für helle Farben.

Um mit Ihren Inhalten zu interagieren, müssen diese Nutzer:innen die Möglichkeit haben:

- Vergrößern oder Verkleinern von Text und Bildern
- Anpassen der Einstellungen für Schriftarten, Farben und Abstände
- Hören Sie sich die Text-to-Speech-Synthese des Inhalts an (d.h. verwenden Sie einen Bildschirmleser)
- Audio-Beschreibungen von Videos anhören
- Text mit aktualisierbarer Braille-Schrift lesen

{% alert note %}
- Weltweit haben mindestens 2,2 Milliarden Menschen eine Sehschwäche im Nah- oder Fernbereich (siehe [WHO](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment))
- Etwa 1 von 12 Männern und 1 von 200 Frauen haben einen gewissen Grad an Farbsehschwäche, das sind schätzungsweise 300 Millionen Menschen auf der Welt (siehe [NHS](https://www.nhs.uk/conditions/colour-vision-deficiency/)).
{% endalert %}

{% endtab %}
{% tab Anhören %}

Hör- oder Hörbehinderungen können leichte bis mittelschwere Hörstörungen auf einem oder beiden Ohren umfassen. Selbst ein teilweiser Hörverlust kann in Bezug auf Audioinhalte problematisch sein.

Um Ihre Inhalte zu verstehen, verlassen sich diese Nutzer:innen auf:

- Transkripte und Untertitel von Audioinhalten
- Medienplayer, die Untertitel anzeigen und Optionen zum Anpassen der Textgröße und der Farben von Untertiteln bieten
- Optionen zum Anhalten, Pausieren und Anpassen der Lautstärke von Audioinhalten (unabhängig von der Systemlautstärke)
- Qualitativ hochwertige Vordergrundgeräusche, die sich deutlich von Hintergrundgeräuschen unterscheiden

{% alert note %}
- Einer von acht Menschen in den Vereinigten Staaten (13% oder 30 Millionen) im Alter von 12 Jahren oder älter hat einen Hörverlust auf beiden Ohren, basierend auf Standard-Hörprüfungen
- Ungefähr 15% der amerikanischen Erwachsenen (37,5 Millionen) im Alter von 18 Jahren und älter berichten über Hörprobleme (siehe [NIH](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing))
{% endalert %}

{% endtab %}
{% tab Physisch %}

Körperliche Behinderungen können Schwäche und Einschränkungen der Muskelkontrolle oder des Gefühls, Gelenkbeschwerden, Schmerzen, die die Bewegung behindern, und fehlende Gliedmaßen umfassen.

Diese Nutzer:innen sind auf die Tastaturunterstützung angewiesen, um Funktionen zu aktivieren (auch wenn sie keine Standardtastatur verwenden). Um mit Ihren Inhalten zu interagieren, benötigen diese Nutzer:innen:

- Große anklickbare Bereiche
- Genug Zeit, um Aufgaben zu erledigen
- Sichtbare Indikatoren für den aktuellen Fokus
- Mechanismen zum Überspringen von Inhaltsblöcken, wie Seitenkopfzeilen oder Navigationsleisten

{% alert note %}
Fast 2 Millionen Menschen in den USA leben mit dem Verlust von Gliedmaßen (siehe [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1))
{% endalert %}

{% endtab %}
{% tab Kognitiv %}

Kognitive, Lern- und neurologische Behinderungen umfassen neurodiverse und neurologische Störungen sowie Verhaltensstörungen und psychische Erkrankungen, die nicht unbedingt neurologischer Natur sind. Sie können jeden Teil des Nervensystems betreffen und beeinflussen, wie gut Menschen hören, sich bewegen, sehen, sprechen und Informationen verstehen.

Je nach individuellem Bedarf verlassen sich diese Nutzer:innen auf:

- Klar strukturierte Inhalte
- Konsistente Beschriftung von Formularen, Buttons und anderen Inhalten
- Prognostizierbare Link-Targets und Gesamtinteraktion
- Verschiedene Navigationsmöglichkeiten, wie Menüs und Suchleisten
- Einstellungen zum Ausschalten von blinkenden, blinkenden oder anderweitig ablenkenden Inhalten
- Einfacher Text, der durch Bilder unterstützt wird


{% alert note %}
- Einer von fünf Menschen in den Vereinigten Staaten hat Lern- und Aufmerksamkeitsprobleme (siehe [LDA](https://ldaamerica.org/lda_today/the-state-of-learning-disabilities-today/#:~:text=LD%20Today,have%20learning%20and%20attention%20issues.))
- Ungefähr 10-20% der Weltbevölkerung gelten als neurodivergent (siehe [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- Etwa 1 von 100 Kindern weltweit hat Autismus (siehe [WHO](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

{% endtab %}
{% endtabs %}

## Bewährte Praktiken

Die Erstellung zugänglicher Inhalte muss nicht überwältigend sein. Kleine, durchdachte Entscheidungen können einen großen Unterschied machen. In diesem Abschnitt finden Sie praktische Tipps, die dazu beitragen, dass mehr Menschen Ihre Nachrichten erfolgreich lesen, navigieren und mit ihnen interagieren. Egal, ob Sie Ihre Texte anpassen, Ihre Buttons gestalten oder Alt-Text zu Bildern hinzufügen, jede Änderung führt zu einem besseren Erlebnis. Schauen wir mal rein.

### Content

#### Struktur und Ablauf

Beginnen wir mit dem Fundament. Wenn Ihre Inhalte klar strukturiert sind, ist es für jeden einfacher, ihnen zu folgen - insbesondere für Menschen, die auf Bildschirmlesegeräte oder Tastaturnavigation angewiesen sind.

- **Unterteilen Sie Ihre Inhalte in Abschnitte:** Die Verwendung von Überschriften, Aufzählungspunkten und Listen hilft den Lesern, Ihre Inhalte schnell zu verstehen und zu überfliegen - auch wenn sie in Eile sind. 
- **Überspringen Sie keine Überschriftenebenen:** Überschriften strukturieren Ihren Inhalt und helfen den Lesern, schnell zu verstehen, wie die einzelnen Abschnitte zusammenhängen. Wenn Sie Überschriftenebenen überspringen (z.B. direkt von einer H2 zu einer H4 springen), brechen Sie diese logische Struktur. Dies erschwert es Nutzern:innen, insbesondere denen, die Bildschirmlesegeräte verwenden, zu navigieren und Ihre Nachrichten klar zu verstehen. Halten Sie sich immer an eine logische, sequentielle Hierarchie von Überschriften (H1 bis H2 bis H3 usw.), um sicherzustellen, dass Ihre Inhalte geordnet, zugänglich und für jeden leicht zu verfolgen sind.

#### Lesbarkeit

Sobald Ihre Struktur steht, müssen Sie im nächsten Schritt dafür sorgen, dass Ihre Worte auch tatsächlich leicht zu lesen sind. Das bedeutet, dass wir die Dinge einfach halten, sie scannen und über alle Geräte und Nutzer:innen hinweg bequem lesen können.

- **Schreiben Sie kurze, klare Sätze:** Kurze Sätze sind für jedermann leicht zu verstehen, insbesondere für Menschen, die Bildschirmlesegeräte verwenden oder Schwierigkeiten haben, komplexe Informationen zu verarbeiten. Schreiben Sie auf dem Leseniveau der siebten Klasse in den Vereinigten Staaten. Sie können Ressourcen wie die [Hemingway App](https://hemingwayapp.com/) verwenden, um das Leseniveau Ihres Textes zu überprüfen.
- **Wählen Sie lesbare Schriftgrößen und Abstände:** Zu kleiner Text kann schwer zu lesen sein - vor allem auf dem Handy. Verwenden Sie mindestens 14px für den Textkörper. Vergrößern Sie die Überschriften, damit die Nutzer:innen den Unterschied deutlich erkennen können. Ein zusätzlicher Abstand zwischen den Zeilen (etwa 1,5 Zeilenhöhe) und Absätzen verbessert die Lesbarkeit, insbesondere für Menschen mit visuellen oder kognitiven Einschränkungen.
- **Vermeiden Sie Blocksatz:** Blocksatz erzeugt ungleichmäßige Abstände zwischen den Wörtern, was Menschen mit Legasthenie oder kognitiven Behinderungen das Lesen erschwert. Ziehen Sie in Erwägung, Inhalte, die sich über mehr als zwei Zeilen erstrecken, bei Sprachen, die von links nach rechts verlaufen, linksbündig und bei [Sprachen, die von rechts nach links verlaufen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages), rechtsbündig auszurichten.
- **Verwenden Sie fett, kursiv und in Großbuchstaben geschriebenen Text sparsam:** Die Betonung von zu viel Text erschwert das Lesen - vor allem für Menschen mit Legasthenie oder Sehschwäche. Halten Sie es einfach.

#### Klarheit und Benutzerfreundlichkeit

Lassen Sie uns zum Schluss noch über die Feinheiten sprechen - Dinge, die den Nutzer:innen helfen, Ihre Inhalte nicht nur zu sehen, sondern auch zu verstehen und mit ihnen zu interagieren. 

- **Beschriften Sie Links und Buttons deutlich:** Achten Sie darauf, dass Ihr [Link](#links) und Ihr [Button-Text](#buttons) klar und deutlich erklärt, was als nächstes passiert. Es hilft Menschen, die Screenreader verwenden oder mit einer Tastatur navigieren, zu wissen, was sie erwartet.
- **Gehen Sie sparsam mit Symbolen und Emojis um:** Sonderzeichen und Emojis können Ihre Inhalte verspielt gestalten, aber sie können beim Lesen durch Bildschirmlesegeräte verwirrend sein. Verwenden Sie sie sparsam und achten Sie darauf, dass sie keinen klaren, beschreibenden Text ersetzen.
- **Test auf Trunkierung:** Testen Sie Ihren Text immer, indem Sie an ein Gerät [eine Testnachricht senden]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/), um sicherzustellen, dass Ihr Text nicht abgeschnitten wird. Wenn Ihre Nachrichten abgeschnitten werden, schadet dies sowohl Ihnen als auch Ihrer Zielgruppe, da Ihre Inhalte sie nicht erreichen.

### Buttons

Verwenden Sie **Buttons**, um eine Aktion anzuzeigen, z. B. das Absenden eines Formulars oder das Abspielen eines Karussells. Wenn Sie zu einer neuen URL navigieren, sollten Sie stattdessen einen [Link](#links) verwenden.

#### Schreiben Sie klare, handlungsorientierte Texte

Ähnlich wie der Linktext sollten auch die Beschriftungen der Buttons die Aktion klar beschreiben. Ein effektiver Button-Text ist spezifisch und handlungsorientiert. Zum Beispiel sagt "Bestellung abschicken" dem Nutzer:innen eindeutig, was passiert, wenn er klickt, während "Abschicken" zweideutig sein kann. Jedes Etikett sollte die beabsichtigte Aktion genau beschreiben, damit Screenreader und alle Nutzer:innen das Ergebnis der Interaktion mit Ihren Buttons leicht verstehen und prognostizieren können.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Guter Button-Text <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Schlechter Button-Text <span aria-hidden="true">🚫.</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Bestellung abschicken"</td>
      <td>"Abschicken"</td>
    </tr>
    <tr>
      <td>"Konto erstellen"</td>
      <td>"Registrierung"</td>
    </tr>
    <tr>
      <td>"Unsere Broschüre herunterladen"</td>
      <td>"Herunterladen"</td>
    </tr>
    <tr>
      <td>"Details zum Produkt anzeigen"</td>
      <td>"Mehr erfahren"</td>
    </tr>
    <tr>
      <td>"Für Updates abonnieren"</td>
      <td>"Abonnieren"</td>
    </tr>
  </tbody>
</table>

Halten Sie den Text der Buttons kurz, damit er nicht abgeschnitten wird. Wenn der Text eines Buttons zu lang ist, kann er mit einer Ellipse abgeschnitten werden, anstatt ihn umzubrechen.

#### Verwenden Sie einen ausreichenden Farbkontrast

Der Text des Buttons muss vor der Hintergrundfarbe des Buttons gut lesbar sein. Vergewissern Sie sich, dass Ihr Button-Text den [Mindestkontrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) der WCAG 2.2 AA erfüllt:

- Kontrastverhältnis 4,5:1 für normal großen Text (die meisten Buttons)
- Kontrastverhältnis 3:1 für großen Text (typischerweise über 18pt)

Der hohe Kontrast sorgt dafür, dass die Buttons für alle lesbar und anklickbar bleiben, auch für Nutzer:innen mit Sehbehinderungen oder solche, die Ihre Nachrichten in schwierigen Umgebungen betrachten. Weitere Hinweise finden Sie im Abschnitt [Farbkontrast](#color-contrast).

#### Machen Sie Buttons leicht antippbar

Achten Sie darauf, dass Ihre Buttons (und Links) groß genug sind und einen ausreichenden Abstand für Nutzer:innen auf mobilen Geräten haben. Kleine oder überfüllte [Touch Targets](#touch-targets) können für Nutzer:innen mit motorischen Einschränkungen frustrierend oder unmöglich sein.  

### Links

Verwenden Sie Links zur Navigation, z.B. um Nutzer:innen auf eine externe Seite zu leiten.

#### Schreiben Sie einen beschreibenden Linktext

Schreiben Sie einen Linktext, der klar beschreibt, wohin der Nutzer:innen gelangt. Nutzer:innen von Bildschirmlesegeräten springen oft von Link zu Link, um den Inhalt zu überfliegen. Stellen Sie also sicher, dass Ihr Linktext für sich stehen kann. Vermeiden Sie Phrasen wie "hier klicken", "mehr" und "für Details klicken", da sie zweideutig sind, wenn sie aus dem Zusammenhang gerissen werden.

Denken Sie zum Beispiel daran, wie Sie einen Link zur Anzeige eines Wetterberichts schreiben könnten.

| Schlecht  | Besser | Beste |
| --- | --- | --- | 
| Hier klicken | Klicken Sie hier, um das heutige Wetter abzurufen | Das Wetter von heute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Wie bei allen anderen Inhalten auch, halten Sie sie einfach und mit so wenig zusätzlichen Wörtern wie möglich.

#### Vermeiden Sie es, Links wie Buttons zu gestalten

Braze Drag-and-Drop-Editoren geben standardmäßig semantisches HTML aus, so dass Links dort nicht wie Buttons gestylt werden. Wenn Sie jedoch mit [angepasstem HTML](#custom-html) arbeiten oder Änderungen auf Code-Ebene vornehmen, sollten Sie dies berücksichtigen:

- **Links (`<a>`)** reagieren auf die <kbd>Enter</kbd>-Taste.
- **Buttons (`<button>`)** reagieren sowohl auf die <kbd>Enter</kbd>- als auch auf die <kbd>Space</kbd>-Taste.

Wenn Sie einen Link so gestalten, dass er wie ein Button aussieht, kann das Menschen verwirren, die mit der Tastatur navigieren - sie könnten versuchen, die <kbd>Leertaste</kbd> zu drücken und erwarten, dass es funktioniert.

Verwenden Sie das richtige Element für die Aktion:

- Verwenden Sie `<button>` für Aktionen, wie das Absenden eines Formulars oder das Öffnen eines Modals.
- Verwenden Sie `<a>` für die Navigation, z. B. für die Verknüpfung mit einer anderen Seite oder Datei.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Ziele berühren

Touch Targets sind alle Teile Ihrer Nachricht, auf die Nutzer:innen tippen, um eine Aktion auszuführen, wie Buttons, Links oder Symbole. Diese Elemente müssen groß genug sein und einen ausreichenden Abstand zueinander haben, damit sie leicht angetippt werden können, insbesondere auf mobilen Geräten.

Wenn die Touch-Targets zu klein sind oder zu dicht beieinander liegen, kann es für Nutzer:innen mit eingeschränkter Mobilität oder Geschicklichkeit frustrierend oder unmöglich sein, mit Ihrer Nachricht zu interagieren. Wenn Sie dies verbessern, können Sie Fehler reduzieren und eine reibungslosere Erfahrung für alle schaffen.

Das sollten Sie beachten:
- **Erleichtern Sie das Antippen.** Streben Sie eine Mindestgröße für das Targeting von 44 x 44 Pixeln an. Dies entspricht den WCAG 2.2-Richtlinien für [Touch-Targeting](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) und den üblichen Standards für mobile Benutzerfreundlichkeit.
- **Geben Sie jedem Targeting Raum zum Atmen.** Wenn Tap-Targets zu dicht beieinander liegen - wie gestapelte Links oder eng gruppierte Buttons -, kann man sie leicht übersehen oder auf das falsche tippen. Fügen Sie Abstand oder Padding zwischen den Elementen hinzu, um dies zu verhindern.
- **Verlassen Sie sich nicht nur auf das Visuelle.** Selbst kleine Symbole können durch zusätzliches Padding besser nutzbar gemacht werden, so dass sie die Mindestgrößenanforderungen erfüllen, ohne das Layout zu verändern.
- **Vorschau auf das Handy.** Testen Sie Ihre Nachrichten auf verschiedenen Bildschirmgrößen und stellen Sie sicher, dass die interaktiven Elemente einfach zu bedienen sind.

Die Verbesserung des Targetings ist eine der effektivsten Methoden, um Ihre Nachrichten auf dem Handy zugänglicher zu machen - und es ist eine gute UX für alle.

### Bilder

#### Alt-Text bereitstellen

Alternativtext (Alt-Text) ist eine kurze Beschreibung des Inhalts oder der Funktion eines Bildes, die Bildschirmlesegeräte und andere unterstützende Technologien den Nutzer:innen zur Verfügung stellen. Schreiben Sie für jedes aussagekräftige Bild einen beschreibenden Alt-Text, damit auch Nutzer:innen, die das Bild nicht sehen können, Ihre Nachricht oder Ihren Aufruf zum Handeln verstehen. 

#### Vermeiden Sie Bilder von Text

Vermeiden Sie es nach Möglichkeit, Text innerhalb von Bildern zu platzieren - Bildschirmleser können bildbasierten Text nicht lesen, und Nutzer:innen können die Schriftgröße oder -farbe nicht einfach anpassen, um eine bessere Sichtbarkeit zu erreichen. Beachten Sie diese Tipps:

- **Entfernen Sie Text, wo Sie können:** Verschieben Sie den beschreibenden oder werbenden Text aus dem Bild in ein Textfeld Ihrer Nachricht. Auf diese Weise können Nutzer:innen die Größe und Farbe des Bildes je nach den Einstellungen ihres Geräts oder Browsers ändern.
- **Testen Sie die Lesbarkeit und den Kontrast:** Wenn Sie Text im Bild behalten müssen, sollten Sie den [Farbkontrast](#color-contrast) beachten und eine [große Schriftart](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale) verwenden. Das bedeutet, dass der Text mindestens 18 Punkt (ca. 24 Pixel) groß sein sollte, wenn er nicht fett gedruckt ist, oder 14 Punkt (ca. 18 Pixel), wenn er fett gedruckt ist. Die Verwendung dieser Größen trägt dazu bei, dass der Text lesbar bleibt, ohne dass die Nutzer:innen zum Zoomen gezwungen werden, und verbessert den Gesamtkontrast und die Lesbarkeit des Inhalts. Testen Sie, ob es auf kleineren Bildschirmen noch lesbar ist.
- **Geben Sie einen Alt-Text an:** Für wichtigen Text, der im Bild verbleiben muss, fügen Sie einen Alt-Text hinzu, der die Wörter beschreibt.

Wenn Bilder Text enthalten, der nicht bearbeitet werden kann, verlieren Nutzer:innen mit Sehbehinderungen die Möglichkeit, Anpassungen beim Lesen vorzunehmen. Indem Sie Text und Bilder voneinander trennen, können mehr Nutzer:innen Ihre Nachricht bequem lesen und mit ihr interagieren.

#### Tipps zum Schreiben von Alt-Text

- [Beschreiben Sie, was auf dem Bild zu sehen ist](#tip-1)
- [Halten Sie es kurz, aber präzise](#tip-2)
- [Vermeiden Sie "Bild von" oder "Bild von".](#tip-3) 
- [Text, der im Bild erscheint, reflektieren](#tip-4)
- [Halten Sie sich an den relevanten Kontext - kein zusätzlicher Marketing-Jargon](#tip-5)
- [Berücksichtigen Sie den Zweck des Bildes](#tip-6)

##### Beschreiben Sie, was auf dem Bild zu sehen ist {#tip-1}

Nutzer:innen von Screenreadern verlassen sich auf den Alt-Text, um den Inhalt oder die Funktion eines Bildes zu verstehen. Vermeiden Sie generische "Marketing-Sprache", die nicht mit dem übereinstimmt, was visuell dargestellt wird.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Gute Beispiele <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Schlechte Beispiele <span aria-hidden="true">🚫.</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Lächelnde Frau mit blauer Jeansjacke, die eine Einkaufstasche hält."</td>
      <td>"Zeit, sich etwas zu gönnen!" (Ohne zu erwähnen, was tatsächlich auf dem Bild zu sehen ist)</td>
    </tr>
    <tr>
      <td>"Mann mit schwarzem T-Shirt, der sich in einer Straße in der Stadt an ein Fahrrad lehnt."</td>
      <td>"Umarmen Sie jetzt Ihr bestes Leben!" (Ignoriert das Fahrrad und die Stadtkulisse)</td>
    </tr>
    <tr>
      <td>"Blaues Apartmenthaus mit einem Schild 'Zu vermieten' davor."</td>
      <td>"Der Schlüssel zu einer besseren Zukunft!" (entspricht nicht der Wohnung oder dem Schild)</td>
    </tr>
  </tbody>
</table>

##### Halten Sie es kurz, aber präzise {#tip-2}

Ein prägnanter Alt-Text erleichtert Nutzern:innen die Verarbeitung. Geben Sie genügend Details an, um den Zweck zu vermitteln, aber lassen Sie jeglichen Fluff weg. In der Regel sollten Sie den Alt-Text auf 125 Zeichen oder weniger beschränken. Wenn mehr als eine kurze Phrase oder ein Satz erforderlich ist, sollten Sie eine der [langen Beschreibungsmethoden](https://www.w3.org/WAI/tutorials/images/complex/) des W3C verwenden.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Gute Beispiele <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Schlechte Beispiele <span aria-hidden="true">🚫.</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Rote Laufschuhe auf weißem Hintergrund"</td>
      <td>"Laufschuhe, die extrem bequem sind und sich perfekt für Ihren aktiven Lebensstil eignen, in einem leuchtenden Rotton." (Zu lang und zu viel Werbung)</td>
    </tr>
    <tr>
      <td>"Vier Laptops auf einem Ständer"</td>
      <td>"Entdecken Sie den ultimativen Produktivitätsbooster, der die Art und Weise, wie Sie jeden Tag arbeiten, auf jede erdenkliche Weise neu definiert." (Beschreibt nicht, was tatsächlich gezeigt wird)</td>
    </tr>
    <tr>
      <td>"Eine Gruppe von Freunden isst Eis an einem sonnigen Tag"</td>
      <td>"Fangen Sie pures Glück mit der süßesten Leckerei ein - das Leben ist besser mit unserer Eismarke!" (Zu abstrakt und markenorientiert)</td>
    </tr>
  </tbody>
</table>

##### Vermeiden Sie "Bild von" oder "Bild von". {#tip-3}

Bildschirmleser kündigen bereits ein Bild an. Beginnen Sie gleich mit der Beschreibung des Themas.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Gute Beispiele <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Schlechte Beispiele <span aria-hidden="true">🚫.</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Gedeckter Tisch zum Brunch mit Pfannkuchen, Obst und Kaffee."</td>
      <td>"Bild eines zum Brunch gedeckten Tisches"</td>
    </tr>
    <tr>
      <td>"Plakatwand am Straßenrand mit fettem Text 'Grand Opening'".</td>
      <td>"Bild einer Werbetafel am Straßenrand"</td>
    </tr>
    <tr>
      <td>"Verschneite Berglandschaft bei Sonnenuntergang"</td>
      <td>"Foto von Schnee und Bergen"</td>
    </tr>
  </tbody>
</table>

##### Text, der im Bild erscheint, reflektieren {#tip-4}

Wenn ein Bild wichtigen Text enthält, fügen Sie diese Information in den Alt-Text ein, damit die Nutzer:innen sie nicht übersehen.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Gute Beispiele <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Schlechte Beispiele <span aria-hidden="true">🚫.</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Banner mit der Aufschrift 'Summer Sale-50% auf alle Bademode'."</td>
      <td>"Werbebanner für eine Aktion" (ohne den eigentlichen Rabatt zu erwähnen)</td>
    </tr>
    <tr>
      <td>"Logo mit dem Text 'Café Toscana' in Script-Schrift".</td>
      <td>"Logo-Bild für ein Café" (enthält nicht den Text 'Café Toscana')</td>
    </tr>
    <tr>
      <td>"Anzeige mit der Ankündigung 'Konzertkarten ab 5. Juni erhältlich'".</td>
      <td>"Konzertanzeige" (keine Angaben zum Ereignis)</td>
    </tr>
  </tbody>
</table>

##### Halten Sie sich an den relevanten Kontext - kein zusätzlicher Marketing-Jargon {#tip-5}

Padding Sie den Alt-Text nicht mit SEO-Begriffen oder Handlungsaufforderungen, die nicht direkt mit dem Bild zusammenhängen. Bieten Sie einen Mehrwert für diejenigen, die das Bild nicht sehen können.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Gute Beispiele <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Schlechte Beispiele <span aria-hidden="true">🚫.</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Laptop mit dem Braze-Dashboard Analytics Chart"</td>
      <td>"Steigern Sie die Konversionen und erhöhen Sie den ROI mit der besten Plattform der Welt!" (Fügt unnötige Marketing-Sprache hinzu)</td>
    </tr>
    <tr>
      <td>"Terrassenset für den Garten mit vier Stühlen und einem Glastisch"</td>
      <td>"Veranstalten Sie jetzt eine unglaubliche Sommerparty für alle Ihre Freunde und Ihre Familie!" (Beschreibt ein Szenario, nicht das Bild)</td>
    </tr>
    <tr>
      <td>"Handy mit Wettervorhersage App mit 75°F im Blick"</td>
      <td>"Erleben Sie Realtime-Innovationen beim Wetter Tracking, die das Spiel verändern" (Gibt nicht wieder, was sichtbar angezeigt wird)</td>
    </tr>
  </tbody>
</table>

##### Berücksichtigen Sie den Zweck des Bildes {#tip-6}

Wenn ein Bild wie ein Link oder eine Aufforderung zur Handlung funktioniert, beschreiben Sie die beabsichtigte Handlung ("Einkaufen", "Link zu", "Registrieren"), nicht nur das Label oder das abgebildete Produkt.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Gute Beispiele <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Schlechte Beispiele <span aria-hidden="true">🚫.</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Kaufen Sie die Herbstkollektion"</td>
      <td>"Fall Collection" (Fehlende beabsichtigte Aktion)</td>
    </tr>
    <tr>
      <td>"Link zum kostenlosen E-Book"</td>
      <td>"Kostenloses E-Book" (Es wird nicht deutlich, dass es sich um einen Link handelt)</td>
    </tr>
    <tr>
      <td>"Registrieren Sie sich für die Mailingliste"</td>
      <td>"Mailingliste" (Beschreibt nicht, was der Nutzer:innen tun kann)</td>
    </tr>
  </tbody>
</table>

Wenn das Bild keinen Zweck hat, sollten Sie auch das mitteilen. Dekorative Bilder, wie z.B. Logos, sollten einen leeren alt Tag (`alt=""`) haben, damit Bildschirmleser wissen, dass sie die Anzeige überspringen sollen. Ohne sie wird stattdessen normalerweise der Name der Bilddatei gelesen.

### Videos

Videos sind fesselnd, aber wenn sie nicht zugänglich sind, laufen Sie Gefahr, einen Teil Ihrer Zielgruppe auszuschließen. Nutzen Sie die folgenden Tipps, um Ihre Video-Inhalte inklusiver zu gestalten:

- [Bereitstellung von Untertiteln](#closed-captions)
- [Wiedergabesteuerung bereitstellen](#playback-controls)
- [Vermeiden Sie die automatische Wiedergabe](#no-auto-play)
- [Vermeiden Sie blinkende oder flackernde Inhalte](#no-seizures)

#### Bereitstellung von Untertiteln {#closed-captions}

Fügen Sie Ihren Videos Untertitel bei, damit die Nutzer:innen den Dialogen, Soundeffekten und anderen Audioinhalten folgen können. Bildunterschriften helfen:

- Menschen, die gehörlos oder schwerhörig sind
- Zuschauer, die in einer schalltoten Umgebung zuschauen
- Nicht-Muttersprachler, die lieber mitlesen

Geschlossene Untertitel können ein- oder ausgeschaltet werden, so dass Nutzer:innen selbst entscheiden können, was für sie am besten funktioniert.

{% multi_lang_include accessibility/video.md %}

#### Wiedergabesteuerung bereitstellen {#playback-controls}

Stellen Sie sicher, dass Ihr eingebettetes Video zugängliche Steuerelemente für die Wiedergabe enthält, wie z. B. Abspielen, Pause, Stummschalten und Suchen, damit die Nutzer:innen auf die für sie beste Weise damit interagieren können.

#### Vermeiden Sie die automatische Wiedergabe {#no-auto-play}

Vermeiden Sie es nach Möglichkeit, Videos automatisch abspielen zu lassen. Die automatische Wiedergabe kann für Sie störend oder verwirrend sein:

- Nutzer:innen, die auf Bildschirmleser oder Tastaturnavigation angewiesen sind
- Menschen mit Bewegungsempfindlichkeit
- Jeder, der sich in einer ruhigen Umgebung aufhält (z.B. am Arbeitsplatz oder spätabends)

Lassen Sie die Nutzer:innen entscheiden, wann ein Video abgespielt werden soll, indem Sie klare Kontrollen einbauen.

#### Vermeiden Sie blinkende oder flackernde Inhalte {#no-seizures}

Verzichten Sie auf Videos mit Blink- oder Stroboskopeffekten, insbesondere bei hoher Frequenz. Diese können bei Nutzer:innen mit lichtempfindlicher Epilepsie Anfälle triggern und bei anderen zu Unwohlsein führen.

### Farbkontrast

Ein ausreichender Farbkontrast sorgt dafür, dass Ihre Nachrichten für jeden gut lesbar sind, auch für Menschen mit Sehschwäche oder für diejenigen, die Ihre Inhalte unter hellen oder schwierigen Bedingungen betrachten. Streben Sie ein Kontrastverhältnis an, das den [Anforderungen der WCAG 2.2 Stufe AA](https://www.w3.org/TR/WCAG/#contrast-minimum) entspricht:

- 4,5:1 Kontrastverhältnis für normalen Text (denken Sie an Fließtext, Buttons und Links)
- Kontrastverhältnis 3:1 für großen Text (z. B. Überschriften und größere Beschriftungen)

Sie können Ihre Farbauswahl mit dem [WebAim Contrast Checker Tool](https://webaim.org/resources/contrastchecker/) testen.

{% multi_lang_include accessibility/color.md %}

### Benutzerdefiniertes HTML

Wenn Sie in Ihren Nachrichten angepasstes HTML verwenden:

- Verwenden Sie [semantisches HTML](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Das bedeutet, dass Sie die richtigen HTML-Elemente für den vorgesehenen Zweck verwenden, anstatt ein Element so zu gestalten, dass es wie ein anderes aussieht. Die meisten HTML-Elemente haben ihre eigene Unterstützung für Barrierefreiheit eingebaut.
- Legen Sie das [Attribut`lang` ](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang) in Ihrem HTML-Code fest, um die Sprache zu identifizieren, in der Ihr Inhalt vorliegt. Bildschirmlesegeräte verwenden für jede Sprache unterschiedliche Bibliotheken, die auf der Aussprache und den Eigenschaften der jeweiligen Sprache basieren. Wird dies nicht angegeben, geht ein Bildschirmlesegerät davon aus, dass der Inhalt in der Standardsprache geschrieben ist, die der Nutzer:in bei der Einrichtung des Bildschirmlesegeräts gewählt hat. Wenn die Nachricht nicht in der Standardsprache verfasst ist, kann es sein, dass das Bildschirmlesegerät die Nachricht nicht richtig ausspricht. 

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

{% alert note %}
Wenn Sie den E-Mail Drag-and-Drop-Editor verwenden, können Sie die Sprache für die E-Mail festlegen, indem Sie auf den Tab **Einstellungen** gehen und den entsprechenden Sprachwert auswählen.
{% endalert %}

- Verwenden Sie [ARIA Attribute](#aria-attributes), um zusätzlichen Kontext zu liefern. Diese Attribute liefern zusätzliche Informationen für Hilfstechnologien und helfen dabei, die Rolle, den Zustand oder die Eigenschaften von UI-Elementen zu klären, die andernfalls unklar sein könnten. 

### ARIA-Attribute

Wenn Sie angepassten Code in Braze-Editoren verwenden, können Sie Accessible Rich Internet Applications[(ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)) einsetzen, um Nutzern:innen, die auf Hilfsmittel angewiesen sind, zusätzliche Unterstützung für die Barrierefreiheit zu bieten. ARIA-Rollen und -Attribute helfen Bildschirmlesern, Ihre Inhalte klarer zu interpretieren, insbesondere wenn Sie Elemente verwenden, die für sich genommen keine Bedeutung haben (wie `<div>` oder `<span>`).

{% alert important %}
ARIA wurde zwar entwickelt, um Webinhalte zugänglicher zu machen, kann aber bei falscher Anwendung mehr Schaden als Nutzen anrichten. ARIA ersetzt kein semantisches HTML, sondern ergänzt es. Verwenden Sie ARIA also nur, wenn native HTML-Elemente Ihren Anforderungen nicht genügen.
{% endalert %}

Hier sind ein paar Beispiele, die besonders im Zusammenhang mit Messaging nützlich sind:

- [aria-label](#aria-label)
- [aria-labelledby](#aria-labelledby)
- [aria-hidden="true"](#aria-hiddentrue)
- [role="Präsentation"](#rolepresentation)
- [aria-live="höflich"](#aria-livepolite)

#### aria-label

`aria-label` fügt einen zugänglichen Namen zu Elementen hinzu, die keinen sichtbaren Text haben. Wenn Sie ein Symbol ohne Text verwenden (z. B. einen Mülleimer oder ein "X" für "Schließen"), weiß jemand, der ein Bildschirmlesegerät verwendet, nicht, was es bedeutet - es sei denn, Sie beschriften es. `aria-label` gibt diesem Symbol eine Stimme.

{% raw %}
```html
<button aria-label="Close message">
  <svg ...></svg>
</button>
```
{% endraw %}

#### aria-labelledby

`aria-labelledby` verbindet ein Element mit etwas, das bereits eine sichtbare Beschriftung hat. Wenn Sie also ein Banner oder einen Bereich haben, der mit einem Titel laut vorgelesen werden soll, können Sie `aria-labelledby` verwenden, um der assistiven Technologie mitzuteilen: "Hey, benutze diese Überschrift dort drüben, um diesen Teil zu benennen."

{% raw %}
```html
<h2 id="banner-title">Important Update</h2>
<div role="region" aria-labelledby="banner-title">...</div>
```
{% endraw %}

#### aria-hidden="true"

`aria-hidden="true"` blendet Dinge vor Bildschirmlesern aus.  Es ist hilfreich für Text oder visuelle Elemente, die keine wichtige Bedeutung haben, wie z.B. ein Glitzern, ein Häkchen oder ein Emoji, das nur aus Stilgründen verwendet wird.

Dies sorgt für eine saubere Darstellung für Nutzer:innen von Bildschirmlesegeräten, die sonst redundante oder verwirrende Inhalte hören könnten. Es ist auch nützlich, um Dinge wie Akkordeoninhalte auszublenden, die noch nicht erweitert wurden.

{% raw %}
```html
<span aria-hidden="true">✔️</span>
```
{% endraw %}

Im Allgemeinen ist es besser, `alt=""` für [dekorative Bilder](#images) und Symbole zu verwenden, als `aria-hidden="true"`. Während semantisches HTML von allen Screenreadern und Hilfsprogrammen weitgehend unterstützt wird, variiert die Unterstützung von ARIA. Auch wenn Sie `aria-hidden` verwenden, sollten Sie ein leeres alt-Attribut einfügen.

#### role="Präsentation"

`role="presentation"` weist Hilfsmittel an, reine Layout-Elemente, wie z.B. Tabellen, zu ignorieren. In E-Mails zum Beispiel werden häufig Tabellen verwendet, um die Dinge aneinanderzureihen. Ohne diese Rolle könnten Bildschirmlesegeräte annehmen, dass es sich bei Ihrem Layout um eine Datentabelle handelt und beginnen, Zeilen- und Spaltennummern vorzulesen.  

{% raw %}
```html
<table role="presentation">...</table>
```
{% endraw %}

E-Mails, die mit dem Drag-and-Drop-Editor für E-Mails erstellt wurden, sind automatisch mit dem ARIA Attribut `role="presentation"` gekennzeichnet.

#### aria-live="höflich"

`aria-live="polite"` kündigt Updates an, wenn sich Inhalte ändern, ohne dass Nutzer:innen eingreifen müssen. Verwenden Sie es, wenn Sie dynamische Updates innerhalb einer Nachricht anzeigen, wie Erfolge, Fehler oder andere Benachrichtigungen.

{% raw %}
```html
<div aria-live="polite">Your preferences have been saved.</div>
```
{% endraw %}

## Automatisierte Zugänglichkeitstests

Damit Sie Probleme mit der Barrierefreiheit frühzeitig erkennen und beheben können, bietet Braze automatisierte Barrierefreiheitstests in den folgenden Bereichen an:

- [Posteingang Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) für E-Mails
- [Barrierefreiheits-Scanner]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/#accessibility-scanner) für Nachrichten, die mit unserem HTML-Editor erstellt wurden (z.B. In-App-Nachrichten, HTML Content-Blöcke, [angepasste E-Mail-Fußzeilen]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer), [Opt-in-Seiten]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-opt-in-page) und [Seiten zum Abmelden von E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-unsubscribe-page)).

Diese Tests überprüfen Ihre Nachrichten anhand der Web Content Accessibility Guidelines[(WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), einer Reihe international anerkannter technischer Standards für barrierefreie Inhalte. Alle Probleme, die automatisch erkannt werden können, werden markiert und nach Schweregrad kategorisiert, damit Sie Prioritäten setzen können.

{% alert note %}
Inbox Vision funktioniert sowohl für HTML- als auch für Drag-and-Drop-E-Mails. Der Scanner läuft nur bei Inhalten, die mit dem HTML-Editor erstellt wurden.
{% endalert %}

### Was automatisierte Tests abfangen können und was nicht

Automatisierte Zugänglichkeitstests sind ein guter Ausgangspunkt - aber sie können nicht alles erfassen. Es gibt Themen, die eine menschliche Note benötigen, um sie richtig zu bewerten, insbesondere wenn der Kontext oder das visuelle Design eine Rolle dabei spielen, wie Nutzer:innen Ihre E-Mail erleben.

Es kann sein, dass Sie einige Ausgaben als **überarbeitungsbedürftig** markiert sehen. Dies sind Fälle, in denen der Checker nicht mit Sicherheit sagen kann, ob etwas ein Problem für die Zugänglichkeit darstellt. In diesem Fall empfehlen wir Ihnen, sie manuell zu überprüfen.

Einige Beispiele dafür, was automatisierte Tools nicht zuverlässig erkennen können, sind:

- Wenn die Fokusreihenfolge der interaktiven Elemente einer logischen Abfolge folgt
- Wenn der Inhalt vollständig mit einer Tastatur bedienbar ist, ohne dass eine Maus erforderlich ist
- Wenn der Alt-Text ein Bild aussagekräftig beschreibt
- Wenn Überschriften richtig verwendet werden, um den Inhalt zu organisieren
- Wenn Links und Buttons klar beschriftet und leicht zu verstehen sind
- Wenn die Touching-Ziele groß genug sind und einen angemessenen Abstand haben
- Wenn Text auf Hintergrundbildern die Anforderungen an den Farbkontrast erfüllt
- Wenn die Anweisungen oder Etiketten für alle Nutzer:innen klar und hilfreich sind

Diese Einschränkungen sind nicht eindeutig bei Braze, sondern bei allen Tools zur Automatisierung der Barrierefreiheit. Automatisierte Prüfungen können nicht alle Hilfsmittel, Bildschirmleser oder Nutzer:innen nachahmen. Deshalb ist Barrierefreiheit keine einmalige Angelegenheit, sondern eine ständige Praxis.

Auch wenn Ihre Nachricht alle Automatisierungen durchläuft, ist es wichtig, dass Sie das tun:

- Überprüfen Sie gekennzeichnete Themen sorgfältig, insbesondere solche, die als **überarbeitungsbedürftig** gekennzeichnet sind.
- Testen Sie, wenn möglich, manuell, insbesondere für Layout und Interaktionsmuster.
- Verwenden Sie Tools wie Bildschirmlesegeräte, Navigation nur über die Tastatur und Browser-Zoom, um verschiedene Zugangsanforderungen zu simulieren.

Wenn Sie automatisierte Tests mit einer sorgfältigen manuellen Überprüfung kombinieren, erkennen Sie mehr potenzielle Probleme und erstellen umfassendere, nutzbare Kampagnen für jeden Empfänger:in.
