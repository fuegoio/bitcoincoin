export interface Currency {
  id: number
  rank: number
  name: string
  symbol: string
  last_value: number
  icon: string
  last_rates: number[] | undefined
}

export interface Datetime {
  str: string
  diff: string
}

export interface CurrencyRate {
  id: number
  currency: number
  datetime: Datetime
  value: number
}
