---
nav_title: Rechner für Rechnungen
article_title: SMS- und RCS-Abrechnungsrechner
page_order: 5
description: "In diesem referenzierten Artikel erfahren Sie, was ein SMS-Segment ist, wie es für die Abrechnung gezählt wird und was Sie bei der Erstellung von SMS- und RCS-Nachrichtenkopien beachten müssen."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# SMS- und RCS-Abrechnungsrechner

> Bei Braze werden SMS-Nachrichten pro Nachrichten-Segment abgerechnet, während RCS-Nachrichten pro Nachricht abgerechnet werden. Wenn Sie verstehen, was ein SMS Segment und die verschiedenen RCS-Abrechnungsarten definiert, können Sie besser nachvollziehen, wie Sie abgerechnet werden und versehentliche Mehrkosten vermeiden.

## SMS Nachrichten kopieren und Segmentierung berechnen

SMS Nachrichten werden pro Nachrichten-Segment abgerechnet. Um Ihre Abrechnung zu verstehen, müssen Sie wissen, wie die SMS-Nachrichten aufgeteilt werden.

### Was ist ein SMS-Segment?

Der Short Messaging Service (SMS) ist ein standardisiertes Kommunikationsprotokoll, mit dem Geräte kurze Textnachrichten senden und empfangen können. Es wurde so konzipiert, dass es zwischen andere Signalisierungsprotokolle passt. Deshalb ist die Länge von SMS-Nachrichten auf 160 7-Bit-Zeichen begrenzt, also 1120 Bits oder 140 Bytes. SMS-Nachrichtensegmente sind die Zeichenpakete, die die Telefongesellschaften zur Messung von Textnachrichten verwenden. Nachrichten werden pro Nachrichtensegment abgerechnet. Kunden, die SMS nutzen, profitieren also sehr davon, wenn sie die Feinheiten der Aufteilung der Nachrichten kennen.

