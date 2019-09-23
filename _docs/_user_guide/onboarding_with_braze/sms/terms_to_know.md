---
page_order: 0
nav_title: Terms to Know
layout: glossary_page
glossary_top_header: "SMS Terms to Know"
glossary_top_text: "SMS - everyone has it and knows what it is. What they don't know is the nuance. Check out the terms below to learn more about SMS ecosystems, technologies, and processes."

glossaries:
  - name: SMS (Short Message Service)
    description: A messaging channel created in 1980 and one of the oldest texting technologies. It also happens to be one of the most wide-spread and more frequently used, of all texting channels. This channel is a more direct way to reach your users and customers than most other messaging channels, as it utilizes their personal phone number to reach them. As such, SMS has more rules and regulations around it than other messaging channels.
  - name: Short Code
    description: Either a short or a long code are required. <br><br> This is a short, memorable 5-6 digit sequences that allows senders to send more messages at more consistent rates than long numbers (1 message per second).
  - name: Long Code
    description: Either a short or a long code are required. <br><br> This is the standard, 10-digit phone number (in most countries) that allows senders to send more messages at the rate of 1 message per second.
  - name: Encoding
    description: The conversion of anything into a coded form. SMS content can be encoded in either GSM-7 or UCS-2.
  - name: GSM-7 Encoding (Global System for Mobile Communications)
    description: GSM-7 is the most seen encoding standard for most SMS messaging. It uses most of the Greek and English alphabets, as well as some additional characters. You can <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38'>learn more about GSM-7 encoding and which character sets you can use here</a>. Languages such as Chinese, Korean or Japanese must be transferred using the 16-bit UCS-2 character encoding.
  - name: UCS-2 Encoding (Universal Coded Character Set)
    description: UCS-2 encoding is a fallback encoding standard, especially when a message cannot be encoded using GSM-7 or when a language needs more than 128 characters to be rendered. USC-2 is better measured by <a href='https://en.wikipedia.org/wiki/Code_point'>"code points"</a>, as opposed to "characters".
  - name: Subscription Groups for SMS
    description: Subscription Groups are a Braze tool that allows you to target specific subscription levels of users or customers. Subscription Groups for SMS are constructed internally based on your message service and cannot be shared across appgroups.
  - name: Message Segments
    description: A message segment is a grouping of up to a defined number of characters (160 for GSM-7 encoding; 67 for UCS-2 encoding) that will be sent in a single SMS dispatch. If you dispatch an SMS with 161 characters using GSM-7 encoding, you will see that there are two (2) message segments that were sent. Sending multiple message segments may result in additional charges.
  - name: Message Service
    description: A collection of long codes, short codes and alpha-numeric ID's used to send your SMS message with Braze.
  - name: Keyword
    description: "A short word that is sent to a short or long code to interact with a pre-defined SMS program or to request to OPT-OUT of a specific program or all programs on a code. For example, `STOP`. Keywords should <br> - be alphanumeric <br> have no spaces <br> be less than 10 (ten) characters. <br> <br> A specific keyword and short code combination may only be used on one active program at a time. If a keyword is entered that is already in use by another program, a validation error will appear. <br> <br> There are two mandatory keyword categories that all SMS content providers must comply with: `STOP` and `HELP`."
  - name: Mandatory Keyword HELP
    description: For each program that is created in the SMS Campaign Manager platform, content for this keyword must be provided and has to meet the best practices and carrier compliance per country or region in which the SMS traffic is being sent and received. In most cases this content should have a brief explanation of the SMS program, and how to OPTED-OUT.
  - name: Global STOP Keywords
    description: Variations include `STOP`, `END`, `QUIT`, `UNSUBSCRIBE`, `CANCEL`, `STOPALL`. These are referred to as `Global-Stop-Keywords`. If any of these keywords are texted in to a short or long code, it results in the mobile number (the originating mobile phone number) being opted-out of every active SMS program on that code it is associated with.
  - name: "<KEYWORD> STOP (Unsubscribe from Specific SMS Program)"
    description: "Keywords can be used to categorize their SMS programs and therefore enable their mobile users to unsubscribe from those specific programs, rather than all of the programs. For example, if a brand used the keyword `SAVINGS` as the keyword to enter their marketing SMS program and the mobile user only wants to OPT-OUT of that specific single program on that code, then they would text in 'SAVINGS STOP'."






---
