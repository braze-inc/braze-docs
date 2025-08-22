#!/bin/bash
#
# Prints all the unique Braze Docs syntax to the terminal. It doesn't include
# standard Markdown syntax, only unique syntax. The full list is found here:
#   https://www.braze.com/docs/contributing/styling_examples
# 
# Usage: ./bdocs syntax

cat << EOF
These are all the supported parameters for 'rake':

# for 'en' language:
rake

# for other languages:
rake de
rake es
rake fr
rake ja
rake ko
rake pt_br

# to render content in '{% markdown_embed %}' tags:
MARKDOWN_API=true rake

# to render tiles on partner landing pages:
PARTNER_API=true rake

# to render both APIs:
MARKDOWN_API=true PARTNER_API=true rake
EOF
