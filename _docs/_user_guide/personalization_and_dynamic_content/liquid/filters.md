---
nav_title: Filters
article_title: Liquid Filters
page_order: 3
description: "Filters can be used to reformat static or dynamic content. This reference article covers the Liquid filters supported by Braze."

---

# Filters

> This reference article provides an overview of filters in liquid, and covers which filters are supported by braze. Looking for ideas on how you can use these filters? Check out our [liquid use case library]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

{% raw %}

Filters are how you can modify the output of numbers, strings, variables, and objects in Liquid. You can use filters to reformat static or dynamic text, such as changing a string from lowercase to uppercase or to perform mathematical operations, like addition or division.

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

In the example above, `Big Sale` is a string, and `upcase` is the filter being applied.

You can use multiple filters on one output. They are applied from left to right.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: “BIG” }}
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

{% alert important %}
Braze does not support all Liquid filters from Shopify. This page attempts to outline the Liquid filters that Braze has tested, but it may not be a complete list. Always test your Liquid before sending out any messages. 
<br><br>If you have any questions about a filter that is not listed here, please contact Support or reach out to your Customer Success Manager.
{% endalert %}

## Array filters

Array filters are used to change the output of arrays.

| Filter         | Definition                                                                                                         | Supported |
| :------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join][1.1]    | Joins the elements of an array with the character passed as the parameter. The result is a single string.          | ✅  Yes   |
| [first][1.2]   | Returns the first element of an array. In a custom attribute array, this is the most recently added value.         | ✅  Yes   |
| [last][1.3]    | Returns the last element of an array. In a custom attribute array, this is the oldest added value.                 | ✅  Yes   |
| [concat][1.4]  | Combines an array with another array.                                                                              | ⛔  No    |
| [index][1.5]   | Returns the item at the specified index location in an array. The first item in an array is referenced with `[0]`. | ✅  Yes   |
| [map][1.6]     | Accepts an array element's attribute as a parameter and creates an array out of each array element's value.        | ✅  Yes   |
| [reverse][1.7] | Reverses the order of the items in an array.                                                                       | ✅  Yes   |
| [size][1.8]    | Returns the size of a string (the number of characters) or an array (the number of elements).                      | ✅  Yes   |
| [sort][1.9]    | Sorts the elements of an array by a given attribute of an element in the array.                                    | ✅  Yes   |
| [uniq][1.10]   | Removes any duplicate instances of elements in an array.                                                           | ✅  Yes   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Color filters

[Color filters][2.1] are not supported in Braze.

## Font filters

[Font filters][3.1] are not supported in Braze.

## Math filters

Math filters allow you to perform mathematical operations. Remember—if you use multiple filters on one output, they are applied from left to right.

| Filter            | Definition                                                                                                                     | Supported |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [abs][4.1]        | Returns the absolute value of a number.                                                                                        | ✅  Yes   |
| [at_most][4.2]    | Limits a number to a maximum value.                                                                                            | ⛔  No    |
| [at_least][4.3]   | Limits a number to a minimum value.                                                                                            | ⛔  No    |
| [ceil][4.4]       | Rounds an output up to the nearest integer.                                                                                    | ✅  Yes   |
| [divided_by][4.5] | Divides an output by a number. The output is rounded down to the nearest integer. Check out the tip below to prevent rounding. | ✅  Yes   |
| [floor][4.6]      | Rounds an output down to the nearest integer.                                                                                  | ✅  Yes   |
| [minus][4.7]      | Subtracts a number from an output.                                                                                             | ✅  Yes   |
| [plus][4.8]       | Adds a number to an output.                                                                                                    | ✅  Yes   |
| [round][4.9]      | Rounds the output to the nearest integer or specified number of decimals.                                                      | ✅  Yes   |
| [times][4.10]     | Multiplies an output by a number.                                                                                              | ✅  Yes   |
| [modulo][4.11]    | Divides an output by a number and returns the remainder.                                                                       | ✅  Yes   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
When dividing integers (whole numbers) by integers in Liquid, if the answer is a float (number with a decimal), Liquid will automatically round down to the nearest integer. However, dividing integers by floats will always give you a float. That means you can turn your integers into a float (1.0, 2.0, 3.0) to return a float.
{% raw %}
<br><br>For example,`{{15 | divided_by: 2}}` will output `7`, whereas  `{{15 | divided_by: 2.0}}` will output `7.5`.
{% endraw %}
{% endalert %}

### Mathematical operations with custom attributes

