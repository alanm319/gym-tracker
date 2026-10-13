import { NavLink } from 'react-router'
import { Home, Dumbbell, LineChart } from 'lucide-react'
import { cn } from '../lib/utils'

const navItems = [
  { to: '/', label: 'Home', icon: Home, end: true },
  { to: '/workouts', label: 'Workouts', icon: Dumbbell, end: false },
  { to: '/exercises', label: 'Exercises', icon: LineChart, end: false },
]

export default function Sidebar() {
  return (
    <aside className="flex w-60 shrink-0 flex-col bg-sidebar text-slate-200">
      <div className="px-6 py-6">
        <h1 className="text-lg font-semibold tracking-tight text-white">
          Gym Tracker
        </h1>
      </div>

      <nav className="flex flex-col gap-1 px-3">
        {navItems.map(({ to, label, icon: Icon, end }) => (
          <NavLink
            key={to}
            to={to}
            end={end}
            className={({ isActive }) =>
              cn(
                'flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium transition-colors',
                isActive
                  ? 'bg-accent text-white'
                  : 'text-slate-300 hover:bg-sidebar-hover hover:text-white',
              )
            }
          >
            <Icon size={18} strokeWidth={2} />
            {label}
          </NavLink>
        ))}
      </nav>

    </aside>
  )
}
