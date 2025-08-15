---
page_order: 1
nav_title: Terms to know
article_title: SMS Terms to Know
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Terms to Know"
glossary_top_text: "SMS–everyone has it and knows what it is. What they don't know is the nuance. Check out the following terms to learn more about SMS ecosystems, technologies, and processes."
page_type: glossary
description: "This glossary defines various SMS terms you should know."
channel: SMS 

glossaries:
  - name: SMS (Short Message Service)
    description: A messaging channel created in 1980 and one of the oldest texting technologies. It also happens to be one of the most wide-spread and more frequently used, of all texting channels. This channel is a more direct way to reach your users and customers than most other messaging channels, as it utilizes their personal phone number to reach them. As such, SMS has more rules and regulations around it than other messaging channels.
  - name: Short Code
    description: This is a short, memorable 5-6 digit sequence that allows senders to send more messages at more consistent rates than long numbers (one message per second).<br><br>Either a short or a long code is required.
  - name: Long Code
    description: This is the standard, 10-digit phone number (in most countries) that allows senders to send more messages at the rate of one message per second.<br><br>Either a short or a long code is required.
  - name: Encoding
    description: The conversion of anything into a coded form. SMS content can be encoded in either GSM-7 or UCS-2.
  - name: GSM-7 Encoding (Global System for Mobile Communications)
    description: GSM-7 is the most seen encoding standard for most SMS messaging. It uses most of the Greek and English alphabets, as well as some additional characters. You can learn more about GSM-7 encoding and which character sets you can use from <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title="GSM 7-bit default alphabet and extension table">Wikipedia</a>. Languages such as Chinese, Korean, or Japanese must be transferred using the 16-bit UCS-2 character encoding. <br> <br> You can estimate that the character limit per segment for this type of encoding is 128 characters.
  - name: UCS-2 Encoding (Universal Coded Character Set)
    description: UCS-2 encoding is a fallback encoding standard, especially when a message cannot be encoded using GSM-7 or when a language needs more than 128 characters to be rendered. USC-2 is better measured by <a href='https://en.wikipedia.org/wiki/Code_point'>code points</a>, as opposed to "characters". Regardless, you could estimate that the character limit per segment for this type of encoding is 67 characters.
  - name: Subscription Groups for SMS
    description: Subscription groups are a Braze tool that allows you to target specific subscription levels of users or customers. subscription groups for SMS are constructed internally based on your message service and cannot be shared across workspaces.
  - name: Message Segments
    description: A message segment is a grouping of up to a defined number of characters (160 for GSM-7 encoding; 67 for UCS-2 encoding) that will be sent in a single SMS dispatch. If you dispatch an SMS with 161 characters using GSM-7 encoding, you will see that there are two (2) message segments that were sent. Sending multiple message segments may result in additional charges.
  - name: Message Service
    description: A collection of long codes, short codes, and alphanumeric IDs used to send your SMS message with Braze.
  - name: Keyword
    description: "A short word that is sent to a short or long code to interact with a pre-defined SMS program or to request to OPT-OUT of a specific program or all programs on a code. For example, <code>STOP</code>. Keywords should <br> - be alphanumeric <br> - have no spaces <br> - be less than 10 characters. <br> <br> A specific keyword and short code combination may only be used on one active program at a time. If a keyword is entered that is already in use by another program, a validation error will appear. <br> <br> There are two mandatory keyword categories that all SMS content providers must comply with: <code>STOP</code> and <code>HELP</code>."
  - name: Mandatory Keyword HELP
    description: For each program that is created in the SMS Campaign Manager platform, content for this keyword must be provided and has to meet the best practices and carrier compliance per country or region in which the SMS traffic is being sent and received. In most cases, this content should have a brief explanation of the SMS program, and how to OPT-OUT.
  - name: Global STOP Keywords
    description: Variations include <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. These are referred to as <code>Global-Stop-Keywords</code>. If any of these keywords are texted in to a short or long code, it results in the mobile number (the originating mobile phone number) being opted-out of every active SMS program on that code it is associated with.
  - name: Vanity Code
    description: A vanity short code is a 5-6 digit phone number that is specifically selected by a brand. Vanity short codes are branded and easier for consumers to remember.
  - name: Shared Short Code
    description: When using a shared short code, all text messages, no matter what business or organization sends them, arrives on a consumer's mobile device from the same 5-6 phone number. While shared short codes are relatively low cost and immediately available, this means that your business will not have a dedicated short code, and are subject to other businesses following the correct protocol with your shared short code. 
  - name: Alphanumeric Sender ID
    description: Alphanumeric Sender ID allows you to set your company name or brand as the Sender ID using alphanumeric characters when sending one-way messages to supported countries.
  - name: Toll-Free Number
    description: An toll-free telephone number or freephone number is a telephone number that is billed for all arriving calls instead of incurring charges to the originating telephone subscriber. Toll-free numbers in the US and Canada are SMS-enabled, where subscribers are charged for incoming and outgoing texts.<br><br>Toll-Free messaging works best when your use case is person-to-person, such as customer support or sales, with both the sender and the recipient having a conversation via text.
  - name: One-Way Messaging
    description: One-way messaging allows you to communicate with your customers by sending text messages. One-way messaging is useful if you are implementing an alphanumeric sender ID in markets where long and short codes are not available. 
  - name: Two-Way Messaging
    description: Two-way messaging allows you to carry on a conversation by both sending and receiving text messages. 
---
