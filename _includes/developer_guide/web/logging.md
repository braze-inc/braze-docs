## Logging

To quickly enable logging, you can add `?brazeLogging=true` as a parameter to your website URL. Alternatively, you can enable [basic](#basic-logging) or [custom](#custom-logging) logging.

### Basic logging

{% tabs local %}
{% tab before initialization %}
Use `enableLogging` to log basic debugging messages to the javascript console before the SDK is initialized.

```javascript
enableLogging: true
```

Your method should be similar to the following:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab after initialization %}
Use `braze.toggleLogging()` to log basic debugging messages to the javascript console after the SDK is initialized. Your method should be similar to the following:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
Basic logs are visible to all users, so consider disabling, or switch to [`setLogger`](#custom-logging), before releasing your code to production.
{% endalert %}

### Custom logging

Use `setLogger` to log custom debugging messages to the javascript console. Unlike basic logs, these logs are not visible to users.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Replace `STRING` with your message as a single string parameter. Your method should be similar to the following:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```
