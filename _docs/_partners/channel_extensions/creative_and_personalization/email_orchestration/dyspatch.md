---
nav_title: Dyspatch
alias: /partners/dyspatch
---

# Dyspatch

> Use [Dyspatch][1] and Braze together to simplify your email creation lifecycle and deliver engaging email experiences at scale. 

With Dyspatch, use the intuitive drag and drop email builder to create beautiful, responsive, and engaging emails without needing to write code. Collaborate with your team to create and approve emails within Dyspatch and then upload them to use within Braze, all in a couple of quick steps!

## Pre-Requisites

Requirement   |Origin| Notes
--------------|------|-------------
Braze Account    | [Braze][2] | To upload your email into Braze, the account will need to have permissions allowing you to [Manage the Media Library][3]. |
Dyspatch Account | [Dyspatch][4]| To export the email from Dyspatch the account will need to have a [owner or admin role][5] assigned. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration
Dyspatch supports exporting email templates to Braze using the Liquid download option.

### Step 1: Download Template from Dyspatch
Once your team has approved an email in Dyspatch, click __Download Template__ and select __Liquid__ to download a zip file containing your email.

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_downloading.png %})

### Step 2: Upload Template to Braze
![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_upload.png %}){: style="float:right;max-width:30%;margin-left:15px;"}
Within Braze, select __Templates & Media__ from the sidebar and create a new email template using the __From File__ option. Select and upload the zip file downloaded from Dyspatch. 

### Step 3: Customize the Template
- __Template Name__: We recommend using the same name used for the template in Dyspatch.<br>
- __Sending Info__: Enter your subject line from Dyspatch, you can find it in the metadata text file included in the Dyspatch download.<br>
- __Preheader__: If you have already added a preheader in Dyspatch, you can leave the "Preheader" field empty.<br>

{% alert important %}
Make sure __Inline CSS__ in the __Sending Info__ section is __not selected__. Dyspatch takes care of this by making sure your emails are robust and responsive, making it so CSS inlining with Dyspatch email templates is not needed.
{% endalert %}

## Usage
Once you have finished building and previewing your email template, it can be found in the __Templates & Media__ > __Email Templates__ section of your Braze account. You can now use this email template to start sending engaging email messages to your customers!

[1]: https://www.dyspatch.io
[2]: https://dashboard.braze.com/sign_in
[3]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/
[4]: https://www.dyspatch.io/login/
[5]: https://docs.dyspatch.io/administration/dyspatch_roles/
