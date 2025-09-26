---
nav_title: Calculadora de Faturamento
article_title: Calculadoras de Faturamento SMS e RCS
page_order: 5
description: "Este artigo de referência cobre o que é um segmento de SMS, como eles são contados para faturamento, bem como coisas a ter em mente ao criar cópias de mensagens SMS e RCS."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# calculadoras de faturamento SMS e RCS

> Na Braze, mensagens SMS são cobradas por segmento de mensagem, enquanto mensagens RCS são cobradas por mensagem. Entender o que define um segmento de SMS e os diferentes tipos de faturamento RCS informará sua compreensão de como você será cobrado e ajudará a evitar cobranças acidentais.

## Cópia de mensagem SMS e calculadora de segmentos

Mensagens SMS são cobradas por segmento de mensagem. Entender como as mensagens SMS são divididas é fundamental para entender seu faturamento.

### O que é um segmento de SMS?

O Serviço de Mensagens Curtas (SMS) é um protocolo de comunicação padronizado que permite que dispositivos enviem e recebam mensagens de texto breves. Foi projetado para "se encaixar entre" outros protocolos de sinalização, razão pela qual o comprimento da mensagem SMS é limitado a 160 caracteres de 7 bits, como 1120 bits, ou 140 bytes. Os segmentos de mensagens SMS são os lotes de caracteres que as operadoras de telefonia usam para medir mensagens de texto. As mensagens são cobradas por segmento de mensagem, então os clientes que utilizam SMS se beneficiam muito de entender as nuances de como as mensagens serão divididas. 

À medida que você cria uma campanha de SMS ou canva usando o Braze, as mensagens que você cria no criador são representativas do que seus usuários podem ver quando a mensagem é entregue em seus telefones, mas **não é indicativo de como sua mensagem será dividida em segmentos e, em última análise, como você será cobrado**. Compreender quantos segmentos serão enviados e estar ciente dos possíveis excessos que podem ocorrer é sua responsabilidade, mas fornecemos alguns recursos para facilitar isso para você. Confira nossa [calculadora de segmento](#segment-calculator).

![]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Divisão de segmento

O limite de caracteres para **um segmento de SMS independente** é de 160 caracteres ([codificação GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)) ou 70 caracteres ([codificação UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)) com base no tipo de codificação. No entanto, a maioria dos telefones e redes suporta concatenação, oferecendo mensagens SMS mais longas de até 1530 caracteres (GSM-7) ou 670 caracteres (UCS-2). Portanto, embora uma mensagem possa incluir vários segmentos, se não exceder esses limites de concatenação, será vista como uma mensagem e relatada como tal.

É importante **notar que, à medida que você ultrapassa o limite de caracteres do seu primeiro segmento, caracteres adicionais farão com que toda a sua mensagem seja dividida e segmentada com base em novos limites de caracteres**:
- **Codificação GSM-7**
    - Mensagens que excederem o limite de 160 caracteres agora serão segmentadas em segmentos de 153 caracteres e enviadas individualmente, depois reconstruídas pelo dispositivo do destinatário. Por exemplo, uma mensagem de 161 caracteres será enviada como duas mensagens, uma com 153 caracteres e a segunda com 8 caracteres. 
- **Codificação UCS-2**
    - Se você incluir caracteres não GSM, como Emojis, script chinês, coreano ou japonês em mensagens SMS, essas mensagens terão que ser enviadas via codificação UCS-2. Mensagens que excederem o limite inicial de 70 caracteres serão concatenadas em segmentos de mensagem de 67 caracteres. Por exemplo, uma mensagem de 71 caracteres será enviada como duas mensagens, uma com 67 caracteres e a segunda com 4 caracteres. 

Independentemente do tipo de codificação, cada mensagem SMS enviada pela Braze tem um limite de até 10 segmentos e é compatível com [Liquid templating]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/), [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), Emojis e links.

