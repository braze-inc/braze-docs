---
permalink: "/partner_docs/"
title: Partner Documentation
nav_title: Partner Docs
hidden: true
page_type: reference
---

# Partnership Documentation

Welcome Braze Partners and thank you for contributing to our customer knowledge base. Creating and adding partner pages to the Braze docs repo can be quick and simple with the right tools and set up.

## Step 1: Set up Your Local Environment

To contribute to Braze docs, you must have a Github account with which you can commit changes and edits. 

Follow our instructions here on how to set up you [local environment](https://github.com/Appboy/braze-docs/wiki/Set-Up-Your-Local-Environment)

After setting up your local environment, make sure to sign our [CLA](https://www.braze.com/docs/cla) (Contribution License Agreement), this step is Required.

## Step 2: Create Your Page

To create your partner page, open the Braze-docs repo and navigate to the `wip_partnerships` folder within the directory. <br>This can be found by in following this file path: `braze-docs` -> `_docs` -> `_hidden` -> `wip_partnerships`.

Here you will find a partnership template. Navigate to the partnerships_files folder, create a new folder, name it and copy this template into this folder and get to work!

### Template Components

Yout partnership template is composed of three main components, the metadata, the content, and the references. 

{% tabs %}
{% tab MetaData %}
This information helps the Braze search properly find and label your docs page. 
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
Note that we require to fill out all metadata fields __except__ `page_order` and `page_type`. Please reference the provided [template](https://www.braze.com/doc/hidden/wip_partnerships/partnership_template.md) for a fleshed out example of these fields.

{% endtab %}
{% tab Content %}
This information is the meat of the document. Here you cover the pre-requisites, integration steps, use cases, etc...
For more information on what to include in the content, check out our Partnership Template that breaks down what should be included, as well as a completed partnership docs [here].
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
This last section, while the shortest is located at the end of the document. Here you will list out all references you need to links and images that you want to include in your doc. Please see the next step on best practices for adding images and links to your doc.
```
[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
```
{% endtab %}
{% endtabs %}

Useful links to reference as you write:
- [Braze Writing Style Guide and Best Practices](https://github.com/Appboy/braze-docs/wiki/Writing-Style-Guide-&-Best-Practices)
- Other thing 1
- Other thing 2

## Step 3: Add Images and Links

Links and images are a necessary part of any integration document. They help supplement your instructions with helpful pictures, helping communicate to users information that might be hard to explain in words. 

### Images

The higher quality the images you can provide the better. Images should not include important information such as API keys or employee names, we recommend burring information such as this out. Images should also be tightly cropped to display only useful information. If you are unsure of the best way to display, crop, or blur images, check out some [examples].

To add images to your partner doc, you must place them in the correct directory, to locate this directory, navigate to `braze-docs` -> `assets` -> `img`

Within this new directory, create a folder to keep your partnership images in, name this folder the name of your Braze partner.

To reference your images in your document use this format:

{% raw %}
```
![topic_name][1]{: style="max-width:60%"}
```
{% endraw %}

And at the end of your document, link out to your image

{% raw %}
```
[1]: {% image_buster /assets/img/your_partner_file/image_name.png %}
```
{% endraw %}

### Links

To add links to your document you must follow this format:
{% raw %}
```
For more information, check out [this website][1].
```
{% endraw %}

If your link references a pre-existing braze document, you must follow this format:
{% raw %}
```
{{site.baseurl}} = https://www.braze.com/docs/

[1]: {{site.baseurl}} + rest of link after /docs/
```
{% endraw %}

If your link comes from outside braze docs:
{% raw %}
```
[1]: https://www.yourlinkgoeshere.com/
```
{% endraw %}
### Testing

One of the most important things you can do before committing your changes is to test it. This can be done by running a `rake` command in your terminal.

In your terminal, you will see the command begin to work. This process may take several minutes. You will know when the command is done when you see "done in x seconds, press ctrl-c to stop" appear in the terminal.

Next, you can check your [localhost](http://localhost:4000/docs/).

Here you can navigate to your page that you created through your perma_link you assigned earlier. Once you open the localhost, append the permalink to access your page.

Example: `http://localhost:4000/docs/` + `/your_perma_link/`

Your page will be viewable at: `http://localhost:4000/docs/your_perma_link/`

Once you are done checking press Ctrl-C in the terminal, ending the rake command.

### Commiting

Once you have made the adequate changes to your partnership doc, save your document, and commit your changes. 

Within the Braze docs GitHub repo, you will be able to find your branch. If your document is completed and ready to review, Select `New Pull Request`, name your request your partnership name and provide any relevant information that we can use to reference when reviewing your content. 

1. Name your Pull Request as your Partnership Name
2. Provide any relevant information that can help the Braze documentation team confirm your changes, as well as your __Braze Product Manager__ so we can reach out to them to get in contact with you about your changes, if needed.
3. Tag @KellieHawks and the @Growth team, and our team will take a look.
4. Add a `Done` label so that we can go ahead and evaluate your addition to the docs website.

### Review Process

The review process may take several days, we understand other companies may have a different writing style than we do at Braze, so we will need time to make sure it aligns with the Braze voice and the specific formatting that we use.

Once the Pull Request has been approved by our writers, we will move it out of `WIP_partnerships` to the correct location in the Directory.

And you are done! Thanks for contributing to Braze Docs! 
