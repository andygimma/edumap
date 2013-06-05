var clusterer=null;
var global_markers=[];
var still_loading;
$(function(){
  $('.program_slide_toggle_box').hide();
  $('.age_group_slide_toggle_box').hide();
    $("#subject").click(function () {
   $('.program_slide_toggle_box').slideToggle();
  });
  $("#age_group").click(function () {
   $('.age_group_slide_toggle_box').slideToggle();
  });
})
