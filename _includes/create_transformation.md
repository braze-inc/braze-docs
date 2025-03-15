In the Braze dashboard, go to **Data Settings** > **Data Transformation**.

Select **Create Transformation** to name your transformation, then choose your editing experience.

![Transformation details with the option to choose "Use a template" or "Start from scratch" for your editing experience.]({% image_buster /assets/img/data_transformation/data_transformation10.png %})

Select **Use a template** to browse through a template library, including Data Transformation use cases. Or, select **Start from scratch** to load a default code template. 

If you're starting from scratch, choose a destination for your transformation. You can still insert a code template from the template library.

{% details More on destinations %}
* **POST: Track users:** Transforms webhooks from a source platform into user profile updates, such as attributes, events, or purchases.
* **PUT: Update multiple catalog items:** Transforms webhooks from a source platform into catalog item updates.
* **DELETE: Delete multiple catalog items:** Transforms webhooks from a source platform into catalog item deletions.
* **PATCH: Edit multiple catalog items:** Transforms webhooks from a source platform into catalog item edits.
* **POST: Send messages immediately via API Only:** Transforms webhooks from a source platform to send immediate messages to designated users.
{% enddetails %}

{% alert note %}
Want to request additional templates or destinations? Consider leaving [product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

After creating your transformation, you'll see the detailed view of the transformation. Here, you can view the most recent webhook received for this transformation under **Webhook details** and a space to write your transformation code under **Transformation code**.

{% if include.location == "typeform" %}

![]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

Capture your **Webhook URL** for use in the next step.

{% endif %}
