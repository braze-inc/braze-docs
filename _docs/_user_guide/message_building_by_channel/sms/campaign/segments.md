---
nav_title: Message Copy and SMS Segment Calculator
page_order: 5
description: "This reference article covers SMS message segments."
page_type: reference
tool:
  - Dashboard
  - Docs
  - Campaigns

platform:
  - iOS
  - Android

channel:
  - SMS
---

# SMS Message Segments

> SMS messages at Braze are charged per message segment. Understanding how message segments work at Braze is key in understanding how you will be billed for messages and will help prevent accidental overages.

## What is an SMS Segment?

SMS message segments are the character batches that phone carriers use to measure text messages. Messages are charged per message segment, so clients leveraging SMS greatly benefit from understanding the nuances of segments.

Segments are typically 160 characters per message ([GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) encoding) or 67 characters per message ([UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) encoding) based on the encoding type. Languages such as Chinese, Korean, or Japanese must be transferred using the 16-bit UCS-2 character encoding. Regardless of the encoding type, each SMS message sent out by braze has a limit of up to 10 segments and is compatible with Liquid templating, Connected Content, Emojis, and links.

SEGMENT IMAGE HERE

### Things to Keep in Mind as you Create your Copy:
- __Character Limit per Segment__
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) has a 160 character limit per message segment.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) has a 67 character limit per message segment.<br><br>
- __Segment Limit per Message__
    - No more than __10 segments__ of messages may be sent in a single Braze SMS message.
    - Those 10 segments will be limited to __1600 characters (GSM-7 encoding) or 670 characters (UCS-2 encoding)__.<br><br>
- __Compatible with Liquid Templating, Connected Content, Emojis, and Links__
    - Liquid templating and Connected Content may put your message at risk of going over the character limit for your encoding type. You may be able to use the [truncate words filter](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) to limit the number of words that your Liquid could bring to the message.
    - Emojis have no standard character count across all emojis, so make sure to test that your messages are segmenting and displaying correctly.
    - Links may make use of many characters, resulting in more message segments than intended. Though the use of link shorteners is possible, they are best used with short codes. Please visit our [SMS FAQs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/) for more information.<br><br>
- __Testing__
    - Always test your SMS messages before launch, especially when using Liquid and Connected Content as going over message or copy limits may result in additional charges. Please note that test messages will count toward your message limits.

{% alert important %}
Please note that the __character limit displayed in the Dashboard is generic for GSM-7 encoding__, and will not correctly display for other encoding types. To ensure you are following the limits set by your encoding type, use our SMS Segment Calculator shown below to make sure your messages are following all encoding and copy limits. 
{% endalert %}

## SMS Segment Calculator
---
{% alert tip %}
__Test Your SMS Copy Length__
<br><br>
If you'd like to see how many segments your message will dispatch, enter your copy below. Please note that this will not process or predict the output of liquid or connected content.

<form id="sms_split">
<textarea id="sms_message_split" placeholder="Type your SMS copy here..." style="width:100%;border: 1px solid #33333333;" rows="5"></textarea><br />
<input type="radio" name="sms_type" value="auto" checked="checked" id="sms_type_auto" /> <label for="sms_type_auto" style="padding-left: 5px;"> Auto Detect</label><br />
<input type="radio" name="sms_type" value="gsm" id="sms_type_gsm" /> <label for="sms_type_gsm" style="padding-left: 5px;">GSM-7 Encoding</label><br />
<input type="radio" name="sms_type" value="ucs2" id="sms_type_ucs2" /> <label for="sms_type_ucs2" style="padding-left: 5px;">USC-2 Encoding</label><br />
<br />
Message Length: <span id="sms_length" style="padding-left: 5px;">0</span> characters.<br />
SMS Segments: <span id="sms_segments" style="padding-left: 5px;">0</span> segments. <br />
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
Encode a single (Unicode) character into UTF16 "bytes"
A single Unicode character may be 2 javascript characters
*/
encodeCharUtf16: function (char) {
return smsutil.concatMap(char, function (c) {
    return [((0xff00 & c.charCodeAt(0)) >> 8), 0x00ff & c.charCodeAt(0)];
});
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
    return "gsm";
} else {
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
ucs2: smsutil._encodeEachWith(smsutil.encodeCharUtf16),
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
}
$('#sms_message_split').keyup(function(e){
    updateSMSSplit();
});
$('#sms_split input[name=sms_type]').change(function(e){
    updateSMSSplit();
});
</script>

{% endalert %}
---
