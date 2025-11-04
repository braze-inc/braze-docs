---
nav_title: 課金計算機
article_title: SMSおよびRCS課金計算機
page_order: 5
description: "この参考記事では、SMSセグメンテーションとは何か、課金のためにセグメンテーションがどのようにカウントされるのか、またSMSやRCSのメッセージコピーを作成する際に注意すべき点などについて説明する。"
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# SMS および RCS の請求額の計算

> Braze では、SMS メッセージはセグメント単位で請求され、RCS メッセージはメッセージ単位で請求されます。SMSセグメンテーションの定義とRCS課金タイプの違いを理解することで、課金方法を理解し、超過料金を防ぐことができる。

## SMS メッセージコピーとセグメントの計算

SMS メッセージはセグメント単位で請求されます。請求を理解するには、SMS メッセージの分割の仕組みを理解しておくことが重要です。

### SMSセグメントとは何か？

ショートメッセージングサービス (SMS) は、標準化された通信プロトコルであり、デバイスが短いテキストメッセージを送受信できるようにするものです。SMSは、他の信号プロトコルの「中間に収まる」ように設計されており、そのため、SMSメッセージの長さは、1120ビット（140バイト）のような160個の7ビット文字に制限されている。SMSメッセージ・セグメントとは、電話キャリアがテキスト・メッセージを測定するために使用する文字バッチのことである。メッセージはメッセージセグメントごとに課金されるため、SMS を活用するクライアントは、メッセージの分割方法の微妙な差異を理解すると多大なメリットを享受できます。 

Braze を使用して SMS のキャンペーンやキャンバスを作成するときに作成画面で作成したメッセージは、ユーザーの携帯電話にメッセージが配信されたときに表示される代表的なものですが、**メッセージがどのようにセグメントに分割され、最終的にどのように課金されるかを示すものではありません**。送信されるセグメント数を理解し、発生する可能性のある超過料金を認識することはお客様の責任ですが、当社では理解を容易にするためのいくつかのリソースを提供しています。当社独自の[セグメント計算ツール](#segment-calculator)を確認してください。

\![]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### セグメントの内訳

**スタンドアロン SMS セグメント**の文字数制限は、エンコーディングのタイプに基づき、160 文字 ([GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) エンコーディング)、または 70 文字 （[ UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) エンコーディング) です。しかし、ほとんどの携帯電話やネットワークは連結をサポートしており、1530 文字 (GSM-7) または 670 文字 (UCS-2) までの長い形式の SMS メッセージを提供します。そのため、ひとつのメッセージが複数のセグメントを含んでいても、連結の制限を超えなければ、ひとつのメッセージとみなされ、そのように報告される。

重要なのは、**最初のセグメントの文字数制限を過ぎると、追加の文字によってメッセージ全体が分割され、新しい文字数制限に基づいてセグメント化される**ことだ：
- **GSM-7エンコーディング**
    - 160 文字の制限を超えるメッセージは、153 文字のセグメントに分割されて個別に送信され、受信者のデバイスで再構成されます。例えば、161 文字のメッセージは、153 文字と 8 文字の 2 つのメッセージとして送信されます。 
- **UCS-2エンコーディング**
    - SMSメッセージに絵文字、中国語、韓国語、日本語などの非GSM文字を含める場合、それらのメッセージはUCS-2エンコーディングで送信されなければならない。最初のセグメント制限である70文字を超えるメッセージは、メッセージ全体が67文字のメッセージセグメントに連結される。例えば、71 文字のメッセージは、67 文字と 4 文字の 2 つのメッセージとして送信されます。 

エンコーディングの種類に関係なく、Brazeから送信される各SMSメッセージは最大10セグメントまでで、[Liquidテンプレート]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)、絵文字、リンクに対応している。

{% tabs %}
{% tab GSM-7 encoding %}
| 文字数｜セグメント数|
| -------------------- | ----------------- |
| 0 ～ 160 文字 | 1 セグメント
| 161〜306文字｜2セグメント
| 307〜459文字｜3セグメント
| 460文字～612文字｜4セグメント
| 全角613～765文字｜5セグメント｜英語
| 766文字～918文字｜6セグメント
| 919文字〜1071文字｜7セグメント
| 1072 〜 1224 文字｜8 セグメント
| 文字数｜1225～1377文字｜9セグメント
| 1378～1530文字｜10セグメント｜英語
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab UCS-2 encoding %}
| 文字数｜セグメント数|
| -------------------- | ----------------- |
| 0～70文字｜1セグメント
| 71～134文字｜2セグメント
| 135～201文字｜3セグメント
| 202-268文字｜4セグメント
| 269～335文字｜5セグメント｜英語
| 全角336～402文字｜6分割
| 403-469文字｜7セグメント｜英語
| 470～536文字｜8セグメント
| 537～603文字｜9セグメント｜英語
| 全角604～670文字｜10分割
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

