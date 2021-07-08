import React, { useState, useEffect } from 'react'
import axios from 'axios'
import PeopleOutlineTwoToneIcon from '@material-ui/icons/PeopleOutlineTwoTone';
import PageHeader from "../components/PageHeader"
import { Paper, makeStyles, Grid } from "@material-ui/core"
import { convertMinute } from '../utils'

const useStyles = makeStyles(theme => ({
	pageContent: {
		margin: theme.spacing(2),
		padding: theme.spacing(1)
	}
}))

const Services = () => {
	const [services, setServices] = useState([])

	const getServices = async () => {
		let response = await axios.get('http://localhost:5000/services')
		setServices(response.data.data)
	}

	useEffect(() => {
		getServices()

	}, [])
	const classes = useStyles();
	return (


		<>
			<PageHeader
				title="Services"
				subTitle="All available serives"
				icon={<PeopleOutlineTwoToneIcon fontSize="large" />}
			/>
			{services.map((service) => (
				<Paper className={classes.pageContent}>
					<Grid container key={service.id}>
						<Grid items xs={6}>
							<h3 >{service.name}</h3>

						</Grid>
						<Grid items xs={6}>
							<h2>{convertMinute(service.duration)}</h2>
						</Grid>

					</Grid>


				</Paper>
			))}

		</>
	)
}

export default Services
