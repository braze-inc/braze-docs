---
nav_title: Braze Docs Style Guide
article_title: Braze Docs Style Guide
description: "Schreibstil-Leitfaden für Braze Docs."
page_order: 0
noindex: true
---

# Braze Docs Style Guide

## Schreibstil-Leitfaden

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

### Allgemeine Richtlinien {#general-guidelines}

#### Stimme und Tonalität {#voice-and-tone}

Die Markenstimme von Braze ist klug, gesprächig und direkt. Wir sind eine menschliche Stimme in einer Welt voller Tech-Buzzwords; wir bieten Klarheit und Orientierung für alle, die sich für Customer-Engagement interessieren; und wir verzichten auf Fachjargon zugunsten einer prägnanten Sprache, die ebenso leicht verständlich wie wirkungsvoll ist.

Um diese Markenstimme in unserem Schreiben und Redigieren abzustimmen, verwenden wir drei Stimmrichtlinien: **geradlinig, befähigend** und **menschlich**.

##### Geradlinig

Strukturieren Sie Ihre Texte klar und machen Sie es den Lesenden leicht, die benötigten Informationen zu finden.

* Erklären Sie komplizierte Dinge einfach.
* Fassen Sie sich kurz.
* Verwenden Sie einheitliche Begriffe für Funktionen und Aktionen.

###### Richtlinien

✅ Verwenden Sie visuelle Elemente, um komplexe Themen zu verdeutlichen. <br>
**Beispiel:** Das Bild zum Nutzerprofil-Lebenszyklus im [Artikel zum Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) hilft, ein schwieriges Konzept zu veranschaulichen.

✅ Schaffen Sie eine klare Informationshierarchie. <br>
**Beispiel:** „Dies ist eine Übersicht darüber, wie Inhalte in Braze Docs verwaltet werden. Um mehr über ein bestimmtes Thema zu erfahren, wählen Sie die entsprechende Themenseite in der Navigation."

✅ Streichen Sie Fachjargon und Abkürzungen konsequent, wenn möglich. Falls nicht möglich, definieren Sie sie. <br>
**Beispiel:** „Der Short Messaging Service (SMS) wird zum Senden und Empfangen kurzer Textnachrichten verwendet."

##### Befähigend

Welches Problem versuchen Sie mit Ihrem Text zu lösen? Behalten Sie dieses Problem beim Erstellen jeglicher Inhalte im Hinterkopf.

* Erklären Sie das „Warum" und „Wie", um den Nutzenden das Vertrauen zu geben, aktiv zu werden.
* Seien Sie konkret bei der Erklärung von Vorteilen und machen Sie deutlich, was möglich ist und was nicht.
* Bieten Sie praktische Ratschläge und aufrichtige Ermutigung.

###### Richtlinien

✅ Machen Sie es leicht, den optimalen Weg zu finden. <br>
**Beispiel:** „Wenn Sie einen Canvas stoppen, gilt Folgendes: 1. Nutzende können den Canvas nicht mehr betreten. 2. Es werden keine weiteren Nachrichten gesendet, unabhängig davon, wo sich eine Person im Ablauf befindet. 3. **Ausnahme:** E-Mail-Canvases stoppen nicht sofort."

✅ Stellen Sie Beispiele, Anwendungsfälle und Vorlagen bereit, die die Arbeit der Nutzenden vereinfachen oder verbessern. <br>
**Beispiel:** „`IInAppMessageManagerListener` enthält auch Delegate-Methoden für Klicks auf die Nachricht selbst oder einen der Buttons. Ein häufiger Anwendungsfall wäre das Abfangen einer Nachricht, wenn ein Button oder eine Nachricht angeklickt wird, um sie weiter zu verarbeiten."

##### Menschlich

Informationstexte sind von Natur aus trocken – wir möchten, dass sich die Lesenden auf den Inhalt konzentrieren, nicht auf die Darstellung. Wir können trotzdem so schreiben, dass es unseren Lesenden hilft, die Informationen zu verarbeiten und das Wissen besser zu verinnerlichen. Seien Sie menschlich, lassen Sie Ihre Persönlichkeit durchscheinen und bleiben Sie einprägsam.

* Streben Sie einen gesprächigen statt einen formellen Ton an.
* Stellen Sie die Nutzenden in den Mittelpunkt; respektieren Sie ihre Situation und ihren emotionalen Zustand.
* Rücken Sie aktiv die menschliche Erfahrung in den Vordergrund, nicht den Maschinenzustand.

###### Richtlinien

✅ Wenden Sie Markenton und -elemente durchdacht an. <br>
**Beispiel:** „Die Integration mit Braze ist ein lohnender Prozess. Aber Sie sind klug. Sie sind hier. Offensichtlich wissen Sie das bereits."