Keep in mind that you can’t perform mathematical operations between two custom attributes.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

This example wouldn’t work because you can’t reference multiple custom attributes in one line of Liquid. Instead, you would need to assign a variable to at least one of these values before the math functions take place. Adding two custom attributes together would require two lines of Liquid:

1. One to assign the custom attribute to a variable,
2. One to perform the addition.

For example, let’s say we want to calculate a user’s current balance by adding their gift card balance and rewards balance. First, use the `assign` tag to substitute the custom attribute of `current_rewards_balance` with the term “balance”. This means that you now have a variable named `balance`, which you can manipulate.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

Next, use the `plus` filter to combine each user’s gift card balance with their rewards balance, signified by the `{{balance}}` object. 
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

If you’re updating a user on their purchase, an account balance, or anything regarding money, you should use money filters. Money filters ensure that your decimals are in the proper place and that no piece of your update is lost (like that pesky `0` at the end).

| Filter                              | Definition                                                                                                             | Supported |
| :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :-------- |
| [money][5.1]                        | Formats numbers to ensure that decimals are in the proper place, and zeros are not dropped off the end of any numbers. | ✅  Yes   |
| [money_with_currency][5.2]          | Formats numbers with the currency symbol. | ✅  Yes   |
| [money_without_trailing_zeros][5.3] | Formats numbers to exclude the decimal separator (either `.` or `,`) and trailing zeros. If there are no trailing zeros, then this filter behaves like the `money` filter. | ✅  Yes   |
| [money_without_currency][5.4]       | Formats numbers without the currency symbol.                                                       | ⛔  No    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Shopify money filter vs Braze money filter

{% alert warning %}
The behavior of the Shopify `money` filter differs from how it is used in Braze. Refer to the examples below for an accurate depication of the expected behavior.
{% endalert %}

{% raw %}
In the event you are inputting a custom attribute (like `account_balance`), you should always use the `money` filter to ensure that your decimals are in the proper place, and zeros are not dropped off the end of any numbers, as shown below:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| WITH THE MONEY FILTER                       | WITHOUT THE MONEY FILTER                    |
| :------------------------------------------ | :------------------------------------------ |
| ![With money filter][1]                     | ![Without money filter][2]                  |
| Where `account_balance` is input at `17.8`. | Where `account_balance` is input at `17.8`. |
{: .reset-td-br-1 .reset-td-br-2}

The `money` filter in Braze differs from Shopify in that it does not automatically apply decimal points according to a preset setting. For example, take the following scenario where `rewards_redeemed` contains a value of `145`:

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

According to Shopify's [money][5.1] filter, this should have an output of `$1.45`, however in Braze, this will have an output of `$145.00`. As a workaround, we can use the `divided_by` filter to manipulate the number into a decimal, before applying the money filter:

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
Straight quotes are different from curly quotes in Liquid. Be careful when copying and pasting Liquid from a text editor into Braze, as curly quotes will cause errors with your Liquid. If you are writing your Liquid directly into Braze, straight quotes will be applied automatically.
{% endalert %}