Wenn Sie eine SMS-Kampagne oder ein Canvas mit Braze erstellen, sind die Nachrichten, die Sie im Editor erstellen, zwar repräsentativ für das, was Ihre Nutzer:innen sehen, wenn die Nachricht ihrem Telefon zugestellt wird, aber **sie geben keinen Hinweis darauf, wie Ihre Nachricht in Segmente aufgeteilt wird und wie Sie letztendlich abgerechnet werden**. Es liegt in Ihrer Verantwortung, zu verstehen, wie viele Segmente gesendet werden, und sich der potenziellen Überschreitungen bewusst zu sein, die auftreten können. Wir stellen jedoch einige Ressourcen zur Verfügung, um Ihnen dies zu erleichtern. Sehen Sie sich unseren internen [Segmentrechner](#segment-calculator) an.

![]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Segmentierung

Das Zeichenlimit für **ein eigenständiges SMS-Segment** beträgt 160 Zeichen[(GSM-7-Kodierung](https://en.wikipedia.org/wiki/GSM_03.38) ) oder 70 Zeichen[(UCS-2-Kodierung](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) ), je nach Kodierungstyp. Die meisten Telefone und Netze unterstützen jedoch die Verkettung und bieten längere SMS-Nachrichten mit bis zu 1530 Zeichen (GSM-7) oder 670 Zeichen (UCS-2). Eine Nachricht kann zwar mehrere Segmente enthalten, aber wenn sie diese Verkettungsgrenzen nicht überschreitet, wird sie als eine Nachricht betrachtet und als solche gemeldet.

Bitte beachten Sie, dass **zusätzliche Zeichen, sobald Sie das Zeichenlimit Ihres ersten Segments überschreiten, dazu führen, dass Ihre gesamte Nachricht geteilt und auf der Grundlage der neuen Zeichengrenzen segmentiert** wird:
- **GSM-7-Kodierung**
    - Nachrichten, die die 160-Zeichen-Grenze überschreiten, werden jetzt in Segmente mit 153 Zeichen segmentiert und einzeln versendet und dann vom Gerät des Empfängers:in wieder zusammengesetzt. Eine Nachricht mit 161 Zeichen wird z. B. in zwei Nachrichten gesendet, eine mit 153 Zeichen und die zweite mit 8 Zeichen.
- **UCS-2-Kodierung**
    - Wenn Sie Nicht-GSM-Zeichen wie Emojis, chinesische, koreanische oder japanische Schriftzeichen in SMS-Nachrichten einfügen, müssen diese Nachrichten mit UCS-2-Kodierung gesendet werden. Nachrichten, die das anfängliche Segmentlimit von 70 Zeichen überschreiten, werden in 67-Zeichen-Nachrichtensegmente unterteilt. Zum Beispiel wird eine Nachricht mit 71 Zeichen als zwei Nachrichten gesendet, eine mit 67 Zeichen und die zweite mit 4 Zeichen.

Unabhängig von der Kodierungsart hat jede von Braze versandte SMS ein Limit von bis zu 10 Segmenten und ist kompatibel mit [Liquid Templating]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/), [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), Emojis und Links.

{% tabs %}
{% tab GSM-7 encoding %}
| Anzahl der Zeichen | Wie viele Segmente? |
| -------------------- | ----------------- |
| 0 - 160 Zeichen | 1 Segment |
| 161 - 306 Zeichen | 2 Segmente |
| 307 - 459 Zeichen | 3 Segmente |
| 460 - 612 Zeichen | 4 Segmente |
| 613 - 765 Zeichen | 5 Segmente |
| 766 - 918 Zeichen | 6 Segmente |
| 919 - 1071 Zeichen | 7 Segmente |
| 1072 - 1224 Zeichen | 8 Segmente |
| 1225 - 1377 Zeichen | 9 Segmente |
| 1378 - 1530 Zeichen | 10 Segmente |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab UCS-2 encoding %}
| Anzahl der Zeichen | Wie viele Segmente? |
| -------------------- | ----------------- |
| 0 - 70 Zeichen | 1 Segment |
| 71 - 134 Zeichen | 2 Segmente |
| 135 - 201 Zeichen | 3 Segmente |
| 202 - 268 Zeichen | 4 Segmente |
| 269 - 335 Zeichen | 5 Segmente |
| 336 - 402 Zeichen | 6 Segmente |
| 403 - 469 Zeichen | 7 Segmente |
| 470 - 536 Zeichen | 8 Segmente |
| 537 - 603 Zeichen | 9 Segmente |
| 604 - 670 Zeichen | 10 Segmente |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

### Was Sie bei der Erstellung Ihrer Texte beachten sollten

- **Zeichenlimit pro Segment**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) hat ein Limit von 160 Zeichen für ein einzelnes SMS-Segment. Für Nachrichten mit mehr als 160 Zeichen werden alle Nachrichten mit einem Limit von 153 Zeichen segmentiert.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) hat ein Limit von 70 Zeichen pro Nachrichtensegment. Für Nachrichten mit mehr als 70 Zeichen werden alle Nachrichten mit einem Limit von 67 Zeichen segmentiert.<br><br>
- **Segmentlimit pro Nachricht**
    - Die Anzahl der Segmente, die Sie senden können, ist aufgrund der Beschränkungen des Mediums begrenzt. Es können nicht mehr als **10 Nachrichtensegmente** in einer einzigen Braze SMS-Nachricht versendet werden.
    - Diese 10 Segmente sind auf 1530 Zeichen (GSM-7-Kodierung) oder 670 Zeichen (UCS-2-Kodierung) begrenzt.<br><br>
- **Kompatibel mit Liquid Templating, Connected Content, Emojis und Links**
    - Bei Liquid-Templates und Connected-Content besteht die Gefahr, dass Ihre Nachricht das Zeichenlimit für Ihren Kodierungstyp überschreitet. Möglicherweise können Sie den [Filter „Wörter kürzen“](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) verwenden, um die Anzahl der Wörter zu begrenzen, die Ihr Liquid in die Nachricht einfügen könnte.
    - Für Emojis gibt es keine einheitliche Zeichenzahl für alle Emojis. Testen Sie also, ob Ihre Nachrichten korrekt segmentiert und angezeigt werden.
    - Links können viele Zeichen verwenden, was zu mehr Nachrichtensegmenten als beabsichtigt führt. Die Verwendung von Linkverkürzern ist zwar möglich, aber sie werden am besten mit kurzen Codes verwendet. Besuchen Sie unsere [SMS FAQ]({{site.baseurl}}/sms_faq/) für weitere Informationen.<br><br>
