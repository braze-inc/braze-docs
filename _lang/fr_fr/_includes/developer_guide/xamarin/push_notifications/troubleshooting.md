## Résolution des problèmes

### La notification push n’apparaît pas après la fermeture de l’application à l’aide du commutateur de tâche

Si vous constatez que les notifications push ne s'affichent plus après la fermeture de l'application à partir du sélecteur de tâches, votre application est probablement en mode Debug. NET MAUI ajoute un échafaudage en mode Debug qui empêche les applications de recevoir des notifications push après que leur processus a été tué. Si vous exécutez votre application en mode Libérer, vous devriez voir vos notifications push, même après la fermeture de l’application à l’aide du commutateur de tâche.

### Le générateur de notifications personnalisées n’est pas correctement configuré

Les générateurs de notifications personnalisées (et tous les délégués) doivent étendre [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) afin de fonctionner correctement au-delà du fossé entre C# et Java. Consultez [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) pour plus d’informations concernant l’implémentation d’interfaces Java.
