{% if include.alert == "Liquid email display name and reply-to address" %}

{% alert tip %}
Sie können [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) in den Feldern **Absender-Anzeigename + Adresse** und **Antwort-Annahme-Adresse** verwenden, um diese auf der Grundlage angepasster Attribute dynamisch anzupassen. So können Sie mit einer einzigen E-Mail-Kampagne oder einem einzigen Canvas-Schritt von verschiedenen Marken, Regionen oder Abteilungen aus versenden.
{% endalert %}

{% endif %}

{% if include.alert == "Reference properties from triggering event" %}

{% alert tip %}
Sie benötigen keinen Kontextschritt, um Eigenschaften des triggernden Ereignisses in [Zielgruppen-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) oder [Decision-Split-Schritten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) zu referenzieren. Sie können die Eigenschaften direkt in den Filtergruppen mit dem Filter **Kontextvariable** referenzieren. Stellen Sie sicher, dass Sie den richtigen Datentyp auswählen.
{% endalert %}

{% endif %}

{% if include.alert == 'catalog data images' %}

{% alert tip %}
Um Bilder für triggernde Artikel im Katalog zu verwenden, muss Ihr Katalog ein Feld namens `image_url` enthalten. Sie können sie dann mit {%raw%}``{{ items[0].image_url }}``{%endraw%} referenzieren.
{% endalert %}

{% endif %}

{% if include.alert == 'Export troubleshooting' %}

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endif %}
{% if include.alert == 'SMS segment calculator' %}

{% alert tip %}

**Testen Sie die Länge Ihres SMS-Textes**

<br>

