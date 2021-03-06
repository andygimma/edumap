var clusterer=null;
var global_markers=[];
var filtered_markers = [];

var still_loading;
$(function(){
  $('.program_slide_toggle_box').hide();
  $('.age_group_slide_toggle_box').hide();


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
    
    

  
    $("#subject").click(function () {
   $('.program_slide_toggle_box').slideToggle();
         clusterer.addMarkers(filtered_markers);

  });
  $("#age_group").click(function () {
   $('.age_group_slide_toggle_box').slideToggle();
         clusterer.addMarkers(filtered_markers);

  });
  
    $("a.filter_button_subheader").click(function(event) {
    

      var filter_name = event.target.id;
      var filter = $(this).text();
      filtered_markers.length = 0;

      if (still_loading != true) {
	clusterer.clearMarkers();
	console.log(3);
	for (var i = 0; i < global_markers.length; i++) {
	  console.log(global_markers[i].age_group);
	  console.log(global_markers[i].subject);
	  if (global_markers[i].age_group == filter_name) {
	    filtered_markers.push(global_markers[i]);

	  }
	  
	  if (global_markers[i].subject == filter_name) {
	    filtered_markers.push(global_markers[i]);
	  }
	}
	
      clusterer.addMarkers(filtered_markers);
      console.log(filtered_markers);
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
    "/public_site_ajax_handler",
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
					     'address': sites_list[i].full_address, 
					      'id': sites_list[i].id,
					      'age_group': sites_list[i].age_group, 
					      'contact_number': sites_list[i].contact_number, 
					      'program': sites_list[i].program, 
					      'program_type': sites_list[i].program_type, 
					      'subject': sites_list[i].subject,
					      'notes': sites_list[i].notes,
					      'name': sites_list[i].name});
	 markers.push(marker);
	google.maps.event.addListener(marker, "click", function() {
	  new Messi("<p>Program Name:" + this.name + "</p><p>Subject: " + this.subject + "</p><p>Age Group: " + this.age_group + "</p><p>Address: " + this.address + "</p><p>Notes: " + this.notes + "</p>",
	  {title: this.agency, titleClass: 'info', 
	  buttons: [
	  {id: 0, label: 'More Info', val: this.id }, 
	  {id: 1, label: 'Close', val: 'None'}], callback: function(val) { if (val != "None") {openRequestedPopup("/site/" + val);} }});

	});
       }
       
	var total_markers = old_markers.concat(markers)
	clusterer.addMarkers(total_markers);
		 
// 		 filtered_markers = total_markers;
		 
		 
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