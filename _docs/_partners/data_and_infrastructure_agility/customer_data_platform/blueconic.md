---
nav_title: BlueConic
page_order: 8
description: "This article covers the Braze and BlueConic integration. BlueConic is a leading pure-play customer data platform providing accessible first-party data wherever and whenever it is required to transform customer relationships and drive business growth."
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [BlueConic][1], the leading pure-play customer data platform, liberates companies' first-party data from disparate systems and makes it accessible wherever and whenever it is required to transform customer relationships and drive business growth. 

With Blueconic, Braze users can unify data into persistent, individual profiles and then sync it across customer touchpoints and systems in support of a wide range of growth-focused initiatives, including customer lifecycle orchestration, modeling and analytics, digital products and experiences, audience-based monetization, and more.

## Prerequisites

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][2] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | This API Key allows you to authenticate Braze within the BlueConic platform |
| S3 Authentication | Amazon Web Services (AWS) | [AWS Account][2] | You need to have access to an Amazon Web Services (S3) server because the data will be exported and/or imported via an S3 server. |
| Access Key ID & Secret Access Key | AWS | [S3 security credentials page][3] | The Access Key ID will allow you to authenticate your S3 server for importing and exporting<br><br>The Secret Access Key will allow you to authenticate your S3 server for importing and exporting |
| Bucket | AWS | You will need to connect to S3 within the plugin. After authentication, the available buckets will show in a dropdown menu | This is where the files to be imported or exported are stored. |
| BlueConic Account | BlueConic | [BlueConic][1] | You will need to have [access to view and edit Connections][4] within your BlueConic account to access the plugins |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

The Braze and BlueConic connection allows you to enrich profile data across the two platforms for import goals via an Amazon S3 server. This connection supports scheduled batch import and export. The BlueConic customer data platform harnesses the data required to power the recognition of an individual at each interaction and then synchronizes their intent across the marketing ecosystem. By exchanging profile data between BlueConic and Braze, you can share first-party customer data from BlueConic profiles using data stored in Braze.

### Step 1: Creating a Braze Connection

1. On the BlueConic platform, select __Connections__ in the navigation bar, and then __Add Connection__. In the pop-up window that appears, enter "Braze" in the search bar and select __Braze connection__.<br><br>![BlueConic Plugin Gallery Braze Connection]({% image_buster /assets/img/blueconic/braze1.png %}){: style="max-width:50%;"}<br><br>
2. In the Braze connection, expand or collapse metadata fields by clicking the grey chevron icon. Within these fields, you can mark the connection as a favorite, add labels, and write a brief description. You can also choose to get [email notifications when the connection runs or fails to run][5]. <br><br>
3. Lastly, enter the name for your connection at the top of the page and save your settings. 

### Step 2: Configuring A Braze Connection With BlueConic

To configure the connection between BlueConic and Braze, you must add your Braze account credentials and Amazon Web Services (S3) account information to authenticate the connection. 

1. Select __Set up and run__ in the Setup section in the left panel.<br><br>
2. In the Braze authentication section, enter your Braze instance URL and Braze API key.<br><br>![BlueConic Authentication]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. In the S3 setup and authentication section, enter the Amazon Web Services (S3) access key ID, secret access key, and S3 bucket.<br><br>![BlueConic S3 Authentication]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}<br><br>
4. Save your settings.

### Step 3: Creating Import Goals (Import Mapping)

Once the authentication is complete, you'll create at least one import or export goal, turn the connection on, and either schedule or run the connection.

1. Select __Import data into BlueConic__ in the left panel to open the page to configure your data import from Braze to BlueConic.<br><br>
2. Select the location of the data in Braze. Here you can tell BlueConic where to find the data to be imported by selecting your Braze audience.<br><br>![BlueConic Import Goal]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. Next, you must map identifiers between Braze and BlueConic. <br><br>![BlueConic Import Goal]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> To link the customer data between the two systems, enter one or more customer identifiers. Use the drop down fields to select either the BlueConic profile identifier or a profile property on the left and then select the corresponding Braze profile identifier. Next, use the dropdown menu to specify how imported content should be added to existing values: added, summed, set only if the profile property is empty, or set to clear (if the Braze field is empty). <br><br>Use the __Allow creation...__ checkbox to allow BlueConic to create new profiles for data that does not match an existing BlueConic profile.<br><br>![BlueConic Import Map]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
4. Use the __Add Mapping__ button to create additional mapping rows as needed. You can add multiple mapping rows at once with the __Add remaining fields__ option. BlueConic detects the remaining Braze fields and matches them with BlueConic profile properties. You can set the merge strategy for imported (set, add, sum, set if empty or clear) and provide a custom prefix to the names of BlueConic profile properties.<br><br>
5. Lastly, select __Run the connection__ to start the connection. See [Scheduling and running connections][6].

## Step 4: Creating Export Goals (Export Mapping)

Select __Export data to Braze__ in the left panel to configure your data export from BlueConic to Braze. Choose a BlueConic segment for the export. Only profiles in this segment that have matching identifiers in Braze will be exported.

Like the import mapping shown in step 3, you must link identifiers between BlueConic and Braze, matching export identifiers between BlueConic profiles and Braze fields. You can optionally choose to let BlueConic create new records in Braze if no existing match is found.

![BlueConic Export Map]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}

Use the dropdown menu from the BlueConic icon to choose the type of information you want to export.

Lastly, click __Run the connection__ to start the connection. See [Scheduling and running connections][6]

## Using This Integration

Use the toggle next to the Braze connection title to toggle the connection on and off. A connection must be _on_ to run during scheduled times. 

[1]: https://www.blueconic.com/
[2]: https://portal.aws.amazon.com/billing/signup#/start
[3]: https://console.aws.amazon.com/iam/home?#security_credential
[4]: https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles
[5]: https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ
[6]: https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections
