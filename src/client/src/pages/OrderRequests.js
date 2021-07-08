import React from 'react'
import OrderForm from './OrderForm'
import PageHeader from "../components/PageHeader"
import PeopleOutlineTwoToneIcon from '@material-ui/icons/PeopleOutlineTwoTone';
import { Paper, makeStyles } from "@material-ui/core"

const useStyles = makeStyles(theme => ({
	pageContent: {
		margin: theme.spacing(5),
		padding: theme.spacing(3)
	}
}))

const OrderRequests = () => {
	const classes = useStyles();
	return (
		<>
			<PageHeader
				title="New Service Request"
				subTitle="Make a new service request"
				icon={<PeopleOutlineTwoToneIcon fontSize="large" />}
			/>
			<Paper className={classes.pageContent}>
				<OrderForm />
			</Paper>

		</>
	)
}

export default OrderRequests
