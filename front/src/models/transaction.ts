import { User } from '@/models/user'

export interface Transaction {
  id: number
  user: User
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
