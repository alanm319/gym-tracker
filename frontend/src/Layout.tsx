import { Outlet } from 'react-router'
import Sidebar from './components/Sidebar'

export default function Layout() {
  return (
    <div className="flex h-screen bg-slate-50">
      <Sidebar />
      <main className="flex-1 overflow-y-auto">
        <div className="mx-auto max-w-5xl px-8 py-10">
          <Outlet />
        </div>
      </main>
    </div>
  )
}
