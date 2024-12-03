---
nav_title: Partenariat Apptimize
page_order: 0

page_type: update
description: "Cet article archivé couvre le partenariat entre Apptimize et Braze. Braze a cessé la prise en charge du partenariat avec Apptimize en septembre 2019."
---

# Apptimize

{% alert update %}
Braze a cessé la prise en charge du partenariat avec Apptimize en septembre 2019.

<br>

Si vous utilisez actuellement Apptimize avec Braze, vous ne subirez pas d’interruption de service. Vous pouvez toujours définir des attributs personnalisés Apptimize sur les profils utilisateur Braze. Cependant, aucune escalade de support formelle avec le partenaire ne sera fournie.

<br>

Contactez votre conseiller Braze ou Apptimize si vous avez d’autres questions.
{% endalert %}


[Apptimize](https://apptimize.com/) est une plateforme de test et de croissance d'applications mobiles
qui permet aux clients d’itérer rapidement tout au long du processus de développement de l’application.

Apptimize peut être utilisé conjointement avec Braze pour compléter vos stratégies marketing/CRM 
avec des tests de l’interface utilisateur du produit, en synchronisant les expériences et
les données sur les deux plateformes.

## Cas d’utilisation

Avec Braze et Apptimize ensemble, vous pouvez tirer parti des deux plateformes conjointement
pour créer de puissantes expériences « end-to-end » :

* Synchronisez les expériences marketing dans les applications et CRM pour une promotion personnalisée.
* Testez une nouvelle expérience d’onboarding dans Apptimize et utilisez Braze pour accompagner les utilisateurs tout au long du nouveau parcours.
* Testez simultanément les configurations de fonctionnalité du produit et les communications pertinentes envoyées aux utilisateurs.
* Adapter les expériences dans l'application et leurs messages appropriés pour différents segments d'utilisateurs.

## Fonctionnement

Braze et Apptimize peuvent être intégrés ensemble pour transmettre des données du SDK au SDK.
Vous pouvez synchroniser les groupes de tests A/B Apptimize actifs avec Braze, ce qui vous permet
de recibler avec Braze des utilisateurs dans un test donné d’Apptimize, via push, e-mail 
ou des messages In-app.

Nous avons un code d’intégration de l’échantillon qui montre comment les SDK Braze et Apptimize
peuvent transmettre des données pour alimenter le ciblage personnalisé et la segmentation dans Braze en fonction 
des données d’expérience d’Apptimize.

Cet échantillon d’intégration définira des attributs personnalisés sur les profils utilisateur Braze de vos utilisateurs
pour les données Apptimize suivantes :

* La liste complète des expériences actives auxquelles l’utilisateur est actuellement inscrit.
* La liste complète des expériences auxquelles l’utilisateur a déjà été inscrit, y compris les expériences terminées.
* La ou les variantes que l’utilisateur a vues dans le cadre d’une participation à une expérience.

> Les indicateurs de fonctionnalité sont considérés comme des expériences quand la seule variante est si l’indicateur de fonctionnalité est activé ou non. Si l’indicateur de fonctionnalité est désactivé, aucune donnée ne sera rapportée.

En outre, cette intégration enregistrera un événement personnalisé Braze pour le premier événement 
de participation à une expérience. Cela peut être fait de deux manières :

* Un événement personnalisé est généré avec des données de propriété indiquant le nom de l'expérience, l'ID de l'expérience, le nom de la variante et l'ID de la variante. Vous pouvez ensuite recibler les utilisateurs via un déclenchement en temps réel grâce à nos campagnes et Canvas avec livraison par événement. Utilisez ces propriétés pour identifier l’expérience Apptimize que vous souhaitez déclencher.
* Une matrice d'attributs est générée avec des entrées pour chaque participation qui a eu lieu. Chaque participation est formatée comme suit `experiment_id_EXPERIMENT_ID:variant_id_VARIANT_ID:experiment_name_EXPERIMENT_NAME:variant_name_VARIANT_NAME`

Vous pouvez ensuite utiliser les campagnes de livraison par événement de Braze ou les canvas pour envoyer
des messages de suivi en temps réel aux utilisateurs lorsque ces événements sont déclenchés.

## Intégration

### iOS
Pour intégrer votre application, importez les fichiers `Appboy-Apptimize.m` et
fichiers `Apptimize-Appboy.h` suivants dans votre projet Xcode, importez l’en-tête `Appboy-Apptimize.h`
dans votre implémentation AppDelegate et ajoutez le code ci-dessous à 
`didFinishLaunchingWithOptions` après avoir initialisé Appboy et Apptimize :

```objc
[ApptimizeAppboy setupExperimentTracking];
```

#### Appboy-Apptimize.h:

```objc
//  Apptimize-Appboy.h

#ifndef Apptimize_Appboy_h
#define Apptimize_Appboy_h

@interface ApptimizeAppboy : NSObject
+ (void)setupExperimentTracking;
@end

#endif /* Apptimize_Appboy_h */
```

#### Appboy-Apptimize.m:

```objc
//  Apptimize-Appboy.m

#import <Foundation/Foundation.h>

#import "Apptimize-Appboy.h"

#import <Apptimize/Apptimize.h>
#import <Apptimize/Apptimize+Variables.h>

#import "Appboy.h"
#import "ABKUser.h"

// Key to store previous enrollment dictionary to check against to see if enrollment has changed
NSString *const ApptimizeAppboyTestEnrollmentStorageKey = @"ApptimizeAppboyTestEnrollmentStorageKey";

@implementation ApptimizeAppboy

+ (void)setupExperimentTracking
{
    // Track for enrollment changes
    [[NSNotificationCenter defaultCenter] addObserver:self
                                                selector:@selector(apptimizeTestsProcessed:)
                                                    name:ApptimizeTestsProcessedNotification
                                                object:nil];
    // Track for participation events
    [[NSNotificationCenter defaultCenter] addObserver:self
                                                selector:@selector(experimentDidGetViewed:)
                                                    name:ApptimizeTestRunNotification
                                                object:nil];
}

+ (void)apptimizeTestsProcessed:(NSNotification*)notification
{
    NSLog(@"Appboy-Apptimize integration processing new Apptimize tests");
    [self updateForNewTests];
}

+ (void)updateForNewTests
{
    NSDictionary *savedEnrollmentDictionary = [[NSUserDefaults standardUserDefaults] objectForKey:ApptimizeAppboyTestEnrollmentStorageKey];
    NSDictionary *currentEnrollmentDictionary = [self getEnrollmentDictionaryFromTestInfo];

    BOOL enrollmentChanged = NO;

    for (id key in currentEnrollmentDictionary) {
        if (![savedEnrollmentDictionary[key] isEqualToString:currentEnrollmentDictionary[key]]) {
            enrollmentChanged = YES;
            NSString *testAttributeKey = [@"apptimize_test_" stringByAppendingString:key];
            [[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:testAttributeKeyvalue :currentEnrollmentDictionary[key]];
        }
    }

    if (currentEnrollmentDictionary.count != savedEnrollmentDictionary.count) {
        enrollmentChanged = YES;
    }

    if (enrollmentChanged) {
        [[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"active_apptimize_tests" array:currentEnrollmentDictionary.allKeys];

        for (id key in currentEnrollmentDictionary.allKeys) {
            [[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"all_apptimize_tests" value:key];
        }

        [[NSUserDefaults standardUserDefaults] setObject:currentEnrollmentDictionary forKey:ApptimizeAppboyTestEnrollmentStorageKey];
        [[NSUserDefaults standardUserDefaults] synchronize];
    }
}

// Dictionary with variant IDs keyed by test ID, both as NSStrings
+ (NSMutableDictionary *)getEnrollmentDictionaryFromTestInfo
{
    NSMutableDictionary *enrollmentDictionary = [NSMutableDictionary dictionary];

    for(id key in [Apptimize testInfo]) {
        NSLog(@"key=%@ value=%@", key, [[Apptimize testInfo] objectForKey:key]);
        NSDictionary<ApptimizeTestInfo> *testInfo = [[Apptimize testInfo] objectForKey:key];
        enrollmentDictionary[[testInfo.testID stringValue]] = [testInfo.enrolledVariantID stringValue];
    }

    return enrollmentDictionary;
}

+ (void)experimentDidGetViewed:(NSNotification*)notification
{
    if (![notification.userInfo[ApptimizeTestFirstRunUserInfoKey] boolValue]) {
        return;
    }

    // Apptimize doesn't notify with IDs, so we iterate over all experiments to find the matching one.
    NSString *name = notification.userInfo[ApptimizeTestNameUserInfoKey];
    NSString *variant = notification.userInfo[ApptimizeVariantNameUserInfoKey];

    [[Apptimize testInfo] enumerateKeysAndObjectsUsingBlock:^(id key, id<ApptimizeTestInfo> experiment, BOOL *stop) {
        BOOL match = [experiment.testName isEqualToString:name] && [experiment.enrolledVariantName isEqualToString:variant];
        if (!match) {
            return;
        }

        // If you want to log a custom event for each participation
        [[Appboy sharedInstance] logCustomEvent:@"apptimize_experiment_viewed"
                                    withProperties: @{@"apptimize_experiment_name" : [experiment testName],
                                                        @"apptimize_variant_name" : [experiment enrolledVariantName],
                                                        @"apptimize_experiment_id" : [experiment testID],
                                                        @"apptimize_variant_id" : [experiment enrolledVariantID]}];

        // If you want a custom attribute array set for each participation
        [[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"apptimize_experiments"
                                                                    value:[NSString stringWithFormat:@"experiment_id_%@:variant_id_%@:experiment_name_%@:variant_name_%@",
                                                                            [experiment testID], [experiment enrolledVariantID], [experiment testName], [experiment enrolledVariantName] ]];
        *stop = YES;
    }];
}

@end
```

### Android

importez la classe `apptimizeappboy.java` dans votre application et dans votre implémentation `activity`
principale, créez un membre privé `appboyApptimizeIntegration` :

```java
private ApptimizeAppboy appboyApptimizeIntegration;
```

Puis dans votre méthode onCreate, après avoir initialisé Braze et Apptimize :

```java
appboyApptimizeIntegration = new ApptimizeAppboy();
appboyApptimizeIntegration.configureExperimentTracking(this);
```    

#### ApptimizeAppboy.java :

```java
package com.apptimize.appboykit;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Map;
import java.util.HashMap;
import android.util.Log;

import android.content.Context;

import com.apptimize.Apptimize;
import com.apptimize.ApptimizeTestInfo;
import com.apptimize.Apptimize.OnExperimentsProcessedListener;
import com.apptimize.Apptimize.OnExperimentRunListener;

import com.appboy.Appboy;
import com.appboy.AppboyUser;
import com.appboy.models.outgoing.AppboyProperties;

public class ApptimizeAppboy
        implements Apptimize.OnExperimentRunListener,
                    Apptimize.OnExperimentsProcessedListener {

    public void configureExperimentTracking(Context context) {
        appboyInstance = Braze.getInstance(context);
        enrollmentStorage = new File(context.getDir("apptimize-appboy", Context.MODE_PRIVATE), ApptimizeAppboyTestEnrollmentStorage);

        Apptimize.setOnExperimentRunListener(this);
        Apptimize.addOnExperimentsProcessedListener(this);
    }

    @Override
    public void onExperimentRun(String experimentName, String variantName, boolean firstRun) {
        if (!firstRun) {
            return;
        }
        Map<String,ApptimizeTestInfo> testInfoMap = Apptimize.getTestInfo();

        if (testInfoMap == null) {
            return;
        }

        String experimentId = "";
        String variantId = "";

        Log.d("Apptimize-Appboy", "In onExperimentRun");

        for (ApptimizeTestInfo testInfo : testInfoMap.values()) {
            if (testInfo.getTestName().equals(experimentName) &&
                testInfo.getEnrolledVariantName().equals(variantName)) {
                experimentId = String.valueOf(testInfo.getTestId());
                variantId = String.valueOf(testInfo.getEnrolledVariantId());
            }
        }
        Log.d("Apptimize-Appboy", "Logging participation for " + experimentName + ":" + experimentId + " and variant " + variantName + ":" + variantId);

        // If you want to log a custom event for each participation
        logParticipationEventAsEvent(experimentName, variantName, experimentId, variantId);

        // If you want a custom attribute array set for each participation
        logParticipationEventAsAttributes(experimentName, variantName, experimentId, variantId);
    }

    private void logParticipationEventAsEvent(String experimentName, String variantName, String experimentId, String variantId) {
        AppboyProperties eventProperties = new AppboyProperties();

        eventProperties.addProperty("apptimize_experiment_name", experimentName);
        eventProperties.addProperty("apptimize_variant_name", variantName);
        eventProperties.addProperty("apptimize_experiment_id", experimentId);
        eventProperties.addProperty("apptimize_variant_id", variantId);

        appboyInstance.logCustomEvent("apptimize_experiment_viewed", eventProperties);
    }

    private void logParticipationEventAsAttributes(String experimentName, String variantName, String experimentId, String variantId) {
        appboyInstance.getCurrentUser().addToCustomAttributeArray("apptimize_experiments",
                "experiment_id_" + experimentId + ":variant_id_" + variantId + ":experiment_name_" + experimentName + ":variant_name_" + variantName);
    }

    @Override
    public void onExperimentsProcessed() {
        Map<String,String> currentEnrollmentDictionary = getEnrollmentDictionary();
        Map<String,String> savedEnrollmentDictionary = getPreviousEnrollmentDictionary();
        AppboyUser appboyUser = appboyInstance.getCurrentUser();

        boolean enrollmentChanged = false;

        Log.d("Apptimize-Appboy", "Processing experiments");

        for (String key : currentEnrollmentDictionary.keySet()) {
            if (savedEnrollmentDictionary == null ||
                !currentEnrollmentDictionary.get(key).equals(savedEnrollmentDictionary.get(key))) {
                Log.d("Apptimize-Appboy", "Found change in enrollment" + currentEnrollmentDictionary.get(key));
                enrollmentChanged = true;
                String testAttributeKey = "apptimize_test_" + key;
                appboyUser.addToCustomAttributeArray(testAttributeKey, currentEnrollmentDictionary.get(key));
            }
        }

        if (currentEnrollmentDictionary.size() == 0 && savedEnrollmentDictionary.size() != 0) {
            enrollmentChanged = true;
        }

        if (enrollmentChanged) {
            Log.d("Apptimize-Appboy", "Enrollment changed");
            appboyUser.setCustomAttributeArray("active_apptimize_tests", currentEnrollmentDictionary.keySet().toArray(new String[0]));

            for (String key : currentEnrollmentDictionary.keySet()) {
                appboyUser.addToCustomAttributeArray("all_apptimize_tests", key);
            }

            storePreviousEnrollmentDictionary(currentEnrollmentDictionary);
        }
    }

    private Map<String,String> getEnrollmentDictionary()
    {
        Map<String,String> enrollment = new HashMap<String,String>();
        Map<String,ApptimizeTestInfo> testInfoMap = Apptimize.getTestInfo();
        for (ApptimizeTestInfo testInfo : testInfoMap.values()) {
            Log.d("Apptimize-Appboy", "TestID: " + String.valueOf(testInfo.getTestId()) + " VariantID: " + String.valueOf(testInfo.getEnrolledVariantId()));
            enrollment.put(String.valueOf(testInfo.getTestId()), String.valueOf(testInfo.getEnrolledVariantId()));
        }
        return enrollment;
    }

    private Map<String,String> getPreviousEnrollmentDictionary()
    {
        ObjectInputStream enrollmentStream;
        try {
            enrollmentStream = new ObjectInputStream(new FileInputStream(enrollmentStorage));
        } catch(Exception e) {
            Log.d("Apptimize-Appboy", "Unable to open file");
            return null;
        }

        Map<String, String> previousEnrollment;
        try {
                previousEnrollment = (Map<String,String>)enrollmentStream.readObject();
        } catch (Exception e) {
            Log.d("Apptimize-Appboy", "Unable to get previous enrollment");
            return null;
        }

        return previousEnrollment;
    }

    private void storePreviousEnrollmentDictionary(Map<String,String> enrollmentDictionary)
    {
        try {
            ObjectOutputStream enrollmentStream = new ObjectOutputStream(new FileOutputStream(enrollmentStorage));
            enrollmentStream.writeObject(enrollmentDictionary);
            enrollmentStream.flush();
            enrollmentStream.close();
        } catch (Exception e) {
            Log.d("Apptimize-Appboy", "Unable to save enrollment information");
        }

    }

    private Appboy appboyInstance;
    private File enrollmentStorage;

    private static String ApptimizeAppboyStorageDirectory;
    private static String ApptimizeAppboyTestEnrollmentStorage = "ApptimizeAppboyTestEnrollmentStorage";
}
```
