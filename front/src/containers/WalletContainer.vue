<template>
  <v-row>
    <v-col v-for="crypto in cryptoCurrencies" :key="crypto.id" :cols="4">
      <CurrencyCard :crypto="crypto" />
    </v-col>
  </v-row>
</template>

<script>
import CurrencyCard from '@/components/currencies/CurrencyCard'
export default {
  name: 'WalletContainer',
  components: { CurrencyCard },
  data: function() {
    return {
      cryptoCurrencies: [
        {
          name: 'Bitcoin',
          number: 30,
          currentValue: 6780.82,
        },
        {
          name: 'Ethereum',
          number: 50,
          currentValue: 135.19,
        },
        {
          name: 'CoinCoin',
          number: 100,
          currentValue: 150,
        },
        {
          name: 'Bitcoin Cash',
          number: 200,
          currentValue: 190.86,
        },
        {
          name: 'Litecoin',
          number: 100,
          currentValue: 40.68,
        },
        {
          name: 'XRP',
          number: 100,
          currentValue: 0.21,
        },
      ],
    }
  },
}
</script>

<style scoped></style>
