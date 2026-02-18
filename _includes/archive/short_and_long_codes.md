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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pros and cons

| Pros |
| ---- |
| **Verified trust and branding**<br> Unlike traditional SMS, where your brand appears as a random 5-digit short code or long code, RCS allows for verified sender profiles. These profiles include your brand's logo, name, and a "verified" checkmark. |
| **Rich messaging features**<br> RCS supports carousels, high-resolution videos, and suggested action buttons (such as "Book Now", "Track Package", or "Pay Bill"). Users can complete complex tasks without leaving their messaging app, which can lead to higher conversion rates than a plain text link. |
{: .reset-td-br-1 role="presentation"}

| Cons |
| ---- |
| **Fragmented support**<br> Though Google has pushed RCS heavily for Android, and Apple has recently introduced RCS support for iOS, the implementation can still be uneven across different carriers and regions. If a user's phone or carrier doesn't support RCS, the message usually sends as a plain SMS, consequently losing all the "rich" RCS features. |
| **Platform inconsistencies**<br> RCS user experience varies depending on the recipient's carrier, device model, and what messaging app they use (for example, Google Messages or iMessage). |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Short Codes %}

#### SMS short codes

A short code is a 5-6 digit number that can send and receive SMS to and from mobile phones at faster rates than long codes. Short codes are recommended for high-volume and time-sensitive sending.

Some countries allow you to choose a specific number for an increased fee. These short codes are called vanity short codes. If you're interested in vanity short codes, contact your Braze account representative for details.

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| 5-6 digits | 4-12 week application| 100 messages per second or more | Yes | 2-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pros and cons

| Pros |
| ---- |
| **Speed and scalability**<br> Short codes are specifically designed for high-volume traffic. They can send messages at faster rates than long codes and, because they are pre-vetted directly by the carriers, they have the lowest risk of being flagged by automated spam filters. |
| **Easy memorability for "Call to Action"**<br> For marketing campaigns, (for example, "Text WIN to 55555"), a short code is much easier for users to remember and type than a 10-digit number. This makes short codes the gold standard for radio, TV, and billboard advertisements, where the user only has a few seconds to see or hear the number. |
{: .reset-td-br-1 role="presentation"}

| Cons |
| ---- |
| **Short codes are available in fewer countries**<br> Short codes are not available in all countries. Contact your Braze account team to inquire about countries you plan to send messages in. |
| **Longer application process**<br> Unlike long codes and alphanumeric sender IDs, which can be provisioned within 1-2 weeks at times, a short code can take 4-12 weeks or longer to be provisioned. Every major carrier must manually approve your specific application before the code is active on their network. If you have a marketing launch next week, a short code is not an option. |
| **Higher cost**<br> Short codes tend to be the most expensive sender type because of the setup and yearly lease fees. |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Long Codes %}

#### SMS long codes

A long code is a standard phone number used to send and receive SMS messages. These phone numbers are typically called “long codes” (10-digit long numbers in many countries) when compared with SMS short codes (5-6 digit numbers).

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| 10 digits | 4-6 week application (can be shorter or longer for different countries) | In the United States, long code throughput depends on your 10DLC trust score; in international markets, throughput can vary or increase in some circumstances, but typically starts around 10 message segments per second (MPS). | Yes | 2-way (depending on where you're sending) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

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
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Alphanumeric Sender ID %}

#### SMS alphanumeric sender ID

An alphanumeric sender ID (often called "alpha") is a recognizable string made up of any combination of letters and numbers (often your company name or brand) displayed as the sender ID for one-way text messaging.

They can have up to 11 characters and contain upper (A-Z) and lower (a-z) case letters, spaces, and digits (0-9). They **cannot** contain only numbers.

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| Up to 11 characters | Available immediately if pre-registration is not required. Otherwise, 1-4 weeks in most countries where registration is required. | Varies depending on country | No | 1-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pros and cons

| Pros | Cons |
| ---- | ---- | 
| {::nomarkdown} <ul><li> Improved brand recognition </li><li> In many international markets, local carriers pre-register and vet alphanumeric senders so your messages are less likely to be caught in aggressive carrier spam filters that might otherwise block random long codes </li><li> Available within 1 week if pre-registration is not required </li></ul> {:/} | {::nomarkdown} <ul><li> <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>Two-way messaging</a> is not supported </li><li> Not all countries support this feature. For example, it is supported in the UK but is blocked in the US. </li><li> Some countries have an extensive pre-registration process that requires legal documentation to be submitted and longer lead times. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

