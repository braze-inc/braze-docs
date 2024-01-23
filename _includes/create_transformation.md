Navigate to the Braze dashboard, and go to **Data Settings** > **Data Transformation**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Transformations** under **Data**.
{% endalert %}

Click **Create Transformation** to name your transformation, then choose a destination.

### More on destinations

* **POST: Track users:** Transforms webhooks from a source platform into user profile updates, such as attributes, events, or purchases.
* **Update catalog item:** Transforms webhooks from a source platform into catalog item updates.
* **DELETE: Delete catalog item:** Transforms webhooks from a source platform into catalog item deletions.
* **EDIT: Edit catalog item:** Transforms webhooks from a source platform into catalog item edits.

{% alert note %}
Want to request additional destinations? Consider leaving [product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

Create and name your new transformation. This will open a detailed view, showing your most recent webhook this transformation has received and a space to write your transformation.

After creating your transformation, you'll see the detailed view of the transformation. Here, you can view the most recent webhook received for this transformation under **Webhook details** and a space to write your transformation code under **Transformation code**.

{% if include.location == "typeform" %}

![]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

Capture your **Webhook URL** for use in the next step.

{% elsif include.location == "default" %}

![]({% image_buster /assets/img/data_transformation/data_transformation10.png %})

{% endif %}
