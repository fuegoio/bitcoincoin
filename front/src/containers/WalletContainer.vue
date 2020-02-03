<template>
  <v-row>
    <v-col
      v-for="currencyWalletInfo in cryptoCurrenciesWallet"
      :key="currencyWalletInfo.id"
      lg="4"
      md="6"
      sm="12"
    >
      <WalletCurrencyCard
        v-if="currencyWalletInfo.volume > 0"
        :currencyWalletInfo="currencyWalletInfo"
      />
    </v-col>
  </v-row>
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
    axios.get('http://localhost:8000/api/v1/me/wallet').then(response => {
      console.log(response.data)
      this.cryptoCurrenciesWallet = response.data
    })
  },
}
</script>

<style scoped></style>
