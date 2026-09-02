import { useQuery } from '@tanstack/react-query'
import './App.css'

function App() {

  const { data, isLoading, error } = useQuery({
    queryKey: ["exercises"],
    queryFn: () => fetch("http://localhost:8000/exercises/Bench Press (Barbell)/heaviest").then(res => res.json()),
  })

  if (isLoading) return <p>Loading...</p>
  if (error) return <p>Error</p>

  return (
    <pre>
      {JSON.stringify(data, null, 2)}
    </pre>
  )
}

export default App
