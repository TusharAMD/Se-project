import M from "materialize-css";
import options from "materialize-css";
import {useState} from "react";
import axios from 'axios';
import { useAuth0 } from "@auth0/auth0-react";

function DailyIntake(){
const [formdata, setFormdata]=useState([])


return(
<div className="DailyIntakeContainer">
<form>
    <h3>Vegetables</h3>
    <select  value={formdata.gender} onChange={e=>setFormdata({...formdata,gender:e.target.value})} className="browser-default">
        <option value="male">Male</option>
        <option value="female">Female</option>
    </select>
    <input />
    <button className="btn waves-effect waves-light" type="submit">Submit
        <i className="material-icons right">send</i>
    </button>
</form>
</div>
)
};

export default DailyIntake;