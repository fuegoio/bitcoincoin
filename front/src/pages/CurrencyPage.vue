<template>
  <v-row>
    <v-col v-if="!loading" cols="12" class="px-4">
      <v-row>
        <v-col cols="3" class="pl-6 pt-3">
          <v-img
            :src="currency.icon"
            :alt="currency.symbol"
            class="currency-icon"
          />
          <span class="headline font-weight-bold">{{ currency.name }}</span>
          <div class="caption">
            {{ currency.symbol.toUpperCase() }}
          </div>
        </v-col>
        <v-col cols="3" class="pr-6 pt-5 text-right">
          <v-row justify="center" align="center">
            <v-icon large color="success">mdi-menu-up</v-icon>
            <span class="headline font-weight-light ml-3">
              {{ currency.last_value | toCurrency }}
            </span>
          </v-row>
        </v-col>
        <v-col cols="2" align-self="center">
          <BuyingModal :currency="currency" @finished="updateWallet" />
        </v-col>
        <v-col cols="2" align-self="center">
          <SellingModal :currency="currency" @finished="updateWallet" />
        </v-col>
        <v-col cols="2">
          <v-row justify="end" class="px-2">
            <v-btn-toggle
              v-model="interval"
              shaped
              mandatory
              @change="updateInterval"
            >
              <v-btn value="day">
                1d
              </v-btn>

              <v-btn value="hour">
                1h
              </v-btn>

              <v-btn value="minute">
                1m
              </v-btn>
            </v-btn-toggle>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
    <v-col v-if="wallet" cols="12">
      <CurrencyWallet :wallet="wallet" />
    </v-col>
    <v-col v-if="!ratesLoading" cols="12">
      <CurrencyHistoric :rates="rates" />
    </v-col>
    <v-col v-else cols="12" class="text-center pa-12">
      <v-progress-circular indeterminate />
    </v-col>
    <v-col cols="12">
      <CurrencyTransactions :transactions="transactions" />
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import axios, { AxiosResponse } from 'axios'

import { Currency, CurrencyRate } from '@/models/currency'
import { Transaction } from '@/models/transaction'

import BuyingModal from '@/components/transactions/BuyingModal.vue'
import SellingModal from '@/components/transactions/SellingModal.vue'
import CurrencyHistoric from '@/components/currencies/CurrencyHistoric.vue'
import CurrencyWallet from '@/components/currencies/CurrencyWallet.vue'
import CurrencyTransactions from '@/components/currencies/CurrencyTransactions.vue'
import { Wallet } from '@/models/wallet'

@Component({
  components: {
    CurrencyTransactions,
    CurrencyHistoric,
    BuyingModal,
    SellingModal,
    CurrencyWallet,
  },
})
export default class CurrencyPage extends Vue {
  currency: Currency = null
  rates: CurrencyRate[] = []
  transactions: Transaction[] = []
  wallet: Wallet = null
  loading = true
  ratesLoading = true
  interval = 'minute'

  async fetchCurrency(): Promise<Currency> {
    const currencyId: number = parseInt(this.$route.params.currencyId)
    const response: AxiosResponse = await axios.get('/currencies/' + currencyId)
    return response.data
  }

  async fetchCurrencyRates(interval: string): Promise<CurrencyRate[]> {
    const currencyId: number = parseInt(this.$route.params.currencyId)
    const response: AxiosResponse = await axios.get(
      '/currencies/' + currencyId + '/rates',
      { params: { interval: interval } },
    )
    return response.data
  }

  async fetchCurrencyTransactions(): Promise<Transaction[]> {
    const currencyId: number = parseInt(this.$route.params.currencyId)
    const response: AxiosResponse = await axios.get('/transactions', {
      params: { currency: currencyId },
    })
    return response.data
  }

  async fetchCurrencyWallet(): Promise<Wallet> {
    const currencyId: number = parseInt(this.$route.params.currencyId)
    const response: AxiosResponse = await axios.get('/me/wallet/' + currencyId)
    return response.data
  }

  updateInterval(interval: string): void {
    this.interval = interval
    this.ratesLoading = true
    this.fetchCurrencyRates(this.interval).then(rates => {
      this.rates = rates
      this.ratesLoading = false
    })
  }

  updateWallet(): void {
    this.fetchCurrency().then(currency => {
      this.currency = currency
      this.loading = false
    })

    this.fetchCurrencyRates(this.interval).then(rates => {
      this.rates = rates
      this.ratesLoading = false
    })

    this.fetchCurrencyTransactions().then(transactions => {
      this.transactions = transactions
    })

    this.fetchCurrencyWallet().then(wallet => {
      this.wallet = wallet
    })
  }

  created() {
    this.updateWallet()
  }
}
</script>

<style lang="scss" scoped>
.currency-icon {
  width: 42px;
  margin-top: 6px;
  margin-right: 22px;
  float: left;
}
</style>
