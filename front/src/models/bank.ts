export interface Bank {
  id: number
  name: string
  symbol: string
  cash_flow: number
  wallet_value: number
  membership: boolean
  memberships: any[]
  demands: any[]
}
