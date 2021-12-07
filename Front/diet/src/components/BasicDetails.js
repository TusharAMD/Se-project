import M from "materialize-css";
import options from "materialize-css";
import {useState} from "react";
import axios from 'axios';
import { useAuth0 } from "@auth0/auth0-react";

function BasicDetails(){
const { user, isAuthenticated, isLoading } = useAuth0();
const [formdata, setFormdata]=useState({name:user.name,email:user.email,age:"",height:"", weight:"", gender:""})

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
  });

function submitHandler(event){
    event.preventDefault();
    console.log(formdata)
    axios.post("http://127.0.0.1:5000/basicdetails", { formdata })
      .then(res => {
        console.log(res);
        console.log(res.data);
        
      })
}  

return(



<div className="BasicDetailsContainer">
<form onSubmit={submitHandler}>
<h3>Basic Details</h3>
<input value={formdata.age} onChange={e=>setFormdata({...formdata,age:e.target.value})} placeholder = "Please Enter your Age" />
<input value={formdata.height} onChange={e=>setFormdata({...formdata,height:e.target.value})} placeholder = "Please Enter your Height" />
<input value={formdata.weight} onChange={e=>setFormdata({...formdata,weight:e.target.value})} placeholder = "Please Enter your Weight" />
<select  value={formdata.gender} onChange={e=>setFormdata({...formdata,gender:e.target.value})} className="browser-default">
    <option value="male">Male</option>
    <option value="female">Female</option>
</select>

 <button className="btn waves-effect waves-light" type="submit" name="action">Submit
    <i className="material-icons right">send</i>
    
  </button>
</form>
{JSON.stringify(formdata)}
</div>

);
}

export default BasicDetails;