✅ Wenden Sie [Best Practices für Barrierefreiheit](#accessibility) sowohl für visuelle als auch verbale Inhalte an. <br>
**Beispiel:** Das Ersetzen von Redewendungen wie „out-of-the-box" durch „Standard" macht Ihren Text für Personen zugänglicher, deren Muttersprache nicht Englisch ist.

✅ Bieten Sie konsistente Unterstützung entlang der gesamten User Journey. <br>
**Beispiel:** Verwenden Sie das Diátaxis-Framework, um sicherzustellen, dass Sie die Bedürfnisse verschiedener Nutzender zu verschiedenen Zeitpunkten erfüllen.

#### Barrierefreiheit {#accessibility}

Braze strebt ein inklusives Erlebnis an. Verwenden Sie die folgenden Richtlinien, um sicherzustellen, dass Ihre Lerninhalte für die [1 Milliarde Menschen](https://www.who.int/en/news-room/fact-sheets/detail/disability-and-health) mit Barrierefreiheitsbedarf zugänglich sind.

##### Allgemein

* Vermeiden Sie voreingenommene oder ableistische Sprache. Weitere Informationen finden Sie im Abschnitt [Inklusive Sprache](#inclusive-language).
* Verwenden Sie einen [Screenreader](https://support.apple.com/guide/mac-help/use-accessibility-features-mh35884/mac), um Ihre Inhalte zu testen.
* Verwenden Sie kein [kaufmännisches Und](#ampersands) (&) anstelle von „und", es sei denn, Sie beziehen sich auf UI-Elemente, die ein kaufmännisches Und verwenden.

##### Sprache und Formatierung

* Verwenden Sie [einfache Sprache](https://www.plainlanguage.gov/guidelines/).
* Stellen Sie die wichtigsten Informationen an den Anfang von Abschnitten. Verwenden Sie das journalistische Modell der [umgekehrten Pyramide](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)).
* Unterbrechen Sie Textwände, um den Lesenden das Scannen nach Informationen zu erleichtern. Verwenden Sie Absätze, [Listen](#lists), [Hinweise](#callouts-and-alerts) und [Bilder](#figures-and-other-images), um die Lesbarkeit zu verbessern.
* [Schreiben Sie kurze Sätze und Absätze](https://www.usability.gov/how-to-and-tools/methods/writing-for-the-web.html). Als allgemeine Regel sollten Sie nicht mehr als 20 Wörter pro Satz und fünf Sätze pro Absatz anstreben.
* Vermeiden Sie lateinische Abkürzungen und Phrasen, da sie schwer zu übersetzen sein können. Verwenden Sie stattdessen einfache Wörter oder Formulierungen.

##### Überschriften

* Verwenden Sie einzigartige, beschreibende und klare [Überschriften und Titel](#headings-and-titles).
* Verwenden Sie ein h1 für Seitentitel.
* Überspringen Sie keine Überschriftenebenen. Auf ein h2 sollte ein h3 folgen, und so weiter.

##### Links

* Verwenden Sie keinen Linktext wie „Mehr erfahren", „hier" oder „dieses Dokument". Weitere zu vermeidende Formulierungen finden Sie im Abschnitt [Links schreiben](#writing-links).
* Vermeiden Sie es, zwei Links direkt hintereinander in einem Satz zu platzieren. Setzen Sie ein Zeichen oder Wort dazwischen, um sie zu trennen.
* [Links zum Herunterladen von Dateien](#links-for-file-download) sollten darauf hinweisen, dass ein Klick auf den Link die Datei herunterlädt, sowie den Dateityp angeben (PDF, CSV usw.).
* Wenn es aus dem Kontext nicht klar hervorgeht, sollten Links zu Abschnitten im selben Dokument eine [Standardformulierung](#structuring-links) verwenden, die diese Aktion anzeigt.

##### Bilder, Videos und GIFs

* Stellen Sie [Alternativtext](#alt-text) für jedes Bild bereit, der die im Bild dargestellten Informationen zusammenfasst.
* Verwenden Sie Bilder nicht als einzige Möglichkeit, Informationen darzustellen. Geben Sie die Schritte, Inhalte oder andere Details, die im Bild dargestellt werden, immer auch im umgebenden Text an.
* Verwenden Sie keine Bilder von Terminalausgaben, Codebeispielen oder Text. Verwenden Sie stattdessen tatsächlichen Text.
* Stellen Sie Untertitel für Videoinhalte bereit.
* Verwenden Sie keine blinkenden Elemente in Videos oder GIFs.

##### Tabellen {#tables-1}

* Verwenden Sie immer einen einleitenden Satz, um den Zweck der Tabelle zu beschreiben.
* Vermeiden Sie Tabellen mitten in einer Liste, insbesondere in einer Schrittliste.

#### Globales Publikum {#global-audience}

Wir schreiben unsere Lerninhalte in amerikanischem Englisch. Braze ist jedoch eine globale Marke, und als solche schreiben wir für ein globales Publikum. Verwenden Sie die folgenden Richtlinien, um sicherzustellen, dass Ihre Inhalte auch dann verständlich sind, wenn Englisch nicht die Muttersprache der Lesenden ist.

1. **Schreiben Sie mit Blick auf Lokalisierung:**
  * Formatieren Sie [Daten und Uhrzeiten](#dates-and-times) auf eindeutige Weise.
  * Legen Sie keine Textüberlagerungen auf Bilder, da dieser Text nicht übersetzt werden kann.
  * Vermeiden Sie [Slang und Redewendungen](#slang-and-idioms).
  * Stellen Sie Kontext bereit. Gehen Sie nicht davon aus, dass die Lesenden wissen, wovon Sie sprechen.
2. **Schreiben Sie kurze und präzise Sätze:**
  * Verwenden Sie [einfache Sprache](https://www.plainlanguage.gov/guidelines/).
  * Definieren Sie [Abkürzungen](#abbreviations).
  * Vermeiden Sie [mehrdeutige Pronomen](#ambiguous-pronouns). Wenn ein Pronomen mehrdeutig sein könnte, ersetzen Sie es durch das entsprechende Substantiv.
3. **Seien Sie konsistent:**
  * Verwenden Sie denselben Begriff für ein Konzept bei allen Erwähnungen des Begriffs, einschließlich derselben Groß-/Kleinschreibung und Textformatierung.
  * Schreiben Sie Sätze in der Reihenfolge Subjekt + Verb + Objekt.
  * Wenn Anweisungen von einer Bedingung abhängen, stellen Sie den Bedingungssatz an den Anfang. Weitere Informationen finden Sie unter [Satzgliedstellung](#clause-order).
4. **Seien Sie inklusiv:**
  * Verwenden Sie [inklusive Sprache](#inclusive-language).
  * Verwenden Sie vielfältige [Beispielnamen](#example-names).
  * Vermeiden Sie kulturspezifischen Humor.

#### Inklusive Sprache {#inclusive-language}

Wir mögen ein B2B-Unternehmen sein, aber Menschen stehen im Mittelpunkt unserer Arbeit, und unsere Marke ist global. Wann immer wir in unseren Inhalten auf eine Person Bezug nehmen, achten wir darauf, inklusiv und rücksichtsvoll zu sein. Im Zweifelsfall konsultieren Sie diesen Abschnitt oder [The Diversity Style Guide](https://www.diversitystyleguide.com/).

##### Alter

Sofern es für Ihren Text nicht relevant ist, beziehen Sie sich nicht auf das Alter einer Person. Verwenden Sie keine Qualifizierer wie „jung" oder „alt", um eine Person oder Zielgruppe zu beschreiben.

Wenn Sie eine Altersgruppe darstellen, seien Sie beschreibend und spezifisch wie „Generation Z" statt „Jugend". Verwenden Sie keine vagen Beschreibungen wie „im Studienalter", wenn Sie stattdessen „Studierende" sagen könnten.

##### Farbe

Vermeiden Sie es, Farbbegriffe in Ihren Texten zu verwenden, es sei denn, es ist absolut notwendig, und fügen Sie in diesem Fall erklärenden Text hinzu.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Klicken Sie auf ✅ Speichern.</td><td style="width: 50%;">Klicken Sie auf das grüne Speichern-Symbol.</td></tr>
<tr><td style="width: 50%;">Klicken Sie auf das grüne Häkchen-Symbol.</td><td style="width: 50%;">Klicken Sie auf das grüne Symbol neben dem roten Abbrechen-Button.</td></tr>
<tr><td style="width: 50%;">Klicken Sie auf das grüne Symbol.</td><td style="width: 50%;"></td></tr>
</tbody>
</table>
{:/}

Verlassen Sie sich nicht auf Farbe als einzigen Indikator für interaktive Elemente. Unterstreichen Sie beispielsweise Links beim Hover oder markieren Sie ein Pflichtfeld mit einem Sternchen.

Vermeiden Sie es, sich ausschließlich auf Grün und Rot für „gut" und „schlecht" (oder häufiger „richtig" und „falsch") als Indikatoren zu verlassen. Rot-Grün-Farbenblindheit ist die häufigste Art der Farbenblindheit. Wenn Sie Farbe verwenden, um Richtig und Falsch zu kommunizieren, stellen Sie sicher, dass Sie auch anderen Text oder Symbole einbeziehen, um denselben Punkt zu vermitteln.

##### Herablassende Sprache {#condescending-language}

Wenn Sie Anweisungen schreiben oder Schritte für die Lesenden beschreiben, vermeiden Sie Wörter oder Formulierungen wie:

* einfach, wie „Eine Kampagne zu erstellen ist einfach."
* einfach, wie „...fügen Sie einfach X in Y ein"
* nur, wie „...installieren Sie nur X"
* „Das ist leicht"

Wenn jemand Schwierigkeiten mit den Schritten oder Anweisungen hat, können Ihre beiläufigen Beschreibungen herablassend wirken. Sie könnten auch unbeabsichtigt Personen von Ihrer Dokumentation ausschließen, die dies als Hinweis interpretieren, dass sie in irgendeiner Weise nicht qualifiziert genug sind, um Ihren Anweisungen zu folgen.

##### Kunden versus Klienten

Wenn Sie sich auf Unternehmensnutzende und deren Verbraucher beziehen, verwenden Sie die folgenden Begriffe entsprechend:

* **Kunden:** Marken, mit denen wir zusammenarbeiten. Bezeichnen Sie unsere Kunden niemals als „Klienten".
 * **Unternehmensnutzende:** Im Kontext der Dokumentation, wenn es wichtig ist, zwischen Nutzenden der Plattform und den Endnutzenden, die Marketingnachrichten erhalten, zu unterscheiden, verwenden Sie „Unternehmensnutzende".
* **Verbraucher:** Kunden einer Marke, mit der wir zusammenarbeiten.
* **Nutzende:** Generell reserviert für eine bestimmte Statistik, die von „Nutzer"-Metriken abhängt (wie „Kundenbindung"). Wenn Sie sich in unseren Inhalten auf „Nutzende" beziehen, versuchen Sie zunächst, spezifischer zu sein. Denken Sie an Käufer, Verbraucher, Patienten, Spieler.

##### Abteilungen und Teams

Schreiben Sie die Namen von Abteilungen oder Teams groß. Schreiben Sie „Team" oder „Abteilung" nicht groß.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Marketing, Business-Intelligence-Produktteam</td><td style="width: 50%;">marketing, business-intelligence-Produktteam</td></tr>
<tr><td style="width: 50%;">Revenue-Abteilung</td><td style="width: 50%;">Revenue-Abteilung</td></tr>
</tbody>
</table>
{:/}

##### Behinderung

Beziehen Sie sich nicht auf die Behinderung einer Person, es sei denn, es ist für Ihren Text spezifisch relevant. Seien Sie in diesem Fall rücksichtsvoll und fragen Sie, ob die betreffende Person identitätsbezogene oder personenbezogene Sprache bevorzugt. Wenn Sie sich auf eine Person mit Behinderung beziehen, verwenden Sie keine Begriffe wie „behindert" im abwertenden Sinne.

Ableistische Sprache umfasst Wörter oder Formulierungen wie „verrückt", „wahnsinnig", „blind für", „verkrüppeln", „dumm" und andere. Wählen Sie je nach Kontext alternative Wörter.

##### Krankheit

Wenn Sie eine Krankheit beschreiben, vermeiden Sie Wörter wie „leiden", „kämpfen" oder „Opfer". Streben Sie eine neutrale und sachliche Darstellung an.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Bei ihr wurde Krebs diagnostiziert.</td></tr>
<tr><td style="width: 100%;">Sie leben mit HIV.</td></tr>
<tr><td style="width: 100%;">Er hat sich von seinem Schlaganfall erholt.</td></tr>
</tbody>
</table>
{:/}


##### Inklusivität in Inhalten

Heben Sie eine vielfältige Community hervor und repräsentieren Sie sie. Seien Sie achtsam und inklusiv, wenn Sie unsere Kunden, Referenten, Branchenexperten und Braze-Teammitglieder einbeziehen.

##### Berufsbezeichnungen

Bei Berufsbezeichnungen weichen wir vom AP-Stil ab. In allen Fällen schreiben wir Berufsbezeichnungen groß, wenn wir uns auf eine bestimmte Person beziehen.

###### Berufsbezeichnung mit Firmenname

Schreiben Sie formelle Berufsbezeichnungen groß, wenn sie vor oder nach dem Namen einer Person stehen. Wir formatieren sie auf drei Arten:

1. **[Formelle Bezeichnung]** bei **[Firmenname]** + **[Vollständiger Name]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Creative Director bei PantsLabyrinth David Bowie</td><td style="width: 50%;">creative director bei PantsLabyrinth David Bowie</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[Vollständiger Name]** + Komma + **[Formelle Bezeichnung]** bei **[Firmenname]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">David Bowie, Creative Director bei PantsLabyrinth</td><td style="width: 50%;">David Bowie, creative director bei PantsLabyrinth</td></tr>
</tbody>
</table>
{:/}

{: start="3"}
3. **[Firmenname]** + **[Formelle Bezeichnung]** + **[Vollständiger Name]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">PantsLabyrinth Creative Director David Bowie</td><td style="width: 50%;">PantsLabyrinth creative director David Bowie</td></tr>
</tbody>
</table>
{:/}

###### Berufsbezeichnung ohne Firmenname

Wenn Sie sich mit formeller Bezeichnung auf eine bestimmte Person beziehen, schreiben Sie die formelle Bezeichnung und den Namen wie folgt groß:

1. **[Formelle Bezeichnung]** + **[Vollständiger Name]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CEO Robin Fenty</td><td style="width: 50%;">Chief executive officer Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[Formelle Bezeichnung]** + Komma + **[Vollständiger Name]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">SVP, Product, Robin Fenty</td><td style="width: 50%;">senior vice president, product, Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

###### Sonstiges

Formelle Bezeichnungen stehen „bei [UNTERNEHMEN]." Gründer und Mitgründer stehen „von [UNTERNEHMEN]." Formelle Bezeichnungen und Berufe allein müssen nicht großgeschrieben werden.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Ich habe dem Chief Data Officer geschrieben.</td><td style="width: 50%;">Ich habe dem Chief Data Officer geschrieben</td></tr>
<tr><td style="width: 50%;">Wir haben mit mehreren Business-Intelligence-Analysten gesprochen.</td><td style="width: 50%;">Wir haben mit mehreren Business-Intelligence-Analysten gesprochen.</td></tr>
<tr><td style="width: 50%;">Kontaktieren Sie Ihren Braze Account Manager.</td><td style="width: 50%;">Ich habe dem Chief Data Officer geschrieben Kontaktieren Sie Ihren Braze Account Manager.</td></tr>
</tbody>
</table>
{:/}

Verwenden Sie geschlechtsneutrale Berufsbezeichnungen, sofern das Geschlecht nicht bereits feststeht.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Vertriebsperson</td><td style="width: 50%;">Verkäufer/Verkäuferin</td></tr>
</tbody>
</table>
{:/}

Kürzen Sie Bezeichnungen ab, wo es angemessen ist, wie VP oder SVP, wenn die Person sich selbst so bezeichnet. Bei begrenztem Platz sind Standardabkürzungen (VP, SVP, Sr. oder Jr.) akzeptabel.

##### Geschlecht

Machen Sie keine Annahmen über das Geschlecht von Personen. Fragen Sie Personen, die in Ihren Inhalten vorkommen, wie sie sich identifizieren.

Wenn Sie sich auf Mitglieder der Community beziehen, ist „queer" akzeptabel. „Schwul" als Sammelbegriff ist es nicht. Sie können eine Gruppe von Personen als „LGBTQ" bezeichnen. Verwenden Sie dies nicht zur Beschreibung einer Einzelperson.

Wenn Sie Gruppen von Personen in Ihren Inhalten ansprechen, vermeiden Sie es, Ihr Publikum geschlechtsspezifisch anzusprechen (Beispiel: „OK, meine Damen!"). Verwenden Sie stattdessen geschlechtsneutrale Ausdrücke (Beispiel: „Legen wir los, alle zusammen!").

„Sie/ihnen/ihr" ist immer als Singular- oder Pluralpronomen in all unseren Inhalten akzeptabel.

##### Psychische Gesundheit

Psychische Gesundheit und Erkrankungen umfassen ein breites Spektrum an Zuständen. Sofern es für Ihren Text nicht relevant ist, beziehen Sie sich nicht auf die psychische Gesundheit einer Person. Vermeiden Sie stigmatisierende Wörter und Formulierungen. Verwenden Sie medizinische Begriffe nicht umgangssprachlich (Beispiel: „Der deprimierende Zustand der Dinge...").

##### Namen

Wenn Sie eine Person zum ersten Mal erwähnen, verwenden Sie ihren Vor- und vollständigen Namen. Danach verwenden Sie entweder den Vor- oder Nachnamen.

##### Pronomen

Informationen zur angemessenen Verwendung von Pronomen finden Sie im Abschnitt Sprache und Grammatik unter [Pronomen](#pronouns).

##### Ethnie, Religion und Herkunft

Beziehen Sie sich nicht auf die Ethnie, Religion oder Herkunft einer Person, es sei denn, es ist für Ihren Text relevant. In Texten, in denen Ethnie oder Herkunft eine Rolle spielen, fragen Sie die betreffende Person, wie sie sich identifiziert.

Verwenden Sie keinen Bindestrich, um doppelte Herkunft oder Religion anzuzeigen. Verwenden Sie stattdessen ein Leerzeichen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Muslim American</td><td style="width: 50%;">Muslim-American</td></tr>
<tr><td style="width: 50%;">Cuban American</td><td style="width: 50%;">Cuban-american</td></tr>
</tbody>
</table>
{:/}

Schreiben Sie die Eigennamen von Ethnien, Nationalitäten, Völkern und Stämmen groß.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Cambodian</td><td style="width: 50%;">cambodian</td></tr>
<tr><td style="width: 50%;">Black Americans</td><td style="width: 50%;">black Americans</td></tr>
</tbody>
</table>
{:/}

Schreiben Sie die Namen von Religionen oder religiösen Begriffen groß.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Bahá'í Faith</td><td style="width: 50%;">bahá'í faith</td></tr>
<tr><td style="width: 50%;">Buddhist</td><td style="width: 50%;">buddhist</td></tr>
</tbody>
</table>
{:/}

Übernehmen Sie keine Wörter oder Redewendungen, die zum African American Vernacular English gehören (on fleek, bae, lit, woke).

Übernehmen Sie keine Wörter oder Redewendungen, die spezifisch für indigene Völker sind (Beispiel: spirit animal, powwow).

#### Drittanbieterquellen {#third-party-sources}

Kopieren Sie niemals Inhalte von anderen Websites, da dies das Urheberrecht verletzen kann. Inhalte können sowohl Text als auch Bilder sein.

Anstatt Drittanbieter-Websites zu kopieren oder zu zitieren, paraphrasieren Sie den Inhalt oder stellen Sie einen Link zur Drittanbieter-Website für weitere Informationen bereit. Weitere Informationen finden Sie unter [Links zu anderen Websites](#links-to-other-sites).

### Sprache und Grammatik {#language-and-grammar}

Die Einhaltung vereinbarter Grammatik- und Mechanikregeln hilft uns, unsere Texte klar und konsistent zu halten. Dieser Abschnitt behandelt, was wir in unserer technischen Dokumentation befolgen, sofern nicht anders angegeben.

#### Abkürzungen {#abbreviations}

Abkürzungen wie Akronyme, Initialwörter und verkürzte Wörter können unsere Klarheit, Stimme und SEO beeinträchtigen.

Obwohl einige Abkürzungen allgemein bekannt sind, sind andere nicht gut bekannt oder nur einer bestimmten Kundengruppe vertraut. Nutzen Sie Ihr bestes Urteilsvermögen, und als allgemeine Regel ist es in Ordnung, eine Abkürzung nicht auszuschreiben, wenn sie im [American Heritage Dictionary](https://ahdictionary.com/) aufgeführt ist.

Wenn eine Abkürzung nicht allgemein bekannt ist, schreiben Sie sie bei der ersten Erwähnung aus, gefolgt von der Abkürzung in Klammern. Verwenden Sie bei allen weiteren Erwähnungen des Begriffs die Abkürzung.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Unbekannte Abkürzungen bei der ersten Erwähnung ausschreiben</em></th><th style="width: 50%;">Falsch: <em>Bekannte Abkürzungen ausschreiben</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Top-Level-Domain (TLD)</td><td style="width: 50%;">Portable Document Format (PDF)</td></tr>
<tr><td style="width: 50%;">Universally Unique Identifier (UUID)</td><td style="width: 50%;">Universal Serial Bus (USB)</td></tr>
</tbody>
</table>
{:/}


Behandeln Sie Abkürzungen wie reguläre Wörter, wenn Sie sie in den Plural setzen, und fügen Sie keinen Apostroph hinzu – zum Beispiel APIs und SDKs. Dasselbe gilt für den Artikel – schauen Sie sich an, wie die Abkürzung ausgesprochen wird. Wenn eine Abkürzung mit einem Vokalklang beginnt, verwenden Sie den entsprechenden Artikel; bei Konsonantenklängen ebenso.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig: <em>Artikel je nach Aussprache der Abkürzung verwenden, nicht nach Schreibweise</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">ein ISP</td></tr>
<tr><td style="width: 100%;">eine DLL</td></tr>
<tr><td style="width: 100%;">eine HTML-Website</td></tr>
<tr><td style="width: 100%;">eine CSV-Datei</td></tr>
</tbody>
</table>
{:/}

#### Aktive Stimme {#active-voice}

Wir verwenden bei Braze nach Möglichkeit die aktive Stimme. Die aktive Stimme ist unser Goldstandard. Vermeiden Sie die passive Stimme, bei der es schwierig sein kann, festzustellen, wer oder was eine bestimmte Aktion ausführt.

Um zu prüfen, ob Ihr Satz im Passiv steht, fügen Sie „von jemandem" nach dem Verb ein. Wenn der Satz Sinn ergibt, steht er höchstwahrscheinlich im Passiv.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Aktive Stimme verwenden</em></th><th style="width: 50%;">Falsch: <em>Passive Stimme verwenden, wenn möglich</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Braze verbindet Verbraucher mit den Marken, die sie lieben.</td><td style="width: 50%;">Verbraucher werden mit den Marken verbunden, die sie lieben.</td></tr>
<tr><td style="width: 50%;">Braze verlangt von Mitarbeitenden, ihre Adressen aktuell zu halten.</td><td style="width: 50%;">Mitarbeitende sind verpflichtet, ihre Adressen aktuell zu halten.</td></tr>
<tr><td style="width: 50%;">Unternehmensadministratoren können Authentifizierungsanforderungen für die Anmeldung bei Braze konfigurieren.</td><td style="width: 50%;">Authentifizierungsanforderungen für die Anmeldung bei Braze können von Unternehmensadministratoren konfiguriert werden.</td></tr>
</tbody>
</table>
{:/}

##### Ausnahmen

Es ist in Ordnung, die passive Stimme in folgenden Fällen zu verwenden:

* Um ein Subjekt abzuschwächen, in der Regel um zu vermeiden, den Lesenden die Schuld zu geben:
  - **Richtig:** Es wurden zwei Fehler in der E-Mail gefunden.
  - **Falsch:** Sie haben zwei Fehler in der E-Mail erstellt.
* Wenn es nicht wichtig ist zu wissen, wer für die Aktion verantwortlich ist:
  - **Richtig:** Dieser Artikel wurde zuletzt im Dezember 2020 aktualisiert.

#### Artikel {#articles}

Verwenden Sie die Artikel „ein", „eine" und „der/die/das", um Ihre Texte klar zu gestalten und die Übersetzung zu erleichtern. Verwenden Sie „der/die/das" vor einem bestimmten Singular- oder Pluralnomen und „ein" oder „eine" vor einem unbestimmten Singularnomen.

Um zu bestimmen, ob Sie „ein" oder „eine" verwenden sollten, schauen Sie sich die Aussprache des folgenden Wortes an. Verwenden Sie „ein" vor einem Konsonantenklang und „eine" vor einem Vokalklang. Dieselben Richtlinien gelten für [Abkürzungen](#abbreviations).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig: <em>Artikel je nach Aussprache des folgenden Wortes verwenden.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">eine Stunde</td></tr>
<tr><td style="width: 100%;">eine Minute</td></tr>
<tr><td style="width: 100%;">ein FAQ-Artikel</td></tr>
<tr><td style="width: 100%;">ein LAB-Kurs</td></tr>
</tbody>
</table>
{:/}

#### Pronomen {#pronouns}

##### Personalpronomen

Verwenden Sie nach Möglichkeit die Anrede „Sie".

Bezeichnen Sie Braze-Kunden in externen Texten nicht als „Nutzer", sondern sprechen Sie die Lesenden direkt mit „Sie" an. Um sich auf die Kunden unserer Kunden zu beziehen, verwenden Sie „Ihre Verbraucher" oder, wenn es sich um Nutzerstatistiken handelt, „Ihre Nutzer".

Vermeiden Sie Pronomen der ersten Person (ich, wir, uns, unser), außer in folgenden Fällen:

* Einträge in FAQs. Zum Beispiel: „Wie setze ich mein Passwort zurück?".
* Verwendung von „wir", um sich auf Braze als Organisation zu beziehen.
 * Wenn unklar sein könnte, auf wen sich „wir" bezieht, nennen Sie zuerst Braze beim Namen und verwenden Sie dann „wir" bei nachfolgenden Erwähnungen.

##### Geschlechtsneutrale Pronomen

Verwenden Sie die Pronomen, die Ihre Personen verwenden. Bei Unsicherheit verwenden Sie „sie" und „ihr" als Singular-Pronomen. Verwenden Sie nicht „er/sie" als Alternative zum Singular-„sie".

Verwenden Sie geschlechtsspezifische Pronomen (er/sie, ihm/ihr, sein/ihr) nur, wenn die Person, auf die Sie sich beziehen, tatsächlich dieses Geschlecht hat.

##### Mehrdeutige Pronomen {#ambiguous-pronouns}

Pronomen ersetzen Substantive. Das Wort, auf das sich ein Pronomen bezieht, wird als Bezugswort bezeichnet. Wenn Sie Anweisungen oder Lernmaterial schreiben, stellen Sie sicher, dass die Bezüge zwischen einem Pronomen und seinem Bezugswort klar sind. Dies kann erfordern, Subjekte zu wiederholen, um die Bedeutung klarzustellen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Sicherstellen, dass ein Pronomen klar auf sein Bezugswort verweist</em></th><th style="width: 50%;">Falsch: <em>Mehrdeutige Pronomenverweise verwenden</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Wenn Sie Text in das Feld eingeben, ändert sich der Text nicht.</td><td style="width: 50%;">Wenn Sie Text in das Feld eingeben, ändert er sich nicht.</td></tr>
<tr><td style="width: 50%;">Sie sagte Sarah, dass Sarahs Antwort falsch war.</td><td style="width: 50%;">Sie sagte Sarah, dass ihre Antwort falsch war.</td></tr>
<tr><td style="width: 50%;">Sie können eine archivierte Kampagne nicht bearbeiten. Heben Sie die Archivierung einer Kampagne auf, um sie zu bearbeiten.</td><td style="width: 50%;">Sie können eine archivierte Kampagne nicht bearbeiten. Heben Sie sie auf, um sie zu bearbeiten.</td></tr>
</tbody>
</table>
{:/}

##### Optionale Pronomen

Um Ihrem Text zusätzliche Klarheit zu verleihen und die Lokalisierung zu unterstützen, verwenden Sie Pronomen wie „das", „welches" und „wer".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>„Das", „welches" und „wer" für zusätzliche Klarheit verwenden.</em></th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Rechtsklicken Sie auf den Link, den Sie öffnen möchten.</td><td style="width: 50%;">Rechtsklicken Sie auf den Link, den Sie öffnen möchten.</td></tr>
<tr><td style="width: 50%;">Von hier aus können Sie die Tinyclues-Kohorte auswählen, die Sie einbeziehen möchten.</td><td style="width: 50%;">Von hier aus können Sie eine Tinyclues-Kohorte auswählen, die Sie einbeziehen möchten.</td></tr>
</tbody>
</table>
{:/}

#### Groß- und Kleinschreibung {#capitalization}

Vermeiden Sie unnötige Großschreibung. In den meisten Fällen verwenden Sie Satzschreibung. Titelschreibung sollte nur für Eigennamen oder Feature-Namen verwendet werden.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Kleinschreibung für Website-URLs und E-Mail-Adressen verwenden</em></th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">www.braze.com/docs</td><td style="width: 50%;">www.Braze.com/docs</td></tr>
<tr><td style="width: 50%;">sample@email.com</td><td style="width: 50%;">SAMPLE@EMAIL.COM</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Himmelsrichtungen kleinschreiben</em></th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Norden, Süden, Osten, Westen</td><td style="width: 50%;">norden, süden, osten, westen</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Bestimmte Regionen großschreiben und Großbuchstaben für abgekürzte Regionen verwenden</em></th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">der Nordwesten</td><td style="width: 50%;">der nordwesten</td></tr>
<tr><td style="width: 50%;">Südliches Connecticut</td><td style="width: 50%;">südliches Connecticut</td></tr>
<tr><td style="width: 50%;">Osteuropa</td><td style="width: 50%;">osteuropa</td></tr>
<tr><td style="width: 50%;">APAC, EMEA</td><td style="width: 50%;">Apac, emea</td></tr>
</tbody>
</table>
{:/}

##### Marken und Produkte

Wenn Sie sich auf eine Marke oder ein Produkt beziehen, verwenden Sie die Groß-/Kleinschreibung, die die Marke verwendet. In den meisten Fällen schreiben Sie die Namen von Marken (Grindr, Walmart) und Produkten (Benchmarks, Looker Blocks) groß. Es ist in Ordnung, einen Satz mit Kleinbuchstaben zu beginnen, wenn das erste Wort der stilisierte Name einer Marke wie eBay oder iTunes ist.

Bei Binnenmajuskeln beziehen Sie sich immer auf die von der Marke bevorzugte Schreibweise in Druckform (OkCupid, YouTube). Verwenden Sie keine Binnenmajuskeln, die nur in Logos oder grafischen Gestaltungen erscheinen (Amazon).

#### Satzgliedstellung {#clause-order}

Wenn Sie den Lesenden mitteilen möchten, dass sie etwas unter bestimmten Umständen tun sollen, erwähnen Sie die Umstände, bevor Sie die Anweisung geben. So können die Lesenden die Anweisung überspringen, wenn die Umstände nicht zutreffen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Für Schritte zur Fehlerbehebung siehe Kampagnen-FAQs.</td><td style="width: 50%;">Siehe Kampagnen-FAQs für Schritte zur Fehlerbehebung.</td></tr>
<tr><td style="width: 50%;">Um Ihre Kampagne zu archivieren, klicken Sie auf das Zahnradsymbol und wählen Sie Archivieren.</td><td style="width: 50%;">Klicken Sie auf das Zahnradsymbol und wählen Sie Archivieren, um Ihre Kampagne zu archivieren.</td></tr>
</tbody>
</table>
{:/}

#### Zusammengesetzte Formen {#combining-forms}

[Setzen Sie einen Bindestrich](#hyphens) bei zusammengesetzten Formen, wenn die Phrase als Adjektiv vor dem Substantiv verwendet wird.

**Beispiel:** Ein einzigartiges Produkt

#### Kontraktionen {#contractions}

Eine Kontraktion ist eine verkürzte Version eines Wortes oder einer Phrase. Im Deutschen sind Kontraktionen weniger üblich als im Englischen. Verwenden Sie einen natürlichen, zugänglichen Ton, aber vermeiden Sie umgangssprachliche Verkürzungen, die den Lesefluss und die Verständlichkeit des Satzes stören könnten.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Natürlichen Ton verwenden</em></th><th style="width: 50%;">Falsch: <em>Umgangssprachliche Verkürzungen verwenden</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Wenn Sie Administrator sind, können Sie die Kontaktinformationen Ihres Unternehmens verwalten.</td><td style="width: 50%;">Braze unterstützt jetzt die Shoptify-Integration.</td></tr>
<tr><td style="width: 50%;">Sie können eine archivierte Kampagne nicht bearbeiten.</td><td style="width: 50%;">Sie hätten die eingeschränkte Upload-Größe möglicherweise nicht gesehen.</td></tr>
</tbody>
</table>
{:/}

#### Hängende und fehlplatzierte Modifikatoren {#dangling-and-misplaced-modifiers}

Modifikatoren sind Wörter oder Phrasen, die andere Wörter oder Phrasen modifizieren. Ein hängender Modifikator modifiziert kein Subjekt im Satz. Ein fehlplatzierter Modifikator steht weit entfernt von dem Subjekt, das er modifizieren soll. Im Wesentlichen können hängende und fehlplatzierte Modifikatoren Verwirrung stiften, indem sie sich mit dem falschen Teil des Satzes verbinden.

Das Schreiben in aktiver Stimme hilft, die Verwendung von hängenden und fehlplatzierten Modifikatoren zu vermeiden. Stellen Sie sicher, dass Sie einen Modifikator verwenden, der klar modifiziert.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Sätze kurz und prägnant halten. Aktive Stimme verwenden.</em></th><th style="width: 50%;">Falsch: <em>Lange Sätze mit Modifikatoren verwenden, die Verwirrung stiften können</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Kunden müssen ihre SAML-Einstellungen einrichten.</td><td style="width: 50%;">Sie haben möglicherweise Testnachrichten in Ihren Kampagnen, die gelöscht werden können.</td></tr>
<tr><td style="width: 50%;">Stellen Sie sicher, dass Sie Ihre Kampagnenentwürfe speichern.</td><td style="width: 50%;">Auf dem Heimweg fand Sarah eine goldene Herren-Stoppuhr.</td></tr>
</tbody>
</table>
{:/}

#### Präpositionen {#prepositions}

Es ist nichts falsch daran, einen Satz mit einer Präposition zu beenden, wenn es die Lesbarkeit verbessert. Platzieren Sie eine Präposition oder Präpositionalphrase dort, wo sie im Satz am meisten Sinn ergibt. Wenn Sie Schwierigkeiten haben, lesen Sie den Satz laut vor und prüfen Sie, ob er natürlich klingt.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Jede Option entspricht der Priorität, in der die Benachrichtigung angezeigt wird.</td><td style="width: 50%;">Jede Option entspricht der Priorität, in welcher die Benachrichtigung erscheint.</td></tr>
<tr><td style="width: 50%;">Weitere Details finden Sie in der SDK-Dokumentation für die Plattform, mit der Sie arbeiten.</td><td style="width: 50%;">Weitere Details finden Sie in der SDK-Dokumentation für die Plattform, mit welcher Sie arbeiten.</td></tr>
</tbody>
</table>
{:/}

#### Präsens {#present-tense}

Verwenden Sie Präsens statt Futur. Präsens vermittelt Unmittelbarkeit und demonstriert Zuversicht. Vermeiden Sie die Verwendung von „wird" oder hypothetischem „würde", insbesondere wenn Sie sich auf das Ergebnis einer Nutzeraktion beziehen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Archivierte Abo-Gruppen können nicht bearbeitet werden und erscheinen nicht mehr in Segment-Filtern.</td><td style="width: 50%;">Archivierte Abo-Gruppen können nicht bearbeitet werden und werden nicht mehr in Segment-Filtern erscheinen.</td></tr>
<tr><td style="width: 50%;">Die Verwendung eines Shortcodes ist der zuverlässigste Nummerntyp für das Einfügen von Links.</td><td style="width: 50%;">Die Verwendung eines Shortcodes wäre der zuverlässigste Nummerntyp für das Einfügen von Links.</td></tr>
</tbody>
</table>
{:/}

Verwenden Sie Futur nur, wenn Sie tatsächlich über die Zukunft sprechen. Vermeiden Sie Vorhersagen über [zukünftige Funktionen](#describing-limitations).

#### Vulgäre Sprache {#profanity}

Halten Sie es jugendfrei. Das hat weniger mit Moral zu tun als mit der Tatsache, dass vulgäre Sprache bei einem so breiten und internationalen Publikum wie dem unseren spaltend und abstoßend wirken kann. Es gibt auch ein Argument dafür, dass Vulgärsprache manchmal eine Tarnung für halbgare Texte ist. Das ist einfach nicht unser Stil.

#### Plurale in Klammern {#plurals-in-parentheses}

Verwenden Sie keine Plurale in Klammern. Verwenden Sie stattdessen die Plural- oder Singularform des Wortes.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Passen Sie Ihre Kampagne mit den folgenden Filtern an.</td><td style="width: 50%;">Passen Sie Ihre Kampagne mit dem/den folgenden Filter(n) an.</td></tr>
</tbody>
</table>
{:/}

#### Zweite und erste Person {#second-person-and-first-person}

Verwenden Sie in Ihren Anweisungen die zweite Person statt der ersten Person – „Sie" statt „wir".

Beziehen Sie sich auf die Lesenden als diejenigen, die die Aktion ausführen. Schlagen Sie einen gesprächigen Ton an – die meisten Lesenden greifen auf Dokumentation zurück, wenn sie keinen unmittelbaren Zugang zu einem Support-Mitarbeitenden haben. Lassen Sie es so wirken, als würde der Artikel mit ihnen sprechen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Wenn Sie eine Variante hinzufügen möchten...</td><td style="width: 50%;">Wenn wir eine Variante hinzufügen möchten...</td></tr>
</tbody>
</table>
{:/}

Wenn Sie den Lesenden auffordern, etwas zu tun, können Sie das „Sie" weglassen und den Imperativ verwenden.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Laden Sie die CSV-Datei hoch.</td><td style="width: 50%;">Sie können die CSV-Datei hochladen.</td></tr>
<tr><td style="width: 50%;">Wählen Sie Absenden.</td><td style="width: 50%;">Sie müssen Absenden auswählen.</td></tr>
</tbody>
</table>
{:/}

Wenn Sie die zweite Person verwenden, stellen Sie sicher, dass Sie wissen, wer die Zielgruppe des Dokuments ist, und seien Sie konsistent darin, wen Sie ansprechen.

#### Slang und Redewendungen {#slang-and-idioms}

Wir sind ein sachlicher Haufen. Vermeiden Sie trendigen Slang oder Redewendungen, die zu spezifisch für ein einzelnes Publikum sind. Das kann Materialien auch schnell veralten lassen und die Lokalisierung von Inhalten erschweren.

#### Rechtschreibung {#spelling}

Verwenden Sie die amerikanische englische Schreibweise für Wörter, die sich im britischen Englisch unterscheiden. Wenn Sie sich nicht sicher sind, wie ein Wort geschrieben wird, schauen Sie zuerst im [Glossar](#glossary) nach. Wenn das Wort dort nicht aufgeführt ist, schauen Sie im [Merriam-Webster's Collegiate Dictionary](https://www.merriam-webster.com/) nach.

Für Wörter mit Akzenten oder Sonderzeichen stellen Sie sicher, dass Sie die Wörterbuchschreibweise korrekt befolgen. In einigen Fällen kann das unbeabsichtigte Weglassen dieser Akzente zu einem anderen Wort führen. Zum Beispiel bedeutet „resume" im Englischen „wieder aufnehmen", während „résumé" ein Lebenslauf ist.

### Zeichensetzung {#punctuation}

#### Kaufmännisches Und {#ampersands}

Verwenden Sie kein kaufmännisches Und (&) anstelle von „und" in Text oder Überschriften, es sei denn, Sie beziehen sich direkt auf die Benutzeroberfläche.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Drag-And-Drop-Editor</td><td style="width: 50%;">Drag & Drop Editor</td></tr>
<tr><td style="width: 50%;">SMS und MMS</td><td style="width: 50%;">SMS & MMS</td></tr>
</tbody>
</table>
{:/}

#### Apostrophe {#apostrophes}

Wir verwenden einen Apostroph am häufigsten, um ein Substantiv possessiv zu machen.

* Für Singularnomen, die auf S enden, ist es in Ordnung, ein weiteres S nach dem Apostroph zu setzen.
 * **Beispiel:** Chris's, business's, alias's
* Für Pluralnomen, die auf S enden, fügen Sie einen Apostroph hinzu, aber kein zusätzliches S.
 * **Beispiel:** users'

#### Doppelpunkte {#colons}

Verwenden Sie Doppelpunkte am Ende einer einleitenden Phrase, die einer Liste oder einem Beispiel vorangeht. Ihr einleitender Satz sollte als vollständiger Satz allein stehen können. Dies dient sowohl der Barrierefreiheit als auch der Lokalisierung, da es schwierig ist, Satzfragmente zu übersetzen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Die allgemeine Struktur ist wie folgt:</td><td style="width: 50%;">Die allgemeine Struktur ist:</td></tr>
</tbody>
</table>
{:/}

Wenn der Text vor dem Doppelpunkt fett ist, formatieren Sie den Doppelpunkt ebenfalls fett.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Geplant:</strong> Zeitbasierter Eintritt.</td><td style="width: 50%;"><strong>Geplant</strong>: Zeitbasierter Eintritt.</td></tr>
</tbody>
</table>
{:/}

Wenn der Text vor dem Doppelpunkt Codetext ist, schließen Sie den Doppelpunkt nicht in den Codetext ein, es sei denn, er ist Teil des Code-Elements.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>user_alias_label</code>: Ein gemeinsames Label, um Nutzer-Aliase zu gruppieren.</td><td style="width: 50%;"><code>user_alias_label:</code> Ein gemeinsames Label, um Nutzer-Aliase zu gruppieren.</td></tr>
</tbody>
</table>
{:/}

Sie können auch einen Doppelpunkt verwenden, um zwei verwandte Phrasen in einem Satz zu verbinden. Verwenden Sie Doppelpunkte dafür jedoch sparsam. Zwei Sätze sind in der Regel besser lesbar.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Nächste Woche steht an: Wir machen eine Tour durch das West Village.</td></tr>
</tbody>
</table>
{:/}


#### Kommas {#commas}

Braze verwendet das Oxford-Komma (Serienkomma) beim Schreiben von Anweisungen oder Lerninhalten. Verwenden Sie ein Komma vor der letzten Konjunktion, um Elemente in einer Reihe zu trennen.

Verwenden Sie ein Komma nach einer einleitenden Phrase.

Wenn eine koordinierende Konjunktion (Wörter wie „und", „aber", „oder", „doch", „also") zwei unabhängige Sätze trennt, setzen Sie das Komma nach dem ersten Satz und vor die Konjunktion. Dieses Komma ist jedoch nicht notwendig, wenn beide Sätze kurz sind.

Zum Beispiel sind hier zwei unabhängige Sätze:

* „Alle Felder sind optional."
* „Sie müssen mindestens ein Feld angeben."

Der Satz mit der koordinierenden Konjunktion „aber" lautet: „Alle Felder sind optional, aber Sie müssen mindestens ein Feld angeben."

Wenn ein unabhängiger Satz und ein abhängiger Satz im selben Satz verwendet werden, verwenden Sie kein Komma, um sie zu trennen. Verwenden Sie ein Komma in diesem Szenario nur, wenn der Satz ohne die Kommasetzung falsch interpretiert werden könnte.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Push-Abo-Status sind Filter und können es Nutzenden ermöglichen, Benachrichtigungseinstellungen zu bearbeiten.</td><td style="width: 50%;">Push-Abo-Status sind Filter, und können es Nutzenden ermöglichen, Benachrichtigungseinstellungen zu bearbeiten.</td></tr>
</tbody>
</table>
{:/}

#### Striche {#dashes}

##### Geviertstrich

Verwenden Sie einen Geviertstrich (—), wenn Sie einen Strich in einem Satz verwenden, um einen separaten Gedanken oder eine Unterbrechung anzuzeigen. Setzen Sie keine Leerzeichen vor oder nach dem Geviertstrich. Verwenden Sie keinen Geviertstrich, wo ein Komma oder eine Klammer genauso gut funktionieren würde.

So geben Sie einen Geviertstrich ein:

* **macOS:** Drücken Sie Option + Shift + Bindestrich.
* **Windows:** Schalten Sie Num Lock ein, halten Sie dann die linke Alt-Taste gedrückt und geben Sie 0151 auf dem Ziffernblock ein.

##### Halbgeviertstrich {#en-dash}

Verwenden Sie einen Halbgeviertstrich (–) für Zahlenbereiche, als Minuszeichen oder für negative Zahlen. Setzen Sie keine Leerzeichen vor oder nach dem Halbgeviertstrich, außer wenn er als Minuszeichen verwendet wird. Verwenden Sie keinen Bindestrich (-).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Halbgeviertstrich für Zahlenbereiche verwenden</em></th><th style="width: 50%;">Falsch: <em>Bindestrich verwenden</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">2018–2021</td><td style="width: 50%;">2018-2021</td></tr>
</tbody>
</table>
{:/}

Verwenden Sie keinen Halbgeviertstrich für Zeitbereiche. Weitere Details finden Sie im Abschnitt [Daten und Uhrzeiten](#dates-and-times).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Halbgeviertstrich als Minuszeichen verwenden und Leerzeichen um den Halbgeviertstrich setzen</em></th><th style="width: 50%;">Falsch: <em>Bindestrich verwenden</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">15 – 5 = 10</td><td style="width: 50%;">15-5=10</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Halbgeviertstrich für negative Zahlen verwenden</em></th><th style="width: 50%;">Falsch: <em>Bindestrich verwenden</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">–30</td><td style="width: 50%;">-30</td></tr>
</tbody>
</table>
{:/}

So geben Sie einen Halbgeviertstrich ein:

* **macOS:** Drücken Sie Option + Bindestrich.
* **Windows:** Schalten Sie Num Lock ein, halten Sie dann die linke Alt-Taste gedrückt und geben Sie 0150 auf dem Ziffernblock ein.

#### Auslassungspunkte {#ellipses}

Auslassungspunkte sind eine Reihe von drei Punkten (...), die eine Auslassung eines oder mehrerer Wörter anzeigen. Vermeiden Sie im Allgemeinen die Verwendung von Auslassungspunkten beim Schreiben von Anweisungen oder Lerninhalten.

#### Ausrufezeichen {#exclamation-points}

Ein Ausrufezeichen kann sparsam für einen informellen Ton verwendet werden. Vermeiden Sie jedoch die übermäßige Verwendung von Ausrufezeichen im Text. Erwägen Sie stattdessen die Verwendung von [Hinweisen](#callouts-and-alerts).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Ausrufezeichen für einen informellen Ton bei Erinnerungen und Einführungen verwenden</em></th><th style="width: 50%;">Falsch: <em>Ausrufezeichen verwenden, um Lesende vor Warnungen oder Vorsicht zu warnen</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Vergessen Sie nicht, Ihre Änderungen zu speichern, bevor Sie die Seite verlassen!</td><td style="width: 50%;">Nutzende müssen eine oder mehrere Nachrichten von einem Schritt erhalten, um als eindeutige Empfänger:innen gezählt zu werden!</td></tr>
</tbody>
</table>
{:/}

#### Bindestriche {#hyphens}

Bindestriche können den Lesenden helfen, mehr Klarheit in einem Satz zu gewinnen, indem sie Wörter in einer Phrase miteinander verbinden. Hier sind einige Richtlinien, um es richtig zu machen.

Verwenden Sie Bindestriche für zusammengesetzte Modifikatoren, die den Lesenden helfen, das Subjekt klarer zu verstehen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Echtzeit-Datenstreaming</td></tr>
</tbody>
</table>
{:/}

Verwenden Sie Bindestriche, um eine Phrase zu verbinden, mit einem Leerzeichen zwischen dem Modifikator und dem Subjekt.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">All-in-one-Lösungen</td></tr>
</tbody>
</table>
{:/}

Verwenden Sie Bindestriche für eine Phrase, die ein Subjekt modifiziert. Es ist nicht nötig, einen Bindestrich zu verwenden, wenn die Phrase das Subjekt ist.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Es war eine allgemein bekannte Tatsache.</td><td style="width: 50%;">Diese Tatsache ist allgemein-bekannt.</td></tr>
</tbody>
</table>
{:/}

Verwenden Sie keine Bindestriche anstelle eines Geviertstrichs, um eine Pause in einem Satz zu erzeugen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">...Drittanbieter-Integrationen—wie Slack—und automatisieren...</td><td style="width: 50%;">...Drittanbieter-Integrationen-wie Slack-und automatisieren...</td></tr>
</tbody>
</table>
{:/}

Verwenden Sie keinen Bindestrich nach einem Adverb. Lassen Sie die Wörter getrennt.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Hastig gemacht</td><td style="width: 50%;">Hastig-gemacht</td></tr>
</tbody>
</table>
{:/}

#### Klammern {#parentheses}

Verwenden Sie Klammern sparsam. Setzen Sie niemals wichtige Informationen in Klammern, da einige Lesende Inhalte in Klammern überspringen.

Für weniger wichtige Einschübe erwägen Sie, den Satz umzuformulieren, um die Klammern zu entfernen. Sie können die Phrase oder den Satz beispielsweise mit Kommas, Strichen, Semikolons oder durch Hinzufügen eines neuen Satzes abtrennen.

Wenn eine Klammer Teil eines größeren Satzes ist, setzen Sie den Punkt außerhalb der Klammer. Wenn die Klammer einen vollständigen Satz enthält, setzen Sie den Punkt innerhalb.

**Verwandter Abschnitt:** [Plurale in Klammern](#plurals-in-parentheses)

#### Punkte {#periods}

Verwenden Sie einen Punkt, um Sätze zu beenden. Verwenden Sie keinen Punkt, um Schlagzeilen, Überschriften, Unterüberschriften oder UI-Elemente zu beenden.

Richtlinien zur Verwendung von Punkten bei Listenelementen finden Sie unter [Listen](#lists).

#### Semikolons {#semicolons}

Semikolons eignen sich hervorragend, um einen längeren, komplizierteren Satz aufzuteilen. Verwenden Sie ein Semikolon, um zwei unabhängige Sätze zu trennen, die thematisch eng verwandt sind.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig: <em>Semikolon verwenden, um einen Satz mit zwei verwandten unabhängigen Sätzen aufzuteilen</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Die Katze schlief durch den Sturm; der Hund kauerte unter dem Bett.</td></tr>
</tbody>
</table>
{:/}

Semikolons können verwendet werden, um Listenelemente zu trennen, wenn eines (oder mehrere) der Listenelemente ein Komma enthält.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig: <em>Semikolon verwenden, um einen längeren Satz aufzuteilen</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Jane Lang, unsere Moderatorin; Simon Mayer, CEO und Mitgründer von PantsLabyrinth; und Kara Seberg, CMO von Yachtr.</td></tr>
</tbody>
</table>
{:/}

#### Schrägstriche {#slashes}

Es gibt zwei Arten von Schrägstrichen: rückwärts (\\) und vorwärts (/). Verwenden Sie keine Schrägstriche, um alternative Wörter oder Beispiele anzuzeigen („und/oder").

Verwenden Sie Schrägstriche nach Bedarf in Dateipfaden und URLs.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Schrägstrich für Dateipfade verwenden</em></th><th style="width: 50%;">Falsch: <em>Schrägstrich zum Trennen von Alternativen verwenden</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/campaigns/data_series</code></td><td style="width: 50%;">Sie/Ihre Kunden</td></tr>
</tbody>
</table>
{:/}

#### Anführungszeichen {#quotation-marks}

Es gibt zwei Arten von Anführungszeichen: gerade (" ") und typografische („ "). Punkte und Kommas stehen innerhalb der Anführungszeichen. Eine Ausnahme besteht, wenn die Anführungszeichen exakte Informationen wie eine Zeichenkette enthalten. Verwenden Sie Anführungszeichen, wenn Sie Nutzende anweisen, eine bestimmte Zeichenkette in ein Textfeld einzugeben.

{% alert note %}

Bei der Beschreibung der Suchsyntax werden Anführungszeichen häufig verwendet, um die Suche nach exaktem Text zu kennzeichnen. Verwenden Sie in diesem Fall eckige Klammern um die Zeichenkette und Anführungszeichen wie von der Suchsyntax gefordert. Zum Beispiel: <br><br>

*Setzen Sie Anführungszeichen um ein beliebiges Wort oder eine Phrase, wie ["Testsegment"], und wir zeigen Ergebnisse an, die nur diese exakten Wörter oder Phrasen enthalten.*

{% endalert %}

Codebeispiele müssen gerade Anführungszeichen verwenden. Weitere Informationen zur Formatierung von Code im Text finden Sie unter [Code im Text](#code-in-text).

### Technische Dokumentation {#technical-documentation}

#### API-Endpunkte {#api-endpoints}

Im Allgemeinen sollte die Dokumentation für API-Endpunkte den Richtlinien in diesem Style Guide folgen. Es gibt jedoch Nischenthemen, die möglicherweise andere Inhaltsrichtlinien erfordern, die in diesem Dokument aufgeführt sind. Weitere Informationen zur Formatierung und Referenzierung von Endpunkten finden Sie in den [Richtlinien zur API-Endpunkt-Dokumentation]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/).

#### Garantien vermeiden {#avoid-guarantees}

Unsere Dokumentation muss davon absehen, Zusagen zu machen, die möglicherweise rechtliche Konsequenzen haben könnten. Vermeiden Sie die Verwendung definitiver Begriffe wie „garantieren" oder „sicherstellen". Verwenden Sie stattdessen zukunftsgerichtete Aussagen wie „Entwickelt für" oder „Vorgesehen für", um die Fähigkeiten und Absichten des Produkts genau zu vermitteln.

#### Beschreibung von Interaktionen mit der UI {#describing-interactions-with-the-ui}

Wenn Sie sich auf UI-Elemente beziehen, passen Sie die Groß-/Kleinschreibung an die Darstellung in der UI an. Wenn ein Label jedoch komplett in Großbuchstaben steht, verwenden Sie Satzschreibung (Ausnahme: kurze Labels wie AND- oder OR-Operatoren).

Wenn Sie Lesende anweisen, mit der UI zu interagieren, formatieren Sie das UI-Element, mit dem sie interagieren, fett. Für Zeichenketten, die Nutzende in ein Feld eingeben würden, verwenden Sie Anführungszeichen.

Hinweise zu den Verben, die bei der Beschreibung von Interaktionen mit der UI verwendet werden sollten, finden Sie in der folgenden Tabelle:

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 20%;">
<col style="width: 40%;">
<col style="width: 40%;">
</colgroup>
<thead>
<tr><th>Verb</th><th>Verwendung</th><th>Beispiel</th></tr>
</thead>
<tbody>
<tr><td>Öffnen</td><td><ul><li>Apps öffnen</li><li>Dateien und Ordner öffnen</li></ul></td><td><ul><li>Öffnen Sie Droidboy.</li><li>Öffnen Sie die Datei braze.xml.</li></ul></td></tr>
<tr><td>Schließen</td><td><ul><li>Apps schließen</li><li>Dateien und Ordner schließen</li></ul></td><td><ul><li>Schließen Sie Droidboy.</li><li>Schließen Sie die Datei braze.xml.</li></ul></td></tr>
<tr><td>Gehen Sie zu</td><td><ul><li>Zu einer bestimmten Seite in der UI navigieren (Tab, Seite, Abschnitt)</li><li>Zu einer Webseite navigieren</li></ul></td><td><ul><li>Gehen Sie zur Seite <strong>Segments</strong> und klicken Sie auf…</li><li>Gehen Sie zu example.com, um sich anzumelden.</li></ul></td></tr>
<tr><td>&gt;</td><td>Einer Abfolge von Schritten folgen, wenn alle Schritte vom gleichen Typ sind.</td><td>Gehen Sie zu <strong>Segments</strong> &gt; <strong>Segment Insights</strong>.</td></tr>
<tr><td>Wählen</td><td>Eine Entscheidung treffen, die subjektiv, strategisch, offen oder komplex ist.</td><td>Wählen Sie eine Kampagnenstrategie.</td></tr>
<tr><td>Auswählen</td><td><ul><li>Ein Kontrollkästchen auswählen</li><li>Elemente aus einem Dropdown auswählen</li><li>Einen Tab auswählen</li><li>Eine einfache Entscheidung treffen</li></ul></td><td><ul><li>Wählen Sie <strong>Passwort anzeigen</strong> aus.</li><li>Wählen Sie einen Datentyp aus dem Dropdown aus.</li><li>Wählen Sie auf der Seite <strong>Einstellungen verwalten</strong> den Tab <strong>Angepasste Events</strong> aus.</li><li>Wählen Sie ein Bild aus.</li></ul></td></tr>
<tr><td>Abwählen</td><td>Die Auswahl eines Kontrollkästchens aufheben.</td><td>Deaktivieren Sie das Kontrollkästchen <strong>Passwort anzeigen</strong>.</td></tr>
<tr><td>Auswählen</td><td>Ein Element in der UI auswählen.</td><td>Fügen Sie ein angepasstes Attribut hinzu und wählen Sie <strong>Speichern</strong>.</td></tr>
<tr><td>Aktivieren</td><td>Eine Umschaltoption aktivieren</td><td>Aktivieren Sie den <strong>List-Unsubscribe-Header</strong>.</td></tr>
<tr><td>Deaktivieren</td><td>Eine Umschaltoption deaktivieren</td><td>Deaktivieren Sie <strong>Inline-CSS bei neuen E-Mails standardmäßig</strong>.</td></tr>
<tr><td>Eingeben</td><td>Einen Wert eingeben.</td><td><ul><li>Geben Sie im Textfeld den Namen Ihres angepassten Attributs ein.</li><li>Geben Sie „Braze" als Quellnamen ein.</li></ul></td></tr>
</tbody>
</table>
{:/}

#### Beschreibung von Einschränkungen {#describing-limitations}

Schreiben Sie offen über die Einschränkungen des Produkts, ohne Verzerrung oder Manipulation. Lesende reagieren intensiv darauf, manipuliert oder getäuscht zu werden, und dies gefährdet die Wirksamkeit der Dokumentation als Quelle nützlicher Wahrheit. Kunden verlassen sich auf die Dokumentation, um die Grenzen des Systems zu verstehen, auf dem sie aufbauen, damit sie Braze erfolgreich nutzen können.

Gleichzeitig unterstützen Sie die Intentionalität der Produktentwicklung, indem Sie Einschränkungen mit angemessenem, positivem Kontext rahmen.

* Wenn es eine weiche Einschränkung gibt (zum Beispiel ein API-Rate-Limit), rahmen Sie die Einschränkung, indem Sie über das **Standardlimit** oder die **Anfangszuteilung** sprechen.
* Bieten Sie einen sinnvollen Weg nach vorn, um weiche Limits zu navigieren. Geben Sie gegebenenfalls Beispiele für diese Workarounds.
 * Zum Beispiel verwendet Braze während des Onboardings Dimensionierungsübungen, um Kunden zu helfen zu verstehen, wie Dinge wie Datenpunkte von anderen Unternehmen ähnlicher Größe genutzt werden. Bei der Diskussion von Datenpunkten ist es angemessen, gleichzeitig über die Dimensionierungsübung zu sprechen.
* Es ist besser, einen Weg nach vorn positiv zu beschreiben als als Schadensbegrenzung.
 * Zum Beispiel: Anstatt zu sagen „Braze erlaubt es Kunden nicht, dies selbst zu tun. Das Support-Team muss diese Funktion für Sie aktivieren", sagen Sie „Um diese Funktion zu aktivieren, kontaktieren Sie das Support-Team."
* Verlassen Sie sich nicht zu sehr auf dieselben Standardphrasen, um weiche Limits zu navigieren. Wenn Nutzende immer wieder „Sprechen Sie mit Ihrer Vertretung" lesen, wird der Rat bedeutungslos.
* Wenn es eine harte Einschränkung gibt, versuchen Sie, die Begründung hinter diesem Limit zu beschreiben.
 * Zum Beispiel: „Es gibt ein Limit von 200 aktiven, aktionsbasierten In-App-Nachrichten-Kampagnen pro App-Gruppe, um die Geschwindigkeit der Nachrichtenzustellung zu optimieren und Timeouts zu verhindern. …Der durchschnittliche Braze-Kunde hat insgesamt 26 aktive Kampagnen gleichzeitig – es ist also unwahrscheinlich, dass diese Einschränkung Sie betrifft."
* Beschreiben Sie keine [geplante Funktionalität oder zukünftige Features](#future-features) als Möglichkeit, aktuelle Einschränkungen zu erklären.
* Wenn Sie sich auf Limits bei angepassten Daten beziehen, verwenden Sie den Begriff „Kapazität" anstelle von Limits.
 * Zum Beispiel: Standardmäßig können Sie 20 segmentierbare Event-Eigenschaften pro Workspace haben. Kontaktieren Sie Ihren Braze Account Manager, um Ihre Kapazität zu erhöhen.

#### Zukünftige Features {#future-features}

Vermeiden Sie Verweise auf zukünftige Features oder Andeutungen, dass etwas in Zukunft unterstützt werden könnte.

Verwenden Sie keine Wörter und Phrasen, die Ihren Text an einen bestimmten Zeitpunkt binden, da sie Inhalte schnell veralten lassen. Konzentrieren Sie sich darauf, wie das Produkt jetzt funktioniert, nicht darauf, was sich geändert hat (außer bei zeitbezogenen Inhalten wie Release Notes).

Vermeiden Sie insbesondere die folgende Liste von Wörtern und Phrasen, entnommen aus dem [Developer Documentation Style Guide](https://developers.google.com/style/timeless-documentation) von Google:

* zum Zeitpunkt des Schreibens
* derzeit
* noch nicht
* irgendwann
* Zukunft, in der Zukunft
* neueste
* neu, neuer
* jetzt
* alt, älter
* gegenwärtig, zum gegenwärtigen Zeitpunkt
* bald

#### Feature-Abkündigungen {#features-deprecations}

Bevor Sie Informationen über Feature-Abkündigungen aufnehmen, stellen Sie sicher, dass Sie einen allgemeinen Zeitrahmen haben, wann die Lesenden mit der Abkündigung des Features rechnen können (zum Beispiel Ende 2025).

Nachdem Sie einen allgemeinen Zeitrahmen haben, kommunizieren Sie die Feature-Abkündigung frühzeitig. Schreiben Sie klar über Abkündigungen, damit die Lesenden deutlich verstehen können, was sie erwartet.

Verwenden Sie keine Formulierungen, die bei den Lesenden Angst, Unsicherheit oder Zweifel hervorrufen könnten. Bieten Sie einen klaren Weg nach vorn, wie zum Beispiel wodurch das abgekündigte Feature ersetzt wird oder eine alternative Lösung.

#### Allgemein versus spezifisch {#general-vs-specific}

Als Best Practice schreiben Sie Artikel, die Funktionalität auf allgemein anwendbare Weise besprechen. Wenn mehr Details für spezifische Fälle oder Ausnahmen benötigt werden, erstellen Sie einen separaten Abschnitt (oder einen separaten Artikel, wenn der Inhalt die Länge eines Webartikels hat, ~500 Wörter), der diesen Sonderfall beschreibt. Erstellen Sie Querverweise vom allgemeinen Artikel zum spezifischen, um den Nutzenden zu helfen, diese Konzepte zu verbinden.

Vermeiden Sie die Erstellung von dupliziertem oder sich wiederholendem Inhalt für verschiedene Kanäle oder Features. Wenn Wiederholung nötig ist, verwenden Sie `includes`-Dateien und andere [Best Practices für wiederverwendbare Inhalte]({{site.baseurl}}/contributing/content_management/reusing_content).

**Als Beispiel:** Ein häufiger Anwendungsfall für Braze-Kunden ist das Retargeting von Nutzenden, die zuvor mit ihren Nachrichten interagiert haben. Das Retargeting von Nutzenden kann über viele Engagement-Tools erfolgen, einschließlich Kampagnen, Canvases, Landing-Pages und Segments. Das Retargeting von Nutzenden kann über viele Kanäle erfolgen: WhatsApp, SMS, Content Cards, E-Mail, Push-Benachrichtigungen und mehr. Oft versuchen Kunden, Nutzende über einen anderen Kanal als den zuvor verwendeten erneut anzusprechen.
Anstatt einen Artikel für jedes Engagement-Tool und jeden Kanal zu erstellen, erstellen Sie einen einzelnen Artikel, der Strategien für das Retargeting von Nutzenden bespricht und alle verfügbaren Optionen beschreibt. Wenn es besondere Überlegungen für bestimmte Kanäle/Tools gibt, erstellen Sie einen separaten Artikel, der diese Überlegungen beschreibt, und ordnen Sie ihn in diesem Dokumentationsabschnitt ein. Erstellen Sie Querverweise zwischen dem allgemeinen und dem spezifischen Artikel.

#### Metadaten und YAML {#metadata-and-yaml}

Artikel in der Braze-Dokumentation erfordern bestimmte Metadaten für Such- und Indexzwecke. Informationen zu den erforderlichen Metadaten finden Sie auf der GitHub-Seite zu [YAML und Metadaten-Layouts](https://github.com/braze-inc/braze-docs/wiki/YAML-%26-Metadata-Layouts).

#### Namenskonventionen {#naming-conventions}

Wenn Sie Artikel und Dateinamen benennen, stellen Sie sicher, dass Sie das allgemeine Thema im Titel beschreiben. Fügen Sie immer ein Schlüsselwort und eine kurze Beschreibung hinzu, die die Lesenden leicht verstehen, insbesondere bei Artikeltiteln.

Für Dateinamen halten Sie den Namen kurz und vermeiden Sie die Verwendung von Artikeln (ein, eine, der/die/das). Trennen Sie jedes Wort mit einem Unterstrich (_).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Targeting users</td></tr>
<tr><td style="width: 100%;">Creating an email campaign</td></tr>
<tr><td style="width: 100%;">API errors and responses</td></tr>
<tr><td style="width: 100%;">sms_historical_performance.png</td></tr>
<tr><td style="width: 100%;">push_notification_test.png</td></tr>
</tbody>
</table>
{:/}

Im Allgemeinen verwenden Sie für Artikel und Bilddateien dieselbe Schreibweise und Groß-/Kleinschreibung wie der referenzierte Artikel und die Dateien. Richtlinien zur Gestaltung von Artikeltiteln finden Sie unter [Überschriften und Titel](#headings-and-titles).

Wenn Sie sich auf eine bestimmte Datei beziehen, verwenden Sie dieselbe Schreibweise des Dateinamens und Code-Schriftart. Formatierungsdetails finden Sie auf der GitHub-Seite zu [Spezialformatierung](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting).

#### Verfahren und Anweisungen {#procedures-and-instructions}

Dieser Abschnitt behandelt einige Richtlinien, die beim Schreiben von Anweisungen für Verfahren im Braze-Dashboard zu beachten sind.

Allgemeine Richtlinien:

* **Verwenden Sie den richtigen Ton.** Halten Sie Ihre Anweisungen kurz, prägnant und aufgabenorientiert. Ihr Text muss nicht knapp oder trocken sein, aber er sollte direkt sein. Wenn Sie Aufgaben oder Teilaufgaben einführen, können Sie einen informelleren Ton verwenden, um Abwechslung zu schaffen. Vermeiden Sie die Verwendung von „bitte", um den Ton informell zu halten. Verwenden Sie einen zugänglichen Ton, um Ihre Texte nahbar zu gestalten.
* **Folgen Sie einem parallelen Überschriftenformat.** Wählen Sie ein Format für Ihre Überschriften und bleiben Sie dabei. Halten Sie Ihre Inhalte scannbar und vorhersehbar. Für aufgabenbasierte Überschriften und Seitentitel bevorzugen Sie Imperativverben (zum Beispiel „E-Mail-Kampagne erstellen").

Vor Anweisungen:

* **Verwenden Sie Einleitungen und Voraussetzungen.** Springen Sie nicht direkt in die Schritte. Geben Sie stattdessen Kontext darüber, was Ihr Artikel oder Abschnitt behandelt, und stellen Sie alle Informationen bereit, die die Lesenden kennen müssen, bevor sie die Anweisungen durchgehen. Stellen Sie sicher, dass alle Voraussetzungen am Anfang des Artikels mit der Überschrift „Voraussetzungen" aufgeführt sind. Tabellenüberschriften in diesem Abschnitt sollten „Anforderungen" lauten. „Anforderungen" ist ein akzeptabler Begriff für die Angabe einer Anforderung von Braze, einem Drittanbieter oder Partner.
* **Beginnen Sie am Anfang des Verfahrens.** Gehen Sie nicht davon aus, dass die Lesenden diese Seite nach Abschluss eines vorherigen Schritts erreicht haben. Wenn die Anweisungen für eine Aufgabe dort fortfahren, wo eine andere aufgehört hat, geben Sie einen Überblick darüber, wo sich die Lesenden im Verfahren befinden und was sie vor diesem Schritt abschließen müssen. Fügen Sie Links zu vorherigen Schritten hinzu.

Anweisungen schreiben:

* **Verwenden Sie handlungsorientierte Sprache.** Strukturieren Sie die Dokumentation um das, was die Nutzenden tun können, nicht um das, was das Produkt kann. Vermeiden Sie Formulierungen wie „Diese Funktion [macht xyz]". Denken Sie stattdessen in Begriffen wie „Verwenden Sie diese Funktion, um [xyz zu tun]".
* **Geben Sie bei Bedarf Standortschritte an.** Stellen Sie sicher, dass die Lesenden an der richtigen Stelle schauen, mit kurzen Phrasen wie „Wählen Sie auf der Seite **Einstellungen** die Option **Bearbeiten**." Wenn das nicht klar genug sein könnte, geben Sie einen einleitenden Schritt an. Zum Beispiel: „Gehen Sie zu **Einstellungen verwalten** und wählen Sie den Tab **Einstellungen**."
* **Stellen Sie bedingte Aussagen voran.** Setzen Sie [Bedingungssätze](#clause-order) an den Anfang. Für bedingte Anweisungen leiten Sie den Schritt mit „wenn" ein, damit die Lesenden wissen, dass sie den Schritt überspringen können, wenn die Bedingung nicht auf sie zutrifft. Zum Beispiel: „Wenn Sie X benötigen, dann führen Sie A > B > C aus."
* **Verstärken Sie die Aufgabenreihenfolge.** Für den Fortschritt innerhalb einer Reihe von Schritten verwenden Sie die Phrase „Wenn Sie" oder „Nachdem Sie". Für den Fortschritt zwischen Aufgaben beginnen Sie einen Abschnitt mit „Nachdem Sie" oder „Nun, da Sie". Vermeiden Sie die Phrase „Sobald Sie", da diese spezifische Verwendung von „sobald" sich nicht gut übersetzen lässt.

#### Tabs {#tabs}

Tabs können in der technischen Dokumentation als Möglichkeit verwendet werden, gruppierte Informationen zu organisieren.

Ein Tab bezieht sich auf ein Element, das beim Schreiben von Anweisungen verwendet werden kann, um eine Workflow-Zusammenfassung zu demonstrieren oder gruppierte Informationen zu organisieren. Dies ähnelt einer Tabelle oder Liste, aber die Informationen sind in Panels gruppiert.

Erwägen Sie die Verwendung von Tabs, wenn Informationen zusammengefasst werden können, um Duplikation zu vermeiden oder einen Workflow für die Lesenden zu visualisieren. Stellen Sie sicher, dass die Tabs parallele Informationen enthalten und nicht für Fälle verwendet werden, in denen die Lesenden sequenzielle Schritte in einem Workflow befolgen müssen.

Zum Beispiel können Sie Tabs verwenden, um Codebeispiele in verschiedenen Programmiersprachen anzuzeigen. In diesem Fall würden die Lesenden zwischen den Beispielen basierend auf den Tab-Labels wechseln, anstatt durch den Artikel zu scrollen.

Formatierungsdetails finden Sie auf der GitHub-Seite zu [Spezialformatierung](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting). Alternativ können Sie auch eine [Liste](#lists) oder [Tabelle](#tables-1) verwenden, um Informationen zu organisieren.

### Formatierung und Organisation {#formatting-and-organizing}

#### Adressen {#addresses}

Verwenden Sie die Zahl gefolgt vom Straßennamen wie folgt:

*330 W. 34th St.*

Um eine vollständige Adresse anzuzeigen, verwenden Sie die Zahl, gefolgt vom Straßennamen, gefolgt von Stadt, Bundesstaat und Postleitzahl. Zwischen Bundesstaat und Postleitzahl ist kein Komma erforderlich.

*330 W. 34th St., New York, NY 10001*

#### Button-Labels {#buttons-labels}

Button-Labels sollten klar und vorhersehbar sein – die Nutzenden sollten wissen, welche Aktion beim Auswählen des Buttons ausgeführt wird. Verwenden Sie Satzschreibung für Button-Labels und beginnen Sie mit einem starken Verb. Wenn unklar sein könnte, worauf sich das Verb bezieht, verwenden Sie das Format [Verb] + [Substantiv].

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Registrieren</td><td style="width: 50%;">REGISTRIEREN</td></tr>
<tr><td style="width: 50%;">Anmelden</td><td style="width: 50%;">ANMELDEN</td></tr>
<tr><td style="width: 50%;">Abonnieren</td><td style="width: 50%;">ABONNIEREN</td></tr>
<tr><td style="width: 50%;">Mehr erfahren</td><td style="width: 50%;">Mehr</td></tr>
</tbody>
</table>
{:/}

Lassen Sie unnötige Wörter und Artikel wie „ein", „eine" oder „der/die/das" weg.

#### Hinweise und Alerts {#callouts-and-alerts}

Alerts, auch als Hinweise bekannt, werden verwendet, um auf Informationen aufmerksam zu machen, die für die Lesenden hilfreich sind. Es gibt vier Alert-Typen, die in unserer Dokumentation verwendet werden:

* Wichtig
* Hinweis
* Tipp
* Warnung

Verwenden Sie Alerts sparsam in Artikeln. Weitere Informationen finden Sie unter [Best Practices für Alerts]({{site.baseurl}}/contributing/style_guide/alerts/).

#### Code im Text {#code-in-text}

Es gibt einige Szenarien, in denen Sie Code-Schriftart verwenden sollten, um Text innerhalb eines Satzes zu formatieren. Hier ist eine unvollständige Liste von Elementen, die in Code-Schriftart stehen sollten:

* Attributnamen und -werte
* API-Anfrageparameter
* Dateinamen
* Dateipfade
* Methoden-, Variablen- oder Parameternamen
* HTML- und XML-Elementnamen
* HTTP-Statuscodes
* Texteingabe in ein Terminal

Um Inline-Codetext in der Braze-Dokumentation zu erstellen, umgeben Sie den Text mit Backticks (`).

#### Codebeispiele {#code-samples}

Codebeispiele beziehen sich auf Blöcke von Codetext, die ein Beispiel-Code-Snippet anzeigen. Führen Sie das Codebeispiel aus Gründen der Barrierefreiheit nach Möglichkeit mit einem erklärenden Satz ein.

Um sicherzustellen, dass Ihre Codebeispiele lesbar sind, rücken Sie jede Zeile um zwei Leerzeichen pro Einrückungsebene ein. Wenn Sie Schwierigkeiten bei der Formatierung Ihrer Codebeispiele haben, versuchen Sie, Ihren Code mit einem Pretty-Print-Formatierer zu verschönern, wie zum Beispiel [JSON Formatter](https://jsonformatter.org/json-pretty-print).

Um Codeblöcke in der Braze-Dokumentation zu erstellen, lesen Sie den [Code Snippet Test](https://github.com/braze-inc/braze-docs/blob/develop/_docs/_home/styling_test_page.md#code-snippet-test). Denken Sie daran, dass Codeblöcke den Sprachtyp angeben sollten, um eine korrekte Syntaxhervorhebung sicherzustellen.

#### Daten und Uhrzeiten {#dates-and-times}

Schreiben Sie den Monat und die Wochentage aus. Vermeiden Sie Abkürzungen, wenn möglich. Für Fälle, in denen die Abkürzung von Monaten erforderlich ist, kürzen Sie nur die folgenden ab:

* Jan.
* Feb.
* Aug.
* Sept.
* Okt.
* Nov.
* Dez.

Verwenden Sie ein [Komma](#commas), um das Datum vom Jahr zu trennen. Wenn ein Wochentag mit dem Datum verwendet wird, fügen Sie ihn vor dem Monat hinzu.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig: <em>Das bevorzugte Datumsformat verwenden.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">September 2021</td></tr>
<tr><td style="width: 100%;">15. September 2021</td></tr>
<tr><td style="width: 100%;">Mittwoch, 15. September 2021</td></tr>
</tbody>
</table>
{:/}

Für Datumsbereiche verwenden Sie einen [Halbgeviertstrich](#en-dash).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">2010–2021</td></tr>
</tbody>
</table>
{:/}

Verwenden Sie einen Halbgeviertstrich für Datumsbereiche.

Verwenden Sie Ziffern mit am oder pm, gefolgt von einem Leerzeichen, gefolgt von der Tageszeit (am oder pm). Entfernen Sie die Minuten bei vollen Stunden.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Ziffern mit am oder pm verwenden.</em></th><th style="width: 50%;">Falsch: <em>Minuten bei vollen Stunden verwenden (es sei denn, es handelt sich um einen Bereich).</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">12 pm</td><td style="width: 50%;">12:00 P.M.</td></tr>
</tbody>
</table>
{:/}

Für Zeitbereiche verwenden Sie einen Halbgeviertstrich zur Trennung. Fügen Sie keine Leerzeichen vor oder nach dem Halbgeviertstrich hinzu.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig: <em>Halbgeviertstrich für Zeitbereiche verwenden.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">12:45–14:30</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig: <em>Minuten für Zeitbereiche verwenden.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">8:00–14:30</td></tr>
</tbody>
</table>
{:/}

Für Referenzen in Fällen, in denen Parteien aus anderen Zeitzonen einbezogen sind (wie Webinare, Meetings oder Events), geben Sie die Zeitzone wie folgt an:

* Eastern Standard Time: EST
* Central Standard Time: CST
* Mountain Standard Time: MST
* Pacific Standard Time: PST
* Greenwich Mean Time: GMT
* Coordinated Universal Time: UTC
* Central European Time: CET
* Eastern Europe Time: EET
* Western Europe Time: WET
* Singapore Time: SGT
* China Standard Time: CST

#### Emojis {#emojis}

Obwohl wir ein lockerer Haufen sind, vermeiden Sie die Verwendung von Emojis in Lerninhalten, da sie auf verschiedene Weisen interpretiert werden können und oft unprofessionell wirken.

Ausnahmen umfassen die folgenden Szenarien:

* Bei Verwendung von ✅ und ❌ in Tabellen, um Inhalte zu kennzeichnen, die unterstützt versus nicht unterstützt oder empfohlen versus nicht empfohlen sind
* Bei Verwendung in Beispieltexten für eine Kampagne oder Canvas-Nachricht

#### Beispielnamen {#example-names}

Verwenden Sie niemals echte Namen, E-Mail-Adressen oder andere personenbezogene Daten (PII). Verwenden Sie stattdessen fiktive Beispiele oder [Platzhaltertext](#placeholder-text).

Wenn Sie Namen in Ihren Texten verwenden müssen, beziehen Sie sich auf die Wikipedia-Liste der [geschlechtsneutralen Vornamen](https://en.wikipedia.org/wiki/Unisex_name). Verwenden Sie nach Möglichkeit die Pronomen „sie" und „ihr" und vermeiden Sie Beispiele, die auf ein bestimmtes Geschlecht beschränkt sind.

##### Beispiel-E-Mail-Adressen

Verwenden Sie das Format „name@example.com" für generische E-Mail-Adressen. Ersetzen Sie „name" durch einen Beispielnamen. Zum Beispiel:

* alex@example.com
* lee@example.com
* yuri@example.com

#### Abbildungen und andere Bilder {#figures-and-other-images}

Beim Erstellen von Abbildungen und Bildern beziehen Sie sich auf den [Bild-Style-Guide]({{site.baseurl}}/contributing/style_guide/image_style_guide/). Fügen Sie niemals personenbezogene Daten (PII) in Abbildungen oder Bilder ein.

##### Alternativtext {#alt-text}

Fügen Sie immer Alternativtext zu Bildern hinzu. Screenreader lesen den Alternativtext vor, um Bilder für Personen mit Sehverlust zu erklären. Daher muss Ihr Alternativtext alle wichtigen Informationen vermitteln, die im Bild dargestellt werden.
Verwenden Sie die folgenden Richtlinien beim Schreiben von Alternativtext:

* Verwenden Sie [einfache Sprache](https://www.plainlanguage.gov/guidelines/).
* Schreiben Sie in vollständigen Sätzen und verwenden Sie Satzschreibung.
* Lassen Sie unnötige Wörter weg.
* Fügen Sie nicht „Bild von" oder „Abbildung von" hinzu. Es wird bereits verstanden, dass Sie sich auf ein Bild beziehen.
* Fügen Sie keine Sonderzeichen ein. Verwenden Sie zum Beispiel anstelle von kaufmännischen Und-Zeichen (&) das ausgeschriebene Wort „und".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Seite für angepasste Events im Braze-Dashboard mit hervorgehobenem „Bericht hinzufügen".</td><td style="width: 50%;">Ein Screenshot der Seite Einstellungen verwalten > Angepasste Events im Braze-Dashboard mit der hervorgehobenen Option zum Hinzufügen eines Berichts.</td></tr>
</tbody>
</table>
{:/}

Lassen Sie Alt-Tags explizit leer (alt=""), wenn das Bild eine redundante visuelle Komponente zu dem hinzufügt, was im Text erklärt wird.

Das Hinzufügen von Alternativtext zu jedem Bild macht Webseiteninhalte nicht automatisch leicht navigierbar und konsumierbar. Redundante visuelle Elemente sind für sehende Nutzende wirkungsvoll, da visuelle Informationen leicht zu verstehen und zu merken sind. Alternativtext, der redundante Bilder beschreibt, kann jedoch für Nutzende, die das Bild nicht sehen können, unnötig sein, da jedes Seitenelement von Screenreader-Nutzenden gleiche Aufmerksamkeit erfordert, um festzustellen, ob es für ihre Aufgabe nützlich ist.

##### Beispiel-Firmennamen

Wenn möglich, machen Sie Screenshots von [dashboard-06](https://dashboard-06.braze.com/), damit Sie einen der FakeBrandz-Firmennamen verwenden.

#### Dateitypen und Dateinamen {#file-types-and-filenames}

Wenn Sie sich auf einen Dateityp beziehen, verwenden Sie den Standardnamen des Typs. Wenn der Dateityp ein Akronym ist, schreiben Sie den Dateityp in Großbuchstaben.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Den Standardnamen des Dateityps verwenden</em></th><th style="width: 50%;">Falsch: <em>Die Dateierweiterung verwenden</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CSV</td><td style="width: 50%;">.csv</td></tr>
<tr><td style="width: 50%;">ausführbare Datei</td><td style="width: 50%;">.exe</td></tr>
<tr><td style="width: 50%;">GIF</td><td style="width: 50%;">.gif</td></tr>
<tr><td style="width: 50%;">JAR</td><td style="width: 50%;">.jar</td></tr>
<tr><td style="width: 50%;">JPEG</td><td style="width: 50%;">.jpg, .jpeg</td></tr>
<tr><td style="width: 50%;">JSON</td><td style="width: 50%;">.json</td></tr>
<tr><td style="width: 50%;">PDF</td><td style="width: 50%;">.pdf</td></tr>
<tr><td style="width: 50%;">PNG</td><td style="width: 50%;">.png</td></tr>
<tr><td style="width: 50%;">Python-Datei</td><td style="width: 50%;">.py</td></tr>
<tr><td style="width: 50%;">Bash-Datei</td><td style="width: 50%;">.sh</td></tr>
<tr><td style="width: 50%;">Textdatei</td><td style="width: 50%;">.txt</td></tr>
<tr><td style="width: 50%;">YAML</td><td style="width: 50%;">.yaml</td></tr>
<tr><td style="width: 50%;">ZIP</td><td style="width: 50%;">.zip</td></tr>
</tbody>
</table>
{:/}

Wenn Sie sich auf den Namen einer Datei beziehen, formatieren Sie den Dateinamen als Codetext. Weitere Informationen finden Sie im Abschnitt [Code im Text](#code-in-text).

Wenn Sie Dateien in der Braze-Dokumentation benennen, wie Artikel- oder Bilddateien, verwenden Sie Kleinbuchstaben und trennen Sie Wörter mit Unterstrichen, nicht mit Bindestrichen. Weitere Informationen finden Sie unter [Dateien und Ordner erstellen](https://github.com/braze-inc/braze-docs/wiki/Creating-Files-&-Folders) auf GitHub.

#### Fußnoten {#footnotes}

Fußnoten sind Anmerkungen, die zusätzliche Informationen liefern und normalerweise am Ende einer Seite platziert werden. Aufgrund der Formatierung unseres Textes sind Fußnoten für die meisten Anwendungsfälle nicht optimal. Im Folgenden wird beschrieben, wann Fußnoten im Vergleich zu anderen Zuordnungsmethoden verwendet werden sollten:

* Wenn Sie eine Liste von Statistiken oder anderen dichten Informationen präsentieren, die alle Quellen zugeordnet werden müssen, verwenden Sie Fußnoten.
* Wenn Sie ein oder zwei Informationen präsentieren, verwenden Sie einen Link oder einen Alert.
* Wenn Sie zusätzliche Informationen zu Elementen in einer Tabelle bereitstellen müssen, verwenden Sie ein Sternchen (*) neben dem Tabellenelement und präsentieren Sie die Informationen nach der Tabelle.

#### Textformatierung in Anweisungen {#formatting-text-in-instructions}

Verwenden Sie eine konsistente Textformatierung, um den Lesenden zu helfen, Informationen zu finden und zu interpretieren. Dieser Abschnitt enthält Richtlinien dazu, welche Formatierung bei der Beschreibung oder Bezugnahme auf verschiedene Textelemente in Ihren Anweisungen zu verwenden ist.

Dieser Abschnitt behandelt die folgenden Elemente:

* [Buttons](#buttons)
* [Kontrollkästchen](#checkboxes)
* [Befehlszeilenbefehle und -optionen](#command-line-commands-and-options)
* [Dialogfelder](#dialog-boxes-(modals))
* [Fehlermeldungen](#error-messages)
* [Filter- und Operatornamen](#filter-and-operator-names)
* [Ordner- und Dateinamen](#folder-and-filenames)
* [Tastennamen und -kombinationen](#key-names-and-combinations)
* [Metriken](#metrics)
* [Seiten](#pages)
* [Berechtigungsnamen](#permission-names)
* [Tabs](#tabs-1)
* [Texteingabe](#text-input)

##### Buttons {#buttons}

Wenn Sie sich auf einen Button beziehen, verwenden Sie fetten Text für das Button-Label. In den meisten Fällen passen Sie die Groß-/Kleinschreibung der UI an. Für Buttons, bei denen das Label komplett in Großbuchstaben steht (außer OK-Buttons), verwenden Sie stattdessen Satzschreibung.

Um sich auf einen Button zu beziehen, verwenden Sie nur das Label des Buttons. Bezeichnen Sie einen Button nicht als „den [Label]-Button".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Wählen Sie <strong>Sprachen hinzufügen</strong>.</td><td style="width: 50%;">Wählen Sie den Button <strong>Sprachen hinzufügen</strong>. <br><br> Wählen Sie „Sprachen hinzufügen".</td></tr>
</tbody>
</table>
{:/}

Wenn das Label mit einem Doppelpunkt oder Auslassungspunkten endet, lassen Sie die abschließende Interpunktion weg.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Wählen Sie <strong>Speichern unter</strong></td><td style="width: 50%;">Wählen Sie <strong>Speichern unter…</strong></td></tr>
</tbody>
</table>
{:/}

Wenn ein Button ein Symbol ist, geben Sie den Namen des Buttons an, wie er im Tooltip angezeigt wird. Wenn ein Button mit einem Symbol keinen Tooltip enthält, reichen Sie eine Anfrage ein, dass ein Tooltip hinzugefügt wird.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Wählen Sie ➕ <strong>Hinzufügen</strong>.</td><td style="width: 50%;">Wählen Sie das ➕-Symbol.</td></tr>
</tbody>
</table>
{:/}

##### Kontrollkästchen {#checkboxes}

Wenn Sie sich auf ein Kontrollkästchen beziehen, verwenden Sie fetten Text für das Kontrollkästchen-Label. Fügen Sie das Wort „Kontrollkästchen" nicht hinzu, es sei denn, Klarheit ist erforderlich. Bevorzugen Sie die Begriffe „auswählen/abwählen" gegenüber „ankreuzen/abkreuzen".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Wählen Sie <strong>Kampagne an Nutzer in ihrer lokalen Zeitzone senden</strong>.</td><td style="width: 50%;">Kreuzen Sie <strong>Kampagne an Nutzer in ihrer lokalen Zeitzone senden</strong> an.</td></tr>
<tr><td style="width: 50%;">Deaktivieren Sie das Kontrollkästchen <strong>Beenden</strong>.</td><td style="width: 50%;">Entfernen Sie das Häkchen beim Kontrollkästchen <strong>Beenden</strong>.</td></tr>
</tbody>
</table>
{:/}

##### Befehlszeilenbefehle und -optionen {#command-line-commands-and-options}

Wenn Sie sich auf Befehlszeilenbefehle oder -optionen beziehen, verwenden Sie Code-Formatierung. Passen Sie die Groß-/Kleinschreibung an die Darstellung oder die erforderliche Eingabe an.

##### Dialogfelder (Modals) {#dialog-boxes-(modals)}

Vermeiden Sie es, Dialogfelder beim Namen zu nennen, es sei denn, Klarheit ist erforderlich. Beschreiben Sie stattdessen, was die Lesenden tun müssen. Wenn Sie sich auf ein Dialogfeld beziehen, verwenden Sie fetten Text für den Namen des Dialogfelds und passen Sie die Groß-/Kleinschreibung der UI an.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Wählen Sie <strong>Hochladen</strong> und wählen Sie dann eine Datei zum Hochladen aus.</td><td style="width: 50%;">Wählen Sie <strong>Hochladen</strong> und verwenden Sie das Dialogfeld <strong>Datei hochladen</strong>, um eine Datei zum Hochladen auszuwählen.</td></tr>
</tbody>
</table>
{:/}

##### Fehlermeldungen {#error-messages}

Wenn Sie sich auf Fehlermeldungen beziehen, die Lesende möglicherweise sehen, setzen Sie die Fehlermeldung in Anführungszeichen. Für längere Fehlermeldungen verwenden Sie ein Blockzitat.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">„Push Bounced: MismatchSenderId"</td><td style="width: 50%;"><em>Push Bounced: MismatchSenderID</em><br><br><code>Push Bounced: MismatchSenderID</code></td></tr>
</tbody>
</table>
{:/}

##### Filter- und Operatornamen {#filter-and-operator-names}

Wenn Sie sich auf die Namen von Filtern und Operatoren für Segments oder andere Bereiche des Dashboards beziehen, verwenden Sie Codetext. Passen Sie die Groß-/Kleinschreibung der UI an, einschließlich Elemente, die komplett in Großbuchstaben stehen, wie `OR`- und `AND`-Operatoren.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Wählen Sie den Filter <code>First Used App</code> und…</td><td style="width: 50%;">Wählen Sie den Filter <strong>First Used App</strong> und…</td></tr>
<tr><td style="width: 50%;">Kombinieren Sie Filter mit dem Operator <code>OR</code>.</td><td style="width: 50%;">Kombinieren Sie Filter mit dem Operator „OR".</td></tr>
</tbody>
</table>
{:/}

##### Ordner- und Dateinamen {#folder-and-filenames}

Wenn Sie sich auf Ordnernamen und Dateinamen beziehen, verwenden Sie Codetext.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Öffnen Sie die Datei <code>braze.xml</code>.</td><td style="width: 50%;">Öffnen Sie die Datei <strong>braze.xml</strong>.</td></tr>
</tbody>
</table>
{:/}

##### Tastennamen und -kombinationen {#key-names-and-combinations}

Wenn Sie sich auf Tastennamen oder Tastenkombinationen beziehen, verwenden Sie den [HTML-`<kbd>`-Tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd). Dieser kennzeichnet textuelle Benutzereingaben von einer Tastatur, Spracheingabe oder einem anderen Texteingabegerät. Wenn Sie in einem Editor arbeiten, der kein benutzerdefiniertes HTML unterstützt, verwenden Sie stattdessen [Codetext](#code-in-text).

Schreiben Sie die Namen von Tasten wie Command, Control, Option und Shift aus. Verwenden Sie keine Symbole für diese Tasten.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Drücken Sie <strong>Option</strong>.</td><td style="width: 50%;">Drücken Sie ⌥.</td></tr>
</tbody>
</table>
{:/}

Für Tastenkombinationen verwenden Sie ein Pluszeichen (+) zwischen den Tasten, lassen Sie das Plus aber aus jeder speziellen Formatierung heraus.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Drücken Sie <strong>Option + F12</strong>.</td><td style="width: 50%;">Drücken Sie ⌥ + F12.</td></tr>
</tbody>
</table>
{:/}

So erscheinen Tastatur-Tags beispielsweise in der Braze-Dokumentation:
Um den Befehl zu stoppen, drücken Sie **Control + C**.

##### Metriken {#metrics}

Wenn Sie sich auf eine Metrik in einer Tabelle oder einem Glossareintrag beziehen, verwenden Sie Anfangsbuchstaben groß ohne spezielle Formatierung. Wenn Sie sich auf eine Metrik in einem Satz beziehen, verwenden Sie Anfangsbuchstaben groß mit Kursivschrift (wie *Machine Opens*).

##### Seiten

Verwenden Sie den Begriff Seite, wenn Sie sich auf eine Webseite im Allgemeinen oder eine bestimmte Seite im Braze-Dashboard beziehen. Wenn Sie sich auf einen Seitennamen beziehen, verwenden Sie das Format „die Seite [Label]" und formatieren Sie den Namen der Seite fett.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Gehen Sie zur Seite Segments.</td><td style="width: 50%;">Gehen Sie zur „Segments"-Seite.</td></tr>
</tbody>
</table>
{:/}

##### Berechtigungsnamen {#permission-names}

Wenn Sie sich auf Namen von Berechtigungen innerhalb des Dashboards beziehen, setzen Sie den Berechtigungsnamen in Anführungszeichen.

{% alert note %}

Derzeit verwenden wir Titelschreibung, um die Formatierung des Dashboards zu übernehmen. Es ist geplant, die Berechtigungsnamen innerhalb der UI auf Satzschreibung zu aktualisieren, um unseren Standards zu entsprechen.

{% endalert %}

##### Tabs {#tabs-1}

Wenn Sie sich auf einen Tab beziehen, verwenden Sie das Format „den Tab [Label]" und formatieren Sie den Namen des Tabs fett.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Gehen Sie zur Seite <strong>Einstellungen verwalten</strong> und wählen Sie den Tab <strong>Tags</strong>.</td><td style="width: 50%;">Gehen Sie zur Seite „Einstellungen verwalten" und wählen Sie den Tab „Tags".</td></tr>
</tbody>
</table>
{:/}

##### Texteingabe {#text-input}

Wenn Sie Lesende anweisen, eine bestimmte Zeichenkette einzugeben, setzen Sie den Text in Anführungszeichen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Geben Sie im Feld <strong>Name</strong> „Passive Nutzer:innen" ein</td><td style="width: 50%;">Geben Sie im Feld <strong>Name</strong> <code>Passive Nutzer:innen</code> ein.</td></tr>
</tbody>
</table>
{:/}

#### Häufig gestellte Fragen (FAQs) {#frequently-asked-questions-faqs}

Ordnen Sie die FAQs, indem Sie mit den Informationen beginnen, die die Lesenden am meisten wissen möchten oder müssen, und organisieren Sie die FAQs dann nach Themenkategorie, wenn es mehrere gibt.

Beantworten Sie bei jeder FAQ zunächst direkt die Frage und gehen Sie dann ins Detail. Verwenden Sie echte Fragen, die typischen Suchanfragen und dem Vokabular der Nutzenden entsprechen, was die Auffindbarkeit der FAQ verbessert. Fügen Sie Links zu Ressourcen hinzu, die die Nutzenden hilfreich finden könnten, wie verwandte Artikel, Anweisungen zur Kontaktaufnahme mit dem Support und Lehrmaterialien (Anleitungen, Tutorials und andere), wenn verfügbar.

#### Geografie {#geography}

##### Städte

Schreiben Sie alle Städtenamen bei der ersten Erwähnung im Text aus. Danach ist es in Ordnung, bekannte Städtenamen wie NYC oder LA abzukürzen.

**Erste Erwähnung:** San Francisco
**Zweite Erwähnung:** SF

Für bekannte Städte wie London oder Tokyo ist es in Ordnung, sie ohne Komma gefolgt vom Bundesstaat, der Provinz oder dem Land einzuführen.

Für Städte oder Orte, die Ihrem Publikum möglicherweise nicht vertraut sind, geben Sie den Bundesstaat, die Provinz oder das Land an.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Richtig</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Biloxi, Mississippi</td></tr>
<tr><td style="width: 100%;">New Bedford, MA</td></tr>
<tr><td style="width: 100%;">Antwerpen, Belgien</td></tr>
</tbody>
</table>
{:/}

##### Länder

Schreiben Sie die Namen aller Länder groß. Um einen Ländernamen abzukürzen, schreiben Sie die erste Erwähnung vollständig aus, gefolgt von den Initialen für weitere Erwähnungen.

**Erste Erwähnung:** Vereinigte Staaten
**Zweite Erwähnung:** US

Setzen Sie keine Punkte zwischen abgekürzte Ländernamen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">UK</td><td style="width: 50%;">U.K.</td></tr>
<tr><td style="width: 50%;">Washington, DC</td><td style="width: 50%;">Washington, D.C.</td></tr>
</tbody>
</table>
{:/}

##### Regionen

Schreiben Sie sowohl die Region als auch die modifizierende Himmelsrichtung groß.

**Beispiel:** Nordkalifornien, Osteuropa

Schreiben Sie Eigennamen, die eine bestimmte Region oder einen bestimmten Ort beschreiben, groß.

**Beispiel:** West Midlands, Südamerika, South Chicago

##### Bundesstaaten und Provinzen

Schreiben Sie alle Bundesstaaten und Provinzen groß.

**Beispiel:** New York, Quebec

#### Überschriften und Titel {#headings-and-titles}

Verwenden Sie für Artikelüberschriften und -titel Satzschreibung. Seien Sie beschreibend beim Schreiben von Überschriften und Titeln und konzentrieren Sie sich auf den Hauptzweck des Inhalts basierend auf dem Artikeltyp. Verwenden Sie keine kaufmännischen Und-Zeichen anstelle des Wortes „und".

Für Artikeltitel vermeiden Sie nach Möglichkeit Gerundien (Verben, die auf *-end* enden) zugunsten von Imperativverben. Halten Sie die Artikeltitel prägnant und stellen Sie sicher, dass sie für den Inhalt angemessen sind. Zum Beispiel könnte ein Referenzartikel über SMS-Nachrichten den Titel „Über SMS" tragen.

Für Artikelüberschriften seien Sie prägnant und konsistent über die Überschriftentitel hinweg. Wenn zum Beispiel der Heading-1-Stil des Artikels jeden Schritt definiert (z. B. **Schritt 1: Neue Push-Kampagne erstellen**), dann behalten Sie dieses Format über die Artikelüberschriften hinweg bei.

Hilfe zur Gestaltung in Braze Docs finden Sie auf der Contributing-Seite für [Gestaltungsbeispiele]({{site.baseurl}}/contributing/styling_examples/?tab=markdown).

##### Numerische Teilaufgaben

Für Überschriften, die geordnete Schritte beschreiben, verwenden Sie Ziffern in den Teilaufgaben-Überschriften.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Schritt 2: SMS-Kampagne erstellen <br><br> Schritt 2.1: Nachricht verfassen <br><br> Schritt 2.2: Zustellung planen</td><td style="width: 50%;">Schritt 2: SMS-Kampagne erstellen <br><br> Schritt 2a: Nachricht verfassen <br><br> Schritt 2b: Zustellung planen</td></tr>
</tbody>
</table>
{:/}

#### Einleitungen {#introductions}

Einleitungen dienen als schnelle Überprüfung für Nutzende, die sich fragen:

* Bin ich im richtigen Dokument? Ist das für mich relevant?
* Was lerne ich, wenn ich die Zeit investiere, dieses Dokument zu lesen?
* Habe ich das Gefühl, einer klaren Integrations- oder Einrichtungsreise für SMS, E-Mail, IAM oder andere zu folgen (obwohl nicht angegeben wird, welches Dokument als nächstes gelesen werden sollte)?

Die folgenden sind allgemeine Richtlinien für Einleitungen. Beziehen Sie sich auf abschnittsspezifische Richtlinien für speziellere Anwendungsfälle.

* Einleitungen können 1–5 Sätze lang sein
* Einleitungen sollten einen Überblick über den Inhalt des Dokuments geben oder eine Einführung in das Thema sein
* Verwenden Sie Blockzitate
* Platzieren Sie Einleitungen unter der H1-Überschrift des Artikels

##### Partner

Fügen Sie einen Überblick über den Partner und eine kurze Unternehmensbeschreibung hinzu. Fügen Sie auch einen Link zur Partner-Website hinzu.

##### API

Fügen Sie nur den Satz „Verwenden Sie diesen Endpunkt..." in die Einleitung ein. Wir möchten die API-Endpunkte so einfach wie möglich navigierbar halten. Weitere Informationen zur Struktur und Formatierung von API-Endpunkten finden Sie in den [Richtlinien zur API-Endpunkt-Dokumentation]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/).

##### Benutzerhandbuch und Entwicklerhandbuch

Einleitungsabsätze sollten auf eine von zwei Arten geschrieben werden:

1. Mit einem einleitenden Absatz oder einer Einführung in das Thema
2. Eine Aussage darüber, was der Artikel enthält. Dies sieht oft so aus: „Dieser Referenzartikel...".

Während die Schritte im Benutzerhandbuch und Entwicklerhandbuch die Nutzenden stark auf Hinweise aus der Navigation während ihrer Customer Journey angewiesen sind, ist es, obwohl manchmal redundant, hilfreich, den Wert des Dokuments gleich zu Beginn explizit zu nennen.

Wenn zum Beispiel ein Nutzer das Entwicklerhandbuch durchgeht und Unity integriert. Diese Seite mit dem Titel „Integration" wäre ohne den einleitenden Satz nicht ausreichend.

#### Listen {#lists}

Listen eignen sich am besten zur Formatierung verwandter Informationen. Verwenden Sie keine Liste, um nur ein Element anzuzeigen. Wenn Sie ein einzelnes Element vom umgebenden Text abheben möchten, verwenden Sie eine andere Formatierung.

Es gibt drei Arten von Listen: Aufzählungslisten, Buchstabenlisten und nummerierte Listen. Fügen Sie einen einleitenden vollständigen Satz hinzu, der mit einem Doppelpunkt oder Punkt enden kann.

* Aufzählungslisten organisieren Informationen, die nicht in einer bestimmten Reihenfolge stehen müssen.
* Buchstabenlisten werden verwendet, um sich gegenseitig ausschließende Optionen zu definieren.
* Nummerierte Listen zeigen eine Abfolge geordneter Schritte an.

Verwenden Sie nach Möglichkeit dieselbe Syntax für alle Listenelemente.

Für die Groß-/Kleinschreibung von Listenelementen beginnen Sie jedes Listenelement mit einem Großbuchstaben. Für die abschließende Interpunktion von Listenelementen verwenden Sie keine abschließende Interpunktion in den folgenden Szenarien:

* Wenn das Listenelement ein einzelnes Wort oder ein unvollständiger Satz ist
* Wenn das Listenelement kein Verb enthält
* Wenn das Listenelement in Code-Schriftart steht
* Wenn das Listenelement ein Link oder Dokumenttitel ist

#### Medienformatierung {#media-formatting}

Dieser Abschnitt enthält allgemeine Richtlinien zur Formatierung von Bildern und GIFs in Ihren Inhalten. Weitere Informationen, einschließlich Beispiel-Screenshots, finden Sie im [Bild-Style-Guide]({{site.baseurl}}/contributing/style_guide/image_style_guide/).

| **Richtig** | {::nomarkdown}<ul><li>Schneiden Sie eng auf das erwähnte Feature oder die Komponente zu.</li><li>Machen Sie hochwertige Screenshots, vorzugsweise auf einem Retina-Monitor (MacBook-Display).</li><li>Erstellen Sie ein GIF einer Interaktion oder eines Workflows.</li><li>Bedenken Sie, dass Nutzende ein GIF nicht anhalten oder durchscrollen können, um Details zu sehen.</li><li>Lassen Sie Bilder durch einen Optimierer laufen, um die Dateigröße zu reduzieren (ImageOptim, TinyPNG oder Ezgif).</li><li>Streben Sie hohen Kontrast zwischen Elementen für die Barrierefreiheit an.</li><li>Ändern Sie die Bildgröße nach Höhenprozentsätzen statt nach bestimmten Pixelwerten.</li></ul>{:/} |
| **Falsch** | {::nomarkdown}<ul><li>Fügen Sie nicht den Header oder die Seitenleiste des Dashboards ein, da diese in einem einfachen Satz erklärt werden können.</li><li>Fügen Sie nicht das gesamte Dashboard ein.</li><li>Fügen Sie keine personenbezogenen Daten ein (es sei denn, sie sind unkenntlich gemacht oder gehören einem Demo-Nutzer).</li><li>Fügen Sie nicht den Browser-Rahmen ein (URL-Feld, Lesezeichen, Tabs usw.).</li><li>Fügen Sie keine Dashboards von Technologie-Partnern ein.</li><li>Fügen Sie keinen Rahmen oder Schlagschatten zu Bildern hinzu.</li></ul>{:/} |

#### Zahlen {#numbers}

Beginnen Sie einen Satz niemals mit einer Ziffer. Die Ausnahme ist, wenn Sie sich auf ein Jahr beziehen (Beispiel: „2019 war ein besonderes Jahr").

Schreiben Sie Zahlen bis neun aus. Für Maßeinheiten oder Zahlen ab 10 verwenden Sie die Ziffer. Für Zahlen über drei Stellen verwenden Sie einen Punkt als Tausendertrennzeichen. Schreiben Sie größere Zahlen aus.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">1.000</td><td style="width: 50%;">1000</td></tr>
<tr><td style="width: 50%;">200.000</td><td style="width: 50%;">200000</td></tr>
<tr><td style="width: 50%;">1.000.000</td><td style="width: 50%;">1000000</td></tr>
<tr><td style="width: 50%;">9 Milliarden</td><td style="width: 50%;">9000000000</td></tr>
<tr><td style="width: 50%;">5 MB</td><td style="width: 50%;">fünf MB</td></tr>
</tbody>
</table>
{:/}

##### Währung

Geben Sie immer an, auf welche Währung Sie sich beziehen, indem Sie das Währungssymbol vor dem Betrag verwenden oder die Währung ausschreiben (Beispiel: Pesos, Euro, Pfund usw.).

Verwenden Sie die Dezimalstelle für Beträge, bei denen die Centanzahl größer als null ist. Für Beträge über drei Stellen verwenden Sie einen Punkt als Tausendertrennzeichen. Fügen Sie kein „,00" bei ganzen Geldbeträgen hinzu.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">US $20</td><td style="width: 50%;">$20</td></tr>
</tbody>
</table>
{:/}

##### Telefonnummern

Wenn eine Telefonnummer referenziert wird, setzen Sie Bindestriche zwischen die Ziffern. Setzen Sie die Vorwahl nicht in Klammern.

Wenn Sie Telefonnummern mit einer Landesvorwahl formatieren, verwenden Sie ein Pluszeichen (+) vor der Landesvorwahl und setzen Sie die Vorwahl in Klammern.

Geben Sie eine Nummer mit Landesvorwahl wie folgt an: +1 (504) 327-7269

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">123-456-7890</td><td style="width: 50%;">(123)-456-7890</td></tr>
<tr><td style="width: 50%;">+1 (123) 456-7890</td><td style="width: 50%;">1 234-567-9012</td></tr>
</tbody>
</table>
{:/}

##### Brüche

Schreiben Sie Brüche aus und verwenden Sie einen Bindestrich zwischen Zähler und Nenner. Verwenden Sie keine Ziffern, die durch einen Schrägstrich getrennt sind.

In einigen Fällen, in denen es notwendig ist, einen Bruch als Dezimalzahl auszudrücken, fügen Sie eine Null vor dem Dezimalpunkt für Brüche kleiner als eins hinzu.

Wenn Sie Bewertungssysteme mit Brüchen ausdrücken, verwenden Sie Ziffern, um die Bewertung auszuschreiben.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">0,5</td><td style="width: 50%;">1/2</td></tr>
<tr><td style="width: 50%;">ein Drittel</td><td style="width: 50%;">ein drittel</td></tr>
<tr><td style="width: 50%;">9 von 10</td><td style="width: 50%;">neun von zehn</td></tr>
</tbody>
</table>
{:/}

##### Prozentangaben

Verwenden Sie Ziffern und ein Prozentzeichen (%) ohne Leerzeichen dazwischen. Wenn der Prozentsatz jedoch den Satz beginnt, schreiben Sie den gesamten Prozentsatz aus (Zahl und Prozent).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">10%</td><td style="width: 50%;">10 %</td></tr>
<tr><td style="width: 50%;">Zwanzig Prozent der Unternehmensnutzenden sind...</td><td style="width: 50%;">20% der Unternehmensnutzenden sind...</td></tr>
</tbody>
</table>
{:/}

##### Bereiche

Verwenden Sie einen Bindestrich, um einen Zahlenbereich anzuzeigen. Verwenden Sie keinen Halbgeviertstrich, um Zahlen in einem Bereich zu trennen.

Für Zahlenbereiche mit Einheiten wiederholen Sie die Maßeinheit nach der Zahl. Dies gilt nicht für die Wiederholung von Substantiven. Verwenden Sie das Wort „bis" zwischen den Zahlen im Bereich, um Verwirrung zu vermeiden.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">5 bis 100</td><td style="width: 50%;">5–100</td></tr>
<tr><td style="width: 50%;">-10°C bis 50°C</td><td style="width: 50%;">-10°C-50°C</td></tr>
</tbody>
</table>
{:/}

#### Platzhaltertext {#placeholder-text}

Verwenden Sie Platzhaltertext, um anzuzeigen, wo die Lesenden den relevanten Wert angeben sollten. Platzhaltertext sollte den dargestellten Inhalt angeben. Zum Beispiel zeigt *YOUR_API_KEY* den API-Schlüssel der Lesenden an.

##### Platzhalter schreiben

Beim Erstellen von Platzhaltertext beziehen Sie sich auf die folgenden Richtlinien:

| Richtlinie | Beispiel |
| :---- | :---- |
| Verwenden Sie Großbuchstaben und trennen Sie Wörter mit Unterstrichen (_). | `PLACEHOLDER_VARIABLE` |
| Für Inline-Platzhaltertext verwenden Sie Kursivschrift. | *`PLACEHOLDER_VARIABLE`* |
| Für API-Codeblock-Platzhaltertext (wo Sie keine Kursivschrift verwenden können) setzen Sie die Platzhalter in geschweifte Klammern ({}). | `<string name="com_appboy_api_key">{YOUR_APP_IDENTIFIER_API_KEY}</string>` |
| Für Liquid-Codeblock-Platzhaltertext (wo Sie keine Kursivschrift verwenden können) verwenden Sie Großbuchstaben. | `{% raw %}{%- connected_content YOUR-API-URL :save items -%}{% endraw %}` |
| Opfern Sie nicht die Klarheit für Kürze. Verwenden Sie so viele Wörter wie nötig, um einen Platzhalter darzustellen. | **Richtig:** `CAMPAIGN_NAME` <br> **Falsch**: _`NAME`_|

##### Platzhalter verwenden

Beim Einführen oder Erklären eines Platzhalters beziehen Sie sich auf die folgenden Richtlinien:

| Richtlinie | Beispiel |
| :---- | :---- |
| Weisen Sie auf Platzhalter unmittelbar nach dem Platzhalter hin. | Ersetzen Sie `<YOUR_APP_IDENTIFIER_API_KEY>` durch Ihren [App Identifier API Key]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key), den Sie auf der Seite **Einstellungen** finden. |
| Um auf zwei oder mehr Platzhalter gleichzeitig hinzuweisen, verwenden Sie eine Aufzählungsliste. Listen Sie jeden Platzhalter in der Reihenfolge auf, in der er im Code erscheint. | Ersetzen Sie Folgendes: {::nomarkdown}<ul><li><code>PLACEHOLDER_VARIABLE</code>: eine Beschreibung dessen, was der Platzhalter darstellt</li><li><code>PLACEHOLDER_VARIABLE</code>: eine Beschreibung dessen, was der Platzhalter darstellt</li></ul>{:/} |
| Beziehen Sie sich auf den Platzhalter in derselben Formatierung, in der er im Text oder Code angezeigt wird. | `target <YOUR_APP_TARGET> do pod 'Appboy-iOS-SDK' end` <br><br> Ersetzen Sie `<YOUR_APP_TARGET>` durch den Namen Ihrer Ziel-App. |

#### Produkte {#products}

Wenn Sie sich auf Braze und seine Features beziehen, verwenden Sie vollständige Produkt- und Feature-Namen und schreiben Sie sie gemäß der UI groß. Schreiben Sie Vorlagen oder allgemeine Features nicht groß. Eine Liste der Produktnamen und ihrer Schreibweise finden Sie im [Glossar](#glossary).

Kürzen Sie Produkt- oder Feature-Namen nicht ab, außer in den folgenden Fällen:

* Um der UI zu entsprechen
* Um begrenzten Platzanforderungen gerecht zu werden

Verwenden Sie niemals Produkt- oder Feature-Namen als Verben.

Verwenden Sie niemals einen Apostroph nach Braze (Beispiel: „Braze's"). Es klingt unnatürlich. Bilden Sie stattdessen Possessive mit einer Präposition („von, aus") gefolgt vom Firmennamen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Das neueste Produktupdate von Braze</td><td style="width: 50%;">Brazes neuestes Produktupdate</td></tr>
<tr><td style="width: 50%;">Das ist eines der bestimmenden Features von Braze.</td><td style="width: 50%;">Das ist eines von Brazes bestimmenden Features.</td></tr>
</tbody>
</table>
{:/}

Beziehen Sie sich auf „Braze" als „wir/unser/unsere". Niemals „es/sein/sie/ihr".

#### Tabellen {#tables}

Die Verwendung von Tabellen kann eine hilfreiche und organisierte Möglichkeit sein, Informationen darzustellen. Stellen Sie sicher, dass Sie klare, beschreibende Überschriften und relevante Daten in den jeweiligen Spalten und Zeilen haben.

Verwenden Sie immer einen einleitenden Satz, um den Zweck der Tabelle zu beschreiben. Vermeiden Sie die Verwendung von Tabellen mitten in nummerierten Verfahren. Erwägen Sie stattdessen die Verwendung einer Liste.

#### Maßeinheiten {#units-of-measurement}

Verwenden Sie für HTML und Markdown ein geschütztes Leerzeichen (&nbsp) zwischen der Zahl und der Einheit, wenn Sie eine Maßeinheit angeben. Dies umfasst die meisten Maßeinheiten wie Entfernung, Pixel, Punkte, Gewicht und Temperaturgrade (zwischen dem Grad und der Maßeinheit).

Für Währung, Prozent oder Winkelgrade verwenden Sie kein Leerzeichen zwischen der Zahl und der Einheit.

Für Zahlenbereiche mit Einheiten wiederholen Sie die Einheit für jede Zahl. Verwenden Sie bei Raten „pro" anstelle eines Schrägstrichs (/).

### Verlinkung {#linking}

#### Querverweislinks {#cross-reference-links}

Verwenden Sie Querverweise, um Nutzende zu zusätzlichen Ressourcen zu führen. Verwenden Sie in der Braze-Dokumentation site-root-relative URLs, um auf andere Braze-Dokumente zu verlinken (ersetzen Sie „www.braze.com/docs" durch „{{site.baseurl}}").

Vermeiden Sie es, mehrere Links zum selben Dokument innerhalb einer bestimmten Seite hinzuzufügen, da dies zu Link-Müdigkeit führen kann. Doppelte Links sind in Maßen in Ordnung, wenn Sie auf einen bestimmten Abschnitt auf einer anderen Seite verlinken oder wenn die Seite, von der Sie verlinken, lang ist.

#### Videos einbetten {#embedding-videos}

Ähnlich wie Bilder verwenden Sie Videos, um Abwechslung in Ihre Lernmaterialien zu bringen. Die meisten Menschen lernen am besten mit einer Kombination von Medien, stellen Sie also sicher, dass alle Inhalte, die Sie in ein Video aufnehmen, auch im Artikel oder in der Lektion behandelt werden.

Um ein Video in die Braze-Dokumentation einzubetten, lesen Sie den [Embedded Video Test]({{site.baseurl}}/home/styling_test_page/#embedded-video-test).

#### Überschriften als Linkziele {#headings-as-link-targets}

In der Braze-Dokumentation werden Anker automatisch für Überschriften erstellt. Sie möchten jedoch möglicherweise einen benutzerdefinierten Anker zu einer Überschrift hinzufügen, wenn:

* Ihr automatisch generierter Anker sehr lang ist.
* Ihre Überschrift häufig verlinkt werden könnte. Das Hinzufügen eines benutzerdefinierten Ankers reduziert die Wahrscheinlichkeit, dass Links brechen, wenn der Überschriftentext später geändert wird.

Um einen Anker zu einer Überschrift in der Braze-Dokumentation hinzuzufügen, lesen Sie [Benutzerdefinierte Anker]({{site.baseurl}}/home/styling_test_page/#custom-header-anchor).

#### Linktext {#link-text}

Effektiver Linktext hilft, die Auffindbarkeit, Entdeckbarkeit und Barrierefreiheit Ihrer Inhalte zu verbessern.

##### Links strukturieren {#structuring-links}

Verwenden Sie eines der folgenden Formate beim Schreiben von Links:

* Passen Sie den Linktext an den Titel oder die Überschrift des Linkziels an.
* Verwenden Sie eine Beschreibung des Linkziels als Linktext.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Linktext an den Titel oder die Überschrift des Linkziels anpassen.</em></th><th style="width: 50%;">Richtig: <em>Eine Beschreibung des Linkziels als Linktext verwenden.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Starten Sie mit dem Braze <a href="{{site.baseurl}}/user_guide/getting_started/web_sdk/">Web SDK</a>.</td><td style="width: 50%;">Um Ihren spezifischen Cluster oder Endpunkt herauszufinden, <a href="{{site.baseurl}}/braze_support/">kontaktieren Sie den Support</a>.</td></tr>
<tr><td style="width: 50%;">Weitere Informationen finden Sie unter <a href="{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/">Liquid-Nachrichten abbrechen</a>.</td><td style="width: 50%;">Im Zweifelsfall können Sie jederzeit <a href="{{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password">Ihr Passwort zurücksetzen</a>.</td></tr>
</tbody>
</table>
{:/}

Möglicherweise müssen Sie einen Satz umformulieren, um guten Linktext zu erstellen.

Wenn Sie auf einen Abschnitt auf derselben Seite verlinken, verwenden Sie eine Standardformulierung, die diese Aktion anzeigt. Zum Beispiel:

* Auf dieser Seite siehe [Überschrift].
* In diesem Dokument lesen Sie [Überschrift].
* Weitere Informationen finden Sie im Abschnitt [Überschrift].

##### Links schreiben {#writing-links}

Wenden Sie die folgenden Richtlinien beim Schreiben von Linktext an:

* Setzen Sie den Link in die relevanten Schlüsselwörter.
* Wenn Sie einen vollständigen Satz schreiben, der die Lesenden auf einen anderen Artikel verweist, verwenden Sie die Phrase „Weitere Informationen finden Sie unter" oder „Weitere Informationen zu [Thema] finden Sie unter".
* Fügen Sie nur dann einen „Mehr erfahren…"-Satz hinzu, wenn der Hilfetext mehr als ein Konzept behandelt, von denen jedes auf ein eigenes Hilfedokument verlinkt werden könnte. Wählen Sie in dieser Situation den am besten geeigneten Link und kontextualisieren Sie ihn mit „Mehr erfahren…"
* Um einen informellen Ton beizubehalten, verwenden Sie nicht „bitte", um Linktext einzuführen. Vermeiden Sie zum Beispiel die Phrasen „Bitte lesen Sie", „Bitte sehen Sie" und „Bitte kontaktieren Sie".
* Schreiben Sie einzigartigen, beschreibenden Linktext, der auch ohne den umgebenden Text Sinn ergibt. Forschung der [Nielsen Norman Group](https://www.nngroup.com/articles/link-promise/#links-should-stand-alone) (NN/g) zeigt, dass Lesende nach auffälligen Informationen auf einer Seite scannen, stellen Sie also sicher, dass Links für sich allein stehen können.
* Verwenden Sie nicht die folgenden Wörter oder Phrasen als Linktext. Sie sind schlecht für Barrierefreiheit und Scannbarkeit.
 * Mehr erfahren (allein)
 * Hier klicken
 * hier
 * dieses Dokument
 * dieser Artikel

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Sicherstellen, dass der Linktext auch ohne den umgebenden Text Sinn ergibt</em></th><th style="width: 50%;">Falsch: <em>Vagen oder nicht-beschreibenden Linktext verwenden</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Weitere Informationen zum Importieren von Kundendaten finden Sie unter <a href="{{site.baseurl}}">Nutzerimport</a>.</td><td style="width: 50%;">Weitere Informationen finden Sie <a href="{{site.baseurl}}">hier</a>.</td></tr>
<tr><td style="width: 50%;">Diese Funktion verbindet sich mit dem Endpunkt <a href="{{site.baseurl}}">Nutzer tracken</a>.</td><td style="width: 50%;">Siehe <a href="{{site.baseurl}}">diesen Artikel</a>.</td></tr>
<tr><td style="width: 50%;">Erfahren Sie mehr über <a href="{{site.baseurl}}">die Neuerungen in Android SDK 16.0.0</a>.</td><td style="width: 50%;">Folgen Sie den Anweisungen <a href="{{site.baseurl}}">hier</a>.</td></tr>
<tr><td style="width: 50%;">Erfahren Sie mehr über die <a href="https://www.braze.com/product">Braze-Plattform</a>.</td><td style="width: 50%;">Für die Schritte lesen Sie <a href="{{site.baseurl}}">dieses Dokument</a>. <a href="{{site.baseurl}}">Mehr erfahren</a>.</td></tr>
<tr><td style="width: 50%;">Storefront-API-Schlüssel sind pro Hydrogen-Storefront einzigartig, aber ihre Berechtigungsbereiche werden von allen Hydrogen-Storefronts geteilt. Erfahren Sie mehr über <a href="{{site.baseurl}}">Storefront-API-Tokens.</a></td><td style="width: 50%;"><a href="{{site.baseurl}}">Storefront-API-Tokens</a> sind pro <a href="{{site.baseurl}}">Hydrogen-Storefront</a> einzigartig, aber ihre <a href="{{site.baseurl}}">Berechtigungsbereiche</a> werden über alle Hydrogen-Storefronts geteilt.</td></tr>
</tbody>
</table>
{:/}

#### Links für Endpunkte {#links-for-endpoints}

Wenn Sie auf Endpunkt-Artikel verweisen, verwenden Sie [aussagekräftigen Linktext](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.79ujl0qtumog), der auch ohne Kontext Sinn ergibt. Wenn Sie den Pfad des Endpunkts als Link verwenden, stellen Sie sicher, dass Sie Details im umgebenden Text angeben, da der Pfad die Funktion des Endpunkts möglicherweise nicht klar kommuniziert.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Löschen Sie Nutzerprofile mit dem Braze-Endpunkt <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Nutzer löschen</a>.</td><td style="width: 50%;">Löschen Sie Nutzerprofile mit dem Braze-Endpunkt <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Nutzer löschen</a>.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code>-Endpunkt</a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a>-Endpunkt</td></tr>
</tbody>
</table>
{:/}

#### Links zum Dateidownload {#links-for-file-download}

Wenn ein Link eine Datei herunterlädt, machen Sie das im Linktext deutlich und erwähnen Sie den Dateityp.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig: <em>Sicherstellen, dass der Linktext kommuniziert, dass die Auswahl eine Datei herunterlädt</em></th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Für Tipps laden Sie das <a href="{{site.baseurl}}">Regex-Spickzettel-PDF</a> herunter.</td><td style="width: 50%;">Schauen Sie sich unseren <a href="{{site.baseurl}}">RegEx-Spickzettel</a> an.</td></tr>
<tr><td style="width: 50%;">Weitere Informationen finden Sie im <a href="{{site.baseurl}}">Success and Support Services Handbook PDF</a> zum Download.</td><td style="width: 50%;"><a href="{{site.baseurl}}">Success and Support Services Handbook</a></td></tr>
</tbody>
</table>
{:/}

#### Links zu anderen Websites {#links-to-other-sites}

Als allgemeine Regel verlinken Sie nicht auf eine andere Website, wenn Sie die Informationen mit einer kurzen Erklärung abdecken können. Wir können nicht nachverfolgen, wann sich der Inhalt auf einer anderen Website ändert.

Wenn Sie auf eine externe Website verlinken, stellen Sie sicher, dass die Website, auf die Sie verlinken, hochwertig, zuverlässig und seriös ist. Wenn möglich, verlinken Sie auf die relevanteste Überschrift auf einer Seite.

Verwenden Sie ein Symbol für externe Links, um anzuzeigen, dass der Link zu einer anderen Domain führt. In der Braze-Dokumentation wird dies automatisch auf externe Links angewendet.

#### URLs für Bilder {#urls-for-images}

Verwenden Sie in der Braze-Dokumentation site-root-relative URLs, um auf Bilder zu verlinken. Weitere Informationen finden Sie unter [Bilder hinzufügen und bearbeiten](https://github.com/braze-inc/braze-docs/wiki/Editing-Content#adding-and-editing-images).

### Glossar {#glossary}

⚠️ = Mit Vorsicht verwenden, relevante Hinweise beachten
⛔️ = Nicht verwenden

#### Ziffern

**24/7**
Nur mit Bindestrich (24-7), wenn als Modifikator vor einem Substantiv verwendet.

**2D / zweidimensional**

**3D / dreidimensional**

#### A

**A/B-Tests**

⚠️ **abort**
Vermeiden Sie die Verwendung, es sei denn, Sie beziehen sich auf einen spezifisch benannten Prozess. Verwenden Sie stattdessen Wörter wie „stoppen", „beenden", „abbrechen" oder „aufhören".

**Aktions-Buttons**

**aktionsbasierte Zustellung**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

⛔️ **ad hoc**
Nicht verwenden. Verwenden Sie „einmalig" oder ähnliches.

**AI**
Bevorzugt gegenüber „künstliche Intelligenz" nach der ersten Erwähnung.

**AI-Artikelempfehlung**

**Alloys / Braze-Technologie-Partner**
Immer großgeschrieben.

**alphanumerisch**
Nicht mit Bindestrich.

**always-on**

**am**
Kleingeschrieben bei Zeitangaben (zum Beispiel „10 am"). Siehe auch [pm](#glossary).

**Amazon S3**

**Amazon Web Services (AWS)**
Immer großgeschrieben. Bei der ersten Erwähnung ausschreiben, danach ist das Akronym in Ordnung.

**AMP for Email / Braze AMP for Email**

**Android**

**API / Application Programming Interface**
Bei der ersten Erwähnung ausschreiben, danach ist das Akronym in Ordnung.

**API key**

**APNs / Apple Push Notification service**

**⛔️ App-Gruppe**
Nicht verwenden. App-Gruppe wurde in Workspace umbenannt.

**Apple iOS-Plattform**

**AppleWatch**

**.avro**

#### B

**Verhalten, Verhaltensweisen**

**Benchmarks**

**Beta**

**BI Insights**

**Binge-Watching**

**Binge-Watch**

**Bonfire / Bonfire-Community / Braze Bonfire-Community**
Verwenden Sie „Braze Bonfire-Community" bei der ersten Erwähnung, danach ist „Bonfire" oder „Bonfire-Community" in Ordnung.

**boolean**

⛔️ **Blacklist**
Nicht verwenden. Verwenden Sie stattdessen „Blocklist" oder „Denylist". Für die Verbform dieser Wörter erwägen Sie, den Satz umzuformulieren, um den problematischen Begriff zu entfernen. Zum Beispiel:

>✅ **Empfohlen:** Um eine vorhandene Eigenschaft für die Verwendung in neuen Nachrichten zu blockieren, wählen Sie **Eigenschaften verwalten**. <br>
>⛔️ **Nicht empfohlen:** Um eine vorhandene Eigenschaft auf die Blocklist zu setzen, wählen Sie **Eigenschaften verwalten**.

**Braze-to-Braze-Webhook**

**Business-Intelligence (BI)**
Bei der ersten Erwähnung ausschreiben, danach ist das Akronym in Ordnung.

#### C

**California Consumer Privacy Act (CCPA)**
Bei der ersten Erwähnung ausschreiben, danach ist das Akronym in Ordnung. Siehe auch [CCPA-Compliance (Substantiv) / CCPA-konform (Adjektiv)](#ccpa-compliance)

**can**
Verwenden Sie „können", um sich auf eine optionale Aktion oder ein Ergebnis zu beziehen. Zum Beispiel:

> ✅ **Empfohlen:** Sie können auch Nutzerprofile mit CSV-Dateien hochladen und aktualisieren.
> ✅ **Empfohlen:** Der Importvorgang kann einige Minuten dauern.

Verwenden Sie „können" nicht für Anweisungen. Bevorzugen Sie stattdessen das Imperativverb. Beispiele finden Sie unter [Zweite und erste Person](#second-person-and-first-person).

**Canvas**
Immer großgeschrieben. Plural ist „Canvases".

**Canvas Flow**
Verwenden Sie dies, wenn Sie zwischen dem ursprünglichen Canvas-Editor und Canvas Flow unterscheiden. Verwenden Sie andernfalls „Canvas".

**Kampagne**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**Kapazität**
Verwenden Sie dies, wenn Sie sich auf Limits bei angepassten Daten beziehen, anstelle des Wortes „Limit".

**Katalog**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**CCPA-Compliance (Substantiv) / CCPA-konform (Adjektiv)** {#ccpa-compliance}

**CEO, CFO, CMO, COO, CTO**

**Abwanderung**
Verwenden Sie dies, um sich auf Kundenfluktuation oder -verlust zu beziehen.

**Abwanderungsprognose**
Kleingeschrieben, außer wenn auf die UI verwiesen wird.

**Kontrollkästchen**

**Check-in (Substantiv) / einchecken (Verb)**

**City x City**

**Mitgründer**

**Content Cards / Braze Content Cards**

**Content-Blöcke**

**Kontrollgruppe**

**Konversion**

**Konversionsgruppenanalyse**
Kleingeschrieben.

**Cordova**

**Currents / Braze-Currents**
Immer großgeschrieben.

**CRM / Customer Relationship Management**
Bei der ersten Erwähnung ausschreiben, danach ist das Akronym in Ordnung.

**kanalübergreifendes Messaging / kanalübergreifende Personalisierung**

**C-Suite**

**CSV / kommagetrennte Werte**

**angepasste Attribute**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**angepasste Events**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**Kundenattribute**

**Kundenverhalten**

**Customer Data Platform (CDP)**
Kleingeschrieben.

**Customer-Engagement**

**Kunden-Events**

**Customer Journey**

**Kundenzustimmung**

**Kundenbindung**

#### D

**Dark-Mode-Theme / Dark-Mode-Vorschau / Dark-Mode-Konzept**

**Dashboard / Braze-Dashboard**
Verwenden Sie dies, um sich auf Braze als Plattform zu beziehen. Verwenden Sie Kleinschreibung (Dashboard, nicht Dashboard).

**datengestützt (Adjektiv)**

**Datenschutz**

**Datenblatt**

**Datenstreaming**

**DAU / täglich aktive:r Nutzer:in**

**Decision-Splits**

**Deeplinking**

**Verzögerte Nachrichten**

**Ausfallzeit**

**per Drag-and-Drop (Verb) / Drag-and-Drop (Adjektiv)** {#drag-and-drop}
Verwenden Sie dies, wenn Sie sich auf das Ziehen von Dateien in eine Upload-Zone beziehen.

**Drag-and-Drop-Editor**
Verwenden Sie Titelschreibung, wenn Sie sich auf das Feature in der UI beziehen. Verwenden Sie andernfalls Kleinschreibung (Drag-and-Drop-Editor). Verwenden Sie das Verb, wenn Sie darauf verweisen, wie Kunden Elemente im Editor [per Drag-and-Drop](#drag-and-drop) verschieben können.

**aufschlüsseln (Verb) / Aufschlüsselung (Substantiv oder Adjektiv)**
Verwenden Sie dies in Inhalten über Daten und die daraus generierten Berichte.

**DTC / Direct to Consumer**

**dynamischer Content**

#### E

**Early Access**

⛔️ **z. B.**
Nicht verwenden. Verwenden Sie die Phrasen „zum Beispiel", „wie" oder ähnliches.

**eBook**

**E-Commerce**
Nicht „ecommerce" oder „e-commerce".

**Ökosystem**

**E-Mail**
Nicht „Email" oder „e-mail".

**E-Mail-Zustellbarkeit**

**E-Mail-Reputation**

**EMEA (Europa, Naher Osten und Asien)**

**Emoji**
Singular- und Pluralform.

**Endnutzer:in (Substantiv) / Endnutzer- (Adjektiv)**
Bevorzugen Sie „Ihre Nutzer" gegenüber „Endnutzer".

⚠️ **sicherstellen**
Vermeiden Sie die Verwendung, wenn Sie darüber sprechen, was ein Feature tut. Weitere Informationen finden Sie unter [Garantien vermeiden](#avoid-guarantees).

**ESP / E-Mail-Anbieter**

**Event-Prognose**

**Event-Eigenschaften / angepasste Event-Eigenschaften**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**Ausnahme-Events**

**extrahieren**
Verwenden Sie „extrahieren" anstelle von „entpacken", um sich auf das Extrahieren von Dateien aus einem komprimierten Ordner zu beziehen.

**externe ID**
Nicht „Externe ID". Bei Bezugnahme auf Code-Snippets verwenden Sie external_id.

#### F

**Facebook**

**FCM / Firebase Cloud Messaging**

**Firebrand / Firebrands**

**Forge [JAHR]**

**Frequency-Capping**

**Vollbild**
Wenn als Adjektiv verwendet (zum Beispiel „Vollbild-In-App-Nachrichten"), ohne Bindestrich schreiben.

#### G

**DSGVO / Datenschutz-Grundverordnung**
Bei der ersten Erwähnung ausschreiben, danach ist das Akronym in Ordnung.

**DSGVO-Compliance (Substantiv) / DSGVO-konform (Adjektiv)**

**Geofence**

**GIF**

**GitHub**
Nicht „Github" oder „github".

**Google / googelbar**

#### H

**Hochleistungs-**

**High-Value-Aktionen**

**HQ / Hauptsitz**

**HTML-E-Mail-Editor**

**HTTP**

#### I

⛔️ **d. h.**
Nicht verwenden. Verwenden Sie die Phrase „das heißt" oder ähnliches.

**In-App-Nachrichten**

**In-Browser-Nachricht (IBM)**

**Infografik**

**Install-Attribution**

**Integer**

**Intelligence Suite**
Titelschreibung verwenden.

**Intelligent Channel**
Titelschreibung verwenden.

**Intelligent Selection**
Titelschreibung verwenden.

**Intelligent Timing**
Titelschreibung verwenden.

⛔️ **Internet of Things**
Nicht verwenden.

**iOS**

**IP-Warming**

**iPad**

**iPhone**

**IT**

#### J

**JavaScript**

**JPEG / JPG**

**JSON / JavaScript Object Notation**

#### K

**Keynote (Programm) / Keynote (Substantiv)**

**anstoßen (Verb) / Kickoff (Substantiv)**

⚠️ **kill**
Vermeiden Sie die Verwendung, es sei denn, Sie beziehen sich auf einen spezifisch benannten Prozess. Verwenden Sie stattdessen Wörter wie „stoppen", „beenden", „abbrechen" oder „aufhören".

**KPI / Leistungskennzahl**

#### L

**Landing-Page**

**Lebenszyklus**

**Lift-Rate**

**LinkedIn**

**Liquid**
Immer großgeschrieben.

**Live-Vorschau**

**langfristig (Substantiv) / langfristig (Adjektiv)**

**LTV / Lifetime-Value**

#### M

**Marketingtechnologie**
Bevorzugt gegenüber „Martech".

**MAU / monatlich aktive:r Nutzer:in**

**Maximum**
Nicht „Max".

**Medienbibliothek**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**Microsoft**

**Microsoft Azure**

**ML / maschinelles Lernen**

**Mobile-Marketing**

**Mobile-Marketingautomatisierung**

**Mobile Moment**

**Mobiltelefon**

**Multichannel-Kampagne**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist. Kein Bindestrich.

**Mehrsprachige Unterstützung**

**Multivariate Tests**

#### N

**N/A**
Nicht „NA". Verwenden Sie „N/A" nach Bedarf in Tabellen, um Spalten- oder Zeileninhalte zu kennzeichnen, die für eine bestimmte Zelle nicht zutreffen. Im Fließtext bevorzugen Sie das ausgeschriebene „nicht verfügbar" oder „nicht zutreffend" für Klarheit.

⚠️ **neu**
Vermeiden Sie die Verwendung in Produktdokumentation und Lernmaterial, da dies Ihre Inhalte schnell veralten lassen kann. Weitere Informationen finden Sie unter [Zukünftige Features](#describing-limitations).

**NRT / nahezu in Echtzeit (Adjektiv) / nahezu Echtzeit (Substantiv)**

**NYC / New York City**

#### O

**On Demand**

**Onboarding**

**einmal**
Verwenden Sie dies, um sich auf die einmalige Ausführung einer Aktion zu beziehen. Verwenden Sie „einmal" nicht anstelle von „nachdem" oder „wenn".

**Öffnungsrate (OR)**

**Opt-in-Anfrage**

**Orchestrierung**

**OS / Betriebssystem**

**OTT / Over-the-top-Mediendienste**

⛔️ **out-of-the-box**
Nicht verwenden. Verwenden Sie stattdessen eine Alternative wie „Standard".

#### P

**Partner, Partner, Partnerschaft**

**Persona (Singular) / Personas (Plural)**

**Personalisierung**

**personenbezogene Daten (PII)**

**Personalized Path**
Titelschreibung verwenden.

**Personalized Variant**
Titelschreibung verwenden.

**PhD / PhDs**

**pm**
Kleingeschrieben bei Zeitangaben (zum Beispiel „10 pm"). Siehe auch [am](#glossary).

**vorangehend**

**Prognose**
Kleingeschrieben, es sei denn, „Braze" steht davor, wie „Eine Braze-Prognose ist…".

**Predictive Analytics**

**Predictive Churn**
Titelschreibung verwenden. Predictive Churn ist der Produktname, während Kunden eine [Abwanderungsprognose](#glossary) erstellen.

**Predictive Events**
Titelschreibung verwenden.

**Predictive Purchases**
Titelschreibung verwenden. Predictive Purchases ist der Produktname, während Kunden eine [Kaufprognose](#glossary) erstellen.

**Predictive Suite**
Titelschreibung verwenden.

**Präferenzcenter**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**Priming for Location**

**Priming for Push**

**Aktionscode**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist. Verwenden Sie nicht „Promo-Code".

**Kaufprognose**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**Kauf-Details**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**Push-Action-Buttons**

**Push Max**
Titelschreibung verwenden.

**Push-Benachrichtigung**

**Push-Storys**
Titelschreibung verwenden.

#### Q

**Q&A**

⛔️ **QA (Qualitätssicherung)**
Verwenden Sie das Akronym nicht als Verb. Formulieren Sie stattdessen um zu „Qualitätssicherung durchführen".

**Ruhezeiten**
Verwenden Sie „Ruhezeiten" am Satzanfang und „Ruhezeiten" in der Satzmitte. Verwenden Sie keine Titelschreibung „Ruhezeiten", da es kein Markenfeature ist.

⚠️ **schnell / schnell**
Vermeiden Sie die Verwendung. Was für Sie schnell ist, ist möglicherweise nicht schnell für andere. Verwandte Richtlinien finden Sie unter [Herablassende Sprache](#condescending-language).

#### R

**Rate-Limiting**

**Realtime (Substantiv) / Echtzeit- (Adjektiv)**

**erneute Interaktion**

⚠️ **regulärer Ausdruck / Regex**
Bevorzugen Sie die ausgeschriebene Version gegenüber der Abkürzung „Regex". Verwenden Sie nicht „RegEx".

**Beziehungsmarketing**

**Retargeting**

**Bindung**

**Rich-Push-Benachrichtigung**

**rechtsklicken**

**nach rechts wischen**

**ROI / Kapitalrendite**

#### S

**Sage AI by Braze™**

⛔️ **Sanity Check**
Nicht verwenden. Verwenden Sie stattdessen einen Begriff wie „schnelle Überprüfung" oder „vorläufige Überprüfung". Alternativ leiten Sie Überprüfungsanweisungen mit einer Phrase wie „Lassen Sie uns überprüfen, ob alles funktioniert" ein.

**geplante Zustellung**
Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**Screenshot**

**Screenshot**

**SDK / Software Developer Kit**

**Segment (Zielgruppe)**

**Segmenterweiterungen**
Titelschreibung verwenden.

**Segment-Insights**
Titelschreibung verwenden.

**Segmentierung**

**Auswahl**
Wie beim Feature innerhalb von Katalogen. Kleingeschrieben, außer wenn auf ein UI-Element verwiesen wird, das großgeschrieben ist.

**SF / San Francisco**

**Silicon Valley**

**Silo, Silos, isoliert**

**einfache Umfrage**

**Diashow**

**Smartphone**

**Smartwatch**

**SMS**

**Software as a Service (SaaS)**
Bei der ersten Erwähnung ausschreiben, danach ist das Akronym in Ordnung.

**Spam-Test**

**SQL / Structured Query Language**

**SQL-Segmenterweiterungen**
Titelschreibung verwenden.

**Stickiness**

**Streaming**

**String**
Für nicht-technische Zielgruppen definieren Sie einen String als Text, der „alphanumerische Zeichen" enthält. Für technische Zielgruppen ist es in Ordnung, diesen Begriff nicht zu definieren.

**Abo-Gruppe**

**Sunsetting**

#### T

**gezielte Antwort**

⚠️ **terminate**
Vermeiden Sie die Verwendung, es sei denn, Sie beziehen sich auf einen spezifisch benannten Prozess. Verwenden Sie stattdessen Wörter wie „stoppen", „beenden", „abbrechen" oder „aufhören".

**Drittanbieter-**

**Zeitzone**
Nicht „Timezone".

**Zeitstempel**

**Touchscreen**

**getriggerte Nachricht**

**Twitter**

#### U

**UK / Vereinigtes Königreich**

⛔️ **entpacken**
Nicht verwenden. Verwenden Sie stattdessen „extrahieren".

**URL**
Wird als einzelne Buchstaben U-R-L ausgesprochen, schreiben Sie also „eine URL" statt „ein URL". Verwenden Sie Großbuchstaben. Für den Plural verwenden Sie URLs.

**US / USA**
Keine Punkte.

**Anwendungsfälle**

**Nutzerattribute / Standard-Nutzerattribute**
Verwenden Sie dies, um sich auf Nutzerdaten zu beziehen, die automatisch von Braze erfasst werden.

**Nutzerprofil**

**Benutzername**

⚠️ **nutzen**
Verwenden Sie nicht „nutzen", wenn Sie „verwenden" meinen. Verwenden Sie „nutzen", um sich auf etwas zu beziehen, das über seinen ursprünglich vorgesehenen Zweck hinaus verwendet wird.

#### V

**Variante**

⛔️ **via**
Nicht verwenden. Verwenden Sie stattdessen Begriffe wie „über" oder Phrasen wie „mittels" oder „auf dem Weg über".

⛔️ **vice versa**
Nicht verwenden. Verwenden Sie stattdessen Begriffe wie „umgekehrt" oder eine Phrase wie „andersherum".

**schreibgeschützt**

⚠️ **vs.**
Verwenden Sie nicht „vs." als Abkürzung für „versus". Schreiben Sie stattdessen das Wort aus.

#### W

**Web-Messaging**

**Web-Push**

**Webhook**

**Webinar**

**Whitelabel**

⛔️ **Whitelist**
Nicht verwenden, es sei denn, Sie beziehen sich auf die UI. Verwenden Sie stattdessen „Allowlist" oder „Safelist". Für die Verbform dieser Wörter erwägen Sie, den Satz umzuformulieren, um den problematischen Begriff zu entfernen. Beispiele finden Sie unter [Blacklist](#glossary).

⚠️ **Wi-Fi**
Verwenden Sie nicht „WiFi", „wi-fi" oder „wifi".

**wird**
Vermeiden Sie die Verwendung von „wird" oder „würde". Siehe [Präsens](#present-tense).

**Winning Path**
Titelschreibung verwenden.

**Winning Variant**
Titelschreibung verwenden.

⛔️ **Wizard**
Nicht verwenden. Verwenden Sie stattdessen „Composer".

**WordPress**

**Workspace**

**www**

#### Y

**YAML**
Verwenden Sie keine Dateierweiterung, um sich auf den Dateityp zu beziehen. Verwenden Sie zum Beispiel „YAML-Datei" anstelle von „.yaml-Datei".

**YouTube**

#### Z

**Postleitzahl**

**ZIP-Datei / komprimierte Dateien**

**ZIP**
Verwenden Sie keine Dateierweiterung, um sich auf den Dateityp zu beziehen. Verwenden Sie zum Beispiel „ZIP-Datei" anstelle von „.zip-Datei".