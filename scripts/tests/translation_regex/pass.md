---
nav_title: Regex collection examples
article: Regex Collection Examples
description: "Concrete examples of patterns used in Braze Docs–style pages."
page_order: 0
noindex: true
---

# Overview

This page demonstrates common constructs that your regex collection will ignore or capture. Each item appears in realistic context.

## Liquid raw blocks

Content inside raw blocks should be ignored by Liquid-related patterns:

$${% raw %}$$
$${{ user.email }}$$ should not be captured here.
$${% endraw %}$$

Another raw block:

$${% raw %}$$
$${% if user %}$$Hello$${% endif %}$$
$${% endraw %}$$

## Fenced code blocks

Example with backticks:

$$```python
def greet(name):
    return f"Hello, {name}"
print(greet("Docs"))
```$$

Example with tildes:

$$~~~bash
echo "deploy started"
git status
~~~$$

## Inline code

Use inline code for short snippets like $$`npm run build`$$ or $$`print("ok")`$$.

## Markdown attribute blocks

Paragraph with custom attributes $${: data-role="example" }$$
Centered image style:

![Alt text here we go.$$](some string here)$$$${: style="max-width:80%;"}$$

## HTML tags

$$<div class="note">$$Rendered as HTML, not Markdown.$$</div>$$
$$<br>$$
$$<img src="/assets/img/examples/placeholder.png" alt="placeholder">$$

## Hex color codes

The theme uses primary $$`#0f3a9c`$$ and secondary $$#FFAA00$$ colors.

## Dotted identifiers

Use $$`Braze.iOS.BrazeLocation`$$ for location services.
Compat layer: $$Braze.iOS.BrazeKitCompat$$.

## Markdown reference tokens

An image reference:

![Some alt text here.$$](some string here)$$

And a [markdown link$$](/link/to/something/)$$.

## Curly comment blocks $${#custom-anchor-link}$$

$${# internal note: do not translate this line}$$
$${# lorem ipsum marker #}$$

## Liquid tags

Conditionals and assignments that should be captured:

$${% if user %}$$
Welcome back.
$${% endif %}$$

$${% assign region = "us" %}$$

Loop example:

$${% for item in site.data.menu %}$$
- $${{ item.title }}$$
$${% endfor %}$$

## Liquid outputs

Base URLs and variables:

Link root: $${{site.baseurl}}$$
Learning index: $${{ site.learning_index_name }}$$
Current language: $${{ site.language }}$$

## Table attributes

Table with attributes:

| Key | Code Value | Plain Value |
|-----|------------|-------------|
| Hex | $$`#0f3a9c`$$ | $$#0f3a9c$$ |
| Dotted ID | $$`Braze.iOS.BrazeKitCompat`$$ | $$Braze.iOS.BrazeKitCompat$$ |
$${: .reset-td-br-1 role="presentation" }$$
