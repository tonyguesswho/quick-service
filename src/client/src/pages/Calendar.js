import React, { useState, useEffect } from 'react'
import PageHeader from "../components/PageHeader";
import PeopleOutlineTwoToneIcon from '@material-ui/icons/PeopleOutlineTwoTone';
import { Paper, makeStyles } from '@material-ui/core';
import { ViewState } from '@devexpress/dx-react-scheduler';
import {
	Scheduler,
	MonthView,
	Appointments,
	AppointmentTooltip,
} from '@devexpress/dx-react-scheduler-material-ui';


import axios from "axios"



const useStyles = makeStyles(theme => ({
	pageContent: {
		margin: theme.spacing(5),
		padding: theme.spacing(3)
	},
	searchInput: {
		width: '75%'
	},
	newButton: {
		position: 'absolute',
		right: '10px'
	}
}))




function Calendar() {
	const classes = useStyles();
	const [orders, setOrders] = useState([])


	const getOrders = async () => {
		let response = await axios.get('http://localhost:5000/orders')
		setOrders(response.data.data)
	}


	const setupSchedule = () => {
		let data = []
		orders.map((order) => (
			data.push({
				startDate: order.request_date,
				endDate: order.end_date,
				title: `${order.service.name} for ${order.email}`
			})

		))
		return data

	}

	useEffect(() => {
		getOrders()
	})


	return (
		<>
			<PageHeader
				title="Requests Calendar"
				subTitle="Month View"
				icon={<PeopleOutlineTwoToneIcon fontSize="large" />}
			/>
			<Paper className={classes.pageContent}>
				<Scheduler
					data={setupSchedule()}
				>
					<ViewState
						currentDate={new Date()}
					/>
					<MonthView

					/>
					<Appointments />
					<AppointmentTooltip />
				</Scheduler>
			</Paper>
		</>
	)
}

export default Calendar
