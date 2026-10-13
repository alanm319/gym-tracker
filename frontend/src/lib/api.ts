// Central place for talking to the FastAPI backend.
// Change API_BASE if your backend runs somewhere other than localhost:8000.
export const API_BASE = 'http://localhost:8000'

export interface ExerciseMetricsRow {
  start_time: string
  heaviest: number
  session_volume: number
  best_volume: number
  estimated_1rm: number
}

async function fetchJson<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`)
  if (!res.ok) {
    throw new Error(`Request to ${path} failed with status ${res.status}`)
  }
  return res.json()
}

export function getExerciseNames(): Promise<string[]> {
  return fetchJson<string[]>('/exercise-names')
}

export function getExerciseMetrics(name: string): Promise<ExerciseMetricsRow[]> {
  return fetchJson<ExerciseMetricsRow[]>(
    `/exercises/${encodeURIComponent(name)}/metrics`,
  )
}