| Filter                                           | Description                     | Supported |
| :----------------------------------------------- | ------------------------------- | --------- |
| [append][6.1]                                    | Appends characters to a string. | ✅  Yes   |
| [camelcase][6.2]                                 | Converts a string into CamelCase. | ⛔  No    |
| [capitalize][6.3]                                | Capitalizes the first word in a string.   | ✅  Yes   |
| [downcase][6.4]                                  | Converts a string into lowercase. | ✅  Yes   |
| [escape][6.5]                                    | Escapes a string.  | ✅  Yes   |
| [handle/handleize][6.6]                          | Formats a string into a handle.     | ⛔  No    |
| [md5][6.7]                                       | Converts a string into an MD5 hash. Refer to [Encoding Filters][3] for more. | ✅  Yes   |
| [sha1][6.8]                                      | Converts a string into a SHA-1 hash. Refer to [Encoding Filters][3] for more. | ✅  Yes   |
| hmac_sha1_hex<br>(previously [hmac_sha_1][6.10]) | Converts a string into a SHA-1 hash using a hash message authentication code (HMAC). Pass the secret key for the message as a parameter to the filter. Refer to [Encoding Filters][3] for more. | ✅  Yes   |
| [hmac_sha256][6.11]                              | Converts a string into a SHA-256 hash using a hash message authentication code (HMAC). Pass the secret key for the message as a parameter to the filter.| ✅  Yes   |
| [newline_to_br][6.12]                            | Inserts a `<br>` linebreak HTML tag in front of each line break in a string. | ✅  Yes   |
| [pluralize][6.13]                                | Outputs the singular or plural version of an English string based on the value of a number. | ⛔  No    |
| [prepend][6.14]                                  | Prepends characters to a string.  | ✅  Yes   |
| [remove][6.15]                                   | Removes all occurrences of a substring from a string. | ✅  Yes   |
| [remove_first][6.16]                             | Removes only the first occurrence of a substring from a string. | ✅  Yes   |
| [replace][6.17]                                  | Replaces all occurrences of a string with a substring.  | ✅  Yes   |
| [replace_first][6.18]                            | Replaces the first occurrence of a string with a substring.  | ✅  Yes   |
| [slice][6.19]                                    | The slice filter returns a substring, starting at the specified index. | ✅  Yes   |
| [split][6.20]                                    | The split filter takes on a substring as a parameter. The substring is used as a delimiter to divide a string into an array.   | ✅  Yes   |
| [strip][6.21]                                    | Strips tabs, spaces, and newlines (all whitespace) from the left and right side of a string. | ✅  Yes   |
| [lstrip][6.22]                                   | Strips tabs, spaces, and newlines (all whitespace) from the left side of a string. | ⛔  No    |
| [rstrip][6.23]                                   | Strips tabs, spaces, and newlines (all whitespace) from the right side of a string. | ⛔  No    |
| [strip_html][6.24]                               | Strips all HTML tags from a string. | ✅  Yes   |
| [strip_newlines][6.25]                           | Removes any line breaks/newlines from a string. | ✅  Yes   |
| [truncate][6.26]                                 | Truncates a string down to the number of characters passed as the first parameter. An ellipsis (...) is appended to the truncated string and is included in the character count. | ✅  Yes   |
| [truncatewords][6.27]                            | Truncates a string down to the number of words passed as the first parameter. An ellipsis (...) is appended to the truncated string. | ✅  Yes   |
| [upcase][6.28]                                   | Converts a string into uppercase. | ✅  Yes   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Additional filters

The following general filters serve many different purposes, including formatting or converting content.

