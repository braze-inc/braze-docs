{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Tracking sessions

The Braze SDK reports session data used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. based on the following session semantics, our SDK generates "start session" and "close session" data points that account for session length and session counts viewable within the Braze dashboard.

To set a user ID or start a session, use the `changeUser` method, which takes a user ID parameter.

```javascript
Braze.changeUser("user_id");
```
