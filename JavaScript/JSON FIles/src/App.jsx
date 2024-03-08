import { useEffect, useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'
import { StatusButton } from './components/StatusButton'

function App() {
  const [services, setServices] = useState([])
  const [instances, setInstances] = useState([])
  
  useEffect(() => {
    fetch('http://localhost:8000/services')
      .then(res => res.json())
      .then((data) => {
        setServices(data.data);
        setInstances(data.data.instances);
      })
  },[])

  return (
      <table>
        <thead>
        <tr>
          <th>Port Number</th>
          <th>Port Status</th>
          <th>Service Name</th>
          <th>Service Status</th>
          <th>Number of Instances</th>
        </tr>
        </thead>

        <tbody>
          {services.map((service, index) => (
            <tr key={index}>
              <td>{service.port.number}</td>
              <td>{service.port.open ? 'Listening': 'Offline'}</td>
              <td>{service.name}</td>
              <td>
                < StatusButton
                text={service.status === 'available'? 'ONLINE' : 'OFFLINE'}
                color={service.status === 'available'? 'green' : 'red'} 
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
  )
}

export default App
