import { useQuery } from '@tanstack/react-query'
import { LineChart } from "@tremor/react"

import './App.css'

function App() {

  const { data, isLoading, error } = useQuery({
    queryKey: ["heaviest", "Bench Press (Barbell)"],
    queryFn: () => fetch("http://localhost:8000/exercises/Bench Press (Barbell)/heaviest").then(res => res.json()),
  })

  if (isLoading) return <p>Loading...</p>
  if (error) return <p>Error</p>

  const formattedData = data.map((point: { start_time: string; value: number }) => ({
    ...point,
    start_time: new Date(point.start_time).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
    }),
  }))

  return (
    <LineChart
      className="h-80"
      data={formattedData}
      index="start_time"
      categories={["value"]}
      colors={["blue"]}
    />
  )
}

export default App
