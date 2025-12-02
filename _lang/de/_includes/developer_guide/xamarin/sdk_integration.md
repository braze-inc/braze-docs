## Integration des .NET MAUI SDK

Durch die Integration des Braze .NET MAUI SDK erhalten Sie grundlegende Analytics-Funktionen sowie funktionierende In-App-Nachrichten, mit denen Sie Ihre Nutzer:innen einbinden können. 

### Voraussetzungen

Bevor Sie das .NET MAUI Braze SDK integrieren können, müssen Sie sicherstellen, dass Sie die folgenden Anforderungen erfüllen:

- Ab `version 3.0.0` erfordert dieses SDK die Verwendung von .NET 6+ und entfernt die Unterstützung für Projekte, die das Xamarin-Framework verwenden.
- Ab `version 4.0.0` hat dieses SDK die Unterstützung für Xamarin und Xamarin.Forms eingestellt und Unterstützung für .NET MAUI hinzugefügt. Siehe [Microsofts Richtlinie](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin) über das Supportende für Xamarin.

### Schritt 1: .NET MAUI-Binding

{% tabs %}
{% tab android %}
Ein .NET MAUI-Binding ist eine Möglichkeit, native Bibliotheken in .NET MAUI-Apps zu verwenden. Die Implementierung des Bindings besteht darin, eine C#-Schnittstelle zur Bibliothek zu erstellen und diese Schnittstelle dann in Ihrer Anwendung zu verwenden.  Siehe die [Xamarin-Dokumentation](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/). Es gibt zwei Möglichkeiten, das Braze SDK Binding einzuschließen: mit NuGet oder durch Kompilieren aus der Quelle.

