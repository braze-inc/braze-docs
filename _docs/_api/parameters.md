---
page_order: 2.4
nav_title: Parameters
layout: glossary_page
glossary_top_header: "Parameters"
glossary_top_text: "Use these parameters to define your API requests. Though the parameters you need are listed under endpoints, this should give you more insight into their nuance and other specifications."

description: "This glossary covers in detail the parameters involved in making API requests." 
page_type: glossary
tool: 
  - Docs
platform: 
  - API

glossaries:
  - name: App Group REST API Key
    description: The <code>api_key</code> indicates the app title with which the data in this request is associated and authenticates the requester as someone who is allowed to send messages to the app. It must be included with every request as a HTTP Authorization header. It can be found in the <strong>Developer Console</strong> section of the Braze dashboard.
    field: "api_key"
  - name: App Identifier
    description: If you want to send push to a set of device tokens (instead of users), you need to indicate on behalf of which specific app you are messaging. In that case, you will provide the appropriate App Identifier in a Tokens Object. It can be found in the <strong>Developer Console</strong> section of the Braze dashboard.
    field: "app_id"
  - name: External User ID
    description: A unique identifier for sending a message to specific users. This identifier should be the same as the one you set in the Braze SDK. You can only target users for messaging who have already been identified through the SDK or the User API. A maximum of 50 External User IDs are allowed in a request. <br> <br> For campaign trigger endpoints, if you provide this field, the criteria will be layered with the campaign's segments and only users who are in the list of External User IDs and the campaign's segment will receive the message.
    field: "external_user_ids"
  - name: Segment Identifier
    description: The <code>segment_id</code> indicates the segment to which the message should be sent. A Segment Identifier for each of the segments you have created can be found in the <strong>Developer Console</strong> section of the Braze dashboard. <br> <br> For message endpoints, if you provide both a Segment Identifier and a list of External User IDs in a single messaging request, the criteria will be layered and only users who are in both the list of External User IDs and the provided segment will receive the message.
    field: "segment_id"
  - name: Campaign Identifier
    description: For messaging endpoints, the <code>campaign_id</code> indicates the API Campaign under which the analytics for a message should be tracked. A Campaign Identifier for each of the campaigns you have created can be found in the <strong>Developer Console</strong> section of the Braze dashboard. If you provide a Campaign Identifier in the request body, you must provide a <code>message_variation_id</code> in each of the message objects indicating the represented variant of your campaign. <br> <br> For campaign trigger endpoints, the <code>campaign_id</code> indicates the API ID of the campaign to be triggered. This field is required for all trigger endpoint requests.
    field: "campaign_id"
  - name: Canvas Identifier
    description: For Canvas triggering endpoints, the <code>canvas_id</code> indicates the identifier of the Canvas to be triggered or scheduled. This field is required for all trigger endpoint requests.
    field: "canvas_id"
  - name: Send Identifier
    description: For messaging endpoints, the <code>send_id</code> indicates the send under which the analytics for a message should be tracked. The <code>send_id</code> allows you to pull back analytics for a specific instance of a campaign send via the <code>sends/data_series</code> endpoint. API and API trigger campaigns that are sent as a broadcast will automatically generate a send identifier if a send identifier is not provided. <br> <br> If you want to specify your own <code>send_id</code>, you'd have to first create one via the <code>sends/id/create</code>  endpoint. The <code>send_id</code> must be all ASCII characters and at most 64 characters long.  You can reuse a send identifier across multiple sends of the same campaign if you want to group analytics of those sends together. <br> <br> Please note that <code>send_id</code> tracking is not available for emails sent via Mailjet. <br> <br> Campaign conversions are attributed to the last tracked <code>send_id</code> that the user received from that campaign, unless the last send the user received was untracked.
    field: "send_id"
  - name: Trigger Properties
    description: "When using one of the endpoints for sending a campaign with API Triggered Delivery, you may provide a map of keys and values to customize your message. If you make an API request that contains an object in <code>\"trigger_properties\"</code>, the values in that object can then be referenced in your message template under the <code>api_trigger_properties</code> namespace. <br> <br> For example, a request with <code>\"trigger_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}</code> could add the word \"shoes\" to the message by adding <code>{{api_trigger_properties.${product_name}}}</code>."
    field: "trigger_properties"
  - name: Canvas Entry Properties
    description: "When using one of the endpoints for triggering or scheduling a Canvas via the API, you may provide a map of keys and values to customize messages sent by the first steps of your Canvas, in the <code>\"canvas_entry_properties\"</code> namespace. <br> <br> For example, a request with <code>\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}</code> could add the word \"shoes\" to a message by adding <code>{{canvas_entry_properties.${product_name}}}</code>."
    field: "canvas_entry_properties"
  - name: Broadcast
    description: "When sending a message to a segment or campaign audience using an API endpoint, Braze requires you to explicitly define whether or not your message is a \"broadcast\" to a large group of users by including a <code>broadcast</code> boolean in the API call. That is, if you intend to send an API message to the entire segment that a campaign or Canvas targets, you must include <code>broadcast: true</code> in your API call. <br><br>Broadcast is a required field and the default value set by Braze when a campaign or Canvas is made is <code>broadcast: false</code>. You can't have both <code>broadcast: true</code> and a <code>recipients</code> list specified. If the <code>broadcast</code> flag is set to true and an explicit list of recipients is provided, the API endpoint will return an error. Similarly, including <code>broadcast: false</code> and not providing a recipient list will return an error. 
    
    <br><br>Use caution when setting <code>broadcast: true</code>, as unintentionally setting this flag may cause you to send your campaign or Canvas to a larger than expected audience. The <code>broadcast</code> flag is required to protect against accidental sends to large groups of users."
    field: "broadcast"
    
---
