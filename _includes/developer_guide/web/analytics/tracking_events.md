## Tracking custom events

To track custom events through the Web Braze SDK, use the following method:

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

See the [`logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) documentation for more information.

## Adding properties {#properties-events}

You can optionally add metadata about custom events by passing a properties object with your custom event.

Properties are defined as key-value pairs. Keys are strings and values can be `string`, `numeric`, `boolean`, or [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) objects.

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```

See the [`logCustomEvent()` documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) for more information.

