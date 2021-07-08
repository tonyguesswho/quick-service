import React from 'react'
import { AppBar, Toolbar, Button, Grid, Typography, makeStyles } from "@material-ui/core"
import { NavLink } from 'react-router-dom'
const useStyles = makeStyles({
	root: {
		backgroundColor: '#fff',
		color: "black",
	}
})



const Header = () => {
	const classes = useStyles();
	return (
		<div>
			<AppBar position="static" className={classes.root}>
				<Toolbar>
					<Grid container>
						<Grid item >
							<NavLink to="/">
								<Typography variant="h6" >Home</Typography>
							</NavLink>
						</Grid>
						<Grid item >
							<NavLink to="/calendar">
								<Button color="inherit">Calender</Button>
							</NavLink>
						</Grid>
						<Grid item sm></Grid>
						<Grid item >
							<NavLink to="/options">
								<Button color="inherit">Services Available</Button>
							</NavLink>

						</Grid>
						<Grid item >
							<NavLink to="/new">
								<Button color="inherit">New Request</Button>
							</NavLink>
						</Grid>
					</Grid>
				</Toolbar>
			</AppBar>

		</div >
	)
}

export default Header

