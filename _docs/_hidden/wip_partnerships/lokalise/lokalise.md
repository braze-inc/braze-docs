---
nav_title: Lokalise
article_title: Lokalise
page_order: 1

description: "This article outlines the partnership between Braze and Lokalise, a translation management service for agile teams."
alias: /partners/lokalise/

page_type: partner
search_tag: Partner
hidden: true

---

# Lokalise

> [Lokalise](https://lokalise.com) a translation management service for agile teams.

With Lokalise you can easily translate your Braze campaigns. Follow the instructions on this page to get started with your Lokalise integration.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Lokalise account | A Lokalise account is required to take advantage of this partnership. |
| Lokalise translation project | A Lokalise translation project should be created before starting to set up this integration. |
{: .reset-td-br-1 .reset-td-br-2}

### Create a new Lokalise project

In order to create a new translation project, proceed to Lokalise, log into the system, and click **New project**. Give your project a name, choose a **base language** (usually, that's the language you are going to translate from), add one or more **target languages**, and choose **software localization** project type. Once you are ready, click **Proceed**.

## Integration

This integration is based on Braze's connected content. On Braze, you will use connected content whenever you want a piece of content to be localized, including within content blocks. The connected content will be retrieved from a different dedicated URL for each language; therefore, your users should have language information tied to their profiles.

### Step 1: Configuring user languages

If you haven't already done so, open your Braze dashboard and proceed to **Users > User import**. Here you can import your users as explained in Braze documentation. When preparing a CSV file for importing, make sure to include a language column with users' languages. We will use this language field later when displaying translations. It’s very important that you use the same language codes as on Lokalise.

In Lokalise, you will create a translation key for each one of the connected content variables that you define in Braze. Once the translations are ready, you can generate one JSON file per language, and get it published on the URLs that will serve your connected content.  

### Step 2: Preparing your translations on Lokalise

Prepare your translations on Lokalise. You'll need to create the translation keys manually, with the sames name that you're using on Braze connected content variables. For example, let's create a simple translation key `description`. To achieve that, open your Lokalise project, click **Add key**, enter "description" in the **Key** field, type "Demo description" in the **Base language value** field, and make sure to choose "Web" in the **Platforms** dropdown. Once you are ready, click **Save**:

![Add a new translation key.][1]

Your translation key should appear in the project editor:

![Translation key was added.][2]

### Known issues

- Your keys must be assigned to the **Web** platform.
- Please avoid using keys that contain periods (`.`) or the `_on` string. For instance, use `this_is_the_key` instead of `this.is.the.key`, and use `join_us_instagram` instead of `join_us_on_instagram`.

### Step 3: Configuring the Braze app on Lokalise

Open your Lokalise project, and click **Apps**. Here search for the Braze app, click on it and then press **Install**.

You are going to see the following screen:

![Braze configuration on Lokalise.][3]

On the **translation file URL**, Lokalise publishes a JSON file containing all the translations for your keys in the project. You'll get as many translation file URLs as target languages you have in your project. This is why the resulting translation file URLs have two pieces:

- The first part of the URL path is common to all languages.
- The JSON file name at the end of the URL is based on the language code. Remember, it's very important that you use exactly the same language codes on Lokalise and on Braze user profiles.

The translation file URL is the URL that you will need when configuring a Braze campaign. You can update the content on the JSON file by clicking **Refresh**; note that the URL will stay the same and you won't need to change your connected content call on Braze's side. 

To test that this URL works correctly, just copy it, replace `{{${language}}}` with a language code (for example, `en`) and open this URL in your browser. You will see a JSON file with your keys and translations:

![Testing JSON file URL.][4]

### Step 4: Using translations in Braze campaign

When you are ready, return to Braze and proceed to Campaigns. 

First, remember that the connected content will be retrieved from a different dedicated URL for each language; therefore, your users should have language information tied to their profiles.

Open an existing campaign or create a new one. For the purposes of this article, we'll create a new Email campaign with some sample content.

Click **Edit Email Body**:

![Editing email body.][5]

You will see your email's HTML markup which utilizes Liquid template language.

In order to utilize your translations, you need to add the connected content request once in the HTML, either at the top of the document or right before the first place where a translation is needed. You do it by inserting the following markup:

{% raw %}
{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}
{% endraw %}

Replace the `https://exports.live.lokalise.cloud/...` URL with the translation file URL fetched in the previous step.

- `{{${language}}}` means "insert user language on this position". Alternatively, you can hardcode your language code, for example `en.json`.
  + Note: To ensure that the appropriate translated JSON file is retrieved for each user, you must place either the {{${language}}} profile attribute or another similar custom attribute that holds the user’s language at the end of the translation files URL. E.g., /{{${language}}}.json. The values held in these attributes must match the prefix of each of the translated JSON files. This will ensure the correct translation file is returned for each user.
- `:save translations` is going to save the JSON content under translations variable.

Now simply use the translations variable to display the desired translations by their keys.

For example, to display the `description` key you would say:

{{ translations.description }}

![Using connected content.][6]

Now simply save the email template and preview it. You should see your translation being displayed.

## Frequently asked questions

- **What happens if I accidentally delete a key from Lokalise?** The corresponding string on Braze won't have a translation anymore.
- **If I have an `en` locale but override it with `en-US` on Lokalise, will Braze read it as `en-US`?** No, locale ISO codes must match on Braze and Lokalise.
- **Can we use the `:rerender` flag when connecting Lokalise content?** Yes, sure. You can consult Braze docs to learn how to add this flag.
- **After refreshing the translation file on Lokalise, I can't see any changed on the translated content on Braze. Why?** Braze caches translated content on their side, and it can take a few minutes to refresh. If you're testing your campaigns and you need to see the results of translations immediately, you can use the `:cache_max_age` parameter as explained in this article.

[1]: {% image_buster /assets/img/lokalise/1_add_key.png %}
[2]: {% image_buster /assets/img/lokalise/2_translation_key_added.png %}
[3]: {% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %}
[4]: {% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %}
[5]: {% image_buster /assets/img/lokalise/5_edit_email.png %}
[6]: {% image_buster /assets/img/lokalise/6_integration_usage_sample.png %}