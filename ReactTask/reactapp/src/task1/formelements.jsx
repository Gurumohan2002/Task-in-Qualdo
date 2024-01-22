import { useState } from "react";
import './style1.css';
function MyFormElements() {
    const [myCar, setMyCar] = useState("Volvo");
  
    const handleChange = (event) => {
      setMyCar(event.target.value)
    }   
    return (
        <>
      <form>
      <label htmlFor="name">Name:</label>
        <input type="text" id="name" name="name" /><br></br>

        <label htmlFor="email">Email:</label>
        <input type="email" id="email" name="email" /><br></br>

        <button type="submit">Submit</button>
        <h3>Choose Your Favourite Car:</h3>
        <select value={myCar} onChange={handleChange}>
          <option value="Ford">Ford</option>
          <option value="Volvo">Volvo</option>
          <option value="Fiat">Fiat</option>
        </select>
            
      <h3>Your favourite food</h3>
        
            {/* The first radio button is checked by default using the defaultChecked attribute */}
            <label><input type='radio' name="favourite_food" value="Pizza" defaultChecked></input>Pizza</label>
            <label><input type='radio' name="favourite_food" value="Rice"></input>Rice</label>
            <label><input type='radio' name="favourite_food" value="Roti"></input>Roti</label>
            <label><input type='radio' name="favourite_food" value="Pasta"></input>Pasta</label>
            <br/>
        </form>
        </>
    )
  }

  export default MyFormElements;