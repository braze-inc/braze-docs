## Solução de problemas

### O push não aparece depois que o app é fechado no alternador de tarefas

Se você observar que as notificações por push não aparecem mais após o app ser fechado pelo alternador de tarefas, seu app provavelmente está em modo de depuração. O .NET MAUI adiciona estruturas no modo de depuração que impedem os apps de receberem push após seu processo ser encerrado. Se você executar seu app no modo de lançamento, deverá ver o push mesmo depois que o app for fechado no alternador de tarefas.

### A fábrica de notificações personalizadas não está sendo definida corretamente

Os fatos de notificação personalizados (e todos os delegates) devem estender [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) para funcionar corretamente na divisão entre C# e Java. Para saber mais, consulte [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) sobre a implementação de interfaces Java.