{% subtabs local %}
{% subtab NuGet %}
Die einfachste Methode der Integration besteht darin, sich das Braze SDK aus dem zentralen [NuGet.org](https://www.nuget.org/)-Repository zu holen. Klicken Sie in der Seitenleiste von Visual Studio mit der rechten Maustaste auf den Ordner `Packages` und dann auf `Add Packages...`.  Suchen Sie nach "Braze" und installieren Sie das Paket [`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/) in Ihr Projekt.
{% endsubtab %}

{% subtab Source %}
Die zweite Methode besteht darin, die [Binding-Quelle](https://github.com/braze-inc/braze-xamarin-sdk) einzubeziehen. Unter [`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding) finden Sie den Quellcode unserer Bindung. Wenn Sie in Ihrer Xamarin-Anwendung eine Projektreferenz auf ```BrazeAndroidBinding.csproj``` hinzufügen, wird die Bindung mit Ihrem Projekt erstellt und Sie erhalten Zugriff auf das Braze Android SDK.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert important %}
Die iOS-Bindings für .NET MAUI SDK Version 4.0.0 und höher verwenden das [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/), frühere Versionen hingegen das [ältere AppboyKit SDK](https://github.com/Appboy/Appboy-ios-sdk).
{% endalert %}

Ein .NET MAUI-Binding ist eine Möglichkeit, native Bibliotheken in .NET MAUI-Apps zu verwenden.  Die Implementierung eines Bindings besteht darin, eine C#-Schnittstelle zur Bibliothek zu erstellen und diese Schnittstelle dann in Ihrer Anwendung zu verwenden. Es gibt zwei Möglichkeiten, das Braze SDK Binding einzuschließen: mit NuGet oder durch Kompilieren aus der Quelle.

{% subtabs local %}
{% subtab NuGet %}
Die einfachste Methode der Integration besteht darin, sich das Braze SDK aus dem zentralen [NuGet.org](https://www.nuget.org/)-Repository zu holen. Klicken Sie in der Seitenleiste von Visual Studio mit der rechten Maustaste auf den Ordner `Packages` und dann auf `Add Packages...`.  Suchen Sie nach 'Braze' und installieren Sie die neuesten .NET MAUI iOS NuGet Pakete: [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit), [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI) und [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation) in Ihr Projekt.

Wir stellen auch die Pakete der kompatiblen Bibliotheken – [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat) und [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat) – zur Verfügung, um Ihnen die Migration zu .NET MAUI zu erleichtern.
{% endsubtab %}

{% subtab Source %}
Die zweite Methode besteht darin, die [Binding-Quelle](https://github.com/braze-inc/braze-xamarin-sdk) einzubeziehen. Unter [`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding) finden Sie den Quellcode unserer Bindung. Wenn Sie in Ihrer Xamarin-Anwendung eine Projektreferenz auf ```BrazeiOSBinding.csproj``` hinzufügen, wird die Bindung mit Ihrem Projekt erstellt und Sie erhalten Zugriff auf das Braze iOS SDK. Stellen Sie sicher, dass `BrazeiOSBinding.csproj` im Ordner "Referenzieren" Ihres Projekts angezeigt wird.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Schritt 2: Konfigurieren Sie Ihre Braze-Instanz

{% tabs %}
{% tab android %}
#### Schritt 2.1: Konfigurieren Sie das Braze SDK in Braze.xml

Nachdem die Bibliotheken nun integriert wurden, müssen Sie eine `Braze.xml`-Datei im `Resources/values`-Ordner Ihres Projekts erstellen. Der Inhalt dieser Datei sollte dem folgenden Code-Snippet ähneln:

{% alert note %}
Stellen Sie sicher, dass Sie `YOUR_API_KEY` durch den API-Schlüssel ersetzen, den Sie unter **Einstellungen** > **API-Schlüssel** im Braze-Dashboard finden.
<br><br>
Wenn Sie die [ältere Navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) verwenden, finden Sie API-Schlüssel unter **Entwicklungskonsole** > **API-Einstellungen**...
{% endalert %}

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
    <string translatable="false" name="com_braze_api_key">YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
  </resources>
```
Wenn Sie den Quellcode des Bindings manuell einbinden, entfernen Sie `<item>NUGET</item>` aus Ihrem Code.

{% alert tip %}
Ein Beispiel für `Braze.xml` sehen Sie in unserer [Android MAUI App](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml).
{% endalert %}

#### Schritt 2.2: Erforderliche Berechtigungen zum Android-Manifest hinzufügen

Nachdem Sie den API-Schlüssel hinzugefügt haben, müssen Sie die folgenden Berechtigungen zur `AndroidManifest.xml`-Datei hinzufügen:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
Ein Beispiel für Ihre `AndroidManifest.xml` finden Sie in der [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml) Beispielanwendung.

#### Schritt 2.3: Tracking von Nutzer:innen-Sitzungen und Registrierung für In-App-Nachrichten

Um das Tracking von Nutzersitzungen zu aktivieren und Ihre App für In-App-Nachrichten zu registrieren, fügen Sie den folgenden Aufruf in die `OnCreate()`-Lebenszyklus-Methode der Klasse `Application` in Ihrer App ein:

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab ios %}
Wenn Sie Ihre Braze-Instanz einrichten, fügen Sie das folgende Snippet hinzu, um Ihre Instanz zu konfigurieren:

{% alert note %}
Stellen Sie sicher, dass Sie `YOUR_API_KEY` durch den API-Schlüssel ersetzen, den Sie unter **Einstellungen** > **API-Schlüssel** im Braze-Dashboard finden.

Wenn Sie die [ältere Navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) verwenden, finden Sie API-Schlüssel unter **Entwicklungskonsole** > **API-Einstellungen**...
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

Siehe die Datei `App.xaml.cs` in der [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs) Beispielanwendung.
{% endtab %}
{% endtabs %}

### Schritt 3: Testen Sie die Integration

{% tabs %}
{% tab android %}
Jetzt können Sie Ihre Anwendung starten und sehen, wie die Sitzungen im Braze-Dashboard protokolliert werden (zusammen mit Geräteinformationen und anderen Analytics). Eine ausführlichere Diskussion über die besten Praktiken für die grundlegende SDK-Integration finden Sie in der [Anleitung zur Android-Integration]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).
{% endtab %}

{% tab ios %}
Jetzt können Sie Ihre Anwendung starten und sehen, wie die Sitzungen im Braze-Dashboard protokolliert werden. Eine ausführlichere Diskussion der besten Praktiken für die grundlegende SDK-Integration finden Sie in der [Anleitung zur iOS-Integration]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift).

{% alert important %}
Unser aktuelles öffentliches .NET MAUI-Binding für das iOS SDK stellt keine Verbindung zum iOS Facebook SDK her (Verknüpfung von Social-Daten) und beinhaltet nicht das Senden des IDFA an Braze.
{% endalert %}
{% endtab %}
{% endtabs %}
