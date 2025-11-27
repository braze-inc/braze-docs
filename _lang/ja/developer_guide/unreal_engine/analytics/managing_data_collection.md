## 過去に保存したデータを消去する

データフラッシュを手動でトリガーし、キューに入れられたユーザーデータやイベントがBrazeサーバーに送信されるようにするには、`UBraze` オブジェクトの`RequestImmediateDataFlush()` メソッドを使用する。

```cpp
UBraze->RequestImmediateDataFlush();
```
