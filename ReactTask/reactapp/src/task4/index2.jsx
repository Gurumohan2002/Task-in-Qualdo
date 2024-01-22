import React, { Component } from 'react';
import './style.css';

class ApiCall extends Component {
  constructor(props) {
    super(props);
    this.state = {
      city: '',
      weatherData: null,
    };
  }
       

  handleButtonClick = async () => {
    const { city } = this.state;
    try {
      const response = await fetch(`https://weatherapi-com.p.rapidapi.com/current.json?q=${city}`, {
        method: 'GET',
        headers: {
          'X-RapidAPI-Key': 'ea1736c136msh0f5c187e704eedbp15d852jsn9c8eb45d2ffd',
          'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com',
        },
      });

      if (!response.ok) {
        throw new Error('Failed to fetch weather data');
      }

      const data = await response.json();
      this.setState({ weatherData: data });
    } catch (error) {
      console.error('Error');
      this.setState({ weatherData: null });
    }
  };
     
     

  render() {
    const { city, weatherData } = this.state;

    return (
      <div >
        <label>
          
          <label htmlFor="city">Enter Location : </label>
        <input  type="text"  id="city" value={city} onChange={(e) => this.setState({ city: e.target.value })}
        />
        <button onClick={this.handleButtonClick}>Get Weather</button>
        {weatherData && (
        <div>
            <h3>Weather Information for {city}</h3>
            <p>Location: {weatherData.location.name}</p>
            <p>Temperature: {weatherData.current.temp_c}°C</p>
            <p>Condition: {weatherData.current.condition.text}</p> 
          </div>
        )}
        </label>

        </div>
    );
  }
}

export default ApiCall; 
