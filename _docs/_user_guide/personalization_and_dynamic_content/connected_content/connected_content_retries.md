---
nav_title: Connected Content Retries
article_title: Connected Content Retries
page_order: 3
description: "Because Connected Content relies on receiving data from APIs, there is the possibility that an API is intermittently unavailable while Braze makes the call. This article covers how to go about dealing with connected content retries."

---

# Connected Content retries

Because Connected Content relies on receiving data from APIs, there is the possibility that an API is intermittently unavailable while Braze makes the call. In this case, Braze supports retry logic to re-attempt the request using exponential backoff. To enable retries, add `:retry` in the Connected Content call, as shown below:
{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

If the API call fails and this is enabled, Braze will retry the call while respecting the [rate limit][47] you set for each resend. Braze will move any failed messages to the back of the queue and add additional minutes, if necessary, to the total minutes it would take to send your message.

If a retried attempt succeeds, the message is sent and no further retries are attempted for that message. If the Connected Content call errors out 5 times, the message is aborted similar to if an [abort message tag][1] was triggered.

{% alert note %}
Connected Content `:retry` is not available for In-App Messages.
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[16]: [success@braze.com](mailto:success@braze.com)
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
