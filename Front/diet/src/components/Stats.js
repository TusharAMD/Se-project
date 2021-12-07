import M from "materialize-css";
import options from "materialize-css";
import {useState,useEffect} from "react";
import axios from 'axios';
import { useAuth0 } from "@auth0/auth0-react";
import { Doughnut } from 'react-chartjs-2';




function Stats(){
const[recvdata,setData] = useState({result:[]})

useEffect(() => {
        axios.get("http://127.0.0.1:5000/stats")
      .then(res => {
        console.log(res);
        console.log(res.data.result);
        setData(res.data)
      })
    },[])    


return(
<div className="StatsContainer">
{recvdata.result.map((d)=>(
    <div>
    <h3>On {d["date"]}</h3>
    
        <div className="nutrients">
            <div className="chartNutrients">
                    <Doughnut data={
                {
              labels: ['Calories', 'Cholesterol', 'Fat', 'Fiber', 'Potassium ', 'Protein', 'Sodium', 'Sugar'],
              datasets: [
                {
                  label: '# of Votes',
                  data: [d['Calories']/10, d['Cholesterol']/100, d['Fat'], d['Fiber'], d['Potassium']/100, d['Protein'], d['Sodium']/100, d['Sugar']],
                  backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(245, 119, 14, 0.2)',
                    'rgba(205, 219, 84, 0.2)',
                  ],
                  borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(245, 119, 14, 0.2)',
                    'rgba(205, 219, 84, 0.2)',
                  ],
                  borderWidth: 2,
                },
              ],
            }
                
            } />
            </div>
            <div className="tableNutrients">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Nutrition</th>
                  <th scope="col">Weight</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>Calories</td>
                  <td>{d['Calories']}</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Cholesterol</td>
                  <td>{d['Cholesterol']}</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>Fat</td>
                  <td>{d['Fat']}</td>
                </tr>
                <tr>
                  <th scope="row">4</th>
                  <td>Fiber</td>
                  <td>{d['Fiber']}</td>
                </tr>
                <tr>
                  <th scope="row">5</th>
                  <td>Potassium</td>
                  <td>{d['Potassium ']}</td>
                </tr>
                <tr>
                  <th scope="row">6</th>
                  <td>Protein</td>
                  <td>{d['Protein']}</td>
                </tr>
                <tr>
                  <th scope="row">7</th>
                  <td>Sodium</td>
                  <td>{d['Sodium']}</td>
                </tr>
                <tr>
                  <th scope="row">8</th>
                  <td>Sugar</td>
                  <td>{d['Sugar']}</td>
                </tr>
                
                  
              </tbody>
            </table>
            </div>
        </div>
    </div>
    
))}
</div>
)
};

export default Stats;