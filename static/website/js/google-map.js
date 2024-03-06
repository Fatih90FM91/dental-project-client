
// var google;

// function init() {
//     // Basic options for a simple Google Map
//     // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
//     // var myLatlng = new google.maps.LatLng(40.71751, -73.990922);
//     var myLatlng = new google.maps.LatLng(52.0940203, 4.3851613);
//     // 39.399872
//     // -8.224454
    
//     var mapOptions = {
//         // How zoomed in you want the map to start at (always required)
//         zoom: 7,

//         // The latitude and longitude to center the map (always required)
//         center: myLatlng,

//         // How you would like to style the map. 
//         scrollwheel: false,
//         styles: [
//             {
//                 "featureType": "administrative.country",
//                 "elementType": "geometry",
//                 "stylers": [
//                     {
//                         "visibility": "simplified"
//                     },
//                     {
//                         "hue": "#ff0000"
//                     }
//                 ]
//             }
//         ]
//     };

    

//     // Get the HTML DOM element that will contain your map 
//     // We are using a div with id="map" seen below in the <body>
//     var mapElement = document.getElementById('map');

//     // Create the Google Map using out element and options defined above
//     //https://maps.app.goo.gl/SHsH9jpSJcBUgXKt5
//     var map = new google.maps.Map(mapElement, mapOptions);
    
//     var addresses = ['Leidschendam'];

//     for (var x = 0; x < addresses.length; x++) {
//         $.getJSON('http://maps.googleapis.com/maps/api/geocode/json?address='+addresses[x]+'&sensor=false', null, function (data) {
//             var p = data.results[0].geometry.location
//             var latlng = new google.maps.LatLng(p.lat, p.lng);
//             new google.maps.Marker({
//                 position: latlng,
//                 map: map,
//                 icon: 'static/website/images/loc.png'
//             });

//         });
//     }
    
// }
// google.maps.event.addDomListener(window, 'load', init);



// This example uses SVG path notation to add a vector-based symbol
// as the icon for a marker. The resulting icon is a marker-shaped
// symbol with a blue fill and no border.
// Initialize and add the map
// Initialize and add the map
// let map;

// async function initMap() {
//   // The location of Uluru
//   const position = { lat: -25.344, lng: 131.031 };
//   // Request needed libraries.
//   //@ts-ignore
//   const { Map } = await google.maps.importLibrary("maps");
//   const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

//   // The map, centered at Uluru
//   map = new Map(document.getElementById("map"), {
//     zoom: 4,
//     center: position,
//     mapId: "DEMO_MAP_ID",
//   });

//   // The marker, positioned at Uluru
//   const marker = new AdvancedMarkerElement({
//     map: map,
//     position: position,
//     title: "Uluru",
//   });
// }

// initMap();



// Initialize and add the map
// let map;

// async function initMap() {
//   // The location of Uluru
//   const position = { lat: -25.344, lng: 131.031 };
//   // Request needed libraries.
//   //@ts-ignore
//   const { Map } = await google.maps.importLibrary("maps");
//   const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

//   // The map, centered at Uluru
//   map = new Map(document.getElementById("map"), {
//     zoom: 4,
//     center: position,
//     mapId: "DEMO_MAP_ID",
//   });

//   // The marker, positioned at Uluru
//   const marker = new AdvancedMarkerElement({
//     map: map,
//     position: position,
//     title: "Uluru",
//   });
// }

// initMap();


// Initialize and add the map
// let map;

// async function initMap() {
//   // The location of Uluru
//   const position = { lat: -25.344, lng: 131.031 };
//   // Request needed libraries.
//   //@ts-ignore
//   const { Map } = await google.maps.importLibrary("maps");
//   const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

//   // The map, centered at Uluru
//   map = new Map(document.getElementById("map"), {
//     zoom: 4,
//     center: position,
//     mapId: "DEMO_MAP_ID",
//   });

//   // The marker, positioned at Uluru
//   const marker = new AdvancedMarkerElement({
//     map: map,
//     position: position,
//     title: "Uluru",
//   });
// }

// initMap();




function initMap(){
    let leidschendam = {lat: 52.0940203, lng: 4.3851613}
    let map = new google.maps.Map(
      document.getElementById('map'), {zoom: 14, center: leidschendam}
    );
    let marker = new google.maps.Marker({position: leidschendam, map: map})
  }

  initMap()