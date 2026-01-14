---
nav_title: Filters
article_title: Liquid Filters
page_order: 3
description: "This reference page lists filters that can be used to reformat static or dynamic content."

---

# Filters

> This reference article provides an overview of filters in Liquid, and covers which filters are supported by Braze. Looking for ideas on how you can use these filters? Check out our [Liquid use case library]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

Filters are how you can modify the output of numbers, strings, variables, and objects in Liquid. You can use filters to reformat static or dynamic text, such as changing a string from lowercase to uppercase or to perform mathematical operations, like addition or division.

{% alert important %}
Braze does not support all Liquid filters from Shopify. This page attempts to outline the Liquid filters that Braze has tested, but it may not be a complete list. Always test your Liquid before sending out any messages. <br><br>If you have any questions about a filter that is not listed here, contact your customer success manager.
{% endalert %}

## Filter syntax

{% raw %}

Filters must be placed within an output tag `{{ }}` and are denoted by a pipe character `|`.

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

In this example, `Big Sale` is a string, and `upcase` is the filter being applied.

### Syntax for multiple filters

You can use multiple filters on one output. They are applied from left to right.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Array filters

Array filters are used to change the output of arrays.

| Filter               | Definition                                                                                                         | Supported |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join](https://shopify.dev/docs/api/liquid/filters/join)          | Joins the elements of an array with the character passed as the parameter. The result is a single string.          | ✅  Yes   |
| [first](https://shopify.dev/docs/api/liquid/filters/first)         | Returns the first element of an array. In a custom attribute array, this is the oldest added value.                | ✅  Yes   |
| [last](https://shopify.dev/docs/api/liquid/filters/last)          | Returns the last element of an array. In a custom attribute array, this is the most recently added value.          | ✅  Yes   |
| [compact](https://shopify.dev/api/liquid/filters/compact)       | Removes any `nil` items from an array.                                                                             | ✅  Yes   |
| [concat](https://shopify.dev/api/liquid/filters/concat)        | Combines an array with another array.                                                                              | ✅  Yes   |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index)         | Returns the item at the specified index location in an array. The first item in an array is referenced with `[0]`. | ⛔  No   |
| [map](https://shopify.dev/api/liquid/filters/map)           | Accepts an array element's attribute as a parameter and creates an array out of each array element's value.        | ✅  Yes   |
| [reverse](https://shopify.dev/api/liquid/filters/reverse)       | Reverses the order of the items in an array.                                                                       | ✅  Yes   |
| [size](https://shopify.dev/api/liquid/filters/size)          | Returns the size of a string (the number of characters) or an array (the number of elements).                      | ✅  Yes   |
| [sort](https://shopify.dev/api/liquid/filters/sort)         | Sorts the elements of an array by a given attribute of an element in the array.                                    | ✅  Yes   |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | Sorts the items in an array in case-insensitive alphabetical order.                                                | ✅  Yes   |
| [uniq](https://shopify.dev/api/liquid/filters/uniq)         | Removes any duplicate instances of elements in an array.                                                           | ✅  Yes   |
| [where](https://shopify.dev/api/liquid/where)        | Filters an array to only include items with a specific property value.                                             | ✅  Yes   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Color filters

[Color filters](https://shopify.dev/api/liquid/filters/color-filters) are not supported in Braze.

## Font filters

[Font filters](https://shopify.dev/api/liquid/filters/font-filters) are not supported in Braze.

## Math filters

Math filters allow you to perform mathematical operations. If you use multiple filters on one output, they will be applied from left to right.

| Filter  | Definition      | Supported |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/abs)        | Returns the absolute value of a number.     | ✅  Yes   |
| [at_most](https://shopify.dev/api/liquid/filters/at_most)    | Limits a number to a maximum value.   | ✅  Yes   |
| [at_least](https://shopify.dev/api/liquid/filters/at_least)   | Limits a number to a minimum value.   | ✅  Yes   |
| [ceil](https://shopify.dev/api/liquid/filters/ceil)       | Rounds an output up to the nearest integer.  | ✅  Yes   |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | Divides an output by a number. The output is rounded down to the nearest integer. Check out the following tip to prevent rounding. | ✅  Yes   |
| [floor](https://shopify.dev/api/liquid/filters/floor)      | Rounds an output down to the nearest integer.        | ✅  Yes   |
| [minus](https://shopify.dev/api/liquid/filters/minus)      | Subtracts a number from an output.          | ✅  Yes   |
| [plus](https://shopify.dev/api/liquid/filters/plus)       | Adds a number to an output.     | ✅  Yes   |
| [round](https://shopify.dev/api/liquid/filters/round)      | Rounds the output to the nearest integer or specified number of decimals.  | ✅  Yes   |
| [times](https://shopify.dev/api/liquid/filters/times)     | Multiplies an output by a number.       | ✅  Yes   |
| [modulo](https://shopify.dev/api/liquid/filters/modulo)    | Divides an output by a number and returns the remainder.   | ✅  Yes   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
When dividing integers (whole numbers) by integers in Liquid, if the answer is a float (number with a decimal), Liquid will automatically round down to the nearest integer. However, dividing integers by floats will always give you a float. That means you can turn your integers into a float (1.0, 2.0, 3.0) to return a float.
{% raw %}
<br><br>For example,`{{15 | divided_by: 2}}` will output `7`, whereas  `{{15 | divided_by: 2.0}}` will output `7.5`.
{% endraw %}
{% endalert %}

### Mathematical operations with custom attributes

Keep in mind that you can't perform mathematical operations between two custom attributes.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

This example wouldn't work because you can't reference multiple custom attributes in one line of Liquid. Instead, you would need to assign a variable to at least one of these values before the math functions take place. Adding two custom attributes together would require two lines of Liquid:

1. One to assign the custom attribute to a variable,
2. One to perform the addition.

#### Use case: Calculate current balance

Let's say we want to calculate a user's current balance by adding their gift card balance and rewards balance.

1. Use the `assign` tag to substitute the custom attribute of `current_rewards_balance` with the term "balance". This means that you now have a variable named `balance`, which you can manipulate.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2. Use the `plus` filter to combine each user's gift card balance with their rewards balance, signified by the `{{balance}}` object. 
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Money filters

If you're updating a user on their purchase, an account balance, or anything regarding money, you should use money filters. Money filters ensure that your decimals are in the proper place and that no piece of your update is lost (like that pesky `0` at the end).

| Filter         | Definition          | Supported |
| :--------------- | :--------------- | :-------- |
| [money](https://shopify.dev/api/liquid/filters/money)      | Formats numbers to ensure that decimals are in the proper place, and zeros are not dropped off the end of any numbers.   | ✅  Yes   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency)    | Formats numbers with the currency symbol.     | ⛔  No    |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency)     | Formats numbers without the currency symbol.      | ⛔  No    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
To properly format a number with the `money` filter, remove any commas in the number and add the `plus: 0` filter before the `money` filter. For example, see the following Liquid:<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Shopify money filter versus Braze money filter

{% alert warning %}
The behavior of the Shopify `money` filter differs from how it's used in Braze. Refer to the following examples for an accurate depiction of the expected behavior.
{% endalert %}

{% raw %}
In the event you are inputting a custom attribute (like `account_balance`), you should always use the `money` filter to put your decimals in the proper place and prevent zeros from dropping off the end of any numbers:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| WITH THE MONEY FILTER                       | WITHOUT THE MONEY FILTER                    |
| :------------------------------------------ | :------------------------------------------ |
| ![With money filter]({% image_buster /assets/img/with_money_filter.png %})                     | ![Without money filter]({% image_buster /assets/img/without_money_filter.png %})                  |
| Where `account_balance` is input at `17.8`. | Where `account_balance` is input at `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The `money` filter in Braze differs from Shopify because it doesn't automatically apply decimal points according to a preset setting. For example, take the following scenario where `rewards_redeemed` contains a value of `145`:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

According to Shopify's [money](https://shopify.dev/api/liquid/filters/money) filter, this should have an output of `$1.45`, however in Braze, this will have an output of `$145.00`. As a workaround, we can use the `divided_by` filter to manipulate the number into a decimal, before applying the money filter:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## String filters

String filters are used to manipulate the outputs and variables of strings. Strings are a combination of alphanumeric characters and must be wrapped in straight quotes.

{% alert note %}
Straight quotes are different from curly quotes in Liquid. Be careful when copying and pasting Liquid from a text editor into Braze, as curly quotes will cause errors with your Liquid. If you're writing your Liquid directly into Braze, straight quotes will be applied automatically.
{% endalert %}

| Filter          | Description     | Supported |
| :--------------- | ------------- | --------- |
| [append](https://shopify.dev/api/liquid/filters/append)     | Appends characters to a string.           | ✅  Yes   |
| [camelize](https://shopify.dev/docs/api/liquid/filters/camelize)     | Converts a string into CamelCase.             | ⛔  No    |
| [capitalize](https://shopify.dev/api/liquid/filters/capitalize)     | Capitalizes the first word in a string and downcases the remaining characters.         | ✅  Yes   |
| [downcase](https://shopify.dev/api/liquid/filters/downcase)      | Converts a string into lowercase.         | ✅  Yes   |
| [escape](https://shopify.dev/api/liquid/filters/escape)    | Escapes a string.             | ✅  Yes   |
| [handleize](https://shopify.dev/api/liquid/filters/handleize)        | Formats a string into a handle.        | ⛔  No    |
| [md5](https://shopify.dev/api/liquid/filters/md5)    | Converts a string into an MD5 hash. Refer to [Encoding Filters]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters) for more.   | ✅  Yes   |
| [sha1](https://shopify.dev/api/liquid/filters/sha1)    | Converts a string into a SHA-1 hash. Refer to [Encoding Filters]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters) for more.  | ✅  Yes   |
| hmac_sha1_hex<br>(previously [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | Converts a string into a SHA-1 hash using a hash message authentication code (HMAC). Pass the secret key for the message as a parameter to the filter. Refer to [Encoding Filters]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters) for more. | ✅  Yes   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256)    | Converts a string into a SHA-256 hash using a hash message authentication code (HMAC). Pass the secret key for the message as a parameter to the filter.       | ✅  Yes   |
| hmac_sha512 | Converts a string into a SHA-512 hash using a hash message authentication code (HMAC). Pass the secret key for the message as a parameter to the filter. | ✅  Yes  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br)     | Inserts a `<br>` line break HTML tag in front of each line break in a string.        | ✅  Yes   |
| [pluralize](https://shopify.dev/api/liquid/filters/pluralize)   | Outputs the singular or plural version of an English string based on the value of a number.      | ⛔  No    |
| [prepend](https://shopify.dev/api/liquid/filters/prepend)     | Prepends characters to a string.      | ✅  Yes   |
| [remove](https://shopify.dev/api/liquid/filters/remove)      | Removes all occurrences of a substring from a string.       | ✅  Yes   |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first)    | Removes only the first occurrence of a substring from a string.      | ✅  Yes   |
| [replace](https://shopify.dev/api/liquid/filters/replace)        | Replaces all occurrences of a string with a substring.   | ✅  Yes   |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first)        | Replaces the first occurrence of a string with a substring.      | ✅  Yes   |
| [slice](https://shopify.dev/api/liquid/filters/slice)       | The slice filter returns a substring, starting at the specified index.       | ✅  Yes   |
| [split](https://shopify.dev/api/liquid/filters/split)  | The split filter takes on a substring as a parameter. The substring is used as a delimiter to divide a string into an array.            | ✅  Yes   |
| [strip](https://shopify.dev/api/liquid/filters/strip)   | Strips tabs, spaces, and newlines (all whitespace) from the left and right side of a string.                                                                                                    | ✅  Yes   |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip)     | Strips tabs, spaces, and newlines (all whitespace) from the left side of a string.    | ⛔  No    |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip)             | Strips tabs, spaces, and newlines (all whitespace) from the right side of a string.          | ⛔  No    |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html)         | Strips all HTML tags from a string.        | ✅  Yes   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines)  | Removes any line breaks/newlines from a string.        | ✅  Yes   |
| [truncate](https://shopify.dev/api/liquid/filters/truncate)    | Truncates a string down to the number of characters passed as the first parameter. An ellipsis (...) is appended to the truncated string and is included in the character count.    | ✅  Yes   |
| [truncatewords](https://shopify.dev/api/liquid/filters/truncatewords)   | Truncates a string down to the number of words passed as the first parameter. An ellipsis (...) is appended to the truncated string.    | ✅  Yes   |
| [upcase](https://shopify.dev/api/liquid/filters/upcase)   | Converts a string into uppercase.      | ✅  Yes   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Additional filters

The following general filters serve many purposes, including formatting or converting content.

| Filter                | Description                                                                                                                      | Supported |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date](https://shopify.dev/api/liquid/filters/date)           | Converts a timestamp into another date format. Refer to [Date Filter](#date-filter) for more.         | ✅  Yes   |
| [default](https://shopify.dev/api/liquid/filters/default)        | Sets a default value for any variable with no assigned value. Can be used with strings, arrays, and hashes.      | ✅  Yes   |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | Formats an address to print the elements of the address in order according to their locale.        | ⛔  No    |
| [highlight](https://shopify.dev/api/liquid/filters/highlight)      | Wraps words inside search results with an HTML `<strong>` tag with the class highlight if it matches the submitted search terms. | ⛔  No    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

You can find more supported filters, such as encoding and URL filters, on our [Advanced Filters]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/) page.

### Date filter {#date-filter}

The `date` filter can be used to convert a timestamp into a different date format. You can pass in parameters to the `date` filter to reformat the timestamp. For examples of these parameters, refer to [strfti.me](http://www.strfti.me/).

For example, let's say that the value of `date_attribute` is the timestamp `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

In addition to the `strftime` formatting options, Braze also supports converting a timestamp to Unix time with the `%s` date filter. For example, to get the `date_attribute` in Unix time:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}