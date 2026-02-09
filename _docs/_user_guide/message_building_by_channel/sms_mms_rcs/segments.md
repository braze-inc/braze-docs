---
nav_title: Billing calculator
article_title: SMS and RCS Billing Calculators
page_order: 5
description: "This reference article covers what an SMS segment is, how they are counted for billing, as well as things to keep in mind when creating SMS and RCS message copy."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# SMS and RCS billing calculators

> At Braze, SMS messages are charged per message segment, while RCS messages are charged per message. Understanding what defines an SMS segment and the different RCS billing types will inform your understanding of how you will be billed and will help prevent accidental overages.

## SMS message copy and segment calculator

SMS messages are charged per message segment. Understanding how SMS messages are split is key to understanding your billing.

### What is an SMS segment?

The Short Messaging Service (SMS) is a standardized communication protocol that enables devices to send and receive brief text messages. It was designed to "fit in between" other signaling protocols, which is why SMS message length is limited to 160 7-bit characters, such as 1120 bits, or 140 bytes. SMS message segments are the character batches that phone carriers use to measure text messages. Messages are charged per message segment, so clients leveraging SMS greatly benefit from understanding the nuances of how messages will be split.

As you create an SMS campaign or Canvas using Braze, the messages you build in the composer are representative of what your users may see when the message gets delivered to their phone, but **is not indicative of how your message will be split into segments and ultimately how you be charged**. Understanding how many segments will be sent and being aware of the potential overages that could occur is your responsibility, but we provide some resources to make this easier for you. Check out our in-house [segment calculator](#segment-calculator).

![]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Segment breakdown

The character limit for **a stand-alone SMS segment** is 160 characters ([GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) encoding) or 70 characters ([UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) encoding) based on the encoding type. However, most phones and networks support concatenation, offering longer-form SMS messages of up to 1530 characters (GSM-7) or 670 characters (UCS-2). So while a message may include several segments, if it does not exceed these concatenation limits, it will be viewed as one message, and reported as such.

It's important to note that **as you pass the character limit of your first segment, additional characters will cause your entire message to be split and segmented based on new character limits**:
- **GSM-7 encoding**
    - Messages exceeding the 160 character limit will now be segmented into 153 character segments and sent individually, then rebuilt by the recipient's device. For example, a 161 character message will be sent as two messages, one with 153 characters and the second with 8 characters.
- **UCS-2 encoding**
    - If you include non-GSM characters such as Emojis, Chinese, Korean, or Japanese script in SMS messages, those messages have to be sent via UCS-2 encoding. Messages exceeding the initial segment limit of 70 characters will cause the entire message to be concatenated into 67 character message segments. For example, a 71 character message will be sent as two messages, one with 67 characters and the second with 4 characters.

Regardless of the encoding type, each SMS message sent out by Braze has a limit of up to 10 segments and is compatible with [Liquid templating]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/), [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), Emojis, and links.

{% tabs %}
{% tab GSM-7 encoding %}
| Number of characters | How many segments? |
| -------------------- | ----------------- |
| 0 - 160 characters | 1 segment |
| 161 - 306 characters | 2 segments |
| 307 - 459 characters | 3 segments |
| 460 - 612 characters | 4 segments |
| 613 - 765 characters | 5 segments |
| 766 - 918 characters | 6 segments |
| 919 - 1071 characters | 7 segments |
| 1072 - 1224 characters | 8 segments |
| 1225 - 1377 characters | 9 segments |
| 1378 - 1530 characters | 10 segments |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab UCS-2 encoding %}
| Number of characters | How many segments? |
| -------------------- | ----------------- |
| 0 - 70 characters | 1 segment |
| 71 - 134 characters | 2 segments |
| 135 - 201 characters | 3 segments |
| 202 - 268 characters | 4 segments |
| 269 - 335 characters | 5 segments |
| 336 - 402 characters | 6 segments |
| 403 - 469 characters | 7 segments |
| 470 - 536 characters | 8 segments |
| 537 - 603 characters | 9 segments |
| 604 - 670 characters | 10 segments |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

### Things to keep in mind as you create your copy

- **Character limit per segment**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) has a 160 character limit for a single SMS segment. For messages with more than 160 characters, all messages will be segmented with a 153 character limit.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) has a 70 character limit per message segment. For messages with more than 70 characters, all messages will be segmented with a 67 character limit.<br><br>
- **Segment limit per message**
    - There is a maximum amount of segments you can send due to the medium's limitations. No more than **10 segments** of messages may be sent in a single Braze SMS message.
    - Those 10 segments will be limited to 1530 characters (GSM-7 encoding) or 670 characters (UCS-2 encoding).<br><br>