- **Testen**
    - Testen Sie Ihre SMS-Nachrichten immer vor dem Start, insbesondere bei der Verwendung von Liquid und Connected Content, da das Überschreiten von Nachrichten- oder Kopierlimits zu zusätzlichen Gebühren führen kann. Beachten Sie, dass Testnachrichten auf Ihr Nachrichtenlimit angerechnet werden.

### SMS-Segmentrechner {#segment-calculator}
---

{% include alerts/tip_alerts.md alert='SMS segment calculator' %}

## Abrechnung von RCS Nachrichten

RCS-Nachrichten werden auf der Grundlage ihres Inhalts und des Landes, in dem die Nachricht zugestellt wird, abgerechnet. Um die Kosten genau einschätzen zu können, müssen Sie die verschiedenen Arten von Nachrichten verstehen und wissen, wie sie abgerechnet werden.

### RCS-Abrechnungsarten

Unsere Plattform unterstützt zwei primäre Abrechnungsmodelle: ein globales Modell und ein Modell für die Vereinigten Staaten.

#### Globales Modell (Nicht-US-Märkte)

Messaging wird pro Nachricht abgerechnet und entweder als Basic oder Single eingestuft.

{% tabs local %}
{% tab Basic %}

Einfache RCS-Nachrichten sind reine Textnachrichten mit bis zu 160 Zeichen und werden als eine einzige Nachricht abgerechnet.

{% alert note %}
Wenn Sie Buttons oder andere Rich-Elemente hinzufügen, ändert sich der Nachrichtentyp in eine einzelne RCS-Nachricht.
{% endalert %}

{% endtab %}
{% tab Single %}

Einzelne RCS-Nachrichten sind Nachrichten, die mehr als 160 Zeichen umfassen ODER Rich-Elemente wie Buttons oder Medien enthalten. Diese werden unabhängig von der Länge der Nachricht als eine einzige Nachricht abgerechnet.

{% alert note %}
Das Versenden einer Textnachricht und einer separaten Mediendatei wird immer noch als zwei verschiedene Nachrichten abgerechnet.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Modell Vereinigte Staaten

Nachrichten werden entweder als Rich oder Rich Media kategorisiert.

{% tabs local %}
{% tab Rich messages %}

Rich Messages sind reine Textnachrichten mit oder ohne Buttons. Sie werden pro Segment abgerechnet, wobei jedes Segment auf 160 UTF-8 Bytes begrenzt ist, d.h. **die Anzahl der Zeichen pro Segment ist nicht festgelegt**. Eine Nachricht mit nur 160 einfachen englischen Zeichen ist ein Segment, aber eine Nachricht mit längerem Text und Emojis könnte aus mehreren Segmenten bestehen.

{% endtab %}
{% tab Rich media messages %}

Rich Media Nachrichten enthalten eine Mediendatei (Bild, Video) oder eine Rich Card und werden als einzelne Nachricht abgerechnet.

{% endtab %}
{% endtabs %}

### Nachrichten-Editor und Dashboard für die Verwendung von Nachrichten

Während Sie Ihre Nachricht erstellen, zeigt der Nachrichten-Editor die Art der Abrechnung in Realtime durch ein Etikett an (Basic RCS, Single RCS, Rich oder Rich Media), so dass Sie die Kosten vor dem Versand verfolgen können.

Ihr [Dashboard für die Nutzung von Nachrichten]({{site.baseurl}}/message_usage_dashboard/) spiegelt diese Abrechnungsarten wider und gibt die Anzahl der Segmente an, die für US-Nachrichten verwendet werden. So erhalten Sie einen transparenten Überblick über den Verbrauch Ihres Nachrichten-Guthabens.
