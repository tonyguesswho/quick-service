import React, { useState, useEffect } from 'react'
import {
	FormControl,
	Grid,
	TextField,
	makeStyles,
	FormHelperText,
	NativeSelect,
	Button as MuiButton
} from "@material-ui/core"


import DateFnsUtils from '@date-io/date-fns';
import {
	MuiPickersUtilsProvider,
	KeyboardDateTimePicker,
} from '@material-ui/pickers';
import axios from 'axios'
import { validateEmail } from '../utils'
import Notification from "../components/Notification";


const useStyles = makeStyles(theme => ({
	root: {
		'& .MuiFormControl-root': {
			width: "80%",
			margin: theme.spacing(1),
		},
		'& .MuiButtonBase-root': {
			padding: '6px 12px'
		}


	},
	label: {
		textTransform: 'none'
	}
}))


function OrderForm() {

	const initialValues = { "service_id": 0, "email": "", "date": "" }
	const [values, setValues] = useState(initialValues)
	const [services, setServices] = useState([])
	const [errors, setErrors] = useState({})
	const [notify, setNotify] = useState({ isOpen: false, message: '', type: '' })


	const handleInputChange = (e) => {

		const { name, value } = e.target
		setValues({
			...values,
			[name]: value
		})
	}

	const resetForm = () => {
		setValues(initialValues);
		setErrors({})
	}
	const validate = (fieldValues = values) => {
		let temp = { ...errors }
		if ('date' in fieldValues)
			temp.date = fieldValues.date ? "" : "This field is required."
		if ('email' in fieldValues)
			temp.email = (validateEmail(fieldValues.email)) ? "" : "Email is not valid."
		if ('service_id' in fieldValues)
			temp.service_id = fieldValues.service_id != 0 ? "" : "This field is required."
		setErrors({
			...temp
		})

		if (fieldValues == values)
			return Object.values(temp).every(x => x == "")
	}
	const handleSubmit = async (e) => {
		e.preventDefault()

		if (validate()) {
			// resetForm()
			try {
				let res = await axios.post('http://localhost:5000/orders', {
					request_date: values.date,
					email: values.email,
					service_id: parseInt(values.service_id)
				})
				setNotify({ isOpen: true, message: res.data.message, type: 'success' })

			} catch (error) {
				if (error.response) {
					const { message } = error.response.data
					setNotify({ isOpen: true, message, type: 'error' })
				}

			}




		}
	}


	const getServices = async () => {
		let response = await axios.get('http://localhost:5000/services')
		setServices(response.data.data)
	}

	const convertToEvent = (name, value) => ({
		target: {
			name, value
		}
	})

	const classes = useStyles();

	useEffect(() => {
		getServices()

	}, [])
	return (
		<>
			<Notification
				notify={notify}
				setNotify={setNotify}
			/>
			<form className={classes.root} onSubmit={handleSubmit}>
				<Grid container>
					<Grid item xs={6}>
						<TextField
							{...(errors.email && { error: true, helperText: errors.email })}
							label="Customer's Email"
							value={values.email}
							onChange={handleInputChange}
							name="email" />
						<FormControl className={classes.formControl}
							{...(errors.service_id && { error: true, helpertext: errors.service_id })}
						>

							<NativeSelect
								className={classes.selectEmpty}
								value={values.service_id}
								name="service_id"
								onChange={handleInputChange}
								inputProps={{ 'aria-label': 'service' }}
							>
								<option value={0} >None</option>
								{services.map((option) => (
									<option value={option.id} key={option.id}>{option.name}</option>
								))}
							</NativeSelect>
							<FormHelperText>{errors.service_id}</FormHelperText>
						</FormControl>
					</Grid>
					<Grid item xs={6}>
						<FormControl>
							<MuiPickersUtilsProvider utils={DateFnsUtils}>
								<Grid container justifyContent="space-around">

									<KeyboardDateTimePicker
										error={errors.date}
										{...(errors.date && { error: true, helperText: errors.date })}
										margin="normal"
										id="date-picker-dialog"
										label="Select Date and Time"
										format="yyyy-MM-dd HH:mm:ss"
										name="date"
										value={values.date}
										onChange={date => handleInputChange(convertToEvent("date", date))}
										KeyboardButtonProps={{
											'aria-label': 'choose date',
										}}
									/>
								</Grid>
							</MuiPickersUtilsProvider>
						</FormControl>
						<FormControl>
							<MuiButton
								size="large"
								variant="outlined"
								color="primary"
								type="submit"
								classes={{ root: classes.root, label: classes.label }}>
								Submit
						</MuiButton>
						</FormControl>
					</Grid>
				</Grid>

			</form >
		</>
	)
}

export default OrderForm
