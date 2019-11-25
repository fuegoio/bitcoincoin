import { Posology } from '@/models/drugs'

export const RuleTypeDefinitions: RuleTypeDefinition[] = [
  {
    key: 'OVERDOSE',
    label: 'Surdosage',
    icon: 'mdi-chevron-triple-up',
  },
  {
    key: 'UNDERDOSE',
    label: 'Sousdosage',
    icon: 'mdi-chevron-triple-down',
  },
  {
    key: 'INTERACTION',
    label: 'Interactions',
    icon: 'mdi-arrow-collapse-all',
  },
  {
    key: 'UNTREATED_INDICATION',
    label: 'Indication non traitée',
    icon: 'mdi-close-box-multiple-outline',
  },
  {
    key: 'DRUG_WITHOUT_INDICATION',
    label: 'Medicament sans indication',
    icon: 'mdi-comment-remove-outline',
  },
  {
    key: 'ADVERSE_EVENT',
    label: 'Effet indésirable',
    icon: 'mdi-contactless-payment',
  },
  {
    key: 'INAPPROPRIATE_ROUTE',
    label: 'Voie innapropriée',
    icon: 'mdi-call-missed',
  },
]

export const RuleGravityDefinitions: RuleGravityDefinition[] = [
  {
    key: 'MINOR',
    label: 'Mineur',
  },
  {
    key: 'MEDIUM',
    label: 'Moyen',
  },
  {
    key: 'HARMFUL',
    label: 'Nuisible',
  },
  {
    key: 'MAJOR',
    label: 'Majeur',
  },
  {
    key: 'VITAL',
    label: 'Vital',
  },
]

export interface RuleTypeDefinition {
  key: string
  label: string
  icon: string
}

export interface RuleGravityDefinition {
  key: string
  label: string
}

export interface BaseRule {
  id: number
  name: string
  molecule: number
  category: string
  gravity: string
}

export interface OverdoseRule extends BaseRule {
  maxPosology: Posology
  patientPredicates: string[]
}

export interface UnderdoseRule extends BaseRule {
  minPosology: Posology
  patientPredicates: string[]
}

export type Rule = OverdoseRule | UnderdoseRule
