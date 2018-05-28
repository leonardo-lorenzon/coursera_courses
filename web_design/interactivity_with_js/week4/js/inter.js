function checkEmail() {
	if (document.getElementById('email').value != document.getElementById('emailrepeat').value) {
		alert('Email don\'t matche!');
		return false;
	}
}