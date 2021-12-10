---
nav_title: Copie de message et Calculatrice de segment
article_title: Copie de message SMS et Calculatrice de segment
page_order: 5
description: "Cet article de référence couvre ce qu'est un segment SMS, comment ils sont comptabilisés pour la facturation, ainsi que les choses à garder à l'esprit lors de la création de la copie de message SMS."
page_type: Référence
tool:
  - Outils de test
channel:
  - SMS
---

# Segments de SMS et limites de copie

> Les messages SMS à Braze sont facturés par segment de message. Comprendre ce qui définit un segment et comment ces messages seront divisés est essentiel pour comprendre comment vous serez facturé pour les messages et vous aidera à prévenir les dépassements accidentels.

## Qu'est-ce qu'un segment de SMS ?

Les segments de messages SMS sont les caractères utilisés par les opérateurs téléphoniques pour mesurer les messages textuels. Les messages sont facturés par segment de message, de sorte que les clients qui utilisent les SMS profitent grandement de la compréhension des nuances de la façon dont les messages seront partagés.

Lorsque vous créez une campagne SMS ou Canvas en utilisant Braze, les messages que vous construisez dans l'assistant sont représentatifs de ce que vos utilisateurs peuvent voir lorsque le message est transmis à leur téléphone, mais __n'est pas indicatif de la façon dont votre message sera divisé en segments et finalement de la façon dont vous serez facturé__. Il est de votre responsabilité de comprendre combien de segments seront envoyés et d'être au courant des éventuels excédents qui pourraient se produire. mais nous fournissons quelques ressources pour vous faciliter la tâche. Consultez notre [calculatrice de segment](#segment-calculator) en interne ci-dessous.

![Image du segment SMS]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

### Répartition du segment

La limite de caractères pour __un segment SMS autonome__ est de 160 caractères ([GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) encodage) ou 70 caractères ([encodage UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) ) basés sur le type d'encodage. Cependant, la plupart des téléphones et des réseaux supportent la concaténation, offrant des messages SMS de forme plus longue allant jusqu'à 1530 caractères (GSM-7) ou 670 caractères (UCS-2).

Il est important de noter que __lorsque vous passez la limite de caractères de votre premier segment, les caractères additionnels provoqueront la division et la segmentation de votre message entier en fonction des nouvelles limites de caractères__:
- __Encodage GSM-7__
    - Les messages dépassant la limite de 160 caractères seront maintenant segmentés en segments de 153 caractères et envoyés individuellement, puis reconstruits par l'appareil du destinataire. Par exemple, un message de 161 caractères sera envoyé sous la forme de deux messages, l'un avec 153 caractères et l'autre avec 8 caractères.
- __Encodage UCS-2__
    - Si vous incluez dans les SMS des caractères non-GSM tels que les Emojis, les Chinois, les Coréens ou les Japonais, ces messages doivent être envoyés via l'encodage UCS-2. Les messages dépassant la limite du segment initial de 70 caractères provoqueront la concaténation du message entier en segments de messages de 67 caractères. Par exemple, un message de 71 caractères sera envoyé sous la forme de deux messages, l'un avec 67 caractères et l'autre avec 4 caractères.

Indépendamment du type d'encodage, chaque SMS envoyé par Braze a une limite de 10 segments et est compatible avec le [modèle Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/), [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), Emojis, et liens.

{% tabs %}
{% tab GSM-7 Encoding %}
| Nombre de caractères   | Combien de segments ? |
| ---------------------- | --------------------- |
| 0 à 160 caractères     | 1 segment             |
| 161 - 306 caractères   | 2 segments            |
| 307 - 459 caractères   | 3 segments            |
| 460 - 612 caractères   | 4 segments            |
| 613 - 765 caractères   | 5 segments            |
| 766 - 918 caractères   | 6 segments            |
| 919 - 1071 caractères  | 7 segments            |
| 1072 - 1224 caractères | 8 segments            |
| 1225 - 1377 caractères | 9 segments            |
| 1378 - 1530 caractères | 10 segments           |
{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}
{% tab UCS-2 Encoding %}
| Nombre de caractères | Combien de segments ? |
| -------------------- | --------------------- |
| 0 à 70 caractères    | 1 segment             |
| 71 - 134 caractères  | 2 segments            |
| 135 - 201 caractères | 3 segments            |
| 202 - 268 caractères | 4 segments            |
| 269 - 335 caractères | 5 segments            |
| 336 - 402 caractères | 6 segments            |
| 403 - 469 caractères | 7 segments            |
| 470 - 536 caractères | 8 segments            |
| 537 - 603 caractères | 9 segments            |
| 604 - 670 caractères | 10 segments           |
{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}
{% endtabs %}

