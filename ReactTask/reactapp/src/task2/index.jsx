import React, { useState } from 'react';
import './style.css';

function AddNumbers() {
  const [number1, setNumber1] = useState('');
  const [number2, setNumber2] = useState('');
  const [result, setResult] = useState('');

  const handleAdd = () => {
    const num1 = parseFloat(number1);
    const num2 = parseFloat(number2);

    if (isNaN(num1) || isNaN(num2)) {
      setResult('Please enter valid numbers.');
    } else {
      setResult(num1 + num2);
    }
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setResult(''); // Clear result on input change
    if (name === 'number1') {
      setNumber1(value);
    } else {
      setNumber2(value);
    }
  };

  return (
    <div>
      <form>
        <label htmlFor="number1">Number 1:</label>
        <input
          type="number"
          id="number1"
          name="number1"
          value={number1}
          onChange={handleChange}
        />
        <br />
        <label htmlFor="number2">Number 2:</label>
        <input
          type="number"
          id="number2"
          name="number2"
          value={number2}
          onChange={handleChange}
        />
        <br />
        <button type="button" onClick={handleAdd}>
          Add
        </button>
      </form>
      <p>Result: {result}</p>
    </div>
  );
}

export default AddNumbers;
