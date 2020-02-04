<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="pl-8 title">
        Portfolio
      </v-col>
    </v-row>
    <v-row>
      <v-col
        v-for="currencyWalletInfo in cryptoCurrenciesWallet"
        :key="currencyWalletInfo.id"
        lg="4"
        md="6"
        sm="12"
      >
        <WalletCurrencyCard
          :currencyWalletInfo="currencyWalletInfo"
          @updated="loadAll"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import WalletCurrencyCard from '@/components/currencies/WalletCurrencyCard'
import axios from 'axios'

export default {
  name: 'WalletContainer',
  components: { WalletCurrencyCard },
  data: function() {
    return {
      cryptoCurrenciesWallet: [],
    }
  },
  mounted() {
    this.getCurrencyData()
  },
  methods: {
    loadAll() {
      this.getCurrencyData()
    },
    getCurrencyData() {
      axios.get('http://localhost:8000/api/v1/me/wallet').then(response => {
        const wallet = []
        for (const currencyWalletInfo of response.data) {
          if (currencyWalletInfo.volume > 0) {
            wallet.push(currencyWalletInfo)
          }
        }
        this.cryptoCurrenciesWallet = wallet
      })
    },
  },
}
</script>

<style scoped></style>
