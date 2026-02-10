# SMS and RCS senders

> This article provides an overview of the codes and senders available for sending SMS and RCS messages.

## Types of SMS and RCS senders

{% tabs %}
{% tab RCS-Verified Sender %}

#### RCS-verified sender

RCS is a modern messaging system that offers more features than traditional SMS, introducing capabilities like branded sender IDs, rich media, and interactive content, such as scrollable carousels, quick replies, CTA buttons, and more. It’s designed to provide a sleeker and more engaging user experience.  

##### Details

| Visual components | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| - Brand name<br>- logo<br>- optional caption<br> - verified badge | 4—6 weeks for carrier approval | Throughput and delivery rely on the recipient having an active data connection (mobile data or Wi-Fi). RCS doesn’t rely on fixed network-imposed limits like SMS does; RCS messages are sent over data networks rather than the traditional cellular signaling channels used by SMS. | N/A | 2-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

![Example of an RCS message sent from a RCS-verified sender.]()

##### Pros and cons

| Pros |
| ---- |
| **Verified trust and branding**<br> Unlike traditional SMS, where your brand appears as a random 5-digit short code or long code, RCS allows for verified sender profiles. These profiles include your brand's logo, name, and a "verified" checkmark. |
| **Rich messaging features**<br> RCS supports carousels, high-resolution videos, and suggested action buttons (such as "Book Now", "Track Package", or "Pay Bill"). Users can complete complex tasks without leaving their messaging app, which can lead to higher convcersion rates than a plain text link. |
{: .reset-td-br-1}

| Cons |
| ---- |
| **Fragmented Supported**<br> Through Google has pushed RCS heavily for Android, and Apple has recently introduced RCS support for iOS, the implementation can still be uneven across different carriers and regions. If a user's phone or carrier doesn't support RCS, the message usually sends as a plain SMS, consequently losing all the "rich" RCS features. |
| **Higher cost of rich messaging**<br> RCS messages that use a lot of rich messaging capabilities tend to cost more per message than SMS messages. This isn’t surprising given the benefits of rich features, but can be important to note for your marketing budget. |
{: .reset-td-br-1}

{% endtab %}
{% tab SMS Short Codes %}

#### SMS short codes

A short code is a 5-6 digit number that can send and receive SMS to and from mobile phones at faster rates than long codes. Short codes are recommended for high-volume and time-sensitive sending.

Some countries allow you to choose a specific number for an increased fee. These short codes are called vanity short codes. If you're interested in vanity short codes, contact your Braze account representative for details.

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| 5-6 digits | 4-12 week application| 100 messages per second or more | Yes | 2-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

![Example of a message sent from an SMS short code.]()

##### Pros and cons

| Pros |
| ---- |
| **Speed and scalability**<br> Short codes are specifically designed for high-volume traffic. They can send messages at faster rates than long codes and, because they are pre-vetted directly by the carriers, they have the lowest risk of being flagged by automated spam filters. |
| **Easy memorability for "Call to Action"**<br> For marketing campaigns, (for example, "Text WIN to 55555"), a short code is much easier for users to remember and type than a 10-digit number. This makes short codes the gold standard for radio, TV, and billboard advertisements, where the user only has a few seconds to see or hear the number. |
{: .reset-td-br-1}

| Cons |
| ---- |
| **Short codes are available in fewer countries**<br> Short codes are not available in all countries. Contact your Braze account team to inquire about countries you plan to send messages in. |
| **Longer application process**<br> Unlike long codes and alphanumeric sender IDs, which can be provisoned within 1-2 weeks at times, a short code can take 4-12 weeks or longer to be provisioned. Every major carrier must manually approve your specific application before the code is active on their network. If you have a marketing launch next week, a short code is not an option. |
| **Higher cost**<br> Short codes tend to be the most expensive sender type because of the setup and yearly lease fees. |
{: .reset-td-br-1}

{% endtab %}
{% tab SMS Long Codes %}

#### SMS long codes

