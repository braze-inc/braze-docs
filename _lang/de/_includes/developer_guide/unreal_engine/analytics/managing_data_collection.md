## Löschen von zuvor gespeicherten Daten

Um einen Datenflush manuell zu triggern und sicherzustellen, dass Nutzerdaten oder Ereignisse in der Warteschlange an die Braze Server gesendet werden, verwenden Sie die Methode `RequestImmediateDataFlush()` für das Objekt `UBraze`.

```cpp
UBraze->RequestImmediateDataFlush();
```
