import Login from './Login';
import Logout from './Logout';
import Profile from './Profile';
import BasicDetails from './BasicDetails';
import DailyIntake from './DailyIntake';
import DailyDetails from './DailyDetails';
import Stats from './Stats';
import { useAuth0 } from "@auth0/auth0-react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


function Navbar(){
const { user, isAuthenticated, isLoading } = useAuth0();
console.log(isAuthenticated)

if (isLoading) {
    return <img src="https://acegif.com/wp-content/uploads/loading-58.gif"></img>;
  }

else if (isAuthenticated==true){
return (
    <Router>
    <div>
    <nav>
    <div className="nav-wrapper">
      <a href="#" className="brand-logo"><img className="logo" src="https://i.ibb.co/GJXvHNV/image.png"></img></a>
      <ul id="nav-mobile" className="right hide-on-med-and-down">
        <Logout />
        
        <li>
          <Link to="/BasicDetails">My Details</Link>
        </li>
        <li>
          <Link to="/Stats">Check My Diet</Link>
        </li>
        <li>
          <Link to="/">Home</Link>
        </li>
      </ul>
    </div>
  </nav>
  <Switch>
          <Route path="/BasicDetails">
            <BasicDetails />
          </Route>
          <Route path="/DailyIntake">
            <DailyDetails />
          </Route>
          <Route path="/Stats">
            <Stats />
          </Route>
          <Route exact path="/">
            <Profile />
          </Route>
        </Switch>
  </div>
  </Router>
    
);
}
else {
return (
    <>
    <nav>
    <div className="nav-wrapper">
      <a href="#" className="brand-logo"><img className="logo" src="https://i.ibb.co/GJXvHNV/image.png"></img></a>
      <ul id="nav-mobile" className="right hide-on-med-and-down">
        <Login />
      </ul>
    </div>
  </nav>
  <div className="Info">
    
    <p className="infopara">
    <h3>My Diet</h3>
    We have grown up listening to the term ‘balanced diet’ in science. It refers to a diet that has all the essential nutrients and minerals that will keep us healthy. Having a balanced diet has been encouraged by our childhood. After all, it is important in keeping our health well.
    Most people believe that a balanced diet is definitely the key to a healthy lifestyle. It is rightly believed as even scientists say so. When we always consume a balanced diet, we will maintain our physical as well as mental health. A balanced diet must contain the proper foods that are consumed in apt quantities. A perfect balanced diet is composed of carbohydrates, proteins, fats, minerals, high fiber content, vitamins, and more.
    <p id="quote">"Pasta doesn't make you fat. How much pasta you eat makes you fat."
       <br/><b> Giada De Laurentiis</b></p>
    </p>
    
  </div>
  </>
    
);
}

}
export default Navbar;