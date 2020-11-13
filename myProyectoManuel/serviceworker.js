var CACHE_NAME = 'Lavado de autos Don Manuel';
var urlsToCache = [
    '/',
    '/Galeria/',
    '/Nosotros/',
    '/Sucursales/',
    '/static/css/EstilosIndex.css',
    '/static/css/MenuyFooter.css',
    '/static/css/EstilosNosotros.css',
    '/static/css/EstilosGaleria.css',
    '/static/img/Logos/Logo1.png',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
            console.log('Opened cache');
            return cache.addAll(urlsToCache);
        })
    );
});

/*
self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {

            return fetch(event.request)
                .catch(function(rsp) {
                    return response; 
                });
          
          
        })
    );
});
*/

/* Todos los elementos */
self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
        
      })
      .catch(function(e){
          return caches.match(event.request)
      })
  

     
    );
});

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
    apiKey: "AIzaSyBvqLErqAlub1cP40ssg0oQP43mF6bAXlM",
    authDomain: "lavado-de-autos-don-manuel.firebaseapp.com",
    databaseURL: "https://lavado-de-autos-don-manuel.firebaseio.com",
    projectId: "lavado-de-autos-don-manuel",
    storageBucket: "lavado-de-autos-don-manuel.appspot.com",
    messagingSenderId: "968286739764",
    appId: "1:968286739764:web:4b9265b69389fba0d45961"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

let messaging = firebase.messaging(); //Instancia del servicio de mensajeria

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//Modelo OffLine

messaging.setBackgroundMessageHandler(function(payload){
    let titulo = payload.notificacion.title
    let opciones = {
        bodi: payload.notificacion.body,
        icon: payload.notificacion.icon
    }
    self.registration.showNotification(titulo,opciones)
})

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////