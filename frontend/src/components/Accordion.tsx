import * as RadixAccordion from '@radix-ui/react-accordion'
import { ChevronDown } from 'lucide-react'
import type { ReactNode } from 'react'
import { cn } from '../lib/utils'

export const Accordion = RadixAccordion.Root

export function AccordionItem({
  value,
  children,
  className,
}: {
  value: string
  children: ReactNode
  className?: string
}) {
  return (
    <RadixAccordion.Item
      value={value}
      className={cn(
        'overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm',
        className,
      )}
    >
      {children}
    </RadixAccordion.Item>
  )
}

export function AccordionTrigger({ children }: { children: ReactNode }) {
  return (
    <RadixAccordion.Header>
      <RadixAccordion.Trigger
        className={cn(
          'group flex w-full items-center justify-between gap-4 px-5 py-4 text-left',
          'text-sm font-medium text-slate-800 transition-colors hover:bg-slate-50',
        )}
      >
        {children}
        <ChevronDown
          size={18}
          className="shrink-0 text-slate-400 transition-transform duration-200 group-data-[state=open]:rotate-180"
        />
      </RadixAccordion.Trigger>
    </RadixAccordion.Header>
  )
}

export function AccordionContent({ children }: { children: ReactNode }) {
  return (
    <RadixAccordion.Content
      className={cn(
        'overflow-hidden border-t border-slate-100 px-5 py-5',
        'data-[state=open]:animate-accordion-down data-[state=closed]:animate-accordion-up',
      )}
    >
      {children}
    </RadixAccordion.Content>
  )
}