- **Compatible with Liquid templating, Connected Content, emojis, and links**
    - Liquid templating and Connected Content may put your message at risk of going over the character limit for your encoding type. You may be able to use the [truncate words filter](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) to limit the number of words that your Liquid could bring to the message.
    - Emojis have no standard character count across all emojis, so make sure to test that your messages are segmenting and displaying correctly.
    - Links may make use of many characters, resulting in more message segments than intended. Though the use of link shorteners is possible, they are best used with short codes. Visit our [SMS FAQ]({{site.baseurl}}/sms_faq/) for more information.<br><br>
- **Testing**
    - Always test your SMS messages before launch, especially when using Liquid and Connected Content as going over message or copy limits may result in additional charges. Note that test messages will count toward your message limits.

### SMS segment calculator {#segment-calculator}
---

{% alert tip %}

**Test Your SMS Copy Length**

<br>

If you'd like to see how many segments your message will dispatch, enter your copy into the calculator. Note that this will not process or predict the output of Liquid or Connected Content.
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
  <textarea id="sms_message_split" placeholder="Type your SMS copy here..." style="width:100%;border: 1px solid #33333333;" rows="5"></textarea><br />
  <input type="radio" name="sms_type" value="auto" checked="checked" id="sms_type_auto" /> <label for="sms_type_auto" style="padding-left: 5px;"> Auto Detect</label><label id="auto_encoding" style="padding-left: 5px;"></label><br />
  <input type="radio" name="sms_type" value="gsm" id="sms_type_gsm" /> <label for="sms_type_gsm" style="padding-left: 5px;">GSM-7 Encoding</label><br />
  <input type="radio" name="sms_type" value="ucs2" id="sms_type_ucs2" /> <label for="sms_type_ucs2" style="padding-left: 5px;">UCS-2 Encoding</label><br />
  <br />
  Message Length: <span id="sms_length" style="padding-left: 5px;">0</span> characters.<br />
  SMS Segments Count: <span id="sms_segments" style="padding-left: 5px;">0</span> segments. <br />
  Message Output: <span id="sms_output" style="padding-left: 5px;"></span><br />
  <input type="checkbox" id="encoding_section" name="encoding_section"> <label for="encoding_section" style="padding-left: 5px; margin-bottom: 0px;">Display Character Encoding</label>
  <div class="segment_data_hide" id="character_encoding_container">
    <div class="encoding_legend">
      <div class="encoding_legend_item"><span class="encoding_gsm">GSM</span> GSM-7 characters</div>
      <div class="encoding_legend_item"><span class="encoding_ucs2">UCS</span> UCS-2 characters</div>
    </div>
    <span id="character_encoding_label">Character Encoding: </span><span id="character_encoding" style="padding-left: 5px;"></span><br />
  </div>
  <br />
  <input type="checkbox" id="segment_section" name="segment_section"> <label for="segment_section" style="padding-left: 5px; margin-bottom: 0px;">Display Segments</label>
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

  if (t === "gsm") {
    return s.length + (s.match(/\^|€|{|}|\[|\]|~|\|/g) || []).length;
  } else {
    return s.length;
  }
}

function getCharacterEncoding(char, type) {
  if (type === "ucs2") return "ucs2";
  if (type === "gsm") return "gsm";

  // For auto detection, check if character is in GSM-7 set
  const codePoint = char.charCodeAt(0);
  return (codePoint in unicodeToGsm) ? "gsm" : "ucs2";
}

function displayCharacterEncoding(text, type) {
  const characters = smsutil.unicodeCharacters(text);
  return characters.map((char, index) => {
    const encoding = getCharacterEncoding(char, type);
    const displayChar = char === " " ? "&nbsp;" : char;
    const encodingClass = encoding === "gsm" ? "encoding_gsm" : "encoding_ucs2";
    const encodingLabel = encoding === "gsm" ? "GSM" : "UCS";
    return `<span id="character_encoding_data_${index}" class="${encodingClass}" title="${displayChar} - ${encoding.toUpperCase()}">${encodingLabel}</span>`;
  }).join("");
}

