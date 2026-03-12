## Résolution des problèmes

### La notification push n’apparaît pas après la fermeture de l’application à l’aide du commutateur de tâche

Si vous constatez que les notifications push n'apparaissent plus après la fermeture de l'application à partir du sélecteur de tâches, il est probable que votre application soit en mode débogage. .NET MAUI ajoute une structure en mode débogage qui empêche les applications de recevoir des notifications push après la fermeture de leur processus. Si vous exécutez votre application en mode Libérer, vous devriez voir vos notifications push, même après la fermeture de l’application à l’aide du commutateur de tâche.

### Le générateur de notifications personnalisées n’est pas correctement configuré

Les générateurs de notifications personnalisées (et tous les délégués) doivent étendre [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) afin de fonctionner correctement au-delà du fossé entre C# et Java. Consultez [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) pour plus d’informations concernant l’implémentation d’interfaces Java.
