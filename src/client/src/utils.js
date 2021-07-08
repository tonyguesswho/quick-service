

const convertMinute = (min) => {
	const num = min;
	let rminutes=""
	let rhours=""
	const hours = (num / 60);
	rhours = Math.floor(hours);
	const minutes = (hours - rhours) * 60;
	if(minutes){
		rminutes = `${Math.round(minutes)} minutes`
	}
	if(hours){
		rhours = `${Math.round(hours)} hour `
	}	
	return rhours  + rminutes;

}

export {
	convertMinute
}