### コピーを作成する際に留意すべきこと

- **セグメントごとの文字数制限**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) では、1 つの SMS セグメントに 160 文字の制限があります。160文字を超えるメッセージについては、すべてのメッセージが153文字制限でセグメンテーションされる。
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) には、メッセージセグメントあたり 70 文字の制限があります。70文字を超えるメッセージについては、すべてのメッセージが67文字制限でセグメンテーションされる。<br><br>
- **メッセージあたりのセグメント制限**
    - 媒体の制限上、送信できるセグメント数には上限があります。Braze の 1 件の SMS メッセージにつき、**セグメントが 10 個**を超えるメッセージは送信できません。
    - これらの10セグメントは、1530文字（GSM-7エンコーディング）または670文字（UCS-2エンコーディング）に制限される。<br><br>
- **Liquid テンプレート、コネクテッドコンテンツ、絵文字、リンクに対応**
    - リキッドテンプレートとコネクテッドコンテンツは、あなたのメッセージがエンコードタイプの文字数制限を超える危険性がある。Liquid からメッセージに持ち込まれる単語の数を制限するために、[単語切り詰めフィルター](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords)を使用できます。
    - 絵文字には、すべての絵文字に共通する標準的な文字数がないため、メッセージが正しくセグメント化され、表示されていることを必ずテストすること。
    - リンクは多くの文字を使用するため、意図した以上のメッセージセグメントとなる可能性がある。リンクショートナーの使用は可能だが、ショートコードと併用するのがベストだ。詳しくは[SMS FAQを]({{site.baseurl}}/sms_faq/)ご覧いただきたい。<br><br>
- **テスト**
    - 必ず、送信前に SMS メッセージをテストしてください。特に Liquid やコネクテッドコンテンツを使用する場合が該当します。メッセージやコピーの制限を超えると追加料金が発生する可能性があるためです。テストメッセージは、メッセージの上限にカウントされることに注意。

### SMSセグメント計算機 {#segment-calculator}
---

{% alert tip %}

**SMS コピーの長さのテスト**

<br>

メッセージのセグメント数を確認したい場合は、計算機にコピーを入力する。これは、Liquid のコンテンツやコネクテッドコンテンツの出力を処理したり予測したりしない点に注意してください。
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
  <textarea id="sms_message_split" placeholder="SMS のコピーをここに入力..." style="width:100%;border: 1px solid #33333333;" rows="5"></textarea><br />
  <input type="radio" name="sms_type" value="auto" checked="checked" id="sms_type_auto" /> <label for="sms_type_auto" style="padding-left: 5px;"> 自動検出</label><label id="auto_encoding" style="padding-left: 5px;"></label><br />
  <input type="radio" name="sms_type" value="gsm" id="sms_type_gsm" /> <label for="sms_type_gsm" style="padding-left: 5px;">GSM-7エンコーディング</label><br />
  <input type="radio" name="sms_type" value="ucs2" id="sms_type_ucs2" /> <label for="sms_type_ucs2" style="padding-left: 5px;">UCS-2エンコーディング</label><br />
  <br />
  メッセージの長さ: <span id="sms_length" style="padding-left: 5px;">0</span>文字。<br />
  SMSセグメント数：<span id="sms_segments" style="padding-left: 5px;">0</span>セグメント。<br />
  メッセージの出力： <span id="sms_output" style="padding-left: 5px;"></span><br />
  <input type="checkbox" id="segment_section" name="segment_section"> <label style="padding-left: 5px; margin-bottom: 0px;">セグメントを表示する： </label>
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
  const t = (type === "auto") ?smsutil.pickencoding(s) : type；

  if (t === "gsm") {.
    returns.length \+ (s.match(/^|€|{|}|[|]|~|/g) || []).length；
  } else {
    return s.length;
  }
}