{% tabs %}
{% tab Codificação GSM-7 %}
Número de caracteres | Quantos segmentos?
| -------------------- | ----------------- |
| 0 - 160 caracteres | 1 segmento |
| 161 - 306 caracteres | 2 segmentos |
| 307 - 459 caracteres | 3 segmentos |
| 460 - 612 caracteres | 4 segmentos |
| 613 - 765 caracteres | 5 segmentos |
| 766 - 918 caracteres | 6 segmentos |
| 919 - 1071 caracteres | 7 segmentos |
| 1072 - 1224 caracteres | 8 segmentos |
| 1225 - 1377 caracteres | 9 segmentos |
| 1378 - 1530 caracteres | 10 segmentos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Codificação UCS-2 %}
Número de caracteres | Quantos segmentos?
| -------------------- | ----------------- |
| 0 - 70 caracteres | 1 segmento |
| 71 - 134 caracteres | 2 segmentos |
| 135 - 201 caracteres | 3 segmentos |
| 202 - 268 caracteres | 4 segmentos |
| 269 - 335 caracteres | 5 segmentos |
| 336 - 402 caracteres | 6 segmentos |
| 403 - 469 caracteres | 7 segmentos |
| 470 - 536 caracteres | 8 segmentos |
| 537 - 603 caracteres | 9 segmentos |
| 604 - 670 caracteres | 10 segmentos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

### Coisas a ter em mente ao criar seu texto

- **Limite de caracteres por segmento**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) tem um limite de 160 caracteres para um único segmento de SMS. Para mensagens com mais de 160 caracteres, todas as mensagens serão segmentadas com um limite de 153 caracteres.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) tem um limite de 70 caracteres por segmento de mensagem. Para mensagens com mais de 70 caracteres, todas as mensagens serão segmentadas com um limite de 67 caracteres.<br><br>
- **Limite de segmento por mensagem**
    - Há uma quantidade máxima de segmentos que você pode enviar devido às limitações do meio. Não mais do que **10 segmentos** de mensagens podem ser enviados em uma única mensagem SMS da Braze.
    - Esses 10 segmentos serão limitados a 1530 caracteres (codificação GSM-7) ou 670 caracteres (codificação UCS-2).<br><br>
- **Compatível com a modelagem Liquid, Conteúdo Conectado, emojis e links**
    - A modelagem Liquid e o Conteúdo Conectado podem colocar sua mensagem em risco de ultrapassar o limite de caracteres para o seu tipo de codificação. Você pode ser capaz de usar o [filtro de truncar palavras](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) para limitar o número de palavras que seu Liquid poderia trazer para a mensagem.
    - Emojis não têm uma contagem de caracteres padrão em todos os emojis, então certifique-se de testar se suas mensagens estão segmentando e exibindo corretamente.
    - Links podem fazer uso de muitos caracteres, resultando em mais segmentos de mensagem do que o pretendido. Embora o uso de encurtadores de links seja possível, eles são melhores usados com códigos curtos. Visite nosso [FAQ de SMS]({{site.baseurl}}/sms_faq/) para saber mais.<br><br>
- **Testes**
    - Sempre teste suas mensagens SMS antes do lançamento, especialmente ao usar Liquid e Conteúdo Conectado, pois ultrapassar os limites de mensagem ou cópia pode resultar em cobranças adicionais. Nota que mensagens de teste contarão para seus limites de mensagens.

### Calculadora de segmentos de SMS {#segment-calculator}
---

{% alert tip %}

**Teste o comprimento da sua cópia de SMS**

<br>

Se você gostaria de ver quantos segmentos sua mensagem despachará, insira seu texto na calculadora. Nota que isso não processará ou preverá o resultado de Liquid ou Conteúdo Conectado.
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
  <textarea id="sms_message_split" placeholder="Digite seu texto SMS aqui..." style="width:100%;border: 1px solid #33333333;" rows="5"></textarea><br />
  <input type="radio" name="sms_type" value="auto" checked="checked" id="sms_type_auto" /> <label for="sms_type_auto" style="padding-left: 5px;"> Detectar automaticamente</label><label id="auto_encoding" style="padding-left: 5px;"></label><br />
  <input type="radio" name="sms_type" value="gsm" id="sms_type_gsm" /> <label for="sms_type_gsm" style="padding-left: 5px;">Codificação GSM-7</label><br />
  <input type="radio" name="sms_type" value="ucs2" id="sms_type_ucs2" /> <label for="sms_type_ucs2" style="padding-left: 5px;">Codificação UCS-2</label><br />
  <br />
  Comprimento da Mensagem: <span id="sms_length" style="padding-left: 5px;">0</span> caracteres.<br />
  Contagem de Segmentos SMS: <span id="sms_segments" style="padding-left: 5px;">0</span> segmentos. <br />
  Mensagem de saída: <span id="sms_output" style="padding-left: 5px;"></span><br />
  <input type="checkbox" id="segment_section" name="segment_section"> <label style="padding-left: 5px; margin-bottom: 0px;">Segmentos de exibição: </label>
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

