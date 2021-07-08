

const convertMinute = (min) => {
	const num = min;
	let rminutes = ""
	let rhours = ""
	const hours = (num / 60);
	rhours = Math.floor(hours);
	const minutes = (hours - rhours) * 60;
	if (minutes) {
		rminutes = `${Math.round(minutes)} minutes`
	}
	if (hours) {
		rhours = `${Math.round(hours)} hour(s) `
	}
	return rhours + rminutes;

}
function validateEmail(email) {
	const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return re.test(String(email).toLowerCase());
}

export {
	convertMinute,
	validateEmail
}