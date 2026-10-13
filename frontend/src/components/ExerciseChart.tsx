import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from 'recharts'
import { getExerciseMetrics, type ExerciseMetricsRow } from '../lib/api'
import { cn } from '../lib/utils'

type MetricKey = 'heaviest' | 'session_volume' | 'best_volume' | 'estimated_1rm'

const METRIC_TABS: { key: MetricKey; label: string; unit: string }[] = [
  { key: 'heaviest', label: 'Heaviest Weight', unit: 'lbs' },
  { key: 'session_volume', label: 'Session Volume', unit: 'lbs' },
  { key: 'best_volume', label: 'Best Set Volume', unit: 'lbs' },
  { key: 'estimated_1rm', label: 'Estimated 1RM', unit: 'lbs' },
]

function formatDate(iso: string) {
  return new Date(iso).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
  })
}

export default function ExerciseChart({ exerciseName }: { exerciseName: string }) {
  const [metric, setMetric] = useState<MetricKey>('heaviest')

  const { data, isLoading, isError } = useQuery({
    queryKey: ['exercise-metrics', exerciseName],
    queryFn: () => getExerciseMetrics(exerciseName),
  })

  if (isLoading) {
    return <p className="py-8 text-center text-sm text-slate-400">Loading chart…</p>
  }

  if (isError || !data) {
    return (
      <p className="py-8 text-center text-sm text-red-500">
        Could not load metrics for this exercise.
      </p>
    )
  }

  if (data.length === 0) {
    return (
      <p className="py-8 text-center text-sm text-slate-400">
        No logged sets found for this exercise.
      </p>
    )
  }

  const chartData = [...data]
    .sort((a, b) => a.start_time.localeCompare(b.start_time))
    .map((row: ExerciseMetricsRow) => ({
      ...row,
      label: formatDate(row.start_time),
    }))

  const activeTab = METRIC_TABS.find((t) => t.key === metric)!

  const values = chartData.map((row) => row[metric])
  const dataMin = Math.min(...values)
  const dataMax = Math.max(...values)
  const padding = Math.max((dataMax - dataMin) * 0.2, dataMax * 0.05, 1)
  const yDomain: [number, number] = [
    Math.max(0, Math.floor(dataMin - padding)),
    Math.ceil(dataMax + padding),
  ]
  return (
    <div>
      <div className="mb-4 flex flex-wrap gap-1.5">
        {METRIC_TABS.map((tab) => (
          <button
            key={tab.key}
            onClick={() => setMetric(tab.key)}
            className={cn(
              'rounded-full px-3 py-1.5 text-xs font-medium transition-colors',
              metric === tab.key
                ? 'bg-accent text-white'
                : 'bg-slate-100 text-slate-600 hover:bg-slate-200',
            )}
          >
            {tab.label}
          </button>
        ))}
      </div>

      <ResponsiveContainer width="100%" height={260}>
        <LineChart data={chartData} margin={{ top: 8, right: 16, left: 0, bottom: 0 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
          <XAxis
            dataKey="label"
            tick={{ fontSize: 12, fill: '#64748b' }}
            tickLine={false}
            axisLine={{ stroke: '#e2e8f0' }}
          />
          <YAxis
            domain={yDomain}
            tick={{ fontSize: 12, fill: '#64748b' }}
            tickLine={false}
            axisLine={false}
            width={44}
          />
          <Tooltip
            formatter={(value) => [`${Number(value).toFixed(1)} ${activeTab.unit}`, activeTab.label]}
            labelStyle={{ color: '#0f172a', fontWeight: 600 }}
            contentStyle={{
              borderRadius: 8,
              border: '1px solid #e2e8f0',
              fontSize: 12,
            }}
          />
          <Line
            type="monotone"
            dataKey={metric}
            stroke="#6366f1"
            strokeWidth={2.5}
            dot={{ r: 3, fill: '#6366f1' }}
            activeDot={{ r: 5 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