A long code is a standard phone number used to send and receive SMS messages. These phone numbers are typically called “long codes” (10-digit long numbers in many countries) when compared with SMS short codes (5-6 digit numbers).

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| 10 digits | 4-6 week application (can be shorter or longer for different countries) | In the United States, long code throughput depends on your 10DLC trust score; in international markets, throughput can vary or increase in some circumstances, but typically starts around 10 message segments per second (MPS). | Yes | 2-way (depending on where you're sending) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

![Example of a message sent from an SMS long code.]()

##### Pros and cons

| Pros |
| ---- |
| **Familiarity and trust**<br> Long codes look like personal phone numbers, often including a local area code. For brands, this represents a balance between professional presence and a personal, approachable feel. |
| **Greater availability worldwide**<br>Long codes are available in over 100 major countries worldwide. Contact your customer success manager or [Braze support]({{site.baseurl}}/braze_support/) for a list of available countries.|
{: .reset-td-br-1}

| Cons |
| --- |
| **Slower sending speeds and daily messaging limits**<br> Long codes are not built for "blast" marketing the way short codes are. If you try to send a time-sensitive flash sale to 100,000 people at once from a long code, it could take hours for all the messages to deliver. In the US, carriers like T-Mobile may also impose daily sending limits for 10DLC based on your brand's trust score. |
| **Stricter filtering risk**<br> Because long codes look like personal phone numbers, carriers monitor them closely to prevent "person-to-person" numbers from being used for spam. Even with a registered 10DLC campaign, if your message content is too "spammy" or doesn't follow strict formatting, you have a much higher risk of being blocked by carriers compared to a pre-approved short code. |
{: .reset-td-br-1}

{% endtab %}
{% tab SMS Alphanumeric Sender ID %}

#### SMS alphanumeric sender ID

An alphanumeric sender ID (often called "alpha") is a recognizable string made up of any combination of letters and numbers (often your company name or brand) displayed as the sender ID for one-way text messaging.

They can have up to 11 characters and contain upper (A-Z) and lower (a-z) case letters, spaces, and digits (0-9). They **cannot** contain only numbers.

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| Up to 11 characters | Available immediately if pre-registration is not required. Otherwise, 1-4 weeks in most countries where registration is required. | Varies depending on country | No | 1-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

![Example of a message sent from an SMS alphanumeric sender ID.]()

##### Pros and cons

| Pros | Cons |
| ---- | ---- | 
| {::nomarkdown} <ul><li> Improved brand recognition </li><li> In many international markets, local carriers pre-register and vet alphanumeric senders so your messages are less likely to be caught in aggressive carrier spam filters that might otherwise block random long codes </li><li> Available within 1 week if pre-registration is not required </li></ul> {:/} | {::nomarkdown} <ul><li> <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>Two-way messaging</a> is not supported </li><li> Not all countries support this feature. For example, it is supported in the UK but is blocked in the US. </li><li> Some countries have an extensive pre-registration process that requires legal documentation to be submitted and longer lead times. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2}

For more information on alphanumeric sender IDs, contact your customer success manager. 
{% endtab %}
{% tab SMS Toll-Free Number %}

#### SMS-enabled toll-free number

Toll-free numbers have distinct three-digit area codes (for example, 800, 888, 877, and 866), allowing users to reach businesses without being charged. Widely used for customer service, they can also handle all types of A2P messaging (application-to-person), including marketing.

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| 10 digits	 | 2-4 week application | Starts at 3 MPS (segments per second), can be increased for additional fees | Yes | 2-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

![Example of a message sent from an SMS-enabled toll-free number.]()

##### Pros and cons

| Pros |
| ---- |
| **Professional image**<br> Toll-free numbers are widely recognized and trusted in North America for business communication, providing a professional and authoritative touch. |
| **Flexible throughput; no carrier sending limits**<br> Unlike standard long codes, which may set throughput or carrier sending limits depending on the country, toll-free numbers can have throughput increased to help support higher volumes and have no daily carrier sending limits in the US.|
{: .reset-td-br-1}

| Cons |
| --- |
| **Impersonal ad geographix neutrality**<br> Because toll-free numbers lack a local area code, they can feel too "corporate" or anonymous. For a local service business, a toll-free number may perform worse than a standard long code because it lacks the community connection and can sometimes be mistaken for a random telemarketing line. |
| **Extra Layer of STOP Filtering**<br> Toll-Free numbers have a layer of opt-out handling outside of Braze that cannot be removed or customized. When a user texts "STOP" to your toll-free number, the user will be opted-out of further messaging from your number, and will receive a network-generated auto-reply. They will not receive further messages from your toll-free number until they text "START" to be removed from the toll-free number's blocklist. |
{: .reset-td-br-1}

{% endtab %} 
{% endtabs %}

## Setup

Setup requirements and timelines vary by sender type and the country the sender is being provisioned in.

### RCS-verified sender

RCS-verified senders are provisioned on a country-by-country basis. The verification and setup process focuses on your agent or sender—the digital persona that interacts with users. You'll provide brand assets and verification details.

#### Brand assets

- **Verified name:** The name users see at the top of the message thread. It should be a recognizable trade name, not necessarily your legal company name.
- **Logo:** A high-resolution image that is 224x224px. This is displayed in a circular frame so keep critical elements centered.
- **Banner (hero image):** A background image for your business profile card (similar to a Facebook or LinkedIn cover photo).
- **Brand color:** A hex value for the buttons and UI elements to match your company's styling.

