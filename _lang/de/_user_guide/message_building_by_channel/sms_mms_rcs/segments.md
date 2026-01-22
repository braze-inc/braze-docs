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

{% alert tip %}

**Testen Sie die Länge Ihres SMS-Textes**

<br>

Wenn Sie wissen möchten, in wie vielen Segmenten Ihre Nachricht gesendet wird, geben Sie Ihren Text in den Rechner ein. Beachten Sie, dass dies die Ausgabe von Liquid oder Connected Content nicht verarbeitet oder vorhersagt.
<style>
  .segment_data_hide {
    display: none;
  }
  .segment {
    display: inline-flex;
    padding: 2px;
    font-size: 10px;
    overflow-wrap: break-word;
  }
  .message_output_char {
    display: inline-flex;
  }
  .hover_segment {
    background-color: #27368F ! important;
    color: #fff;
  }
  .segment_color_0 {
    background-color: #3accdd59;
  }
  .segment_color_1 {
    background-color: #ff934954;
  }
  .segment_color_2 {
    background-color: #f7918e47;
  }
  .segment_color_3 {
    background-color: #27368f30;
  }
</style>
<form id="sms_split">
  <textarea id="sms_message_split" placeholder="Geben Sie hier Ihren SMS-Text ein..." style="width:100%;border: 1px solid #33333333;" rows="5"></textarea><br />
  <input type="radio" name="sms_type" value="auto" checked="checked" id="sms_type_auto" /> <label for="sms_type_auto" style="padding-left: 5px;"> Automatisch erkennen</label><label id="auto_encoding" style="padding-left: 5px;"></label><br />
  <input type="radio" name="sms_type" value="gsm" id="sms_type_gsm" /> <label for="sms_type_gsm" style="padding-left: 5px;">GSM-7 Kodierung</label><br />
  <input type="radio" name="sms_type" value="ucs2" id="sms_type_ucs2" /> <label for="sms_type_ucs2" style="padding-left: 5px;">UCS-2 Kodierung</label><br />
  <br />
  Länge der Nachricht: <span id="sms_length" style="padding-left: 5px;">0</span> Zeichen.<br />
  Anzahl der SMS-Segmente: <span id="sms_segments" style="padding-left: 5px;">0</span> Segmente. <br />
  Nachrichtenausgabe: <span id="sms_output" style="padding-left: 5px;"></span><br />
  <input type="checkbox" id="segment_section" name="segment_section"> <label style="padding-left: 5px; margin-bottom: 0px;">Segmente anzeigen: </label>
  <span class="segment_data_hide" id="sms_segments_data"></span>
