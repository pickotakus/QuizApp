window.onload = (event) => {
    var map, csv;
require([
"esri/map",
"esri/layers/CSVLayer",
"esri/Color",
"esri/symbols/SimpleMarkerSymbol",
"esri/renderers/SimpleRenderer",
"esri/InfoTemplate",
"esri/config",
"dojo/domReady!"
], function(
Map, CSVLayer, Color, SimpleMarkerSymbol, SimpleRenderer, InfoTemplate, esriConfig
) {
// Use CORS
esriConfig.defaults.io.corsEnabledServers.push("data.gov.lv"); // supports CORS
// Use proxy if the server doesn't support CORS
// esriConfig.defaults.io.proxyUrl = "/proxy/";
map = new Map("map", {
basemap: "gray",
center: [ 24.1052,56.9496 ],
zoom: 8
});

csv = new CSVLayer("https://data.gov.lv/dati/dataset/4e7e1a70-b30d-4bfd-8b07-45924d2f72e1/resource/016c7e6b-cf46-4648-aebc-3f9ced620ea9/download/skirovieglipunkti-2019-10-23.csv", {
    copyright: "data.gov.lv",
    latitudeFieldName: "map".split(",")[0],
    longitudeFieldName: "map".split(",")[1],
    delimiter: ";"
});
csv.latitudeFieldName = "Y koordināta";
csv.longitudeFieldName = "X koordināta";
csv.delimiter = ";";
var orangeRed = new Color([238, 69, 0, 0.5]); // hex is #ff4500
var marker = new SimpleMarkerSymbol("solid", 15, null, orangeRed);
var renderer = new SimpleRenderer(marker);
csv.setRenderer(renderer);
var template = new InfoTemplate("${Nosaukums}", "${Adrese}","${Kategorija}");
csv.setInfoTemplate(template);
map.addLayer(csv);
});
}

