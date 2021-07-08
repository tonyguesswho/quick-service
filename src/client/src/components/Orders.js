import React, { useState } from 'react'


function Orders() {

	const [orders, setOrders] = useState([
		{
			"id": 1,
			"service": "Launndry",
			"time": "2021-07-06T12:34:02.407126",
			"email": "tony@gmail.com"
		},
		{
			"id": 2,
			"service": "Ram",
			"time": "2021-07-06T12:34:02.407126",
			"email": "tony2@gmail.com"
		},
		{
			"id": 2,
			"service": "fish",
			"time": "2021-07-06T12:34:02.407126",
			"email": "tony3@gmail.com"
		}
	])


	return (
		<div>
			{orders.map((order) => (
				<h3 key={order.id}>{order.email}</h3>
			))}
		</div>
	)
}

export default Orders
