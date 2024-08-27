<!-- 

Use this template for creating metric definitions:

{% if include.metric == "METRIC_NAME glossary" %}
Definition formatted for a glossary.

{% elsif include.metric == "METRIC_NAME table" %}
Definition formatted for the "Description" column of a table.

{% elsif include.metric == "METRIC_NAME list" %}
Definition formatted for a bullet point list.

{% elsif include.metric == "METRIC_NAME sentence" %}
Definition formatted in a complete sentence to insert into a paragraph.

{% endif %}

-->

<!-- AMP Clicks -->

{% if include.metric == "AMP Clicks glossary" %}
The total number of clicks in your AMP HTML email, cumulative of the HTML plaintext, and AMP HTML versions of the email. 

{% elsif include.metric == "AMP Clicks table" %}
The total number of clicks in your AMP HTML email, cumulative of the HTML plaintext, and AMP HTML versions of the email. 

{% elsif include.metric == "AMP Clicks list" %}
The total number of clicks in your AMP HTML email, cumulative of the HTML, plaintext, and AMP HTML versions of the email

{% elsif include.metric == "AMP Clicks sentence" %}
*AMP Clicks* is the total number of clicks in your AMP HTML email, cumulative of the HTML, plaintext, and AMP HTML versions of the email.

{% endif %}

<!-- Audience -->

{% if include.metric == "Audience glossary" %}
The percentage of users who received a particular message. This number is received from Braze.

{% elsif include.metric == "Audience table" %}
The percentage of users who received a particular message. This number is received from Braze.

{% elsif include.metric == "Audience list" %}
The percentage of users who received a particular message. This number is received from Braze

{% elsif include.metric == "Audience sentence" %}
*Audience* is the percentage of users who received a particular message. This number is received from Braze.

{% endif %}