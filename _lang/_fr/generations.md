---
nav_title: Generations
article_title: In-App Message Generations
hidden: true
description: "This reference article covers in-app messaging generation support."
channel:
  - in-app messages
---

# In-app messages generations

Braze currently has three generations of in-app messages. Each comes with it own level of support. To take advantage of the newest features of our in-app messages, we recommend upgrading to the newest [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#upgrading-the-sdk), iOS, and Android SDKs.

This chart highlights the features and message types that are currently available and when they were introduced in each generation. This chart also explicitly states what isn't supported within a given generation.

| Generation       | New Features                                                                                                                                                                                                                                     | Unsupported Features                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| __Generation 1__ | • In-app triggered Full-Screen, Modal, and Slideup message types                                                                                                                                                                                 | Custom HTML Messages <br> • Web Email Capture Form <br> • Web Modal with Custom CSS |
| __Generation 2__ | • Text Alignment Controls <br> • Overlay behind Modal <br> • Image Safe Zone in Preview Window                                                                                                                                       | Button Border                                                                                   |
| __Generation 3__ | • Button Border <br> • Refined Look & Feel for All Message Types <br> • Concept of Generations 1, 2 and 3 <br> • New Close X Asset <br> • Improved accessibility on Web <br> • Improved support on Notched Devices | (The latest Generation always has full feature support!)                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

![Difference in Generations]({% image_buster /assets/img/iam-generations-of-modals.png %})

