---
nav_title: Tutorial 1
article_title: Developer Tutorials
page_order: 5.6
description: "Interactive, step-by-step coding tutorials using dynamic, scrollable code."
layout: dev_guide
---

{% tabs %}
{% tab Android %}
{% scrolly %}

```js
const houses = ["Stark", "Lannister", "Baratheon", "Targaryen"];

const winner = houses[Math.floor(Math.random() * houses.length)];
console.log(`Iron Throne: ${winner}`);

const clash = () => {
  const winner = houses[Math.floor(Math.random() * houses.length)];
  return `${winner} wins the battle!`;
};
console.log(clash());

if (winner == "me") {
  console.log("Woohoo");
} else {
  console.log("That sucks");
}
```

!!step
lines=1

#### First step

Some instructions on what this `line` does, and how to use it.

- item 1
- item 2

!!step
lines=3-4

#### Second step

Some instructions on what these lines do, and how to use them.

```js
var x = "hello";
console.log(x);
```

!!step
lines=6-9

## Step 3

Highlighting just the decision logic, lines 6–9.

!!step
lines=10,12-16
Highlighting just the decision logic, line 10.

{% endscrolly %}

{% endtab %}
{% tab iOS %}

{% scrolly %}

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

!!step
lines=1
Some instructions on what this `line` does, and how to use it.

!!step
lines=3-4
Some instructions on what these lines do, and how to use them.

!!step
lines=6-9
Highlighting just the decision logic, lines 6–9.

!!step
lines=10
No lines!

{% endscrolly %}

{% endtab %}

{% endtabs %}
