{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Logging custom events

You can record custom events in Braze to learn more about your app's usage patterns and to segment your users by their actions in the dashboard.

```dart
braze.logCustomEvent('my_custom_event');
```

You can add metadata about the event by passing a properties object with your custom event.

```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