function updateSMSSplit(){
    varsms_text = $('#sms_message_split').val();
    varsms_type = $('#sms_split input[name=sms_type]:checked').val();
    var unicodeinput = 以下のようになる。 smsutil.unicodeCharacters(sms_text);
    var encodedChars = エンコーダー[sms_type](sms_text);
    var smsSegments = セグメンテーション[sms_type](unicodeinput);
    $('#sms_length').html(countLength(sms_type, sms_text));
    $('#sms_segments').html(smsSegments.length);
    const segmentColors = (i) =>`segment_color_${i > 3 ? i%3 : i}` ；
    const segmentsHtml =smsSegments.map((segment,segment_index) =>segment.bytes.map((byte, i) =>`<div id='sms_segments_data_${segment_index}-${i}' class='segment ${segmentColors(segment_index)}'>${byte.map(b => smsutil.hexEncode(b)).join(" ")}</div>`).join(""))；
    const messageOutput =smsSegments.map((segment,segment_index) =>segment.text.map((ch, i) =>`<div id='message_output_data_${segment_index}-${i}' class='message_output_char ${segmentColors(segment_index)}'>${ch !== " " ? ch : "&nbsp;"}</div>`).join(""))；
    $('#sms_output').html(messageOutput);
    $('#sms_segments_data').html(segmentsHtml);
    $('#segment_section').click(function() {
      if($(this).is(":checked")){
        $("#sms_segments_data").show();
      }
      else {
        $("#sms_segments_data").hide();
      }
    })
}
const implementHover =(hover_id, input_id_prefix, output_id_prefix) => {.
  $(hover_id).mouseover(function(e){
    varinput_id =e.target.id ；
    var インデックス = input_id.split(input_id_prefix)[1];
    if(!index) {
      return;
    }
    varoutput_id =`#${output_id_prefix}${index}` ；
    $(`${output_id}, #${input_id}`).addClass("hover_segment");
    $(`#${input_id}`).mouseleave(function() {)
    $(`${output_id}, #${input_id}`).removeClass("hover_segment");
  });
});
};
//メッセージ出力にセグメントをハイライトする
implementHover("#sms_segments_data", "sms_segments_data_", "message_output_data_");
// セグメントに出力されるメッセージを強調表示する
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

## RCSメッセージング

RCSメッセージは、その内容とメッセージが配信された国に基づいて課金される。コストを正確に見積もるには、さまざまなメッセージの種類とその請求方法を理解することが不可欠だ。

### RCSの請求タイプ

当社のプラットフォームは、グローバルモデルと米国モデルの2つの主要な課金モデルをサポートしている。

#### グローバルモデル（米国以外のマーケット）

メッセージングはメッセージごとに課金され、ベーシックまたはシングルに分類される。

{% tabs local %}
{% tab Basic %}

基本RCSメッセージは160文字までのテキストのみのメッセージで、1通のメッセージとして課金される。

{% alert note %}
ボタンやリッチエレメントを追加すると、メッセージタイプはSingle RCSメッセージに変更される。
{% endalert %}

{% endtab %}
{% tab Single %}

シングルRCSメッセージとは、160文字を超えるメッセージ、またはボタンやメディアなどのリッチ要素を含むメッセージのことである。これらはメッセージの長さに関係なく、1つのメッセージとして請求される。

{% alert note %}
テキスト・メッセージと別のメディア・ファイルを送信しても、2つの異なるメッセージとして請求される。
{% endalert %}

{% endtab %}
{% endtabs %}

#### 米国モデル

メッセージングはリッチとリッチメディアのどちらかに分類される。

{% tabs local %}
{% tab Rich messages %}

リッチメッセージとは、ボタンの有無にかかわらず、テキストのみのメッセージのことである。セグメンテーションごとに課金され、**各セグメンテーションは**160UTF-8バイトに制限されている。160文字のプレーンな英語のメッセージは1セグメンテーションだが、長いテキストや絵文字を含むメッセージは複数のセグメンテーションになる可能性がある。

{% endtab %}
{% tab Rich media messages %}

リッチメディアメッセージには、メディアファイル（画像、動画）またはリッチカードが含まれ、1つのメッセージとして課金される。

{% endtab %}
{% endtabs %}

### メッセージ作成画面とメッセージ使用状況ダッシュボード

メッセージ作成画面では、ラベル（ベーシックRCS、シングルRCS、リッチ、リッチメディア）により課金タイプがリアルタイムで表示されるため、送信前にコストを把握することができる。

[メッセージ使用状況ダッシュボードには]({{site.baseurl}}/message_usage_dashboard/)、これらの課金タイプが反映され、米国のメッセージに使用されたセグメンテーション数が表示される。