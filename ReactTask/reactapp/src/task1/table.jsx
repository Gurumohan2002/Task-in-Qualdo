import React from 'react';
import './style.css'
function MyTable() {
  return (

    <table id="center">
      <thead>
        <tr>
          <th>Name</th>
          <th>Age</th>
          <th>City</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Guru</td>
          <td>21</td>
          <td>Trichy</td>
        </tr>
        <tr>
          <td>Srini</td>
          <td>22</td>
          <td>Salem</td>
        </tr>
        <tr>
          <td>Sugumar</td>
          <td>22</td>
          <td>Salem</td>
        </tr>
      </tbody>
    </table>
  );
}
export default MyTable;