</form>
<script type="text/javascript">
var unicodeToGsm = {
0x000A: [0x0A],
0x000C: [0x1B, 0x0A],
0x000D: [0x0D],
0x0020: [0x20],
0x0021: [0x21],
0x0022: [0x22],
0x0023: [0x23],
0x0024: [0x02],
0x0025: [0x25],
0x0026: [0x26],
0x0027: [0x27],
0x0028: [0x28],
0x0029: [0x29],
0x002A: [0x2A],
0x002B: [0x2B],
0x002C: [0x2C],
0x002D: [0x2D],
0x002E: [0x2E],
0x002F: [0x2F],
0x0030: [0x30],
0x0031: [0x31],
0x0032: [0x32],
0x0033: [0x33],
0x0034: [0x34],
0x0035: [0x35],
0x0036: [0x36],
0x0037: [0x37],
0x0038: [0x38],
0x0039: [0x39],
0x003A: [0x3A],
0x003B: [0x3B],
0x003C: [0x3C],
0x003D: [0x3D],
0x003E: [0x3E],
0x003F: [0x3F],
0x0040: [0x00],
0x0041: [0x41],
0x0042: [0x42],
0x0043: [0x43],
0x0044: [0x44],
0x0045: [0x45],
0x0046: [0x46],
0x0047: [0x47],
0x0048: [0x48],
0x0049: [0x49],
0x004A: [0x4A],
0x004B: [0x4B],
0x004C: [0x4C],
0x004D: [0x4D],
0x004E: [0x4E],
0x004F: [0x4F],
0x0050: [0x50],
0x0051: [0x51],
0x0052: [0x52],
0x0053: [0x53],
0x0054: [0x54],
0x0055: [0x55],
0x0056: [0x56],
0x0057: [0x57],
0x0058: [0x58],
0x0059: [0x59],
0x005A: [0x5A],
0x005B: [0x1B, 0x3C],
0x005C: [0x1B, 0x2F],
0x005D: [0x1B, 0x3E],
0x005E: [0x1B, 0x14],
0x005F: [0x11],
0x0061: [0x61],
0x0062: [0x62],
0x0063: [0x63],
0x0064: [0x64],
0x0065: [0x65],
0x0066: [0x66],
0x0067: [0x67],
0x0068: [0x68],
0x0069: [0x69],
0x006A: [0x6A],
0x006B: [0x6B],
0x006C: [0x6C],
0x006D: [0x6D],
0x006E: [0x6E],
0x006F: [0x6F],
0x0070: [0x70],
0x0071: [0x71],
0x0072: [0x72],
0x0073: [0x73],
0x0074: [0x74],
0x0075: [0x75],
0x0076: [0x76],
0x0077: [0x77],
0x0078: [0x78],
0x0079: [0x79],
0x007A: [0x7A],
0x007B: [0x1B, 0x28],
0x007C: [0x1B, 0x40],
0x007D: [0x1B, 0x29],
0x007E: [0x1B, 0x3D],
0x00A1: [0x40],
0x00A3: [0x01],
0x00A4: [0x24],
0x00A5: [0x03],
0x00A7: [0x5F],
0x00BF: [0x60],
0x00C4: [0x5B],
0x00C5: [0x0E],
0x00C6: [0x1C],
0x00C9: [0x1F],
0x00D1: [0x5D],
0x00D6: [0x5C],
0x00D8: [0x0B],
0x00DC: [0x5E],
0x00DF: [0x1E],
0x00E0: [0x7F],
0x00E4: [0x7B],
0x00E5: [0x0F],
0x00E6: [0x1D],
0x00C7: [0x09],
0x00E8: [0x04],
0x00E9: [0x05],
0x00EC: [0x07],
0x00F1: [0x7D],
0x00F2: [0x08],
0x00F6: [0x7C],
0x00F8: [0x0C],
0x00F9: [0x06],
0x00FC: [0x7E],
0x0393: [0x13],
0x0394: [0x10],
0x0398: [0x19],
0x039B: [0x14],
0x039E: [0x1A],
0x03A0: [0x16],
0x03A3: [0x18],
0x03A6: [0x12],
0x03A8: [0x17],
0x03A9: [0x15],
0x20AC: [0x1B, 0x65]
}
var smsutil = {
map: function (sub, func) { return [].map.apply(sub, [func]) },
concatMap: function (sub, func) { return [].concat.apply([], smsutil.map(sub, func)); },
id: function (x) { return x; },
isHighSurrogate: function (c) {
var codeUnit = (c.charCodeAt != undefined) ? c.charCodeAt(0) : c;
  return codeUnit >= 0xD800 && codeUnit <= 0xDBFF;
},
numberToHexString: function(number) {
var number = number.toString(16);
if(number.length == 1) { number = "0" + number; }
  return "0x" + number;
},
hexEncode: (codeUnit) => "0x"+codeUnit.toString(16).padStart(4, '0').toUpperCase(),
/**
take a string and return a list of the Unicode characters
*/
unicodeCharacters: function (string) {
var chars = smsutil.map(string, smsutil.id);
var result = [];
while (chars.length > 0) {
    if (smsutil.isHighSurrogate(chars[0])) {
        result.push(chars.shift() + chars.shift())
    } else {
        result.push(chars.shift());
    }
}
return result;
},
/**
take a string and return a list of the Unicode codepoints
*/
unicodeCodePoints: function (string) {
var charCodes = smsutil.map(string, function (x) { return x.charCodeAt(0); });
var result = [];
while (charCodes.length > 0) {
    if (smsutil.isHighSurrogate(charCodes[0])) {
        var high = charCodes.shift();
        var low = charCodes.shift();
        result.push(((high - 0xD800) * 0x400) + (low - 0xDC00) + 0x10000)
    } else {
        result.push(charCodes.shift());
    }
}
return result;
},
/**
Encode a single (unicode) character into UTF16 "bytes"
A single unicode character may be 2 javascript characters
*/
encodeCharUtf16: function (char) {
  if (char.length === 2) {
    return [char.charCodeAt(0), char.charCodeAt(1)];
  } else {
    return [0x00, char.charCodeAt(0)];
  }
},
/**
Encode a single character into GSM0338 "bytes"
*/
encodeCharGsm: function (char) {
return unicodeToGsm[char.charCodeAt(0)];
},
_encodeEachWith: function (doEncode) {
return function (s) {
    return smsutil.map(smsutil.unicodeCharacters(s), doEncode);
}
},
pickencoding: function (s) {
// choose gsm if possible otherwise ucs2
if(smsutil.unicodeCodePoints(s).every(function (x) {return x in unicodeToGsm})) {
  $('#auto_encoding').html("(GSM)");
  return "gsm";
} else {
  $('#auto_encoding').html("(UCS-2)");
  return "ucs2";
}
},
_segmentWith: function (maxSingleSegmentSize, maxConcatSegmentSize, doEncode) {
return function (listOfUnichrs) {
    var bytes = smsutil.map(listOfUnichrs, doEncode);
    if (listOfUnichrs.length == 0) {
        return [];
    } else if ([].concat.apply([], bytes).length <= maxSingleSegmentSize) {
        return [{text:listOfUnichrs, bytes: bytes}];
    }
    var segments = []
    while(listOfUnichrs.length > 0) {
        var segment = {text: [], bytes: []};
        var length = 0;
        function nextChrLen() {
            return bytes[0] === undefined ? length : length + bytes[0].length;
        }
        while(listOfUnichrs.length > 0 && nextChrLen() <= maxConcatSegmentSize) {
            var c = listOfUnichrs.shift()
            var b = bytes.shift();
            segment.text.push(c);
            segment.bytes.push(b);
            if(b != undefined) length += b.length;
        }
        segments.push(segment);
    }
    return segments;
}
}
}
var encoder = {
gsm: smsutil._encodeEachWith(smsutil.encodeCharGsm),
ucs2: smsutil.encodeCharUtf16,
auto: function (s) { return encoder[smsutil.pickencoding(s)](s); },
}
var segmenter = {
gsm: smsutil._segmentWith(160, 153, smsutil.encodeCharGsm),
ucs2: smsutil._segmentWith(140, 134, smsutil.encodeCharUtf16),
auto: function (s) { return segmenter[smsutil.pickencoding(s)](s); },
}