| Filter         | Description                                                                         | Supported |
| -------------- | ----------------------------------------------------------------------------------- | :-------- |
| [date][7.1]           | Converts a timestamp into another date format. Refer to [Date Filter](#date-filter) below for more. | ✅  Yes   |
| [default][7.2]        | Sets a default value for any variable with no assigned value. Can be used with strings, arrays, and hashes. | ✅  Yes   |
| [format_address][7.3] | Formats an address to print the elements of the address in order according to their locale. | ⛔  No    |
| [highlight][7.4]      | Wraps words inside search results with an HTML `<strong>` tag with the class highlight if it matches the submitted search terms. | ⛔  No    |
| time_zone      | Refer to [Time Zone Filter](#time-zone-filter) below for more. | ✅  Yes   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

You can find more supported filters, such as encoding and URL filters, on our [Advanced Filters]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/) page.

### Date filter {#date-filter}

The `date` filter can be used to convert a timestamp into a different date format. You can pass in parameters to the `date` filter to reformat the timestamp. For examples of these parameters, refer to [strfti.me](http://www.strfti.me/).

For example, let’s say that the value of `date_attribute` is the timestamp `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b','d'}}
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

### Time zone filter {#time-zone-filter}

{% raw %}
In addition to the filters that you’ll find listed in Shopify’s documentation, Braze also supports the `time_zone` filter.

The `time_zone` filter takes a time, a time zone, and a date format and returns the time in that time zone in the specified date format. For example, let’s say that the value of `{{custom_attribute.$date_attribute}}}` is `2021-08-04 9:00:00 UTC`:
{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | time_zone: 'America/Los_Angeles' | date: '%a %b %e %T' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Wed August 4 2:00:00
```
{% endraw %}
{% endtab %}
{% endtabs %}

You can also use the reserved variable `now` to access the current date and time for manipulation.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ 'now' | date: '%Y-%m-%d %H:%M:%S' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
2021-08-04 18:13:13
```
{% endraw %}
{% endtab %}
{% endtabs %}


[1.1]: https://shopify.dev/api/liquid/filters/array-filters#join
[1.2]: https://shopify.dev/api/liquid/filters/array-filters#first
[1.3]: https://shopify.dev/api/liquid/filters/array-filters#last
[1.4]: https://shopify.dev/api/liquid/filters/array-filters#concat
[1.5]: https://shopify.dev/api/liquid/filters/array-filters#index
[1.6]: https://shopify.dev/api/liquid/filters/array-filters#map
[1.7]: https://shopify.dev/api/liquid/filters/array-filters#reverse
[1.8]: https://shopify.dev/api/liquid/filters/array-filters#size
[1.9]: https://shopify.dev/api/liquid/filters/array-filters#sort
[1.10]: https://shopify.dev/api/liquid/filters/array-filters#uniq

[2.1]: https://shopify.dev/api/liquid/filters/color-filters
[3.1]: https://shopify.dev/api/liquid/filters/font-filters

[4.1]: https://shopify.dev/api/liquid/filters/math-filters#abs
[4.2]: https://shopify.dev/api/liquid/filters/math-filters#at_most
[4.3]: https://shopify.dev/api/liquid/filters/math-filters#at_least
[4.4]: https://shopify.dev/api/liquid/filters/math-filters#ceil
[4.5]: https://shopify.dev/api/liquid/filters/math-filters#divided_by
[4.6]: https://shopify.dev/api/liquid/filters/math-filters#floor
[4.7]: https://shopify.dev/api/liquid/filters/math-filters#minus
[4.8]: https://shopify.dev/api/liquid/filters/math-filters#plus
[4.9]: https://shopify.dev/api/liquid/filters/math-filters#round
[4.10]: https://shopify.dev/api/liquid/filters/math-filters#times
[4.11]: https://shopify.dev/api/liquid/filters/math-filters#modulo

[5.1]: https://shopify.dev/api/liquid/filters/money-filters#money
[5.2]: https://shopify.dev/api/liquid/filters/money-filters#money_with_currency
[5.3]: https://shopify.dev/api/liquid/filters/money-filters#money_without_trailing_zeros
[5.4]: https://shopify.dev/api/liquid/filters/money-filters#money_without_currency

[6.1]: https://shopify.dev/api/liquid/filters/string-filters#append
[6.2]: https://shopify.dev/api/liquid/filters/string-filters#camelcase
[6.3]: https://shopify.dev/api/liquid/filters/string-filters#capitalize
[6.4]: https://shopify.dev/api/liquid/filters/string-filters#downcase
[6.5]: https://shopify.dev/api/liquid/filters/string-filters#escape
[6.6]: https://shopify.dev/api/liquid/filters/string-filters#handle-handleize
[6.7]: https://shopify.dev/api/liquid/filters/string-filters#md5
[6.8]: https://shopify.dev/api/liquid/filters/string-filters#sha1
[6.10]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1
[6.11]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha256
[6.12]: https://shopify.dev/api/liquid/filters/string-filters#newline_to_br
[6.13]: https://shopify.dev/api/liquid/filters/string-filters#pluralize
[6.14]: https://shopify.dev/api/liquid/filters/string-filters#prepend
[6.15]: https://shopify.dev/api/liquid/filters/string-filters#remove
[6.16]: https://shopify.dev/api/liquid/filters/string-filters#remove_first
[6.17]: https://shopify.dev/api/liquid/filters/string-filters#replace
[6.18]: https://shopify.dev/api/liquid/filters/string-filters#replace_first
[6.19]: https://shopify.dev/api/liquid/filters/string-filters#slice
[6.20]: https://shopify.dev/api/liquid/filters/string-filters#split
[6.21]: https://shopify.dev/api/liquid/filters/string-filters#strip
[6.22]: https://shopify.dev/api/liquid/filters/string-filters#lstrip
[6.23]: https://shopify.dev/api/liquid/filters/string-filters#rstrip
[6.24]: https://shopify.dev/api/liquid/filters/string-filters#strip_html
[6.25]: https://shopify.dev/api/liquid/filters/string-filters#strip_newlines
[6.26]: https://shopify.dev/api/liquid/filters/string-filters#truncate
[6.27]: https://shopify.dev/api/liquid/filters/string-filters#truncatewords
[6.28]: https://shopify.dev/api/liquid/filters/string-filters#upcase

[7.1]: https://shopify.dev/api/liquid/filters/additional-filters#date
[7.2]: https://shopify.dev/api/liquid/filters/additional-filters#default
[7.3]: https://shopify.dev/api/liquid/filters/additional-filters#format_address
[7.4]: https://shopify.dev/api/liquid/filters/additional-filters#highlight


[1]: {% image_buster /assets/img/with_money_filter.png %}
[2]: {% image_buster /assets/img/without_money_filter.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters
