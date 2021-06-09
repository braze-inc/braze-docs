---
nav_title: Link Aliasing
permalink: /linkaliasing/
description: "This article describes how Link Aliasing works and some of the nuances with the feature."
hidden: true
---

 
### Link Aliasing
Goal: Identifying links set in an email message from Braze by a user generated friendly name.
Goal: Having the ability to re-target users based on clicking a specific link sent in an Email.  
 
 
#### How Link Alisaing works
Link Aliasing works by decorating a Braze generated query parameter on links in the email channel.  For each known link that is present in the Email body, Braze will add a ‘lid={{somevalue}}’ when the client goes to the ‘Link Management’ section or hits ‘done’ on the editor (returning to the ‘compose’ section in campaigns or step overview in canvas).
 
These query parameters are also added to content blocks as well, this way Links present in Content Blocks can also be tracked for segmentation purposes.
 

![link_aliasing_composer][2]{: style="max-width:80%;"}

Clicking the Link Management Tab will decorate all known links in the email body.  From the Link Management tab, the client can set an ‘Alias’ which is how this link will be referenced throughout the Braze product (for reporting and segmentation purposes).  Aliases are required to be uniquely named per email campaign variant  or canvas step.

The client can also add Link Templates from the Link Management section.
 
 
 
 
#### Feature enablement
The process to enable link aliasing is simple and does not require any downtime.  This enablement is not backward compatible, meaning that previously created messages or content blocks will not be recognized by this feature (unless they are modified and launched again).  

##### Preconditions / Limitations
Client is okay with their message being modified by an HTML parser.  This could lead to the parser ‘correcting’ potentially incorrect HTML. (currently this already happening if you use features such as pre-header input field, liquid statements, or link templates)
Client is okay with the implications of being in a partially migrated state (some messages will have aliasing, some will not (same with content blocks))
Editing messages or content blocks prior to having the feature enabled will result in Braze editing links
Link Aliasing is not supported for modifying links in 'mso commented elements'
Updating a content block, such that it is now decorated with lid values, will only support propagating link documents to the first 50 'includers'.  An includer is equal to a message variant where the content block is used or another content block when nested.

##### What happens after the feature has been enabled
Message Variants
New email message variation (campaign or canvas) will have their links modified, where Braze will append a 'lid=somevalue' to each link (where applicable)
Any email message variation that was created prior to us enabling this feature, will only have their links modified when the HTML in those message variants are edited.
HTML Content Blocks
All new content blocks will have their links modified, where Braze will append a lid={{ some placeholder value }} to each link (where applicable).  The placeholder value is resolved when inserted into an email message variant
Any existing content blocks that were created prior to us enabling this feature, will only have their links modified when the HTML in that content block is edited and the content block is re-launched.
When a content block that is not decorated with the 'lid' value is inserted into a new message, the links from that content block are not tracked with an alias.
When a content block that is not decorated with the 'lid' value is inserted into an old message, and that message has not been edited, the links are not tracked with any alias.
When a new content block is inserted into an 'old' message variant, the links from that message variant will be recognized by this feature (since the MV was edited).  Links from the content block are also recognized.
"Old" content blocks (not marked up) cannot nest "new" content blocks.
Recommendation:  For content blocks, a recommendation would be to create copies of existing content blocks that can be used in new messages.  This can be done by using the ‘bulk duplicate’ functionality.  This will prevent some of the edge cases where you might reference a content block that has not been enabled for Link Aliasing in a new message.
 
##### Using HTML content blocks in other channels
If the HTML content block is used in other channels (for example IAM), a 'lid=' value will still be appended on each link.  The value will not be populated, so you will see something like this: "http://www.braze.com?lid="

##### Heatmap
The heatmap feature is not supported with this version of the Link Aliasing product.  Future iterations may support showcasing the heatmap again.

##### Link Templates
For new message variations, any existing Link Template can be used from the "Link Management" tab
For any email message variation that was setup prior to us enabling this feature, the existing Link Templates will still be present.  However, if the message variation is edited, the Link Templates will need to be reapplied.

###### API Triggered
Any message variation where the customer passes data related to links, is not supported by this feature. 

###### Extracting data
Endpoints are available to extract the ‘alias’ set in each Message Variant in a Campaign or from an Email Canvas Step.

##### Link Tracking
By default, only 100 links can be tracked (for segmentation purposes) per AppGroup.  Links within messages that are archived will automatically be untracked.  If archived messages are unarchived, links will need to be tracked again.

##### Link Segmentation
Two new filters are now available, allowing clients to create segment filters based on clicking a specific tracked alias.  The filter displays only campaigns or canvases that have tracked aliases present.
 


In addition to creating segment filters, clients can also create action based messages targeting any link (tracked or not tracked) across any email campaign or canvas step. 


##### Link Click Reporting:
Link reporting will now be indexed by the ‘alias’ rather than top level domains and/or full URLs.  
![link_aliasing_click_table][1]{: style="max-width:80%;"}


[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}

