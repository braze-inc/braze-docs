---
nav_title: 메시지 복사 및 세그먼트 계산기
article_title: SMS 메시지 복사 및 세그먼트 계산기
page_order: 5
description: "이 참고 문서에서는 SMS 세그먼트의 정의, 청구에 포함되는 방법, SMS 메시지 사본 작성 시 유의해야 할 사항에 대해 설명합니다."
page_type: reference
tool:
  - Testing Tools
channel:
  - SMS

---

# 메시지 복사 및 세그먼트 계산기

> Braze의 SMS 메시지는 메시지 세그먼트당 요금이 부과됩니다. 세그먼트를 정의하는 요소와 이러한 메시지가 어떻게 분할되는지 이해하는 것은 메시지 요금이 청구되는 방식을 이해하는 데 핵심이며, 실수로 인한 초과 요금을 방지하는 데 도움이 됩니다.

## SMS 세그먼트란 무엇인가요?

SMS(단문 메시지 서비스)는 기기 간에 간단한 문자 메시징을 주고받을 수 있는 표준화된 통신 프로토콜입니다. 다른 시그널링 프로토콜 사이에 '끼워 맞추기' 위해 설계되었기 때문에 SMS 메시지 길이가 7비트 160자(1120비트 또는 140바이트)로 제한되어 있습니다. SMS 메시지 세그먼트는 휴대폰 사업자가 문자 메시지를 측정하는 데 사용하는 문자 일괄 처리입니다. 메시지는 메시지 세그먼트별로 요금이 부과되므로 SMS를 활용하는 고객은 메시지 분할 방식에 대한 뉘앙스를 이해하면 큰 이점을 얻을 수 있습니다. 

Braze를 사용하여 SMS 캠페인 또는 캔버스를 만들 때 작성기에서 작성하는 메시지는 메시지가 휴대폰으로 전달될 때 사용자에게 표시되는 내용을 **나타내지만, 메시지가 세그먼트로 분할되는 방식과 궁극적으로 요금이 부과되는 방식은 나타내지 않습니다**. 전송할 세그먼트 수를 파악하고 초과량이 발생할 수 있음을 인지하는 것은 사용자의 책임이지만, 이를 보다 쉽게 처리할 수 있도록 몇 가지 리소스를 제공합니다. 사내 [세그먼트 계산기](#segment-calculator)를 확인하세요.

![]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

### 세그먼트 분석

**독립형 SMS 세그먼트**의 문자 수 제한은 인코딩 유형에 따라 160자([GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) 인코딩) 또는 70자([UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) 인코딩)입니다. 그러나 대부분의 휴대폰과 네트워크는 연결 기능을 지원하여 최대 1530자(GSM-7) 또는 670자(UCS-2)의 긴 형식의 SMS 메시지를 제공합니다. 따라서 메시지에 여러 개의 세그먼트가 포함되어 있어도 이러한 연결 제한을 초과하지 않으면 하나의 메시지로 간주되어 그대로 보고됩니다.

**첫 번째 세그먼트의 글자 수 제한을 초과하면 추가 글자 수에 따라 전체 메시지가 새로운 글자 수 제한에 따라 분할 및 세그먼트화된다는** 점에 유의하세요:
- **GSM-7 인코딩**
    - 이제 160자 제한을 초과하는 메시지는 153자로 분할되어 개별적으로 전송된 후 수신자의 기기에서 다시 작성됩니다. 예를 들어 161자 메시지는 하나는 153자, 다른 하나는 8자로 구성된 두 개의 메시지로 전송됩니다. 
- **UCS-2 인코딩**
    - SMS 메시지에 이모티콘, 중국어, 한국어, 일본어 등 GSM 이외의 문자를 포함할 경우 해당 메시지는 UCS-2 인코딩을 통해 전송해야 합니다. 초기 세그먼트 제한인 70자를 초과하는 메시지는 전체 메시지가 67자 메시지 세그먼트로 연결됩니다. 예를 들어 71자 메시지는 하나는 67자, 다른 하나는 4자로 구성된 두 개의 메시지로 전송됩니다. 

인코딩 유형에 관계없이 Braze에서 발송하는 각 SMS 메시지는 최대 10개의 세그먼트로 제한되며, [Liquid 템플릿]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/), [커넥티드 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), 이모지 및 링크와 호환됩니다.

{% tabs %}
{% tab GSM-7 인코딩 %}
| 문자 수 | 세그먼트 수는 몇 개인가요? |
| -------------------- | ----------------- |
| 0 - 160자 | 1 세그먼트 | 1 세그먼트
| 161 - 306자 | 2개 세그먼트 | 161 - 306자
| 307 - 459자 | 3개 세그먼트 | 307 - 459자
| 460 - 612자 | 4분 분량 | 4개 세그먼트
| 613 - 765자 | 5개의 세그먼트 |
| 766 - 918자 | 6개의 세그먼트
| 919 - 1071자 | 7개의 세그먼트
| 1072 - 1224자 | 8개의 세그먼트
| 1225 - 1377자 | 9개 세그먼트 | 1225 - 1377자
| 1378 - 1530자 | 10개의 세그먼트 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab UCS-2 인코딩 %}
| 문자 수 | 세그먼트 수는 몇 개인가요? |
| -------------------- | ----------------- |
| 0 - 70자 | 1 세그먼트 | 1 세그먼트
| 71 - 134자 | 2 세그먼트 | 2 글자
| 135 - 201자 | 3분 분량 | 3개 세그먼트
| 202 - 268자 | 4분 분량 | 4개 세그먼트
| 269 - 335자 | 5개의 세그먼트 |
| 336 - 402자 | 6분 분량 | 6개의 세그먼트
| 403 - 469자 | 7개의 세그먼트
| 470 - 536자 | 8개의 세그먼트 |
| 537 - 603자 | 9개 세그먼트 | 537 - 603자
| 604 - 670자 | 10개의 세그먼트 | 10개의 세그먼트
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## 사본을 만들 때 염두에 두어야 할 사항

- **세그먼트당 글자 수 제한**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)은 단일 SMS 세그먼트에 160자 제한이 있습니다. 160자를 초과하는 메시지의 경우 모든 메시지는 153자 제한으로 세그먼트화됩니다.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)는 메시지 세그먼트당 70자 제한이 있습니다. 70자를 초과하는 메시지의 경우 모든 메시지는 67자 제한으로 세그먼트화됩니다.<br><br>
- **메시지당 세그먼트 제한**
    - 매체의 제한으로 인해 전송할 수 있는 세그먼트의 최대 수량이 정해져 있습니다. 하나의 Braze SMS 메시지에는 **10개 이상의 세그먼트** 메시지를 보낼 수 없습니다.
    - 이 10개의 세그먼트는 1530자(GSM-7 인코딩) 또는 670자(UCS-2 인코딩)로 제한됩니다.<br><br>
- **Liquid 템플릿, 연결된 콘텐츠, 이모티콘 및 링크와 호환 가능**
    - Liquid 템플릿 및 연결된 콘텐츠는 메시지가 인코딩 유형에 대한 글자 수 제한을 초과할 위험이 있습니다. [단어 잘라내기 필터](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords)를 사용하여 Liquid가 메시지에 포함할 수 있는 단어의 수를 제한할 수 있습니다.
    - 이모티콘에는 모든 이모티콘에 표준 글자 수가 없으므로 메시지가 제대로 구분되고 표시되는지 테스트해야 합니다.
    - 링크에는 많은 문자가 사용되어 의도한 것보다 더 많은 메시지 세그먼트가 생성될 수 있습니다. 링크 단축기를 사용할 수 있지만 짧은 코드와 함께 사용하는 것이 가장 좋습니다. 자세한 내용은 [SMS FAQ를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/) 참조하세요.<br><br>
- **테스트**
    - 특히 리퀴드 및 커넥티드 콘텐츠를 사용할 때는 메시지 또는 복사 한도를 초과하면 추가 요금이 부과될 수 있으므로 시작하기 전에 항상 SMS 메시지를 테스트하세요. 테스트 메시지는 메시지 한도에 포함된다는 점에 유의하세요.

## SMS 세그먼트 계산기 {#segment-calculator}
---

{% alert tip %}

**SMS 복사본 길이 테스트**

<br>

메시지를 몇 개의 세그먼트에 발송할지 확인하려면 계산기에 사본을 입력하세요. 리퀴드 또는 커넥티드 콘텐츠의 출력을 처리하거나 예측하지 않는다는 점에 유의하세요.
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
  <textarea id="sms_message_split" placeholder="여기에 SMS 사본을 입력하세요..." style="width:100%;border: 1px solid #33333333;" rows="5"></textarea><br />
  <input type="radio" name="sms_type" value="auto" checked="checked" id="sms_type_auto" /> <label for="sms_type_auto" style="padding-left: 5px;"> 자동 감지</label><label id="auto_encoding" style="padding-left: 5px;"></label><br />
  <input type="radio" name="sms_type" value="gsm" id="sms_type_gsm" /> <label for="sms_type_gsm" style="padding-left: 5px;">GSM-7 인코딩</label><br />
  <input type="radio" name="sms_type" value="ucs2" id="sms_type_ucs2" /> <label for="sms_type_ucs2" style="padding-left: 5px;">UCS-2 인코딩</label><br />
  <br />
  메시지 길이: <span id="sms_length" style="padding-left: 5px;">0자</span>.<br />
  SMS 세그먼트 수: <span id="sms_segments" style="padding-left: 5px;">0</span> 세그먼트. <br />
  메시지 출력: <span id="sms_output" style="padding-left: 5px;"></span><br />
  <input type="checkbox" id="segment_section" name="segment_section"> <label style="padding-left: 5px; margin-bottom: 0px;">세그먼트 표시: </label>
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

함수 countLength(type, s) {
  const t = (type === "auto") ? smsutil.pickencoding(s) : type;

  if (t === "GSM") {
    반환 s.length \+ (s.match(/^|€|{|}|[|]|~||/g) || []).length;
  } else {
    return s.length;
  }
}

함수 updateSMSSplit(){
    var sms_text = $('#sms_message_split').val();
    var sms_type = $('#sms_split 입력[이름=sms_type]:checked').val();
    var unicodeinput = smsutil.unicodeCharacters(sms_text);
    var encodedChars = [encodersms_type](sms_text);
    var smsSegments = segmenter[sms_type](unicodeinput);
    $('#sms_length').html(countLength(sms_type, sms_text));
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
  //highlight 세그먼트에서 메시지 출력으로
implementHover("#sms_segments_data", "sms_segments_data_", "message_output_data_");
//highlight message output to segment
implementHover("#sms_output", "message_output_data_", "sms_segments_data_");
$('#sms_message_split').on("input", function(e){
$('#auto_encoding').html("");
updateSMSSplit();
});
  $('#sms_split 입력[name=sms_type]').change(function(e){
  $('#auto_encoding').html("");
updateSMSSplit();
});
    </script>

{% endalert %}

---