For more information on alphanumeric sender IDs, contact your customer success manager. 
{% endtab %}
{% tab SMS toll-free numbers %}

#### SMS-enabled toll-free numbers

Toll-free numbers have distinct three-digit area codes (for example, 800, 888, 877, and 866), allowing users to reach businesses without being charged. Widely used for customer service, they can also handle all types of A2P messaging (application-to-person), including marketing.

##### Details

| Length | Access | Throughput | MMS enabled | 1-way vs. 2-way |
| --- | --- | --- | --- | --- |
| 10 digits	 | 2-4 week application | Starts at 3 MPS (segments per second), can be increased for additional fees | Yes | 2-way |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pros and cons

| Pros |
| ---- |
| **Professional image**<br> Toll-free numbers are widely recognized and trusted in North America for business communication, providing a professional and authoritative touch. |
| **Flexible throughput; no carrier sending limits**<br> Unlike standard long codes, which may set throughput or carrier sending limits depending on the country, toll-free numbers can have throughput increased to help support higher volumes and have no daily carrier sending limits in the US.|
{: .reset-td-br-1 role="presentation"}

| Cons |
| --- |
| **Impersonal and geographic neutrality**<br> Because toll-free numbers lack a local area code, they can feel too "corporate" or anonymous. For a local service business, a toll-free number may perform worse than a standard long code because it lacks the community connection and can sometimes be mistaken for a random telemarketing line. |
| **Extra Layer of STOP Filtering**<br> Toll-Free numbers have a layer of opt-out handling outside of Braze that cannot be removed or customized. When a user texts "STOP" to your toll-free number, the user will be opted-out of further messaging from your number, and will receive a network-generated auto-reply. They will not receive further messages from your toll-free number until they text "START" to be removed from the toll-free number's blocklist. |
{: .reset-td-br-1 role="presentation"}

{% endtab %} 
{% endtabs %}

## Setup

Setup requirements and timelines vary by sender type and the country the sender is being provisioned in.

{% tabs local %}
{% tab RCS-verified sender %}

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

RCS timelines fluctuate depending on country, and as more carriers adopt the channel. Currently, you can expect an RCS sender to be approved by carriers within 3-6 weeks of requesting launch.

{% endtab %}
{% tab SMS short codes %}

### SMS short codes

Short codes are provisioned on a country-by-country basis. Depending on the country the short code application process is notorious for being unpredictable. Braze is here to help you with each step, so if you want a short code, contact your onboarding manager or other Braze representative.

Braze will assist with gathering all materials and information needed to submit an application and configure a new short code. Requirements vary by country but many require at least the following:

| Application material    | Description    | Requirements    |
|----------------------|----------------|-----------------|
| Call-to-Action (Opt-in) | The primary purpose of the disclosures is to confirm the user consents to receive text messages and understands the nature of the program. | {::nomarkdown}<ul><li>Product Description</li><li>Message frequency disclosure</li><li>Complete terms and conditions OR link to complete terms and conditions</li><li>Privacy policy OR link to privacy policy</li><li>STOP keyword</li><li>"Message and data rates may apply" disclosure.</li></ul>{:/} |
| Terms and conditions | Comprehensive terms and conditions may be fully presented beneath the call-to-action or accessible through a link near the call-to-action. | {::nomarkdown}<ul><li>Program (brand) name</li><li>Message frequency disclosure</li><li>Product description</li><li>Customer care contact information</li><li>Opt-out information</li><li>"Message and data rates may apply" disclosure.</li></ul>{:/} |
| Message flow | Recurring-messages programs should confirm opt-in with a single text message that explicitly states which program the user enrolled to, and provide clear opt-out instructions.<br><br> Braze processes opt-in, opt-out, and help messages, automatically updating the subscription group state for the user and their associated phone number on all inbound requests.<br><br> Note that these default keywords and responses may also be customized. | {::nomarkdown}<ul><li>Opt-In Confirmation:<ul><li>Program (brand) name OR product description</li><li>Opt-out information</li><li>Customer care contact information</li><li>Message frequency disclosure</li><li>"Message and data rates may apply" disclosure.</li></ul></li><li>HELP response:<ul><li>Program (brand) name OR product description</li><li>Customer care contact information (support email or phone number).</li></ul></li><li>Opt-out (STOP) response:<ul><li>Program (brand) name OR product description</li><li>Confirmation that no further messages will be delivered.</li></ul></li></ul>{:/} |
| Program messages | Program messages are sent in the normal course of the Short Code program, after the user has received an opt-in confirmation. | {::nomarkdown}<ul><li>Opt-out instructions should be provided at regular intervals and at least once per month.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

