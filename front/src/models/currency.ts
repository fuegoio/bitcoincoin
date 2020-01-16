export interface Currency {
  id: number
  rank: number
  name: string
  symbol: string
  last_value: number
  icon: string
  last_rates: number[] | undefined
}
