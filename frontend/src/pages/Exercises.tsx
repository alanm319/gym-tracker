import { useQuery } from '@tanstack/react-query'
import { getExerciseNames } from '../lib/api'
import {
  Accordion,
  AccordionItem,
  AccordionTrigger,
  AccordionContent,
} from '../components/Accordion'
import ExerciseChart from '../components/ExerciseChart'

export default function Exercises() {
  const { data: exerciseNames, isLoading, isError } = useQuery({
    queryKey: ['exercise-names'],
    queryFn: getExerciseNames,
  })

  return (
    <div>
      <h1 className="text-2xl font-semibold text-slate-900">Exercises</h1>
      <p className="mt-2 text-sm text-slate-500">
        Expand an exercise to see how your metrics have progressed over time.
      </p>

      <div className="mt-6">
        {isLoading && (
          <p className="text-sm text-slate-400">Loading exercises…</p>
        )}

        {isError && (
          <p className="text-sm text-red-500">
            Could not reach the backend. Is it running at localhost:8000?
          </p>
        )}

        {exerciseNames && exerciseNames.length === 0 && (
          <p className="text-sm text-slate-400">No exercises found yet.</p>
        )}

        {exerciseNames && exerciseNames.length > 0 && (
          <Accordion type="single" collapsible className="flex flex-col gap-2">
            {exerciseNames.map((name) => (
              <AccordionItem key={name} value={name}>
                <AccordionTrigger>{name}</AccordionTrigger>
                <AccordionContent>
                  <ExerciseChart exerciseName={name} />
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        )}
      </div>
    </div>
  )
}
