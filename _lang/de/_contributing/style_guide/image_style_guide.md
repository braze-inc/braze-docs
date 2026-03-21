---
nav_title: Stilrichtlinien für Bildtexte
article_title: Stilrichtlinien für Bildtexte
description: "Richtlinien für die Erstellung und Gestaltung von Bildern in Braze Docs."
page_order: 1
noindex: true
---

# Stilrichtlinien für Bildtexte

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

## Platzierung und Größe optimieren

Platzieren Sie Bilder nach Möglichkeit in der Nähe des zugehörigen Textes und achten Sie darauf, Markdown zur Bildformatierung zu verwenden, um größere Bilder anzupassen. Bei manchen Inhalten sollte dies durch [Verankern von Text an der linken oder rechten Seite der Seite]({{site.baseurl}}/home/styling_test_page/#image-test) erfolgen – je nach Bild und verfügbarem Platz.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_do.png %}" alt="Beispiel für eine korrekt optimierte Bildplatzierung."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_dont.png %}" alt="Beispiel für eine inkorrekt optimierte Bildplatzierung."></td></tr>
</tbody>
</table>
{:/}

## Bilder zuschneiden

Schneiden Sie relevante Bereiche eng zu. Fügen Sie die linke Navigationsleiste nur ein, wenn es unbedingt nötig ist, und geben Sie stattdessen Navigationsanweisungen im Artikel an. So wird die Anzahl der Bilder begrenzt, die bei UI-Änderungen aktualisiert werden müssen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_1.png %}" alt="Beispiel für ein korrekt zugeschnittenes Bild."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_1.png %}" alt="Beispiel für ein inkorrekt zugeschnittenes Bild."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_2.png %}" alt="Beispiel für ein korrekt zugeschnittenes Bild."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_2.png %}" alt="Beispiel für ein inkorrekt zugeschnittenes Bild."></td></tr>
</tbody>
</table>
{:/}

Da Braze Docs bereits einen Rahmen um jedes Bild hinzufügt, lassen Sie Rahmen in Abschnitts-Screenshots weg. Wir streben einen sauberen Zuschnitt an. Der Rahmen kann beibehalten werden, wenn es Komponenten gibt, die außerhalb oder innerhalb des Rahmens liegen – siehe die folgenden Bilder als Beispiele.

**Richtig:**
![Beispiel für ein korrekt zugeschnittenes Bild.]({% image_buster /assets/img/contributing/style_guide/cropping_do_3.png %})

**Falsch:**  
![Beispiel für ein inkorrekt zugeschnittenes Bild.]({% image_buster /assets/img/contributing/style_guide/cropping_dont_3.png %})
  
**Richtig:**  
![Beispiel für ein korrekt zugeschnittenes Bild.]({% image_buster /assets/img/contributing/style_guide/cropping_do_4.png %})

## Sensible Informationen unkenntlich machen

Machen Sie alle personenbezogenen Daten (PII) wie Namen, E-Mails und API-Schlüssel unkenntlich.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_do.png %}" alt="Beispiel für korrektes Unkenntlichmachen."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_dont.png %}" alt="Beispiel für inkorrektes Unkenntlichmachen."></td></tr>
</tbody>
</table>
{:/}

## Keinen wichtigen Text in Bilder einbetten

Vermeiden Sie es, Text in Bilder einzubetten, da nicht alle Nutzer:innen englischen Text lesen können (und Seitenübersetzungstools keine Bilder übersetzen). Dieser Text sollte im Artikel bereitgestellt werden. Fügen Sie Alternativtext für Bilder hinzu, um maximale Barrierefreiheit für Nutzer:innen zu gewährleisten.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_do.png %}" alt="Beispiel für korrektes Vermeiden von eingebettetem Text in einem Bild."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_dont.png %}" alt="Beispiel für inkorrekt eingebetteten Text in einem Bild."></td></tr>
</tbody>
</table>
{:/}

## Komponenten nicht hervorheben

Heben Sie Komponenten in Bildern nur hervor, wenn es unbedingt nötig ist. Verwenden Sie blaue Rechtecke (die barrierefreieste Option) mit dünner bis mittlerer Strichstärke, um verschiedene Komponenten in Bildern hervorzuheben. Stellen Sie sicher, dass die „hervorgehobenen Bereiche" die normale UI nicht verdecken.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_1.png %}" alt="Beispiel für korrektes Hervorheben von Komponenten in einem Bild."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_1.png %}" alt="Beispiel für inkorrektes Hervorheben von Komponenten in einem Bild."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_2.png %}" alt="Beispiel für korrektes Hervorheben von Komponenten in einem Bild."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_2.png %}" alt="Beispiel für inkorrektes Hervorheben von Komponenten in einem Bild."></td></tr>
</tbody>
</table>
{:/}