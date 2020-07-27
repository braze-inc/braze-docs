---
nav_title: Dyspatch
alias: /partners/dyspatch
---

# Dyspatch

Use [Dyspatch](1) and Braze together simplify your email creation lifecycle and deliver engaging email experiences at scale. 

In Dyspatch, use the drag and drop email builder to create beautiful, responsive, and engaging emails without needing to write code. Collaborate with your team to approve emails and then upload them to Braze with only a couple of quick steps.

# Pre-Requisites

Requirement   |Origin| Notes
--------------|------|-------------
Braze Account    | [Braze](2) | To upload the email into Braze the account will need to have the permission to [Manage Media Library](3). |
Dyspatch Account | [Dyspatch](4)| To export the email from Dyspatch the account will need to have the [role of owner or admin](5). |

## Integration
Dyspatch supports exporting to Braze using the Liquid download option.

## Step 1: Download Template from Dyspatch
Once your team has approved an email in Dyspatch, click "Download Template" and select "Liquid" to download a zip file containing your email.

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_downloading.png %})

## Step 2: Upload Template to Braze
Within Braze, select "Templates & Media" from the sidebar and create a new email template using the "From File" option. Select and upload the zip file downloaded from Dyspatch. 

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_upload.png %})

## Step 3: Customize the Template
For the "Template name" we recommend using the same name used for the template in Dyspatch. In "Sending Info" enter your subject line from Dyspatch, you can find it in the metadata text file included in the Dyspatch download. If you have already added a preheader in Dyspatch, you can leave the "Preheader" empty.

{% alert important %}
Make sure "Inline CSS" in the "Sending Info" is not selected. Dyspatch takes care of this so your email is robust and responsive already and doesn’t need CSS inlining within Braze.
{% endalert %}

# Usage
Once you have finished building and previewed the email template, you can find it in the “Templates & Media” > “Email Templates” section of your Braze account. You can now use the email template to start sending engaging email messages to your customers.

[1]: https://www.dyspatch.io
[2]: https://dashboard.braze.com/sign_in
[3]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/
[4]: https://www.dyspatch.io/login/
[5]: https://docs.dyspatch.io/administration/dyspatch_roles/
