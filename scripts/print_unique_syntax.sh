#!/bin/bash
#
# Prints all the unique Braze Docs syntax to the terminal. It doesn't include
# standard Markdown syntax, only unique syntax. The full list is found here:
#   https://www.braze.com/docs/contributing/styling_examples
# 
# Usage: ./bdocs syntax

cat << EOF
This is all of the unique Markdown syntax supported by Braze Docs.

ALERTS
  {% alert TYPE %}
  {% endalert %}

IMAGE LINK
  ![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})

IMAGE RESIZING
  {: style="max-width:NUMBER%;"}

INCLUDES
  {% multi_lang_include PATH_TO_INCLUDE %}

LIQUID RAW TAGS
  {% raw %}{% endraw %}

TABS
  {% tabs %}
  {% tab NAME %}
  {% endtab %}
  {% endtabs %}

SUBTABS
  {% subtabs %}
  {% subtab NAME %}
  {% endsubtab %}
  {% endsubtabs %}

TABLE WORD-BREAK
  {: .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM role="presentation"}
EOF