function countLength(typ, s) {
  const t = (type === "auto") ? smsutil.pickencoding(s) : type;

  wenn (t === "gsm") {
    return s.length \+ (s.match(/^|€|{|}|[|]|~|/g) || []).length;
  } else {
    return s.length;
  }
}

Funktion updateSMSSplit(){
    var sms_text = $('#sms_message_split').val();
    var sms_type = $('#sms_split input[name=sms_type]:checked').val();
    var unicodeinput = smsutil.unicodeCharacters(sms_text);
    var encodedChars = Encoder[sms_type](sms_text);
    var smsSegments = segmenter[sms_type](unicodeinput);
    $('#sms_length').html(countLength(sms_type, sms_text));
    $('#sms_segments').html(smsSegments.length);
    const segmentColors = (i) => `segment_color_${i > 3 ? i%3 : i}`;
    const segmentsHtml = smsSegments.map((segment,segment_index) => segment.bytes.map((byte, i) => `<div id='sms_segments_data_${segment_index}-${i}' class='segment ${segmentColors(segment_index)}'>${byte.map(b => smsutil.hexEncode(b)).join(" ")}</div>`).join(""));
    const messageOutput = smsSegments.map((segment,segment_index) => segment.text.map((ch, i) => `<div id='message_output_data_${segment_index}-${i}' class='message_output_char ${segmentColors(segment_index)}'>${ch !== " " ? ch : "&nbsp;"}</div>`).join(""));
    $('#sms_output').html(messageOutput);
    $('#sms_segments_data').html(segmentsHtml);
    $('#segment_section').click(function() {
      if($(this).is(":checked")) {
        $("#sms_segments_data").show();
      }
      else {
        $("#sms_segments_data").hide();
      }
    })
}
const implementHover = (hover_id, input_id_prefix, output_id_prefix) => {
  $(hover_id).mouseover(function(e){
    var input_id = e.target.id;
    var index = input_id.split(input_id_prefix)[1];
    if(!index) {
      return;
    }
    var output_id = `#${output_id_prefix}${index}`;
    $(`${output_id}, #${input_id}`).addClass("hover_segment");
    $(`#${input_id}`).mouseleave(function() {
    $(`${output_id}, #${input_id}`).removeClass("hover_segment");
  });
});
};
//highlight segment to message output
implementHover("#sms_segments_data", "sms_segments_data_", "message_output_data_");
//highlight message output to segment
implementHover("#sms_output", "message_output_data_", "sms_segments_data_");
$('#sms_message_split').on("input", function(e){
  $('#auto_encoding').html("");
  updateSMSSplit();
});
$('#sms_split input[name=sms_type]').change(function(e){
    $('#auto_encoding').html("");
    updateSMSSplit();
});
</script>

{% endalert %}

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