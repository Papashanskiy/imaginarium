$( '#navbarResponsive .navbar-nav a' ).on( 'click', function () {
	$( '#navbarResponsive .navbar-nav' ).find( 'li.active' ).removeClass( 'active' );
	$( this ).parent( 'li' ).addClass( 'active' );
});


// nav-item
// navbarResponsive
