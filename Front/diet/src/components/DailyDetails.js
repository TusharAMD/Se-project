import React, { useState } from 'react'
import axios from 'axios';
import { useAuth0 } from "@auth0/auth0-react";

const DailyDetails = () => {
    
    const { user, isAuthenticated, isLoading } = useAuth0();
    const [formValues, setFormValues] = useState([{ name: "", weight : ""}])
    const d = new Date();
    console.log(d)
    
    let handleChange = (i, e) => {
        let newFormValues = [...formValues];
        newFormValues[i][e.target.name] = e.target.value;
        setFormValues(newFormValues);
        console.log(newFormValues)
      }
    
    let addFormFields = () => {
        setFormValues([...formValues, { name: "", weight: "" }])
      }
    
    let removeFormFields = (i) => {
        let newFormValues = [...formValues];
        newFormValues.splice(i, 1);
        setFormValues(newFormValues)
    }
    
    let handleSubmit = (event) => {
        event.preventDefault();
        alert(JSON.stringify(formValues));
        axios.post("http://127.0.0.1:5000/dailydetails", { formValues,user,d })
      .then(res => {
        console.log(res);
        console.log(res.data);
        
      })
    }

    return (
    <div className="DailyIntakeContainer">
        <form  onSubmit={handleSubmit}>
          {formValues.map((element, index) => (
            <div className="form-inline" key={index}>
              <label>Name</label>
              
              
              <select name="name" value={element.value} onChange={e => handleChange(index, e)} className="browser-default daily">
                <option disabled value=">Vegetables">>Vegetables</option>
                <option value="Ladyfinger">Ladyfinger</option>
                <option value="Tomato ">Tomato </option>
                <option value="Onion ">Onion </option>
                <option value="Potato ">Potato </option>
                <option value="Turnip ">Turnip </option>
                <option value="Turmeric ">Turmeric </option>
                <option value="Sweet Potato ">Sweet Potato </option>
                <option value="Spring Onion ">Spring Onion </option>
                <option value="Spinach ">Spinach </option>
                <option value="Snake Gourd">Snake Gourd</option>
                <option value="Pumpkin ">Pumpkin </option>
                <option value="Garlic ">Garlic </option>
                <option value="Ginger ">Ginger </option>
                <option value="Fenugreek ">Fenugreek </option>
                <option value="Green Chilli">Green Chilli</option>
                <option value="Green Beans">Green Beans</option>
                <option value="Radish ">Radish </option>
                <option value="Jackfruit ">Jackfruit </option>
                <option value="Lady Finger ">Lady Finger </option>
                <option value="Mushroom ">Mushroom </option>
                <option value="Maize ">Maize </option>
                <option value="Peas ">Peas </option>
                <option value="Cauliflower">Cauliflower</option>
                <option value="Cabbage">Cabbage</option>
                <option value="Carrot ">Carrot </option>
                <option value="Capsicum ">Capsicum </option>
                <option value="Brinjal ">Brinjal </option>
                <option value="Bitter Gourd">Bitter Gourd</option>
                <option value="Beetroot">Beetroot</option>
                <option value="Broccoli ">Broccoli </option>
                <option value="Colocasia Root">Colocasia Root</option>
                <option disabled value=">Food Grains">>Food Grains</option>
                <option value="Rice ">Rice </option>
                <option value="Wheat ">Wheat </option>
                <option value="Maize ">Maize </option>
                <option value="Maida">Maida</option>
                <option value="Barley ">Barley </option>
                <option value="Sago">Sago</option>
                <option value="Sorghum">Sorghum</option>
                <option value="Semolina ">Semolina </option>
                <option value="Oat ">Oat </option>
                <option value="Chickpeas ">Chickpeas </option>
                <option value="Lentil ">Lentil </option>
                <option value="Black gram ">Black gram </option>
                <option value="Millet ">Millet </option>
                <option value="Pinto Beans">Pinto Beans</option>
                <option value="Sugar">Sugar</option>
                <option value="Soya Beans">Soya Beans</option>
                <option disabled value=">Meat and Dairy">>Meat and Dairy</option>
                <option value="Goat Meat">Goat Meat</option>
                <option value="Chicken">Chicken</option>
                <option value="Fishes">Fishes</option>
                <option value="Eggs">Eggs</option>
                <option value="Pork">Pork</option>
                <option value="Cow Milk">Cow Milk</option>
                <option value="Buffalo Milk">Buffalo Milk</option>
                <option value="Cheese">Cheese</option>
                <option value="Ghee">Ghee</option>

                <option disabled value="female">Female</option>
                
              </select>
              
              
              {/*<input type="text" name="name" value={element.name || ""} onChange={e => handleChange(index, e)} />*/}
              <label>Weight</label>
              <input type="text" name="weight" value={element.weight || ""} onChange={e => handleChange(index, e)} />
              {
                index ? 
                  <button type="button"  className="button remove" onClick={() => removeFormFields(index)}>Remove</button> 
                : null
              }
            </div>
          ))}
          <div className="button-section">
              <button className="button add" type="button" onClick={() => addFormFields()}>Add</button>
              <button className="button submit" type="submit">Submit</button>
          </div>
      </form>
      </div>
    )
}

export default DailyDetails