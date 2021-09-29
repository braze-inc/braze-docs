---
nav_title: BlueConic Connection
page_order: 1

description: "BlueConic, the leading pure-play customer data platform, liberates companies’ first-party data from disparate systems and makes it accessible wherever and whenever it is required to transform customer relationships and drive business growth."
alias: /partners/blueconic/

page_type: partner
hidden: true
---

# BlueConic

> [BlueConic][1], the leading pure-play customer data platform, liberates companies’ first-party data from disparate systems and makes it accessible wherever and whenever it is required to transform customer relationships and drive business growth. Over 300 companies worldwide, including Hearst Newspapers, Heineken, ING, T-Mobile, and VF Corp, use BlueConic to unify data into persistent, individual-profiles, and then activate it across customer touchpoints and systems in support of a wide range of growth-focused initiatives, including customer lifecycle orchestration, modeling and analytics, digital products and experiences, audience-based monetization, and more. BlueConic is a global company with offices in the US and Europe.



## Requirements or Prerequisites


| Requirement | Origin | Access | Description |
|---|---|---|---|
| Instance URL | Braze | Your Braze endpoint | As an example: https://rest.iad-01.braze.com, where iad-01 reflects to where your instance it located. | 
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | The API Key will allow you to authenticate Braze within the BlueConic platform |
| S3 Authentication | Amazon Web Services (AWS) | [AWS Account][2] | You need to have access to an Amazon Web Services (S3) server, because the data will be exported and / or imported via an S3 server. |
| Access key ID | AWS | [S3 security credentials page][3] | The Access key ID will allow you to authenticate your S3 server for importing and exporting |
| Secret access key | [S3 security credentials page][3] | The Secret access key will allow you to authenticate your S3 server for importing and exporting |
| Bucket | AWS | You will need to connect to S3 within the plugin. After authentication, the available buckets will show in a dropdown menu | This is where the files to be imported are stored or need to be exported to. |
| BlueConic account | [BlueConic][1] | n/a | You will need to have [access to view and edit Connections][4] within your BlueConic account to access the plugins |

## Integration

The Braze connection allows you to enrich BlueConic profiles with data from Braze and vice versa, for import goals via an Amazon S3 server. This connection supports scheduled batch import and export. The BlueConic customer data platform harnesses the data required to power the recognition of an individual at each interaction, and then synchronizes their intent across the marketing ecosystem. By exchanging profile data between BlueConic and Braze, you can share first-party customer data from BlueConic profiles using data stored in Braze, and vice versa.

### Step 1: Creating a Braze Connection

Click _Connections_ in the BlueConic navigation bar, then click _Add Connection_. A pop-up window will appear. Enter "Braze" in the search bar. 

![BlueConic Plugin Gallery Braze Connection](/assets/img/blueconic/braze1.png){: style="max-width:50%;"}

Click _Braze Connection_. Once the Braze connection opens, you can expand or collapse the metadata fields by clicking on the gray chevron icon. Within the metadata fields, you may mark the connection as a favorite, add labels, or write a brief description about what the connection does. You can also choose whether to get [email notifications when the connection runs or fails to run][5].

Enter a name for your connection at the top of the page and save your settings. 

### Step 2: Configuring A Braze Connection With BlueConic

To set up a connection between BlueConic and Braze, you need to add your Braze account credentials as well as your Amazon Web Services (S3) account information, in order to authenticate the connection. 

Select _Set up and run_ in the Setup section in the left panel.

In the Braze authentication section, enter your _Braze instance URL_, and _API key_.

![BlueConic Authentication](/assets/img/blueconic/braze2.png){: style="max-width:60%;"}

In the S3 setup and authentication section, enter the Amazon Web Services (S3) access key ID, secret access key, and S3 bucket.

![BlueConic S3 Authentication](/assets/img/blueconic/braze3.png){: style="max-width:60%;"}

Save your settings.

Once the authentication is complete, you'll create at least one import or export goal, turn the connection on, and either schedule or run the connection.


### Step 3: Creating Import Goals

Select _Import data into BlueConic_ in the left panel to open the page to configure your data import from Braze to BlueConic. 

Select the location of the data in Braze. Here you can tell BlueConic where to find the data to be imported by selecting your Braze audience.

![BlueConic Import Goal](/assets/img/blueconic/braze4.png){: style="max-width:60%;"}

Link identifiers between Braze and BlueConic. To match customer data between the two systems, enter one or more customer identifiers. Use the dropdown menu in the BlueConic field to select either the BlueConic profile identifier or a profile property. 

![BlueConic Import Goal](/assets/img/blueconic/braze5.png){: style="max-width:60%;"}

Use the _Allow creation..._ checkbox to allow BlueConic to create new profile for data that does not match an existing BlueConic profile.

Map Braze data to BlueConic profile properties. You can match Braze fields on the left column to BlueConic profile properties on the right column. Use the dropdown menu to specify how imported content should be added to existing values: added, summed, set oly if the profile property is empty, or set to clear (if the Braze field is empty). 

![BlueConic Import Map](/assets/img/blueconic/braze6.png){: style="max-width:60%;"}

Use the _Add Mapping_ button to create additional mapping rows. You can add multiple mapping rows at once with the _Add remaining fields_ option. BlueConic detects the remaining Braze fields and matches them with BlueConic profile properties. You can set the merge strategy for imported (set, add, sum, set if empty or clear) as well as provide a custom prefix to the names of BlueConic profile properties.

_Run the connection_. See [Scheduling and running connections][6].


## Step 4: Creating Export Goals

Select _Export data to Braze_ in the left panel to open the page to configure your data export from BlueConic to Braze. 

Select a BlueConic segment for the export. Only profiles in this segment that have matching identifiers in Braze will be exported.

Link identifiers between BlueConic and Braze. At this point, you can match identifiers between BlueConic profiles and Braze fields. You can optionally choose to let BlueConic create new records in Braze if no existing match is found.

![BlueConic Export Map](/assets/img/blueconic/braze7.png){: style="max-width:60%;"}

Use the dropdown menu from the BlueConic icon to choose the type of information you want to export.

_Run the connection_. See [Scheduling and running connections][6]



## Using This Integration

Use the toggle next to the title to turn the connection on and off. A connection must be _on_ to run during scheduled times. 


[1]: https://www.blueconic.com/
[2]: https://portal.aws.amazon.com/billing/signup#/start
[3]: https://console.aws.amazon.com/iam/home?#security_credential
[4]: https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles
[5]: https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ
[6]: https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections
