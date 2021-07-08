import './App.css';
import Header from './components/Header'
import Orders from './components/Orders'
import Services from './components/Services'
import OrderRequest from './pages/OrderRequests'
import { CssBaseline, makeStyles, ThemeProvider, createTheme } from "@material-ui/core"
import { BrowserRouter, Route, Switch } from 'react-router-dom';


const theme = createTheme({
  palette: {
    primary: {
      main: "#333996",
      light: '#3c44b126'
    },
    secondary: {
      main: "#f83245",
      light: '#f8324526'
    },
    background: {
      default: "#f4f5fd"
    },
  },
  overrides: {
    MuiAppBar: {
      root: {
        transform: 'translateZ(0)'
      }
    }
  },
  props: {
    MuiIconButton: {
      disableRipple: true
    }
  }
})


const useStyles = makeStyles({
  appMain: {
    width: '100%'
  }
})

const App = () => {
  const classes = useStyles()
  return (
    <ThemeProvider theme={theme}>
      <div className={classes.appMain}>
        <BrowserRouter>
          <Header />
          <Switch>
            <Route exact path="/" >
              <Orders />
            </Route>
            <Route path="/options" >
              <Services />
            </Route>
            <Route exact path="/new" >
              <OrderRequest />
            </Route>

          </Switch>
        </BrowserRouter>
      </div >
      <CssBaseline />
    </ThemeProvider>
  )
}

export default App
