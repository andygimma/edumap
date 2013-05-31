var clusterer=null;
var global_markers=[];
var still_loading;
$(function(){
    var myLatlng = new google.maps.LatLng(40.714623 ,  -74.006605);
    var mapOptions = {
        zoom: 10,
        center: myLatlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
    
       var markerCluster = new MarkerClusterer(map);
    clusterer = markerCluster;
    populateMapByIncident("1", 0, []);
    
    
  $("a.filter_button").click(function(event) {
    

      var filter_name = event.target.id;
      var filter = $(this).text();
      
      var filtered_markers = [];
      if (still_loading != true) {
	clusterer.clearMarkers();

	for (var i = 0; i < global_markers.length; i++) {
	  if (global_markers[i].age_group == filter) {
	    filtered_markers.push(global_markers[i]);

	  }
	  
	  if (global_markers[i].program_type == filter) {
	    filtered_markers.push(global_markers[i]);
	  }
// 	  if (filter_name == "age_group"){
// 	    if (marker.age_group == filter) {
// 
// 	       filtered_markers.push(marker);
// 	    }
// 	  }
// 	  
// 	  if (filter_name == "program_type") {
// 	    if (marker.program_type = filter) {
// 	       filtered_markers.push(marker);
// 	       
// 	    } 
// 	    
// 	  }
	}
	
      clusterer.addMarkers(filtered_markers);
	// Filter the markers here
	// var new_markers = [];
	// filter old markers
	// add to new markers
	// clusterer.addMarkers(new_markers);
	
      } else {
	Messi.alert("Please wait until the map is finished loading before using the filters");
      }
    });
})
function openRequestedPopup(url)
{
window.location=url;
}



var populateMapByIncident = function(incident, page, old_markers) {
  still_loading = true;
  var run_again = false;
  $.getJSON(
    "http://educationresourcemap.appspot.com/public_site_ajax_handler",
    {"shortname" : incident, "page": page},
    function(sites_list) {
    if (sites_list.length > 99) {
      run_again = true;
    }
          var mapOptions = {
    zoom: 8,
    center: new google.maps.LatLng(40.6501038, -73.8495823),
    mapTypeId: google.maps.MapTypeId.ROADMAP
    }
//     var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
       var markers = [];
       var i = 0;
       for (var i = 0; i < sites_list.length; i++) {
	 var latLng = new google.maps.LatLng(sites_list[i].latitude, sites_list[i].longitude);
	 var marker = new google.maps.Marker({'position': latLng, 
					     'address': sites_list[i].address, 
					      'id': sites_list[i].id,
					      'agency': sites_list[i].agency, 
					      'contact_number': sites_list[i].contact_number, 
					      'program': sites_list[i].program, 
					      'age_group': sites_list[i].age_group, 
					      'program_type': sites_list[i].program_type, 
					      'site_name': sites_list[i].site_name});
	 markers.push(marker);
	google.maps.event.addListener(marker, "click", function() {
	  new Messi("<p>Site Name:" + this.site_name + "</p><p>Program Type: " + this.program_type + "</p><p>Age Group: " + this.age_group + "</p><p>Address: " + this.address + "</p><p>Phone: " + this.contact_number + "</p>",
	  {title: this.agency, titleClass: 'info', 
	  buttons: [
	  {id: 0, label: 'More Info', val: this.id }, 
	  {id: 1, label: 'Close', val: 'None'}], callback: function(val) { if (val != "None") {openRequestedPopup("/site/" + val);} }});

	});
       }
       
       	  var total_markers = old_markers.concat(markers)
	         clusterer.addMarkers(total_markers);
		 
       $("#display_incident").text("Incident: " + incident);

         if (run_again == true) {
	    populateMapByIncident(incident, page + 1, total_markers);
	} else {

	  var total_markers = old_markers.concat(markers);
	  clusterer.addMarkers(total_markers);
	  global_markers = global_markers.concat(total_markers);
	  still_loading=false;

	}
       
    }
  );

}