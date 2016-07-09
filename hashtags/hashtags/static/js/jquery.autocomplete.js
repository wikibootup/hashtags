$(document).ready(function() {
  $( "#id_search_tag" ).autocomplete({
    source: "/",
    messages: {
      //noResults: '',
      //results: '',
    },
    select: function( event, ui ) {
      window.location.href = ui.item.href;
    },
  })
})
