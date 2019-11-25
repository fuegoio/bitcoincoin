export const FrequencyUnitDefinitions: FrequencyUnitDefinition[] = [
  {
    key: 'MINUTES',
    unit: 'mn',
    label: 'Minutes(s)',
  },
  {
    key: 'HOURS',
    unit: 'h',
    label: 'Heure(s)',
  },
  {
    key: 'DAYS',
    unit: 'j',
    label: 'Jour(s)',
  },
]

export interface FrequencyUnitDefinition {
  key: string
  unit: string
  label: string
}

export interface Dosage {
  unit: string
  value: number
}

export interface Frequency {
  unit: string
  value: number
}

export interface Posology {
  dosage: Dosage
  frequency: Frequency
}
