export interface Transaction {
  id: number
  user: number
  currency: number
  quantity: number
  value: number
  is_sale: boolean
  datetime: Datetime
}

export interface Datetime {
  str: string
  diff: string
}
