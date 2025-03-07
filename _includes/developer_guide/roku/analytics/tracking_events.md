## Add a custom event

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```

### Adding properties

You can add metadata about custom events by passing a properties dictionary with your custom event.

Properties are defined as key-value pairs.  Keys are `String` objects and values can be `String`, or `Integer`.

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
