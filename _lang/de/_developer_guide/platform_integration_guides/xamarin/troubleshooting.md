---
nav_title: Fehlersuche
article_title: Fehlerbehebung für Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 6
description: "Dieser Artikel behandelt die Fehlerbehebung für iOS und Android auf der Xamarin-Plattform."

---

# Fehlersuche

> Dieser Artikel enthält mehrere Szenarien zur Fehlerbehebung in Xamarin.

## Android

### Eine Push-Benachrichtigung wird nicht angezeigt, nachdem die App über den Task Switcher geschlossen wurde

Wenn Sie feststellen, dass Push-Benachrichtigungen nicht mehr erscheinen, nachdem Sie die App über den Task Switcher geschlossen haben, befindet sich Ihre App wahrscheinlich im Debug-Modus. Xamarin fügt im Debug-Modus ein Scaffolding  hinzu, das verhindert, dass Apps Push erhalten, nachdem der zugehörige Prozess beendet wurde. Wenn Sie die App im Release-Modus ausführen, sollten Sie die Push-Nachricht auch sehen, wenn die App über den Task Switcher geschlossen wurde.

### Angepasste Benachrichtigungs-Factory ist nicht korrekt eingestellt

Die angepasste Benachrichtigungs-Factory (und alle Delegaten) müssen [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) erweitern, damit sie über die Grenzen von C# und Java hinweg korrekt funktionieren. Weitere Informationen finden Sie unter [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) zur Implementierung von Java-Schnittstellen.

