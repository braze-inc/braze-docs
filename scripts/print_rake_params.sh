#!/bin/bash
#
# Prints all supported parameters for 'rake', which includes:
# non-english languages, markdown embeds, and partner tiles.
# 
# Usage: ./bdocs rake

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
