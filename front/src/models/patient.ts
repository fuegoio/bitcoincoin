export const PatientPredicateDefinitions: PatientPredicateDefinition[] = [
  {
    category: 'Rein',
    label: 'Insuffisance rénale terminale (DFG < 15)',
    value: 'DFG < 15',
  },
  {
    category: 'Rein',
    label: 'Insuffisance rénale sévère (15 < DFG < 30)',
    value: '15 < DFG < 30',
  },
  {
    category: 'Rein',
    label: 'Insuffisance rénale modérée (30 < DFG < 60)',
    value: '30 < DFG < 60',
  },
  {
    category: 'Rein',
    label: 'Insuffisance rénale minime (60 < DFG < 90)',
    value: '60 < DFG < 90',
  },
  {
    category: 'Foie',
    label: 'En insuffisance hépatique',
    value: 'Insuffisance hépatique',
  },
  { category: 'Âge', label: 'Personne âgée ( > 75 ans)', value: '> 75 ans' },
  {
    category: 'Âge',
    label: 'Adulte (18 < âge < 75 ans)',
    value: '18 < âge < 75 ans',
  },
  {
    category: 'Âge',
    label: 'Adolescent (15 < âge < 18 ans)',
    value: '15 < âge < 18 ans',
  },
  {
    category: 'Âge',
    label: 'Enfant (4 < âge < 15 ans)',
    value: '4 < âge < 15 ans',
  },
  {
    category: 'Âge',
    label: 'Enfant bas-âge (1 < âge < 4 ans)',
    value: '1 < âge < 4 ans',
  },
  {
    category: 'Âge',
    label: 'Nourisson (3 mois < âge < 1 an)',
    value: '3 mois < âge < 1 an',
  },
  { category: 'INR', label: 'INR élevé ( INR > 5)', value: 'INR > 5' },
  { category: 'Âge', label: 'Jeune nourisson (< 3 mois)', value: '< 3 mois' },
  { category: 'Poids', label: '< 30 kg', value: 'poids < 30 kg' },
  { category: 'Poids', label: '< 50 kg', value: 'poids < 50 kg' },
  { category: 'Poids', label: '> 120 kg', value: 'poids > 120 kg' },
  {
    category: 'Kaliemie',
    label: 'Hypokaliemie (Potassium < 3,5)',
    value: 'Potassium < 3,5',
  },
  {
    category: 'Kaliemie',
    label: 'Hyperkaliemie (Potassium > 4,5)',
    value: 'Potassium > 4,5',
  },
]

export interface PatientPredicateDefinition {
  label: string
  value: string
  category: string
}