Wenn Sie wissen möchten, in wie vielen Segmenten Ihre Nachricht gesendet wird, geben Sie Ihren Text in den Rechner ein. Beachten Sie, dass dies die Ausgabe von Liquid oder Connected Content nicht verarbeitet oder vorhersagt.
<!-- Note: This calculator uses fixed DOM IDs and global variables. Include only once per page to avoid conflicts. -->
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
  .encoding_gsm {
    background-color: #28a745;
    color: white;
    padding: 1px 3px;
    margin: 1px;
    border-radius: 2px;
    font-size: 10px;
    display: inline-block;
    white-space: nowrap;
  }
  .encoding_ucs2 {
    background-color: #dc3545;
    color: white;
    padding: 1px 3px;
    margin: 1px;
    border-radius: 2px;
    font-size: 10px;
    display: inline-block;
    white-space: nowrap;
  }
  .encoding_legend {
    margin: 10px 0;
    font-size: 12px;
  }
  .encoding_legend_item {
    display: inline-block;
    margin-right: 15px;
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
  <input type="checkbox" id="encoding_section" name="encoding_section"> <label for="encoding_section" style="padding-left: 5px; margin-bottom: 0px;">Zeichencodierung anzeigen</label>
  <div class="segment_data_hide" id="character_encoding_container">
    <div class="encoding_legend">
      <div class="encoding_legend_item"><span class="encoding_gsm">GSM</span> GSM-7 Zeichen</div>
      <div class="encoding_legend_item"><span class="encoding_ucs2">UCS</span> UCS-2 Zeichen</div>
    </div>
    <span id="character_encoding_label">Zeichenkodierung: </span><span id="character_encoding" style="padding-left: 5px;"></span><br />
  </div>
  <br />
  <input type="checkbox" id="segment_section" name="segment_section"> <label for="segment_section" style="padding-left: 5px; margin-bottom: 0px;">Segmente anzeigen</label>
  <span class="segment_data_hide" id="sms_segments_data"></span>
</form>
<script type="text/javascript">
(function() {
// SMS Segment Calculator - Note: Uses fixed DOM IDs, include only once per page
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

function escapeHtml(text) {
  return text.replace(/[&<>"'/]/g, function (c) {
    Schalter (c) {
      case '&': return '&';
      case '<': return '<';
case '>': return '>';
      case '"': return '"';
      case "'": return ''';
      case '/': return '/';
      Standard: return c;
      }
    });
  }

function getCharacterEncoding(char, type) {
  if (type === "ucs2") return "ucs2";
  if (type === "gsm") return "gsm";

  // Bei automatischer Erkennung prüfen, ob das Zeichen im GSM-7-Set enthalten ist
  const codePoint = char.charCodeAt(0);
  return (codePoint in unicodeToGsm) ? "gsm" : "ucs2";
}

function displayCharacterEncoding(text, type) {
  const Zeichen = smsutil.unicodeCharacters(Text);
  return characters.map((char, index) => {
    const encoding = getCharacterEncoding(char, type);
    const displayChar = char === " " ? " " : escapeHtml(char);
    const titleChar = char === " " ? "Leerzeichen" : char;
    const encodingClass = encoding === "gsm" ? "encoding_gsm": "encoding_ucs2";
    const encodingLabel = encoding === "gsm" ? "GSM" : "UCS";
    return `<span id="character_encoding_data_${index}" class="${encodingClass}" title="${escapeHtml(titleChar)} - ${encoding.toUpperCase()}">${encodingLabel}</span>`;
  }).join("");
}

Funktion updateSMSSplit(){
    var sms_text = $('#sms_message_split').val();
    var sms_type = $('#sms_split input[name=sms_type]:checked').val();
    var unicodeinput = smsutil.unicodeCharacters(sms_text);
    var encodedChars = Encoder[sms_type](sms_text);
    var smsSegments = segmenter[sms_type](unicodeinput);
    $('#sms_length').html(countLength(sms_type, sms_text));
    $('#sms_segments').html(smsSegments.length);

    // Display character encoding
    $('#character_encoding').html(displayCharacterEncoding(sms_text, sms_type));

    const segmentColors = (i) => `segment_color_${i > 3 ? i%3 : i}`;
    const segmentsHtml = smsSegments.map((segment,segment_index) =>  segment.bytes.map((byte, i) => `<div id='sms_segments_data_${segment_index}-${i}' class='segment ${segmentColors(segment_index)}'>${byte.map(b => smsutil.hexEncode(b)).join(" ")}</div>`).join("")).join("");

    // Create message output with both segment and character indexing
    let characterIndex = 0;
    const messageOutput = smsSegments.map((segment,segment_index) =>
      segment.text.map((ch, i) => {
        const safeCh = ch === " " ? "\u00A0" : escapeHtml(ch);
        const result = `<div id='message_output_data_${segment_index}-${i}' data-char-index='${characterIndex}' class='message_output_char ${segmentColors(segment_index)}'>${safeCh}</div>`;
        characterIndex++;
        return result;
      }).join("")
    );
    $('#sms_output').html(messageOutput.join(""));
    $('#sms_segments_data').html(segmentsHtml);
}
// Verbesserte Hover-Funktionalität mit dreifacher Hervorhebung
// Verwendung von Mouseenter/Mouseleave zur Vermeidung der Akkumulation von Handlern
$("#sms_segments_data").on("mouseenter", "[id^='sms_segments_data_']", function(e){
  const segmentIndex = e.target.id.split("sms_segments_data_")[1];
  const messageOutputElement = `#message_output_data_${segmentIndex}`;
  const charIndex = $(messageOutputElement).attr('data-char-index');
  const encodingElement = charIndex !== undefined ? `#character_encoding_data_${charIndex}`: null;

  let elementsToHighlight = `${messageOutputElement}, #${e.target.id}`;
  if(encodingElement) elementsToHighlight += `, ${encodingElement}`;

  $(elementsToHighlight).addClass("hover_segment");
}).on("mouseleave", "[id^='sms_segments_data_']", function(e){
  $(".hover_segment").removeClass("hover_segment");
});

$("#sms_output").on("mouseenter", "[id^='message_output_data_']", function(e){
  const segmentIndex = e.target.id.split("message_output_data_")[1];
  const segmentElement = `#sms_segments_data_${segmentIndex}`;
  const charIndex = $(e.target).attr('data-char-index');
  const encodingElement = charIndex !== undefined ? `#character_encoding_data_${charIndex}`: null;

  let elementsToHighlight = `${segmentElement}, #${e.target.id}`;
  if(encodingElement) elementsToHighlight += `, ${encodingElement}`;

  $(elementsToHighlight).addClass("hover_segment");
}).on("mouseleave", "[id^='message_output_data_']", function(e){
  $(".hover_segment").removeClass("hover_segment");
});

$("#character_encoding").on("mouseenter", "[id^='character_encoding_data_']", function(e){
  const charIndex = e.target.id.split("character_encoding_data_")[1];
  const messageOutputElement = $(`[data-char-index='${charIndex}']`);
  const messageOutputId = messageOutputElement.attr('id');

  if(messageOutputId) {
    const segmentIndex = messageOutputId.split("message_output_data_")[1];
    const segmentElement = `#sms_segments_data_${segmentIndex}`;

    const elementsToHighlight = `#${e.target.id}, #${messageOutputId}, ${segmentElement}`;
    $(elementsToHighlight).addClass("hover_segment");
  }
}).on("mouseleave", "[id^='character_encoding_data_']", function(e){
  $(".hover_segment").removeClass("hover_segment");
});
$('#segment_section').click(function() {
  if($(this).is(":checked")) {
    $("#sms_segments_data").show();
  }
  else {
    $("#sms_segments_data").hide();
  }
});
$('#encoding_section').click(function() {
  if($(this).is(":checked")) {
    $("#character_encoding_container").show();
  }
  else {
    $("#character_encoding_container").hide();
  }
});
$('#sms_message_split').on("input", function(e){
  $('#auto_encoding').html("");
  updateSMSSplit();
});
$('#sms_split input[name=sms_type]').change(function(e){
    $('#auto_encoding').html("");
    updateSMSSplit();
});
})(); // Ende IIFE
</script>

{% endalert %}


{% endif %}