function updateSMSSplit(){
    var sms_text = $('#sms_message_split').val();
    var sms_type = $('#sms_split input[name=sms_type]:checked').val();
    var unicodeinput = smsutil.unicodeCharacters(sms_text);
    var encodedChars = encoder[sms_type](sms_text);
    var smsSegments = segmenter[sms_type](unicodeinput);
    $('#sms_length').html(countLength(sms_type, sms_text));
    $('#sms_segments').html(smsSegments.length);

    // Display character encoding
    $('#character_encoding').html(displayCharacterEncoding(sms_text, sms_type));

    const segmentColors = (i) => `segment_color_${i > 3 ? i%3 : i}`;
    const segmentsHtml = smsSegments.map((segment,segment_index) =>  segment.bytes.map((byte, i) => `<div id='sms_segments_data_${segment_index}-${i}' class='segment ${segmentColors(segment_index)}'>${byte.map(b => smsutil.hexEncode(b)).join(" ")}</div>`).join(""));

    // Create message output with both segment and character indexing
    let characterIndex = 0;
    const messageOutput = smsSegments.map((segment,segment_index) =>
      segment.text.map((ch, i) => {
        const result = `<div id='message_output_data_${segment_index}-${i}' data-char-index='${characterIndex}' class='message_output_char ${segmentColors(segment_index)}'>${ch !== " " ? ch : "&nbsp;"}</div>`;
        characterIndex++;
        return result;
      }).join("")
    );
    $('#sms_output').html(messageOutput);
    $('#sms_segments_data').html(segmentsHtml);
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
    })
}
// Enhanced hover functionality with three-way highlighting
$("#sms_segments_data").mouseover(function(e){
  if(e.target.id.startsWith("sms_segments_data_")) {
    const segmentIndex = e.target.id.split("sms_segments_data_")[1];
    const messageOutputElement = `#message_output_data_${segmentIndex}`;
    const charIndex = $(messageOutputElement).attr('data-char-index');
    const encodingElement = charIndex !== undefined ? `#character_encoding_data_${charIndex}` : null;

    let elementsToHighlight = `${messageOutputElement}, #${e.target.id}`;
    if(encodingElement) elementsToHighlight += `, ${encodingElement}`;

    $(elementsToHighlight).addClass("hover_segment");
    $(`#${e.target.id}`).mouseleave(function() {
      $(elementsToHighlight).removeClass("hover_segment");
    });
  }
});

$("#sms_output").mouseover(function(e){
  if(e.target.id.startsWith("message_output_data_")) {
    const segmentIndex = e.target.id.split("message_output_data_")[1];
    const segmentElement = `#sms_segments_data_${segmentIndex}`;
    const charIndex = $(e.target).attr('data-char-index');
    const encodingElement = charIndex !== undefined ? `#character_encoding_data_${charIndex}` : null;

    let elementsToHighlight = `${segmentElement}, #${e.target.id}`;
    if(encodingElement) elementsToHighlight += `, ${encodingElement}`;

    $(elementsToHighlight).addClass("hover_segment");
    $(`#${e.target.id}`).mouseleave(function() {
      $(elementsToHighlight).removeClass("hover_segment");
    });
  }
});

$("#character_encoding").mouseover(function(e){
  if(e.target.id.startsWith("character_encoding_data_")) {
    const charIndex = e.target.id.split("character_encoding_data_")[1];
    const messageOutputElement = $(`[data-char-index='${charIndex}']`);
    const messageOutputId = messageOutputElement.attr('id');

    if(messageOutputId) {
      const segmentIndex = messageOutputId.split("message_output_data_")[1];
      const segmentElement = `#sms_segments_data_${segmentIndex}`;

      const elementsToHighlight = `#${e.target.id}, #${messageOutputId}, ${segmentElement}`;
      $(elementsToHighlight).addClass("hover_segment");
      $(`#${e.target.id}`).mouseleave(function() {
        $(elementsToHighlight).removeClass("hover_segment");
      });
    }
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
</script>

{% endalert %}

## RCS message billing

RCS messages are billed based on their content and the country the message is delivered in. To accurately estimate costs, it's essential to understand the different message types and how they are billed.

### RCS billing types

Our platform supports two primary billing models: a global model and a United States model.

#### Global model (non-US markets)

Messages are billed per message and classified as either Basic or Single.

{% tabs local %}
{% tab Basic %}

Basic RCS messages are text-only messages up to 160 characters and are billed as a single message.

{% alert note %}
Adding buttons or any rich elements will change the message type to a Single RCS message.
{% endalert %}

{% endtab %}
{% tab Single %}

Single RCS messages are messages that are over 160 characters OR include any rich elements like buttons or media. These are billed as a single message, regardless of message length.

{% alert note %}
Sending a text message and a separate media file is still billed as two distinct messages.
{% endalert %}

{% endtab %}
{% endtabs %}

#### United States model

Messages are categorized as either Rich or Rich Media.

{% tabs local %}
{% tab Rich messages %}

Rich messages are text-only messages with or without buttons. They are billed per segment, with each segment limited to 160 UTF-8 bytes, which means **the number of characters per segment is not fixed**. A message with only 160 plain English characters is one segment, but a message with longer text and emojis could be multiple segments.

{% endtab %}
{% tab Rich media messages %}

Rich media messages include a media file (image, video) or a Rich Card and are billed as a single message.

{% endtab %}
{% endtabs %}

### Message composer and Message Usage dashboard

As you create your message, the message composer will display the billing type in real-time through a label (Basic RCS, Single RCS, Rich, or Rich Media), helping you track costs before you send.

Your [Message Usage dashboard]({{site.baseurl}}/message_usage_dashboard/) will reflect these billing types and will provide the number of segments used for US messages, providing a transparent view of your message credit consumption.
