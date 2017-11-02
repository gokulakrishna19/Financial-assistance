var email = document.getElementById('email');
var password = document.getElementById('password');
var bsignup = document.getElementById('signup');

bsignup.addEventListener('click', e => {

	var mail = email.value;
	var pass = password.value;

	var auth = firebase.auth();

	var promise = auth.createUserWithEmailAndPassword(mail, pass);

	promise.catch(function(error) {

		var errorcode = error.code;
		var errormes = error.message;
		console.log(errormes+ "code"+errorcode);
	});
});

firebase.auth().onAuthStateChanged(firebaseUser => {
	if(firebaseUser){
		console.log(firebaseUser);

		window.location="/machine/index.html";
	}else{
		console.log("not logged in");
	}
});
	