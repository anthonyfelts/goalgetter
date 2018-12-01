function validateForm() {
	var un = document.loginform.usr.value;
        var pw = document.loginform.pword.value;
        var pw2 = document.loginform.pword2.value;
	var username = "username"; 
        var password = "password";
        
	if ((un == username) && (pw == password) && (pw == pw2)) {
            return true;
        }
        
	else {
            alert ("Login was unsuccessful, please check your username and password");
            return false;
        }	
}