#### Verification details

- **Point of contact (POC):** This is critical. You must provide an email address for a direct employee of the brand (not an agency email). Google or the carrier will email this person to confirm they've authorized Braze to act on your behalf.
- **Website and privacy policy:** A live website and a privacy policy that explains how you handle user data and messaging.
- **Use case description:** A clear explanation of what you are sending (for example, "Order delivery updates and customer support for retail purchases").

RCS timelines fluctuate depending on country, and as more carriers adapt the channel. Currently, you can expect an RCS sender to be approved by carriers within 3-6 weeks of requesting launch.

### Short code







Besides these differences, know that a brand will usually have one short code, but multiple, back-up long codes, depending on how many recipients they plan to send SMS.

{% alert important %}
Wondering what shared short codes are all about? To learn more about why we recommend straying away from shared short codes, visit the topic in our [SMS FAQ]({{site.baseurl}}/sms_faq/). 
{% endalert %}

## SMS sending phone numbers

Short and long codes are the phone number from which you send messages to your users or customers. They can be 5 to 6-digit short codes, or 10-digit long codes. Each type of code offers specific benefits and all factors should be considered before choosing whether you want a short code, what type of short code you might want, in addition to the long code you will already be assigned.

## How do I get an SMS short code?

Going through the short code application process can be a long process. However, it can be a worthwhile one! If you'd like a short code, contact your onboarding manager or other Braze representative and let them know. After you do, they'll apply for you—they'll ask for some basic information that will help you qualify. Then, all there is to do is wait!

### Short code application

While Braze is responsible for actually applying for the short code, there is some information that we need from you. We recommend reviewing these questions before you contact Braze. 

Regulations require that there are responses to all opt-in, opt-out, and help/info keyword responses. You will need to let us know the specific message flows (the responses you want to send to users after they send a [keyword]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/)) that you want for the following situations.

| Flow Needed | Type | Example |
| ----------- | ---- | ------- |
| Opt-In <br><br>Double Opt-In| SMS | `Welcome to our SMS system! Reply "YES" to receive updates from our company. Respond "STOP" to opt-out and "HELP" for more info.` |
| Opt-In | Website | `Hi there, would you like to sign up for SMS? Text "START" to "23456". Or, enter your number below.` |
| Opt-Out | SMS | `Sorry to see you go! If this was a mistake, text back "UNSTOP". Text "HELP" for more information.` |
| Help | N/A | `Our company is a company that does this and that. For more info on the company, let us know here. Or, you can contact support at 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Depending on your situation, you may need to provide more or fewer flows like the ones listed in the preceding table. You'll also have to let us know **three general examples** of messages you plan to send via SMS - feel free to ask your Braze representative for guidance.

You also must inform us, regardless of which number you use, of how many messages per month you plan to send.

{% alert important %}
If you have your own short code, contact your Customer Success Manager during the onboarding process to discuss migrating or transferring your short code. Short codes must be set up by your Customer Success Manager. 
{% endalert %}

## SMS Application-to-Person 10-Digit Long Codes (A2P 10DLC)

A2P 10DLC refers to a system in the United States that allows businesses to send Application-to-Person (A2P) type messaging via a standard 10-digit long code (10DLC) phone number. 10-digit long codes have traditionally been designed for Person-to-Person (P2P) traffic, causing businesses to be constrained by limited throughput and heightened filtering. This service helps alleviate those issues, improving overall message deliverability, allowing brands to send messages at scale including links and calls to action, and helping further protect consumers from unwanted messages. 

All customers who currently have and/or use US long codes to send to US customers are required to register their long codes for 10DLC. This application process takes 4-6 weeks. To read more about the specifics of 10DLC and why it's required, visit our dedicated [10DLC article]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).

## Frequently asked questions

### How does RCS message throughput compare to SMS message throughput?

RCS message throughput is not as strictly defined or carrier-controlled as it is with SMS. Because RCS messages are sent over data networks rather than the traditional cellular signaling channels used by SMS, RCS doesn't rely on fixed network-imposed limits like SMS does. 

### Do RCS-verified senders support high message throughput like a short code?

No. RCS-verified senders don't have the option of a separate high message throughput.

### Can an RCS-verified sender be shared across multiple subscription groups? 

No. Similar to an SMS sender, an RCS-verified sender can only be used with a single subscription group.

### Can an SMS fallback sender be shared across SMS subscription groups?

No. SMS fallback senders can only be used with a single subscription group.


