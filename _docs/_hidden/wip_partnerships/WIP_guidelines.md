---
permalink: "/partner_docs/"
title: Partner Documentation
nav_title: Partner Docs
hidden: true
page_type: reference
---

# Partnership Documentation

Welcome Braze Partners and thank you for contributing to our customer knowledge base. Creating and adding partner pages to the Braze docs repository can be quick and simple with the right tools and set up.

Partnership Documentation Overview
- [Set up Your Local Environment](#setup_env)
- [Create and Add Content to Your Page](#create_page)
- [Image, Link and Code Snippet Formatting](#image_links)
- [Reviewing and Testing](#testing)
- [Commiting to Github](#committing)
- [Review Process](#review)

{% alert important %}
Note that this Partnership guide is for __new Braze partners that do not have existing documentation__ already hosted on our site. If you are an existing partner updating your documentation, navigate to your partner page located in: `braze-docs` -> `_docs` -> `_partners` and update as you normally would. 
{% endalert %}

## Step 1: Set up Your Local Environment {#setup_env}

To contribute to Braze docs, you must have a Github account with which you can commit changes and edits. 

Follow our instructions here on how to set up your [local environment](https://github.com/Appboy/braze-docs/wiki/Set-Up-Your-Local-Environment)

After setting up your local environment, make sure to sign our [CLA](https://www.braze.com/docs/cla) (Contribution License Agreement), _this step is required_.

## Step 2: Create and Add Content to Your Page {#create_page}

To create your partner page, open the braze-docs repository and navigate to the `wip_partnerships` folder within the repo. <br>This folder can be found by following the file path: `braze-docs` -> `_docs` -> `_hidden` -> `wip_partnerships`.

Here, you will find a partnership template. Navigate to the `partnerships_files` folder, create a partner folder, name it, and copy this template into your folder and get to work!

### Template Components

Your partnership template is composed of three main components, the metadata, the content, and the references. 

Useful links to reference as you write:
- [Braze Writing Style Guide and Best Practices](https://github.com/Appboy/braze-docs/wiki/Writing-Style-Guide-&-Best-Practices): A quick skim of our writing style and best practices helps align your doc with our voice.
- [Braze Docs Styling Test Page](https://www.braze.com/docs/home/styling_test_page/) and [Special Formatting](https://github.com/Appboy/braze-docs/wiki/Special-Formatting): See something cool in our docs that you want to include in your page? Charts? Tabs? Downloadable Files? Check out our Styling test page and Special Formatting pages to get started.


{% tabs %}
{% tab MetaData %}
This information helps our Braze search properly find, label, and categorize your docs page. 
```
---
nav_title: Your Partner Page
page_order: 1

description: "This is the Google Search and SEO description that will appear, try to make this informative and concise, yet brief."
perma_link: /your_perma_link/

page_type: partner
hidden: true
---
```

{% alert note %}
Note that we require you to fill out all metadata fields __except__ `page_order`, `page_type`, and `hidden`.
{% endalert %}

{% endtab %}
{% tab Content %}
This information is the meat of the document. Here you cover the pre-requisites, integration steps, use cases, etc...
For more information on what to include in the content, check out our Partnership [Template](https://www.braze.com/docs/hidden/wip_partnerships/partnership_template.md) that breaks down what should be included.
```
# [Partner Name]

> Welcome to the Partner Page  Template! Here, you'll find everything you need to create your own partner page. In this first section, you should describe the partner in the first paragraph in a sentence or two. Also, include a link to that partner's main site.

In the second paragraph, you should explore and explain the relationship between Braze and this partner. This paragraph should explain how Braze and this partner work together to tighten the bond between the Braze User and their customer. Explain the "elevation" that occurs when a Braze User integrates with or leverages this partner and their services.

## Requirements or Pre-Requisites

This section is all about what you need to integrate with the partner and start using their services. The best way to deliver this information is with a quick instructional paragraph that describes any non-technical important details of "need to know" information, like whether or not your integration will be subject to additional security checks or clearances. Then, you should use a chart to describe the technical requirements of the integration.

{% alert important %}
The requirements listed below are typical requirements you might need from Braze. We recommend using the attributed titling, origin, links, and phrasing as listed in the chart below. Be sure to adjust the description so that you know what each of these requirements is used to do.
{% endalert %}

| Requirement | Origin | Access | Description |
|---|---|---|---|
|Braze App Group REST API Key | Braze platform | Manage App Group > App Settings Page | This description should tell you what to do with the App Group REST API Key. |
|Braze API Endpoint | Braze platform | Check out our [listed endpoints][1] or open a support ticket. | Description pending. |

## [Type of Integration] Integration

This is where you break down the integration into steps. Do not just write endless paragraphs - these are technical documents that will be used by marketers and developers alike to get the integration up and running. Your only goal for this section is to write descriptive documentation that helps the ... Continued in the Partnerships Template.
```

{% endtab %}
{% tab References %}
This last section is located at the very end of your document. Here you will list out all references you need to links and images that you want to include in your document. Please see the next step on best practices for adding images and links to your doc.
```
[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
```
{% endtab %}
{% endtabs %}

## Step 3: Image, Link and Code Snippet Formatting {#image_links}

Links and images are a necessary part of any integration document. They help supplement your instructions with helpful pictures, helping communicate information to users that might be hard or unnecessary to explain in words. 

### Images

The higher quality the images you can provide the better. Images should not include important information such as API keys or employee names, we recommend burring information such as this out. Images should also be tightly cropped to display only useful information. When in doubt, include screenshots, as they can always be removed in the approval process. If in serious doubt, please reach out to @KellieHawks on Github.

To add images to your partner doc, you must place them in the `img` folder in our repository. This folder can be found by following the file path: `braze-docs` -> `assets` -> `img`.

Within this new folder, create a folder to keep your partnership images in, name this folder your partner name.

![Braze Partner Folder][1]{: style="max-width:70%"}

To reference your images in your document use the format listed below. 

{% raw %}
```
![topic_name][1]
```
{% endraw %}

And at the end of your document, link out to your image

{% raw %}
```
[1]: {% image_buster /assets/img/partner_file/image_name.png %}
```
{% endraw %}

### Links

To add links to your document you must follow this format:
{% raw %}
```
For more information, check out [this website or page][1].
```
{% endraw %}

And at the end of your document, add your link.
{% raw %}
```
[1]: https://www.braze.com/docs/user_guide/onboarding_with_braze/integration/
```
{% endraw %}

### Liquid

Partner integrations often leverage our Liquid capabilities within the dashboard. If you plan on including liquid code snippets, they must be wrapped between {% raw %} and {% endraw %} or you'll get a liquid warning in markdown.
{% raw %}
```
{% raw %}
Toggle on the integration to begin sending responses for that survey into Braze. Copy the survey link listed, this is what you'll include in your campaign. Note the `?user_braze_id={{${braze_id}}}` which Braze will automatically replace with the correct braze id of the user you're sending to in the campaign.
{% endraw %}
```
{% endraw %}
## Reviewing and Testing {#testing}

One of the most important things you can do before committing your changes is to test that everything looks and functions as it should. This can be done by running a `rake` command in your terminal.

In your terminal, you will see the command begin to work. This process may take several minutes. You will know when the command is done when you see "done in x seconds, press ctrl-c to stop" appear in the terminal.

Next, you can check your [localhost](http://localhost:4000/docs/).

Here you can navigate to your page that you created through your perma_link you assigned earlier. Once you open the localhost, append the permalink to access your page.

Example: `http://localhost:4000/docs/` + `/your_perma_link/`

Your page will be viewable at `http://localhost:4000/docs/your_perma_link/`

Once you are done reviewing your edits, press Ctrl-C in the terminal, ending the rake command.

## Commiting to Github {#committing}

Once you have made the adequate changes to your partnership doc, save your document, and commit your changes. 

Within the Braze docs GitHub repository, you will be able to find your branch. If your document is completed and ready to review, Select `New Pull Request`, name your request your partnership name and provide any relevant information that we can use to reference when reviewing your content. 

1. Name your Pull Request as your Partnership Name
2. Provide any relevant information that can help the Braze documentation team confirm your changes, as well as your __Braze Product Manager__ so we can reach out to them to get in contact with you about your changes if needed.
3. Tag @KellieHawks and the @Growth team, and our team will take a look.
4. Add a `Done` label so that we can go ahead and evaluate your addition to the docs website.

## Review Process {#review}

The review process may take several days to a week to get approved. We understand other companies may have a different writing style than we do at Braze, so we will need time to make sure it aligns with the Braze voice and the specific formatting that we use.

Once the Pull Request has been approved by our writers, we will move it out of `wip_partnerships` to the correct location in our repository.

And you are done! Thanks for contributing to Braze Docs! 

[1]: {% image_buster /assets/img/partner_template/partner_folder.png %}
