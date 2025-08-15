---
nav_title: Automate Zoom registration
article_title: Automate Zoom Registration
page_order: 1
page_type: tutorial
description: "This article describes how to automate Zoom attendee registration in your email, push, and in-app message campaigns."
channel: 
  - email
  - push
  - in-app messages

---

# Automate Zoom registration

> Webinars have become common for Braze customers to host over the past few years. When hosting a Zoom webinar, users must enter their information on a Zoom landing page to sign up. 

A recommended user flow is outlined below:
1. Schedule a webinar in Zoom and generate a `webinarId`.
2. Use Braze to promote Zoom webinars via email, push, and in-app message channels. 
3. Include a call-to-action button in these communications that automatically adds users to the webinar.

This can be accomplished by using the [Zoom APIs](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) to automatically add a user to a webinar through a button click within an email, push, or in-app message. Use the following endpoint, replacing the webinar ID in the API request. 

POST: `/meetings/{webinarId}/registrants`

For more information, refer to the Zoom [Add webinar registrant endpoint](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate).<br><br>

{% tabs %}
{% tab Email %}

Create an email campaign with a call-to-action button within the message body. When a user clicks the button, redirect them to the webinar landing page (with appropriate parameters included in the redirect link). 

Using the parameters in the URL to pass user data, build an API call to fire when the page loads to add the user to the webinar.

![Email message with Liquid templating used to include first name, last name, email address, and city.]({% image_buster /assets/img/zoom/zoom1.png %})

Users are now registered for the webinar with the details that already exist on their Braze profile.

{% endtab %}
{% tab Push %}

1. Create a push campaign<br><br>

	Set on-click behavior for the button to link out to the webinar landing page.<br>

	![Linking out to the webinar when a button gets clicked.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	A simple example of a landing page for users who sign up via button click from a push. Let the user know what they have signed up for and confirm their registration:<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Create a webhook campaign triggered by the in-app message or button click.<br><br>
 	Using existing user data on their Braze profile, sign up the user for the webinar.<br>

	![A action-based campaign that will be sent to users who clicked a button for a specific campaign.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Example webhook call to Zoom endpoint.<br>
	{% raw %}
	```json
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}

3. Users are now registered for the webinar with the details that already exist on their Braze profile.

{% endtab %}
{% tab In-app message %}

1. Create an in-app message campaign<br><br>

	Set on-click behavior for the button to link out to the webinar landing page<br>

	![Linking out to the webinar when a button gets clicked.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	A simple example of a landing page for users who sign up via button click from an in-app message. Let the user know what they have signed up for and confirm their registration:<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Create a webhook campaign triggered by the in-app message or button click.<br><br>
	Using existing user data on their Braze profile, sign up the user for the webinar.<br>

	![An action-based campaign that will be sent to users who clicked a button for a specific campaign.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Example webhook call to Zoom endpoint.<br>
	{% raw %}
	```json
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}
3. Users are now registered for the webinar with the details that already exist on their Braze profile.

{% endtab %}
{% endtabs %}