function countLength(type, s) {
  const t = (type === "auto") ? smsutil.pickencoding(s) : type;

  se (t === "gsm") {
    retornar s.length \+ (s.match(/^|€|{|}|[|]|~||/g) || []).comprimento;
  } else {
    return s.length;
  }
}

function updateSMSSplit(){
    var sms_text = $('#sms_message_split').val();
    var sms_type = $('#sms_split input[name=sms_type]:checked').val();
    var unicodeinput = smsutil.unicodeCharacters(sms_text);
    var encodedChars = encoder[sms_type](sms_text);
    var smsSegments = segmentador[sms_type](unicodeinput);
    $('#sms_length').html(countLength(sms_type, sms_text));
    $('#sms_segments').html(smsSegments.length);
    const segmentColors = (i) => `segment_color_${i > 3 ? i%3 : i}`;
    const segmentsHtml = smsSegments.map((segment,segment_index) => segment.bytes.map((byte, i) => `<div id='sms_segments_data_${segment_index}-${i}' class='segment ${segmentColors(segment_index)}'>${byte.map(b => smsutil.hexEncode(b)).join(" ")}</div>`).join(""));
    const messageOutput = smsSegments.map((segment,segment_index) =>  segment.text.map((ch, i) => `<div id='message_output_data_${segment_index}-${i}' class='message_output_char ${segmentColors(segment_index)}'>${ch !== " " ? ch : "&nbsp;"}</div>`).join(""));
    $('#sms_output').html(messageOutput);
    $('#sms_segments_data').html(segmentsHtml);
    $('#segment_section').click(function() {
if($(this).is(":checked")) {
$("#sms_segments_data").show();
}
      else {
        $("#sms_segments_data").esconder();
      }
      })
        }
      const implementarHover = (hover_id, input_id_prefix, output_id_prefix) => {
    $(hover_id).mouseover(function(e){
var input_id = e.target.id;
var índice = input_id.split(input_id_prefix)[1];
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
  //destacar segmento para saída de mensagem
implementarHover("#sms_segments_data", "sms_segments_data_", "message_output_data_");
//destacar mensagem de saída para segmento
implementarHover("#sms_output", "message_output_data_", "sms_segments_data_");
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

## Calculadora de mensagens RCS

Mensagens RCS são cobradas por mensagem. Entender os tipos de mensagens RCS faturáveis é fundamental para entender seu faturamento.

### Tipos de mensagens RCS faturáveis

Mensagens RCS são cobradas de algumas maneiras diferentes. A Braze atualmente suporta dois tipos de faturamento: RCS Básico e RCS Único. 

- **Mensagens RCS Básicas**: Mensagens que são apenas texto e têm até 160 caracteres de comprimento. 
- **Mensagens RCS Únicas:** Mensagens que são apenas texto e têm mais de 160 caracteres de comprimento OU mensagens com qualquer elemento rico. Elementos ricos incluem imagens e botões (como respostas sugeridas ou ações sugeridas).

O tipo de cobrança correspondente será exibido dentro do criador de mensagem RCS em um rótulo que possui um dos dois valores: **Texto apenas RCS** (RCS Básico) e **RCS** (RCS Único).

Os dados do seu tipo de cobrança RCS serão preenchidos no seu [dashboard de Uso de Mensagens]({{site.baseurl}}/message_usage_dashboard/), que exibe seu consumo de créditos de mensagem especificando sua proporção de crédito e o número de créditos de mensagem usados. 