---
alias: /partners/partner_walkthrough/
title: Partner Documentation
nav_title: Partner Docs
hidden: true
page_type: reference
---

# Partnership documentation

Welcome, Braze Partners, and thank you for contributing to our customer knowledge base. Creating and adding partner pages to the Braze docs repository can be quick and simple with the right tools and setup.

Partnership Documentation Overview
- [Set up your local environment](#setup_env)
- [Create and add content to your page](#create_page)
- [Image, link, and code snippet formatting](#image_links)
- [Reviewing and testing](#testing)
- [Commiting to Github](#committing)
- [Review process](#review)
<br><br>
{% alert important %}
This partnership guide is for NEW Braze partners that **do not have existing documentation** already hosted on our site. If you are an existing partner updating your documentation, navigate to your partner page located at `braze-docs` > `_docs` > `_partners` and update your pages as you normally would. 
{% endalert %}

## Step 1: Set up your local environment {#setup_env}

To contribute to Braze docs, you must have a GitHub account to commit changes and edits. 

We recommend first [forking](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) our GitHub repository, and then creating a local clone of your fork:
1. Navigate to the main [braze-docs repo](https://github.com/Appboy/braze-docs), and click **Fork** in the upper right corner of the page. <br><br>
2. Next, within this newly forked repo, click the green **Clone or download** button. From the dialogue that appears, click **Use SSH**, and **save the repository link provided** for step 3. <br><br>
3. Lastly, follow our GitHub Wiki Guide on setting up your [local environment](https://github.com/Appboy/braze-docs/wiki/Set-Up-Your-Local-Environment#configuring-the-github-braze-docs-repo) **ommitting step 3 of the guide**, and instead, **using the repository link saved,** to clone your forked repo.

After setting up your local environment, make sure to sign our [CLA](https://www.braze.com/docs/cla) (Contribution License Agreement), _this step is required_.

## Step 2: Create and add content to your page {#create_page}

To create your partner page, open the braze-docs repository and navigate to the `wip_partnerships` folder within the repo. <br>This folder can be found by following the file path: `braze-docs` > `_docs` > `_hidden` > `wip_partnerships`. Here, you will find a [partnership template]({{site.baseurl}}/partners/your_partner_name/).

Next, create a folder, name it your partner name, copy this template into your folder, and get to work!

> Your file pathing should now look like this: <br>`braze-docs` > `_docs` > `_hidden` > `wip_partnerships` > `partner_name` (folder) > `partner.md`.

### Useful Resources

Useful links to reference as you write:
- [Braze writing style guide and best practices](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub): A quick skim of our writing style guide and best practices help align your documentation with our voice.<br>
- [Braze docs styling test page](https://www.braze.com/docs/home/styling_test_page/) and [special formatting](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting): See something cool in our docs that you want to include in your page? Want to know how to add charts, tabs, downloadable files, and more? Check out our styling test page and special formatting pages to get started.

### Template Components

Your [partnership template]({{site.baseurl}}/partners/your_partner_name/) is composed of three main components, the metadata, the content, and the references. 

{% tabs %}
{% tab Meta data %}
This information helps our Braze search find, label, and categorize your docs page properly. 
```
---
nav_title: Your Partner Page
article_title: Your Partner Page
page_order: 1

description: "This is the Google Search and SEO description that will appear; try to make this informative and concise, yet brief."
alias: /partners/your_partner_name/

page_type: partner
search_tag: Partner
hidden: true
---
```

{% alert note %}
Note that we require you to fill out all metadata fields **except** `page_order`, `page_type`, and `hidden`.
{% endalert %}

{% endtab %}
{% tab Content %}
This information is the meat of the document. Here you cover the prerequisites, integration steps, use cases, etc.

For more information on what to include in the content, check out our [partnership template]({{site.baseurl}}/partners/your_partner_name/) that breaks down what should be included.

```
# [Partner Name]

> Welcome to the Braze partner template! Here, you'll find everything you need to create your partner page. In this first section, include a brief description of your company. Also, include a link to your main site. 

In this second paragraph, explore the relationship between your company and Braze. This paragraph should explain how Braze and your company partner together to tighten the bond between the Braze user and their customer. Explain the "elevation" that occurs when a Braze user integrates with or leverages your partnership and the services you offer.

## Prerequisites

This section should list what you need to complete this partnership integration. The best way to deliver this information is with a quick instructional paragraph that describes any non-technically important details or "need to know" information, like whether or not your integration will be subject to additional security checks or clearances. Then, use a chart to describe the technical requirements of the integration.

{% alert important %}
The requirements listed below are typical requirements you might need from Braze. We recommend using the attributed titling and phrasing listed in the chart below. Be sure to adjust the descriptions and tailor them to your partnership integration. 
{% endalert %}

| Requirement | Description |
| ----------- | ----------- |
| Partner account | A partner account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST Endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Use cases can be a critical part of your documentation. Although optional, this is a good place to outline typical or even novel use cases for the integration. This can be used as a way to sell or upsell the relationship - it provides context, ideas, and most importantly, a way to visualize the capabilities of the integration.

## Integration

This is where you break down the integration into steps. Do not just write endless paragraphs - these are technical documents that will be used by marketers and developers alike to get the integration up and running. Your main goal is to write descriptive documentation that helps the Braze user get the job done.
```

{% endtab %}
{% tab References %}
This last section is located at the very end of your document. Here, you will list all references you need to links and images you want to include in your document. Please see the next step on best practices for adding images and links to your doc.
```
[1]: https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints
```
{% endtab %}
{% endtabs %}

## Step 3: Image, link, and code snippet formatting {#image_links}

Links and images are a necessary part of any integration document. They help supplement your instructions with helpful pictures, communicate information to users that might be hard or unnecessary to explain in words. 

### Images

The higher quality of the images you can provide, the better. Images should not include important information such as API keys or employee names; we recommend burring information such as this out. Images should also be tightly cropped to display only useful information. When in doubt, include screenshots, as they can always be removed in the approval process.

To add images to your partner doc, you must place them in our repository's `img` folder. This folder can be found by following the file path: `braze-docs` > `assets` > `img`.

Within this new folder, create a folder to keep your partnership images in. Name this folder your company name.

![Braze partner folder][1]{: style="max-width:70%"}

To reference your images in your document, use the format listed below. 

{% raw %}
```
![topic_name][1]
```
{% endraw %}

And at the end of your document, link out to your image.

{% raw %}
```
[1]: {% image_buster /assets/img/partner_file/image_name.png %}
```
{% endraw %}

### Links

To add links to your document, you must follow this format:
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

Partner integrations often leverage our Liquid capabilities within the dashboard. If you plan on including Liquid code snippets, they must be wrapped between {&#37; raw &#37;} and {&#37; endraw &#37;} or you'll get a Liquid warning in markdown.

{% raw %}

{&#37; raw &#37;}<br>
?user_braze_id={{&#36;{braze_id}}}<br>
{&#37; endraw &#37;}

{% endraw %}

## Step 4: Reviewing and testing {#testing}

One of the most important things you can do before committing your changes is to test that everything looks and functions as it should. This can be done by running a `rake` command in your terminal.

In your terminal, you will see the command begin to work. This process may take several minutes. You will know when the command is done when you see "done in x seconds, press ctrl-c to stop" appear in the terminal.

Next, you can check your [localhost](http://localhost:4000/docs/).

Here you can navigate to the page you created using the alias you assigned earlier in the article's metadata. Once you open the localhost, append the alias to access your page.

Example: `http://localhost:4000/docs/` + `/partners/your_partner_name/`

Your page will be viewable at `http://localhost:4000/docs/partners/your_partner_name/`

After reviewing your edits, press **Ctrl-C** in the terminal and end the rake command.

## Step 5: Commiting to GitHub {#committing}

Once you have made the adequate changes to your partnership doc, save your document, and commit your changes. 

Within the Braze docs GitHub repository, find your branch. If your document is completed and ready to review, navigate to your forked repo in GitHub and select `New Pull Request`. Next, select how you would like your forked branch to be merged, name your request your partnership name and provide any relevant information that we can use to reference when reviewing your content. 

![Merge Branches][2]

1. Set up your branch to be merged in a similar fashion as shown above.<br><br>
2. Name your Pull Request as "Partnership Name - Partner Docs"<br><br>
3. Provide any relevant information that can help the Braze documentation team confirm your changes, as well as your **Braze product manager** so we can reach out to them to get in contact with you about your changes if needed.<br><br>
4. After you are done making changes, tag @KellieHawks and @Timothy-Kim in a comment within the pull request, and our team will take a look.<br><br>

## Review process {#review}

The review process may take several days to a week to get approved. We understand other companies and writers may have a different writing style than we do at Braze, so we will need time to make sure it aligns with the Braze voice and the specific formatting that we use.

Once our writers have approved the pull request, we will move it out of `wip_partnerships` to the correct location in our repository. Please note that we may not merge your documentation into our repository until told to do so by the Braze partnership team. Reach out to your Braze partnership contact for an anticipated release date.

And you are done! Thanks for contributing to Braze docs! 

[1]: {% image_buster /assets/img/partner_template/partner_folder.png %}
[2]: {% image_buster /assets/img/partner_template/partner_merge.png %}
