import { StrictMode } from 'react'
import ReactDOM from 'react-dom/client'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { createBrowserRouter } from 'react-router'
import { RouterProvider } from 'react-router/dom'
import Layout from './Layout'
import Home from './pages/Home'
import Workouts from './pages/Workouts'
import Exercises from './pages/Exercises'
import './index.css'

const queryClient = new QueryClient()

const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      { index: true, element: <Home /> },
      { path: 'workouts', element: <Workouts /> },
      { path: 'exercises', element: <Exercises /> },
    ],
  },
])

const root = document.getElementById('root')!

ReactDOM.createRoot(root).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  </StrictMode>,
)
