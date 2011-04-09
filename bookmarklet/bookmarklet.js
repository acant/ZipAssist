(function(){
	function alerturl() {
		var height = 600;
		var width = 800;
		var url = encodeURIComponent(window.location.href);
		var title = encodeURIComponent(document.title);
		var selected = encodeURIComponent(window.getSelection ? window.getSelection() : document.getSelection ? document.getSelection() : document.selection.createRange().text );
		var w = window.open(
			'/opt/src/ZipAssist/bookmarklet/success.html?url='+url+'&title='+title+'&selected='+selected,
			'ZipAssist',
			'toolbar=no,scrollbar=yes,height='+height+',width='+width+',top='+((screen.height-height)/2)+',left='+((screen.width-width)/2));
	}
	alerturl();
})();
