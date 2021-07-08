import React, { useState, useEffect } from 'react'
import {
	FormControl,
	Grid,
	TextField,
	makeStyles,
	FormHelperText,
	NativeSelect
} from "@material-ui/core"


import DateFnsUtils from '@date-io/date-fns';
import {
	MuiPickersUtilsProvider,
	KeyboardDateTimePicker,
} from '@material-ui/pickers';
import axios from 'axios'


const useStyles = makeStyles(theme => ({
	root: {
		'& .MuiFormControl-root': {
			width: "80%",
			margin: theme.spacing(1),
		},

	},
}))


function OrderForm() {


	const [values, setValues] = useState({ "service_id": "", "email": "" })
	const [selectedDate, setSelectedDate] = React.useState(new Date());
	const [services, setServices] = useState([])


	const handleInputChange = (e) => {

		const { name, value } = e.target
		setValues({
			...values,
			[name]: value
		})
	}


	const handleDateChange = (date) => {
		setSelectedDate(date);
	};


	const getServices = async () => {
		let response = await axios.get('/services')
		setServices(response.data.data)
	}

	const classes = useStyles();

	useEffect(() => {
		getServices()

	}, [])
	return (
		<form className={classes.root}>
			<Grid container>
				<Grid item xs={6}>
					<TextField
						label="Customer's Email"
						value={values.email}
						onChange={handleInputChange}
						name="email" />
					<FormControl className={classes.formControl}>
						<NativeSelect
							className={classes.selectEmpty}
							value={values.service_id}
							name="service_id"
							onChange={handleInputChange}
							inputProps={{ 'aria-label': 'service' }}
						>
							<option value="" >None</option>
							{services.map((option) => (
								<option value={option.id} key={option.id}>{option.name}</option>
							))}
						</NativeSelect>
						<FormHelperText>Select Required Service</FormHelperText>
					</FormControl>
				</Grid>
				<Grid item xs={6}>
					<FormControl>
						<MuiPickersUtilsProvider utils={DateFnsUtils}>
							<Grid container justifyContent="space-around">

								<KeyboardDateTimePicker
									margin="normal"
									id="date-picker-dialog"
									label="Select Date and Time"
									format="yyyy-MM-ddTHH:mm:ss.sss"
									name="date"
									value={selectedDate}
									onChange={handleDateChange}
									KeyboardButtonProps={{
										'aria-label': 'change date',
									}}
								/>
							</Grid>
						</MuiPickersUtilsProvider>
					</FormControl>
				</Grid>
			</Grid>

		</form>
	)
}

export default OrderForm
