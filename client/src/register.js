const bcrypt = require('bcrypt');

function validateForm() {
	var un = document.loginform.usr.value;
        var pw = document.loginform.pword.value;
        var pw2 = document.loginform.pword2.value;
 	//Gotta somehow verify username not taken       

//	if ( un == username) {
//          	alert ("Username already taken.");
//	    	return false;
//      }
        
	else if ( pw != pw2) {
	    	alert ("Passwords do not match.");
            	return false;
        }	
	
	else {
		bcrypt.genSalt(10, function(err, salt) {
    			bcrypt.hash(pw, salt, function(err, hash) {
				//TODO Put password into database if successful	
	    		});
		});
	    	return true;
	}
}

