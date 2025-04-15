## Wiping previously-stored data

To manually trigger a data flush and ensure queued user data or events are sent to Braze servers, use the `RequestImmediateDataFlush()` method on the `UBraze` object.

```cpp
UBraze->RequestImmediateDataFlush();
```
