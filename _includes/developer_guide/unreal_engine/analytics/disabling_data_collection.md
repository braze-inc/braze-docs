## Immediately Flushing Data

To manually trigger a data flush and ensure queued user data or events are sent to Braze's servers, use the `RequestImmediateDataFlush()` method on the `UBraze` object.

```cpp
UBraze->RequestImmediateDataFlush();
```
