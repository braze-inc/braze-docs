## Solución de problemas

### El push no aparece después de cerrar la aplicación desde el conmutador de tareas

Si observas que las notificaciones push ya no aparecen después de cerrar la aplicación desde el conmutador de tareas, es probable que tu aplicación esté en modo Depuración. Xamarin añade un andamiaje en el modo Depuración que impide que las aplicaciones reciban push después de que su proceso haya finalizado. Si ejecutas tu aplicación en Modo Lanzamiento, deberías ver push incluso después de cerrar la aplicación desde el conmutador de tareas.

### La fábrica de notificaciones personalizadas no se configura correctamente

Las fábricas de notificaciones personalizadas (y todos los delegados) deben extender [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) para que funcionen correctamente entre C# y Java. Consulta [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) sobre la implementación de interfaces Java para obtener más información.
