(function(){
  function alerturl() {
    var height = 600;
    var width = 1000;
    var url = encodeURIComponent(window.location.href);
    var title = encodeURIComponent(document.title);
    var selected = encodeURIComponent(window.getSelection ? window.getSelection() : document.getSelection ? document.getSelection() : document.selection.createRange().text );
    var w = window.open(
      'http://sparkle-hackwat.appspot.com/manage?url='+url+'&title='+title+'&selected='+selected,
      'ZipAssist',
      'toolbar=no,scrollbar=yes,height='+height+',width='+width+',top='+((screen.height-height)/2)+',left='+((screen.width-width)/2));
  }
  alerturl();
})();
