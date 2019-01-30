// service-worker.js
workbox.setConfig({debug: false})
// set names for both precache & runtime cache
workbox.core.setCacheNameDetails({
    prefix: 'braze',
    suffix: 'v1',
    precache: 'precache',
    runtime: 'runtime-cache'
});


// let Service Worker take control of pages ASAP
workbox.skipWaiting();
workbox.clientsClaim();

// let Workbox handle our precache list
workbox.precaching.precacheAndRoute(self.__precacheManifest);

// use `networkFirst` strategy for `*.html`, like all my posts
workbox.routing.registerRoute(
    /^[^.]+$/,
    workbox.strategies.networkFirst()
);

// use `networkFirst` strategy for assets
workbox.routing.registerRoute(
    /docs\/assets\/(img|icons|js|css|fonts)/,
    workbox.strategies.networkFirst()
);


// use `networkFirst` strategy for global scripts and css
workbox.routing.registerRoute(
    /docs\/assets\/*\.(css|js)/,
    workbox.strategies.networkFirst()
);

// third party files
workbox.routing.registerRoute(
    /^https?:\/\/cdn.staticfile.org/,
    workbox.strategies.staleWhileRevalidate()
);
