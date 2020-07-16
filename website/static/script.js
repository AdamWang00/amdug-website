const scrollThreshold = 40;

function checkScrolled() {
	if (window.scrollY > scrollThreshold) {
		$("header nav").addClass("scrolled");
	} else {
		$("header nav").removeClass("scrolled");
	}
}

$(document).ready(function(){
	checkScrolled()
	$(window).scroll(checkScrolled);
});