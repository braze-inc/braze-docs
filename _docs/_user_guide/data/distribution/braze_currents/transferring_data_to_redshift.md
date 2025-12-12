---
nav_title: Transferring data to Redshift
article_title: Transferring Data to Redshift
page_order: 8
page_type: tutorial
description: "This how-to article will walk you through how to transfer data from Amazon S3 to Redshift through an Extract, Transform, Load (ETL) process."
tool: Currents

---

# Transferring data to Redshift

> [Amazon Redshift](https://aws.amazon.com/redshift/) is a popular data warehouse that runs on Amazon Web Services alongside Amazon S3. Braze data from Currents is structured for direct transfer to Redshift.

More information on how to transfer data from Amazon S3 to Redshift through an Extract, Transform, Load (ETL) process is available in our Currents examples [GitHub repository](https://github.com/Appboy/currents-examples).

{% alert important %}
This is only one of many options you can choose from when it comes to transferring your data to places that would be most advantageous to you.
{% endalert %}

{% markdown_embed https://raw.githubusercontent.com/Appboy/currents-examples/master/redshift-s3-loader/README.md %}

{% multi_lang_include deprecations/braze_sdk/news_feed.md status="Deprecated" %}