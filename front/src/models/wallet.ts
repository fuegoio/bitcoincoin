import { Currency } from '@/models/currency'

export interface Wallet {
  id: number
  user: number
  currency: Currency
  volume: number
}