## Les choses à garder à l'esprit lorsque vous créez votre copie

- __Limite de caractères par segment__
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) a une limite de 160 caractères pour un seul segment SMS. Pour les messages de plus de 160 caractères, tous les messages seront segmentés avec une limite de 153 caractères.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) a une borne de 70 caractères par segment de message. Pour les messages de plus de 70 caractères, tous les messages seront segmentés avec une limite de 67 caractères.<br><br>
- __Limite de segment par message__
    - Pas plus de __10 segments__ de messages ne peuvent être envoyés en un seul message SMS Braze.
    - Ces 10 segments seront limités à 1530 caractères (encodage GSM-7) ou 670 caractères (encodage UCS-2).<br><br>
- __Compatible avec les modèles liquides, Contenus connectés, Emojis, et Liens__
    - Les modèles de liquides et le contenu connecté peuvent mettre votre message à risque de dépasser la limite de caractères de votre type d'encodage. Vous pouvez utiliser le filtre [tronquer les mots](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) pour limiter le nombre de mots que votre Liquid pourrait apporter au message.
    - Les émojis n'ont pas de nombre de caractères standard à travers tous les émojis, donc assurez-vous de vérifier que vos messages sont segmentés et affichés correctement.
    - Les liens peuvent utiliser de nombreux caractères, ce qui peut donner lieu à plus de segments de message que prévu. Bien que l'utilisation de raccourcisseurs de liens soit possible, ils sont mieux utilisés avec des codes courts. Veuillez visiter notre [FAQ SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/) pour plus d'informations.<br><br>
- __Tests en cours__
    - Toujours tester vos messages SMS avant le lancement, surtout lorsque vous utilisez Liquid et le Contenu connecté comme dépassement de message ou de copie des limites peuvent entraîner des frais supplémentaires. Veuillez noter que les messages de test seront pris en compte dans les limites de vos messages.

## Calculatrice de segment SMS {#segment-calculator}
---

{% alert tip %}

__Tester la longueur de votre copie SMS__

<br>

Si vous souhaitez voir combien de segments votre message va envoyer, entrez votre copie ci-dessous. Veuillez noter que cela ne traitera ni ne préviendra la sortie de Liquid ou du Contenu Connecté.
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
  <textarea id="sms_message_split" placeholder="Tapez votre copie SMS ici..." style="width:100%;border: 1px solid #33333333;" rows="5"></textarea><br />
  <input type="radio" name="sms_type" value="Automatique" checked="checked" id="sms_type_auto" /> <label for="sms_type_auto" style="padding-left: 5px;"> Détection automatique</label><label id="auto_encoding" style="padding-left: 5px;"></label><br />
  <input type="radio" name="sms_type" value="gsm" id="sms_type_gsm" /> <label for="sms_type_gsm" style="padding-left: 5px;">Encodage GSM-7</label><br />
  <input type="radio" name="sms_type" value="ucs2" id="sms_type_ucs2" /> <label for="sms_type_ucs2" style="padding-left: 5px;">Encodage USC-2</label><br />
  <br />
  Longueur du message : <span id="sms_length" style="padding-left: 5px;">0</span> caractères.<br />
  nombre de segments SMS : <span id="sms_segments" style="padding-left: 5px;">0</span> segments. <br />
  Sortie de message : <span id="sms_output" style="padding-left: 5px;"></span><br />
  <input type="checkbox" id="segment_section" name="segment_section"> <label style="padding-left: 5px; margin-bottom: 0px;">Affichage Segments : </label>
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
  $('#auto_encoding').html("(USC-2)");
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
function updateSMSSplit(){
    var sms_text = $('#sms_message_split').val();
    var sms_type = $('#sms_split input[name=sms_type]:checked').val();
    var unicodeinput = smsutil.unicodeCharacters(sms_text);
    var encodedChars = encoder[sms_type](sms_text);
    var smsSegments = segmenter[sms_type](unicodeinput);
    $('#sms_length').html(sms_text.length);
    $('#sms_segments').html(smsSegments.length);
    const segmentColors = (i) => `segment_color_${i > 3 ? i%3 : i}`;
    const segmentsHtml = smsSegments.map((segment,segment_index) =>  segment.bytes.map((byte, i) => `<div id='sms_segments_data_${segment_index}-${i}' class='segment ${segmentColors(segment_index)}'>${byte.map(b => smsutil.hexEncode(b)).join(" ")}</div>`).join(""));
    const messageOutput = smsSegments.map((segment,segment_index) =>  segment.text.map((ch, i) => `<div id='message_output_data_${segment_index}-${i}' class='message_output_char ${segmentColors(segment_index)}'>${ch !== " " ? ch : "&nbsp;"}</div>`).join(""));
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

---