When all your application materials are ready, Braze submits the application to our providers on your behalf. The application is then reviewed and approved by local operators who may provide additional feedback or request additional information. After all operators give approval, you can immediately configure the short code for use in Braze.

The timeline of short code review and approval varies but typically takes 4—12 weeks depending on the country and nature of the program.

{% alert important %}
If you already have your own short code, contact your customer success manager during the onboarding process to discuss migrating or transferring your short code.
{% endalert %}

{% endtab %}
{% tab SMS long codes and toll-free numbers %}

### SMS long codes (10DLC) and toll-free numbers

In many countries, setting up long codes (also called "10DLCs" or "10-digit long codes") and toll-free numbers for SMS sending has shifted from a "plug and play" process to a regulated vetting system. Carriers want to know exactly who you are and what you plan to say before you send.

During the long code setup process, you can expect to share details about your brand identity and campaign intent.

#### Brand identity

- **Legal entity name:** Must exactly match your tax documents (for example, "Acme Corp LLC" not "Acme").
- **Tax ID:** In the US, this is your Employer Identification Number (EIN). Internationally, you'll need a Value-Added Tax (VAT) number or a local Business Registration Number (BRN).
- **Digital presence:** A live and functional website. Carriers may check this to confirm you aren't a "shell" company.
- **Authorized contact:** Name, email, and phone number of a person responsible for the account.

#### Campaign intent

- **Use case:** State if you're sending 2FA codes, appointment reminders, marketing promos, or other.
- **Sample messages:** Provide 2-5 examples of what you will send.
- **Opt-in proof:** Describe (and often show a screenshot of) how a user signs up. Examples include a web form with a checkbox or a "Text START" keyword on a poster.

Braze will work with you to collect all the necessary details to provision your long code or toll-free number, and then submit the details to our provider for review and approval. After our provider approves the program, we immediately configure the long code or toll-free number in Braze.

The setup timeline depends on the provisioning country. Typically, long codes and toll-free numbers take between 1-4 weeks to be approved.

{% alert important %}
All customers who currently have and/or use US long codes to send to US customers are required to register their long codes. To read more about the specifics of US A2P 10DLC registration and why it’s required, visit our dedicated [10DLC article]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).
{% endalert %}

{% endtab %}
{% tab SMS alphanumeric sender ID %}

### SMS alphanumeric sender ID

Alphanumeric sender IDs are highly regulated because they can be easily spoofed for phishing. While some countries allow anyone to set up and send from a name, in many countries you must first prove you own the brand.

You may be asked for the following details to set up an alphanumeric sender ID.

- **Preferred ID:** A string of up to 11 characters. It contains at least one letter and cannot be a generic word like "BANK" or "INFO".
- **Proof of brand ownership:** Your Trademark Certificate or a Business Registration Document (for example, a Certificate of Incorporation issued within the last 12 months).
- **Letter of authorization:** A signed letter on your company letterhead authorizing Braze and our provider to send messages on your behalf using that specific ID.
- **Sample message templates:** In several regions, you must register the exact "templates" of the messages you intend to send. Deviation in the actual messages can cause delivery failures in those countries.

The timeline to set up an alphanumeric sender ID depends heavily on whether the country allows "Dynamic" (immediate, no registration required) setup or requires "Pre-registration". In countries that require pre-registration, the setup timeline varies, but it typically takes between 1-4 weeks.

{% endtab %}
{% endtabs %}

## Frequently asked questions

For answers to frequently asked questions about SMS and RCS senders, refer to our [SMS frequently asked questions]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/faqs#frequently-asked-questions) page.