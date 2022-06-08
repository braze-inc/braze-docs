---
nav_title: FAQs
article_title: Email and Link Template FAQs
page_order: 5

page_type: FAQ
description: "This page covers frequently asked questions about email templates and link templates."
tool:
  - Templates
channel: email

---

# Email and link templates FAQs

> This page provides answers to some frequently asked questions about email templates and link templates.

## Email templates

### Can I add a "view this email in a browser" link to my emails?

No, Braze does not offer this functionality. This is because an increasing majority of email is opened on mobile devices and modern email clients, which render images and content without any problems.

**Workaround:** To achieve this same result, you can host the content of your email on an external landing page (such as your website), which can then be linked to from the email campaign you are building using the **Link** tool when editing the email body.

### How do I create a custom unsubscribe link for my email templates?

There is a redirection option for the unsubscribe page.

You could change the unsubscribe link in the custom footer from {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} to a link to your own website with a query parameter that includes the user ID. For example, something like: 
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Next, you could call the [email status]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) endpoint to update the user's subscription status. For more details, see our documentation on [changing email subscription status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

### What happens if I edit an email template that is currently being used in a campaign?

Edits made to an existing template won't be reflected in campaigns that were created using previous versions of that template.

## Link templates

### Can I upload multiple link templates to my email?

Yes, you can insert as many templates as you would like in your email messages. As a best practice, you should test your emails to ensure that the links are not exceeding 2,000 characters since most browsers will shorten or cut the links.

### How do I preview my links with all of the tags applied?

Once you have applied the [Link template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/), you can send yourself a [test email]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/) to view all the links. Additionally, you can open the links from the preview pane in a new tab to view the links. Lastly, you can hover over the links in the preview pane and see them at the bottom of your browser.

### How does link templating work with Liquid?

Link templates are expanded and added to the each URL prior to any Liquid expansion happening. 

As a best practice, if part of your URL is generated using a Liquid snippet, we recommended that the URL base and question mark (?) is hardcoded for link templates to be expanded correctly. Refrain from adding the question mark (?) to your Liquid as this will cause link templates to first add a question mark (?), and then later the Liquid expansion process will add a second question mark (?).