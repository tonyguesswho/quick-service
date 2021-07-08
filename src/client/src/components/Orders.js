import React, { useState, useEffect } from 'react'
import PageHeader from "../components/PageHeader";
import PeopleOutlineTwoToneIcon from '@material-ui/icons/PeopleOutlineTwoTone';
import { Paper, makeStyles, TableBody, TableRow, TableCell, Toolbar, InputAdornment, TextField } from '@material-ui/core';

import useTable from "../components/useTable";
import { Search } from "@material-ui/icons";
import axios from "axios"
import { convertMinute } from '../utils'


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


const headCells = [
	{ id: 'email', label: "Customer's Email" },
	{ id: 'created_date', label: 'Order date' },
	{ id: 'request_date', label: 'Scheduled Date' },
	{ id: 'end_date', label: 'End Date', },
	{ id: 'service', label: 'Service', },
	{ id: 'duration', label: 'Duration', }
]


function Orders() {
	const classes = useStyles();
	const [orders, setOrders] = useState([])
	const [filterFn, setFilterFn] = useState({ fn: items => { return items; } })


	const {
		TblContainer,
		TblHead,
		TblPagination,
		recordsAfterPagingAndSorting
	} = useTable(orders, headCells, filterFn);

	const handleSearch = e => {
		let target = e.target;
		setFilterFn({
			fn: items => {
				if (target.value == "")
					return items;
				else
					return items.filter(x => x.service.name.toLowerCase().includes(target.value))
			}
		})
	}





	const getOrders = async () => {
		let response = await axios.get('http://localhost:5000/orders')
		setOrders(response.data.data)
	}

	useEffect(() => {
		getOrders()

	}, [])


	return (
		<>
			<PageHeader
				title="Service Requests"
				subTitle="Service Request Orders"
				icon={<PeopleOutlineTwoToneIcon fontSize="large" />}
			/>
			<Paper className={classes.pageContent}>

				<Toolbar>
					<TextField
						label="Search Service"
						className={classes.searchInput}
						InputProps={{
							startAdornment: (<InputAdornment position="start">
								<Search />
							</InputAdornment>)
						}}
						onChange={handleSearch}
					/>
				</Toolbar>
				<TblContainer>
					<TblHead />
					<TableBody>
						{
							recordsAfterPagingAndSorting().map(item =>
								(<TableRow key={item.id}>
									<TableCell>{item.email}</TableCell>
									<TableCell>{new Date(item.created_date).toDateString()}</TableCell>
									<TableCell>{new Date(item.request_date).toUTCString()}</TableCell>
									<TableCell>{new Date(item.end_date).toUTCString()}</TableCell>
									<TableCell>{item.service.name}</TableCell>
									<TableCell>{convertMinute(item.service.duration)}</TableCell>
								</TableRow>)
							)
						}
					</TableBody>
				</TblContainer>
				<TblPagination />
			</Paper>
		</>
	)
}

export default Orders
